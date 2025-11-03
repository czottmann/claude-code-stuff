---
name: swift-package-docs-generator
description: Generates API documentation for Swift package dependencies. Use when encountering unfamiliar import statements (e.g., "import ButtonKit", "import Defaults"), when exploring a dependency's API, or when the user asks about package documentation. Automatically resolves modules to packages and caches documentation for reuse.
allowed-tools: Bash, Read
---

Generates comprehensive API documentation for Swift package dependencies in Xcode projects.

## Quick Usage

When you encounter an unfamiliar module import, invoke this skill with the module name and project path. The skill will generate (or retrieve cached) documentation.

See `reference.md` for detailed usage instructions and examples.
