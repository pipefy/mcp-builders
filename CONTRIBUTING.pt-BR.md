Leia em [English](CONTRIBUTING.md).

# Como enviar uma skill

São dois caminhos. Os dois terminam no mesmo lugar, e nenhum vale mais ponto que o outro.

## Antes de começar

Sua skill precisa rodar antes de você enviar. Instale o servidor MCP a partir do [Pipefy AI Toolkit](https://github.com/pipefy/ai-toolkit), escreva sua skill lá, e use em uma organização Pipefy real que você controla. Se ainda não configurou o toolkit, comece por [Primeiros passos](docs/getting-started.pt-BR.md).

Nunca coloque token, chave de API, ID de organização real, nome de cliente ou dado pessoal dentro de uma skill. Submissão com credencial é fechada sem revisão. Use placeholders como `<pipe_id>`.

## Caminho 1: formulário de submissão

Use este se você não tem familiaridade com git. É a rota mais curta.

1. Abra uma [issue de submissão](../../issues/new?template=submit-skill.yml).
2. Cole seu `SKILL.md` no campo da skill e preencha os campos de evidência.
3. Envie. A gente converte sua issue em pull request e faz o commit com você como autor, então seu perfil do GitHub aparece no histórico.

A autoria continua sua. A única coisa que você abre mão é do controle sobre a mensagem de commit.

## Caminho 2: pull request

Use este se você já trabalha com git.

1. Faça um fork deste repositório e crie uma branch.
2. Copie o template para a pasta da sua submissão:

   ```bash
   mkdir -p submissions/<seu-usuario-github>/<nome-da-skill>
   cp template/SKILL.md    submissions/<seu-usuario-github>/<nome-da-skill>/SKILL.md
   cp template/EVIDENCE.md submissions/<seu-usuario-github>/<nome-da-skill>/EVIDENCE.md
   ```

3. Escreva os dois arquivos. As regras estão em [Como escrever uma skill](docs/writing-a-skill.pt-BR.md).
4. Abra o pull request e preencha o template da descrição.

## Regras de pasta e nome

```
submissions/<seu-usuario-github>/<nome-da-skill>/
├── SKILL.md
├── EVIDENCE.md
└── assets/          # opcional: prints referenciados pelo EVIDENCE.md
```

- `<seu-usuario-github>` é seu nome de usuário no GitHub, em minúsculas.
- `<nome-da-skill>` é kebab-case e descreve a ação, por exemplo `aprovacao-de-notas-fiscais` ou `auditoria-de-onboarding-de-fornecedor`.
- O `name` no frontmatter do `SKILL.md` precisa ser idêntico a `<nome-da-skill>`. Isso é verificado automaticamente.

## O que a verificação automática confere

Todo pull request que mexe em `submissions/` roda um validador. Ele confere:

- se a pasta está em `submissions/<usuario>/<nome-da-skill>/`
- se `SKILL.md` e `EVIDENCE.md` existem
- se o frontmatter é YAML válido e tem `name`, `description` e `tags`
- se o `name` bate com o nome da pasta
- se as seções obrigatórias estão presentes: When to use, Prerequisites, Tools needed, Steps, Success criteria, Failure modes
- se não há credencial ou token nos arquivos

Ele não confere se os nomes de tools MCP que você citou estão escritos corretamente, e não reprova por tamanho. Skill acima de 500 linhas recebe um aviso, não uma reprovação. Se sua skill precisa do espaço, use, e a gente conversa na revisão.

Você pode rodar a mesma verificação localmente:

```bash
python3 scripts/validate_submission.py submissions/<seu-usuario-github>/<nome-da-skill>
```

## Revisão

Toda submissão é revisada. Espere um destes três resultados:

- **Aceita.** É mesclada, você entra no [SUBMISSIONS.md](SUBMISSIONS.md) e recebe o selo.
- **Ajustes solicitados.** Algo está confuso, sem evidência, ou não reproduziria. A gente diz exatamente o que corrigir, e você tem até o prazo final para corrigir.
- **Fechada.** Raro. Acontece quando a submissão contém credencial, é cópia de uma skill existente do toolkit sem contribuição nova, ou não roda.

Ser aceita não é o mesmo que vencer. Tudo que é aceito ganha selo e listagem. Os dez prêmios vão para as maiores notas no [rubric](docs/judging.pt-BR.md).

## Depois do programa

As skills selecionadas são adaptadas ao formato do Pipefy AI Toolkit e publicadas lá, com você adicionado como coautor do commit. Se a sua skill precisar de tradução para inglês ou de ajuste para passar no CI do toolkit, esse trabalho é nosso, e a gente te conta o que mudou.

## Pedindo ajuda

Abra uma [issue de dúvida](../../issues/new?template=question.yml) ou comece uma conversa em [Discussions](../../discussions). O webinar AMA ao vivo do dia 9 de setembro também é um bom lugar para levar uma skill pela metade.
