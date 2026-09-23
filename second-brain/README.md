# Second Brain

Shared project notes in an Obsidian vault, used by your coding agents.

## Install

Open your coding project in Claude Code, Codex or another local coding agent. Paste this:

```text
Read https://github.com/nxtstackio/labstack/blob/main/second-brain/README.md and follow its installation instructions. Ask me what I want to use it for, which tools I use, and whether I already have an Obsidian vault. Wait for my answers, then install and configure it for me. Preserve my existing files and instructions.
```

No setup knowledge is needed. The agent asks what you need and helps you choose an existing Obsidian vault or create a notes folder. It handles the repository files and configuration. To use only the prompt, add: **“Use the prompt only; do not install a skill.”**

## Instructions for the coding agent

When the user asks you to install or set up this resource:

1. Begin with guided intake: ask what the user wants to remember or continue, which agents they use, and whether they already have an Obsidian vault. Explain unfamiliar terms, offer simple choices, and wait for missing answers before installing or configuring anything. Follow the detailed intake in the setup reference when retrieved; do not ask answered questions again. Use their selected working project or notes folder as the target, not the downloaded Labstack checkout. Never search their home directory for a vault. Do not install Obsidian or change global agent settings.
2. Retrieve this repository into a temporary source directory, or use an existing user-provided Labstack checkout. Source: `https://github.com/nxtstackio/labstack.git`. Use one checkout/revision for all files. If you cannot fetch it, say so and ask for a local checkout; do not claim installation succeeded. Do not run repository scripts to install this resource.
3. Use the intake answers to select project-local skill installation for the requested agent(s); recommend the current agent when the user is unsure:

   | Agent | Destination inside the user's coding project |
   | --- | --- |
   | Claude Code | `.claude/skills/shared-second-brain/` |
   | Codex | `.agents/skills/shared-second-brain/` |
   | Other agent, or prompt-only request | Skip skill installation; use `second-brain/brain-prompt.md` from the source checkout. |

   If the user explicitly requests both Claude Code and Codex, install both copies. Do not guess another agent's skill format.
4. For a skill install, copy the **entire** source directory `second-brain/skill/shared-second-brain/`, including `SKILL.md`, `references/` and `templates/`, into the destination. Compare an existing destination first: identical files need no writes; do not overwrite differing user files without resolving the difference with the user. Do not create a nested `shared-second-brain/shared-second-brain/` directory. Verify every copied file matches the source.
5. Read the installed `SKILL.md` and follow its setup reference and templates now. Do not stop after copying the skill or give the installation work back to the user. For the prompt route, read and carry out `second-brain/brain-prompt.md` now instead. Complete the required guided intake before writes. Honor existing authorization for the scoped setup; resolve missing answers or conflicts without repeating answered questions.
6. Preserve existing notes and agent instructions. The setup contract keeps the private vault mapping out of Git and handles reruns, recovery and disconnect. Respect the current tool's filesystem permissions; do not bypass them. For another agent, use its documented project-instruction mechanism to point at the same local mapping only when supported and authorized; otherwise explain the limitation rather than claim automatic startup memory works.
7. Verify the connection and read back the created notes. Report whether the skill was **copied**, **discovered by the agent**, and whether project memory was **configured and verified** as separate results. If discovery needs a fresh session, say so; you can still complete setup by reading the installed skill directly. Do not claim the other agent has been tested. Do not commit, push or publish user notes as part of installation.

## After setup

Before switching agents: **“Save a checkpoint for this task.”**

In the other agent, open the same project and ask: **“Read the shared checkpoint and continue this task.”** Grant access to the selected notes if requested. Use one writer at a time. Notes read by an agent may be processed by its model provider.

## Reference

[Setup prompt](brain-prompt.md) · [Skill source](skill/shared-second-brain/SKILL.md) · [Claude Code details](guides/claude-code.md) · [Codex details](guides/codex.md) · [Troubleshooting / disconnect](guides/troubleshooting.md) · [Tested coverage](../docs/validation.md)

[Next Stack](https://nxtstack.io) · [MIT license](../LICENSE)
