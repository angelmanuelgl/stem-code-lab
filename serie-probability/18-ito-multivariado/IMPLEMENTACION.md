# Video 18: Itô multivariado — implementación Manim CE

Se implementan las ocho escenas de `guion.md`, conservando el guion original.
La carpeta real del video 18 es `18-ito-multivariado`: no corresponde al tema de
funciones características, que está en el video 10 del roadmap.

## Ejecución

Activar el entorno existente `manim-env` y situarse en esta carpeta:

```sh
manim -ql -s scene_01_dos_sensores_oyen_parte_del_mismo_ruido.py Escena01DosSensoresOyenParteDelMismoRuido
python render_all.py
python render_all.py --videos
python test_scenes.py
```

`render_all.py` ejecuta las ocho escenas secuencialmente. Sin opciones utiliza
`-ql -s`: verifica la ejecución y guarda el fotograma final. Con `--videos`
produce los ocho MP4 de prueba a 480p y 15 fps. Ambos modos devuelven código
distinto de cero si alguna escena falla y guardan el detalle en
`media/verification/`, junto con un resumen JSON de códigos de salida.

## Módulos

| Archivo | Clase |
| --- | --- |
| `scene_01_dos_sensores_oyen_parte_del_mismo_ruido.py` | `Escena01DosSensoresOyenParteDelMismoRuido` |
| `scene_02_construir_ruidos_correlacionados.py` | `Escena02ConstruirRuidosCorrelacionados` |
| `scene_03_la_suma_de_productos_cruzados.py` | `Escena03LaSumaDeProductosCruzados` |
| `scene_04_el_estado_y_las_fuentes_tienen_tamanos_distintos.py` | `Escena04ElEstadoYLasFuentesTienenTamanosDistintos` |
| `scene_05_la_hessiana_recoge_todas_las_curvaturas.py` | `Escena05LaHessianaRecogeTodasLasCurvaturas` |
| `scene_06_el_producto_revela_la_correlacion.py` | `Escena06ElProductoRevelaLaCorrelacion` |
| `scene_07_energia_de_un_sistema.py` | `Escena07EnergiaDeUnSistema` |
| `scene_08_evitar_contar_dos_veces_la_correlacion.py` | `Escena08EvitarContarDosVecesLaCorrelacion` |

`scene_utils.py` comparte componentes de LaTeX, geometría y distribución de
elementos. Todos los colores se importan de `styles/theme.py`; no se modifica
ese módulo ni se definen nuevos tonos. Cada escena asigna el fondo al comenzar.
Toda la prosa visible usa `Tex`; las fórmulas y números usan `MathTex`, también
los elementos de las matrices. Los ejes no generan etiquetas de texto automáticas.

## Correspondencia con el guion y precisión

- Cada escena contiene exactamente tres comentarios `[TRIGGER_1]` a
  `[TRIGGER_3]`, que identifican los bloques de animación de la locución.
  Son puntos de edición; no existe todavía una pista de voz grabada ni una
  sincronización automática con audio. Las pausas se pueden ajustar al doblaje.
- Escena 01: 3000 incrementos con semilla 1801; mismos datos normales para
  correlaciones 0, 0.7 y -0.7. La nube representa incrementos normalizados por
  la raíz de su duración y ambos ejes usan la misma escala.
- Escena 02: la construcción permanece definida en los extremos ±1 mediante
  la mezcla explícita, sin intentar una factorización de Cholesky singular.
- Escena 03: 4096 incrementos finos, semilla 1803. Las mallas de 16, 64 y 256
  intervalos se obtienen agrupando esos mismos incrementos. El contador y la
  curva acumulada usan las barras reales; la recta discontinua marca el límite
  terminal, no el valor obligatorio de una suma finita.
- Escena 04: ejemplo rectangular de tres estados y dos ruidos. Las etiquetas
  distinguen claramente la representación independiente de la correlacionada.
- Escena 05: superficie cuadrática representada en proyección oblicua sobre
  una escena 2D. El vector mostrado tiene la dirección del gradiente, ampliada
  para facilitar su lectura. Se conservan los cuatro pares de la contracción.
- Escena 06: media del producto de 4000 trayectorias, semilla 1806, frente al
  valor exacto. La banda es puntual ±2 errores estándar estimados; no es una
  banda simultánea ni una garantía determinista.
- Escena 07: OU bidimensional con parámetros del guion y estado inicial
  `(1.1, 0.6)`. Los puntos de la trayectoria se obtienen con la transición
  exacta del OU, semilla 1807, y se unen para visualizarlos. Las barras describen
  el balance de la energía **media**, no una igualdad trayectoria por trayectoria.
- Escena 08: comprobación numérica con correlación 0.6 y difusión identidad:
  aplicar dos veces el factor eleva la segunda varianza de 1 a 1.576.

## Salidas

- `media/images/`: ocho fotogramas finales de prueba.
- `media/videos/`: ocho animaciones de prueba sin audio y archivos intermedios de Manim.
- `media/verification/`: registros de cada renderizado y resúmenes reproducibles.

Los renders de baja calidad validan ejecución y composición; para producción
se puede sustituir `-ql` por `-qh` y ajustar los tiempos a la locución definitiva.
