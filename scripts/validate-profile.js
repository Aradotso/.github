#!/usr/bin/env node
// Validates that required profile assets are present.

const fs = require('fs');
const path = require('path');

const REQUIRED_FILES = [
  'profile/README.md',
  'profile/hero.png',
  'profile/logo.png',
];

let failed = false;

for (const file of REQUIRED_FILES) {
  const fullPath = path.join(__dirname, '..', file);
  if (!fs.existsSync(fullPath)) {
    console.error(`Missing required file: ${file}`);
    failed = true;
  } else {
    console.log(`OK: ${file}`);
  }
}

if (failed) {
  process.exit(1);
}

console.log('All required profile assets present.');
