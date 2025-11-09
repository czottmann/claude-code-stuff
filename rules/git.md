## git rules

- Absolutely never run destructive git operations (e.g., `git reset --hard`, `rm`, `git checkout`/`git restore` to an older commit) unless the user gives an explicit, written instruction in this conversation. Treat these commands as catastrophic; if you are even slightly unsure, stop and ask before touching them.
- Delete unused or obsolete files when your changes make them irrelevant (refactors, feature removals, etc.), and revert files only when the change is yours or explicitly requested.
- NEVER edit `.env` or any environment variable files—only the user may change them.
- Moving/renaming and restoring files is allowed.
- Never use `git restore` (or similar commands) to revert files you didn't author—coordinate with other agents instead so their in-progress work stays intact.
- Always double-check git status before any commit
- Keep commits atomic: commit only the files you touched and list each path explicitly.
  - For tracked files run `git commit -m "<scoped message>" -- path/to/file1 path/to/file2`.
  - For brand-new files, use the one-liner `git restore --staged :/ && git add "path/to/file1" "path/to/file2" && git commit -m "<scoped message>" -- path/to/file1 path/to/file2`.
- Quote any git paths containing brackets or parentheses (e.g., `src/app/[candidate]/**`) when staging or committing so the shell does not treat them as globs or subshells.

### Commit message format

When asked to commit, do…

- Automatically stage files if none are staged
- Use conventional commit format with descriptive prefixes
- Split commits for different concerns

#### Commit Types:

- "FEAT": New features
- "FIX": Bug fixes
- "DOC": Documentation changes
- "REFACTOR": Code restructuring without changing functionality
- "STYLE": Code formatting, missing semicolons, etc.
- "PERF": Performance improvements
- "TEST": Adding or correcting tests
- "CHORE": Tooling, configuration, maintenance, dependency version updates
- "DEL": Removing code or files
- "SEC": Security improvements
- "HOTFIX": Critical fixes
- "WIP": Work in progress
- "CHG": General changes to existing code or functionality, i.e. anything that's not the above

Use these exclusively unless explicitly told otherwise.

#### Process:

1. Analyze changes to determine commit type
2. Generate descriptive title, prefix with commit type in square brackets ("[TYPE] description"), e.g. "[FEAT] Add new feature" or "[FIX] Fix problems with x, y, z"
3. Generate descriptive commit message
4. Add body for complex changes explaining why
5. Execute commit

#### Best Practices:

- Keep commits atomic and focused
- Write in imperative mood ("Add feature" not "Added feature")
- Explain why, not just what
- Split unrelated changes into separate commits
- Reference issues/ PRs/ ticket numbers only at the end of commit messages, after a blank line, on a separate line: "Part of <ticket-id>"
