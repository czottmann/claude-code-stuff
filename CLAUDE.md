# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Claude Code [sub-agents](https://code.claude.com/docs/en/sub-agents), [agent skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview.md), and rules (which will be used to build global CLAUDE.md/AGENTS.md files).

This is a hybrid architecture that combines:

- **Custom content**: Swift-specific skills and agents for iOS/macOS development
- **External dependencies**: The [superpowers](https://github.com/obra/superpowers) library for battle-tested engineering practices
- **Global rules**: Compiled behavior guidelines deployed to Claude Code's global configuration

Tasks are set up using [mise](https://mise.jdx.dev/tasks/). Run `mise tasks ls` to see available tasks.

## Repository Structure

```
claude-code-stuff/
├── agents/                         # Claude Code sub-agents (4 agents)
│   ├── code-reviewer.md            # Symlink to superpowers
│   ├── documentation-generator.md
│   └── search.md                   # Fast code location specialist
│
├── rules/                          # Source files for AGENTS.md (11 files)
│   ├── 0-start.md                  # Foundational principles
│   ├── 1-skills-usage.md           # Mandatory skill usage protocol
│   ├── git.md                      # Git workflow preferences
│   ├── kagi.md                     # Kagi search integration
│   ├── linear.md                   # Linear issue tracker integration
│   └── ...                         # Additional behavior rules
│
├── skills/                         # Combined skills directory
│   ├── developing-with-swift/      # Custom: Swift language & Xcode tooling
│   ├── generating-swift-package-docs/  # Custom: Swift package docs
│   └── [19 symlinks to superpowers skills]
│       ├── systematic-debugging
│       ├── test-driven-development
│       ├── brainstorming
│       └── ...
│
├── libs/superpowers/               # Git submodule (obra/superpowers)
│   ├── agents/
│   ├── commands/
│   └── skills/
│
├── mise-tasks/                     # Automation scripts (6 tasks)
│   ├── add-libs-agents             # Link superpowers agents
│   ├── add-libs-skills             # Link superpowers skills
│   ├── build-agents-md             # Compile rules → AGENTS.md
│   ├── symlink-agents-md           # Symlink AGENTS.md to ~/.claude/CLAUDE.md etc.
│   └── symlink-folders-to-claude   # Symlink agents, skills, etc. directory
│
├── .build/                         # Build artifacts
│   └── AGENTS.md                   # Compiled from rules/*.md
│
└── CLAUDE.md                       # This file
```

## Key Components

### Agents

Specialized Claude Code sub-agents for specific tasks. Using dedicated agents provides:

- 40-60% cost reduction via task-appropriate models (Haiku for search, Sonnet for exploration)
- 30-50% speed improvement
- Isolated context (no search noise pollution)

**Available Agents**:

- `search` - Fast code location finding (<10 file reads, <30s, <5K tokens)
- `documentation-generator` - Comprehensive documentation creation
- `swift-swiftui-developer` - Swift/SwiftUI development specialist
- `code-reviewer` - Implementation validation against requirements

### Skills

Executable workflows that Claude must follow when relevant. Skills are **mandatory** when they match the task context (see `rules/1-skills-usage.md`).

**Custom Skills** (2):

- `developing-with-swift` - Style guidelines, Swift techniques, Xcode tools
- `generating-swift-package-docs` - On-demand Swift package API documentation

**Linked Superpowers Skills** (19):

- Testing: test-driven-development, testing-anti-patterns
- Debugging: systematic-debugging, root-cause-tracing
- Development: using-git-worktrees, finishing-a-development-branch
- Collaboration: brainstorming, requesting-code-review, receiving-code-review
- Planning: writing-plans, executing-plans, subagent-driven-development
- And more...

### Rules

Source material for global Claude Code behavior. Individual rule files in `/rules/` are compiled into `.build/AGENTS.md` and deployed to:

- `~/.claude/CLAUDE.md`
- `~/.codex/AGENTS.md`
- `~/.config/opencode/AGENTS.md`

**Build Process**:

```bash
mise run build-agents-md   # Concatenate rules/*.md → .build/AGENTS.md
mise run symlink-agents-md # Symlink to global config locations
```

## Mise Tasks

Run `mise tasks ls` to see all available tasks. Common workflows:

### Initial Setup

```bash
mise run add-libs-skills # Link superpowers skills
mise run add-libs-agents # Link superpowers agents
mise run build-agents-md # Build AGENTS.md
```

### Deploy Globally

```bash
mise run symlink-folders-to-claude # links ./agents, ./skills, etc. to  ~/.claude/
```

## Organization Principles

1. **Separation of Concerns**: Rules (behavior) vs Skills (workflows) vs Agents (specialized tasks)
2. **Symlink Architecture**: Easy updates - change source, links reflect instantly
3. **Compilation Pattern**: Small, focused rule files → compiled AGENTS.md
4. **Domain Specialization**: Swift-specific content + generic engineering practices
5. **Deployment Flexibility**: User-level (~/.claude/) vs project-level (.claude/)

## Development Guidelines

When working in this repository:

1. **Editing Rules**: Modify files in `/rules/`, then run `mise run build-agents-md`
2. **Adding Skills**: Create in `/skills/`, follow SKILL.md format (see existing examples)
3. **Creating Agents**: Add to `/agents/`, include YAML frontmatter with model/tools config
4. **Testing Changes**: Deploy locally before committing
5. **Dependencies**: Update superpowers submodule with `git submodule update --remote`
