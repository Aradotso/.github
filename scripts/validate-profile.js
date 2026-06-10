#!/usr/bin/env node
// Validates that required profile assets are present.
// Assumption: repo is a GitHub org profile (profile/ only); no app stack.

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const REQUIRED_FILES = [
  'profile/README.md',
  'profile/hero.png',
  'profile/logo.png',
];

let ok = true;

for (const rel of REQUIRED_FILES) {
  const abs = path.join(ROOT, rel);
  if (fs.existsSync(abs)) {
    console.log(`  ✓  ${rel}`);
  } else {
    console.error(`  ✗  MISSING: ${rel}`);
    ok = false;
  }
}

if (!ok) {
  console.error('\nProfile validation failed — one or more required files are missing.');
  process.exit(1);
}

console.log('\nProfile validation passed.');
