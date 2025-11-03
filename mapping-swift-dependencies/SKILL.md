---
name: mapping-swift-dependencies
description: Maps Swift import statements to their source packages and extracts package metadata from Xcode DerivedData. Use when encountering import statements, needing package version information, or finding which package exports a specific module. Does not cover system frameworks.
allowed-tools: Bash
---

Generates a comprehensive mapping of Swift packages to their exported modules from Xcode's DerivedData.

## How to Use This Skill

When the user asks which package provides a specific module (e.g., "what package is ButtonKit from?"):

1. **Find the Xcode project path** - look for a `.xcodeproj` file in the current working directory

2. **Run the dependency list script**: `./scripts/extract_xcode_dependencies.py "<path_to.xcodeproj>"`

3. **The script outputs JSON** mapping package names to their metadata:
   ```json
   {
     "PackageName": {
       "version": "1.2.3",
       "repo": "https://github.com/...",
       "exported_modules": ["Module1", "Module2"]
     }
   }
   ```

4. **Search the JSON** for the module name in `exported_modules` arrays to find which package provides it

## Example

```
./scripts/extract_xcode_dependencies.py "/path/to/your/project.xcodeproj"
```

Returns JSON showing all packages and their modules. To find which package provides "Module1", search for "Module1" in the `exported_modules` arrays.

## Important Notes

- The script outputs JSON to stdout
- The project must have been built at least once (DerivedData must exist)
- Only shows SPM packages, not system frameworks
- Add `--verbose` flag for debugging output (goes to stderr)
- Uses shared Swift package utilities from `~/.claude/skills/_shared/swift_packages.py`
