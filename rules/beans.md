## Beans

You CAN NOT mark a bean as "completed" if it still contains unchecked todo items. Doing so is a failure state.

When showing beans titles in a TodoWrite for your human's benefit, prefix them with their IDs.

When creating an epic that has children, include the suggested implementation order to the epic.


### Committing to git

When committing, include the completed child bean in the commit together with the work.

**When working through children of an epic:** After completing a child bean …

- If the child bean doesn't need manual evaluation, commit right away.
- If the child bean needs manual evaluation, stop and ask your human for verification. Don't commit unless told to.

**When working on standalone beans that don't belong to epics:** Don't commit unless told to.
