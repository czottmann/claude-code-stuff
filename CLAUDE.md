# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Claude Code skills for working with Swift Package Manager dependencies in Xcode projects. Skills are modular capabilities that extend Claude's functionality through filesystem-based components.

## Repository Structure

```
.
├── _shared/                           # Shared utilities used by multiple skills
│   └── swift_packages.py             # Swift SPM dependency parsing and resolution
├── generating-swift-package-docs/    # Skill: Generate API docs for dependencies
│   ├── SKILL.md                      # Skill definition with YAML frontmatter
│   ├── reference.md                  # Detailed documentation
│   └── scripts/generate_docs.py      # Main implementation
└── mapping-swift-dependencies/       # Skill: Map imports to packages
    ├── SKILL.md                      # Skill definition with YAML frontmatter
    ├── reference.md                  # Detailed documentation
    └── scripts/extract_xcode_dependencies.py  # Main implementation
```

## Skill Architecture

### Skill Components

Each skill follows the Claude Code skills pattern:

1. **SKILL.md** - Entry point with YAML frontmatter (name, description, allowed-tools)
2. **reference.md** - Comprehensive documentation referenced from SKILL.md
3. **scripts/** - Python implementations that output to stdout/stderr

### Progressive Disclosure

Skills implement progressive disclosure per Claude Code best practices:

- **Metadata** (YAML frontmatter): Always loaded (~100 tokens)
- **Instructions** (SKILL.md): Loaded when skill matches user intent (<500 lines recommended)
- **Resources** (reference.md, scripts): Loaded on-demand via explicit references

### Shared Utilities

The `_shared/swift_packages.py` library provides common functionality:

- Parse Package.resolved from Xcode projects
- Locate packages in DerivedData/SourcePackages
- Extract module names from Package.swift files
- Resolve module names to package names

Skills import shared utilities via:

```python
sys.path.insert(0, str(Path.home() / ".claude/skills/_shared"))
from swift_packages import get_all_dependencies, resolve_module_to_package
```

## Testing Skills

### Manual Testing

Test skills by running their Python scripts directly:

```bash
# Test mapping-swift-dependencies
cd mapping-swift-dependencies
./scripts/extract_xcode_dependencies.py /path/to/Project.xcodeproj --verbose

# Test generating-swift-package-docs
cd generating-swift-package-docs
./scripts/generate_docs.py ModuleName /path/to/Project.xcodeproj
```

### Prerequisites

Skills require:

- Python 3.6+
- Xcode project built at least once (DerivedData must exist)
- For docs generation: `interfazzle` CLI tool (https://github.com/czottmann/interfazzle)

## Skill Development Guidelines

When modifying or creating skills, follow these patterns:

### Naming

- Use gerund form (verb + -ing): `mapping-`, `generating-`
- Avoid generic terms like "helper", "utils"
- Be specific and descriptive

### SKILL.md Structure

```markdown
---
name: skill-name
description: Specific description with trigger terms. Use when...
allowed-tools: Bash, Read
---

Brief introduction.

## How to Use This Skill

Step-by-step usage instructions...

## Prerequisites

Required tools and setup...

## Error Handling

Troubleshooting guidance...

## Additional Documentation

For comprehensive details, see [reference.md](reference.md).
```

### Script Conventions

- Output results to **stdout**
- Status/progress messages to **stderr**
- Use `tempfile` module for temporary directories
- Implement proper error handling with helpful messages
- Support `--verbose` flag for debugging

### Documentation

- Keep SKILL.md under 500 lines
- Add table of contents to reference.md if >100 lines
- Reference files explicitly from SKILL.md
- Keep file references one level deep (SKILL.md → reference.md only)
- Use relative paths: `./scripts/script.py (relative to skill directory)`

## Git Commit Conventions

Use commit type prefixes in square brackets:

- `[DOC]` - Documentation changes
- `[REFACTOR]` - Code restructuring without changing functionality
- `[FIX]` - Bug fixes
- `[FEAT]` - New features
- `[CHG]` - General changes to existing code

Example: `[REFACTOR] Use Python tempfile module for temporary directories`

## Key Implementation Details

### Dependency Resolution Flow

1. Read Package.resolved from Xcode project
2. Locate DerivedData/SourcePackages/checkouts for the project
3. Parse Package.swift files to extract module names
4. Map module imports to their source packages

### Documentation Generation Flow

1. Resolve module name to package using shared utilities
2. Check for cached documentation in `<project>/dependency-docs/`
3. If not cached:
   - Locate package in DerivedData
   - Run `interfazzle generate` with OS temp directory
   - Concatenate generated markdown files
   - Append package README if present
   - Save as `<package>-<major.minor>.md`

### Error Handling

Scripts handle common errors:

- Missing DerivedData (project not built)
- Missing Package.resolved
- Package not found in checkouts
- Missing git tags for versioning

All error messages go to stderr with actionable guidance.
