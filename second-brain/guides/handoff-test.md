# Prove the handoff

Use a disposable coding project and a separate disposable Obsidian vault. Do not use private notes. Repeat this exercise once with the copy-only prompt and once with the installed skill. Allow only these test directories. Start a new session for every agent step; never resume the previous conversation or paste its answer into the next agent.

1. **Setup:** Have an agent apply the selected setup route. Seed the project with an existing instruction such as “Preserve the public checkout API.” Verify it remains unchanged outside the managed block. For the skill route, verify discovery in both agents' skill lists before invoking it.
2. **Claude:** Ask Claude to create a fictional checkout task, record “Stripe migration drafted; integration tests not run,” the API constraint, and “inspect PayPal adapter next.” Tell it to pick and save a unique harmless receipt word in the note and report it. Keep that word out of subsequent prompts.
3. **Fresh Codex:** Ask only: “Resume the checkout task from shared memory. Report the receipt word, current state, constraint and next step. Then record that the fictional PayPal adapter was inspected; integration tests remain not run; documentation is next.” Check its retrieved answer against the saved note. It must not claim real code/tests ran.
4. **Fresh Claude:** Ask only: “Read the current checkout checkpoint. What changed and what remains?” Confirm it sees Codex's update without the earlier chat.
5. **Repeat setup:** Run setup again without changing choices. Ensure existing note bytes, unrelated rules and links are preserved; no duplicate managed blocks or setup tasks.
6. **Failure checks:** Try a missing selected vault, unavailable write access, and two candidate tasks. The agent should report missing access/save failure or request task selection rather than fabricate state. Seed a stale test claim and verify resume checks evidence rather than repeating it as current fact.
7. **Privacy:** Check Git tracking and ignore rules. Local mapping, backups, pending notes and private vault notes must not enter a public diff. Review the managed blocks for machine-specific paths.

Record tool versions, OS, route, actual file changes, and observed results. Mark missing runtime access as **not tested**. This is a sequential-handoff test, not a proof of concurrent-writer safety or an automatic-compaction hook.
