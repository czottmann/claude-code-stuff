#!/usr/bin/env fish
# UserPromptSubmit hook for skills use

set SCRIPT_DIR (cd (dirname (status current-filename)) && pwd)

# Output context injection as JSON
echo '{
  hookSpecificOutput: {
    hookEventName: "UserPromptSubmit",
    additionalContext: "<EXTREMELY-IMPORTANT>Check this request against your list of skills, and if one or more apply, use them.</EXTREMELY-IMPORTANT>"
  }
}'

exit 0
