#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { execFile } from 'node:child_process';
import sharp from 'sharp';
import pngquantBin from 'pngquant-bin';
import oxipngBin from 'oxipng-bin';

const IMAGE_RE = /^profile\/.*\.(png|jpe?g)$/i;

function parseArgs(argv) {
  const args = {
    apply: false,
    level: 'balanced',
    webpQuality: 82,
    avifQuality: 52,
    pngquantQuality: '65-90',
    oxipngLevel: 3,
    threshold: 20,
    report: 'profile-image-optimization.md',
    files: []
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--apply') args.apply = true;
    else if (arg === '--level') args.level = argv[++i];
    else if (arg === '--webp-quality') args.webpQuality = Number(argv[++i]);
    else if (arg === '--avif-quality') args.avifQuality = Number(argv[++i]);
    else if (arg === '--pngquant-quality') args.pngquantQuality = argv[++i];
    else if (arg === '--oxipng-level') args.oxipngLevel = Number(argv[++i]);
    else if (arg === '--threshold') args.threshold = Number(argv[++i]);
    else if (arg === '--report') args.report = argv[++i];
    else if (arg === '--files') args.files.push(...argv[++i].split(',').map((item) => item.trim()).filter(Boolean));
    else if (!arg.startsWith('--')) args.files.push(arg);
    else throw new Error(`Unknown argument: ${arg}`);
  }

  return args;
}

function run(bin, args) {
  return new Promise((resolve, reject) => {
    const child = execFile(bin, args, { encoding: 'buffer' }, (error, stdout, stderr) => {
      if (error) {
        error.stdout = stdout?.toString() || '';
        error.stderr = stderr?.toString() || '';
        reject(error);
        return;
      }
      resolve({ stdout: stdout?.toString() || '', stderr: stderr?.toString() || '' });
    });
    child.on('error', reject);
  });
}

async function exists(file) {
  try {
    await fs.access(file);
    return true;
  } catch {
    return false;
  }
}

async function bytes(file) {
  const stat = await fs.stat(file);
  return stat.size;
}

function formatBytes(value) {
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`;
  return `${(value / 1024 / 1024).toFixed(2)} MB`;
}

function savingsPercent(before, after) {
  if (!before) return 0;
  return ((before - after) / before) * 100;
}

function isProfileImage(file) {
  return IMAGE_RE.test(file) && !file.endsWith('.webp') && !file.endsWith('.avif');
}

async function changedProfileImagesFromGit() {
  const base = process.env.GITHUB_BASE_REF ? `origin/${process.env.GITHUB_BASE_REF}` : 'origin/main';
  try {
    const { stdout } = await run('git', ['diff', '--name-only', '--diff-filter=ACMR', `${base}...HEAD`, '--', 'profile/**/*.png', 'profile/**/*.jpg', 'profile/**/*.jpeg']);
    return stdout.split('\n').map((line) => line.trim()).filter(Boolean);
  } catch {
    const { stdout } = await run('git', ['ls-files', 'profile']);
    return stdout.split('\n').map((line) => line.trim()).filter(Boolean);
  }
}

async function inputFiles(args) {
  const fromEnv = process.env.PROFILE_IMAGE_FILES
    ? JSON.parse(process.env.PROFILE_IMAGE_FILES)
    : [];
  const files = args.files.length ? args.files : (fromEnv.length ? fromEnv : await changedProfileImagesFromGit());
  const unique = [...new Set(files.map((file) => file.replace(/^\.\//, '')).filter(isProfileImage))];
  const existing = [];
  for (const file of unique) {
    if (await exists(file)) existing.push(file);
  }
  return existing;
}

async function writeVariant(source, output, format, quality, sourceBytes, threshold, apply) {
  const tmp = `${output}.tmp`;
  await sharp(source).toFormat(format, { quality, effort: format === 'avif' ? 6 : 5 }).toFile(tmp);
  const outputBytes = await bytes(tmp);
  const saved = savingsPercent(sourceBytes, outputBytes);
  if (saved >= threshold) {
    if (apply) await fs.rename(tmp, output);
    else await fs.rm(tmp, { force: true });
    return { file: output, before: sourceBytes, after: outputBytes, saved, action: apply ? 'written' : 'would write' };
  }
  await fs.rm(tmp, { force: true });
  if (apply) await fs.rm(output, { force: true });
  return { file: output, before: sourceBytes, after: outputBytes, saved, action: 'skipped below threshold' };
}

async function compressPng(source, sourceBytes, args) {
  const quantized = `${source}.pngquant.tmp`;
  const optimized = `${source}.oxipng.tmp`;
  await fs.copyFile(source, optimized);

  try {
    await run(pngquantBin, ['--force', '--skip-if-larger', '--quality', args.pngquantQuality, '--output', quantized, source]);
    if (await exists(quantized)) await fs.rename(quantized, optimized);
  } catch (error) {
    const stderr = String(error.stderr || '');
    const toleratedPngquantExit = error.code === 98 || stderr.includes('Not writing output');
    if (!toleratedPngquantExit) throw error;
  }

  await run(oxipngBin, [`-o${args.oxipngLevel}`, '--strip', 'safe', '--quiet', optimized]);
  const outputBytes = await bytes(optimized);
  const saved = savingsPercent(sourceBytes, outputBytes);
  if (saved >= args.threshold) {
    if (args.apply) await fs.rename(optimized, source);
    else await fs.rm(optimized, { force: true });
    return { file: source, before: sourceBytes, after: outputBytes, saved, action: args.apply ? 'rewritten' : 'would rewrite' };
  }

  await fs.rm(optimized, { force: true });
  await fs.rm(quantized, { force: true });
  return { file: source, before: sourceBytes, after: outputBytes, saved, action: 'kept original below threshold' };
}

function reportLine(result) {
  const prefix = result.saved >= 0 ? `${result.saved.toFixed(1)}% smaller` : `${Math.abs(result.saved).toFixed(1)}% larger`;
  return `| \`${result.file}\` | ${formatBytes(result.before)} | ${formatBytes(result.after)} | ${prefix} | ${result.action} |`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const files = await inputFiles(args);
  const results = [];

  for (const file of files) {
    const originalBytes = await bytes(file);
    const ext = path.extname(file).toLowerCase();
    const base = file.slice(0, -ext.length);

    results.push(await writeVariant(file, `${base}.webp`, 'webp', args.webpQuality, originalBytes, args.threshold, args.apply));
    results.push(await writeVariant(file, `${base}.avif`, 'avif', args.avifQuality, originalBytes, args.threshold, args.apply));

    if (ext === '.png') {
      results.push(await compressPng(file, originalBytes, args));
    }
  }

  const mode = args.apply ? 'apply' : 'report-only';
  const lines = [
    `### Profile image optimization (${args.level}, ${mode})`,
    '',
    files.length ? `Processed ${files.length} changed profile image${files.length === 1 ? '' : 's'} with a ${args.threshold}% savings threshold.` : 'No changed profile images were found.',
    '',
    '| File | Before | After | Change | Action |',
    '| --- | ---: | ---: | ---: | --- |',
    ...results.map(reportLine),
    ''
  ];

  await fs.writeFile(args.report, lines.join('\n'));
  console.log(lines.join('\n'));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
