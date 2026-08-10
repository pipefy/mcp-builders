Leia em [English](writing-a-skill.md).

# Como escrever uma skill

Uma skill é um manual de instruções escrito para um assistente de IA, não para uma pessoa. É nessa distinção que a maioria das submissões acerta ou erra.

Um documento de processo conta para um humano o que a empresa faz. Uma skill conta para o assistente o que fazer, em que ordem, com quais ferramentas, e como saber que deu certo. Se o seu texto continuaria fazendo sentido impresso e entregue a uma pessoa recém-contratada, provavelmente ele é um documento de processo.

## O formato de uma skill

```
submissions/<seu-usuario-github>/<nome-da-skill>/
├── SKILL.md
├── EVIDENCE.md
└── assets/          # prints opcionais
```

O `SKILL.md` começa com frontmatter YAML e depois usa um conjunto fixo de seções. O validador cobra o frontmatter e os títulos das seções, então copie o [`template/SKILL.md`](../template/SKILL.md) em vez de começar de um arquivo em branco.

## Frontmatter

```yaml
---
name: aprovacao-de-notas-fiscais
description: >
  Use esta skill quando a pessoa quiser construir ou corrigir um processo de
  aprovação de notas fiscais em várias etapas no Pipefy, incluindo roteamento
  por valor e as automações que movem o card entre níveis de aprovação.
tags: [pipefy, financeiro, aprovacoes, automacoes]
---
```

- `name` precisa ser idêntico ao nome da sua pasta. Isso é verificado.
- `description` é a linha mais importante do arquivo. O assistente lê essa linha para decidir se carrega a sua skill, então escreva como condição de gatilho, não como resumo. "Use esta skill quando a pessoa pedir para..." funciona melhor que "Esta skill trata de...".
- `tags` são em minúsculas, e a primeira é `pipefy`.

## As seções obrigatórias

**When to use.** Liste as intenções que devem acionar a skill e, em seguida, liste o que *não* deve acioná-la. A lista negativa importa tanto quanto a positiva. Veja como a [pipefy-process-design](../skills/pipefy-process-design/SKILL.md) abre: a primeira tabela dela é dedicada a explicar quando ela deve ser ignorada.

**Prerequisites.** O que precisa existir antes do passo um. Nível de acesso, IDs, um pipe já criado, uma integração conectada.

**Tools needed.** Uma tabela das tools MCP que a skill chama. O validador não confere a grafia, mas nome errado é pego na revisão e custa pontos no critério de uso correto do MCP. Pegue os nomes no [toolkit](https://github.com/pipefy/ai-toolkit) ou no seu próprio transcript depois de rodar a skill.

**Steps.** Numerados, em ordem, executáveis. Cada passo diz o que fazer e por quê. Inclua a chamada de ferramenta de verdade. Um passo como "configurar as regras de aprovação" não é executável. Um passo como "criar uma condição de campo na fase de Aprovação para que cards acima de 10.000 sigam para a fase de Diretoria, usando `create_field_condition`" é.

**Success criteria.** Como qualquer pessoa verifica que a skill funcionou, em fatos observáveis. "O pipe tem quatro fases e a automação dispara quando o card entra em Revisão", e não "o processo roda de forma fluida".

**Failure modes.** O que costuma quebrar e o que fazer a respeito. É a seção que separa quem rodou a skill de quem imaginou a skill.

O `See also` é opcional. Use para linkar skills relacionadas em vez de copiar o conteúdo delas.

## Um trecho comentado

```markdown
## Steps

1. **Criar o esqueleto do pipe**: construa as quatro fases antes de qualquer
   campo, porque condições de campo precisam que a fase de destino exista.

   ```
   create_pipe name="Aprovação de Notas" organization_id=<org_id>
   create_phase pipe_id=<pipe_id> name="Recebidas"
   create_phase pipe_id=<pipe_id> name="Análise do Gestor"
   ```

2. **Adicionar o campo de valor ao formulário inicial**: o roteamento depende
   dele, então precisa estar preenchido antes de o card entrar no fluxo.

   ```
   create_phase_field phase_id=<start_form_id> type="currency" label="Valor da nota"
   ```
```

Três coisas acontecem aí. Todo passo dá um motivo, não só uma ação. A ordem importa, e o texto diz por quê. As chamadas usam placeholders como `<pipe_id>` em vez de IDs reais, o que é ao mesmo tempo regra de segurança e o que torna a skill reaproveitável.

## Tamanho

Mire no tamanho das skills de referência, que têm 121 e 136 linhas. Se o seu processo realmente precisa de mais, use o espaço. Acima de 500 linhas o validador emite um aviso e a gente conversa na revisão, mas não reprova a submissão. Não infle uma skill para parecer completa. Enchimento custa pontos em praticidade.

## Regras de segurança

Nunca inclua token, chave de API, ID real de organização ou pipe, nome de cliente ou dado pessoal. Use placeholders. Submissão com credencial é fechada sem revisão, e o validador procura pelos padrões mais comuns.

## EVIDENCE.md

Curto e concreto. Copie o [`template/EVIDENCE.md`](../template/EVIDENCE.md) e responda quatro coisas:

1. **O problema.** O que era doloroso, manual ou lento antes.
2. **O que a skill construiu.** O pipe, as fases, as automações ou a análise que ela produziu.
3. **A prova.** Um print do resultado no Pipefy, ou o transcript do seu assistente executando a skill. Coloque imagens em `assets/` e linke.
4. **O que você teve que corrigir.** O que deu errado na primeira execução e como você mudou a skill. É o parágrafo mais útil que você pode escrever, e é o que soa crível de um jeito que nenhum outro soa.

A evidência vale 15 por cento sozinha, e também é o único jeito de um jurado avaliar os 30 por cento de impacto no processo. Uma skill sem evidência se limita, na prática, a menos da metade dos pontos disponíveis.

## Erros comuns

**Escrever para humano.** Texto corrido sobre como a área funciona, sem nenhum passo executável.

**Uma description que é um título.** `description: Aprovação de notas` não dá ao assistente nada com que decidir.

**Passos sem ferramenta.** Se nenhuma tool MCP aparece em lugar nenhum da skill, ela não está usando o MCP.

**Nunca ter rodado.** Dá para perceber. Skill que nunca foi executada não tem seção de failure modes que valha a leitura, e seus passos pulam a dependência chata que quebra tudo.

**Copiar uma skill existente do toolkit.** Partir de uma delas é ótimo e bem-vindo. Renomear uma delas é submissão fechada.

## Idioma

Inglês é preferencial, porque o toolkit é em inglês e a promoção fica mais simples. Português é aceito e não é penalizado. Se uma skill em português for selecionada, a tradução fica com a gente.
