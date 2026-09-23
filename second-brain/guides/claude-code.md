# Use with Claude Code

## Prompt route

Open the coding-project directory in Claude Code and paste the [setup prompt](../brain-prompt.md). Supply the vault directory when asked. Review the scoped edits. The prompt works without installing a skill.

Claude must have access to the chosen project and vault notes. If access is denied, grant only the needed directory using your session's permission controls. The CLI provides `--add-dir` for additional directories. Do not disable all permission checks to make setup work.

## Install the optional skill

1. Download Labstack and locate `second-brain/skill/shared-second-brain/`.
2. Copy that entire folder, including `references/` and `templates/`, into your project's `.claude/skills/` directory. The result must contain `.claude/skills/shared-second-brain/SKILL.md`.
3. If that destination exists, compare versions before replacing it. Do not nest the folder twice or discard local modifications.
4. Start a fresh Claude Code session in that project. Type `/shared-second-brain` and confirm the skill appears.
5. Invoke `/shared-second-brain` followed by `Set up this project with my Obsidian vault`, `Write a checkpoint for this task`, or `Resume the selected task`.

Project installation limits the skill to that project. Personal installation under `$HOME/.claude/skills/` is optional if you want it across projects; keep project connections separate. Do not copy your configured local mapping into the installed skill.

## Startup and handoff

The setup merges a bounded block into `CLAUDE.md` and `AGENTS.md`. Claude Code documentation also describes `AGENTS.md` support; behavior depends on configuration/version. The two aligned blocks provide compatibility without separate memory systems. If both load, perform each memory operation once. Existing instructions and overrides must be inspected rather than removed.

Run `/context` to check loaded memory files, then ask Claude to identify the connected project and current task from the notes. Merely seeing a file in the folder does not prove that the agent loaded it. Finish with the [fresh-session handoff test](handoff-test.md).

Sources: [Claude Code skills](https://code.claude.com/docs/en/skills), [memory and instruction discovery](https://code.claude.com/docs/en/memory), [data usage](https://code.claude.com/docs/en/data-usage). See [our validation record](../../docs/validation.md) for what was actually tested.
