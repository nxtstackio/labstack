# Shared Second Brain architecture

## Public package and private state

Labstack distributes instructions and synthetic examples, never a user's working memory. No daemon, API, database, Obsidian plugin, telemetry, or automatic transcript archive is installed.

The agent runs setup in the user's coding project, with a separately selected local vault. The project may also be the vault for a notes-only workflow. Generic blocks in project-root `CLAUDE.md` and `AGENTS.md` tell the agent to read `.shared-brain.local.json`. This JSON file is data, not executable configuration; agents explicitly read it. It is ignored by Git before it is created.

Mapping schema version 1 has exactly three fields: `schema_version` (1), `vault_path` (an absolute local directory string), and `project_slug` (lowercase letters/digits separated by hyphens). All notes live under `Shared Brain/Projects/<project_slug>/` in that vault. There is one connection per coding-project directory. Different checkouts need their own local mapping.

`Shared Brain/index.md` links projects. Each project has `project.md`, optional `decisions/` and a `tasks/<unique-task-id>/checkpoint.md` per task. The project note links active tasks explicitly; the latest filesystem modification time does not select the task. Reference folders are added only when needed.

## Agent-led installation

The root README gives one copyable request pointing to the Second Brain README. That resource README is the installation entrypoint: the agent retrieves one source checkout, copies the complete bundle to its project-local skill directory, and immediately performs setup. Prompt-only and other-agent requests use the standalone prompt. Both the skill and generated prompt require first-time guided intake about purpose, tools and Obsidian experience, with a wait for missing answers before installation or configuration. The agent handles technical choices and performs the setup; users do not choose individual files or install paths. Connected reruns reuse known choices and remain read-only when unchanged. Copying a skill, native discovery and configured memory are reported separately.

## One setup contract

The skill's `references/setup.md` and templates are canonical. `scripts/build_prompt.py` assembles the standalone copyable prompt from those files. Maintainer validation rejects drift. The standalone prompt needs no download, Python runtime, or installed skill. Python is only used to maintain this repository.

The skill routes setup to that same contract and checkpoint/resume to `references/operations.md`. Templates use the same instruction block for both tools. Tool-specific guides explain discovery and permissions rather than inventing different memory behavior.

An unchanged setup rerun is a read-only verification path. It does not refresh note timestamps, append checkpoint history or create backups. Repairs and explicit checkpoint requests are separate operations. This avoids turning routine setup checks into changes to the project history.

## Boundaries

Instructions guide an agent; they are not an access-control system. Filesystem permissions enforce access. A local vault is not a promise of local-only model processing. Only selected project notes should enter the agent's context. Saved notes, imported references, and examples never create authorization to execute commands or publish work.

V1 supports sequential handoffs. Per-task checkpoints reduce collisions but do not provide locking or sync conflict resolution. Re-read files before editing and stop on detected divergence. Failed writes must be reported and recovered; no automatic pre-compaction guarantee is made.

## Verification

See [validation](validation.md) for completed checks and unverified surfaces. Setup must preserve existing rules, be safe to rerun, exclude private local state, and prove a fresh-session handoff. A successful directory scaffold alone is not acceptance.

Obsidian discovery precedes first-time intake: inspect installed-app evidence and registered vault metadata without opening notes or scanning the home directory. Ask the user to confirm a discovered vault; do not infer absence from inaccessible or stale metadata. Missing apps trigger an offer to download from the official site, with explicit permission before downloading and authorization for installation before running an installer. The canonical setup reference supplies this behavior to both the skill and generated prompt.

Before setup writes or copying skills, the agent presents concrete project, vault and skill destinations and the selected agents for explicit confirmation. Generic setup authorization is insufficient; an existing explicit confirmation of the same scope may be reused. Changed destinations require a new confirmation; unchanged connected reruns remain read-only.

## Repository automation

GitHub Actions runs Pylint and package/prompt checks on PRs and main pushes. A separate CodeQL workflow scans Python, including a weekly run. Dependabot maintains pinned Actions and the Pylint development dependency through reviewable PRs. Workflow jobs use hosted runners, timeouts, read-only contents access, and no stored checkout credentials; only CodeQL receives security-events write access. There is no deployment or auto-merge. Owner-only security and branch-rule settings are separate from these files.
