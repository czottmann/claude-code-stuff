---
name: making-plans
description: Use when design is complete and you need detailed implementation tasks - breaks epics into coarse-grained Beads issues with TDD guidance, exact file paths, and verification steps
---

# Making Plans

## Overview

Break epics into coarse-grained Beads issues that can be completed in one focused session. Each issue should represent a logical unit of work (e.g., "Implement auth middleware with TDD") with detailed guidance in the description.

Assume the implementing agent has zero context for the codebase. Document: which files to touch, code examples, testing approach, verification steps. DRY. YAGNI. TDD. Frequent commits.

**Announce at start:** "I'm using the `making-plans` skill to create implementation tasks."

### ⚠️ PREREQUISITE: Linear ↔ Beads Epic

Before breaking down tasks, you MUST have:

1. A Linear ticket (e.g., ZCO-123)
2. A Beads epic linked to that ticket via `--external-ref`

If either is missing, STOP and create them first. Use `brainstorming` skill if no design exists yet.

## Task Granularity

**Each Beads issue is one logical unit:**

- "Implement auth middleware with TDD" — issue
- "Add user model and migrations" — issue
- "Create login endpoint with validation" — issue

**Within each issue description, include step-by-step guidance:**

1. Write the failing test
2. Run it to verify failure
3. Implement minimal code to pass
4. Run tests to verify
5. Commit

## Beads Issue Structure

For each task, create a Beads issue:

```bash
bd create --type task --parent <epic-id> "Implement <component>"
```

**Issue description should include:**

````markdown
**Files:**

- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Steps:**

1. Write failing test:
   ```python
   def test_specific_behavior():
       result = function(input)
       assert result == expected
   ```

Run: `pytest tests/path/test.py::test_name -v` Expected: FAIL

2. Implement:
   ```python
   def function(input):
       return expected
   ```
   Run: `pytest tests/path/test.py::test_name -v` Expected: PASS

3. Commit:
   ```bash
   git commit -m "feat: add specific feature" -- tests/path/test.py src/path/file.py
   ```

**Verification:**

- [ ] Tests pass
- [ ] No type errors
- [ ] Committed
````

## Remember

- Exact file paths always
- Complete code examples (not "add validation")
- Exact commands with expected output
- Each task issue is a child of the epic
- Set dependencies with `bd dep` when tasks must be ordered

## Execution Handoff

After creating all issues:

```bash
bd list --parent <epic-id>
````

**"Tasks created under epic `<epic-id>`. Run `bd ready` to see unblocked work. Want me to start implementing?"**

When implementing:

- `bd update <id> --status in_progress` before starting
- `bd close <id>` when done
- `bd sync` after significant progress
