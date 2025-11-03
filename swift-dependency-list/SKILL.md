---
name: Xcode project module origins
description: Provides information on Swift `import …` statements and which module they belong to
---

## Purpose

Generates a comprehensive overview of Swift packages and their exported modules
from Xcode's DerivedData. This helps quickly identify which package a specific
module belongs to when seeing `import` statements in source code.

## Usage

```bash
python3 ./scripts/extract_xcode_dependencies.py /path/to/my_project.xcodeproj
```

Output:

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
  },
  …
}
```

The Python script is located relative to this skill's base directory.

## Example Query

If you see `import ButtonKit` in code, search the output for `"ButtonKit"` in
`exported_modules` arrays to find it comes from the ButtonKit package at version
0.6.1.

## Prerequisites

- Project must be built at least once
- DerivedData must be present and current

## When to Use This Skill

Use this when you see an `import SomeModule` statement and want to know which
Swift package provides that module. It does not cover system frameworks.
