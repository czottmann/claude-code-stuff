# Claude Code Stuff

My personal, current, production-ready configuration system for [Claude Code](https://claude.ai/code) featuring custom agents, skills, and global behavior rules.

## What This Is

This repository provides a complete setup for extending Claude Code with:

- **Custom Agents** - Specialized sub-agents for documentation generation and fast code search
- **Custom Skills** - Workflows for Swift development, Xcode tooling, brainstorming, planning, and issue tracking
- **Global Rules** - Compiled behavior guidelines that configure Claude Code's global behavior
- **Beads Integration** - Git-friendly issue tracking via [obra/beads](https://github.com/obra/beads) for agent workflows

## Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- [mise](https://mise.jdx.dev/) task runner
- Python 3.6+
- Xcode (for Swift-related features)

### Setup

```bash
# Build global rules
mise run build-agents-md

# Deploy to Claude Code
mise run symlink-agents-md
mise run symlink-folders-to-claude
```

### Verify Installation

```bash
# Check available mise tasks
mise tasks ls

# Verify agents are linked
ls -la ~/.claude/agents/

# Verify skills are linked
ls -la ~/.claude/skills/
```

## What You Get

### 🤖 Agents (2)

Specialized sub-agents that provide **40-60% cost reduction** and **30-50% speed improvement** through task-appropriate model selection:

- **search** - Lightning-fast code location (<10 file reads, <30s, <5K tokens)
- **documentation-generator** - Comprehensive documentation creation

### 🎯 Skills (7)

Workflows for development, planning, and collaboration:

- **developing-with-swift** - Style guidelines, Swift techniques
- **generating-swift-package-docs** - On-demand Swift package API documentation
- **using-xcode** - Xcode tooling and build workflows
- **brainstorming** - Collaborative idea refinement
- **making-plans** - Breaking epics into implementation tasks
- **using-linear** - Linear issue tracker integration
- **using-beads** - Git-friendly agent issue tracking (from libs/beads)

### 📜 Global Rules (11)

Compiled behavior guidelines deployed to `~/.claude/CLAUDE.md`:

- Foundational principles and relationship dynamics
- Mandatory skill usage protocol
- Git workflow preferences
- Tool integrations (Kagi, Linear)
- Task implementation guidance

## Architecture

```
┌─────────────────────────────────────────────────────┐
│ This Repository (claude-code-stuff)                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Custom Content         External Dependencies       │
│  ├── agents/            └── libs/beads/             │
│  ├── skills/                (issue tracking)        │
│  └── rules/                                         │
│                                                     │
│  Build System                                       │
│  └── .mise/tasks/       ──▶  .build/AGENTS.md       │
│                                                     │
└─────────────────────────────────────────────────────┘
                          │
                          │ Deploy (symlinks)
                          ▼
┌─────────────────────────────────────────────────────┐
│ Claude Code User Directory (~/.claude/)             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ~/.claude/agents/      ──▶  this/agents/           │
│  ~/.claude/skills/      ──▶  this/skills/           │
│  ~/.claude/CLAUDE.md    ──▶  this/.build/AGENTS.md  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Key Concepts

### Separation of Concerns

- **Rules** (`/rules/`) - Individual behavior guidelines, compiled into AGENTS.md
- **Skills** (`/skills/`) - Executable workflows that Claude must follow
- **Agents** (`/agents/`) - Specialized sub-agents for specific tasks
- **Hook scripts** (`/hook-scripts`) - Used with CC's [hooks](https://code.claude.com/docs/en/hooks)

### Symlink Architecture

All deployments use symlinks - change source files, and Claude Code sees updates instantly. No copying, no syncing.

### Compilation Pattern

Global rules are modular:

1. Write small, focused rule files in `/rules/`
2. Run `mise run build-agents-md` to concatenate
3. Deploy to `~/.claude/CLAUDE.md` via `mise run symlink-agents-md`

## Common Tasks

```bash
# Update beads to latest
git submodule update --remote libs/beads

# Rebuild global rules after editing /rules/
mise run build-agents-md
mise run symlink-agents-md

# Add a new custom skill
mkdir -p skills/my-new-skill
# Create SKILL.md following the pattern in existing skills

# Test a skill's Python script
cd skills/generating-swift-package-docs
./scripts/generate_docs.py ModuleName /path/to/Project.xcodeproj
```

## Development Workflow

1. **Edit Rules**: Modify files in `/rules/`, then `mise run build-agents-md`
2. **Add Skills**: Create in `/skills/`, follow SKILL.md format (see existing examples)
3. **Create Agents**: Add to `/agents/`, include YAML frontmatter with model/tools config
4. **Test Locally**: Deploy to `~/.claude/` before committing
5. **Update Dependencies**: `git submodule update --remote libs/beads`

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

- Mix custom domain expertise (Swift) with proven practices (superpowers)
- Update components independently
- Deploy globally or per-project

### Maintainability

- Single source of truth for each component
- Version-controlled behavior changes
- Auditable rule compilation

## Requirements

- **Claude Code** - The CLI tool this configures
- **mise** - Task runner for automation (`brew install mise`)
- **Python 3.6+** - For skill scripts
- **gum** (optional) - For interactive confirmations (`brew install gum`)
- **Xcode** (optional) - For Swift-related features
- **interfazzle** (optional) - For Swift package docs (https://github.com/czottmann/interfazzle)

## Author

Carlo Zottmann, <carlo@zottmann.dev>, https://c.zottmann.dev, https://github.com/czottmann.

This project is neither affiliated with nor endorsed by Linear. I'm just a very happy customer.

> [!TIP]
> I make Shortcuts-related macOS & iOS productivity apps like [Actions For Obsidian](https://actions.work/actions-for-obsidian), [Browser Actions](https://actions.work/browser-actions) (which adds Shortcuts support for several major browsers), and [BarCuts](https://actions.work/barcuts) (a surprisingly useful contextual Shortcuts launcher). Check them out!

## License

Legally: [MIT License.](LICENSE.md)

Spiritually: [WTFPL.](https://en.wikipedia.org/wiki/WTFPL)

## Credits

- **Beads** - [obra/beads](https://github.com/obra/beads) provides git-friendly issue tracking for agent workflows
- **Claude Code** - [claude.ai/code](https://claude.ai/code)
