# Reference skills

These two skills are copies of skills shipping in the [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit/tree/main/skills). They are here so you can read the standard your submission is measured against without leaving the repository. The toolkit has [many more](https://github.com/pipefy/ai-toolkit/tree/main/skills), and reading the ones near your process is worth the detour.

| Skill | Lines | What it does |
|-------|-------|--------------|
| [pipefy-process-design](pipefy-process-design/SKILL.md) | 121 | Consulting mode: helps a user design a process, and explicitly refuses to fire when the user already has a spec. |
| [pipefy-process-intelligence](pipefy-process-intelligence/SKILL.md) | 136 | Analyst mode: diagnoses an existing pipe and improves it in rounds, showing results each round. |

Read them for the shape, not for the content. What to copy is the structure: a description written as a trigger condition, an explicit list of when *not* to use the skill, named tools, ordered steps with reasons, and verifiable success criteria.

Do not submit a renamed copy of either one. Building on top of them is welcome, and you should say so in your `EVIDENCE.md`.

The canonical versions live in the toolkit and may change there. If the two ever disagree, the toolkit is right.

Your own skill does not go here. Submissions go in [`submissions/`](../submissions), one folder per person. See [CONTRIBUTING.md](../CONTRIBUTING.md).
