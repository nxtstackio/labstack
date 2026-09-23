# Use with Codex

## Prompt route

Open the coding project in a local Codex session and paste the [setup prompt](../brain-prompt.md). Supply the chosen vault directory when asked and review the scoped edits. No skill installation is needed.

The vault may be outside Codex's writable workspace. Add the selected notes directory through the environment's access controls; the CLI provides `--add-dir` for an additional writable directory. Keep sandboxing and approvals appropriate to your project. Hosted environments need their own authorized access; this kit does not synchronize a local vault into the cloud.

## Install the optional skill

1. Download Labstack and locate `second-brain/skill/shared-second-brain/`.
2. Copy the entire folder, including `references/` and `templates/`, into the coding project's `.agents/skills/` directory. The result should contain `.agents/skills/shared-second-brain/SKILL.md`.
3. Compare before replacing an existing skill with that name. Preserve any local modifications.
4. Start a fresh Codex session in the project. Use the skill picker or type `$shared-second-brain` and check that it is discovered.
5. Ask it to set up the project, checkpoint the current task, or resume a selected task.

Codex installations may also expose user-level skill locations. Use the location documented for your installed version if project discovery differs; do not assume a folder elsewhere is loaded automatically. Project installation is the documented route in this kit.

## Startup and handoff

The generic `AGENTS.md` block instructs Codex to read `.shared-brain.local.json` and the relevant notes. The JSON is not native Codex configuration and is not automatically loaded: the project instructions tell the agent how to use it.

Check existing `AGENTS.override.md` and more-specific project rules if startup behavior differs. Do not replace them blindly. Ask a fresh session to identify the connected project and retrieve the selected checkpoint. Complete the [handoff test](handoff-test.md), including a return to Claude Code.

Sources: [Codex skills](https://developers.openai.com/codex/skills/), [AGENTS.md](https://developers.openai.com/codex/guides/agents-md/), [security and permissions](https://developers.openai.com/codex/security/). See [our validation record](../../docs/validation.md) for actual coverage.
