---
# ccs-cr14
title: Create shell scripting skill (fish + gum)
status: completed
type: epic
priority: normal
created_at: 2026-01-18T17:41:38Z
updated_at: 2026-01-18T17:42:57Z
---

## Overview

A skill for writing shell scripts using **fish shell** and **gum** for personal developer tooling and system automation.

## Design

### Frontmatter & Role

```yaml
---
name: writing-shell-scripts
description: Use this before writing any shell scripts - establishes fish shell syntax, gum integration patterns, and script organization conventions
---
```

**Role:** Writing shell scripts for personal tooling and system automation. All scripts use fish shell (not bash/POSIX) and gum for interactive components. Target environment is macOS with fish as the default shell.

**Core principles:**

1. **Fish-first** — Never use bash syntax
2. **Gum for all interaction** — No fallbacks needed
3. **Fail fast, fail loud** — Check preconditions early, exit with clear errors
4. **No over-engineering** — Personal scripts, no unnecessary abstractions

### Fish Syntax Guide

**Variables:**

```fish
set myvar "value"           # local
set -x EXPORTED_VAR "value" # export
set -e myvar                # unset
```

**Conditionals:**

```fish
if test -f "$file"
    echo "exists"
else if test -d "$dir"
    echo "is directory"
end

if command -q git
    # git is available
end
```

**Loops:**

```fish
for item in $list
    echo $item
end
```

**String manipulation — use `string`, not sed/awk:**

```fish
string replace "old" "new" $text
string split ":" $PATH
string match -q "*.txt" $filename
string trim $input
```

**Command substitution:**

```fish
set result (command)  # NOT $(command)
```

### Gum Patterns

**User input:**

```fish
set name (gum input --placeholder "Project name")
```

**Selection:**

```fish
set choice (gum choose "Option A" "Option B" "Option C")
set choices (gum choose --no-limit "one" "two" "three")
```

**Confirmation:**

```fish
if gum confirm "Delete all logs?"
    rm -rf logs/
end
```

**Styled output:**

```fish
gum style --foreground 212 --bold "Success!"
gum style --border rounded --padding "1 2" "Boxed message"
```

**Progress:**

```fish
gum spin --title "Installing..." -- long_running_command
```

### Error Handling

**Precondition checks:**

```fish
for cmd in gum jq curl
    if not command -q $cmd
        fatal "$cmd is required but not installed"
    end
end

if not set -q API_TOKEN
    fatal "API_TOKEN environment variable not set"
end
```

**Confirm destructive actions:**

```fish
if gum confirm "Delete all files in $target_dir?"
    rm -rf "$target_dir"/*
    success "Cleaned $target_dir"
else
    info "Aborted"
end
```

**Output helpers (globally installed in ~/.config/fish/functions/):**

- `success` — green ✓
- `info` — blue •
- `warn` — yellow ⚠
- `error` — orange ✗ (stderr)
- `fatal` — red ✗ (stderr + exit 1)

### Script Organization

**Locations:**

| Location                    | Purpose                          |
| --------------------------- | -------------------------------- |
| `~/.config/fish/functions/` | Reusable functions (auto-loaded) |
| `~/.local/bin/`             | Standalone executable scripts    |
| `<project>/bin/`            | Project-specific scripts         |

**Naming:** lowercase, hyphens: `deploy-staging`, `cleanup-logs`

**Shebang:** `#!/usr/bin/env fish`

**No `.fish` extension** for standalone scripts (use shebang)

**Multi-file tools:**

```
~/.local/bin/mytool                      # main script
~/.local/bin/helpers/mytool-helpers.fish # supporting helpers
```

### Style Guide

**Formatting:** Use `fish_indent -w script.fish`

**Variable naming:**

```fish
set -l local_var "value"      # snake_case
set -x EXPORTED_VAR "value"   # UPPER_SNAKE for exports
```

**Quoting:** Always quote variables: `"$myvar"`

**Line length:** Under 100 chars. Break long pipelines with `\`

### Documentation

**Every script must have `--help`:**

```fish
#!/usr/bin/env fish

argparse 'help' 'force' 'verbose' -- $argv
or return

function usage
    echo '
script-name

Brief description.

USAGE:
  script-name [OPTIONS] <required-arg>

ARGUMENTS:
  required-arg    Description

OPTIONS:
  --force      Override existing files
  --verbose    Show detailed output
  --help       Show this usage description

REQUIRES:
  - gum

OUTPUTS:
  - What the script produces
'
end

if set -q _flag_help
    usage
    exit 0
end
```

## Implementation Tasks

- [x] Create skill directory and SKILL.md
- [x] Add all sections from design
- [x] Test skill auto-discovery
- [x] Symlink to ~/.claude/skills/

## Summary of Changes

Created the `writing-shell-scripts` skill at `skills/writing-shell-scripts/SKILL.md` with:

- Fish shell syntax guide (variables, conditionals, loops, string manipulation, command substitution)
- Gum patterns for user interaction (input, selection, confirmation, styled output, spinners)
- Error handling guidance with output helper functions
- Script organization conventions (locations, naming, shebang, multi-file structure)
- Style guide (formatting with fish_indent, variable/function naming, quoting)
- Documentation requirements (mandatory --help with argparse)

Also created global fish output helper functions in `~/.config/fish/functions/`:

- `success`, `info`, `warn`, `error`, `fatal`
