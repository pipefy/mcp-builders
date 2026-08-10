Read this in [Português (BR)](getting-started.pt-BR.md).

# Getting started

You need three things before you can write a skill: an AI client, the Pipefy MCP server connected to it, and a Pipefy organization you can safely build in.

## 1. Pick your client

Claude Code is the recommended client and the best tested. Cursor, Claude Desktop, and Codex also work.

## 2. Connect the Pipefy MCP server

**Claude Code, fastest path.** One command, no local Python:

```bash
claude mcp add --transport http --scope user --client-id pipefy-mcp pipefy https://mcp.pipefy.com/mcp
```

Finish the browser login when prompted. If the client says it needs authentication, run `claude mcp login pipefy`.

**Cursor, Claude Desktop, or Codex.** One script that installs the CLI, the local server, and wires your client config:

```sh
curl -fsSL https://raw.githubusercontent.com/pipefy/ai-toolkit/main/install.sh | sh -s -- --client cursor
```

Swap `cursor` for `claude-desktop` or `codex`. Then run `pipefy auth login`.

Register exactly one Pipefy MCP server. Mixing the hosted server with a local one causes confusing failures. The other install paths, authentication with a service account, and troubleshooting are all in the [toolkit README](https://github.com/pipefy/ai-toolkit#installation), which is the source of truth. This page only shows the two shortest routes.

## 3. Check that it works

Ask your assistant something that requires the server, for example:

> List the pipes in my Pipefy organization.

If you get your pipes back, you are connected. If not, the toolkit ships a setup checklist you can hand straight to your agent: [`skills/onboarding/pipefy-toolkit-setup/SKILL.md`](https://github.com/pipefy/ai-toolkit/blob/main/skills/onboarding/pipefy-toolkit-setup/SKILL.md).

## 4. Get a place to build

You need Pipe Admin or Org Admin access. A free account is enough. Guest and limited roles cannot create the pipes, phases, and automations that most skills describe.

Build in an organization where a broken pipe does not hurt anyone. If your production org is the only one you have, create a dedicated pipe for the program and keep your skill pointed at it.

## 5. Read two real skills

Before writing anything, read these two. They ship in the toolkit today and they are the standard your submission is measured against:

- [pipefy-process-design](../examples/pipefy-process-design/SKILL.md), 121 lines, a consulting skill that helps a user design a process.
- [pipefy-process-intelligence](../examples/pipefy-process-intelligence/SKILL.md), 136 lines, an analyst skill that diagnoses an existing pipe and improves it in rounds.

Notice what they have in common: they say when *not* to fire, they name the exact tools they use, and every step is something an agent can actually execute.

## 6. Write your skill

Copy [`template/SKILL.md`](../template/SKILL.md) and follow [Writing a skill](writing-a-skill.md). Then run it. Then submit it.

## The program calendar

| Milestone | Date |
|-----------|------|
| Program runs | August 27 to September 18 |
| Live AMA webinar | September 9 |
| Submission deadline | September 18 |
| Winners announced | September 23 |

Learning track on the Pipefy Community: TODO-LINK-COMMUNITY-TRACK

Webinar registration: TODO-LINK-WEBINAR-REGISTRATION

Pipefy Academy: TODO-LINK-ACADEMY
