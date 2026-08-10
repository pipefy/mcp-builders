Read this in [Português (BR)](CONTRIBUTING.pt-BR.md).

# How to submit a skill

There are two paths. Both end in the same place, and neither is worth more points than the other.

## Before you start

Your skill has to run before you submit it. Install the MCP server from the [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), write your skill there, and use it against a real Pipefy organization you control. See [Getting started](docs/getting-started.md) if you have not set the toolkit up yet.

Never put a token, an API key, a real organization ID, a customer name, or personal data in a skill. Submissions containing credentials are closed without review. Use placeholders such as `<pipe_id>` instead.

## Path 1: the submission form

Use this if you are not comfortable with git. It is the shortest route.

1. Open a [skill submission issue](../../issues/new?template=submit-skill.yml).
2. Paste your `SKILL.md` into the skill field and fill in the evidence fields.
3. Submit. We convert your issue into a pull request and commit it with you as the author, so your GitHub profile shows up in the history.

You keep authorship. The only thing you give up is control over the commit message.

## Path 2: a pull request

Use this if you already work with git.

1. Fork this repository and create a branch.
2. Copy the template into your submission folder:

   ```bash
   mkdir -p submissions/<your-github-handle>/<skill-name>
   cp template/SKILL.md    submissions/<your-github-handle>/<skill-name>/SKILL.md
   cp template/EVIDENCE.md submissions/<your-github-handle>/<skill-name>/EVIDENCE.md
   ```

3. Write both files. The rules are in [Writing a skill](docs/writing-a-skill.md).
4. Open a pull request and fill in the description template.

## Folder and naming rules

```
submissions/<your-github-handle>/<skill-name>/
├── SKILL.md
├── EVIDENCE.md
└── assets/          # optional: screenshots referenced from EVIDENCE.md
```

- `<your-github-handle>` is your GitHub username, lowercase.
- `<skill-name>` is kebab-case and describes the action, for example `invoice-approval-flow` or `vendor-onboarding-audit`.
- The `name` in the `SKILL.md` frontmatter must match `<skill-name>` exactly. This is checked automatically.

## What the automated check verifies

Every pull request that touches `submissions/` runs a validator. It checks:

- the folder sits at `submissions/<handle>/<skill-name>/`
- `SKILL.md` and `EVIDENCE.md` both exist
- the frontmatter is valid YAML and has `name`, `description`, and `tags`
- `name` matches the folder name
- the required sections are present: When to use, Prerequisites, Tools needed, Steps, Success criteria, Failure modes
- no credentials or tokens appear in the files

It does not check whether the MCP tool names you reference are spelled correctly, and it does not fail your submission for length. A skill over 500 lines gets a warning, not a rejection. If your skill needs the space, use it, and we will discuss it in review.

You can run the same check locally:

```bash
python3 scripts/validate_submission.py submissions/<your-github-handle>/<skill-name>
```

## Review

We review every submission. Expect one of three outcomes:

- **Accepted.** It is merged, you are added to [SUBMISSIONS.md](SUBMISSIONS.md), and you receive the badge.
- **Changes requested.** Something is unclear, missing evidence, or would not reproduce. We say exactly what to fix, and you have until the deadline to fix it.
- **Closed.** Rare. Happens when a submission contains credentials, is a copy of an existing toolkit skill with no new contribution, or does not run.

Acceptance is not the same as winning. Everything accepted gets the badge and the listing. The ten prizes go to the highest scores on the [rubric](docs/judging.md).

## After the program

Selected skills are adapted to the Pipefy AI Toolkit format and published there, with you added as co-author of the commit. If your skill needs translation into English or an adjustment to pass the toolkit CI, we do that work and tell you what changed.

## Asking for help

Open a [question issue](../../issues/new?template=question.yml) or start a thread in [Discussions](../../discussions). The live AMA webinar on September 9 is also a good place to bring a half-finished skill.
