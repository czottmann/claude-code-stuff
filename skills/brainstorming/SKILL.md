---
name: brainstorming
description: Use when creating or developing, before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Don't use during clear 'mechanical' processes
---

# Brainstorming Ideas Into Designs

## Overview

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

Start by understanding the current project context, then ask questions one at a time to refine the idea. Once you understand what you're building, present the design in small sections (200-300 words), checking after each section whether it looks right so far.

## The Process

**Understanding the idea:**

- Check out the current project state first (files, docs, recent commits)
- Ask questions one at a time to refine the idea
- Prefer multiple choice questions when possible, but open-ended is fine too
- Only one question per message - if a topic needs more exploration, break it into multiple questions
- Focus on understanding: purpose, constraints, success criteria

**Exploring approaches:**

- Propose 2-3 different approaches with trade-offs
- Present options conversationally with your recommendation and reasoning
- Lead with your recommended option and explain why

**Presenting the design:**

- Once you believe you understand what you're building, present the design
- Break it into sections of 200-300 words
- Ask after each section whether it looks right so far
- Cover: architecture, components, data flow, error handling, testing
- Be ready to go back and clarify if something doesn't make sense

## After the Design

### ⚠️ MANDATORY: Linear ↔ Beans Linking

BEFORE continuing, you MUST read your `issue-tracking-with-beans-and-linear` skill.

Every Beans epic MUST have a corresponding Linear ticket. Every Linear ticket MUST have a corresponding Beans epic. No exceptions.

**Capture the design:**

1. If no Linear ticket exists yet, create one first via `issue-tracking-with-linear` skill
2. Create the Beans epic with the Linear ticket reference:
   ```bash
   beans create "<linear-ticket-id>: <design-name>" --type epic --body "<description>" --no-edit
   ```
3. Put the validated design in the epic description

**Implementation (if continuing):**

- Ask: "Ready to break this into implementation tasks (calling the `making-plans` skill)?"
- Use `making-plans` skill

## Key Principles

- **One question at a time** - Don't overwhelm with multiple questions
- **Multiple choice preferred** - Easier to answer than open-ended when possible
- **YAGNI ruthlessly** - Remove unnecessary features from all designs
- **Explore alternatives** - Always propose 2-3 approaches before settling
- **Incremental validation** - Present design in sections, validate each
- **Be flexible** - Go back and clarify when something doesn't make sense
