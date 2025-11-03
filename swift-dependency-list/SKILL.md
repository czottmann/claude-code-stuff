---
name: swift-dependency-list
description: Maps Swift import statements to their source packages. Use when encountering import statements (e.g., "import ButtonKit", "what package provides Defaults"), when needing package version information, or when the user asks which package exports a specific module. Extracts package metadata from Xcode DerivedData. Does not cover system frameworks.
allowed-tools: Bash
---

Generates a comprehensive mapping of Swift packages to their exported modules from Xcode's DerivedData.

## Quick Usage

When you need to identify which package provides a specific module, invoke this skill with the project path. It returns JSON mapping packages to their versions, repositories, and exported modules.

See `reference.md` for detailed usage instructions and examples.
