# Example: Checkout refactor

**Fictional teaching example.** These notes are not a report of work or tests performed by this repository.

## Goal

Move payment providers behind a shared interface while keeping the public checkout API unchanged.

## Current state

Read [the checkpoint after Claude](checkpoint-after-claude.md), then [the checkpoint after Codex](checkpoint-after-codex.md). They illustrate state moving through files rather than copied conversation history.

## Constraints

Preserve the public checkout API and existing retry behavior. No live payments or deployment are authorized.

## Decisions

Migrate one adapter at a time so behavior is easier to compare. Keep retry handling at its existing boundary.

## Active task

Complete the fictional provider refactor, then validate it and update documentation.

## Known issues

Integration tests have not run. Do not infer success from the completed implementation steps.
