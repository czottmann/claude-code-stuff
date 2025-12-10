# Claude Code Stuff

My personal, current, production-ready configuration system for [Claude Code](https://claude.ai/code) featuring custom agents, skills, and global behavior rules.

## What This Is

This repository provides a complete setup for extending Claude Code with:

- **Custom Agents** - Specialized sub-agents for documentation generation and fast code search
- **Custom Skills** - Workflows for Swift development, Xcode tooling, brainstorming, planning, and issue tracking
- **Modular Rules** - Behavior guidelines loaded directly by Claude Code from `~/.claude/rules/`

## Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- [mise](https://mise.jdx.dev/) task runner
- Python 3.6+
- Xcode (for Swift-related features)

### Setup

```bash
# Deploy to Claude Code (symlinks agents, rules, skills, hooks-scripts)
mise run symlink-folders-to-claude
```

### Verify Installation

```bash
# Check symlinks
ls -la ~/.claude/agents/ ~/.claude/rules/ ~/.claude/skills/
```

## What You Get

### 🤖 Agents (2)

Specialized sub-agents that provide **40-60% cost reduction** and **30-50% speed improvement** through task-appropriate model selection:

- **search** - Lightning-fast code location (<10 file reads, <30s, <5K tokens)
- **documentation-generator** - Comprehensive documentation creation

### 🎯 Skills (8)

Workflows for development, planning, and collaboration:

- **developing-with-swift** - Style guidelines, Swift techniques
- **generating-swift-package-docs** - On-demand Swift package API documentation
- **using-xcode** - Xcode tooling and build workflows
- **brainstorming** - Collaborative idea refinement
- **making-plans** - Breaking epics into implementation tasks
- **issue-tracking-with-linear** - Linear issue tracker integration
- **issue-tracking-with-beans** - Beans-only issue tracking (TodoWrite + Beans)
- **issue-tracking-with-beans-and-linear** - Full integration (TodoWrite + Beans + Linear)

### 📜 Modular Rules

Individual rule files in `/rules/`, loaded directly by Claude Code from `~/.claude/rules/`:

- Foundational principles and relationship dynamics
- Git workflow preferences
- Tool integrations (Kagi, Linear)
- Preferred CLI tools

## Architecture

```
┌─────────────────────────────────────────────────────┐
│ This Repository (claude-code-stuff)                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ├── agents/                                        │
│  ├── rules/                                         │
│  ├── skills/                                        │
│  └── hooks-scripts/                                 │
│                                                     │
└─────────────────────────────────────────────────────┘
                          │
                          │ Symlinks
                          ▼
┌─────────────────────────────────────────────────────┐
│ Claude Code User Directory (~/.claude/)             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ~/.claude/agents/       ──▶  this/agents/          │
│  ~/.claude/rules/        ──▶  this/rules/           │
│  ~/.claude/skills/       ──▶  this/skills/          │
│  ~/.claude/hooks-scripts ──▶  this/hooks-scripts/   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Key Concepts

### Separation of Concerns

- **Rules** (`/rules/`) - Individual behavior guidelines, loaded directly by Claude Code
- **Skills** (`/skills/`) - Executable workflows that Claude must follow
- **Agents** (`/agents/`) - Specialized sub-agents for specific tasks
- **Hook scripts** (`/hooks-scripts/`) - Used with Claude Code's [hooks](https://code.claude.com/docs/en/hooks)

### Symlink Architecture

All deployments use symlinks—change source files, and Claude Code sees updates instantly. No compilation, no syncing.

## Development Workflow

1. **Edit Rules**: Modify files in `/rules/` (instant via symlinks)
2. **Add Skills**: Create in `/skills/`, follow SKILL.md format (see existing examples)
3. **Create Agents**: Add to `/agents/`, include YAML frontmatter with model/tools config
4. **Deploy**: Run `mise run symlink-folders-to-claude`

## Documentation

- **CLAUDE.md** - Detailed repository documentation (loaded by Claude Code)
- **skills/*/SKILL.md** - Individual skill documentation

## Why This Approach?

### Cost & Performance

Using specialized agents with appropriate models (Haiku for search, Sonnet for complex tasks):

- **40-60% cost reduction** on exploratory tasks
- **30-50% speed improvement** on code location
- Isolated context prevents token pollution

### Modularity

- Mix custom domain expertise (Swift) with generic engineering practices
- Update components independently
- Deploy globally via symlinks

### Maintainability

- Single source of truth for each component
- Version-controlled behavior changes
- Instant updates via symlinks

## Requirements

- **Claude Code** - The CLI tool this configures
- **mise** - Task runner for automation (`brew install mise`)
- **Python 3.6+** - For skill scripts
- **gum** (optional) - For interactive confirmations (`brew install gum`)
- **Xcode** (optional) - For Swift-related features
- **Interfazzle** (optional) - For Swift package docs (https://github.com/czottmann/interfazzle)
- **Beans** (optional) - For agentic issue tracking (https://github.com/hmans/beans)

## Author

Carlo Zottmann, <carlo@zottmann.dev>, https://c.zottmann.dev, https://github.com/czottmann.

This project is neither affiliated with nor endorsed by Linear. I'm just a very happy customer.

> [!TIP]
> I make Shortcuts-related macOS & iOS productivity apps like [Actions For Obsidian](https://actions.work/actions-for-obsidian), [Browser Actions](https://actions.work/browser-actions) (which adds Shortcuts support for several major browsers), and [BarCuts](https://actions.work/barcuts) (a surprisingly useful contextual Shortcuts launcher). Check them out!

## License

Legally: [MIT License.](LICENSE.md)

Spiritually: [WTFPL.](https://en.wikipedia.org/wiki/WTFPL)

## Credits

- **Claude Code** - [claude.ai/code](https://claude.ai/code)
