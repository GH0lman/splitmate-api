# Contributing to Splitmate API

This project follows standard professional development conventions. The guidelines below exist to keep the codebase consistent and the git history readable.


## Branching Strategy

All work happens on feature branches cut from `develop`. Direct commits to `develop` or `main` are not permitted.

### Branch naming convention:
- `feature/short-description` > New functionality
- `fix/short-description` > Bug fixes
- `chore/short-description` > Maintenance, dependencies, config
- `docs/short-description` > Documentation only

### Examples:
- `feature/jwt-authentication`
- `fix/token-refresh-expiry`
- `chore/update-dependencies`
- `docs/api-endpoint-reference`


## Commit Message Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/).

Format: `<type>[optional scope]: <description>`

### Types:
- `feat` > A new feature
- `fix` > A bug fix
- `docs` > Documentation changes
- `test` > Adding or updating tests
- `chore` > Maintenance, config, dependencies
- `refactor` > Code change that is neither a fix nor a feature

### Examples:
- `feat(auth): add JWT token generation with expiry`
- `fix(tenants): prevent cross-tenant data access in expense query`
- `test(auth): add tests for token refresh flow`
- `chore(deps): pin fastapi to 0.111.0`

### Rules:
- Use present tense - "add feature" not "added feature"
- Keep the subject line under 72 characters
- Do not end the subject line with a period
- If the commit needs more explanation, add a blank line after the subject and write a body explaining the why, not the what

## Pull Requests

- Every branch must be merged via a pull request — no direct merges
- PR title should follow the same convention as commit messages
- PR description must explain what changed and why
- Reference the related issue using `Closes #N` or `Part of #N`
- Review your own PR before merging — check the diff, leave comments on anything non-obvious

## Code Style

- Python code follows [PEP 8](https://pep8.org/)
- Formatting is handled by `black` (line length 88)
- Import sorting is handled by `isort`
- These will be enforced via pre-commit hooks (see setup instructions in the README)

## Environment Setup

Never commit `.env`. Use `.env.example` as the template and create
your own local `.env` file. See the README for full setup instructions.

## Questions

This is a solo portfolio project. If you have found it and have questions or suggestions, feel free to open an issue.