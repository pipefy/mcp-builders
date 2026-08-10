Leia em [English](judging.md).

# Como as submissões são avaliadas

Este rubric é publicado antes de o programa abrir para que você escreva mirando nele. É o mesmo rubric usado para escolher as dez vencedoras.

Toda submissão aceita ganha o selo de contribuidor e a listagem pública, independente da nota. A nota só decide os prêmios.

## Pontuação

Cada critério recebe nota de 1 a 5 e tem um peso. A nota final é a média ponderada, de 0 a 5.

| Critério | Peso | Pergunta que está sendo respondida |
|----------|------|------------------------------------|
| Impacto no processo | 30% | Isso resolve uma dor real e recorrente, e o ganho é visível? |
| Praticidade e reprodutibilidade | 25% | Outra pessoa consegue rodar sem adivinhar? |
| Uso correto do MCP | 20% | Ferramentas certas, ordem certa, sem gambiarra desnecessária? |
| Evidência de execução | 15% | Existe prova de que rodou de verdade no Pipefy? |
| Reusabilidade por outras empresas | 10% | Funciona fora do cenário específico de quem escreveu? |

## Como cada nota se parece

**Impacto no processo, 30%.** Um 5 resolve um problema que custa horas reais de um time toda semana, e a skill deixa o ganho concreto. Um 3 resolve algo real mas estreito, ou afirma o ganho sem mostrar. Um 1 automatiza algo que não era problema.

**Praticidade e reprodutibilidade, 25%.** Um 5 tem passos ordenados, pré-requisitos explícitos, chamadas de ferramenta executáveis e critérios de sucesso que qualquer um verifica. Um 3 funciona mas deixa lacunas que quem lê precisa preencher por intuição. Um 1 não dá para seguir sem perguntar ao autor o que ele quis dizer.

**Uso correto do MCP, 20%.** Um 5 usa a ferramenta certa para cada ação, em ordem segura de dependência, e só recorre a GraphQL cru onde não existe ferramenta. Um 3 funciona mas faz um caminho mais longo que o necessário, ou nomeia ferramentas de forma imprecisa. Um 1 quase não toca no MCP, ou a sequência falharia em uma organização limpa.

**Evidência de execução, 15%.** Um 5 mostra o resultado no Pipefy mais um transcript, e descreve o que quebrou na primeira tentativa e como a skill mudou. Um 3 mostra um print sem contexto. Um 1 não tem evidência, e aí tudo acima vira alegação.

**Reusabilidade por outras empresas, 10%.** Um 5 usa placeholders, declara suas premissas e funcionaria em outra empresa já na primeira leitura. Um 3 precisa de adaptação leve. Um 1 está soldado aos nomes de campo e IDs de uma organização só.

## O que desqualifica uma submissão

- Credencial, token, ID real de organização ou pipe, nome de cliente ou dado pessoal em qualquer arquivo.
- Cópia de uma skill que já está no Pipefy AI Toolkit sem contribuição nova.
- Skill que não roda.
- Submissão recebida depois do prazo de 18 de setembro.

A desqualificação é da submissão, não da pessoa. Corrija antes do prazo e envie de novo.

## Quem avalia

A avaliação é feita por Adrianno Esnarriaga, que lidera o Pipefy AI Toolkit. Toda submissão recebe nota nos cinco critérios, e as dez maiores médias ponderadas ficam com os prêmios.

Empate é resolvido primeiro por impacto no processo, depois por evidência.

## Prêmios

- **Quem não é cliente Pipefy:** 1 ano de plano Business.
- **Quem já é cliente:** 1.000 AI credits por mês durante 1 ano.

Pessoas da Pipefy podem contribuir com skills, mas não concorrem aos prêmios.

Os vencedores são anunciados em 23 de setembro.

## Depois da avaliação

As skills selecionadas são levadas para o [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), adaptadas ao formato e ao CI de lá, com o autor adicionado como coautor do commit de publicação. A promoção não se limita às dez vencedoras. Qualquer skill boa o suficiente para entrar em produção pode ser promovida.
