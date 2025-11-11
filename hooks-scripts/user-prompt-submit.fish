#!/usr/bin/env fish
# UserPromptSubmit hook for skills use

set SCRIPT_DIR (cd (dirname (status current-filename)) && pwd)

# Output context injection as JSON
echo '{
  hookSpecificOutput: {
    hookEventName: "UserPromptSubmit",
    additionalContext: "<IMPORTANT>Remember to use relevant skills</IMPORTANT>"
  }
}'

exit 0
