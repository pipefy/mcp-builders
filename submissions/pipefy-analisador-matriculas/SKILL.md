---
name: pipefy-analisador-matriculas
description: Lê documentos de matrícula de imóvel (PDF ou imagem) via OCR, extrai os dados estruturados e preenche automaticamente os campos de dois cards no Pipefy, emitindo uma decisão de aptidão para alienação fiduciária.
tags:
  - imóvel
  - ocr
  - crédito
  - home-equity
  - documentos
---

# Analisador de Matrículas de Imóvel

Recebe o documento de imóvel anexado a um card do Pipefy (PDF ou imagem), envia para um serviço de OCR externo, interpreta as informações da matrícula e preenche automaticamente os campos do card — incluindo a decisão de **Apto / Não apto / Necessário regularização documental** para alienação fiduciária.

---

## When to use

Usar esta skill quando o documento de imóvel for anexado a um card do Pipefy e for necessário extrair as informações da matrícula:

- "Analise a matrícula do imóvel"
- "Leia o inteiro teor e preencha os campos"
- "Verifique se o imóvel tem restrições"
- "O imóvel está apto para financiamento?"
- "Extraia os dados da matrícula"

**Não usar para:** documentos que não sejam matrículas de imóvel (contratos avulsos, notas fiscais, laudos topográficos sem número de matrícula). Para esses casos, utilizar uma skill genérica de extração de documentos.

---

## Prerequisites

- Card do Pipefy com campo de anexo chamado **"Documento Imóvel"** contendo a URL do arquivo (PDF até 40 MB ou imagem: JPG, PNG, TIFF).
- O card deve conter também o campo **"id_card_pai"** (ou rótulo equivalente) com o ID do card pai no pipe de destino, que receberá um resumo dos dados extraídos.
- Acesso a um serviço de OCR externo capaz de receber uma URL de documento e retornar JSON estruturado (ver contrato na seção Steps).
- O **Pipe Agente** (onde o documento fica) precisa ter os seguintes campos de saída configurados:

  | Rótulo do campo | Slug |
  |---|---|
  | Número Matrícula | `n_mero_matr_cula` |
  | Tipo de Documento Imóvel | `tipo_de_docuemento` |
  | Envolvidos | `envolvidos` |
  | Cartório Responsável | `cart_rio_respons_vel` |
  | Ano Registro | `ano_registro` |
  | Tipo Imóvel | `tipo_im_vel` |
  | Inalienabilidade? | `inalienabilidade` |
  | Motivo Inalienabilidade | `motivo_inalienabilidade` |
  | Alienação Fiduciária? | `aliena_o_fiduci_ria` |
  | Motivo Alienação Fiduciária | `motivo_aliena_o_fiduci_ria` |
  | Status decisão empréstimo | `status_decis_o_empr_stimo` |
  | Justificativa decisão empréstimo | `justificativa_decis_o_empr_stimo` |
  | Endereço Imóvel | `endere_o_im_vel` |
  | Valor Venal | `valor_venal` |
  | Praça | `pra_a` |
  | IPTU Existe? | `iptu_existe` |
  | Matrícula do IPTU | `matricula_do_iptu` |
  | Leitor Funcionou? | `leitor_funcionou` |

- O **Pipe de destino** (card pai) precisa ter estes 7 campos para receber o resumo:

  | Rótulo do campo | Slug |
  |---|---|
  | Matrícula Cartórios de Imóveis | `matr_cula_cart_rios_de_im_veis_1` |
  | Documento do Imóvel | `documento_do_im_vel` |
  | Tipo do Imóvel | `tipo_do_im_vel_2` |
  | Possui Inalienabilidade | `possui_inalienabilidade` |
  | Possui Alienação Fiduciária | `possui_aliena_o_fiduci_ria` |
  | Endereço do Imóvel | `endere_o_do_im_vel` |
  | Valor Venal | `valor_venal_1` |

- Acesso de **Membro ou Admin** nos dois pipes para leitura e atualização dos campos.

---

## Tools needed

| Ferramenta (MCP) | Finalidade |
|---|---|
| get_card | Busca o card e todos os seus campos, incluindo a URL do documento e o id_card_pai |
| update_card_field | Grava os dados extraídos em cada campo do card do Pipe Agente |
| move_card_to_phase | Move o card do Pipe Agente para a fase correta após a gravação |
| update_card_field | Grava o resumo de 7 campos no card pai usando o id_card_pai |

Para montar este fluxo no iPaaS do Pipefy (Advanced Automations), use as meta-tools:

| Meta-tool | Finalidade |
|---|---|
| get_ipaas_tools | Lista as ferramentas disponíveis no iPaaS para montar os steps |
| call_ipaas_tool | Executa cada step da automação (busca do card, chamada ao OCR, gravação dos campos) |

> O OCR e a interpretação do documento acontecem via serviço HTTP externo. A skill envia a URL do documento e recebe de volta o JSON estruturado. O contrato desse serviço está descrito no Passo 2.

---

## Steps

### Passo 1 — Buscar o card e extrair a URL do documento

```
get_card(card_id: <card_id>)
```

Na resposta, localiza o campo com rótulo **"Documento Imóvel"** (busca sem distinção de maiúsculas/acentos). Extrai a URL HTTP do valor do campo.

Localiza também o campo com rótulo **"id_card_pai"** (tentando variações: `id card pai`, `card pai`, `id card cgi`) e armazena o valor para o Passo 4.

Se o campo do documento estiver vazio ou nenhuma URL for encontrada, interrompe e registra o problema no card via `update_card_field` no slug `leitor_funcionou`.

### Passo 2 — Enviar documento para o serviço de OCR

```
call_ipaas_tool(
  tool: "http_request",
  method: "POST",
  url: "<ocr_service_url>",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "<ocr_api_key>"
  },
  body: {
    "type": "imovel",
    "documentUrl": "<document_url_do_passo_1>"
  }
)
```

**Contrato do serviço de OCR:**

Entrada:
```json
{
  "type": "imovel",
  "documentUrl": "<url relativa do documento>"
}
```

Internamente, o serviço executa um OCR no documento e monta um texto estruturado no seguinte formato antes de enviá-lo para o modelo de linguagem:

```
TEXTO:
<conteúdo corrido do documento>

PARES_CHAVE_VALOR:
<campo>: <valor>

TABELAS:
Tabela 1:
<linha 1>
<linha 2>

CODIGOS_DE_BARRAS:
<tipo>: <valor>
```

Esse texto estruturado é enviado ao modelo de linguagem com o seguinte prompt:

```
Você analisa matrícula ou documento de imóvel brasileiro (matrícula, escritura, contrato
particular, certidão narrativa, doação, título definitivo) a partir do texto/tabelas
do serviço de OCR.

Devolva SOMENTE o JSON especificado, sem markdown. Não invente matrícula, valor ou restrição.

O texto pode ter ruído de OCR, quebras ruins e campos fora de ordem.
Use TEXTO, TABELAS e CODIGOS_DE_BARRAS quando vierem.

documento_analisado deve ser um destes: Contrato Particular de Compra e Venda,
Certidão Narrativa, Escritura Pública de Venda e Compra, Escritura Pública de Doação,
Título Definitivo.

inscricao_cadastral.detalhe no formato xx.xx.xxx.xxxx.xxx ou "Não Há".
cep.detalhe no formato xx.xxx-xxx ou "Não Há".
valor_venal_imovel com moeda, ex. R$ 1.500.000,00.

inalienabilidade e alienacao_fiduciaria são cláusulas distintas. Não as inverta.
motivo de inalienabilidade vem de inalienabilidade.detalhes.
motivo de alienação fiduciária vem de alienacao_fiduciaria.detalhes.
clausulas_impeditivas continua no JSON para a decisão.

decisao_emprestimo.status: "Apto para alienação fiduciária" | "Não apto para alienação
fiduciária" | "Necessário regularização documental", com justificativa objetiva
(cláusula impeditiva, inalienabilidade, falta de escritura, matrícula irregular, etc.).

Campo ausente: "não identificado" ou "não se aplica".

{
  "documento_analisado": "Contrato Particular de Compra e Venda | Certidão Narrativa | Escritura Pública de Venda e Compra | Escritura Pública de Doação | Título Definitivo",
  "envolvidos": "",
  "numero_matricula": "",
  "cartorio_responsavel": "",
  "ano_registro": "",
  "tipo_imovel": "",
  "clausulas_impeditivas": { "identificado": "Sim|Não", "detalhes": "" },
  "inscricao_cadastral": { "possui": "Sim|Não", "detalhe": "xx.xx.xxx.xxxx.xxx|Não Há" },
  "cep": { "possui": "Sim|Não", "detalhe": "xx.xxx-xxx|Não Há" },
  "inalienabilidade": { "existe": "Sim|Não", "detalhes": "" },
  "alienacao_fiduciaria": { "existe": "Sim|Não", "detalhes": "" },
  "endereco_imovel": "",
  "valor_venal_imovel": "R$ 1.500.000,00",
  "praca": { "cidade": "" },
  "decisao_emprestimo": {
    "status": "Apto para alienação fiduciária|Não apto para alienação fiduciária|Necessário regularização documental",
    "justificativa": ""
  }
}
```

Saída esperada (campos obrigatórios para a skill funcionar):
```json
{
  "numero_matricula": "string | null",
  "documento_analisado": "string | null",
  "envolvidos": "string | null",
  "cartorio_responsavel": "string | null",
  "ano_registro": "string | null",
  "tipo_imovel": "string | null",
  "endereco_imovel": "string | null",
  "valor_venal_imovel": "string | null",
  "praca": { "cidade": "string | null" },
  "inalienabilidade": { "existe": "Sim | Não", "detalhes": "string | null" },
  "alienacao_fiduciaria": { "existe": "Sim | Não", "detalhes": "string | null" },
  "clausulas_impeditivas": { "identificado": "Sim | Não", "detalhes": "string | null" },
  "inscricao_cadastral": { "possui": "Sim | Não", "detalhe": "string | null" },
  "decisao_emprestimo": {
    "status": "Apto para alienação fiduciária | Não apto para alienação fiduciária | Necessário regularização documental",
    "justificativa": "string"
  }
}
```

O serviço aceita PDF até 40 MB e imagens (JPG, PNG, TIFF). Se `numero_matricula` e `documento_analisado` vierem ambos nulos, o documento é considerado ilegível — interrompa e reporte.

### Passo 3 — Normalizar a resposta

Antes de gravar, converte os valores inválidos para `null`:
- Strings: `"não identificado"`, `"não se aplica"`, `"não há"` e variantes sem acento → `null`

Extrai os valores aninhados com segurança:
- `inalienabilidade.existe`, `inalienabilidade.detalhes`
- `alienacao_fiduciaria.existe`, `alienacao_fiduciaria.detalhes`
- `inscricao_cadastral.possui`, `inscricao_cadastral.detalhe`
- `praca.cidade`

### Passo 4 — Gravar dados no Pipe Agente e mover de fase

```
call_ipaas_tool(
  tool: "move_card_to_phase",
  card_id: <card_id>,
  phase_id: <phase_id>,
  fields: [
    { fieldId: "n_mero_matr_cula", value: <numero_matricula> },
    { fieldId: "tipo_de_docuemento", value: <documento_analisado> },
    { fieldId: "envolvidos", value: <envolvidos> },
    { fieldId: "cart_rio_respons_vel", value: <cartorio_responsavel> },
    { fieldId: "ano_registro", value: <ano_registro> },
    { fieldId: "tipo_im_vel", value: <tipo_imovel> },
    { fieldId: "endere_o_im_vel", value: <endereco_imovel> },
    { fieldId: "valor_venal", value: <valor_venal_imovel> },
    { fieldId: "pra_a", value: <praca.cidade> },
    { fieldId: "inalienabilidade", value: <inalienabilidade.existe> },
    { fieldId: "motivo_inalienabilidade", value: <inalienabilidade.detalhes> },
    { fieldId: "aliena_o_fiduci_ria", value: <alienacao_fiduciaria.existe> },
    { fieldId: "motivo_aliena_o_fiduci_ria", value: <alienacao_fiduciaria.detalhes> },
    { fieldId: "status_decis_o_empr_stimo", value: <decisao_emprestimo.status> },
    { fieldId: "justificativa_decis_o_empr_stimo", value: <decisao_emprestimo.justificativa> },
    { fieldId: "iptu_existe", value: <inscricao_cadastral.possui> },
    { fieldId: "matricula_do_iptu", value: <inscricao_cadastral.detalhe> },
    { fieldId: "leitor_funcionou", value: "Sim" }
  ]
)
```

### Passo 5 — Gravar resumo no card pai

```
call_ipaas_tool(
  tool: "update_card_field",
  pipe_id: <pipe_id_destino>,
  card_id: <id_card_pai>,
  fields: [
    { fieldId: "matr_cula_cart_rios_de_im_veis_1", value: <numero_matricula> },
    { fieldId: "documento_do_im_vel", value: <documento_analisado> },
    { fieldId: "tipo_do_im_vel_2", value: <tipo_imovel> },
    { fieldId: "possui_inalienabilidade", value: <inalienabilidade.existe> },
    { fieldId: "possui_aliena_o_fiduci_ria", value: <alienacao_fiduciaria.existe> },
    { fieldId: "endere_o_do_im_vel", value: <endereco_imovel> },
    { fieldId: "valor_venal_1", value: <valor_venal_imovel> }
  ]
)
```

Se `id_card_pai` não foi encontrado no Passo 1, este passo é ignorado — a gravação no Pipe Agente (Passo 4) segue normalmente.

---

## Success criteria

- Todos os campos aplicáveis do card do Pipe Agente estão preenchidos (ou explicitamente `null` quando o dado não foi encontrado no documento).
- O card do Pipe Agente foi movido para a fase `<phase_id>`.
- O resumo de 7 campos foi gravado no card pai (quando `id_card_pai` está disponível).
- O campo `leitor_funcionou` está marcado como `"Sim"`.
- Nenhum JSON bruto é exibido para o usuário final.

---

## Failure modes

| Situação | Comportamento esperado |
|---|---|
| Campo "Documento Imóvel" vazio | Interrompe e grava o motivo em `leitor_funcionou` |
| URL do documento inválida ou inacessível | Interrompe e grava o motivo em `leitor_funcionou` |
| Serviço de OCR retorna erro | Não grava dados parciais; grava erro em `leitor_funcionou` |
| Documento ilegível (`numero_matricula` e `documento_analisado` nulos) | Interrompe e grava o motivo em `leitor_funcionou` |
| `id_card_pai` ausente no card | Passo 5 é ignorado; Passo 4 segue normalmente |
| Fase de destino não existe no pipe | Grava os campos sem mover de fase; registra aviso |
