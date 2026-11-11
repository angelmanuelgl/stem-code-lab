# Storyboard Manim — ICPC México 2026 (Segunda Parte)

## Convenciones de producción

- **Tiempos:** estimaciones de edición, no texto que aparezca en pantalla. Se calculan con una locución aproximada de 125–140 palabras por minuto y pausas para lectura; se deben ajustar al grabar la voz. Los fragmentos de entrevistas no tienen duración definida, así que su tiempo es provisional.
- **Sistema visual:** usar la identidad de `paper_theme.py`: papel `PAPER` (#F7F6F1), tinta `INK` (#1B1B1F), texto auxiliar `INK_SOFT`, líneas suaves `RULE` y un acento `ACCENT` (#B1262B). `GRAPHITE` sirve para elementos secundarios. Fondo y texto deben mantener contraste alto. La apertura puede comenzar en negro/blanco como continuidad de suspenso; al entrar al análisis, una transición de página revela el fondo de papel y establece la paleta.
- **Jerarquía:** títulos breves; fórmulas y cifras principales en `FS.HEAD` o mayores; texto auxiliar no menor que `FS.NOTE` salvo etiquetas puntuales. No llenar la pantalla con la locución completa.
- **Rigor:** no inventar umbrales de medallas, datos de clasificación, algoritmo de Clumsy Courier ni magnitudes que el guion no dé. Las notas editoriales dentro de escenas son de producción, no narración.

---

## Escena 01 — Pregunta y contraste: escuela / ICPC

**Marca de tiempo estimada:** 00:00–00:25

**Audio / Narración**

> ¿Por qué los problemas de la ICPC son tan diferentes a lo que ves en la escuela? En clase, la estructura es clara: el problema viene con instrucciones directas y, por lo general, el nombre de la técnica que debes usar ya viene implícito o sugerido desde el inicio. Prácticamente sabes de antemano qué herramienta sacar de la caja.

**Objetos Matemáticos / Visuales**

- Apertura negra con texto blanco, sobrio, para enlazar con el suspenso de la primera parte.
- Dos fichas rectangulares: “Ejercicio de clase” y “Problema ICPC”.
- Una caja de herramientas con etiquetas como “técnica indicada” junto a la ficha escolar; en la ficha ICPC, el espacio de técnica queda vacío.
- Al pasar a la explicación, cambiar al fondo `PAPER`, texto `INK` y líneas `RULE`.

**Animaciones y Transformaciones (Manim Actions)**

1. Aparecer la pregunta al centro con `Write` (2–3 s).
2. Desplazar la pregunta hacia arriba y revelar las dos fichas, una a cada lado (`FadeIn`, 0.5 s).
3. En la ficha escolar, una etiqueta de herramienta entra desde la caja (`GrowArrow`/`FadeIn`); la ficha ICPC permanece sin etiqueta.
4. En “sacar de la caja”, la herramienta queda en primer plano (`Indicate`) y luego se atenúa. Cerrar con `FadeTransition` o reemplazo de fondo negro por papel.

**Notas de Código / Implementación**

- `Scene` o `MovingCameraScene`, `VGroup`, `RoundedRectangle`, `Tex`, `Arrow` y `Transform`.
- Definir colores desde `paper_theme.py`; mantener la apertura monocroma y cambiar una sola vez a `PAPER` para la explicación larga.

---

## Escena 02 — La historia es un disfraz

**Marca de tiempo estimada:** 00:25–00:55

**Audio / Narración**

> Pero en la ICPC la lógica cambia por completo. Aquí los problemas vienen disfrazados de historias, cuentos o situaciones cotidianas. Tu trabajo consiste en “pelar la cebolla”: quitar capas de texto hasta descubrir el esqueleto matemático que hay debajo; ya sea un grafo oculto, una tabla de frecuencias o una estructura geométrica. La historia es solo un disfraz.

**Objetos Matemáticos / Visuales**

- Tarjeta central con líneas de relato genéricas; no usar nombres ni hechos que aparenten provenir de un problema real.
- Capas concéntricas o láminas con fragmentos de texto, envolviendo un objeto central todavía abstracto.
- Tres ejemplos alternativos del núcleo: grafo pequeño, tabla de frecuencias y figura geométrica simple.
- Papel `PAPER`, tinta `INK`; la capa que se quita puede llevar un borde `ACCENT`.

**Animaciones y Transformaciones (Manim Actions)**

1. `FadeIn` de la tarjeta y sus capas (0.5 s).
2. Con “pelar la cebolla”, retirar una capa a la vez (`FadeOut`/`Uncreate`, 0.5 s cada una).
3. Transformar el centro sucesivamente en grafo, tabla y figura (`Transform`), no mostrar las tres como respuesta simultánea.
4. Al decir “solo un disfraz”, dejar el objeto matemático legible y mandar el texto narrativo al fondo (`set_opacity`).

**Notas de Código / Implementación**

- `VGroup` para las capas; `Graph` o `Dot` + `Line` para el grafo; `Table`/`MathTable` para frecuencias; `Dot`, `Line`, `Polygon` para geometría.
- Preparar cada modelo como grupo independiente para que `Transform` conserve centro y escala.

---

## Escena 03 — Muchas técnicas, ninguna indicada

**Marca de tiempo estimada:** 00:55–01:20

**Audio / Narración**

> Y cuando abres ese enunciado por primera vez, con el reloj corriendo implacable, te enfrentas de golpe a un menú gigantesco de técnicas: programación dinámica, árboles de sufijos, teoría de grafos, matemáticas avanzadas, flujos máximos, recorrido de Euler... y ninguna viene marcada. Tienes que adivinar el camino correcto entre decenas de opciones, muchas de las cuales tal vez ni siquiera conozcas.

**Objetos Matemáticos / Visuales**

- Reloj de concurso con minutos como marcas, sin hora numérica inventada.
- Mosaico de tarjetas: programación dinámica, árboles de sufijos, teoría de grafos, matemáticas avanzadas, flujos máximos y recorrido de Euler; tarjetas adicionales sin nombre sugieren “decenas”.
- Una pregunta/enunciado neutro al centro y un cursor, sin solución seleccionada.

**Animaciones y Transformaciones (Manim Actions)**

1. Aparecer el reloj y el enunciado (`Create`, `FadeIn`).
2. Las tarjetas entran con `LaggedStart` en 1–2 s; expandir el mosaico al decir “decenas”.
3. El cursor visita opciones sin fijarse en ninguna; las no visitadas permanecen sin marca.
4. Acelerar levemente el barrido de manecillas (`Rotate`) y terminar con “ninguna viene marcada” destacado con `Indicate`.

**Notas de Código / Implementación**

- `VGroup` de tarjetas, `SurroundingRectangle`/cursor y un reloj vectorial de `Circle` + `Line`.
- Evitar que el efecto parezca una recomendación técnica; no asociar una tarjeta con respuesta correcta.

---

## Escena 04 — Elegir las batallas (versión A, provisional)

**Marca de tiempo estimada:** 01:20–01:55

**Audio / Narración**

> De hecho, una de las habilidades más críticas aquí no es saber resolverlo todo porque resolver el set completo es humanamente imposible, asi esta diseñado, sino saber elegir tus batallas. En esta final, los mejores equipos del país lograron resolver entre 8 y 10 problemas; muy pocos pasaron de 11, y lo normal para la gran mayoría se queda entre 2 y 6 aciertos bien peleados. Saber qué problema sí puedes atacar y cuál te va a hacer perder valiosas horas es la diferencia entre subir al podio o quedarte fuera.

**Objetos Matemáticos / Visuales**

- Fila de tarjetas de problemas sin dificultad numérica asignada, dos zonas: “atacar” y “posponer”.
- Escala discreta de problemas resueltos con intervalos anotados: mayoría 2–6, mejores 8–10, pocos >11.
- Reloj/barra temporal para representar el coste de perseguir un problema que no avanza.

**Animaciones y Transformaciones (Manim Actions)**

1. Mostrar set amplio y reloj.
2. Una tarjeta pasa a “atacar”; otra a “posponer” (`Transform`). La barra de tiempo de esta última avanza y luego se detiene.
3. Presentar los rangos como intervalos anotados, no como histograma inventado; destacar el grupo elegido y cerrar con silueta de podio / fuera del podio, sin asignar nombres.

**Notas de Código / Implementación**

- `NumberLine`, `Line`, `Rectangle`, `Brace`, `Tex` y `VGroup`.
- **Bloque duplicado:** el guion repite la idea inmediatamente después con cifras diferentes; mantener esta escena solo si se confirma esta versión. Resolver la discrepancia con la escena 05 antes de grabar/editar.

---

## Escena 05 — Elegir las batallas (versión B, provisional)

**Marca de tiempo estimada:** 01:55–02:30

**Audio / Narración**

> De hecho, una de las habilidades más críticas aquí no es saber resolverlo todo porque resolver el set completo es humanamente imposible, así está diseñado, hay que saber elegir tus batallas. En esta final, los mejores equipos del país lograron resolver entre 8 y 11 problemas; muy pocos pasaron de ahí, mientras que la mediana para el resto de los equipos se quedó en apenas 3 aciertos, moviéndose la gran mayoría en un rango de 2 a 6 problemas bien peleados. Saber qué problema sí puedes atacar y cuál te va a hacer perder valiosas horas es la diferencia entre subir al podio o quedarte fuera.

**Objetos Matemáticos / Visuales**

- Mantener las tarjetas y el reloj de la escena 04 para continuidad.
- Banda 2–6, marca de mediana en 3, banda superior 8–11 y texto “pocos >11”.
- No agregar frecuencias ni tamaño de muestra, pues el guion no los proporciona.

**Animaciones y Transformaciones (Manim Actions)**

1. Transformar solo las etiquetas de cifras de la escena previa (2 s), no repetir toda la metáfora.
2. Colocar la mediana en 3; mostrar los rangos en una `NumberLine` con extremos explícitos.
3. Repetir la decisión de atacar/posponer y cerrar igual que en escena 04.

**Notas de Código / Implementación**

- Reutilizar una clase auxiliar `DecisionBoard` y actualizar los `Tex`/segmentos con `Transform`.
- **Dato por confirmar:** A dice 8–10; B dice 8–11 y mediana 3. Elegir una versión con datos validados y eliminar la otra en el guion final. El tiempo de esta escena se reasigna a la anterior si se suprime.

---

## Escena 06 — Problema C: Clumsy Courier

**Marca de tiempo estimada:** 02:30–03:25

**Audio / Narración**

> Para entenderlo mejor, veamos un ejemplo real. Este fue uno de mis favoritos del torneo, el **Problema C: Clumsy Courier**. Como explicarlo a fondo no es el objetivo de este video eterno, les dejo el enunciado completo en pantalla para los más curiosos, y si les interesa, mi próximo video puede dedicarse enteramente a resolverlo paso a paso.

**Objetos Matemáticos / Visuales**

- Tarjeta de título “Problem C — Clumsy Courier”.
- Cuatro paneles de enunciado en inglés: definición y extremos de la cuadrícula; movimientos y límites; condiciones U/L y visitas repetidas; pregunta, Input/Output y módulo.
- Miniatura constante de cuadrícula con inicio (1,1) y destino (R,C).
- La cuadrícula usa trazos `INK`, aristas auxiliares `RULE`, inicio sólido `INK` y meta marcada con `ACCENT`.

**Animaciones y Transformaciones (Manim Actions)**

1. Título entra (`Write`, 1 s); dejar 1 s de lectura.
2. Mostrar los cuatro paneles de forma sucesiva, 8–12 s por panel, con `FadeIn` y desplazamiento vertical suave.
3. En el panel de movimientos, animar una flecha de cada dirección; las flechas que salen de un borde se muestran tachadas o se omiten.
4. En el último panel, destacar “sequences of moves” y el módulo 998,244,353. Mantener por lo menos 2–3 s de lectura final.

**Notas de Código / Implementación**

- Subescenas `VGroup` o `Succession` con `Tex`/`MathTex`, `Grid` construido con `Line`, y `Arrow`.
- El enunciado completo tiene demasiado texto para una lámina única; renderizar texto por panel y preservar literalmente todas las restricciones del original.

---

## Escena 07 — Traducción del enunciado a movimientos

**Marca de tiempo estimada:** 03:25–03:50

**Audio / Narración**

> En pocas palabreas para no perdernos en el texto: te quieres mover en una cuadrícula desde una esquina hasta la opuesta usando movimientos hacia la derecha y hacia abajo, pero con una trampa: te tienes que regresar obligatoriamente una cantidad fija de veces hacia arriba o hacia la izquierda ($U$ y $L$ movimientos específicos).

**Objetos Matemáticos / Visuales**

- Cuadrícula esquemática con filas/columnas; notación general (1,1) y (R,C).
- Flechas Right/Down en `INK`; Up/Left en `ACCENT` y contadores U/L.
- Un pequeño rótulo “puede repetir intersecciones”.

**Animaciones y Transformaciones (Manim Actions)**

1. Transformar el panel del enunciado en una cuadrícula limpia.
2. Trazar un camino monótono Right/Down entre inicio y meta.
3. Introducir Up y Left como desvíos obligatorios y actualizar U/L; regresar a un vértice ya visitado una vez para representar repetición.
4. Mantener el camino dentro del borde de la cuadrícula durante toda la animación.

**Notas de Código / Implementación**

- `VGroup` de líneas de cuadrícula, `Dot` como courier y flechas por arista.
- Crear una función `move_along(path)` que valide límites antes de animar; usar `MoveAlongPath` solo en caminos que sigan las aristas.

---

## Escena 08 — Caso base 2×2, sin desvíos

**Marca de tiempo estimada:** 03:50–04:05

**Audio / Narración**

> Para que se animen a jugar un poco con el problema: imaginen una cuadrícula pequeña de $2 \times 2$. Si queremos ir de la esquina superior izquierda a la inferior derecha usando cero movimientos hacia arriba y cero hacia la izquierda, ¿cuántos caminos válidos tenemos? Exacto, solo dos formas directas.

**Objetos Matemáticos / Visuales**

- Cuadrícula de 2 filas × 2 columnas de calles: cuatro intersecciones y cuatro segmentos que permiten los dos caminos monotónicos.
- Coordenadas (1,1) arriba a la izquierda y (2,2) abajo a la derecha; U=0, L=0.
- Contador de caminos y flechas de secuencia RD/DR.

**Animaciones y Transformaciones (Manim Actions)**

1. Hacer zoom en la cuadrícula pequeña y fijar U=L=0.
2. Dibujar ruta R-D; reiniciar courier; dibujar D-R (`MoveAlongPath`, 1–2 s por ruta).
3. Incrementar el contador tras cada ruta y terminar en 2. Mantener simultáneamente visible el punto inicial/meta para verificar extremos.

**Notas de Código / Implementación**

- `Square`/`Line` para malla, `Dot`, `Arrow`, `MathTex` y `DecimalNumber`.
- Convención explícita: una ruta es una secuencia de movimientos; los dos recorridos no se cuentan como geometría sin dirección.

---

## Escena 09 — Caso 2×2 con un movimiento Up

**Marca de tiempo estimada:** 04:05–04:25

**Audio / Narración**

> ¿Y qué pasa si permitimos un movimiento hacia arriba y cero hacia la izquierda? Piénselo un par de segundos... Correcto, tendríamos cuatro caminos diferentes.

**Objetos Matemáticos / Visuales**

- La misma cuadrícula 2×2; U=1 y L=0.
- Una ruta destacada en `ACCENT` al subir; los pasos Down/Right en `INK`.
- Contador discreto de 0 a 4.

**Animaciones y Transformaciones (Manim Actions)**

1. Cambiar U de 0 a 1 con `Transform`; dejar una pausa de 2 s para pensar.
2. Mostrar por separado las cuatro secuencias válidas: R-D-U-D; D-R-U-D; D-U-R-D; D-U-D-R. Reiniciar el courier entre ellas.
3. Incrementar el contador una vez por secuencia. No dibujar ningún paso que salga de la cuadrícula; al final dejar las cuatro secuencias resumidas.

**Notas de Código / Implementación**

- Rutas como arrays de coordenadas de intersección; crear un `VMobject` por secuencia y animar `MoveAlongPath`.
- Validar cada secuencia con límites 1≤r,c≤2 antes de incluirla.

---

## Escena 10 — Contar sin enumerar todos los recorridos

**Marca de tiempo estimada:** 04:25–04:45

**Audio / Narración**

> Lo verdaderamente elegante y retador aquí no es probar a mano, sino diseñar un algoritmo eficiente que pueda contar estos trayectos para una cuadrícula gigante y para cualquier cantidad arbitraria de desvíos. Si quieren que armemos la solución completa de este problema, déjenlo en los comentarios.

**Objetos Matemáticos / Visuales**

- La cuadrícula 2×2 se expande a una malla R×C; etiquetas U/L permanecen.
- Muchos caminos posibles se convierten en puntos/estados agregados y luego en un contador abstracto.
- Rótulo final “contar, no enumerar”; no mostrar una fórmula de solución.

**Animaciones y Transformaciones (Manim Actions)**

1. Alejar cámara (`MovingCameraScene`) mientras aparecen filas/columnas adicionales.
2. Multiplicar brevemente los recorridos; después sustituirlos por celdas agrupadas/contador (`Transform`).
3. En “algoritmo eficiente”, estabilizar el contador y enfatizar la palabra “contar”.
4. Salir con `FadeOut` dejando un espacio/ícono de comentario.

**Notas de Código / Implementación**

- `MovingCameraScene`, `VGroup`, líneas creadas por bucle, opacidad progresiva y `DecimalNumber` solo si no comunica un resultado específico.
- No codificar ni insinuar una recurrencia que no está en el guion.

---

## Escena 11 — Tres personas, tres tareas

**Marca de tiempo estimada:** 04:45–05:20 (duración sujeta a los clips)

**Audio / Narración**

> Mientras tanto, veamos cómo operan los equipos en la vida real. Aquí la programación no es un acto solitario; requiere una coordinación milimétrica. Mientras una persona debate la estrategia matemática en la pizarra, otra valida esquemas lógicos en la computadora y la tercera depura código.

**Objetos Matemáticos / Visuales**

- La imagen principal es el clip real del equipo UADY indicado en el guion.
- Rótulos discretos para tres funciones: estrategia, validación y depuración; opcionalmente, diagramas superpuestos en transparencia: grafo en pizarra, flujo lógico en pantalla y líneas de código.
- Paleta de tinta/papel con acento rojo para subrayados; overlays nunca cubren los rostros ni la acción real.

**Animaciones y Transformaciones (Manim Actions)**

1. Entrar al clip con corte directo desde la cuadrícula grande.
2. Al nombrar cada tarea, introducir su rótulo con `FadeIn` (0.4 s) y retirarlo antes de la siguiente.
3. Cerrar los rótulos y dejar respirar el clip 1–2 s.

**Notas de Código / Implementación**

- No es una escena generada solo con Manim: integrar el clip en edición. Para overlays, exportar animaciones con fondo transparente (`--transparent`) o componer `ImageMobject`/video en `Scene` si el flujo de render lo permite.
- Validar disponibilidad, permisos y duración del material UADY antes de fijar timecode.

---

## Escena 12 — Talento bajo presión

**Marca de tiempo estimada:** 05:20–05:55 (duración sujeta a los clips)

**Audio / Narración**

> Esta combinación única trabajo bajo presión extrema y sobretodo de pensamiento analítico profundo, y resiliencia es exactamente la razón por la cual las empresas tecnológicas más importantes del mundo no vienen por casualidad: están aquí buscando talento de élite.

**Objetos Matemáticos / Visuales**

- Clips reales de reclutadores; lower thirds con nombre/empresa solo si se verifican en el metraje.
- Palabras clave “análisis”, “resiliencia” y “colaboración” como tipografía cinética, sin convertir afirmaciones en gráficas cuantitativas.

**Animaciones y Transformaciones (Manim Actions)**

1. Cortar de los competidores a reclutadores al empezar la segunda oración.
2. Hacer aparecer una palabra clave junto a la voz correspondiente; alternar con los clips, no taparlos.
3. Terminar con “talento de élite” y transición a la Final Mexicana.

**Notas de Código / Implementación**

- Composición editorial de clips; Manim para rótulos transparentes si se necesita.
- Duración, nombres, logotipos y cargos quedan pendientes de revisar el material de entrevistas.

---

## Escena 13 — Entrada a los resultados

**Marca de tiempo estimada:** 05:55–06:05

**Audio / Narración**

> Volviendo de lleno a la competencia: ¿Quiénes ganaron? Hagamos cuentas.

**Objetos Matemáticos / Visuales**

- Fondo `PAPER`, tablero vacío centrado, título “Final Mexicana 2026”.
- Tres espacios vacíos destinados a clasificatorias, final y medallas.

**Animaciones y Transformaciones (Manim Actions)**

1. Limpiar la escena previa con `FadeOut`.
2. Dibujar tablero y título con `Create`/`Write`.
3. Pausa corta antes de revelar la primera cifra.

**Notas de Código / Implementación**

- `Scene`, `Rectangle`, `Line`, `Tex`; usar como encabezado visual reutilizable para escenas 14–16.

---

## Escena 14 — Filtro: 509 → 85 → 20

**Marca de tiempo estimada:** 06:05–06:25

**Audio / Narración**

> Iniciamos este camino con **509 equipos** compitiendo a lo largo de las tres fechas clasificatorias. De ese filtro brutal, solo **85 equipos** lograron ganarse un lugar presencial en esta gran final. De ellos, **20 equipos** consiguieron medalla.

**Objetos Matemáticos / Visuales**

- Tres contenedores/columnas conectados: 509 clasificatorios; 85 finalistas presenciales; 20 medallistas.
- Pictogramas solo como textura tenue, no 509 iconos individuales.

**Animaciones y Transformaciones (Manim Actions)**

1. Revelar 509 al escuchar el número; agregar etiqueta “tres fechas clasificatorias”.
2. Transformar el conjunto en 85 finalistas con estrechamiento visual y flecha.
3. Resaltar 20 medallistas dentro del grupo de 85; mantener etiqueta de subconjunto.
4. Dejar las tres cifras visibles durante 2 s.

**Notas de Código / Implementación**

- `DecimalNumber`, `SurroundingRectangle`, `Arrow`, `VGroup`; usar área o cantidad de íconos simbólica sin sugerir proporciones exactas.

---

## Escena 15 — Medallas por bloques de rendimiento

**Marca de tiempo estimada:** 06:25–06:50

**Audio / Narración**

> Aquí surge una duda muy común: si es una competencia, ¿por qué hay múltiples medallas de oro, plata y bronce en lugar de un solo campeón absoluto como en los Juegos Olímpicos? A diferencia de una competencia de velocidad, la ICPC mide el rendimiento de los equipos contra un estándar global de dificultad y distribución por porcentajes de participación, premiando a los bloques más destacados de la tabla general.

**Objetos Matemáticos / Visuales**

- Tabla ordinal estilizada con filas por desempeño y franjas etiquetadas oro, plata y bronce.
- Comparación lateral con una línea de meta de velocidad (un campeón) y un tablero ICPC dividido en bloques.
- No escribir porcentajes ni límites de posición no proporcionados.

**Animaciones y Transformaciones (Manim Actions)**

1. Mostrar un único podio; al preguntar por múltiples medallas, transformar el podio en tabla por bloques.
2. Resaltar cada franja en orden, manteniendo neutral la división hasta que la narración mencione estándar y porcentajes.
3. Transicionar la tabla abstracta a la tabla real de la escena 16.

**Notas de Código / Implementación**

- `Table`/`MathTable`, `Rectangle`, `SurroundingRectangle`, `Transform`.
- Los porcentajes de medallas y sus cortes son un dato pendiente: mantener representación cualitativa, no cuantitativa.

---

## Escena 16 — Los 25 mejores equipos

**Marca de tiempo estimada:** 06:50–07:45 (lectura visual; ajustar al ritmo)

**Audio / Narración**

> Veamos cómo quedó el tablero de los mejores equipos del país en esta final.

**Objetos Matemáticos / Visuales**

- Tabla con columnas: puesto, escuela, nombre del equipo, problemas resueltos y estatus de clasificación.
- Usar las 25 filas enumeradas en la sección 4 del guion; respetar datos y orden originales.
- Fondo claro, texto `INK`, filas alternas `PAPER`/un tinte leve de `RULE`; cifras de problemas centradas; estatus con texto y pequeño distintivo.
- Nombres largos en dos líneas o con truncamiento editorial explícito; nunca hacer el texto tan pequeño que no se lea.

**Animaciones y Transformaciones (Manim Actions)**

1. Entrar con título y encabezados (1 s).
2. Revelar filas 1–14 en un primer panel; después deslizar verticalmente o reemplazar por filas 15–25. Mantener el número de puesto fijo y mostrar suficientes segundos para lectura.
3. Usar un panel de detalle para el nombre largo solo si el editor decide que se debe leer completo; no expandirlo sobre toda la tabla.
4. Mantener la tabla como objeto persistente para las escenas 17–19.

**Notas de Código / Implementación**

- Mejor usar `VGroup` de filas y `MovingCameraScene`/scroll que una sola `Table` comprimida.
- Fuente de filas en una lista de diccionarios; escapar caracteres especiales de `Tex` o usar `Text` para nombres. Verificar la discrepancia entre “25 mejores” y posibles entradas/cupos antes de datos finales.

---

## Escena 17 — Avanzan quienes tienen el boleto

**Marca de tiempo estimada:** 07:45–08:15

**Audio / Narración**

> Y bien, ¿quiénes avanzan a la siguiente etapa? El objetivo final es conformar a la delegación que representará a México en el **Campeonato Latinoamericano (LATAM Championship)**, donde se medirán las mejores mentes de toda la región. Por lógica, esperaríamos que pasen estrictamente los mejores posicionados en la tabla general. Pero aquí nos topamos con una realidad logística: **no siempre es así**.

**Objetos Matemáticos / Visuales**

- Reusar tabla anterior, con columna de clasificación visible.
- Una flecha final apunta a un rótulo “LATAM Championship”.
- Para la expectativa, subrayado fino en verde de los clasificados; texto “No siempre” entra en `ACCENT` (un solo color de énfasis por toma si se mantiene coherencia con papel/tinta).

**Animaciones y Transformaciones (Manim Actions)**

1. Reducir escala de la tabla para dejar sitio al destino LATAM.
2. Iluminar los estatus de clasificación conforme se escucha “quiénes avanzan”.
3. Mostrar ruta general tabla → LATAM; al decir “no siempre”, interrumpir la flecha con una bifurcación o desajuste visual, sin explicar todavía la causa.

**Notas de Código / Implementación**

- Mantener referencias a las mismas filas/celdas, no reconstruir una tabla que cambie datos.
- `Indicate`, `Underline`, `Arrow`, `Transform`; color complementario para clasificación y `ACCENT` para “no siempre”.

---

## Escena 18 — Comparación de puestos 15–19

**Marca de tiempo estimada:** 08:15–08:35

**Audio / Narración**

> Si observan con atención la tabla, se darán cuenta de que hay equipos ubicados entre los lugares 15 y 19 que, a pesar de haber resuelto más problemas que equipos clasificados más abajo (como los lugares 20 a 25), se quedaron fuera del boleto directo.

**Objetos Matemáticos / Visuales**

- Tabla persistente con filas 15–19 en foco inicial; filas 20–25 atenuadas pero aún legibles.
- Comparar columna “problemas resueltos” y estatus; filas 15–19 muestran “No” según la lista, 20–25 aparecen con su estatus tal como está escrito.
- No marcar todos los lugares como si tuvieran la misma cantidad de problemas ni sugerir una causa.

**Animaciones y Transformaciones (Manim Actions)**

1. Foco hover/contorno en filas 15–19; negritas temporales en número de puesto y problemas.
2. Tras el primer fragmento del audio, liberar el foco y pasar a filas 20–25.
3. Dibujar guías comparativas solo para pares que efectivamente tengan más problemas y clasificación, según los valores de la tabla.
4. Retirar ambos focos al final.

**Notas de Código / Implementación**

- `SurroundingRectangle` por rango de filas; `Indicate` o `Flash` en celdas comparadas.
- Los cortes del audio atraviesan el mismo párrafo; sincronizar los dos focos con las frases sin reordenar la voz.
- Verificar la lista: en el texto actual algunos datos de estatus y conteos podrían no sustentar literalmente “más problemas que equipos clasificados más abajo”. No dibujar comparaciones que los datos no respalden.

---

## Escena 19 — Factores logísticos

**Marca de tiempo estimada:** 08:35–09:05

**Audio / Narración**

> En la ICPC no todo depende exclusivamente del mérito puro en una sola tabla nacional. Factores como cuotas regionales, cupos por institución y el estatus de sedes juegan un papel determinante; a veces, formar parte de una universidad con plazas asignadas te da una ventaja logística frente a equipos de otras sedes que tuvieron un desempeño superior.

**Objetos Matemáticos / Visuales**

- La tabla se despliega en tarjetas: “desempeño”, “cuota regional”, “cupo por institución”, “estatus de sede”.
- Diagrama de clasificación como función de múltiples restricciones: tabla de rendimiento + reglas/cupos → selección final. Usar piezas como restricciones, no pesos numéricos.
- Evitar asignar a una institución un cupo concreto sin dato fuente.

**Animaciones y Transformaciones (Manim Actions)**

1. Mantener la tabla atenuada como contexto.
2. Hacer entrar cada factor como tarjeta conectada al diagrama; al final, se cruzan en una puerta de selección.
3. Mostrar dos equipos esquemáticos con rendimiento distinto y una etiqueta “reglas/cupos” que condiciona el resultado, sin adjudicar nombres ni inventar cantidades.

**Notas de Código / Implementación**

- `VGroup`, `Arrow`, `Brace`, `RoundedRectangle`, `Tex`.
- El diagrama representa solo la afirmación del guion; validar las reglas oficiales antes de ilustrar un caso específico.

---

## Escena 20 — Reconocimiento a los participantes

**Marca de tiempo estimada:** 09:05–09:35

**Audio / Narración**

> A pesar de estas asperezas reglamentarias, el mérito de cada competidor es innegable. Todos entregaron horas de esfuerzo absoluto sobre el teclado. Muchas felicidades a todos los participantes, y un reconocimiento especial y muchísimo éxito a los equipos que llevarán la bandera de México al LATAM Championship.

**Objetos Matemáticos / Visuales**

- La tabla desaparece para dejar una composición amplia de equipos/teclados, preferentemente material real de la final.
- Bandera mexicana como elemento discreto, sin convertir nombres de participantes en decoración ilegible.
- Rótulo “LATAM Championship” solo durante la felicitación final.

**Animaciones y Transformaciones (Manim Actions)**

1. Atenuar los datos competitivos y pasar a clips/fotos reales.
2. Hacer aparecer “esfuerzo”, “equipo” y “resiliencia” a medida que se nombran, luego retirarlos.
3. Revelar el destino LATAM y cerrar con fundido a papel/negro según enlace a entrevistas.

**Notas de Código / Implementación**

- Preferir clips/fotos en edición; `ImageMobject` y overlays Manim si hay material autorizado.
- No mostrar otra tabla o ranking en esta parte: el audio cambia de comparación a reconocimiento.

---

## Escena 21 — Cierre con consejos de competidores y entrenadores

**Marca de tiempo estimada:** 09:35–fin (duración indeterminada por entrevistas)

**Audio / Narración**

> Para cerrar este recorrido, le preguntamos a varios competidores experimentados y entrenadores qué recomendación le darían a los chavos de preparatoria, secundaria o incluso primaria que ya muestran esa chispa por la programación y matematicas y en general las ciencias exactas.

**Objetos Matemáticos / Visuales**

- Clips de entrevistas, con identificación de participante/entrenador cuando esté confirmada.
- Intercalar imágenes de jóvenes practicando, pizarras o ejercicios; conservar el tema papel/tinta para títulos y lower thirds.
- No se inventan las respuestas: el guion solo contiene la pregunta y señala clips pendientes.

**Animaciones y Transformaciones (Manim Actions)**

1. Abrir con la pregunta completa como tarjeta breve sobre imágenes de apoyo.
2. Cortar a cada clip cuando empiece la respuesta; dejar el audio original y subtítulos si se necesitan.
3. Cierre editorial con logotipo/canal o créditos, cuando se defina el material final.

**Notas de Código / Implementación**

- Tramo de montaje, no una escena Manim autónoma; Manim puede producir pregunta, lower thirds y cierre con fondo transparente.
- Timecodes, selección de citas y duración dependen de entrevistas aún no incluidas en el guion.

---

## Pendientes de continuidad antes de producir

1. Resolver cuál párrafo de “elegir tus batallas” queda y validar si el rango superior es 8–10 o 8–11, además de la mediana.
2. Contrastar las filas 15–25, el estatus “clasificó” y las cantidades de problemas con el scoreboard oficial: el storyboard evita inferir pares de comparación que los datos no respalden.
3. Revisar la explicación de medallas y clasificación con las reglas oficiales; el guion menciona porcentajes, pero no establece los cortes.
4. Recibir clips UADY, reclutadores y entrevistas finales; fijar duración, nombres, cargos, subtítulos y permisos de uso.
5. Ajustar todos los tiempos después de grabar la voz. Las escenas 06, 11, 12, 16 y 21 dependen especialmente del tiempo de lectura o de material externo.
