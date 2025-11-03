---
name: swift-package-docs-generator
description: Generates comprehensive API documentation for Swift package dependencies on-demand. This skill helps you quickly obtain documentation for packages used in Xcode projects when you encounter unfamiliar module imports. Automatically resolves modules to packages and caches documentation for reuse. This is the primary tool for understanding individual `import` statements. Use when:
    - User asks "what's import X?" or "what does import X do?" / Encountering unfamiliar import statements / Exploring a dependency's API / User asks about package documentation
  allowed-tools: Bash, Read
---

Generates comprehensive API documentation for Swift package dependencies in Xcode projects.

## How to Use This Skill

When the user asks about an unfamiliar Swift module import (e.g., "what's import AppUpdating?"):

1. **Identify the module name** from the user's question (e.g., "AppUpdating")

2. **Find the Xcode project path** - look for a `.xcodeproj` file in the current working directory or ask the user

3. **Run the documentation generator script**:
   ```bash
   python3 ~/.claude/skills/swift-package-docs-generator/scripts/generate_docs.py "<module_name>" "<path_to.xcodeproj>"
   ```

4. **The script will**:
   - Automatically determine which package provides the module (uses shared Swift package utilities)
   - Check if documentation already exists in `<project>/dependency-docs/`
   - If not, generate documentation using `interfazzle` and cache it
   - Print the path to the documentation file on stdout

5. **Use the documentation** on the returned file path as needed

## Example

```bash
python3 ~/.claude/skills/swift-package-docs-generator/scripts/generate_docs.py "AppUpdating" ~/Code/MyProject/MyProject.xcodeproj
```

This returns a file path like:

```
/Users/yourname/Code/MyProject/dependency-docs/MyAppUpdater-1.35.md
```

Then read this file and provide the user with relevant information about the AppUpdating module.

## Important Notes

- The script outputs the documentation file path to stdout
- Status messages go to stderr (you can ignore these)
- If documentation already exists, it returns immediately with the cached path
- The project must have been built at least once (DerivedData must exist)
- Uses shared Swift package utilities from `~/.claude/skills/_shared/swift_packages.py`
