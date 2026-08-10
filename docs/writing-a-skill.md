Read this in [Português (BR)](writing-a-skill.pt-BR.md).

# Writing a skill

A skill is an instruction manual written for an AI assistant, not for a person. That single distinction is where most submissions succeed or fail.

A process document tells a human what the company does. A skill tells an assistant what to do, in what order, with which tools, and how to know it worked. If your text would still make sense printed and handed to a new hire, it is probably a process document.

## The shape of a skill

```
submissions/<your-github-handle>/<skill-name>/
├── SKILL.md
├── EVIDENCE.md
└── assets/          # optional screenshots
```

`SKILL.md` opens with YAML frontmatter and then uses a fixed set of sections. The validator enforces the frontmatter and the section headings, so copy [`template/SKILL.md`](../template/SKILL.md) rather than starting from a blank file.

## Frontmatter

```yaml
---
name: invoice-approval-flow
description: >
  Use this skill when the user wants to build or fix a multi-step invoice
  approval process in Pipefy, including value-based routing and the
  automations that move a card between approval levels.
tags: [pipefy, finance, approvals, automations]
---
```

- `name` must match your folder name exactly. This is checked.
- `description` is the most important line in the file. The assistant reads it to decide whether to load your skill at all, so write it as a trigger condition, not as a summary. "Use this skill when the user asks to..." beats "This skill is about...".
- `tags` are lowercase, and the first one is `pipefy`.

## The required sections

**When to use.** List the user intents that should trigger the skill, and then list what should *not* trigger it. The negative list matters as much as the positive one. Look at how [pipefy-process-design](../skills/pipefy-process-design/SKILL.md) opens: it spends its first table explaining when to skip itself.

**Prerequisites.** What has to exist before step one. Access level, IDs, a pipe that is already created, a connected integration.

**Tools needed.** A table of the MCP tools the skill calls. The validator does not verify the spelling, but a wrong tool name is caught in review and costs you points on the "correct use of the MCP" criterion. Get the names from the [toolkit](https://github.com/pipefy/ai-toolkit) or from your own transcript after running the skill.

**Steps.** Numbered, ordered, executable. Each step says what to do and why. Include the actual tool call. A step like "configure the approval rules" is not executable. A step like "create a field condition on the Approval phase so cards over 10,000 route to the Director phase, using `create_field_condition`" is.

**Success criteria.** How anyone can verify the skill worked, stated as observable facts. "The pipe has four phases and the automation fires when a card enters Review", not "the process runs smoothly".

**Failure modes.** What tends to break and what to do about it. This is the section that separates someone who ran the skill from someone who imagined it.

`See also` is optional. Use it to link related skills instead of copying their content.

## An annotated fragment

```markdown
## Steps

1. **Create the pipe skeleton**: build the four phases before any field,
   because field conditions need the target phase to exist.

   ```
   create_pipe name="Invoice Approval" organization_id=<org_id>
   create_phase pipe_id=<pipe_id> name="Received"
   create_phase pipe_id=<pipe_id> name="Manager Review"
   ```

2. **Add the value field to the start form**: routing depends on it, so it
   must be filled before the card enters the flow.

   ```
   create_phase_field phase_id=<start_form_id> type="currency" label="Invoice amount"
   ```
```

Three things are happening there. Every step gives a reason, not just an action. The order is load bearing and the text says why. The tool calls use placeholders such as `<pipe_id>` instead of real IDs, which is both a security rule and what makes the skill reusable.

## Length

Aim for the size of the reference skills, which are 121 and 136 lines. If your process genuinely needs more, take the room. Over 500 lines the validator prints a warning and we talk about it in review, but it does not reject your submission. Do not pad a skill to look thorough. Padding costs you on practicality.

## Security rules

Never include a token, an API key, a real organization or pipe ID, a customer name, or personal data. Use placeholders. Submissions containing credentials are closed without review, and the validator scans for the common patterns.

## EVIDENCE.md

Short and concrete. Copy [`template/EVIDENCE.md`](../template/EVIDENCE.md) and answer four things:

1. **The problem.** What was painful, manual, or slow before.
2. **What the skill built.** The pipe, phases, automations, or analysis it produced.
3. **Proof.** A screenshot of the result in Pipefy, or the transcript of your assistant executing the skill. Put images in `assets/` and link them.
4. **What you had to fix.** What went wrong on the first run and how you changed the skill. This is the most useful paragraph you can write, and it reads as credible in a way nothing else does.

Evidence is 15 percent of the score on its own, and it is also the only way a judge can assess the 30 percent that goes to process impact. A skill with no evidence effectively caps itself at less than half the available points.

## Common mistakes

**Writing for a human.** Prose about how the department operates, with no executable step.

**A description that is a title.** `description: Invoice approval` gives the assistant nothing to decide with.

**Steps with no tools.** If no MCP tool appears anywhere in the skill, it is not using the MCP.

**Never running it.** It shows. Skills that were never executed have no failure modes section worth reading, and their steps skip the boring dependency that breaks everything.

**Copying an existing toolkit skill.** Building on one is fine and welcome. Renaming one is a closed submission.

## Language

English is preferred, because the toolkit is in English and promotion is simpler. Portuguese is accepted and is not penalized. If a Portuguese skill is selected, we translate it.
