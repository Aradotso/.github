#!/usr/bin/env node
import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, renameSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { dirname, extname, relative } from 'node:path';
import process from 'node:process';
import sharp from 'sharp';

const MIN_SAVINGS_PERCENT = Number(process.env.MIN_SAVINGS_PERCENT || 20);
const PNGQUANT_QUALITY = process.env.PNGQUANT_QUALITY || '70-95';
const OXIPNG_EFFORT = process.env.OXIPNG_EFFORT || '4';
const WEBP_QUALITY = Number(process.env.WEBP_QUALITY || 82);
const AVIF_QUALITY = Number(process.env.AVIF_QUALITY || 55);
const REPORT_PATH = process.env.REPORT_PATH || 'profile-image-optimization.md';
const SUMMARY_JSON_PATH = process.env.SUMMARY_JSON_PATH || 'profile-image-optimization.json';
const CHANGED_IMAGES = process.env.CHANGED_IMAGES || '';

const supportedInputs = new Set(['.png', '.jpg', '.jpeg', '.webp', '.avif']);
const rasterInputs = parseChangedImages(CHANGED_IMAGES).filter((file) => supportedInputs.has(extname(file).toLowerCase()));
const results = [];

for (const file of rasterInputs) {
  if (!existsSync(file)) {
    results.push({ file, skipped: true, reason: 'missing after change detection' });
    continue;
  }

  const extension = extname(file).toLowerCase();
  const originalBytes = sizeOf(file);
  const entry = {
    file,
    originalBytes,
    optimizedBytes: originalBytes,
    originalSavedBytes: 0,
    originalSavedPercent: 0,
    originalCommitted: false,
    variants: [],
  };

  if (extension === '.png') {
    const optimized = await optimizePng(file, originalBytes);
    Object.assign(entry, optimized);
  }

  const [webp, avif] = await Promise.all([
    writeVariant(file, 'webp', originalBytes),
    writeVariant(file, 'avif', originalBytes),
  ]);
  entry.variants.push(webp, avif);

  results.push(entry);
}

writeReport(results);

function parseChangedImages(value) {
  return [...new Set(value.split(/\r?\n|\s+/).map((item) => item.trim()).filter(Boolean))]
    .filter((file) => file.startsWith('profile/'));
}

async function optimizePng(file, originalBytes) {
  const lossyCandidate = `${file}.pngquant.tmp`;
  const losslessCandidate = `${file}.oxipng.tmp`;
  const candidates = [];

  copy(file, lossyCandidate);
  try {
    execFileSync('pngquant', ['--force', '--skip-if-larger', `--quality=${PNGQUANT_QUALITY}`, '--output', lossyCandidate, file], { stdio: 'pipe' });
    if (existsSync(lossyCandidate)) candidates.push({ path: lossyCandidate, tool: `pngquant ${PNGQUANT_QUALITY}`, bytes: sizeOf(lossyCandidate) });
  } catch (error) {
    safeRemove(lossyCandidate);
  }

  copy(file, losslessCandidate);
  try {
    execFileSync('oxipng', ['--quiet', '--opt', 'max', '--strip', 'safe', '--alpha', `--zc=${OXIPNG_EFFORT}`, losslessCandidate], { stdio: 'pipe' });
    candidates.push({ path: losslessCandidate, tool: `oxipng effort ${OXIPNG_EFFORT}`, bytes: sizeOf(losslessCandidate) });
  } catch (error) {
    safeRemove(losslessCandidate);
  }

  const best = candidates.sort((a, b) => a.bytes - b.bytes)[0];
  const savings = best ? savingsPercent(originalBytes, best.bytes) : 0;
  const committed = Boolean(best && savings > MIN_SAVINGS_PERCENT);

  if (committed) {
    renameSync(best.path, file);
  }

  for (const candidate of candidates) {
    if (!committed || candidate.path !== best.path) safeRemove(candidate.path);
  }

  return {
    optimizedBytes: committed ? sizeOf(file) : originalBytes,
    originalSavedBytes: committed ? originalBytes - sizeOf(file) : 0,
    originalSavedPercent: committed ? savingsPercent(originalBytes, sizeOf(file)) : 0,
    originalCommitted: committed,
    originalTool: best?.tool || null,
  };
}

async function writeVariant(file, format, originalBytes) {
  const output = replaceExtension(file, `.${format}`);
  const tmp = `${output}.tmp`;
  mkdirSync(dirname(output), { recursive: true });

  const pipeline = sharp(file, { animated: true });
  if (format === 'webp') {
    await pipeline.webp({ quality: WEBP_QUALITY, effort: Math.min(Number(OXIPNG_EFFORT), 6) }).toFile(tmp);
  } else if (format === 'avif') {
    await pipeline.avif({ quality: AVIF_QUALITY, effort: Math.min(Number(OXIPNG_EFFORT), 9) }).toFile(tmp);
  }

  const variantBytes = sizeOf(tmp);
  const existingBytes = existsSync(output) ? sizeOf(output) : Infinity;
  const savings = savingsPercent(originalBytes, variantBytes);
  const committed = savings > MIN_SAVINGS_PERCENT && variantBytes < existingBytes;

  if (committed) {
    renameSync(tmp, output);
  } else {
    safeRemove(tmp);
  }

  return {
    file: output,
    format,
    bytes: committed ? variantBytes : (Number.isFinite(existingBytes) ? existingBytes : variantBytes),
    savedBytes: Math.max(0, originalBytes - (committed ? variantBytes : (Number.isFinite(existingBytes) ? existingBytes : variantBytes))),
    savedPercent: committed ? savings : (Number.isFinite(existingBytes) ? savingsPercent(originalBytes, existingBytes) : savings),
    committed,
    reason: committed ? 'smaller than existing output' : (Number.isFinite(existingBytes) && existingBytes <= variantBytes ? 'kept smaller existing output' : 'below threshold'),
  };
}

function writeReport(items) {
  const lines = ['## Profile image optimization', ''];

  if (items.length === 0) {
    lines.push('No changed profile images were detected.');
  } else {
    lines.push(`Only optimized originals and variants with more than ${MIN_SAVINGS_PERCENT}% savings are written back.`);
    lines.push('');
    lines.push('| File | Output | Before | After | Savings | Result |');
    lines.push('| --- | --- | ---: | ---: | ---: | --- |');

    for (const item of items) {
      if (item.skipped) {
        lines.push(`| ${item.file} | original | n/a | n/a | n/a | skipped: ${item.reason} |`);
        continue;
      }

      const originalResult = item.originalCommitted ? `committed ${item.originalTool || ''}`.trim() : 'kept original';
      lines.push(`| ${item.file} | original | ${formatBytes(item.originalBytes)} | ${formatBytes(item.optimizedBytes)} | ${formatPercent(item.originalSavedPercent)} | ${originalResult} |`);

      for (const variant of item.variants) {
        lines.push(`| ${item.file} | ${variant.format} | ${formatBytes(item.originalBytes)} | ${formatBytes(variant.bytes)} | ${formatPercent(variant.savedPercent)} | ${variant.committed ? `committed ${variant.file}` : 'below threshold'} |`);
      }
    }
  }

  writeFileSync(REPORT_PATH, `${lines.join('\n')}\n`);
  writeFileSync(SUMMARY_JSON_PATH, `${JSON.stringify({ minSavingsPercent: MIN_SAVINGS_PERCENT, results: items }, null, 2)}\n`);
  console.log(readFileSync(REPORT_PATH, 'utf8'));
}

function replaceExtension(file, replacement) {
  return file.slice(0, -extname(file).length) + replacement;
}

function savingsPercent(before, after) {
  if (!before) return 0;
  return ((before - after) / before) * 100;
}

function formatPercent(value) {
  return `${value.toFixed(1)}%`;
}

function formatBytes(bytes) {
  if (!Number.isFinite(bytes)) return 'n/a';
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
}

function sizeOf(file) {
  return statSync(file).size;
}

function copy(from, to) {
  writeFileSync(to, readFileSync(from));
}

function safeRemove(file) {
  if (existsSync(file)) rmSync(file, { force: true });
}
