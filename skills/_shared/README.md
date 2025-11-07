# Shared Utilities for Claude Code Skills

This directory contains shared Python libraries used by multiple Claude Code skills.

## swift_packages.py

Provides utilities for working with Swift Package Manager dependencies in Xcode projects.

### Key Functions

- **`find_package_resolved(xcodeproj_path)`** - Locates Package.resolved file
- **`find_derived_data_path(project_name)`** - Finds DerivedData/SourcePackages/checkouts directory
- **`parse_package_resolved(resolved_path)`** - Parses Package.resolved JSON
- **`extract_package_info(pin)`** - Extracts name, version, URL from a pin entry
- **`find_package_swift_in_derived_data(checkouts_dir, package_identity)`** - Locates Package.swift file
- **`find_package_directory_in_derived_data(checkouts_dir, package_identity)`** - Locates package directory
- **`read_package_swift(package_swift_path, verbose)`** - Reads Package.swift content
- **`parse_package_name_from_package_swift(content)`** - Extracts package name from Package.swift
- **`parse_targets_from_package_swift(content)`** - Extracts target names from Package.swift
- **`get_all_dependencies(xcodeproj_path, verbose)`** - Gets all dependencies with their metadata
- **`resolve_module_to_package(module_or_package, dependencies)`** - Resolves module name to package name

### Usage in Skills

Skills can import this library by adding to their scripts:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude/skills/_shared"))
from swift_packages import get_all_dependencies, resolve_module_to_package
```

### Used By

- **swift-dependency-list** - Maps Swift imports to packages
- **swift-package-docs-generator** - Generates API documentation for dependencies
