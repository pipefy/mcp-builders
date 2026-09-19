---
name: pipefy-software-pipe
description: >
  Use this skill when the user wants to build, review, or improve a Pipefy pipe
  for a software development workflow (backlog, sprint, dev, QA, release). It
  guarantees that cards capture everything a team needs to actually build the
  software — clear requirements, testable acceptance criteria, and an enforced
  Definition of Ready and Definition of Done — so ambiguity is caught before code
  is written instead of turning into rework. Self-contained: the quality
  standards live in the skill, not in an external doc.
tags: [pipefy, software, backlog, requirements, definition-of-ready, quality-gate]
---

# Software Development Pipe

Design a Pipefy pipe so a card cannot advance into development without carrying the information a team needs to build the software correctly the first time. The goal is not "more fields" — it is **the right fields, required at the right phase**, so ambiguity is caught before code is written.

If your organization also keeps coding standards, engineering guidelines, or team conventions in a separate document, treat this skill's Definition of Ready / Definition of Done checklists as the *card-level enforcement* of those standards — link the card checklist to whatever standards doc you already maintain.

---

## Principle: capture at intake, gate at transitions

Two mistakes to avoid:

1. **Everything on the start form.** Requesters abandon 20-field forms or fill them with junk. Only ask upfront what a requester can genuinely answer.
2. **Nothing gated.** If any card can move into "In Development" regardless of content, the form is theater.

The fix: split information across phases and enforce a **Definition of Ready (DoR)** and **Definition of Done (DoD)** as required fields on the *entry* to the phase that needs them.

| Information | Who provides it | Where it lives |
|---|---|---|
| Problem / value / requester | Requester | Start form |
| Refined requirements + acceptance criteria | Product / analyst | "Refinement" phase (DoR gate) |
| Technical approach, risks, estimate | Dev / tech lead | "Refinement" / "Ready for Dev" |
| Test evidence, review, docs | Dev / QA | "In Development" → "Review" (DoD gate) |

---

## Reference flow

```
[Start form] ──► Backlog ──► Refinement ──► Ready for Dev ──► In Development ──► Code Review ──► QA / Testing ──► Ready for Release ──► Done
                                 │ (DoR gate)                       │                                 │ (DoD gate)
                                 ▼                                  ▼                                 ▼
                             Blocked ◄──────────────── (from any work phase) ─────────────────────────┘
```

- **Backlog** — item received, not yet prioritized.
- **Refinement** — detailed requirements, acceptance criteria written, estimate. **DoR is validated on exit.**
- **Ready for Dev** — prioritized queue; everything the dev needs is on the card.
- **In Development** — implementation.
- **Code Review** — peer review of the code.
- **QA / Testing** — functional and quality validation.
- **Ready for Release** — **DoD validated**, awaiting deploy.
- **Done** — delivered.
- **Blocked** — lateral phase for impediments; the card returns to its origin phase when unblocked.

> **Phase transition rules** (which phases a card can reach from another, including returns and the lateral Blocked) are configured in the **Pipefy UI** (Settings → Phases → *cards can be moved to*). Pipe/field tools create phases and fields; the flow arrows are UI-only.

---

## Start form — the minimum a requester can actually answer

Ask only what adds value at intake. Suggested fields (create in the UI or confirm with `get_start_form_fields`, keeping each `internal_id`):

| Field | Type | Required | Why |
|---|---|---|---|
| Request title | short_text | Yes | Card identity |
| Type | select (`Feature`, `Bug`, `Improvement`, `Tech debt`, `Spike`) | Yes | Routing and field template |
| Problem / objective description | long_text | Yes | The "why", not the "how" |
| Expected value / impact | long_text | Yes | Honest prioritization |
| Requester (email) | email | Yes | Notifications and follow-up |
| Suggested priority | select (`Low`, `Medium`, `High`, `Urgent`) | No | A signal; the call is the PO's |
| Desired date | date | No | An expectation, not a commitment |
| Attachments / evidence | attachment | No | Screenshots, logs, mockups |

For **Bug**, a conditional form (or triage phase) must also require: steps to reproduce, expected vs actual behavior, environment/version, and evidence (log/screenshot). A bug without reproduction steps is not actionable.

---

## Definition of Ready (DoR) — exit gate of Refinement

Before a card enters development, these fields must be filled (make them required on the **Refinement** phase, or as a mandatory checklist on the transition to **Ready for Dev**):

| Field | Type | Content |
|---|---|---|
| Detailed requirements | long_text | What to do; explicit scope and out-of-scope |
| Acceptance criteria | long_text / checklist | **Given/When/Then** format or a verifiable list |
| Business rules | long_text | Constraints, calculations, special cases |
| Dependencies | long_text / connection | Other cards, teams, services, APIs |
| Technical approach | long_text | Architecture / design decision (link an ADR if relevant) |
| Security impact | select + long_text | Touches auth / sensitive data / PII? If yes, a plan |
| Estimate | select (Fibonacci: 1,2,3,5,8,13) or hours | Relative size |
| Card's own "done" definition | checklist | The card-specific DoD |

**DoR checklist (all true to leave Refinement):**

- [ ] The problem and value are clear and unambiguous.
- [ ] Acceptance criteria are testable and written down.
- [ ] Dependencies identified and addressed (or flagged as blocking).
- [ ] Security impact assessed; if sensitive data is involved, a plan exists.
- [ ] Technical approach sketched and fits in one sprint (or was split).
- [ ] Estimate recorded.
- [ ] Test approach known (how this will be verified).

---

## Definition of Done (DoD) — exit gate to Release

Required fields/checklist on entry to **Ready for Release** (or exit from QA). These are self-contained engineering standards; adjust to your stack, but keep them enforced on the card rather than in a document nobody opens:

| DoD item | What "good" looks like |
|---|---|
| Code follows conventions | Consistent naming, ordered imports, small focused functions, no commented-out code |
| No hardcoded config or secrets | Values come from environment / settings, never literals in code |
| Typed error handling | No empty `catch {}`; structured logs; user vs system errors distinguished |
| Input validated and sanitized | No string-concatenated SQL; security headers set where applicable |
| Tests written and passing | Unit/integration cover new logic and edge cases; coverage ≥ 70% on new code |
| Code review approved | At least one reviewer signed off |
| Clean commit history | Conventional Commits; PR scoped to one responsibility, reasonably small |
| Documentation updated | API/architecture/README updated in the same PR as the change |
| Dependencies healthy | No unused deps; pinned/exact versions |
| Tests are deterministic | Pass in any order; no shared global state |

**DoD checklist (all true to move to Release):**

- [ ] Acceptance criteria met and demonstrated.
- [ ] Unit/integration tests passing; new-code coverage ≥ 70%.
- [ ] Code review approved; PR within size and commit conventions.
- [ ] No known vulnerabilities introduced; secrets kept out of code.
- [ ] Documentation and ADRs updated where the change requires it.
- [ ] No known regressions; feature flags / rollback defined if applicable.

---

## Field-type cheat sheet (Pipefy)

When creating fields via pipe tools (`create_pipe_field` / equivalents) or the UI, use types that force input quality:

| Need | Pipefy type | Note |
|---|---|---|
| Controlled short text | `select` / `radio_vertical` | Prefer enum over free text for taxonomy (Type, Priority) |
| Structured text | `long_text` | For requirements/criteria; put a template in the help text |
| Verifiable checklist | `checklist_vertical` | DoR/DoD as checkable items |
| Link to another card | `connector` (pipe relation) | Dependencies, epic ↔ story |
| Requester email | `email` | Needed for notifications |
| Estimate | `select` (Fibonacci) | Avoids arbitrary numbers |
| Evidence | `attachment` | Bug repro, mockups, logs |
| Dates | `date` / `due_date` | Desired date ≠ commitment |

**Rule:** every field that gates a transition must be **required on the phase** (Phase field settings), not just on the start form. Required start-form fields only cover intake.

---

## Build workflow (discover → structure → gate → verify)

Never guess phase, field, or pipe IDs — always discover them.

1. **Metadata** — `get_pipe(pipe_id)` for `uuid`, `phases[].id`, `phases[].name`.
2. **Start form** — `get_start_form_fields(pipe_id)`; create/adjust intake fields.
3. **Phase fields** — `get_phase_fields(phase_id)` per phase; add DoR fields to Refinement and DoD fields before Release, marking the required ones.
4. **Transitions** — configure the flow arrows in the UI (advances, returns, Blocked). Document the transition map in the setup card or the team README.
5. **Gates** — mark DoR/DoD fields required-on-phase; optionally add the AI intake gate (below).
6. **Verify** — move a test card end to end; confirm it **cannot** advance without the required fields and that checklists appear on the right phases.

---

## Optional: AI intake gate

Add an AI agent that reinforces card quality without relying on human discipline (see a dedicated Pipefy AI-agents guide for the full behavior schema):

- **Behavior 1 — Completeness triage (`card_created`):** the agent reads the start-form fields (description, value, type) and, via `update_card` with `inputMode: fill_with_ai`, writes a "Completeness analysis" field pointing out what is missing (e.g. "no acceptance criteria", "bug without repro steps"). Do not let the agent approve or move the card by itself — it **flags**, a human decides.
- **Behavior 2 — Acceptance-criteria draft (`manually_triggered`):** on a card button click, the agent proposes Given/When/Then criteria from the description into a draft field for the analyst to review.
- **Behavior 3 — Security notice (`field_updated` on Type/Description):** if it detects mentions of auth, PII, or sensitive data, it fills a "Security impact" field with a warning.

Modeling rules: `send_email_template` to notify; `update_card` requires `inputMode` on every field entry; **max 5 behaviors per agent**; validate with `validate_ai_agent_behaviors` before creating. **Consent:** only add the agent if the user asked for AI — otherwise suggest it and ask first.

---

## Type-specific card templates

Adjust required fields per **Type** (via conditional fields or distinct phases):

| Type | Extra required fields |
|---|---|
| Feature | Acceptance criteria, mockup/UX, API impact, test plan |
| Bug | Repro steps, expected vs actual, environment/version, evidence, severity |
| Improvement | Current baseline, measurable goal, success criterion |
| Tech debt | Risk of not doing it, affected area, refactor plan, ADR if it changes architecture |
| Spike | Question to answer, timebox, deliverable (document/decision) |

---

## Success criteria

- A card **cannot advance** into development without the DoR fields filled.
- Acceptance criteria exist and are testable before coding.
- DoD is a visible checklist on the card, aligned to the team's engineering standards.
- A test card traverses the whole flow and the gates block when they should.
- (If an agent exists) the completeness analysis appears on the card and reflects real gaps.

## Failure modes

- **Giant start form.** Requesters fill it with junk. Move "how" fields to Refinement; keep only "what/why" on the form.
- **Required only on the start form.** Those don't gate transitions. Make them required **on the phase** that needs them.
- **Free-floating free-text acceptance criteria.** Without a format they aren't testable. Standardize on Given/When/Then or a checklist.
- **DoD as an external doc.** Nobody opens it. Bring it in as a `checklist_vertical` on the Release phase.
- **Agent that approves on its own.** Loses human judgment and can hallucinate on empty fields. The agent flags; a person decides.
- **Transitions with no return/blocked path.** Cards get stuck or skip steps. Configure returns and the lateral Blocked in the UI.

---

## Suggestions to evolve this skill

Ideas to increase value if you expand later:

1. **Per-phase SLA + escalation.** A phase-entry date field plus an automation/agent that notifies when a card sits past its SLA.
2. **Git/PR sync.** Record the PR link and CI status on the card (via automation/webhook), closing the loop between the pipe and your commit conventions.
3. **Agile metrics.** Fields that feed lead time, cycle time, and throughput; a dashboard reading them for the team.
4. **Versioned card templates per Type.** Keep field templates as code/config to recreate the pipe reproducibly for new teams.
5. **DoR/DoD as a shared standard.** Extract the checklists into a standalone team document and reference it from both this pipe and code review, avoiding drift.
6. **RAG pre-fill.** If a knowledge base of past requests/ADRs exists, a data lookup / knowledge base on the agent can suggest requirements and risks from similar past demands.
