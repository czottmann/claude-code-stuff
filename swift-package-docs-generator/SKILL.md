---
name: Swift Package Documentation Generator
description: Generates comprehensive API documentation for Swift package dependencies on-demand. This skill helps you quickly obtain documentation for packages used in Xcode projects when you encounter unfamiliar module imports.
---

## Usage

```bash
python3 ./scripts/generate_docs.py <module_or_package_name> <xcodeproj_path>
```

**Arguments:**

- `module_or_package_name`: The Swift module or package name (e.g., `ButtonKit`, `Defaults`)
- `xcodeproj_path`: Path to the Xcode project file (e.g., `/path/to/MyApp.xcodeproj`)

**Output:**

- Prints the path to the generated (or existing) documentation file
- Documentation saved to `<project_dir>/dependency-docs/<package-name>-<major.minor>.md`

## Example

```bash
python3 ./scripts/generate_docs.py ButtonKit /Users/czottmann/Code/BarCuts/BarCuts.xcodeproj
```

Output:

```
/Users/czottmann/Code/BarCuts/dependency-docs/ButtonKit-0.6.md
```

## What It Does

1. **Resolves module to package** using the `swift-dependency-list` skill if needed
2. **Checks for existing documentation** in `dependency-docs/`
3. **If docs don't exist:**
   - Locates the package in DerivedData
   - Extracts version from git tags (major.minor only)
   - Runs `interfazzle generate` with a unique temp directory
   - Concatenates all generated `.md` files
   - Appends the package's README if it exists
   - Saves to `dependency-docs/<package-name>-<major.minor>.md`
   - Cleans up the temporary output directory
4. **Returns the documentation file path**

## Prerequisites

- Python 3.6+
- `interfazzle` CLI tool installed and in PATH
- Project built at least once (DerivedData must exist)
- `swift-dependency-list` skill available

## When to Use This Skill

Use this skill when:

- You encounter an unfamiliar module import and need its API documentation
- You want to explore a dependency's API surface
- You need to reference package documentation while coding

## Script Location

The Python script is located at: `./scripts/generate_docs.py` (relative to this skill's base directory)
