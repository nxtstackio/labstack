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

## Automated checks

Install maintainer tools in a virtual environment with `python -m pip install -r requirements-dev.txt`, then run `python -m pylint scripts`. Pylint checks errors and warnings; convention and refactoring suggestions are excluded. CI also runs the package validator and generated-prompt check on Python 3.10 and 3.13 for every pull request and main-branch push. There are no path filters because Markdown changes can break package links or prompt parity.

CodeQL scans Python on pull requests, main pushes and weekly. Dependabot proposes weekly updates for GitHub Actions and Python maintainer dependencies; review and merge them explicitly. Actions use pinned commits, minimal permissions and no personal credentials. No workflow deploys or publishes user notes.

Review failures in the Actions tab and security findings in Security and quality. Repository-owner settings such as secret-scanning alerts, push protection, Dependabot vulnerability alerts and required status checks must be verified separately; a workflow file does not enable those settings. See [GitHub secret protection setup](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enable-secret-scanning). Scanners do not detect every secret or personal detail, so retain manual privacy review.
