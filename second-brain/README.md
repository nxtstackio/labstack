# Second Brain

Shared project notes in an Obsidian vault, used by your coding agents.

## Install

Open your coding project in Claude Code, Codex or another local coding agent. Paste this:

```text
Read https://github.com/nxtstackio/labstack/blob/main/second-brain/README.md and follow its installation instructions. Check for Obsidian and existing vaults first. Ask what I want to use it for, which tools I use, and which vault I want to use. If Obsidian is missing, offer to download it and wait for my permission. Wait for my answers, then install and configure it for me. Preserve my existing files and instructions.
```

No setup knowledge is needed. The agent checks for Obsidian and existing vaults, asks what you need, and helps you choose a vault or create a notes folder. If Obsidian is missing, it offers to download it. It handles the repository files and configuration. To use only the prompt, add: **“Use the prompt only; do not install a skill.”**

## Instructions for the coding agent

When the user asks you to install or set up this resource:

1. Follow the read-only Obsidian discovery and guided intake in `second-brain/skill/shared-second-brain/references/setup.md` (retrieve the source as described below first if needed). Check the installed app and registered vault metadata before asking the user; do not scan their home directory or read their notes. Ask what they want to remember and which tools they use. Offer found vaults and ask which to use. If the app is not found, offer an official download and wait for permission; installation also needs authorization. Explain unfamiliar terms and wait for missing choices before project/vault writes. Use their selected working project or notes folder as the target, not the downloaded Labstack checkout. Do not change global agent settings.
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
