# Swift Dependency List - Reference

Generates a comprehensive overview of Swift packages and their exported modules from Xcode's DerivedData. This helps quickly identify which package a specific module belongs to when seeing `import` statements in source code.

## Contents

- [Command-Line Usage](#command-line-usage)
- [Example Usage](#example-usage)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [When to Use This Skill](#when-to-use-this-skill)
- [Limitations](#limitations)
- [Implementation](#implementation)

## Command-Line Usage

```bash
python3 ./scripts/extract_xcode_dependencies.py /path/to/my_project.xcodeproj
```

### Arguments

- Path to the Xcode project file (`.xcodeproj`)

### Output Format

Returns JSON mapping package names to their metadata:

```json
{
  "ButtonKit": {
    "version": "0.6.1",
    "repo": "https://github.com/Dean151/ButtonKit",
    "exported_modules": [
      "ButtonKit"
    ]
  },
  "Defaults": {
    "version": "8.2.0",
    "repo": "https://github.com/sindresorhus/Defaults",
    "exported_modules": [
      "Defaults"
    ]
  }
}
```

Each package entry includes:

- **version**: The exact version installed
- **repo**: The git repository URL
- **exported_modules**: Array of module names that can be imported

## Example Usage

### Finding a Module's Package

If you see `import ButtonKit` in code, search the output for `"ButtonKit"` in `exported_modules` arrays to find it comes from the ButtonKit package at version 0.6.1.

### Identifying Multi-Module Packages

Some packages export multiple modules. For example, SharedBasics exports many modules:

```json
{
  "SharedBasics": {
    "version": "1.35.0",
    "repo": "https://git.zottmann.dev/czottmann/SharedBasics.git",
    "exported_modules": [
      "AppDetails",
      "AppIntentsHelpers",
      "AppUpdating",
      "Licensing",
      "Trialling",
      "..."
    ]
  }
}
```

If you see `import Licensing`, searching the `exported_modules` arrays reveals it comes from the SharedBasics package.

## How It Works

1. Locates the project's DerivedData directory
2. Scans for Swift package checkouts
3. Reads each package's `Package.swift` for metadata
4. Extracts version information from git tags
5. Lists all public modules exported by each package
6. Returns structured JSON output

## Prerequisites

- Project must be built at least once
- DerivedData must be present and current
- Python 3.6+

## When to Use This Skill

Use this skill when:

- You see an `import SomeModule` statement and want to know which Swift package provides it
- You need version information for installed packages
- You want to understand the package structure of a project
- You need to find the repository URL for a package

## Limitations

- Does not cover system frameworks (Foundation, SwiftUI, etc.)
- Only shows packages in DerivedData (project must be built)
- Requires valid git metadata for version extraction

## Implementation

The skill consists of:

- `SKILL.md` - Skill definition with YAML frontmatter
- `reference.md` - This detailed reference documentation
- `scripts/extract_xcode_dependencies.py` - Main implementation script (relative to skill directory)
- `../_shared/swift_packages.py` - Shared Swift package utilities (used by multiple skills)
