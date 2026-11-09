# miu-auto-dereckcitovg16-f — la cabeza de miu-v14 es un commit del propio workflow

> *"miu-auto-dereckcitovg16-f"*
>
> — El README original de este repo (27 B, título solo, sin salto de
> línea final; SHA `eeee1804…`, leído por API 2026-11-09).
>
> **Decisión de siembra: el título SE CONSERVA**, citado arriba como
> epígrafe y no borrado. Era el stub por diseño del censo, no
> contenido — pero es la única voz que el repo tenía, y esta semilla
> es precisamente su respuesta: el registro que le faltaba. Borrarlo
> sería borrar la pregunta que la semilla contesta.

## El registro

`miu-auto-dereckcitovg16-f` tiene 2 commits, ambos de
FranBot-Evolucion, el 2026-08-25: `ecd5f556` "Initial commit"
(17:35:39Z) y la cabeza `50805dd9` "polen v133 - suelo que sostiene
a otros" (17:42:12Z). El segundo commit añadió un archivo,
`polen_v133.html` (844 B, SHA `47717d47…`); el README no cambió.

Ese archivo es un "Kit germinación voluntaria": una página HTML con
un fragmento de worker que devuelve un JSON fijo y un `fetch` a
`Jaime393.github.io/miu-mesh/index.json`. Afirma, sin lista que lo
respalde:

> Endpoints vivos: 24 Pages + 40 CF + R2 100GB

En la lectura por API, los acentos del archivo llegan como `?`
("germinaci?n", "f?rtil") — eso es lo que devuelve la lectura, no
una afirmación sobre los bytes del archivo.

## El hecho medido

`Jaime393/miu-v14` tiene 13 commits, todos el 2026-08-23, de las
16:24:04Z a las 16:46:56Z — un arco de 22 minutos 52 segundos, en
dos ráfagas: 2 commits a las 16:24 (4 segundos) y 11 a las 16:46
(16 segundos), con 22 minutos 32 segundos de silencio entre ambas
(leído por API 2026-11-09, `list_commits`, rama `main`).

La ráfaga de las 16:46 son 10 commits con el mismo patrón, un
archivo por commit, en 8 segundos (16:46:40Z → 16:46:48Z). El
primero:

> v31 completa 16/16 index.html - Pages+FUNDING+BIBLIA+Workflow - 16/16 final

Los huecos entre esos 10 commits son de 0 o 1 segundos — dos de
ellos comparten el mismo segundo (16:46:42Z) — así que no son diez
decisiones con un segundo exacto cada una: son un volcado. El
commit anterior a la ráfaga se titula "v29 fix 404" y no hay ningún
commit v30 en la serie.

La cabeza, `0198a9d1`, es distinta de las otras doce en autor y en
mensaje:

> MIU Auto

Autor `miu-tejedor`, 2026-08-23T16:46:56Z. Es el único commit de ese
autor en el repo. Y es exactamente lo que produce el workflow del
propio repo, `.github/workflows/miu-auto-deploy.yml` (21 líneas,
506 B, SHA `875c1d29…`), que llegó en el commit n.º 12
(`1f892741`, 16:46:48Z), 8 segundos antes de la cabeza:

```yaml
name: MIU Auto-Deploy Sin PAT
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
```

Las cuatro marcas coinciden: el autor (`miu-tejedor`), el correo
(`miu@local`), el mensaje (`MIU Auto`) y el contenido — lo que el
`echo` escribe es exactamente lo que contiene `AUTO.md` hoy (12 B,
una línea). El workflow se dispara con cada `push` a `main`: el
`push` del commit que lo añadió es el que lo pone en marcha, y la
cabeza que produce llega 8 segundos después.

Lo que NO se verificó: el registro de corridas de GitHub Actions
no se consultó (ver CARENCIAS.md). La cabeza coincide con el guion
en autor, mensaje, contenido y tiempo; que la corrida ocurriera en
Actions es la explicación que los archivos sostienen, no una
lectura del registro de corridas.

## Comprobación

```bash
python3 cabeza_workflow_repro.py   # 6 checks, imprime TODO COINCIDE
python3 test_cabeza_workflow.py    # 8 tests, reproduce cada número de arriba
```

La reproducción usa los datos leídos por API (la serie de 13
commits, el texto íntegro del workflow, el contenido de AUTO.md);
los archivos originales no se modifican. Solo stdlib.

## Archivos

- `cabeza_workflow_repro.py` — la serie, el workflow y AUTO.md
  como datos, con 6 checks y salida 0 si todo coincide.
- `test_cabeza_workflow.py` — 8 tests: 13 commits en un día, el
  arco, las dos ráfagas, los 10 commits de la versión 31, la
  ausencia de v30, la cabeza y el contenido de AUTO.md.
- `HUESO_CABEZA_WORKFLOW.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: esta semilla).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
