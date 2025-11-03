---
name: swift-dependency-list
description: Maps Swift import statements to their source packages. Use when encountering import statements (e.g., "import ButtonKit", "what package provides Defaults"), when needing package version information, or when the user asks which package exports a specific module. Extracts package metadata from Xcode DerivedData. Does not cover system frameworks.
allowed-tools: Bash
---

Generates a comprehensive mapping of Swift packages to their exported modules from Xcode's DerivedData.

## How to Use This Skill

When the user asks which package provides a specific module (e.g., "what package is ButtonKit from?"):

1. **Find the Xcode project path** - look for a `.xcodeproj` file in the current working directory

2. **Run the dependency list script**:
   ```bash
   python3 ~/.claude/skills/swift-dependency-list/scripts/extract_xcode_dependencies.py "<path_to.xcodeproj>"
   ```

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

```bash
python3 ~/.claude/skills/swift-dependency-list/scripts/extract_xcode_dependencies.py "/Users/czottmann/Code/Browser Actions/Browser Actions.xcodeproj"
```

Returns JSON showing all packages and their modules. To find which package provides "AppUpdating", search for "AppUpdating" in the `exported_modules` arrays.

## Important Notes

- The script outputs JSON to stdout
- The project must have been built at least once (DerivedData must exist)
- Only shows SPM packages, not system frameworks
- Add `--verbose` flag for debugging output (goes to stderr)
- Uses shared Swift package utilities from `~/.claude/skills/_shared/swift_packages.py`
