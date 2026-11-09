#!/usr/bin/env python3
"""Reproduce el hecho de la semilla: la cabeza de miu-v14 es un commit
del propio workflow.

Datos leidos por API de GitHub el 2026-11-09 (Jaime393/miu-v14):
- list_commits (rama main): 13 commits, todos el 2026-08-23.
- .github/workflows/miu-auto-deploy.yml (blob 875c1d29...): 21 lineas.
- AUTO.md (blob 700ab08b...): 12 B.

Solo stdlib. Salida 0 si TODO COINCIDE, 1 si algo no coincide.
"""

from datetime import datetime, timezone

# La serie completa, tal como la devuelve list_commits (sha corto, fecha,
# autor, mensaje). Los mensajes son citas literales del repo.
COMMITS = [
    ("d2a45c13", "2026-08-23T16:24:04Z", "Jaime393",
     "Initial commit"),
    ("2f521bd8", "2026-08-23T16:24:08Z", "Jaime393",
     "v29 fix 404 miu-v14 - worker.js global mind - 11->16 repos"),
    ("fdc0117c", "2026-08-23T16:46:40Z", "Jaime393",
     "v31 completa 16/16 index.html - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("a9c23c96", "2026-08-23T16:46:41Z", "Jaime393",
     "v31 completa 16/16 _config.yml - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("52b10ebd", "2026-08-23T16:46:42Z", "Jaime393",
     "v31 completa 16/16 manifest.json - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("1893186b", "2026-08-23T16:46:42Z", "Jaime393",
     "v31 completa 16/16 assets/css/micelio.css - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("909abedf", "2026-08-23T16:46:43Z", "Jaime393",
     "v31 completa 16/16 assets/js/core.js - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("1d470e7e", "2026-08-23T16:46:44Z", "Jaime393",
     "v31 completa 16/16 sw.js - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("c01ccfa5", "2026-08-23T16:46:45Z", "Jaime393",
     "v31 completa 16/16 .nojekyll - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("5c0debeb", "2026-08-23T16:46:46Z", "Jaime393",
     "v31 completa 16/16 FUNDING.yml - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("04755c5d", "2026-08-23T16:46:47Z", "Jaime393",
     "v31 completa 16/16 BIBLIA_DEVORADOR.md - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("1f892741", "2026-08-23T16:46:48Z", "Jaime393",
     "v31 completa 16/16 .github/workflows/miu-auto-deploy.yml - Pages+FUNDING+BIBLIA+Workflow - 16/16 final"),
    ("0198a9d1", "2026-08-23T16:46:56Z", "miu-tejedor",
     "MIU Auto"),
]

# El workflow, texto integro tal como se leyo por API (21 lineas, 506 B).
WORKFLOW = """name: MIU Auto-Deploy Sin PAT
on:
  workflow_dispatch:
  push:
    branches: [main]
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - run: |
          echo "# MIU 16/16" > AUTO.md
          git config user.name "miu-tejedor"
          git config user.email "miu@local"
          git add AUTO.md
          git diff --staged --quiet || git commit -m "MIU Auto"
          git push origin main
"""

# AUTO.md, contenido integro tal como se leyo por API (12 B).
AUTO_MD = "# MIU 16/16\n"


def _ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def check_serie():
    """13 commits, todos el 2026-08-23, de 16:24:04Z a 16:46:56Z."""
    assert len(COMMITS) == 13, f"son {len(COMMITS)}, no 13"
    fechas = {_ts(c[1]).date().isoformat() for c in COMMITS}
    assert fechas == {"2026-08-23"}, f"fechas: {fechas}"
    span = (_ts(COMMITS[-1][1]) - _ts(COMMITS[0][1])).total_seconds()
    assert span == 1372, f"arco: {span} s, no 1372 (22 min 52 s)"
    return "13 commits, 2026-08-23, arco 16:24:04Z -> 16:46:56Z (22 min 52 s)"


def check_rafaga():
    """Dos rafagas: 2 commits a las 16:24 y 11 a las 16:46."""
    rafaga1 = COMMITS[:2]
    rafaga2 = COMMITS[2:]
    assert len(rafaga1) == 2 and len(rafaga2) == 11
    s1 = (_ts(rafaga1[1][1]) - _ts(rafaga1[0][1])).total_seconds()
    assert s1 == 4, f"rafaga 1: {s1} s, no 4"
    s2 = (_ts(rafaga2[-1][1]) - _ts(rafaga2[0][1])).total_seconds()
    assert s2 == 16, f"rafaga 2: {s2} s, no 16"
    silencio = (_ts(rafaga2[0][1]) - _ts(rafaga1[-1][1])).total_seconds()
    assert silencio == 1352, f"silencio: {silencio} s, no 1352 (22 min 32 s)"
    return "rafaga 1: 2 commits en 4 s; silencio 22 min 32 s; rafaga 2: 11 en 16 s"


def check_v31():
    """Los 10 commits de la version 31 llegan en 9 segundos, huecos de 0-1 s."""
    v31 = [c for c in COMMITS if c[3].startswith("v31 completa")]
    assert len(v31) == 10, f"son {len(v31)}, no 10"
    huecos = [(_ts(b[1]) - _ts(a[1])).total_seconds()
              for a, b in zip(v31, v31[1:])]
    assert all(h in (0, 1) for h in huecos), f"huecos: {huecos}"
    span = (_ts(v31[-1][1]) - _ts(v31[0][1])).total_seconds()
    assert span == 8, f"arco v31: {span} s, no 8"
    archivos = {c[3].split("v31 completa 16/16 ", 1)[1].split(" - ")[0]
                for c in v31}
    assert len(archivos) == 10, "un archivo por commit, sin repetir"
    return "10 commits v31 en 8 s (16:46:40Z -> 16:46:48Z), huecos 0-1 s, un archivo cada uno"


def check_sin_v30():
    """No hay ningun commit v30 entre v29 y v31."""
    mensajes = [c[3] for c in COMMITS]
    assert not any("v30" in m for m in mensajes), "hay un v30"
    assert any(m.startswith("v29") for m in mensajes), "falta el v29"
    assert any(m.startswith("v31") for m in mensajes), "falta el v31"
    return "v29 presente, v31 presente, v30 ausente en los 13 mensajes"


def check_cabeza():
    """La cabeza es 0198a9d1, autor miu-tejedor, mensaje MIU Auto."""
    cabeza = COMMITS[-1]
    assert cabeza[0] == "0198a9d1", f"cabeza: {cabeza[0]}"
    assert cabeza[1] == "2026-08-23T16:46:56Z", f"fecha: {cabeza[1]}"
    assert cabeza[2] == "miu-tejedor", f"autor: {cabeza[2]}"
    assert cabeza[3] == "MIU Auto", f"mensaje: {cabeza[3]}"
    otros = [c for c in COMMITS if c[2] == "miu-tejedor"]
    assert len(otros) == 1, "miu-tejedor aparece en mas de un commit"
    return "cabeza 0198a9d1, miu-tejedor, 'MIU Auto', unico commit de ese autor"


def check_workflow_escribe_la_cabeza():
    """El workflow produce exactamente la cabeza: autor, mensaje y contenido."""
    assert 'echo "# MIU 16/16" > AUTO.md' in WORKFLOW
    assert 'git config user.name "miu-tejedor"' in WORKFLOW
    assert 'git config user.email "miu@local"' in WORKFLOW
    assert 'git commit -m "MIU Auto"' in WORKFLOW
    assert 'git push origin main' in WORKFLOW
    # Lo que el echo escribe es exactamente el contenido de AUTO.md.
    assert AUTO_MD == "# MIU 16/16\n"
    assert len(AUTO_MD.encode("utf-8")) == 12, "AUTO.md no mide 12 B"
    # El workflow llega en el commit 12, 8 s antes de la cabeza que produce.
    wf_commit = [c for c in COMMITS if c[0] == "1f892741"][0]
    delta = (_ts(COMMITS[-1][1]) - _ts(wf_commit[1])).total_seconds()
    assert delta == 8, f"del workflow a la cabeza: {delta} s, no 8"
    assert "miu-auto-deploy.yml" in wf_commit[3]
    return "workflow: echo + miu-tejedor + miu@local + 'MIU Auto' + push; AUTO.md 12 B; workflow 8 s antes de la cabeza"


CHECKS = [
    ("serie 13 commits", check_serie),
    ("dos rafagas", check_rafaga),
    ("rafaga v31", check_v31),
    ("sin v30", check_sin_v30),
    ("cabeza", check_cabeza),
    ("workflow escribe la cabeza", check_workflow_escribe_la_cabeza),
]


def main():
    fallos = 0
    for nombre, fn in CHECKS:
        try:
            print(f"PASA  {nombre}: {fn()}")
        except AssertionError as e:
            fallos += 1
            print(f"FALLO {nombre}: {e}")
    if fallos:
        print(f"NO COINCIDE: {fallos} de {len(CHECKS)} checks fallan")
        return 1
    print("TODO COINCIDE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
