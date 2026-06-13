#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { spawnSync } from 'node:child_process';
import sharp from 'sharp';

const args = parseArgs(process.argv.slice(2));
const repoRoot = process.cwd();
const level = args.level ?? 'balanced';
const apply = Boolean(args.apply);
const minSavings = Number(args['min-savings'] ?? 20);
const changedFiles = await readChangedFiles(args['changed-files']);
const imageFiles = changedFiles
  .map((file) => file.trim())
  .filter(Boolean)
  .filter((file) => file.startsWith('profile/'))
  .filter((file) => /\.(png|jpe?g)$/i.test(file));

const presets = {
  balanced: {
    webpQuality: 82,
    avifQuality: 50,
    avifEffort: 5,
    pngQuality: '75-95',
    oxipngLevel: 3,
  },
  aggressive: {
    webpQuality: 76,
    avifQuality: 42,
    avifEffort: 8,
    pngQuality: '65-90',
    oxipngLevel: 6,
  },
};

const preset = presets[level];
if (!preset) {
  console.error(`Unknown compression level: ${level}`);
  process.exit(2);
}

const rows = [];
let generatedVariants = 0;
let optimizedOriginals = 0;

await fs.mkdir('profile', { recursive: true });

for (const relativeFile of imageFiles) {
  const absoluteFile = path.join(repoRoot, relativeFile);
  if (!(await exists(absoluteFile))) continue;

  const extension = path.extname(relativeFile).toLowerCase();
  const originalBytes = await sizeOf(absoluteFile);
  const base = relativeFile.slice(0, -extension.length);

  const webpFile = `${base}.webp`;
  const avifFile = `${base}.avif`;

  await sharp(absoluteFile)
    .webp({ quality: preset.webpQuality, effort: 6 })
    .toFile(webpFile);
  const webpRow = await measure(`${relativeFile} → ${webpFile}`, originalBytes, await sizeOf(webpFile), minSavings);
  rows.push(webpRow);
  if (webpRow.kept) generatedVariants += 1;
  else await fs.rm(webpFile, { force: true });

  await sharp(absoluteFile)
    .avif({ quality: preset.avifQuality, effort: preset.avifEffort })
    .toFile(avifFile);
  const avifRow = await measure(`${relativeFile} → ${avifFile}`, originalBytes, await sizeOf(avifFile), minSavings);
  rows.push(avifRow);
  if (avifRow.kept) generatedVariants += 1;
  else await fs.rm(avifFile, { force: true });

  if (extension === '.png') {
    const pngBefore = await fs.readFile(absoluteFile);
    const optimized = await compressPng(absoluteFile, preset);
    const optimizedBytes = await sizeOf(absoluteFile);
    const pngSavings = percentSaved(originalBytes, optimizedBytes);

    if (!optimized || pngSavings < minSavings) {
      await fs.writeFile(absoluteFile, pngBefore);
      rows.push({
        file: `${relativeFile} original`,
        before: originalBytes,
        after: optimizedBytes,
        savings: pngSavings,
        kept: false,
        note: optimized ? `below ${minSavings}% threshold` : 'pngquant/oxipng unavailable or failed',
      });
    } else {
      optimizedOriginals += 1;
      rows.push({
        file: `${relativeFile} original`,
        before: originalBytes,
        after: optimizedBytes,
        savings: pngSavings,
        kept: true,
        note: 'compressed PNG kept',
      });
    }
  }
}

const summary = renderSummary({ level, minSavings, rows, generatedVariants, optimizedOriginals });
await fs.writeFile(`profile-image-optimization-${level}.md`, summary);
console.log(summary);

function parseArgs(argv) {
  const parsed = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) continue;
    const key = arg.slice(2);
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      parsed[key] = true;
    } else {
      parsed[key] = next;
      index += 1;
    }
  }
  return parsed;
}

async function readChangedFiles(changedFilesArg) {
  if (changedFilesArg) return changedFilesArg.split(/[\n, ]+/).filter(Boolean);

  const gitDiff = spawnSync('git', ['diff', '--name-only', 'origin/main...HEAD'], {
    encoding: 'utf8',
  });
  if (gitDiff.status === 0 && gitDiff.stdout.trim()) {
    return gitDiff.stdout.split('\n');
  }

  const fallback = spawnSync('git', ['ls-files', 'profile'], { encoding: 'utf8' });
  if (fallback.status !== 0) return [];
  return fallback.stdout.split('\n');
}

async function compressPng(file, preset) {
  const pngquant = spawnSync(
    'pngquant',
    ['--force', '--skip-if-larger', '--quality', preset.pngQuality, '--ext', '.png', file],
    { stdio: 'inherit' },
  );
  if (pngquant.error || pngquant.status > 1) return false;

  const oxipng = spawnSync('oxipng', ['-o', String(preset.oxipngLevel), '--strip', 'safe', file], {
    stdio: 'inherit',
  });
  if (oxipng.error || oxipng.status !== 0) return pngquant.status === 0;
  return true;
}

async function exists(file) {
  try {
    await fs.access(file);
    return true;
  } catch {
    return false;
  }
}

async function sizeOf(file) {
  const stats = await fs.stat(file);
  return stats.size;
}

async function measure(file, before, after, minSavings) {
  const savings = percentSaved(before, after);
  return {
    file,
    before,
    after,
    savings,
    kept: savings >= minSavings,
    note: savings >= minSavings ? 'variant generated' : `below ${minSavings}% threshold`,
  };
}

function percentSaved(before, after) {
  if (!before) return 0;
  return Number((((before - after) / before) * 100).toFixed(1));
}

function formatBytes(bytes) {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
}

function renderSummary({ level, minSavings, rows, generatedVariants, optimizedOriginals }) {
  const lines = [
    `### Profile image optimization (${level})`,
    '',
    `Changed profile images: ${imageFiles.length}`,
    `Generated WebP/AVIF variants: ${generatedVariants}`,
    `Compressed PNG originals kept: ${optimizedOriginals} (threshold: >${minSavings}% savings)`,
    '',
    '| File | Before | After | Savings | Result |',
    '| --- | ---: | ---: | ---: | --- |',
  ];

  if (!rows.length) {
    lines.push('| No changed profile images | - | - | - | Nothing to optimize |');
  } else {
    for (const row of rows) {
      const result = row.kept ? row.note : `not kept: ${row.note}`;
      lines.push(
        `| ${row.file} | ${formatBytes(row.before)} | ${formatBytes(row.after)} | ${row.savings}% | ${result} |`,
      );
    }
  }

  lines.push('');
  lines.push(
    apply
      ? 'The workflow commits generated variants and PNG originals that clear the savings threshold.'
      : 'Dry run only; no commit was made by this matrix entry.',
  );
  return `${lines.join('\n')}\n`;
}
