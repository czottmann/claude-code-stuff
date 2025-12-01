## Linear + Beads Integration

Linear is for human-visible project tracking. Beads is for agent implementation memory. Both systems
work together with bidirectional linking.

### Starting Work on a Linear Ticket

When beginning work on a Linear ticket (e.g., ZCO-123):

1. Run `bd list --title-contains ZCO-123 --type epic` to find an existing Beads epic
2. If none exists, create one automatically:
   ```
   bd create --type epic --external-ref ZCO-123 "Implement ZCO-123: <ticket title>"
   ```
3. All implementation sub-tasks go under this epic as child issues using `--parent <epic-id>`

### Discovering Work During Implementation

When you discover work that needs doing while implementing something else:

1. Always file a Beads issue with `--deps discovered-from:<current-issue-id>`
2. Never ignore discovered work just because you're tight on context
3. Label discovered issues appropriately for later triage

### When Discovered Work Needs a Linear Ticket

Create a Linear ticket for discovered work IF it:

- Affects scope or timeline of current work
- Requires human decision or approval
- Represents user-facing changes
- Is a security concern
- Is significant enough to track at project level

For purely technical implementation details (refactoring, test fixes, code cleanup), keep them in
Beads only with `--labels implementation-detail`.

### Querying Work

- `bd ready` — Find unblocked work to do next
- `bd list --title-contains ZCO-123` — All Beads issues for a Linear ticket
- `bd show <id>` — View issue details including dependencies

### Provenance for Context

When revisiting a Linear ticket that seems vague, use Beads to trace its origin:

- Find the Beads epic: `bd list --title-contains <ticket-id> --type epic`
- Use `discovered-from` deps to understand why work was filed
- This provides context that Linear alone cannot

### Sync Discipline

- Beads database lives in `.beads/issues.jsonl` (git-tracked)
- After significant Beads work, commit the JSONL changes
- Pull before starting sessions to get latest issue state
