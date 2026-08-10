Read this in [Português (BR)](README.pt-BR.md).

# MCP Builders by Pipefy

A program for the people who build processes in Pipefy to write the skills that teach an AI assistant to build them too.

A skill is a set of instructions that tells an AI assistant how to work inside Pipefy: when to act, how to act, and which tools to use. If you run processes in Pipefy every day, you already know what works. This program turns that knowledge into something anyone can reuse.

Submit your skill here. The selected ones are published in the official [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit) with you credited as a co-author of the commit.

## Program at a glance

| Milestone | Date |
|-----------|------|
| Invitations open | August 17 |
| Program runs | August 27 to September 18 |
| Live AMA webinar | September 9 |
| Submission deadline | September 18 |
| Winners announced | September 23 |

Registration: [use.pipefy.com/mcp-builders](https://use.pipefy.com/mcp-builders)

## What you get

- **A contributor badge.** Everyone whose submission is accepted receives the "MCP Builder by Pipefy" badge, shareable on LinkedIn.
- **Public listing.** Every accepted skill is listed in [SUBMISSIONS.md](SUBMISSIONS.md) with your name and profile.
- **Prizes for the ten best skills**, judged against the [public rubric](docs/judging.md):
  - If you are not a Pipefy customer: one year of the Business plan.
  - If you are already a customer: 1,000 AI credits per month for one year.
- **Credit in the official repository.** Selected skills are promoted into the Pipefy AI Toolkit, and you are added as co-author of the commit that publishes them.

## How to participate

**1. Get set up in two commands.** In Claude Code:

```text
/plugin marketplace add pipefy/mcp-builders
/plugin install mcp-builders@mcp-builders
```

That connects the Pipefy MCP server and installs the two reference skills, so you can start driving Pipefy from your assistant right away. Complete the browser login when prompted. On another client, or if you want the full local tool surface with the CLI, follow [Getting started](docs/getting-started.md) instead.

**2. Build and test your skill in the toolkit.** Copy the [skill template](template/SKILL.md), write your instructions, and run them for real against a Pipefy organization you control. A skill that has never run is not a skill.

**3. Post it here.** Two ways, pick whichever fits you:

- **Form (recommended if you are not a developer).** Open a [skill submission issue](../../issues/new?template=submit-skill.yml) and paste your content into the fields. We turn it into a pull request for you, with your authorship preserved.
- **Pull request (if you are comfortable with git).** Fork this repository, create `submissions/<your-github-handle>/<skill-name>/`, and open a pull request. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## What goes in a submission

```
submissions/<your-github-handle>/<skill-name>/
├── SKILL.md       # the skill itself, in the template format
└── EVIDENCE.md    # proof it ran, and the process problem it solves
```

`SKILL.md` follows the [template](template/SKILL.md), which is the same format used by the skills already shipping in the Pipefy AI Toolkit. `EVIDENCE.md` is short: the problem, what the skill built in Pipefy, and a screenshot or transcript of it running. Evidence is 15 percent of your score, and it is what separates a skill that works from a skill that reads well.

Two real skills are included as reference: [pipefy-process-design](skills/pipefy-process-design/SKILL.md) and [pipefy-process-intelligence](skills/pipefy-process-intelligence/SKILL.md). Both ship in the toolkit today.

## How submissions are judged

| Criterion | Weight |
|-----------|--------|
| Process impact | 30% |
| Practicality and reproducibility | 25% |
| Correct use of the MCP | 20% |
| Evidence that it ran | 15% |
| Reusability by other companies | 10% |

The full rubric, including what disqualifies a submission, is public in [docs/judging.md](docs/judging.md). Read it before you write. It is the same rubric used to pick the ten winners.

## Where things live

| You want to | Go to |
|-------------|-------|
| Install the MCP server, CLI, or SDK | [pipefy/ai-toolkit](https://github.com/pipefy/ai-toolkit) |
| Learn the skill format | [docs/writing-a-skill.md](docs/writing-a-skill.md) |
| Register for the program | [use.pipefy.com/mcp-builders](https://use.pipefy.com/mcp-builders) |
| Post your skill | [Submission issue](../../issues/new?template=submit-skill.yml) or a pull request here |
| Ask a question | [Discussions](../../discussions) or an [issue](../../issues/new?template=question.yml) |

This repository holds the program and the submissions. The plugin here is a shortcut that wires up the hosted MCP server and the reference skills. All the actual code, the server, the CLI, and the SDK, lives in the [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit).

### Prefer to work only in the toolkit?

That works. Install the toolkit plugin instead and use this repository as reference:

```text
/plugin marketplace add pipefy/ai-toolkit
/plugin install pipefy
```

You get the full local tool surface, the `pipefy` CLI, and the whole skill catalog. Read [`skills/`](https://github.com/pipefy/ai-toolkit/tree/main/skills) there for more examples than the two here, write your skill in your own clone, and come back only to post it. Install one Pipefy MCP server, not both.

## Frequently asked questions

**Do I need to know how to program?** No. You need to know a process well enough to explain it step by step. The submission form exists so that git is not a requirement.

**Do I need a paid Pipefy account?** No. Free accounts work. You do need Pipe Admin or Org Admin access to build what your skill describes.

**Can I submit more than one skill?** Yes. Each one is judged on its own.

**Can I write in Portuguese?** Yes. English is preferred because the toolkit is in English, but Portuguese submissions are accepted and we handle the translation when a skill is promoted.

**Who owns my skill?** You wrote it, and you are credited wherever it appears. Contributions to this repository are published under [Apache 2.0](LICENSE), the same license as the toolkit.

**Do Pipefy employees participate?** They can contribute skills, but they are not eligible for prizes.

## Language

The README, the contributing guide, and everything under `docs/` are maintained in English and Portuguese, as `.md` and `.pt-BR.md` pairs kept in sync. The issue and pull request templates carry both languages in the same file.

## Code of conduct and license

Participation is covered by our [Code of Conduct](CODE_OF_CONDUCT.md). Content in this repository is licensed under [Apache 2.0](LICENSE).
