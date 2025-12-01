---
name: using-xcode
description: Use this before running `xcodebuild` or working with Xcode - tells you the specifics of how we use Xcode and its tools
---

## Building Xcode projects

When running Xcode builds, use the `xcodebuild-wrapper` script to automatically capture build data with Argus.

### 1. Run builds with the wrapper script

```bash
xcodebuild-wrapper build -scheme "Actions For Obsidian (macOS)" -destination "platform=macOS"
```

The wrapper automatically:

- Generates a unique `BUILD_TRACE_ID`
- Sets up `XCBBUILDSERVICE_PATH` for Argus integration
- Handles scheme names with parentheses correctly
- Prints the `BUILD_TRACE_ID` to stderr for reference

**Location**: `~/.claude/skills/using-xcode/xcodebuild-wrapper`

### Manual alternative (if needed)

```bash
export BUILD_TRACE_ID=$(uuidgen)
XCBBUILDSERVICE_PATH=$(which argus) \
    BUILD_TRACE_ID=$BUILD_TRACE_ID \
    xcodebuild build -scheme MyScheme
```

### 2. Query build results using the session ID

```bash
argus trace summary --build $BUILD_TRACE_ID
argus trace errors --build $BUILD_TRACE_ID
argus trace slowest-targets --build $BUILD_TRACE_ID --limit 5
argus trace bottlenecks --build $BUILD_TRACE_ID
```

Or use "latest" to query the most recent build:

```bash
argus trace summary --build latest
```

### 3. Use `--json` flag for programmatic access

```bash
argus trace summary --build $BUILD_TRACE_ID --json
```

### Usage

Run `argus trace --help` to discover all available commands.
