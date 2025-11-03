# Swift Package Documentation Generator

Automatically generates comprehensive API documentation for Swift package dependencies using [`interfazzle`](https://github.com/czottmann/interfazzle).

## Features

- **Automatic package resolution**: Maps module names to package names using dependency information
- **Smart caching**: Checks for existing documentation before generating
- **Clean integration**: Uses temporary UUID-based directories for generation, then cleans up
- **Comprehensive output**: Combines all generated markdown with package README files
- **Version-aware**: Generates docs with version-specific filenames (major.minor format)

## Usage

From within Claude Code, invoke this skill when you need documentation for a Swift package dependency. The skill will:

1. Resolve the module/package name
2. Check if docs already exist in `dependency-docs/`
3. If needed, generate fresh documentation from DerivedData
4. Return the path to the documentation file

## Example

When you encounter an unfamiliar import:

```swift
import ButtonKit
```

The skill generates (or retrieves) documentation at:

```
<project>/dependency-docs/ButtonKit-0.6.md
```

## Requirements

- Python 3.6+
- `interfazzle` CLI tool, https://github.com/czottmann/interfazzle
- `swift-dependency-list` skill
- Project must be built at least once

## Output Format

Documentation files are saved as:

```
<project>/dependency-docs/<PackageName>-<major.minor>.md
```

## Implementation

The skill consists of:

- `skill.md` - Skill description and usage instructions
- `scripts/generate_docs.py` - Main implementation script

## Testing

Verified working with:

- ButtonKit 0.6.1 → `ButtonKit-0.6.md` (21KB)
- Defaults 8.2.0 → `Defaults-8.2.md` (47KB)

Both successfully generated, cached on subsequent runs, and temp directories properly cleaned up.
