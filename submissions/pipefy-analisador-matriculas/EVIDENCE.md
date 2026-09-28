[# Evidence — Analisador de Matrículas de Imóvel

## O problema de processo

Equipes de crédito imobiliário (home equity) recebem diariamente matrículas de imóveis em PDF e imagem para análise manual. O analista precisava abrir cada documento, localizar informações como número de matrícula, cláusulas de inalienabilidade, alienação fiduciária e valor venal, preencher manualmente dois cards no Pipefy (um no Pipe Agente e outro no Pipe CGI pai) e escrever um parecer. O processo levava entre 15 e 40 minutos por documento e era suscetível a erros de leitura e esquecimento de campos.

## O que a skill resolve

A skill é acionada automaticamente quando o campo **"Documento Imóvel"** é atualizado em um card do Pipe Agente. Ela:

1. Lê a URL do documento do card via API GraphQL do Pipefy.
2. Envia o documento para um endpoint de OCR + IA especializado em matrículas imobiliárias brasileiras.
3. Normaliza a resposta JSON (removendo valores inválidos como "não identificado").
4. Preenche **18 campos** no card do Pipe Agente e move o card para a fase de resultado.
5. Preenche **7 campos** de resumo no card pai do Pipe CGI, usando o `id_card_pai` capturado do próprio card.

O tempo de análise passou de 15–40 minutos para aproximadamente 30 segundos por documento.

## Ambiente de execução

- **Plataforma:** Pipefy iPaaS (Advanced Automations via ActivePieces) — rodando nativamente dentro do Pipefy, sem ferramenta externa de automação
- **Trigger:** `cardFieldUpdated` no campo `398567923` (Documento Imóvel), Pipe Agente `305714516`, Org `300738585`
- **OCR + IA:** Endpoint HTTP externo especializado em matrículas imobiliárias (`/home-equity-automation/webhooks/documents`) — aceita PDF até 200 MB e imagens
- **Pipes envolvidos:**
  - Pipe Agente: `305714516` (onde o documento é anexado, 18 campos preenchidos)
  - Pipe CGI: `306806519` (card pai, 7 campos de resumo preenchidos)

## Fluxo executado

```
Trigger: campo "Documento Imóvel" atualizado no card
  │
  ├─ step_1: GET card completo via GraphQL (todos os campos)
  │
  ├─ step_2 (CODE): Extrair URL do documento + capturar id_card_pai
  │           Normalização de nome de campo (case-insensitive, sem acento)
  │
  ├─ step_3: POST para endpoint OCR/IA
  │           body: { type: "imovel", documentUrl: "<url relativa>" }
  │           Retorna JSON com 15+ campos estruturados da matrícula
  │
  ├─ step_4 (CODE, skip=true): Normalizar resposta
  │           Remove "não identificado", "não se aplica", "não há" → null
  │           Extrai valores aninhados de forma segura
  │
  ├─ step_5: updateCard no Pipe Agente
  │           18 campos + move para fase 334111706
  │
  └─ step_6: updateCard no Pipe CGI (card pai)
              7 campos de resumo usando id_card_pai
```

## Campos preenchidos automaticamente

**Pipe Agente (18 campos):**

| Campo | Dado extraído |
|---|---|
| `n_mero_matr_cula` | Número da matrícula |
| `tipo_de_docuemento` | Tipo de documento |
| `envolvidos` | Nomes dos envolvidos |
| `cart_rio_respons_vel` | Cartório responsável |
| `ano_registro` | Ano do registro |
| `tipo_im_vel` | Tipo de imóvel |
| `endere_o_im_vel` | Endereço completo |
| `valor_venal` | Valor venal |
| `pra_a` | Cidade/praça |
| `inalienabilidade` | Sim/Não |
| `motivo_inalienabilidade` | Detalhes da cláusula |
| `aliena_o_fiduci_ria` | Sim/Não |
| `motivo_aliena_o_fiduci_ria` | Detalhes da alienação |
| `status_decis_o_empr_stimo` | Apto / Não apto / Regularização |
| `justificativa_decis_o_empr_stimo` | Justificativa em linguagem de negócio |
| `iptu_existe` | Inscrição cadastral: Sim/Não |
| `matricula_do_iptu` | Número da inscrição municipal |
| `leitor_funcionou` | Status da operação |

**Pipe CGI / card pai (7 campos):**

| Campo | Dado extraído |
|---|---|
| `matr_cula_cart_rios_de_im_veis_1` | Número da matrícula |
| `documento_do_im_vel` | Tipo de documento |
| `tipo_do_im_vel_2` | Tipo de imóvel |
| `possui_inalienabilidade` | Sim/Não |
| `possui_aliena_o_fiduci_ria` | Sim/Não |
| `endere_o_do_im_vel` | Endereço completo |
| `valor_venal_1` | Valor venal |

## Exemplo de saída do endpoint OCR/IA

```json
{
  "numero_matricula": "12.345",
  "documento_analisado": "Escritura Pública de Venda e Compra",
  "cartorio_responsavel": "2º Ofício de Registro de Imóveis de Manaus",
  "tipo_imovel": "Apartamento",
  "inalienabilidade": { "existe": "Não", "detalhes": "não se aplica" },
  "alienacao_fiduciaria": { "existe": "Não", "detalhes": "não se aplica" },
  "endereco_imovel": "Rua Exemplo, 123, Apto 45, Manaus - AM",
  "valor_venal_imovel": "R$ 320.000,00",
  "decisao_emprestimo": {
    "status": "Apto para alienação fiduciária",
    "justificativa": "Documento de escritura pública válida, sem restrições de inalienabilidade ou alienação fiduciária ativa registradas na matrícula."
  }
}
```

## Diferenciais desta skill

- **Dois pipes atualizados em uma execução:** o card do Pipe Agente (análise completa) e o card pai do Pipe CGI (resumo executivo) são preenchidos automaticamente na mesma automação.
- **Normalização robusta:** valores como "não identificado" e "não se aplica" são convertidos para `null` antes de gravar, evitando ruído nos campos do Pipefy.
- **Resiliência:** o passo de atualização do card pai tem `continueOnFailure: true`, garantindo que a análise principal não seja bloqueada caso o `id_card_pai` esteja ausente.
- **Rodando em produção:** esta automação está publicada (`status: PUBLISHED`) no iPaaS nativo do Pipefy, validada com documentos reais do processo de home equity da CGI.AI.
](https://github.com/erikbatistaribeiro/mcp-builders/blob/main/submissions/erikbatistaribeiro/pipefy-analisador-matriculas/SKILL.md)
