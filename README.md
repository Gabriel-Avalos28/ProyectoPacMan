# Proyecto Pac‑Man en MARIE

Este repositorio contiene la implementación completa del juego **Pac‑Man** sobre el simulador **MARIE** (Machine Architecture that is Really Intuitive and Easy). El objetivo es demostrar conceptos de arquitectura de computadores: manejo de memoria, control de flujo, subrutinas y lógica de colisiones usando código de bajo nivel.

## Contenido

- `pacman_marie.asm` &mdash; Código fuente en ensamblador MARIE (última versión).
- `pacman_marie_paper.tex` &mdash; Short paper en formato IEEE (LaTeX) que documenta diseño, metodología, resultados y conclusiones.
- `README.md` &mdash; Documentación y guía de uso.

## Requisitos

- **MARIE Simulator**: entorno educativo para ejecutar y depurar programas escritos en MARIE.
- **TeX Live** o similar: para compilar el documento LaTeX (`pacman_marie_paper.tex`).


## Estructura de `pacman_marie.asm`

1. **Inicialización de Datos**
   - Vectores `pacMovimientos` y `ghostMovimientos` con direcciones aleatorias (valores 1–4).
   - Secciones de mapa: colores de fondo, muros (`PARED_COLOR`), monedas (`BOLITA_COLOR`), esteroides (`ESTEROIDE_COLOR`).
   - Variables de estado globales: `vidas`, `score`, punteros y contadores.

2. **Renderizado del Mundo**
   - Subrutina `drawInDisplay()` dibuja cada pixel en la memoria de video.
   - El display se modela como un arreglo lineal de 16×16 posiciones a partir de la dirección `OFFSET`.

3. **Lógica Principal**
   - Etiqueta `PACMAN` y `CLYDE`, `INKY`, `PINKY`, `BLINKY`: lectura de posición, color y salto a `getMovPac()` o `getMovGhost()`.
   - `getMovPac()`, `getMovGhost()`: obtienen la siguiente dirección usando punteros circulares y reinician contadores.
   - `INICIO`: determina la dirección (arriba, abajo, izquierda, derecha) y llama a la subrutina de movimiento.

4. **Prevención de Colisiones**
   - `isPared()`: evita avanzar sobre muros.
   - `touchPacman()`: detecta colisión Pac‑Man vs fantasma y llama a `HandleLifeLoss()`.

5. **Estado de Juego**
   - **Puntuación**: cada moneda vale +1 (`setScoreBolita()`), cada fantasma +10 (`setScoreFantasma()`).
   - **Vidas**: contador `vidas` decrementa en `HandleLifeLoss()`. Si llega a 0, salta a `FINAL`.
   - **Esteroides**: al ingresar a casilla de color `ESTEROIDE_COLOR`, activa modo agresivo por `STEP_LIMIT` pasos.

6. **Finalización**
   - `FINAL`: imprime `score` en la consola de MARIE y finaliza con `Halt`.


## Uso

1. Abre el simulador MARIE.
2. Carga `pacman_marie.asm`.
3. Ensambla y ejecuta.
4. Observa el laberinto generado, movimientos automáticos de Pac‑Man y fantasmas.
5. En la sección de salida (`Output`), aparecerá el puntaje final.


## Personalización

- **Mapas y posiciones**: edita los vectores `pacMovimientos`, `ghostMovimientos` o los bloques de datos de `MAPA` para cambiar el recorrido o la distribución de muros.
- **Duración de esteroides**: modifica `STEP_LIMIT` al valor deseado.
- **Colores**: ajusta constantes como `PARED_COLOR`, `BOLITA_COLOR`, `ESTEROIDE_COLOR` con otros valores hexadecimales.


## Documentación Académica

El short paper (`pacman_marie_paper.tex`) describe detalladamente:

- Metodología de diseño y organización en memoria.
- Pseudocódigo de alto nivel.
- Resultados de pruebas y ejemplos de ejecución.
- Conclusiones y posibles extensiones.

Para compilar:
```
pdflatex pacman_marie_paper.tex
```


## Autores

- Gabriel Ávalos
- David Bucheli
- Jhonatan Quiroga

Universidad San Francisco de Quito (USFQ)


## Licencia

Este proyecto es de uso educativo y está libre para fines académicos. Para cualquier reproducción fuera de este contexto, contactar a los autores.

