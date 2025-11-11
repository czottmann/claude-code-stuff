## Swift: Building Xcode projects

Pipe `xcodebuild` output directly to `xcsift` to get clean, readable results for use by LLM:

```bash
xcodebuild [flags] 2>&1 | xcsift
```

Important: Always use `2>&1` to redirect STDERR to STDOUT. This ensures all compiler errors, warnings, and build output are captured, removing noise and providing clean, structured JSON output.
