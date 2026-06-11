# ara x em-dash style fix

The actual code change is on branch `fix/ara-x-emdash-style` in `Aradotso/ara-cua`.

All 18 em-dashes (U+2014) in the `ara x` experimental subcommands section of
AraCLI.swift were replaced with hyphens and colons across commits:
- ce18325a1 fix(ara-cli): address review-bot feedback on `ara x` namespace
- c53c4a037 (AraDesktop) harden ara x doc-comments: ASCII-only separators

Syntax verified: swiftc -parse passes cleanly.
