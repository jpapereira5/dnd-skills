#!/usr/bin/env python3
"""Lint das skills: cabeçalho, descrição, ficheiros citados e termos da era do vault. Sai com 1 se houver problemas."""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROIBIDOS = ['dashboard.cmd', 'agent_conventions', 'authoring_conventions', 'runsheet_template', 'one_shot_template', 'runsheet_en', 'runsheet_pt', '.cursor/']
problemas: list[str] = []
for d in sorted((RAIZ / 'skills').iterdir()):
    if not d.is_dir():
        continue
    f = d / 'SKILL.md'
    if not f.exists():
        problemas.append(f'{d.name}: sem SKILL.md')
        continue
    s = f.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m:
        problemas.append(f'{d.name}: sem cabeçalho YAML')
        continue
    cab = m.group(1)
    nome = re.search(r'^name:\s*(.+)$', cab, re.M)
    desc = re.search(r'^description:\s*(.+)$', cab, re.M)
    if not nome or nome.group(1).strip() != d.name:
        problemas.append(f'{d.name}: name não é o nome da pasta')
    if not desc:
        problemas.append(f'{d.name}: sem description')
    elif not 150 <= len(desc.group(1)) <= 600:
        problemas.append(f'{d.name}: description com {len(desc.group(1))} caracteres (150 a 600)')
    for citado in re.findall(r'`([a-z0-9_-]+\.md)`', s):
        if citado not in ('SKILL.md', 'AGENTS.md', 'README.md', 'CLAUDE.md') and not (d / citado).exists() and not list(RAIZ.rglob(citado)):
            problemas.append(f'{d.name}: cita {citado}, que não existe')
    for p in PROIBIDOS:
        if p in s:
            problemas.append(f'{d.name}: fala de {p} (era do vault)')
for f in (RAIZ / 'reference').glob('*.md'):
    s = f.read_text(encoding='utf-8')
    for p in PROIBIDOS:
        if p in s:
            problemas.append(f'reference/{f.name}: fala de {p} (era do vault)')
print('\n'.join(problemas) if problemas else 'skills ok')
sys.exit(1 if problemas else 0)
