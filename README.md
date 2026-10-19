# dnd-skills

As skills de DM de João Pereira (Contos & Escudos), em português de Portugal. São **genéricas**: servem a qualquer campanha ou one-shot (Call of the Netherdeep, O Farol Apagado, Marcas de Guerra, The Unmade God…) e a uma conversa solta sem projeto nenhum.

Este repositório é a **cópia-mãe**. Uma skill nova ou alterada grava-se aqui primeiro e, na mesma conversa, atualiza-se em todo o lado: nos projetos que a usam (`.claude/skills/`), na conta do Claude (proposta com o SKILL.md completo), na cópia de leitura da Drive (pasta `DND/skills/`, um `<nome>.md` por skill; versão nova como ficheiro novo, a anterior para o lixo) e nos documentos do Projeto «Dungeons & Dragons» do claude.ai (`skills/<nome>.md`, reescrito no mesmo caminho).

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

Cada skill é uma pasta com um `SKILL.md`: um cabeçalho (`name`, `description`) e as instruções em Markdown. A descrição diz quando usar; o corpo diz como. Qualquer ferramenta de IA as consegue ler.

## O método (`reference/`)

Os documentos de método em que as skills se apoiam. Vieram da pasta `reference/` da Drive a 2026-10-18; a versão daqui é a que vale.

| Documento | O quê |
| :-- | :-- |
| [`campaign_design.md`](reference/campaign_design.md) | Os tenets de campanha, a estrutura de missão à Mass Effect, os tipos de escolha impossível |
| [`one_shot_design.md`](reference/one_shot_design.md) | O método das one-shots: fases, blocos, binário, rubrica de 22 itens |
| [`dm_profile.md`](reference/dm_profile.md) | O estilo do DM à mesa, tirado de 126 transcrições: voz, locais, NPCs, combate, revelações |

Foram escritos na era do vault Obsidian. As menções a `dashboard.cmd`, aos runsheets do dashboard e aos templates (`one_shot_design_template`, `runsheet_template`, `one_shot_template`) referem-se ao dashboard antigo das one-shots, que saiu da Drive a 2026-10-19 com os templates; o `combat_reference.md` continua na pasta `reference/` da Drive. O `agent_conventions` e o `authoring_conventions` foram para o lixo a 2026-10-19: o método continua válido, essas instruções de ferramenta não.

## Como um projeto usa estas skills

1. **Copia** as pastas das skills que quer para `.claude/skills/` do repositório do projeto (o Claude Code carrega-as dali). Para outras ferramentas, basta o `AGENTS.md` apontar para essa pasta.
2. **Escreve o `AGENTS.md`** na raiz do projeto, com uma secção `## Para as skills` que diz o que é próprio daquele projeto. Modelo em [`AGENTS-modelo.md`](AGENTS-modelo.md).
3. **Skills só do projeto** (as que dependem de uma ferramenta dele, como a Grelha da CotN) ficam no repositório do projeto e não vêm para aqui.

Sem projeto (uma conversa solta), as skills trabalham na mesma: entregam na conversa ou num documento na Drive, e perguntam o que precisarem de saber.

## Na conta do Claude

Para estarem em todas as conversas do claude.ai, as skills também se guardam na conta (pelos cartões de proposta). A cópia da conta segue a deste repositório: quando uma muda aqui, propõe-se a versão nova para a conta.

## Projetos que as usam

| Projeto | Repositório | Skills |
| :-- | :-- | :-- |
| Call of the Netherdeep | `jpapereira5/campaign-cotn` | todas (mais `preparar`, `fecho` e `vigia`, só do projeto; a `preparar` faz também o documento de preparação da sessão, que era a antiga `runsheet`) |
