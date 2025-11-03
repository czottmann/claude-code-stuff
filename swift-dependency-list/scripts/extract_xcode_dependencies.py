#!/usr/bin/env python3
"""
Extract Swift Package Manager dependencies and their modules from an Xcode project.
Reads Package.swift files from DerivedData/SourcePackages.
Usage: python3 extract_xcode_dependencies.py <path-to-xcodeproj> [--verbose]
"""

import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List
import glob


def find_package_resolved(xcodeproj_path: Path) -> Path:
    """Find the Package.resolved file in the Xcode project."""
    possible_locations = [
        xcodeproj_path
        / "project.xcworkspace"
        / "xcshareddata"
        / "swiftpm"
        / "Package.resolved",
        xcodeproj_path.parent
        / ".swiftpm"
        / "xcode"
        / "package.xcworkspace"
        / "xcshareddata"
        / "swiftpm"
        / "Package.resolved",
    ]

    for location in possible_locations:
        if location.exists():
            return location

    raise FileNotFoundError("Could not find Package.resolved file")


def find_derived_data_path(project_name: str) -> Path:
    """Find the DerivedData directory for this project."""
    derived_data_base = Path.home() / "Library" / "Developer" / "Xcode" / "DerivedData"

    if not derived_data_base.exists():
        raise FileNotFoundError(
            f"DerivedData directory not found at {derived_data_base}"
        )

    # Xcode replaces spaces with underscores in DerivedData directory names
    normalized_project_name = project_name.replace(" ", "_")

    # Find directories matching the project name
    pattern = f"{normalized_project_name}-*"
    matching_dirs = list(derived_data_base.glob(pattern))

    if not matching_dirs:
        raise FileNotFoundError(
            f"No DerivedData directory found for project '{project_name}'"
        )

    # Use the most recently modified one
    derived_data_dir = max(matching_dirs, key=lambda p: p.stat().st_mtime)

    source_packages = derived_data_dir / "SourcePackages" / "checkouts"

    if not source_packages.exists():
        raise FileNotFoundError(
            f"SourcePackages/checkouts not found in {derived_data_dir}"
        )

    return source_packages


def parse_package_resolved(resolved_path: Path) -> List[Dict]:
    """Parse Package.resolved to get list of dependencies."""
    with open(resolved_path, "r") as f:
        data = json.load(f)

    # Handle different Package.resolved formats (version 2 and 3)
    if "pins" in data:
        return data["pins"]
    elif "object" in data and "pins" in data["object"]:
        return data["object"]["pins"]
    else:
        raise ValueError("Unknown Package.resolved format")


def extract_package_info(pin: Dict) -> Dict:
    """Extract package name and repository URL from a pin entry."""
    # Handle both v2 and v3 formats
    if "package" in pin:
        name = pin["package"]
    elif "identity" in pin:
        name = pin["identity"]
    else:
        name = "Unknown"

    if "repositoryURL" in pin:
        url = pin["repositoryURL"]
    elif "location" in pin:
        url = pin["location"]
    else:
        url = None

    version = pin.get("state", {}).get("version") or pin.get("state", {}).get(
        "revision", "unknown"
    )

    return {"name": name, "url": url, "version": version}


def find_package_swift_in_derived_data(
    checkouts_dir: Path, package_identity: str
) -> Path:
    """Find Package.swift for a given package in DerivedData checkouts."""
    # Try exact match first
    package_dir = checkouts_dir / package_identity
    if package_dir.exists():
        package_swift = package_dir / "Package.swift"
        if package_swift.exists():
            return package_swift

    # Try case-insensitive search
    for subdir in checkouts_dir.iterdir():
        if subdir.is_dir() and subdir.name.lower() == package_identity.lower():
            package_swift = subdir / "Package.swift"
            if package_swift.exists():
                return package_swift

    return None


def read_package_swift(package_swift_path: Path, verbose: bool = False) -> str:
    """Read Package.swift content from local file."""
    try:
        with open(package_swift_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        if verbose:
            print(f"Warning: Could not read {package_swift_path}: {e}", file=sys.stderr)
        return None


def parse_package_name_from_package_swift(content: str) -> str:
    """Extract the actual package name from Package.swift content."""
    if not content:
        return None

    # Match Package(name: "PackageName", ...) with DOTALL to handle multi-line
    package_name_pattern = r'Package\s*\([^)]*?name\s*:\s*"([^"]+)"'
    match = re.search(package_name_pattern, content, re.DOTALL)

    if match:
        return match.group(1)

    return None


def parse_targets_from_package_swift(content: str) -> List[str]:
    """Extract target names from Package.swift content."""
    if not content:
        return []

    targets = []

    # Match .target patterns
    # .target(name: "TargetName", ...)
    target_pattern = r'\.target\s*\(\s*name\s*:\s*"([^"]+)"'
    targets.extend(re.findall(target_pattern, content))

    # Also match .executableTarget patterns
    executable_target_pattern = r'\.executableTarget\s*\(\s*name\s*:\s*"([^"]+)"'
    targets.extend(re.findall(executable_target_pattern, content))

    # Match .testTarget patterns (optional, but sometimes useful)
    # test_target_pattern = r'\.testTarget\s*\(\s*name\s*:\s*"([^"]+)"'
    # targets.extend(re.findall(test_target_pattern, content))

    return targets


def generate_json(dependencies: List[Dict]) -> str:
    """Generate JSON formatted output of dependencies and their targets."""
    output = {}

    for dep in dependencies:
        output[dep["name"]] = {
            "version": dep["version"],
            "repo": dep["url"] if dep["url"] else None,
            "exported_modules": sorted(dep["targets"]) if dep["targets"] else [],
        }

    return json.dumps(output, indent=2, ensure_ascii=False)


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
        print(f"Error: {xcodeproj_path} does not exist")
        sys.exit(1)

    try:
        # Extract project name from .xcodeproj
        project_name = xcodeproj_path.stem

        # Find and parse Package.resolved
        resolved_path = find_package_resolved(xcodeproj_path)
        if verbose:
            print(f"Found Package.resolved at: {resolved_path}", file=sys.stderr)

        pins = parse_package_resolved(resolved_path)
        if verbose:
            print(f"Found {len(pins)} dependencies", file=sys.stderr)

        # Find DerivedData checkouts directory
        try:
            checkouts_dir = find_derived_data_path(project_name)
            if verbose:
                print(f"Found package checkouts at: {checkouts_dir}", file=sys.stderr)
        except FileNotFoundError as e:
            if verbose:
                print(f"Warning: {e}", file=sys.stderr)
                print(
                    "Will not be able to extract module information.", file=sys.stderr
                )
            checkouts_dir = None

        dependencies = []

        for pin in pins:
            pkg_info = extract_package_info(pin)
            if verbose:
                print(f"Processing {pkg_info['name']}...", file=sys.stderr)

            targets = []
            actual_package_name = pkg_info["name"]  # Default to identity

            # Try to read Package.swift from DerivedData
            if checkouts_dir:
                package_swift_path = find_package_swift_in_derived_data(
                    checkouts_dir, pkg_info["name"]
                )
                if package_swift_path:
                    if verbose:
                        print(
                            f"  Found Package.swift at: {package_swift_path}",
                            file=sys.stderr,
                        )
                    package_swift_content = read_package_swift(
                        package_swift_path, verbose
                    )

                    # Extract actual package name
                    parsed_name = parse_package_name_from_package_swift(
                        package_swift_content
                    )
                    if parsed_name:
                        actual_package_name = parsed_name
                        if verbose:
                            print(
                                f"  Package name: {actual_package_name}",
                                file=sys.stderr,
                            )

                    targets = parse_targets_from_package_swift(package_swift_content)
                else:
                    if verbose:
                        print(
                            f"  Package.swift not found in checkouts", file=sys.stderr
                        )

            dependencies.append(
                {
                    "name": actual_package_name,
                    "version": pkg_info["version"],
                    "url": pkg_info["url"],
                    "targets": targets,
                }
            )

        # Generate and print JSON
        json_output = generate_json(dependencies)
        if verbose:
            print("\n" + "=" * 60, file=sys.stderr)
        print(json_output)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
