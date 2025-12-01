---
name: using-xcode
description: Use this before running `xcodebuild` or working with Xcode - tells you the specifics of how we use Xcode and its tools
---

## Building Xcode projects

When running Xcode builds, use the `xcodebuild-wrapper` script to automatically capture build data with Argus. Wrapper accepts the same arguments as `xcodebuild` itself.

### 1. Run builds with the wrapper script

```bash
xcodebuild-wrapper -scheme "Actions For Obsidian (macOS)" -destination "platform=macOS"
```

The wrapper automatically:

- Sets up `XCBBUILDSERVICE_PATH` for Argus integration
- Handles scheme names with parentheses correctly

**Location**: `~/.claude/skills/using-xcode/xcodebuild-wrapper`

### 2. Query build results using the session ID

```bash
argus trace summary --build latest
argus trace errors --build latest
argus trace slowest-targets --build latest --limit 5
argus trace bottlenecks --build latest
```

Or use "latest" to query the most recent build:

```bash
argus trace summary --build latest
```

### 3. Use `--json` flag for programmatic access

```bash
argus trace summary --build latest --json
```

### Usage

Run `argus trace --help` to discover all available commands.
