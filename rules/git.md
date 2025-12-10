## git rules

- Never run destructive git operations (`git reset --hard`, `rm`, `git checkout`/`git restore` to older commits) without explicit written permission. When in doubt, stop and ask.
- Delete obsolete files when your changes make them irrelevant; revert only your own changes or when explicitly requested.
- Never edit `.env` or environment variable files.
- Never use `git restore` on files you didn't author.
- Always check `git status` before committing.
- Keep commits atomic—only commit files you touched, listing each path explicitly:
  - Tracked files: `git commit -m "<message>" -- path/to/file1 path/to/file2`
  - New files: `git restore --staged :/ && git add "path/to/file1" && git commit -m "<message>" -- path/to/file1`
- Quote paths containing brackets, parentheses, or asterisks.

### Commit format

Use [Conventional Commits](https://www.conventionalcommits.org/) with these types:

| Type       | Purpose                                 |
| ---------- | --------------------------------------- |
| `feat`     | New features                            |
| `fix`      | Bug fixes                               |
| `docs`     | Documentation                           |
| `refactor` | Restructuring without behavior change   |
| `style`    | Formatting, whitespace                  |
| `perf`     | Performance improvements                |
| `test`     | Adding or fixing tests                  |
| `build`    | Build system, dependencies              |
| `ci`       | CI configuration                        |
| `chore`    | Maintenance, tooling                    |
| `del`      | Removing code or files _(non-standard)_ |
| `sec`      | Security improvements _(non-standard)_  |

**Format**: `type(scope): description` or `type: description`

```bash
# Simple
git commit -m "fix: resolve null pointer in auth flow"

# With scope
git commit -m "feat(api): add rate limiting endpoint"

# With body and ticket reference
git commit -m "refactor(auth): extract token validation" -m "Reduces duplication across three auth handlers.

Part of ZCO-123"
```

**Guidelines**:

- Use imperative mood ("add" not "added")
- Explain _why_, not just _what_
- Split unrelated changes into separate commits
- Reference tickets at the end, after a blank line: `Part of <ticket-id>`
- For breaking changes, add `!` after type: `feat!: remove deprecated API`
