# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Claude Code [sub-agents](https://code.claude.com/docs/en/sub-agents), [agent skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview.md), and rules (which will be used to build global CLAUDE.md/AGENTS.md files).

This is a hybrid architecture that combines:

- **Custom content**: Skills and agents for iOS/macOS development, planning, and collaboration
- **Global rules**: Compiled behavior guidelines deployed to Claude Code's global configuration

Tasks are set up using [mise](https://mise.jdx.dev/tasks/). Run `mise tasks ls` to see available tasks.

## Repository Structure

```
claude-code-stuff/
├── agents/                         # Claude Code sub-agents (2 agents)
│   ├── documentation-generator.md
│   └── search.md                   # Fast code location specialist
│
├── rules/                          # Source files for AGENTS.md
│   ├── 0-start.md                  # Foundational principles
│   ├── git.md                      # Git workflow preferences
│   ├── kagi.md                     # Kagi search integration
│   ├── issue-tracking.md           # Issue tracking integration
│   └── ...                         # Additional behavior rules
│
├── skills/                         # Skills directory (8 skills)
│   ├── developing-with-swift/      # Swift language guidelines
│   ├── generating-swift-package-docs/  # Swift package docs
│   ├── using-xcode/                # Xcode tooling
│   ├── brainstorming/              # Idea refinement
│   ├── making-plans/               # Implementation planning
│   ├── issue-tracking-with-linear/ # Linear integration
│   ├── issue-tracking-with-beans/  # Beans-only projects
│   └── issue-tracking-with-beans-and-linear/  # Both systems
│
├── .mise/tasks/                    # Automation scripts (3 tasks)
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

**Available Agents** (2):

- `search` - Fast code location finding (<10 file reads, <30s, <5K tokens)
- `documentation-generator` - Comprehensive documentation creation

### Skills

Executable workflows that Claude must follow when relevant. Skills are **mandatory** when they match the task context.

**Available Skills** (8):

- `developing-with-swift` - Style guidelines, Swift techniques
- `generating-swift-package-docs` - On-demand Swift package API documentation
- `using-xcode` - Xcode tooling and build workflows
- `brainstorming` - Collaborative idea refinement
- `making-plans` - Breaking epics into implementation tasks
- `issue-tracking-with-linear` - Linear issue tracker integration
- `issue-tracking-with-beans` - Beans-only issue tracking (TodoWrite + Beans)
- `issue-tracking-with-beans-and-linear` - Full integration (TodoWrite + Beans + Linear)

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

### Build and Deploy

```bash
mise run build-agents-md          # Compile rules/*.md → .build/AGENTS.md
mise run symlink-agents-md        # Symlink AGENTS.md to ~/.claude/CLAUDE.md etc.
mise run symlink-folders-to-claude # Symlink ./agents, ./skills, etc. to ~/.claude/
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
