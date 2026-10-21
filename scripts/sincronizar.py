#!/usr/bin/env python3
"""Sincroniza as skills pelos sítios onde vivem (README, «Como um projeto usa estas skills»).

Uso:
  python3 scripts/sincronizar.py copiar <projeto> [...]     copia as genéricas para <projeto>/.claude/skills/
  python3 scripts/sincronizar.py gerar  SAIDA [<projeto> ...] gera as cópias com os nomes da Drive e do Projeto
  python3 scripts/sincronizar.py diferencas SAIDA MANIFESTO  diz o que mudou desde a última cópia (JSON)
  python3 scripts/sincronizar.py conferir <projeto> [...]    sai com 1 se alguma genérica diverge no projeto

«gerar» escreve em SAIDA:
  drive/<nome>.md            (hífen → `_`; as só do projeto como <nome>_cotn.md; extras como <skill>_<ficheiro>.md)
  projeto/<nome>.md          (os documentos do Projeto «Dungeons & Dragons»: as só do projeto como «<nome> (só CotN).md»)
  manifesto.json             (sha256 de cada ficheiro; compara-se com o manifesto anterior em «diferencas»)
As skills só de um projeto são as de <projeto>/.claude/skills/ que não existem aqui; o sufixo vem do nome do projeto
(campaign-cotn → cotn). Nada aqui escreve na Drive nem no Projeto: o Claude envia o que «diferencas» disser.
"""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ROTULO = {'cotn': 'CotN'}  # como o sufixo do projeto se escreve nos títulos do Projeto do claude.ai
GENERICAS = RAIZ / 'skills'


def sufixo(projeto: Path) -> str:
    n = projeto.name
    return n.split('-')[-1] if '-' in n else n


def skills_de(pasta: Path) -> dict[str, Path]:
    return {d.name: d for d in sorted(pasta.iterdir()) if d.is_dir() and (d / 'SKILL.md').exists()}


def copiar(projetos: list[Path]) -> None:
    for p in projetos:
        alvo = p / '.claude' / 'skills'
        alvo.mkdir(parents=True, exist_ok=True)
        for nome, d in skills_de(GENERICAS).items():
            if (alvo / nome).exists():
                shutil.rmtree(alvo / nome)
            shutil.copytree(d, alvo / nome)
            print(f'{p.name}: {nome}')


def conferir(projetos: list[Path]) -> int:
    falhas = 0
    for p in projetos:
        alvo = p / '.claude' / 'skills'
        for nome, d in skills_de(GENERICAS).items():
            for f in sorted(d.rglob('*')):
                if f.is_dir():
                    continue
                g = alvo / nome / f.relative_to(d)
                if not g.exists() or g.read_bytes() != f.read_bytes():
                    print(f'{p.name}: diverge {nome}/{f.relative_to(d)}')
                    falhas += 1
    print('skills genéricas iguais' if not falhas else f'{falhas} ficheiro(s) diferentes')
    return 1 if falhas else 0


def nome_drive(skill: str, ficheiro: Path, so: str | None) -> str:
    base = skill.replace('-', '_')
    if ficheiro.name == 'SKILL.md':
        return f'{base}_{so}.md' if so else f'{base}.md'
    return f"{base}_{ficheiro.stem.replace('-', '_')}.md"


def nome_projeto(skill: str, ficheiro: Path, so: str | None) -> str:
    if ficheiro.name == 'SKILL.md':
        return f'{skill} (só {ROTULO.get(so, so)}).md' if so else f'{skill}.md'
    return f'{skill}-{ficheiro.stem}.md'


def gerar(saida: Path, projetos: list[Path]) -> None:
    if saida.exists():
        shutil.rmtree(saida)
    (saida / 'drive').mkdir(parents=True)
    (saida / 'projeto').mkdir()
    fontes: list[tuple[str, Path, str | None]] = [(n, d, None) for n, d in skills_de(GENERICAS).items()]
    for p in projetos:
        for n, d in skills_de(p / '.claude' / 'skills').items():
            if n not in skills_de(GENERICAS):
                fontes.append((n, d, sufixo(p)))
    manifesto: dict[str, dict] = {}
    for skill, d, so in fontes:
        for f in sorted(d.rglob('*.md')):
            dados = f.read_bytes()
            for pasta, nome in (('drive', nome_drive(skill, f, so)), ('projeto', nome_projeto(skill, f, so))):
                (saida / pasta / nome).write_bytes(dados)
                manifesto[f'{pasta}/{nome}'] = {'sha256': hashlib.sha256(dados).hexdigest(), 'tamanho': len(dados), 'skill': skill, 'origem': str(f.relative_to(d.parent.parent if so else RAIZ))}
    (saida / 'manifesto.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{len(manifesto)} ficheiros em {saida}')


def diferencas(saida: Path, antigo: Path) -> None:
    novo = json.loads((saida / 'manifesto.json').read_text(encoding='utf-8'))
    velho = json.loads(antigo.read_text(encoding='utf-8')) if antigo.exists() else {}
    enviar = [k for k, v in novo.items() if velho.get(k, {}).get('sha256') != v['sha256']]
    apagar = [k for k in velho if k not in novo]
    print(json.dumps({'enviar': enviar, 'apagar': apagar, 'nada_a_fazer': not enviar and not apagar}, ensure_ascii=False, indent=1))


def main() -> None:
    a = sys.argv[1:]
    if not a or a[0] not in ('copiar', 'gerar', 'diferencas', 'conferir'):
        print(__doc__)
        sys.exit(2)
    cmd, resto = a[0], [Path(x).resolve() for x in a[1:]]
    if cmd == 'copiar':
        copiar(resto)
    elif cmd == 'conferir':
        sys.exit(conferir(resto))
    elif cmd == 'gerar':
        gerar(resto[0], resto[1:])
    else:
        diferencas(resto[0], resto[1])


if __name__ == '__main__':
    main()
