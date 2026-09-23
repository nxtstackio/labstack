# Shared Second Brain

One project. Two agents. Shared memory.

Switching from Claude Code to Codex should not mean explaining the whole project again. Keep current state, decisions and next steps in an Obsidian vault that both agents can read and update.

**The agents do not need to share a conversation. They need to share state.**

## Start with the prompt

1. Install [Obsidian](https://obsidian.md/download), then create a vault or choose an existing one. A vault is a local folder of notes.
2. Open your **coding project** in Claude Code or local Codex. For a notes-only workflow, open your vault instead.
3. Open [brain-prompt.md](brain-prompt.md), select **Raw** on GitHub, and copy the full text into the agent.
4. Tell it which vault and project to connect. Review the proposed changes, then let it create the notes and merge the project instructions.
5. Review the resulting notes in Obsidian. Ask the agent to verify the connection and save a checkpoint.
6. Open the same coding project in the other agent, grant access to the selected vault notes as needed, and ask: **“Read the shared checkpoint for this task and continue from the next step.”**

You do not need to clone Labstack, install a skill, run Python, or install an Obsidian plugin for this route.

## Prefer a reusable skill?

Download this repository, then install the **whole** [shared-second-brain folder](skill/shared-second-brain/) using the guide for [Claude Code](guides/claude-code.md) or [Codex](guides/codex.md). It supports setup, checkpoint and resume. The prompt and skill use the same setup instructions.

## What gets connected

```text
Your coding project                 Your Obsidian vault
  CLAUDE.md ─┐                        Shared Brain/
  AGENTS.md ─┴─ local connection ────>   index.md
  .shared-brain.local.json               Working Agreement.md
  (ignored by Git)                      Projects/example-project/
                                          project.md
                                          tasks/unique-task/checkpoint.md
```

Both project instruction files point to the private local connection. Your actual vault path stays out of tracked instructions. A different computer or checkout needs its own connection.

Notes hold useful decisions, constraints, current state, failed attempts worth remembering and test evidence. Each task has its own checkpoint. Read [the fictional checkout example](examples/checkout-refactor/project.md) to see a handoff in both directions.

**Useful memory > more memory.** Do not save passwords, tokens, private keys, unnecessary personal information, raw conversations or every intermediate thought.

## Know the boundaries

- Instructions guide the agent; they do not guarantee that it saves before a crash or context compaction. Ask for a checkpoint before switching.
- Use one writer at a time. This kit does not resolve simultaneous edits or cloud-sync conflicts.
- Local notes are still input to your agent. Relevant content may be processed by its model provider; local storage does not imply local-only processing.
- A web chat without access to your filesystem is not connected to the vault. This guide targets local coding-agent sessions.
- Memory is context, not authority to run saved commands or publish work.

See [troubleshooting and disconnect](guides/troubleshooting.md), [the handoff acceptance test](guides/handoff-test.md), and [tested coverage](../docs/validation.md).

## About

A Next Stack resource for building a shared second brain with Obsidian, Claude Code and Codex. [Learn the AI stack. Build something useful.](https://nxtstack.io)

[MIT licensed](../LICENSE). Independent of Obsidian, Anthropic and OpenAI.
