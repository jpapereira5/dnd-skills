# dnd-skills

As skills de DM de João Pereira (Contos & Escudos), em português de Portugal. São **genéricas**: servem a qualquer campanha ou one-shot (Call of the Netherdeep, O Farol Apagado, Marcas de Guerra, The Unmade God…) e a uma conversa solta sem projeto nenhum.

Este repositório é a **cópia-mãe**. Uma skill nova ou alterada grava-se aqui primeiro e, na mesma conversa, atualiza-se nos projetos que a usam (`.claude/skills/`) e no Projeto do claude.ai; a cópia de leitura da Drive atualiza-se numa tarefa agendada diária (decidido pelo DM a 2026-10-24) (pasta `DND/skills/`, um `<nome>.md` por skill, com `_` no lugar do hífen, por exemplo `registo_mesa.md`; os ficheiros extra como `<skill>_<ficheiro>.md`, por exemplo `batalha_referencia_combate.md`; versão nova como ficheiro novo, a anterior para o lixo). No Projeto «Dungeons & Dragons», `skills/<nome>.md`, reescrito no mesmo caminho.

## As skills

| Skill | Quando |
| :-- | :-- |
| `decidir` | O DM decide, confirma ou rejeita alguma coisa; escolhas como perguntas, decisões gravadas |
| `arcos` | O percurso, os segredos e as descobertas dos PCs, capítulo a capítulo |
| `capitulo` | Desenhar um capítulo, um arco ou uma zona à Mass Effect, por rondas com pontos de controlo |
| `npc` | Um NPC em dois níveis: figurante (Brennan Lee Mulligan) ou elenco (Matt Mercer) |
| `local` | Um local ou uma loja, vivo e cinematográfico |
| `batalha` | A folha de um combate: combatentes, terreno, táticas e descrições por resultado |
| `livro` | O que dizem os livros, com a referência, separado do que o projeto mudou |
| `confessionario` | As perguntas de confessionário de uma sessão já jogada, para os jogadores responderem em personagem à câmara |
| `registo-mesa` | O índice de sessões e a lista de jogadores do DM (Google Docs na pasta `tabletop` da Drive), sempre atualizados: no fim de cada fecho e de cada sessão fora da campanha |

Cada skill é uma pasta com um `SKILL.md`: um cabeçalho (`name`, `description`) e as instruções em Markdown. A descrição diz quando usar; o corpo diz como. Qualquer ferramenta de IA as consegue ler.

## O método (`reference/`)

Os documentos de método em que as skills se apoiam. Vieram da pasta `reference/` da Drive a 2026-10-18; a versão daqui é a que vale.

| Documento | O quê |
| :-- | :-- |
| [`campaign_design.md`](reference/campaign_design.md) | Os tenets de campanha, a estrutura de missão à Mass Effect, os tipos de escolha impossível |
| [`one_shot_design.md`](reference/one_shot_design.md) | O método das one-shots: fases, blocos, binário, rubrica de 22 itens |
| [`dm_profile.md`](reference/dm_profile.md) | O estilo do DM à mesa, tirado de 126 transcrições: voz, locais, NPCs, combate, revelações |

Foram escritos na era do vault Obsidian; o `one_shot_design.md` foi corrigido a 2026-10-21 para o que existe hoje (um Google Doc de preparação em pt-PT por one-shot; a referência de combate em `skills/batalha/referencia-combate.md`, revista de `dm_tools/references/combat/` da Drive).

## Como um projeto usa estas skills

1. **Copia** as pastas das skills que quer para `.claude/skills/` do repositório do projeto (o Claude Code carrega-as dali): `python3 scripts/sincronizar.py copiar ../<projeto>`. Para outras ferramentas, basta o `AGENTS.md` apontar para essa pasta.
2. **Escreve o `AGENTS.md`** na raiz do projeto, com uma secção `## Para as skills` que diz o que é próprio daquele projeto. Modelo em [`AGENTS-modelo.md`](AGENTS-modelo.md).
3. **Skills só do projeto** (as que dependem de uma ferramenta dele, como a Grelha da CotN) ficam no repositório do projeto e não vêm para aqui.

Sem projeto (uma conversa solta), as skills trabalham na mesma: entregam na conversa ou num documento na Drive, e perguntam o que precisarem de saber.

## Scripts

| Comando | O quê |
| :-- | :-- |
| `python3 scripts/verificar.py` | Lint das skills (cabeçalho, descrição, ficheiros citados, termos da era do vault); corre no CI |
| `python3 scripts/sincronizar.py copiar ../campaign-cotn` | Copia as genéricas para o projeto |
| `python3 scripts/sincronizar.py conferir ../campaign-cotn` | Diz se alguma cópia diverge (o CI do projeto faz o mesmo) |
| `python3 scripts/sincronizar.py gerar SAIDA ../campaign-cotn` | Gera as cópias com os nomes da Drive (`drive/`) e do Projeto (`projeto/`) e um `manifesto.json` |
| `python3 scripts/sincronizar.py diferencas SAIDA manifesto-antigo.json` | O que há para enviar e apagar desde a última vez |

Para atualizar a Drive e o Projeto: `gerar`, depois `diferencas` contra o `manifesto.json` da vez anterior (guardado na pasta `DND/skills/` da Drive), e o Claude envia só o que mudou (Drive: ficheiro novo e o antigo para o lixo; Projeto: reescrito no mesmo caminho) e no fim o manifesto.

## Na conta do Claude

As skills **não** se guardam na conta do claude.ai (decidido pelo DM a 2026-10-21): vivem no Projeto «Dungeons & Dragons» do claude.ai (`skills/<nome>.md`), neste repositório, nos projetos que as usam e na Drive (`DND/skills/`).

## Projetos que as usam

| Projeto | Repositório | Skills |
| :-- | :-- | :-- |
| Call of the Netherdeep | `jpapereira5/campaign-cotn` | todas (mais `preparar`, `fecho` e `vigia`, só do projeto; a `preparar` faz também o documento de preparação da sessão, que era a antiga `runsheet`) |
