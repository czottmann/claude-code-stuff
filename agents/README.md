# Claude Code Custom Subagents

This directory contains custom subagent definitions for use with Claude Code.

## Installation

Symlink this directory to make these agents available:

```bash
# For all projects (user-level):
ln -s /Users/czottmann/Code/claude-code-stuff/agents ~/.claude/agents

# For specific project (project-level):
ln -s /Users/czottmann/Code/claude-code-stuff/agents /path/to/project/.claude/agents
```

Project-level agents take precedence over user-level agents.

## Available Agents

### Search Agent

**File**: `search.md`

**Purpose**: Fast code location finding with minimal context pollution.

**Use when**: You need to find code in a codebase but don't know where it is.

**Model**: Haiku (fast, cost-efficient)

**Tools**: Grep, Glob, Read, Bash

**Typical queries**:

- "Where is the authentication code?"
- "Find the issue parser implementation"
- "Locate where GraphQL queries are executed"

**How it works**:

1. Uses multiple grep strategies with keyword variations
2. Validates results by reading small code snippets
3. Returns structured locations with confidence scores
4. Designed to run quickly (<30 seconds, <10 file reads)

**Output**: Structured text with file paths, line ranges, confidence levels, and reasoning.

**Works with**: The built-in Explore agent - Search finds locations, Explore explains them.

## Usage

### Automatic Delegation

Claude Code will automatically use these agents when appropriate. The Search agent includes "PROACTIVELY" in its description, so Claude will use it for location-finding queries without prompting.

### Explicit Invocation

You can request specific agents:

```
"Use the search agent to find authentication code"
```

### Search → Explore Pipeline

For understanding existing code:

1. Ask a question: "How does authentication work?"
2. Claude uses Search agent to find relevant code locations
3. Claude then uses Explore agent to understand and explain the code
4. You get a comprehensive answer without context pollution

## Architecture

### Why Separate Search and Explore?

**Problem**: Searching for code creates noise:

- Multiple grep iterations with different keywords
- Reading many irrelevant files
- 10-50K tokens of failed searches polluting context

**Solution**: Two-stage pipeline:

1. **Search (Haiku)**: Fast location finding in isolated context
2. **Explore (Sonnet)**: Deep understanding with pre-found locations

**Benefits**:

- 40-60% cost reduction for exploratory tasks
- 30-50% faster completion
- Cleaner main conversation context
- Each agent optimized for its specific task

## Agent Details

### Search Agent Configuration

```yaml
name: search
description: Fast code location finding...
tools: Grep, Glob, Read, Bash
model: haiku
```

**Search Strategies**:

1. Direct keyword matching (with case variations)
2. Pattern matching (function/class definitions)
3. File naming conventions (globs)
4. Layered expansion (start specific, broaden if needed)
5. Smart filtering (file types, directories)

**Output Format**:

```
SEARCH RESULT: found|partial|not_found
CONFIDENCE: high|medium|low

LOCATIONS:
1. FILE: path/to/file.ts
   LINES: 142-167
   CONFIDENCE: high
   SNIPPET: parseIssueIdentifier(id: string)...
   REASON: Main implementation, handles ABC-123 format

SEARCH STRATEGY:
Searched for "parseIssue", filtered to *.ts files...

STATS:
Files searched: 127
Files read: 8
Grep iterations: 4
```

### Performance Guidelines

Search agent aims for:

- <10 file reads per search
- <30 seconds completion time
- <5K tokens context usage
- 90% accuracy finding correct locations

## Examples

### Example 1: Simple Location Query

**User**: "Where is parseIssueIdentifier defined?"

**Flow**:

1. Search agent finds `src/utils/linear-service.ts:142-167`
2. Returns location with high confidence
3. Main agent reports: "Found at src/utils/linear-service.ts:142-167"

**Cost**: ~500 tokens (Search only)

### Example 2: Understanding Implementation

**User**: "How does authentication work in this project?"

**Flow**:

1. Search agent finds auth.ts, linear-service.ts, commands/*.ts
2. Returns 5 locations with confidence scores
3. Explore agent receives those locations
4. Explore reads files, traces flow, explains architecture
5. Main agent synthesizes: "Authentication uses a 3-tier fallback system..."

**Cost**: ~500 (Search) + ~5K (Explore) = ~5.5K tokens **Without pipeline**: Would be ~15-20K tokens in main conversation

### Example 3: Complex Multi-Part Search

**User**: "Explain the complete issue lifecycle in this CLI"

**Flow**:

1. Main agent launches 3 Search agents in parallel:
   - "Find issue creation code"
   - "Find issue update code"
   - "Find issue deletion code"
2. Each returns 2-3 locations
3. Explore agent receives all 9 combined locations
4. Explore synthesizes full lifecycle explanation

**Cost**: 3×500 (Search) + ~8K (Explore) = ~9.5K tokens **Without pipeline**: Would be ~40-60K tokens

## Development

### Creating New Agents

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with name, description, tools, model
3. Write detailed system prompt
4. Test with real queries
5. Iterate based on results

### Agent Template

```markdown
---
name: agent-name
description: What this agent does and when to use it. Include PROACTIVELY for automatic delegation.
tools: Tool1, Tool2, Tool3
model: haiku|sonnet|opus
---

You are a specialized agent for...

## Core Responsibilities

1. First responsibility
2. Second responsibility

## Input Format

Describe what input this agent expects...

## Output Format

Describe what this agent returns...

## Key Behaviors

**DO:**

- Thing to do
- Another thing

**DO NOT:**

- Thing to avoid
- Another thing to avoid
```

### Testing Agents

After creating or modifying an agent:

1. Reload Claude Code (or start new session)
2. Run `/agents` to verify agent appears
3. Test with explicit invocation: "Use the [agent-name] agent to..."
4. Test automatic delegation with natural queries
5. Monitor token usage and performance

## References

- [Claude Code Subagents Documentation](https://code.claude.com/docs/en/sub-agents.md)
- [Search → Explore Pipeline Specification](../SEARCH_EXPLORE_PIPELINE_SPEC.md)
- [Claude Code Documentation](https://code.claude.com/docs)

## Contributing

When adding or modifying agents:

1. Follow the agent template structure
2. Test thoroughly with real-world queries
3. Document expected behavior and output format
4. Update this README with new agents
5. Commit with descriptive message using project conventions

## Version History

- 2025-11-07: Initial creation with Search agent
