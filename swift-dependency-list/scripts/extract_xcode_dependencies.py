#!/usr/bin/env python3
"""
Extract Swift Package Manager dependencies and their modules from an Xcode project.
Reads Package.swift files from DerivedData/SourcePackages.
Usage: python3 extract_xcode_dependencies.py <path-to-xcodeproj> [--verbose]
"""

import sys
import json
import argparse
from pathlib import Path

# Import shared utilities
sys.path.insert(0, str(Path.home() / ".claude/skills/_shared"))
from swift_packages import get_all_dependencies


def main():
    parser = argparse.ArgumentParser(
        description="Extract Swift Package Manager dependencies and their modules from an Xcode project."
    )
    parser.add_argument("xcodeproj", help="Path to .xcodeproj file")
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output showing processing details",
    )

    args = parser.parse_args()

    xcodeproj_path = Path(args.xcodeproj)
    verbose = args.verbose

    if not xcodeproj_path.exists():
        print(f"Error: {xcodeproj_path} does not exist", file=sys.stderr)
        sys.exit(1)

    try:
        # Get all dependencies using shared library
        dependencies = get_all_dependencies(xcodeproj_path, verbose=verbose)

        # Generate and print JSON
        if verbose:
            print("\n" + "=" * 60, file=sys.stderr)
        print(json.dumps(dependencies, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
