Read this in [Português (BR)](judging.pt-BR.md).

# How submissions are judged

This rubric is published before the program opens so you can write against it. It is the same rubric used to pick the ten winners.

Every accepted submission gets the contributor badge and a public listing regardless of score. The score only decides the prizes.

## Scoring

Each criterion is scored 1 to 5 and weighted. The final score is the weighted average, from 0 to 5.

| Criterion | Weight | Question being answered |
|-----------|--------|-------------------------|
| Process impact | 30% | Does this solve a real, recurring pain, and is the gain visible? |
| Practicality and reproducibility | 25% | Can someone else run this without guessing? |
| Correct use of the MCP | 20% | Right tools, right order, no unnecessary workarounds? |
| Evidence that it ran | 15% | Is there proof it actually executed in Pipefy? |
| Reusability by other companies | 10% | Does it work outside the author's specific setup? |

## What each score looks like

**Process impact, 30%.** A 5 solves a problem that costs a team real hours every week, and the skill makes the gain concrete. A 3 solves something real but narrow, or the gain is asserted without being shown. A 1 automates something that was not a problem.

**Practicality and reproducibility, 25%.** A 5 has ordered steps, explicit prerequisites, executable tool calls, and success criteria anyone can check. A 3 works but leaves gaps a reader has to fill from intuition. A 1 cannot be followed without asking the author what they meant.

**Correct use of the MCP, 20%.** A 5 uses the right tool for each action, in a dependency-safe order, and falls back to raw GraphQL only where no tool exists. A 3 works but takes a longer route than necessary or names tools imprecisely. A 1 barely touches the MCP, or the sequence would fail on a clean organization.

**Evidence that it ran, 15%.** A 5 shows the result in Pipefy plus a transcript, and describes what broke on the first attempt and how the skill changed. A 3 shows a screenshot with no context. A 1 has no evidence, and everything above it becomes a claim.

**Reusability by other companies, 10%.** A 5 uses placeholders, states its assumptions, and would work at a different company on the first read. A 3 needs light adaptation. A 1 is welded to one organization's field names and IDs.

## What disqualifies a submission

- Credentials, tokens, real organization or pipe IDs, customer names, or personal data in any file.
- A copy of a skill already in the Pipefy AI Toolkit with no new contribution.
- A skill that does not run.
- Submissions received after the deadline of September 18.

Disqualification is about the submission, not the person. Fix it before the deadline and resubmit.

## Who judges

Judging is done by Adrianno Esnarriaga, who leads the Pipefy AI Toolkit. Every submission is scored on all five criteria, and the ten highest weighted scores take the prizes.

Ties are broken by process impact first, then by evidence.

## Prizes

- **Not a Pipefy customer:** one year of the Business plan.
- **Already a customer:** 1,000 AI credits per month for one year.

Pipefy employees can contribute skills but are not eligible for prizes.

Winners are announced on September 23.

## After judging

Selected skills are promoted into the [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), adapted to its format and CI, with the author added as co-author of the publishing commit. Promotion is not limited to the ten winners. Any skill good enough to ship can be promoted.
