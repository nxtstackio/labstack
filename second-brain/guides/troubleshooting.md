# Troubleshooting and disconnect

| Symptom | What to check |
| --- | --- |
| Agent does not know the project | Open the coding project, confirm its instruction file is loaded, and ask it to read the local connection explicitly. |
| Connection is missing after cloning | `.shared-brain.local.json` is deliberately not committed. Run setup for this checkout and select your own vault. |
| Vault not found | Confirm the selected folder exists on this machine. Use an explicit reconnect after a move; do not silently create a replacement vault. |
| Access denied | Grant the session access only to the chosen notes directory. Do not disable all permission checks. |
| Skill not found | Check the agent-specific install directory, ensure SKILL.md is directly inside shared-second-brain, copy the full bundle, and start a fresh session. |
| Agent reads wrong task | Select the task linked in project.md. Newest modification time does not identify the right task. |
| Existing instructions conflict | Preserve them, identify the conflicting rule or override, and choose a narrow reconciliation. |
| Duplicate or broken managed markers | Stop setup and review the file. Do not delete everything between guessed boundaries. |
| Git still shows a private file | Ignore rules do not untrack already tracked files. Stop before writing private content and decide how to repair it. |
| Notes conflict or another agent is writing | Stop the write, preserve both versions, and choose one writer. The kit does not merge simultaneous edits. |
| Checkpoint differs from code | Check live files and test evidence; record the mismatch. Never treat an old “passed” note as a new test result. |

## Incomplete setup or failed save

Ask the agent to inspect the current files and local backup manifest, then apply only missing edits. Existing notes should remain intact. If the vault cannot be written, the agent may save a recovery note in the ignored `.shared-brain-pending/` directory, but only after verifying it is private and writable. Otherwise it must report that no save occurred.

When access returns, reconcile the pending note into the right task, read back the result, and only then decide whether to remove the recovery copy.

## Disconnect without losing notes

Ask: “Disconnect this project from Shared Brain. Preserve my notes and all unrelated instructions.”

The agent removes its marked blocks from `CLAUDE.md` and `AGENTS.md` and the local connection. It should remove an entire instruction file only when setup created it and it still contains only the unchanged managed block. Keep ignore rules while local backups or pending notes remain. The vault and task history remain yours.

## Undo a setup edit

Backups are stored locally under `.shared-brain-backups/<run-id>/` with before/after hashes and file-existence records. Restore a whole file only if its current content still matches the recorded post-setup hash. If you edited it since setup, merge out the setup-owned changes rather than restoring an old copy over your work.

Do not automatically delete a vault, clear task history, alter global agent settings or rewrite Git history as part of recovery.
