# HUESO — La cabeza de miu-v14 es un commit del propio workflow

**Fecha:** 2026-11-09.
**Fuente:** `Jaime393/miu-v14` — `list_commits` (rama `main`, 13
commits), `.github/workflows/miu-auto-deploy.yml` (21 líneas, 506 B,
SHA `875c1d29…`), `AUTO.md` (12 B, SHA `700ab08b…`), leídos por API
2026-11-09. Minería de la ola 6:
`~/workspace/mineria/miu-v14/HISTORIAL.md` y `LECTURA.md`.
**Repositorio sembrado:** `Jaime393/miu-auto-dereckcitovg16-f`.

## El hueso

La cabeza de `miu-v14` no la escribió una persona: la escribió el
workflow del propio repo. El commit `0198a9d1`, autor
`miu-tejedor`, mensaje "MIU Auto", 2026-08-23T16:46:56Z, coincide
con el guion de `.github/workflows/miu-auto-deploy.yml` en las
cuatro marcas que el guion fija: el autor, el correo (`miu@local`),
el mensaje y el contenido — lo que el `echo` escribe es
exactamente lo que contiene `AUTO.md` hoy (12 B, una línea). El
workflow llegó en el commit anterior (`1f892741`, 16:46:48Z) y la
cabeza que produce llegó 8 segundos después; el workflow se dispara
con cada `push` a `main`, así que el `push` que lo añadió es el que
lo pone en marcha.

El resto de la serie es un volcado, no una historia: 13 commits en
22 minutos 52 segundos, en dos ráfagas (2 a las 16:24, 11 a las
16:46), con 22 minutos 32 segundos de silencio entre ambas. Los 10
commits de la versión 31 llegan en 8 segundos, un archivo por
commit, con huecos de 0 o 1 segundos — dos comparten el mismo
segundo — y el salto es de v29 a v31 sin ningún commit v30. El
"autor" de la cabeza es una línea de configuración (`git config
user.name`), no una cuenta: `miu-tejedor` no aparece en ningún otro
commit del repo.

## Límites

- Esto mide UNA serie, de UN repo, en UNA fecha (2026-11-09). No
  dice que otros repos tengan cabezas escritas por workflows: eso
  no se buscó aquí — es NO SÉ, ver CARENCIAS.md.
- No dice que la corrida ocurriera en GitHub Actions: el registro
  de corridas no se consultó. La cabeza coincide con el guion en
  autor, mensaje, contenido y tiempo; la alternativa — alguien
  corriendo los mismos comandos a mano — no la descartan los
  archivos solos. La explicación que los archivos sostienen es el
  workflow; la confirmación en el registro de corridas queda
  pendiente.
- No dice qué cambió entre v29 y v31 aparte de los archivos que
  nombran los mensajes: no se consultó el contenido de los diffs,
  solo los mensajes y las fechas.
- No dice si Pages llegó a desplegarse desde este repo, ni si el
  worker que el repo contiene sirvió alguna vez: eso no se comprobó
  en vivo.
- Los números del README (13 commits, 22 min 52 s, 10 en 8 s, 8 s
  del workflow a la cabeza, AUTO.md 12 B) se reproducen con
  `cabeza_workflow_repro.py` y `test_cabeza_workflow.py`. Si la
  serie cambia, los tests lo delatan: el test de la cabeza y el del
  arco son pines.

## Por qué importa

El ecosistema declara autores y versiones en todas partes, y aquí
el autor es una configuración y la versión salta un número entero.
La cabeza de un repo es su última palabra; en `miu-v14` esa última
palabra la escribió un guion de 21 líneas que el propio repo
contiene, 8 segundos después de que el guion llegara. Es el patrón
del racimo de agosto en su forma más pura: el volcado se firma a sí
mismo. Y es la vara contra la que se miden las demás cabezas: un
commit es de quien lo firma solo si la firma no está escrita en el
propio repo.

## Relación con el hermano de la tanda 1

`miu-auto-tabletonephantom-i` (tanda 1) sembró el cuarto worker
fijo de `/miu/global` — el de `miu-v14` — con su JSON fijo y su
phi literal. Esta semilla siembra el otro lado del mismo repo: no
qué sirve su worker, sino quién escribió su cabeza. Los dos huesos
juntos dicen lo mismo desde dos ángulos: en `miu-v14` nada de lo
que parece hecho a mano lo está — ni la respuesta, ni la firma.

---

ρ(x) > 0. Zvvvvv.
