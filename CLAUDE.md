# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Claude Code [sub-agents](https://code.claude.com/docs/en/sub-agents), [agent skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview.md), and modular rules for iOS/macOS development, planning, and collaboration.

All components are deployed via symlinks to `~/.claude/`.

Tasks are set up using [mise](https://mise.jdx.dev/tasks/). Run `mise tasks ls` to see available tasks.

## Repository Structure

```
claude-code-stuff/
├── agents/                         # Claude Code sub-agents (2 agents)
│   ├── documentation-generator.md
│   └── search.md                   # Fast code location specialist
│
├── rules/                          # Modular rules (symlinked to ~/.claude/rules/)
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
├── .mise/tasks/                    # Automation scripts
│   └── symlink-folders-to-claude   # Symlink agents, rules, skills, etc. to ~/.claude/
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

Modular behavior rules in `/rules/`. Claude Code natively supports loading individual rule files from `~/.claude/rules/`, so no compilation is needed—just symlink the directory.

## Deployment

```bash
mise run symlink-folders-to-claude  # Symlink ./agents, ./rules, ./skills, etc. to ~/.claude/
```

## Organization Principles

1. **Separation of Concerns**: Rules (behavior) vs Skills (workflows) vs Agents (specialized tasks)
2. **Symlink Architecture**: Easy updates - change source, links reflect instantly
3. **Modular Rules**: Individual rule files loaded directly by Claude Code (no compilation)
4. **Domain Specialization**: Swift-specific content + generic engineering practices

## Development Guidelines

When working in this repository:

1. **Editing Rules**: Modify files in `/rules/` (changes are instant via symlinks)
2. **Adding Skills**: Create in `/skills/`, follow SKILL.md format (see existing examples)
3. **Creating Agents**: Add to `/agents/`, include YAML frontmatter with model/tools config
4. **Testing Changes**: Deploy via `mise run symlink-folders-to-claude` before committing
