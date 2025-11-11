#!/usr/bin/env fish
# SessionStart hook for skills use

set SCRIPT_DIR (cd (dirname (status current-filename)) && pwd)

# Read using-superpowers content
set using_skills_content (cat ../skills/superpowers:using-superpowers/SKILL.md 2>&1 || echo "Error reading superpowers:using-superpowers skill")
set additional_context "<EXTREMELY_IMPORTANT>You have skills. **Below is the full content of your 'superpowers:using-superpowers' skill - your introduction to using skills. For all other skills, use the 'Skill' tool:**\n$using_skills_content</EXTREMELY_IMPORTANT>"

# Output context injection as JSON
jq --arg ctx "$additional_context" \
    --null-input \
    --raw-output \
    '{
        hookSpecificOutput: {
          hookEventName: "SessionStart",
          additionalContext: $ctx
        }
      }'

exit 0
