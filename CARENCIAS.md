# CARENCIAS — miu-auto-dereckcitovg16-f

Lo que NO se sabe va aquí, nunca en la semilla. Cada ítem lleva dónde
se buscó (o que no se buscó) y fecha.

- **NO SÉ — si la corrida que produjo la cabeza ocurrió en GitHub
  Actions.** El registro de corridas no se consultó (2026-11-09).
  La cabeza coincide con el guion en autor, mensaje, contenido y
  tiempo, y el workflow se dispara con cada `push` a `main` — pero
  los archivos solos no descartan que alguien corriera los mismos
  comandos a mano. La confirmación está en el registro de corridas
  del repo, que no se leyó.
- **NO SÉ — qué cambió entre v29 y v31 aparte de los archivos que
  nombran los mensajes.** No hay ningún commit v30 en la serie
  (verificado en los 13 mensajes, 2026-11-09), pero no se consultó
  el contenido de los diffs, solo mensajes y fechas. El salto de
  versión sin pasos intermedios es el hecho; su contenido es NO SÉ.
- **NO SÉ — si Pages llegó a desplegarse desde miu-v14.** La
  minería de la ola 6 no lo comprobó en vivo y esta semilla tampoco
  (2026-11-09). El repo trae `_config.yml` con tema Jekyll y un
  `index.html`; el despliegue es NO SÉ.
- **NO SÉ — si `miu-tejedor` existe como cuenta.** Solo se leyó
  como autor del commit cabeza y como `user.name` en el workflow
  (2026-11-09). No se buscó el usuario en GitHub ni en ningún otro
  repo. Puede ser solo una cadena de configuración.
- **NO SÉ — si otros repos tienen cabezas escritas por workflows.**
  No se buscó fuera de `miu-v14` (2026-11-09). El patrón — un
  workflow que escribe y empuja con autor configurado — podría
  repetirse en el racimo de agosto; esta semilla no lo midió.
- **NO SÉ — qué respalda la afirmación de `polen_v133.html` de
  "24 Pages + 40 CF + R2 100GB".** El archivo la afirma sin lista
  (leído por API 2026-11-09). El índice de `miu-mesh` al que hace
  `fetch` no se leyó, y no se comprobó que la página se sirviera
  alguna vez.
- **NO SÉ — si el worker de miu-v14 sirvió alguna vez.** La
  minería de la ola 6 lo leyó entero (401 B, JSON fijo, 0 lecturas
  vivas) y esta semilla no lo ejecutó ni lo consultó en vivo
  (2026-11-09). El cuarto worker lo sembró el hermano de la tanda
  1 (`miu-auto-tabletonephantom-i`); su vida en producción es NO SÉ.
