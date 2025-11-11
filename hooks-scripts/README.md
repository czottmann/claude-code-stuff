## Setup

1. Symlink this here folder to the user-level Claude folder using `mise run symlink-folders-to-claude`.
2. In `~/.claude/settings.json`, hook (heh) the scripts in this folder up like so:

```json
"hooks": {
  "SessionStart": [
    {
      "matcher": "startup|resume|clear|compact",
      "hooks": [
        {
          "type": "command",
          "command": "~/.claude/hooks-scripts/session-start.fish"
        }
      ]
    }
  ],
  "UserPromptSubmit": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "~/.claude/hooks-scripts/user-prompt-submit.fish"
        }
      ]
    }
  ],
  …
```
