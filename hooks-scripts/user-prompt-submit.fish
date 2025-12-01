#!/usr/bin/env fish
# UserPromptSubmit hook for skills use

set additional_context "
<EXTREMELY-IMPORTANT>
🛑 STOP. Before responding, you MUST complete this checklist:

This is not negotiable. This is not optional. You cannot rationalize your way
out of this.

1. Check your list of available skills.
2. For EACH available skill, ask: \"Does this task involve [skill domain], could
   [skill] even marginally apply here?\" Err on the side of using skills. If you
   think there is even a 1% chance a skill might apply to what you are doing,
   you ABSOLUTELY MUST read the skill.

IF ANY SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

If NONE apply: State which skills you checked and why none fit.

No exceptions. No \"I already know this.\". No \"Let me just …\".
You MUST NOT skip a skill because because the task at hand seems simple.
</EXTREMELY-IMPORTANT>
"

# Output context injection as JSON
jq -n \
    --raw-output \
    --arg ctx "$additional_context" \
    '{
        hookSpecificOutput: {
            hookEventName: "UserPromptSubmit",
            additionalContext: $ctx
        }
    }'

exit 0
