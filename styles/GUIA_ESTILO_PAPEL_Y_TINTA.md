# Guía de Identidad Visual: "Papel y Tinta"

**Another Math Channel · by AngelGL**

> Principio rector: *cada trazo es una decisión de tinta.* Si un elemento no guía la mirada, no entra. Lo que ya está en pantalla se comporta como tinta seca; lo nuevo se dibuja como pluma.

La estética es una elección deliberada: una página de cuaderno de investigación o de un libro de posgrado, no un "modo claro" de Manim. Lo que la separa de un borrador es la **disciplina**: pocos valores de gris, pocos grosores, una sola tipografía y un único acento.

---

## 1. Especificaciones técnicas para Manim

### 1.1 Paleta

| Rol | Nombre | Hex | Uso |
|---|---|---|---|
| Fondo | `PAPER` | `#F7F6F1` | Fondo de todas las escenas. Papel cálido: reduce el brillo de un blanco puro y hace que la tinta "asiente". |
| Tinta principal | `INK` | `#1B1B1F` | Texto, objeto principal, funciones, trazo protagonista. |
| Tinta secundaria | `INK_SOFT` | `#4B4B53` | Ejes, anotaciones, texto de apoyo, ecuaciones secundarias. |
| Gris estructural | `GRAPHITE` | `#8C8C92` | Contexto, elementos "ya vistos", fondo decorativo. |
| Cuadrícula | `RULE` | `#D8D5CB` | Papel milimetrado, filetes de fondo. Casi invisible a propósito. |
| Acento | `ACCENT` (carmín) | `#B1262B` | **Un solo foco por momento.** Ver 3.3. |

Reglas de color:

- No hay más colores. Si necesitas distinguir cosas, usa **grosor, punteado, relleno/hueco u opacidad** antes que un color nuevo.
- Con opacidad: las áreas de acento usan carmín al **15–20 %** (lavado de tinta), nunca sólido.
- Un segundo acento (azul pluma `#234A8C`) está **reservado** para videos con dos magnitudes que se contrastan (p. ej. "antes / después"). No lo uses por defecto.
- Para **impresión** (tarjetas, stickers, póster) se usa tinta pura `#000` sobre blanco `#FFF`, sin grises (ver 6).

### 1.2 Grosores de trazo (`stroke_width`)

| Constante | Valor | Se usa en |
|---|---|---|
| `SW.GRID` | 0.8 | Cuadrícula de fondo |
| `SW.HAIR` | 1.2 | Filetes finos, marcos interiores |
| `SW.AUX` | 1.8 | Líneas auxiliares, construcciones punteadas, contexto |
| `SW.AXIS` | 2.0 | Ejes |
| `SW.FRAME` | 2.5 | Marcos, aristas de grafos |
| `SW.CURVE` | 3.5 | **Funciones y objeto principal** |
| `SW.ACCENT` | 4.5 | Trazo de acento carmín |
| `SW.EMPHASIS` | 5.0 | Máximo énfasis en tinta (uso excepcional) |

Regla de proporción: cada nivel es ~1.3–1.5× el anterior. **Nunca más de 3 grosores distintos en un mismo plano**, y la diferencia entre dos grosores vecinos debe ser visible a simple vista; si no lo es, son el mismo grosor.

Nada por debajo de 1.2 en tinta: los trazos muy finos vibran al comprimirse en YouTube.

### 1.3 Tipografía

- **Todo en LaTeX** (`MathTex` / `Tex`). Un solo sistema tipográfico: Computer Modern (el de los libros de texto). Es lo que da la sensación de "libro de posgrado".
- Evita `Text()` con fuentes del sistema. Para texto monoespaciado (URLs, etiquetas de código) usa `Tex(r"\texttt{...}")`.
- Títulos en `\textbf{}`, notas en `\textit{}`; no mezcles más de dos estilos en el mismo bloque.
- Escala de tamaños (frame 16×9):

| Constante | pt | Uso |
|---|---|---|
| `FS.TITLE` | 56 | Título de escena / sección |
| `FS.HEAD` | 44 | Ecuación o enunciado central |
| `FS.BODY` | 36 | Cuerpo, pasos de demostración |
| `FS.NOTE` | 28 | Anotaciones al margen |
| `FS.MICRO` | 22 | Mínimo legible en video (etiquetas) |

Los tamaños menores a 22 solo se permiten en **decoración** (no transmite información, como las fórmulas del banner).

- Opcional: si quieres una voz más "editorial" que Computer Modern, usa `TexTemplate` con `\usepackage{mathpazo}` (Palatino). Elige una vez y no la cambies entre videos.

### 1.4 Código base

Todo lo anterior está implementado en **`paper_theme.py`** (`PAPER`, `INK`, `SW`, `FS`, `PaperScene`, `tex()`, `node()`, `edge()`, `pen_axes()`). Cada escena hereda de `PaperScene`, que ya pone el fondo:

```python
from paper_theme import *

class MiEscena(PaperScene):
    def construct(self):
        ax = pen_axes([0, 5, 1], [-1, 3, 1], 8, 4)
        f = ax.plot(lambda x: np.log1p(x), color=INK, stroke_width=SW.CURVE)
        self.play(Create(ax), run_time=1.2)
        self.play(Create(f), run_time=1.6)
```

---

## 2. Lenguaje visual: cómo "habla" la tinta

Un código fijo y consistente en todos los videos. El espectador lo aprende sin que se lo expliques.

| Rasgo | Significa |
|---|---|
| Línea **sólida** | Relación establecida, cosa demostrada |
| Línea **punteada** | Auxiliar, hipotética, construcción, "supongamos que…" |
| Nodo / punto **relleno** | Dato, valor conocido, objeto fijo |
| Nodo / punto **hueco** | Incógnita, variable, objeto por determinar |
| **Recuadro negro** con texto en papel | Etiqueta o categoría (inversión de tinta) |
| Lavado **carmín** al 18 % | La región / cantidad que se está calculando |
| Subrayado o trazo **carmín** | El paso clave, el *core insight* |
| Elemento en **GRAPHITE** | Contexto: ya se vio, o es el telón de fondo |

---

## 3. Lineamientos de composición

### 3.1 Jerarquía visual (solo con peso y tipografía)

Tres niveles de tinta, más un acento:

1. **Protagonista** (`INK`, `SW.CURVE`, `FS.HEAD`/`BODY`): lo que se está explicando *ahora*. Un solo protagonista por plano.
2. **Soporte** (`INK_SOFT`, `SW.AXIS`, `FS.NOTE`): ejes, definiciones, ecuaciones de apoyo.
3. **Contexto** (`GRAPHITE`, `SW.AUX`, opacidad 0.5–0.7): lo ya visto, lo que da orientación.
4. **Acento** (`ACCENT`): *una cosa por momento.* Si dos elementos están en carmín al mismo tiempo, ninguno destaca.

Cuando algo pasa de protagonista a "ya visto", **desciende un nivel** (INK → INK_SOFT → GRAPHITE), no desaparece de golpe. Así la página va acumulando historia, como un cuaderno.

Test del entrecerrar los ojos: si al desenfocar la pantalla no ves dónde está el protagonista, sobra tinta en el resto.

### 3.2 Retícula y márgenes

- Frame 16×9. **Margen exterior de 0.6 u**; la zona de trabajo es 14.8 × 7.8.
- Título de sección: arriba-izquierda, `FS.TITLE`, con un filete `SW.HAIR` debajo (como encabezado de página).
- Anotaciones tipo **marginalia** (`FS.NOTE`, `INK_SOFT`, `\textit{}`) en el margen derecho, unidas al objeto con una línea punteada `SW.AUX`.
- Deja **al menos 30 % del cuadro en blanco**. El papel vacío es parte del diseño.
- Cuadrícula `RULE` solo cuando el espacio coordenado importa. En escenas conceptuales, fondo liso.

### 3.3 Reglas del acento

- Máximo **un elemento carmín** simultáneo (dos si son la misma cosa: p. ej. un área y su etiqueta).
- El carmín se **gana**: el objeto entra en tinta y *pasa* a carmín cuando llega el momento clave.
- Al terminar el momento, regresa a `INK` o desciende a `GRAPHITE`.

### 3.4 Errores a evitar (lecciones de la tarjeta)

1. **Marcos que cruzan texto.** El halo circular de la primera versión cortaba el título "Another Math Channel". El contenedor debe ser **más grande que el contenido** o no existir; por eso el banner usa un cartucho rectangular con marco doble.
2. **Retícula de puntos tocando fórmulas.** Un fondo decorativo nunca debe pisar texto: o se recorta, o se tapa con un relleno `PAPER`.
3. **Mezclar demasiados "idiomas" decorativos** (puntos, mallas, punteados, marcos) en un cuadro pequeño. En formatos chicos, 3 recursos como máximo.
4. **Grises en impresión.** Un gris se vuelve tramado sucio; en impreso solo tinta pura.

---

## 4. Animación

La metáfora: **una pluma escribiendo sobre papel.** Nada rebota, nada brilla, nada gira porque sí.

### 4.1 Lo que sí

| Intención | Animación | Duración |
|---|---|---|
| Aparece un objeto geométrico / curva | `Create` (trazo dibujándose), `rate_func=smooth` | 1.2–1.8 s |
| Aparece texto o ecuación | `Write` (rápido) o `FadeIn(shift=0.1*UP)` | 0.8–1.2 s |
| Transformar una expresión en otra | `TransformMatchingTex` | 1.2–1.6 s |
| Marcar el paso clave | `Create(Underline(obj, color=ACCENT))` o `Circumscribe` con `ACCENT`, `fade_out=True` | 0.8–1.0 s |
| Descartar / corregir | Un tachado `Line` en `INK` (`SW.AXIS`) y luego `FadeOut` | 0.6 s |
| Devolver al contexto | `obj.animate.set_color(GRAPHITE).set_opacity(0.6)` | 0.6 s |
| Rellenar un área | `FadeIn` del lavado carmín (`opacity=0.18`) | 1.0 s |

Recetas:

```python
# Trazo de pluma
self.play(Create(curve), run_time=1.6, rate_func=smooth)

# Destacar el paso clave: subrayado carmín que se dibuja
ul = Underline(eq, color=ACCENT, stroke_width=SW.ACCENT)
self.play(Create(ul), run_time=0.8)

# Bajar un elemento a contexto
self.play(old.animate.set_color(GRAPHITE).set_opacity(0.6), run_time=0.6)

# "Pasar la hoja": un filete cruza la pantalla y se limpia la página
rule = Line(LEFT * 8, RIGHT * 8, stroke_color=INK, stroke_width=SW.HAIR).shift(UP * 4.5)
self.play(Create(rule), run_time=0.3)
self.play(FadeOut(*self.mobjects), run_time=0.5)
```

### 4.2 Ritmo

- **Una idea nueva por beat.** No lances más de 2–3 animaciones simultáneas.
- Pausa de **0.4–0.8 s** (`self.wait`) después de cada idea clave: es el silencio del lector.
- `rate_func=smooth` por defecto. `linear` solo para trazos largos tipo "pluma constante". Prohibido `there_and_back`, `rush_from` y rebotes (`ease_out_bounce`).
- Mantén `lag_ratio` entre 0.05–0.15 al dibujar grupos, para que se sienta escritura y no aparición en bloque.

### 4.3 Lo que no

- Brillos, glow, sombras, degradados.
- Rotaciones o zooms decorativos; cámara moviéndose "porque sí". Si la cámara se mueve, es para seguir el razonamiento.
- 3D salvo que el tema lo exija; y si lo exige, en tinta con `SW.AUX` y sin superficies sombreadas.
- Colores nuevos "solo esta vez".
- `Indicate` con su pulso grande, `Flash`, `ShowPassingFlash` brillante.

### 4.4 Transiciones entre secciones

1. **Pasar la hoja** (filete + fade, 0.8 s total): cambio de tema.
2. **Continuación en la misma página**: el contenido antiguo desciende a `GRAPHITE` y se desplaza hacia arriba/izquierda (`shift`), y se escribe debajo. Ideal para demostraciones encadenadas.
3. **Corte limpio** con pausa de 0.5 s en papel vacío: entre capítulos mayores.

---

## 5. Banner del canal

Archivo: **`banner_paper.py`** (escena `YouTubeBannerPaper`, 2048×1152).

```
manim -s banner_paper.py YouTubeBannerPaper
```

### 5.1 Decisiones de diseño

- **Fondo:** `PAPER` con cuadrícula `RULE` muy tenue (papel milimetrado).
- **Cartucho central:** marco doble (`SW.FRAME` + `SW.HAIR`) relleno de papel, que limpia la cuadrícula tras el título. Reemplaza al halo circular, que cortaba el texto. Cabe en la zona segura de móviles (5.2 × 2.3 < 9.65 × 2.64).
- **Contenido del cartucho:** título en negrita `INK`, filete **carmín** (acento), "by **AngelGL**", y el subtítulo CS • Math • Physics en recuadro de tinta invertida (el mismo recurso de la tarjeta).
- **Acento único del banner:** el filete bajo el título y el lavado carmín del área bajo la curva. Nada más es carmín.
- **Columnas de móvil** (|x| ≤ 4.825): `O(log n)`, mini gráfica de cálculo, `KMP · DP`; `A = UΣVᵀ`, matriz de rotación, integral gaussiana. Tinta `INK` / `INK_SOFT`.
- **Columnas de escritorio** (|x| 4.8–8, |y| ≤ 1.65): Navier–Stokes, procesos de Itô, factor de Lorentz; ecuación de Bellman, tensor de Riemann, rotacional.
- **Franja solo-TV:** grafo en las esquinas (nodos rellenos/huecos, aristas sólidas/punteadas en `GRAPHITE`), etiquetas de algoritmos y fórmulas de los demás temas (topología, límites, variedades, Cantor, convolución…), todo en gris de contexto.

### 5.2 Verificación

1. Pon `DEBUG = True` en el script y renderiza: el rectángulo rojo es la zona de móviles y el amarillo la de escritorio. Todo lo que comunica (título, autor, subtítulo) debe estar dentro del rojo.
2. Revisa que ninguna fórmula decorativa cruce el cartucho ni los bordes del cuadro.
3. Reduce la imagen a ~600 px de ancho: el título debe seguir leyéndose.
4. Sube el PNG; el límite de YouTube es 6 MB.

---

## 6. Impresos (tarjeta, stickers)

El mismo sistema, pero en **tinta pura** (`#000` sobre `#FFF`, sin grises): marco doble, retícula de puntos en vez de malla, recuadro negro invertido como único punto de contraste, trazos ≥ 2.5. Ver `card_front_bw.py` y `make_sheet_bw.py`.

---

## 7. Checklist antes de renderizar cualquier video

- [ ] ¿Fondo `PAPER` y escena heredando de `PaperScene`?
- [ ] ¿Solo colores de la paleta? ¿Un único acento por momento?
- [ ] ¿Máximo 3 grosores distintos y ninguno bajo 1.2?
- [ ] ¿Un solo protagonista por plano; lo viejo desciende a contexto?
- [ ] ¿Todo es LaTeX, con tamaños ≥ `FS.MICRO` en lo informativo?
- [ ] ¿Sólido = establecido, punteado = auxiliar, relleno = dato, hueco = incógnita?
- [ ] ¿Animaciones de pluma (`Create`, `Write`), sin rebotes, brillos ni giros?
- [ ] ¿Al menos 30 % del cuadro libre?

---

## 8. Nota sobre el repositorio

La sección 2 del `MANIFIESTO.md` actual describe la estética "Modern Dark / Slate" (`#181C24`). Si esta identidad reemplaza a la anterior, actualiza ese apartado y mueve la paleta a `styles/theme.py` (copiando `paper_theme.py`) para que todas las escenas compartan una sola fuente de verdad. Los videos que ya hayas empezado en oscuro pueden quedar como serie aparte, o migrarse cambiando solo el tema.
