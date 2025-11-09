# Claude Code Configuration

My personal, current, production-ready configuration system for [Claude Code](https://claude.ai/code) featuring custom agents, skills, and global behavior rules.

## What This Is

This repository provides a complete setup for extending Claude Code with:

- **Custom Agents** - Specialized sub-agents for Swift/iOS development, documentation generation, and fast code search
- **Custom Skills** - Swift-specific workflows including package documentation generation and development guidelines
- **Global Rules** - Compiled behavior guidelines that configure Claude Code's global behavior
- **Superpowers Integration** - selective 20+ battle-tested engineering skills from [obra/superpowers](https://github.com/obra/superpowers)

## Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- [mise](https://mise.jdx.dev/) task runner
- Python 3.6+
- Xcode (for Swift-related features)

### Setup

```bash
# Link external skills and agents
mise run add-libs-skills
mise run add-libs-agents

# Build global rules
mise run build-agents-md

# Deploy to Claude Code
mise run deploy-agents-to-claude
mise run deploy-skills-to-claude
mise run deploy-agents-md
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

### 🤖 Agents (4)

Specialized sub-agents that provide **40-60% cost reduction** and **30-50% speed improvement** through task-appropriate model selection:

- **search** - Lightning-fast code location (<10 file reads, <30s, <5K tokens)
- **documentation-generator** - Comprehensive documentation creation
- **code-reviewer** - Implementation validation (from superpowers)

### 🎯 Custom Skills (3)

Domain-specific workflows for Swift development:

- **developing-with-swift** - Style guidelines, Swift techniques, Xcode tooling
- **generating-swift-package-docs** - On-demand Swift package API documentation
- **_shared** - Reusable utilities (Swift package parser)

### 🦸 Superpowers Skills (19)

Battle-tested engineering practices:

- **Testing** - test-driven-development, testing-anti-patterns, condition-based-waiting
- **Debugging** - systematic-debugging, root-cause-tracing, defense-in-depth
- **Development** - using-git-worktrees, finishing-a-development-branch
- **Collaboration** - brainstorming, requesting-code-review, receiving-code-review
- **Planning** - writing-plans, executing-plans, subagent-driven-development
- And more...

### 📜 Global Rules (11)

Compiled behavior guidelines deployed to `~/.claude/CLAUDE.md`:

- Foundational principles and relationship dynamics
- Mandatory skill usage protocol
- Git workflow preferences
- Tool integrations (Kagi, Linear)
- Task implementation guidance

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ This Repository (claude-code-stuff)                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Custom Content          External Dependencies              │
│  ├── agents/            ├── libs/superpowers/              │
│  ├── skills/            │   ├── agents/                    │
│  └── rules/             │   ├── skills/                    │
│                         │   └── commands/                  │
│                                                              │
│  Build System                                               │
│  └── mise-tasks/        ──▶  .build/AGENTS.md              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ Deploy (symlinks)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ Claude Code User Directory (~/.claude/)                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ~/.claude/agents/      ──▶  this/agents/                  │
│  ~/.claude/skills/      ──▶  this/skills/                  │
│  ~/.claude/CLAUDE.md    ──▶  this/.build/AGENTS.md         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Key Concepts

### Separation of Concerns

- **Rules** (`/rules/`) - Individual behavior guidelines, compiled into AGENTS.md
- **Skills** (`/skills/`) - Executable workflows that Claude must follow
- **Agents** (`/agents/`) - Specialized sub-agents for specific tasks

### Symlink Architecture

All deployments use symlinks - change source files, and Claude Code sees updates instantly. No copying, no syncing.

### Compilation Pattern

Global rules are modular:

1. Write small, focused rule files in `/rules/`
2. Run `mise run build-agents-md` to concatenate
3. Deploy to `~/.claude/CLAUDE.md` via `mise run deploy-agents-md`

## Common Tasks

```bash
# Update superpowers to latest
git submodule update --remote

# Rebuild global rules after editing /rules/
mise run build-agents-md
mise run deploy-agents-md

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
5. **Update Dependencies**: `git submodule update --remote` for superpowers

## Documentation

- **CLAUDE.md** - Detailed repository documentation (loaded by Claude Code)
- **agents/README.md** - Agent system documentation
- **skills/*/SKILL.md** - Individual skill documentation
- **SEARCH_EXPLORE_PIPELINE_SPEC.md** - Agent pipeline architecture

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

- **Superpowers** - [obra/superpowers](https://github.com/obra/superpowers) provides the foundation of battle-tested engineering skills
- **Claude Code** - [claude.ai/code](https://claude.ai/code)

