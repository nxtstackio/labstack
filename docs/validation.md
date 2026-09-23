# Validation record

Date: 2026-09-23. Test platform: Windows. This is an instruction-driven starter kit, not an installer or a guaranteed memory service.

## Package checks

| Check | Result |
| --- | --- |
| Standalone prompt matches canonical setup reference and templates | Passed: `python scripts/build_prompt.py --check` |
| Local Markdown links, bundled templates, matching agent instructions and skill metadata | Passed: `python scripts/validate.py` |
| Skill-creator metadata validator | Passed |
| Git whitespace check | Passed |
| Public-file review for private identifiers, home-directory paths and credential patterns | Passed for the reviewed source set; separate from the package validator |
| Signed commit identity | Next Stack, brand email, locally verified SSH signature |
| Independent source review | No actionable defects found |

Package checks do not prove runtime behavior or certify that arbitrary user notes contain no sensitive data.

## Actual agent sessions

Claude Code **2.1.265** ran in new, nonpersistent CLI sessions against separate disposable project/vault folders with spaces in their names. Each fixture began with existing instruction text. Only synthetic data was used.

| Exercise | Standalone prompt | Installed skill |
| --- | --- | --- |
| Claude performs setup | Passed | Passed using bundled references/templates |
| Original instruction bytes preserved; one managed block per file | Passed | Passed |
| Local schema valid, private paths absent from instruction blocks | Passed | Passed |
| Connection/backups/pending paths ignored by Git | Passed | Passed |
| Backups present and note placeholders resolved | Passed | Passed |
| Fresh Claude records task state, constraint and a private-to-the-test receipt word | Passed | Passed |
| Fresh-context Codex app subagent retrieves saved state and receipt, then records synthetic progress | Passed | Passed; installed skill read |
| Fresh Claude retrieves Codex update, receipt, constraint and tests-NOT-RUN status | Passed | Passed |
| Unchanged setup rerun preserves existing state | Passed: all 9 compared project/note files byte-identical | Passed: all 29 compared project/note/skill files byte-identical |

The handoff supplied no prior conversation or receipt word to the receiving agent. Each route used a different receipt. Both receivers distinguished fictional progress from real code/test evidence. This verifies a **Claude CLI -> Codex app subagent -> Claude CLI** sequence; it is not evidence of a successful standalone Codex CLI write session.

Codex CLI **0.153.4** passed a no-tool smoke test and reported the project-installed skill in its available metadata. Its attempted filesystem inspection was rejected by the local tool policy; it reported read-only access and changed nothing. We did not relax that policy. Standalone Codex CLI setup, file access and handoff remain **unverified in this environment**. Interactive skill-picker UI behavior was not exercised.

A seed session without a clock tool used nominal timestamps. The instructions were corrected to require actual clock time or explicitly unknown time with a collision-resistant ID. Historical fixture entries were preserved and their discrepancy recorded. The correction passed source review and prompt-parity checks; a separate clock-denial runtime exercise has not been claimed.

Initial actual reruns appended verification metadata to existing notes. Setup was corrected to make an unchanged rerun read-only, including no timestamp/checkpoint/manifest changes. The final rerun result above refers to the corrected contract, not the initial behavior.

## Additional behavioral fixtures

A separate Codex subagent followed the skill in disposable folders and checked:

- Existing CRLF/LF instruction content preserved byte-for-byte.
- Repeat setup leaves existing files unchanged and creates no duplicate setup task.
- Private mapping, backups and pending notes are ignored and untracked.
- Backup before/after hashes and generated wikilinks resolve correctly.
- Missing selected vault causes no directory creation or file writes.
- Ambiguous tasks require selection without changing either checkpoint.
- Later edits cause after-hash mismatch; whole-file rollback is refused.
- Disconnect removes only managed blocks and the connection, preserving original/later rules, all vault notes, backups and ignore rules.

These exercise an agent's execution of documented instructions, not a shipped deterministic installer. They are distinct from the fresh-session handoff tests above.

## Coverage limits

macOS/Linux, hosted Codex, multi-computer synchronization, an already-tracked vault, actual write-permission denial, interrupted/crash recovery and simultaneous writers were not runtime-tested. V1 supports sequential handoffs only. Do not claim automatic saves before compaction or interruption.

No user vault was installed or migrated, and no private fixture logs are distributed. Nothing was pushed or published during validation. Before a release, repeat the [acceptance exercise](../second-brain/guides/handoff-test.md) on any additional environment you intend to claim as tested.

## Guided onboarding revision

The README now delegates installation to the agent. The skill setup contract and generated standalone prompt require a first-time conversation about purpose, tools and Obsidian experience before writes. Package validation, generated-prompt parity and whitespace checks passed for this revision. The revised intake and README-led download/install sequence have not been retested in a fresh agent session; earlier runtime results elsewhere in this document cover the previous setup entry flow.
