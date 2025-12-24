#!/bin/bash

# Read JSON input from stdin and extract basic info in one jq call
IFS=$'\t' read -r current_dir model_name ctx_size ctx_input ctx_cache_create ctx_cache_read ctx_output < <(jq -r '[.workspace.current_dir, .model.display_name, .context_window.context_window_size, .context_window.current_usage.input_tokens // 0, .context_window.current_usage.cache_creation_input_tokens // 0, .context_window.current_usage.cache_read_input_tokens // 0, .context_window.current_usage.output_tokens // 0] | @tsv')

# Convert path to relative to home (~/...)
home_path="$HOME"
if [[ "$current_dir" == "$home_path"* ]]; then
    relative_path="~${current_dir#$home_path}"
else
    relative_path="$current_dir"
fi

# Get git branch if in a git repo
git_branch=""
if git -C "$current_dir" rev-parse --git-dir > /dev/null 2>&1; then
    branch_name=$(git -C "$current_dir" -c core.fileMode=false branch --show-current 2>/dev/null || echo "")
    if [ -n "$branch_name" ]; then
        # Green color for branch
        git_branch=$(printf " · \033[32m%s\033[0m" "$branch_name")
    fi
fi

# Helper function to colorize percentage based on thresholds
colorize_pct() {
    local pct=$1
    local text=$2

    # Remove % if present for numeric comparison
    local num_pct="${pct%%%}"

    if [ "$num_pct" -ge 75 ]; then
        # Orange (dim mode will make it visible)
        printf "\033[38;5;208m%s\033[0m" "$text"
    elif [ "$num_pct" -ge 50 ]; then
        # Yellow
        printf "\033[33m%s\033[0m" "$text"
    else
        # Muted gray (lighter than model name's dark gray)
        printf "\033[38;5;245m%s\033[0m" "$text"
    fi
}

# Calculate session (context window) usage percentage
session_info=""
if [ -n "$ctx_size" ] && [ "$ctx_size" != "null" ] && [ "$ctx_size" -gt 0 ] 2>/dev/null; then
    ctx_total=$((ctx_input + ctx_cache_create + ctx_cache_read + ctx_output))
    ctx_pct=$((ctx_total * 100 / ctx_size))
    session_info=$' \033[38;5;245m(\033[0m'"$(colorize_pct "$ctx_pct" "${ctx_pct}%")"$'\033[38;5;245m)\033[0m'
fi

# Get 5h usage (primary) and weekly usage (secondary)
# Data is generated periodically by a Keyboard Maestro macro
fivehours_info=""
week_info=""
usage_file="$HOME/.claude/usage-via-codexbar-cli.json"
if [ -f "$usage_file" ]; then
    IFS=$'\t' read -r primary_pct secondary_pct < <(jq -r '[.[0].usage.primary.usedPercent // "", .[0].usage.secondary.usedPercent // ""] | @tsv' "$usage_file" 2>/dev/null)

    if [ -n "$primary_pct" ] && [ "$primary_pct" != "null" ]; then
        fivehours_info=$' · \033[38;5;245m5h:\033[0m '"$(colorize_pct "$primary_pct" "${primary_pct}%")"
    fi
    if [ -n "$secondary_pct" ] && [ "$secondary_pct" != "null" ]; then
        week_info=$' · \033[38;5;245mw:\033[0m '"$(colorize_pct "$secondary_pct" "${secondary_pct}%")"
    fi
fi

# Output the status line with colored path (cyan), muted model name (dark gray)
printf "\033[36m%s\033[0m%s · \033[38;5;242m%s\033[0m%s%s%s" "$relative_path" "$git_branch" "$model_name" "$session_info" "$fivehours_info" "$week_info"
