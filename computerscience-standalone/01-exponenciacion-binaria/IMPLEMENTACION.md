# Exponenciación binaria: escenas Manim CE

Diez escenas independientes basadas en `guion.md`. La paleta global vive en
`../../styles/theme.py`; `scene_utils.py` contiene los componentes visuales del
proyecto. El archivo previo `scene.py` y el guion se conservan.

Todo texto visible se compone mediante LaTeX: `Tex` para prosa y código,
`MathTex` para fórmulas, números y bits. El contador `Integer` utiliza
explícitamente `MathTex` para sus dígitos. No se utilizan fuentes del sistema.
`escape_tex` protege caracteres especiales de prosa y código; las fórmulas se
pasan directamente a `formula`, sin escapar su sintaxis matemática.

## Ejecución

Desde esta carpeta, con el entorno existente `manim-env` activo:

```sh
manim -ql -s scene_01_gancho.py Escena01Gancho
python render_all.py --stills
python render_all.py
```

El primer comando guarda el fotograma final de una escena; el segundo verifica
las diez escenas con ese mismo modo; el tercero genera diez videos de baja
calidad. Los PNG están en `media/images/` y los MP4 en `media/videos/`.
Los registros de cada ejecución están en `media/verification/`.
El verificador termina con error si encuentra fallos o advertencias.

| Archivo | Clase |
| --- | --- |
| scene_01_gancho.py | Escena01Gancho |
| scene_02_memoria.py | Escena02Memoria |
| scene_03_modular.py | Escena03Modular |
| scene_04_naive.py | Escena04Naive |
| scene_05_intuicion.py | Escena05Intuicion |
| scene_06_exponentes.py | Escena06Exponentes |
| scene_07_binario.py | Escena07Binario |
| scene_08_traza.py | Escena08Traza |
| scene_09_codigo.py | Escena09Codigo |
| scene_10_cierre.py | Escena10Cierre |

## Decisiones de precisión para la locución

Antes de grabar, ajustar la narración original a las cifras de las escenas:

- Escenas 01 y 10: un millón tiene 20 bits. El código mostrado hace 20
  iteraciones, 20 cuadrados y 7 productos del acumulador: 27 multiplicaciones.
  El método ingenuo que parte de 3 hace 999 999 multiplicaciones.
- Escena 02: la potencia tiene 477 122 dígitos y necesita 1 584 963 bits
  (aproximadamente 194 KiB de datos binarios, sin sobrecarga del objeto).
  No cabe en un entero fijo de 64 bits, pero sí se puede almacenar en RAM
  con precisión arbitraria. La magnitud astronómica no impide su almacenamiento.
- Escena 03: obtener el residuo es un objetivo diferente de obtener el entero
  completo. Para M = 10^9 + 7 y factores reducidos no negativos, el producto
  cabe en 64 bits con signo. No es una garantía para cualquier módulo.
- Escena 08: se aplica módulo M desde el comienzo. El resultado es 288 603 514.
  Se conserva el último cuadrado, aunque ya no sea necesario, para corresponder
  exactamente al código de la escena 09: cinco iteraciones, ocho multiplicaciones.
- Escena 09: para n > 0, la cantidad exacta de bits es floor(log2(n)) + 1.
  El código presentado supone base y exponente no negativos y M = 10^9 + 7.
  O(log n) describe el número de operaciones aritméticas con módulo fijo.
- Escena 10: el residuo de la potencia inicial es 64 935 414.

## Audio y ritmo

Los comentarios `[TRIGGER_n]` identifican los bloques de la locución. Las pausas
y duraciones son una base visual editable, no una sincronización con audio
grabado. Los videos se generan sin narración ni música. La escena final conserva
una tarjeta legible al terminar para permitir revisar también su PNG.

La paleta respeta `COLOR_MODULO = "#6366F1"` solicitado; `COLOR_CYAN` aporta
el cian adicional del guion. Se utiliza `Create`, compatible con Manim CE,
en lugar de `ShowCreation`.
