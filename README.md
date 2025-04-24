# Proyecto Pac‑Man en MARIE

Este repositorio contiene la implementación del clásico juego **Pac‑Man** sobre el simulador **MARIE** (Machine Architecture that is Really Intuitive and Easy). El objetivo principal es ilustrar conceptos de arquitectura de computadores (gestión de memoria, control de flujo, subrutinas y lógica de colisiones) mediante código de bajo nivel.

## Contenido del repositorio

- `pacman_marie.mas` — Código fuente en ensamblador MARIE (última versión).  
- `movPac.py` — Generador de `pacMovimientos` en Python (evita giros de 180°).  
- `movGhost.py` — Generador de `ghostMovimientos` en Python (direcciones uniformes).  
- `pacman_marie_paper.tex` — Short paper en formato IEEE que documenta diseño, metodología, resultados y conclusiones.  
- `README.md` — Guía de uso y descripción de la arquitectura implementada.

## Requisitos

- **MARIE Simulator**: para compilar y ejecutar programas en MARIE.  
- **Python 3**: para ejecutar `movPac.py` y `movGhost.py`.  
- **TeX Live** (o similar): para compilar el documento LaTeX.

## Generar vectores de movimiento

Para actualizar las secuencias de movimiento basta con ejecutar los scripts y copiar su salida:

```bash
python movPac.py     # imprime en consola las 100 líneas DEC para pacMovimientos
python movGhost.py   # imprime en consola las 100 líneas DEC para ghostMovimientos
```
## Estructura de `pacman_marie.mas`

1. **Inicialización de Datos**
   - `pacMovimientos` y `ghostMovimientos` se generan mediante los scripts Python `movPac.py` y `movGhost.py`, que imprimen las 100 líneas `DEC` necesarias (1=arriba, 2=abajo, 3=izquierda, 4=derecha) para copiar directamente en `pacman_marie.mas`.
   - Secciones de mapa: colores de fondo, muros (`PARED_COLOR`), monedas (`BOLITA_COLOR`), esteroides (`ESTEROIDE_COLOR`) y personajes (`BLINKY_COLOR`, `INKY_COLOR`, `PINKY_COLOR`, `CLYDE_COLOR`, `PAC-MAN_COLOR`).
   - Variables globales: `vidas`, `score`, punteros (`ptrPac`, `ptrGhost`), contadores y estado de esteroide.

2. **Renderizado del Mundo**
   - Subrutina `drawInDisplay()`: mapea un arreglo lineal de 16×16 posiciones (offset `0xF00`) a píxeles en memoria de video.

3. **Generación de Movimientos**
   - `getMovPac()` y `getMovGhost()`: leen y avanzan punteros circulares sobre los vectores de direcciones, reiniciando contadores al llegar a 100.

4. **Lógica de Personajes**
   - **Pac‑Man** (`pacmanLogic()`): evita muros (`isPared()`), gestiona esteroides (`isEsteroide()`), actualiza puntaje (`getScore()`), detecta colisiones (`GameOver`) y refresca pantalla (`moverse()`).
   - **Fantasmas** (`ghostLogic()`): identifica cada fantasma por `id`, restablece color previo, evita borrar objetos valiosos (`atravesar()`) y redibuja.

5. **Prevención de Colisiones**
   - `isPared()`: detiene movimiento si hay muro.
   - `touchPacman()`: detecta choque fantasma–Pac‑Man y llama a `HandleLifeLoss()`.

6. **Gestión de Estado**
   - **Puntuación**: +1 por moneda (`setScoreBolita()`), +10 por fantasma (`setScoreFantasma()`).
   - **Vidas**: decremento en `HandleLifeLoss()`; si 
     - `vidas > 0` → `ResetPositions()`.  
     - `vidas == 0` → `FINAL` y fin de ejecución.
   - **Esteroides**: activación por `STEP_LIMIT` pasos, con contador y restauración de color.

7. **Restablecimiento de Posiciones**
   - `ResetPositions()`: limpia sprites, reubica personajes en coordenadas iniciales, restaura colores y retoma flujo.

8. **Finalización**
   - `FINAL`: imprime `score` en `Output` y ejecuta `Halt`.

## Uso

1. Inicia MARIE Simulator.
2. Abre y ensambla `pacman_marie.mas`.
3. Ejecuta el programa y observa el display.
4. Al finalizar, el score aparece en la sección `Output`.

## Personalización

- **Recorridos**: modifica `pacMovimientos` y `ghostMovimientos`.
- **Mapa**: ajusta los datos bajo la etiqueta `MAPA`.
- **Esteroides**: cambia `STEP_LIMIT`.
- **Colores**: redefine constantes hexadecimales.

## Documentación Académica

El short paper (`pacman_marie_paper.tex`) incluye:
- Arquitectura de memoria y diseño de subrutinas.
- Pseudocódigo de alto nivel.
- Ejemplos de ejecución y resultados.
- Conclusiones y perspectivas de extensión.

Para compilar el documento:
```bash
detectnull= pdflatex pacman_marie_paper.tex
```

## Perspectivas de Extensión

Estas mejoras podrían enriquecer el proyecto:
- **IA avanzada**: algoritmos de búsqueda (A*, BFS) para persecución de fantasmas.
- **Laberintos procedurales**: generación automática de mapas con algoritmos DFS o Prim.
- **Interfaz gráfica externa**: aplicación en Python, JavaScript o Flutter que lea la memoria de MARIE y ofrezca control en tiempo real.

## Autores

- Gabriel Ávalos
- David Bucheli
- Jhonatan Quiroga

**Universidad San Francisco de Quito (USFQ)**

## Licencia

Proyecto de uso educativo. Para otros usos, contactar a los autores.

