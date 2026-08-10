Leia em [English](getting-started.md).

# Primeiros passos

Você precisa de três coisas antes de escrever uma skill: um cliente de IA, o servidor MCP do Pipefy conectado a ele, e uma organização Pipefy onde dá para construir sem medo.

## 1. Escolha seu cliente

O Claude Code é o cliente recomendado e o mais testado. Cursor, Claude Desktop e Codex também funcionam.

## 2. Conecte o servidor MCP do Pipefy

**Claude Code, caminho mais rápido.** Instale este repositório como plugin. Ele traz um `.mcp.json` apontando para o servidor hospedado do Pipefy, então a conexão vem junto e não há Python local para instalar:

```text
/plugin marketplace add pipefy/mcp-builders
/plugin install mcp-builders@mcp-builders
```

Conclua o login no navegador quando for solicitado. Se você preferir configurar o servidor na mão, este é o comando equivalente:

```bash
claude mcp add --transport http --scope user --client-id pipefy-mcp pipefy https://mcp.pipefy.com/mcp
```

Já instalou o plugin `pipefy` do toolkit? Então você já tem o servidor. Não adicione um segundo, e pule para o passo 3.

**Cursor, Claude Desktop ou Codex.** Um script que instala a CLI, o servidor local e configura seu cliente:

```sh
curl -fsSL https://raw.githubusercontent.com/pipefy/ai-toolkit/main/install.sh | sh -s -- --client cursor
```

Troque `cursor` por `claude-desktop` ou `codex`. Depois rode `pipefy auth login`.

Registre exatamente um servidor MCP do Pipefy. Misturar o servidor hospedado com um local causa falhas confusas. Os outros caminhos de instalação, a autenticação por service account e a solução de problemas estão no [README do toolkit](https://github.com/pipefy/ai-toolkit#installation), que é a fonte da verdade. Esta página mostra só as duas rotas mais curtas.

## 3. Confirme que funcionou

Peça ao seu assistente algo que dependa do servidor, por exemplo:

> Liste os pipes da minha organização no Pipefy.

Se os seus pipes voltarem, está conectado. Se não, o toolkit tem um checklist de configuração que você pode entregar direto para o seu agente: [`skills/onboarding/pipefy-toolkit-setup/SKILL.md`](https://github.com/pipefy/ai-toolkit/blob/main/skills/onboarding/pipefy-toolkit-setup/SKILL.md).

## 4. Tenha onde construir

Você precisa de acesso Pipe Admin ou Org Admin. Conta gratuita basta. Perfis de convidado e papéis limitados não conseguem criar os pipes, fases e automações que a maioria das skills descreve.

Construa em uma organização onde um pipe quebrado não prejudica ninguém. Se a sua org de produção for a única que você tem, crie um pipe dedicado ao programa e mantenha sua skill apontada para ele.

## 5. Leia duas skills reais

Antes de escrever qualquer coisa, leia estas duas. Elas estão em produção no toolkit hoje, e são o padrão contra o qual sua submissão é medida:

- [pipefy-process-design](../skills/pipefy-process-design/SKILL.md), 121 linhas, uma skill de consultoria que ajuda a pessoa a desenhar um processo.
- [pipefy-process-intelligence](../skills/pipefy-process-intelligence/SKILL.md), 136 linhas, uma skill de análise que diagnostica um pipe existente e o melhora em rodadas.

Repare no que as duas têm em comum: elas dizem quando *não* devem ser acionadas, nomeiam as ferramentas exatas que usam, e cada passo é algo que um agente consegue de fato executar.

## 6. Escreva sua skill

Copie o [`template/SKILL.md`](../template/SKILL.md) e siga [Como escrever uma skill](writing-a-skill.pt-BR.md). Depois rode. Depois envie.

## Calendário do programa

| Etapa | Data |
|-------|------|
| Programa aberto | 27 de agosto a 18 de setembro |
| Webinar AMA ao vivo | 9 de setembro |
| Prazo final de submissão | 18 de setembro |
| Anúncio dos vencedores | 23 de setembro |

Trilha de conteúdo na Comunidade Pipefy: TODO-LINK-COMMUNITY-TRACK

Inscrição no webinar: TODO-LINK-WEBINAR-REGISTRATION

Pipefy Academy: TODO-LINK-ACADEMY
