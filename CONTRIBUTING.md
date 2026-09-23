# Contributing

Keep resources self-contained, useful without private context, and branded as Next Stack. Use fictional examples, relative paths and generic placeholders. Never contribute your local connection, vault notes, logs, tokens or private project history. Review both file contents and commit metadata before publishing.

## Maintaining Shared Second Brain

Edit the skill's `references/setup.md` and `templates/`, then regenerate the standalone prompt:

```sh
python scripts/build_prompt.py
python scripts/build_prompt.py --check
python scripts/validate.py
```

Python 3.10+ is needed only for these maintainer checks. Both instruction templates must retain equivalent behavior. Keep the skill bundle usable when copied on its own.

Changes to setup, discovery or permissions require the [handoff exercise](second-brain/guides/handoff-test.md). Update [architecture](docs/architecture.md) when implementation decisions change and [validation](docs/validation.md) with real results. Never replace an untested case with a claimed pass.

Propose narrow changes with the problem, result, and relevant verification. Do not add empty resource categories, new services or dependencies without a concrete need.
