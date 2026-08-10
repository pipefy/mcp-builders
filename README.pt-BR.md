Leia em [English](README.md).

# MCP Builders by Pipefy

Um programa para quem constrói processos no Pipefy escrever as skills que ensinam um assistente de IA a construí-los também.

Uma skill é um conjunto de instruções que diz a um assistente de IA como trabalhar dentro do Pipefy: quando agir, como agir e quais ferramentas usar. Quem usa o produto no dia a dia já sabe o que funciona. Este programa transforma esse conhecimento em algo que qualquer pessoa pode reaproveitar.

Sua skill é publicada aqui. As selecionadas vão para o repositório oficial do [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), com você creditado como coautor do commit.

## O programa em uma tabela

| Etapa | Data |
|-------|------|
| Início dos convites | 17 de agosto |
| Programa aberto | 27 de agosto a 18 de setembro |
| Webinar AMA ao vivo | 9 de setembro |
| Prazo final de submissão | 18 de setembro |
| Anúncio dos vencedores | 23 de setembro |

Inscrição: [use.pipefy.com/mcp-builders](https://use.pipefy.com/mcp-builders)

## O que você ganha

- **Selo de contribuidor.** Todo mundo que tiver a submissão aceita recebe o selo "MCP Builder by Pipefy" para compartilhar no LinkedIn.
- **Listagem pública.** Toda skill aceita entra no [SUBMISSIONS.md](SUBMISSIONS.md) com seu nome e seu perfil.
- **Prêmios para as dez melhores skills**, avaliadas pelo [rubric público](docs/judging.pt-BR.md):
  - Quem não é cliente Pipefy: 1 ano de plano Business.
  - Quem já é cliente: 1.000 AI credits por mês durante 1 ano.
- **Crédito no repositório oficial.** As skills selecionadas são levadas para o Pipefy AI Toolkit, e você entra como coautor do commit que as publica.

## Como participar

**1. Instale o toolkit.** O servidor MCP do Pipefy, a CLI e o catálogo de skills vivem no [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit#installation), que é de onde você instala e onde as instruções ficam atualizadas. Rota mais curta se você está no Claude Code:

```bash
claude mcp add --transport http --scope user --client-id pipefy-mcp pipefy https://mcp.pipefy.com/mcp
```

Outros clientes, a instalação local e a CLI estão em [Primeiros passos](docs/getting-started.pt-BR.md).

**2. Escreva e teste sua skill no toolkit.** Copie o [template de skill](template/SKILL.md), escreva suas instruções e rode de verdade em uma organização Pipefy que você controla. Skill que nunca rodou não é skill.

**3. Publique aqui.** São dois caminhos, escolha o que combina com você:

- **Formulário (recomendado se você não é pessoa desenvolvedora).** Abra uma [issue de submissão](../../issues/new?template=submit-skill.yml) e cole seu conteúdo nos campos. A gente transforma em pull request preservando sua autoria.
- **Pull request (se você já usa git).** Faça um fork deste repositório, crie `submissions/<seu-usuario-github>/<nome-da-skill>/` e abra o pull request. Detalhes em [CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md).

## O que compõe uma submissão

```
submissions/<seu-usuario-github>/<nome-da-skill>/
├── SKILL.md       # a skill em si, no formato do template
└── EVIDENCE.md    # a prova de que rodou, e o problema de processo que resolve
```

O `SKILL.md` segue o [template](template/SKILL.md), que é o mesmo formato das skills que já estão no Pipefy AI Toolkit. O `EVIDENCE.md` é curto: o problema, o que a skill construiu no Pipefy, e um print ou transcript da execução. A evidência vale 15 por cento da nota, e é o que separa uma skill que funciona de uma skill que só está bem escrita.

Duas skills reais entram como referência: [pipefy-process-design](examples/pipefy-process-design/SKILL.md) e [pipefy-process-intelligence](examples/pipefy-process-intelligence/SKILL.md). As duas estão em produção no toolkit hoje.

## Como as submissões são avaliadas

| Critério | Peso |
|----------|------|
| Impacto no processo | 30% |
| Praticidade e reprodutibilidade | 25% |
| Uso correto do MCP | 20% |
| Evidência de execução | 15% |
| Reusabilidade por outras empresas | 10% |

O rubric completo, incluindo o que desqualifica uma submissão, está público em [docs/judging.pt-BR.md](docs/judging.pt-BR.md). Leia antes de escrever. É o mesmo rubric usado para escolher as dez vencedoras.

## Onde fica cada coisa

| Se você quer | Vá para |
|--------------|---------|
| Instalar o servidor MCP, a CLI ou o SDK | [pipefy/ai-toolkit](https://github.com/pipefy/ai-toolkit) |
| Aprender o formato de skill | [docs/writing-a-skill.pt-BR.md](docs/writing-a-skill.pt-BR.md) |
| Se inscrever no programa | [use.pipefy.com/mcp-builders](https://use.pipefy.com/mcp-builders) |
| Publicar sua skill | [Issue de submissão](../../issues/new?template=submit-skill.yml) ou um pull request aqui |
| Tirar uma dúvida | [Discussions](../../discussions) ou uma [issue](../../issues/new?template=question.yml) |

Este repositório guarda o programa e as submissões, e nada além disso. Não há servidor aqui e não há nada para instalar. O servidor MCP, a CLI, o SDK e o catálogo completo de skills vivem no [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), que é o único lugar onde as instruções de instalação são mantidas.

Na prática: você instala e trabalha no toolkit, lê [as skills de lá](https://github.com/pipefy/ai-toolkit/tree/main/skills) como referência, e vem aqui para ler as regras e publicar sua submissão.

## Perguntas frequentes

**Preciso saber programar?** Não. Você precisa conhecer um processo bem o suficiente para explicá-lo passo a passo. O formulário de submissão existe justamente para que git não seja pré-requisito.

**Preciso de uma conta paga do Pipefy?** Não. Conta gratuita funciona. Você precisa ter acesso de Pipe Admin ou Org Admin para construir o que sua skill descreve.

**Posso enviar mais de uma skill?** Pode. Cada uma é avaliada separadamente.

**Posso escrever em português?** Pode. Inglês é preferencial porque o toolkit é em inglês, mas submissões em português são aceitas e a tradução fica com a gente quando a skill for promovida.

**De quem é a minha skill?** Você escreveu, e você é creditado onde quer que ela apareça. As contribuições deste repositório são publicadas sob [Apache 2.0](LICENSE), a mesma licença do toolkit.

**Pessoas da Pipefy participam?** Podem contribuir com skills, mas não concorrem aos prêmios.

## Idioma

O README, o guia de contribuição e tudo que está em `docs/` são mantidos em inglês e português, como pares `.md` e `.pt-BR.md` em sincronia. Os templates de issue e de pull request trazem os dois idiomas no mesmo arquivo.

## Código de conduta e licença

A participação é regida pelo nosso [Código de Conduta](CODE_OF_CONDUCT.md). O conteúdo deste repositório é licenciado sob [Apache 2.0](LICENSE).
