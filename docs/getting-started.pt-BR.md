Leia em [English](getting-started.md).

# Primeiros passos

Você precisa de três coisas antes de escrever uma skill: um cliente de IA, o servidor MCP do Pipefy conectado a ele, e uma organização Pipefy onde dá para construir sem medo.

## 1. Instale o toolkit

Tudo sobre instalação vive no [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit#installation), e só lá. São cinco caminhos de instalação, e o time mantém todos atualizados. Esta página não repete nenhum deles, porque uma cópia ficaria desatualizada e te deixaria depurando a instrução errada.

O Claude Code é o cliente recomendado e o mais testado. Cursor, Claude Desktop e Codex também funcionam.

Se você quer a rota mais curta e está no Claude Code, o servidor hospedado não exige Python local:

```bash
claude mcp add --transport http --scope user --client-id pipefy-mcp pipefy https://mcp.pipefy.com/mcp
```

Conclua o login no navegador quando for solicitado. Todo o resto, incluindo a instalação local com a CLI `pipefy` e o conjunto completo de ferramentas, está no README do toolkit.

Registre exatamente um servidor MCP do Pipefy. Misturar o servidor hospedado com um local causa falhas confusas.

## 2. Confirme que funcionou

Peça ao seu assistente algo que dependa do servidor, por exemplo:

> Liste os pipes da minha organização no Pipefy.

Se os seus pipes voltarem, está conectado. Se não, o toolkit tem um checklist de configuração que você pode entregar direto para o seu agente: [`skills/onboarding/pipefy-toolkit-setup/SKILL.md`](https://github.com/pipefy/ai-toolkit/blob/main/skills/onboarding/pipefy-toolkit-setup/SKILL.md).

## 3. Tenha onde construir

Você precisa de acesso Pipe Admin ou Org Admin. Conta gratuita basta. Perfis de convidado e papéis limitados não conseguem criar os pipes, fases e automações que a maioria das skills descreve.

Construa em uma organização onde um pipe quebrado não prejudica ninguém. Se a sua org de produção for a única que você tem, crie um pipe dedicado ao programa e mantenha sua skill apontada para ele.

## 4. Leia duas skills reais

Antes de escrever qualquer coisa, leia estas duas. Elas estão em produção no toolkit hoje, e são o padrão contra o qual sua submissão é medida:

- [pipefy-process-design](../examples/pipefy-process-design/SKILL.md), 121 linhas, uma skill de consultoria que ajuda a pessoa a desenhar um processo.
- [pipefy-process-intelligence](../examples/pipefy-process-intelligence/SKILL.md), 136 linhas, uma skill de análise que diagnostica um pipe existente e o melhora em rodadas.

Repare no que as duas têm em comum: elas dizem quando *não* devem ser acionadas, nomeiam as ferramentas exatas que usam, e cada passo é algo que um agente consegue de fato executar.

O toolkit tem [muitas outras](https://github.com/pipefy/ai-toolkit/tree/main/skills), cobrindo automações, agentes de IA, relatórios, portais e tabelas. Leia as que ficam perto do seu processo.

## 5. Escreva sua skill

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
