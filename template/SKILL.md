---
name: my-skill-name
description: >
  Use this skill when the user wants to [trigger condition]. Write this as
  a condition, not a summary: the assistant reads this line to decide whether
  to load the skill at all.
tags: [pipefy, domain, action]
---

# [Skill title]

[One or two sentences: what this skill does and when an agent should load it.]

---

## When to use

- [User intent or example phrase that should trigger this skill.]
- [Another trigger.]

Do not use this skill for:

- [Out of scope. Point to another approach or skill when relevant.]

## Prerequisites

- [Access level, for example Org Admin.]
- [IDs or objects that must exist first, for example an existing `<pipe_id>`.]
- [Any integration or configuration that has to be in place.]

## Tools needed

| Tool (MCP) | What it does here | Read-only |
|------------|-------------------|-----------|
| `create_pipe` | [Why this skill calls it.] | No |
| `get_pipe` | [Why this skill calls it.] | Yes |

## Steps

1. **[Step name]**: [what to do and why the order matters.]

   ```
   create_pipe name="[Name]" organization_id=<org_id>
   ```

2. **[Next step]**: [what to do and why.]

   ```
   create_phase pipe_id=<pipe_id> name="[Phase]"
   ```

## Success criteria

- [Observable outcome anyone can verify, for example: the pipe has four phases and the automation fires when a card enters Review.]

## Failure modes

| Symptom | Likely cause | Recovery |
|---------|--------------|----------|
| [Error or bad state] | [Cause] | [Fix or fallback] |

## See also

- [Related skill, if any.]
