## Linear: Ticketing & Project Management

Tickets and projects are tracked in Linear (https://linear.app), a project management service. Use your Bash tool to call the `linearis` executable for communicating with Linear. Prior to your first use of `linearis`, run `linearis usage` once to learn how to use it.

The ticket numbers follow the format "ZCO-<number>". Always reference tickets by their number.

If you create a ticket, and it's not clear which project to assign it to, stop and ask the user. When creating subtasks, use the project of the parent ticket by default.

When you work on or make changes to a ticket, you must add your label to it. You'll find your label in the env var `AGENTS_CONSTRUCTION_KIT__LINEAR_LABEL`.

The return values of the `issues` commands contain an `embeds` array containing files uploaded to Linear (screenshots, documents, etc.) with signed download URLs and expiration timestamps. If a ticket or comment contains a embeds, fetch and view them as well. Use local caching when needed.

Never declare "Implementation Complete!" in a ticket unless explicitly told so.

### Updating tickets with progress

When the the status of a task in the ticket description has changed (task incomplete -> task done), update the description.

When updating a ticket with a progress report that is more than just a checkbox change, add that report as a ticket comment.

General rule: The ticket description is the starting point for planning. But when work is ongoing, I want to be able to retrace our steps by looking at the ticket and its comments.
