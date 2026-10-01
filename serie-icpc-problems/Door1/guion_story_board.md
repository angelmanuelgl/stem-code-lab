# Guion Storyboard / Técnico: Door 1

**Fuente de contenido:** `guion_sol.md` de Door1. Este documento especifica animación; no contiene una implementación de Manim. Los ejemplos añadidos desarrollan el mismo modelo del análisis.

**Formato y sincronía.** Lienzo 16:9, `frame_width=128/9`, `frame_height=8`, cámara fija. Área útil x∈[−6.3,6.3], y∈[−3.5,3.5]; título habitual en UP*3.25. Las posiciones son centros de objetos y las coordenadas tienen z=0. Los textos de una misma fila deben caber en su panel; partir fórmulas antes que reducirlas por debajo de 24 puntos. Títulos de 36 puntos, texto de 28 y fórmulas de 30 como punto de partida. No asumir que una ecuación larga cabe sólo porque su centro está indicado.

Cada escena tiene cuatro disparadores locales, reiniciados desde `[TRIGGER_1]`. El par (escena, disparador) es el identificador único. La voz se reproduce literalmente desde `guion_voz.md`. Los intervalos son estimaciones editoriales a 140 palabras por minuto, más margen visual y pausas; se ajustarán a la grabación real. No son marcas de audio ya medido. Todas las operaciones de una viñeta pertenecen a ese disparador; se ejecutan en el orden de sus frases, con la aparición del concepto correspondiente en la voz. La última imagen se mantiene hasta el disparador siguiente. La transición de cierre se incluye en el último disparador; no hay cambios narrativos sin marca.

**Convención de operaciones.** «Crear» un contorno o una arista significa `Create`; «mostrar/revelar/escribir» texto significa `Write`, y un conjunto geométrico ya construido, `FadeIn`; «actualizar/sustituir/calcular» una expresión usa `TransformMatchingTex`; mover fichas usa `.animate.move_to`; «destacar/señalar» usa `Indicate`; eliminar una hipótesis usa `Cross` y `FadeOut`, sin borrar la alternativa válida. «Agrupar» usa `VGroup` y `Brace`; fusionar objetos usa `ReplacementTransform`. En cada disparador la secuencia concreta indica qué objetos reciben esas operaciones. Las apariciones duran aproximadamente 0.6–1.0 s, los desplazamientos 0.8–1.2 s y los énfasis 0.5 s; el resto del intervalo permite leer y escuchar. Las pausas de locución no disparan transiciones nuevas.

**Tipografía y diagramas.** Todo texto visible, incluidos títulos, créditos, leyendas, índices, números y etiquetas de ejes, se construye con `Tex` o `MathTex`; nunca con `Text`, `Code`, `DecimalNumber` ni etiquetas automáticas incompatibles con esta regla. Las expresiones mencionadas en prosa se transcriben a LaTeX: por ejemplo, α como `\alpha`, ≤ como `\le`, y los subíndices con llaves. Los estados son `MathTex(r"(i,s,h,g)")`; el texto español usa un preámbulo LaTeX con soporte de acentos. Los `Axes` y `NumberLine` reciben etiquetas `MathTex` manuales. La geometría usa `Rectangle`, `Square`, `Circle`, `Dot`, `Line`, `Arrow`, `Polygon`, `Ellipse`, `Brace` y `VGroup`. No se muestran bloques de código fuente.

**Gramática visual.** Un cuadrado representa una decisión; un círculo, un suceso aleatorio. Cada arista porta su probabilidad condicional, cada hoja su estado y su valor de continuación. Multiplicar pesos a lo largo de una ruta y sumar rutas excluyentes se anima antes de compactar fórmulas. Las ramas mortales terminan en cero y conservan su masa: jamás se renormaliza el conjunto superviviente. La disposición del árbol factoriza probabilidades; no impone una cronología física de encuentros. Los diagramas esquemáticos de crecimiento se rotulan como tales y no sustituyen las enumeraciones completas de las acciones.

**Diccionario que permanece estable.** i es la hora que comienza; s, las baterías iniciales; h, las horas consecutivas sin comer; g, las apariciones observadas durante las i−1 horas anteriores. p es el peligro fijo desconocido, mientras α es la predicción que cambia con la información. Los símbolos b,c,v,q de una escena representan b_i,c_i,v_i,q_i en esa hora; v es condicional a encontrar comida. Las probabilidades conocidas se combinan según la independencia del modelo fuente; el gigante comparte p entre horas. Las curvas se rotulan como densidad o peso sin normalizar: una altura no es una probabilidad puntual. Todos los estados posteriores avanzan a i+1 aunque una tabla de recursos omita esa coordenada para ganar espacio.

**Paleta semántica de `styles.theme` / `theme.py`.** `BG_COLOR=#181C24`; `TEXT_MAIN=#ECEFF4`; `TEXT_MUTED=#64748B`; `ACCENT_INDIGO=#6366F1` para estado, refugio y decisión; `ACCENT_CYAN=#38BDF8` para probabilidades y baterías; `ACCENT_MINT=#2DD4BF` para alimento seguro, resultados válidos y certificados; `ACCENT_TERRACOTTA=#D97706` para hambre, tiempo y condiciones; `ACCENT_VINO=#C0392B` para muerte e hipótesis inválidas. No usar `COLOR_DANGER`: el papel de peligro corresponde a `ACCENT_VINO`. El color siempre se acompaña de forma, etiqueta o símbolo; verde en una rama protegida de un ataque no afirma que se sobreviva al hambre.

**Continuidad.** Cada escena reconstruye únicamente los elementos indicados en sus objetos y layout; al reutilizar una tabla se conservan valores, índices y colores. El tablero de dos horas de las escenas 22–25 usa exactamente los mismos parámetros. Las escenas de cálculo hacia atrás animan la evaluación matemática, nunca un personaje que conoce sucesos futuros.


## Escena: 01

## Nombre: Una puerta y dos clases de incertidumbre

## Descripcion Breve: Una persona entra en una madriguera y debe decidir cómo sobrevivir.

## Objetivo Pedagogico: Plantear la tensión entre recursos, riesgo e información sin anticipar la DP.

## Voz en off:

> "[TRIGGER_1] Eliges la puerta uno. Detrás hay una madriguera, una lámpara y una cuenta regresiva. Para escapar tienes que sobrevivir cierto número de horas. Puedes esconderte… pero tarde o temprano tendrás hambre. [TRIGGER_2] Salir permite buscar comida o baterías. También permite que te encuentren los hurones. Algunos se espantan con la luz. Hay otro, gigante, del que no puedes escapar si te sorprende fuera. [TRIGGER_3] Y todavía falta lo más extraño: no sabes con qué frecuencia aparece ese gigante. Su peligro permanece fijo durante toda la partida, pero tú lo vas descubriendo. [Pausa.] ¿Cómo decides cuando sobrevivir también te enseña algo? [TRIGGER_4] Door 1, de la primera fecha del Gran Premio de México de dos mil veintiséis, combina esas dos preguntas: qué sabemos del peligro y qué conviene hacer con ese conocimiento."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Puerta con Rectangle y Dot; madriguera mediante tres caminos Line; avatar Dot, lámpara con Polygon y una silueta pequeña y otra grande hechas de elipses. Textos Tex; MathTex(r"N\ \text{horas}").
- Reloj de N casillas esquemáticas con puntos suspensivos, tres tarjetas Tex(r"\text{Esconderse}"), Tex(r"\text{Buscar batería}"), Tex(r"\text{Buscar comida}"); indicador de peligro sin número.

## Layout y disposicion:

- Puerta en (-4.8,0,0); bifurcación en ORIGIN; caminos hacia (3.6,1.5,0),(3.6,0,0),(3.6,-1.5,0).
- Título en (0,3.25,0); reloj en y=2.2; pregunta conceptual en y=-2.7. Las siluetas no requieren imágenes externas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** FadeIn de puerta y avatar; abrir dos hojas con Rotate y revelar madriguera. Aparecer reloj, sin consumir horas todavía.
- [TRIGGER_2] **00:15–00:30:** Create de las tres rutas y sus tarjetas. Colocar lámpara junto a silueta pequeña y un gran contorno de peligro sobre la ruta exterior.
- [TRIGGER_3] **00:30–00:48:** Revelar indicador sin cifra; separar físicamente una tarjeta de peligro real y otra de conocimiento. Mantener la pausa sin desplazamientos del avatar.
- [TRIGGER_4] **00:48–01:02:** Write del nombre del problema y procedencia; conservar las tres acciones para explicar reglas, sin mostrar aún fórmulas de optimización.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para refugio; ACCENT_CYAN para lámpara; ACCENT_TERRACOTTA para hambre y reloj; ACCENT_VINO para muerte; TEXT_MAIN para narración visible.

---

## Escena: 02

## Nombre: Antes de que empiece cada hora

## Descripcion Breve: Una decisión precede a todos los resultados aleatorios de esa hora.

## Objetivo Pedagogico: Fijar acciones, probabilidades conocidas y orden de información.

## Voz en off:

> "[TRIGGER_1] Cada hora comienza con una decisión. Exactamente una: esconderte, buscar una batería o buscar comida. La eliges antes de saber qué aparecerá. No puedes asomarte, ver el peligro y cambiar de plan para esa misma hora. [TRIGGER_2] En la hora i, buscar batería tiene una probabilidad conocida de encontrar una. Buscar comida tiene otra probabilidad de encontrar alimento; si lo encuentras, todavía existe una probabilidad de que esté envenenado. [TRIGGER_3] También conoces la probabilidad del hurón sensible a la luz. Esas cuatro probabilidades pueden cambiar de una hora a la siguiente, y sus valores vienen dados por el problema. [TRIGGER_4] El gigante es distinto: su probabilidad no viene revelada. Al esconderte puedes observar si apareció sin sufrir daño. Al salir, una aparición suya es mortal. La decisión ocurre primero; la información nueva llega después."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Línea temporal dividida en decisión, resultados y estado siguiente, con Arrow; Tex para rótulos.
- Cuatro tarjetas MathTex(r"b_i"), MathTex(r"c_i"), MathTex(r"v_i"), MathTex(r"q_i") con Tex de hallazgo batería, hallazgo comida, veneno condicionado a hallazgo y fotosensible; tarjeta oculta MathTex(r"p").

## Layout y disposicion:

- Eje horizontal de x=-5.8 a 5.8 en y=1.35: decisión x=-4.3, resultados x=0, siguiente x=4.3.
- Tarjetas conocidas en cuadrícula 2×2 con centros (-3,-0.3,0),(3,-0.3,0),(-3,-1.5,0),(3,-1.5,0); p oculto en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Crear las tres etapas y mover token de decisión a resultados. Dibujar un candado tras elegir para impedir una flecha de vuelta durante la misma hora.
- [TRIGGER_2] **00:17–00:32:** Revelar b_i, c_i, v_i por separado; unir v_i mediante flecha a la rama comida encontrada, no directamente a toda búsqueda.
- [TRIGGER_3] **00:32–00:46:** Revelar q_i y pasar una hoja de calendario i→i+1 que cambia los cuatro valores simbólicos. No asignar valores arbitrarios.
- [TRIGGER_4] **00:46–01:02:** Mostrar p oculto y las ramas del gigante: observar desde refugio o morir fuera. Conservar la secuencia decidir→observar como regla global.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para probabilidades conocidas; ACCENT_INDIGO para información oculta y refugio; ACCENT_TERRACOTTA para decisión; ACCENT_VINO para rama mortal.

---

## Escena: 03

## Nombre: La batería que llega demasiado tarde

## Descripcion Breve: La defensa consume dos baterías iniciales y el hallazgo se incorpora después.

## Objetivo Pedagogico: Comprender el requisito s>=2 y el orden de consumo y saturación.

## Voz en off:

> "[TRIGGER_1] La lámpara necesita dos baterías y consume las dos al usarse. Si el hurón fotosensible aparece mientras estás fuera y comenzaste la hora con menos de dos, no sobrevives. [TRIGGER_2] Una batería encontrada durante esa búsqueda no puede rescatarte a tiempo. Empezar con una y encontrar otra no equivale a empezar con dos. La condición se comprueba sobre lo que ya llevabas. [TRIGGER_3] Si empezaste con tres, espantas al hurón y después encuentras una batería, terminas con dos: tres menos dos más una. Si no encontraste nada, terminas con una. [TRIGGER_4] La bolsa tiene capacidad K. Sin ataque, encontrar una batería con la bolsa llena no aumenta la reserva. Con ataque y hallazgo, pasarías de K a K menos uno. Esas diferencias pequeñas cambiarán algunas decisiones."

## Descripcion Visual Detallada:

Duración orientativa: 00:58. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- VGroup de iconos de batería hechos con Rectangle; registros MathTex s, K; requisito MathTex(r"s\ge2").
- Tres diagramas MathTex(r"1\ \not\Rightarrow\ \text{defensa}"), MathTex(r"3-2+1=2"), MathTex(r"\min(K,K+1)=K,\quad K-2+1=K-1").

## Layout y disposicion:

- Reservas iniciales en x=-4.5, y=0.8; ataque en x=0; reserva final en x=4.3.
- Ejemplo concreto en y=1.7; casos de capacidad en y=-1.4 y-2.5. Un icono pendiente de hallazgo se sitúa por debajo de la línea de defensa, nunca en la reserva inicial.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Encender dos baterías y retirarlas juntas al usar la lámpara. Mostrar s≥2 junto al punto de defensa.
- [TRIGGER_2] **00:14–00:29:** Presentar s=1 y una batería futura con contorno discontinuo. Bloquear su traslado hacia el pasado; marcar captura antes de incorporar hallazgo.
- [TRIGGER_3] **00:29–00:42:** Animar explícitamente 3→1 por consumo, después 1→2 por hallazgo; presentar la alternativa sin hallazgo 3→1.
- [TRIGGER_4] **00:42–00:58:** Con bolsa llena, añadir batería y descartarla visualmente por capacidad; luego mostrar K→K-2→K-1. No saturar antes de restar el consumo en la segunda trayectoria.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para baterías; ACCENT_TERRACOTTA para condición inicial; TEXT_MUTED para recurso aún no obtenido; ACCENT_VINO para captura; ACCENT_MINT para defensa exitosa.

---

## Escena: 04

## Nombre: El refugio también tiene un límite

## Descripcion Breve: El contador de hambre avanza o vuelve a cero y puede matar en la última hora.

## Objetivo Pedagogico: Definir h como horas consecutivas sin comer y el límite estricto h<H.

## Voz en off:

> "[TRIGGER_1] Esconderse evita los ataques, pero no detiene el hambre. Llamemos h al número de horas consecutivas sin comer con éxito. Al comenzar vale cero; una hora sin alimento lo aumenta en uno. [TRIGGER_2] Si H vale tres, puedes pasar de cero a uno y de uno a dos. Una tercera hora sin comer te lleva a tres y mueres. Comer algo seguro, en cambio, reinicia el contador a cero. [TRIGGER_3] Encontrar comida envenenada no reinicia una vida que pueda continuar: esa rama termina. No encontrar comida significa seguir con hambre. Son resultados distintos y no debemos mezclarlos. [TRIGGER_4] Y llegar al límite de hambre en la última hora también mata. La salida no borra lo que ocurrió durante esa hora. Primero comprobamos que sobrevivimos; sólo entonces podemos celebrar que terminó la cuenta regresiva."

## Descripcion Visual Detallada:

Duración orientativa: 01:01. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Barra de tres casillas con MathTex 0,1,2,3 y marcador h; MathTex(r"0\le h<H").
- Tres flechas de resultado: MathTex(r"h\to h+1"), MathTex(r"h\to0"), nodo Tex(r"\text{Muerte}"); iconos de alimento seguro y veneno como formas.

## Layout y disposicion:

- Contador centrado en y=1.2, casillas en x=-3,-1,1,3; h=3 tiene marco de umbral.
- Ramas comida en y=-0.5, veneno en y=-1.6; salida al final del horizonte en (4.7,-2.5,0) detrás del control de supervivencia.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Construir contador e incrementar 0→1 con una hora de refugio.
- [TRIGGER_2] **00:15–00:32:** Incrementar 1→2 y luego mostrar dos alternativas separadas: no comer 2→3 y muerte, comer 2→0. No animar ambas como si fueran la misma historia.
- [TRIGGER_3] **00:32–00:45:** Separar no hallazgo y veneno: una rama conserva vida con h+1 si es válido, la otra termina en cero probabilidad de continuación.
- [TRIGGER_4] **00:45–01:01:** Situar el umbral mortal antes de la puerta de escape en el eje temporal. Una ficha con h=H no atraviesa a éxito aunque se haya llegado al final de N.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_TERRACOTTA para hambre; ACCENT_MINT para reinicio seguro; ACCENT_VINO para muerte; ACCENT_INDIGO para salida y refugio.

---

## Escena: 05

## Nombre: Una moneda elegida una sola vez

## Descripcion Breve: El parámetro p se sortea al inicio y gobierna todas las horas.

## Objetivo Pedagogico: Distinguir incertidumbre sobre p de fluctuación del parámetro real.

## Voz en off:

> "[TRIGGER_1] Imagina una colección continua de monedas: algunas hacen aparecer al gigante casi siempre; otras, casi nunca. Antes de entrar se elige una, uniformemente entre probabilidades cero y uno. [TRIGGER_2] Esa misma moneda gobierna todas las horas. No se elige una nueva después de cada tirada. El valor de p permanece fijo, aunque nosotros no podamos verlo. [TRIGGER_3] Por eso, observar al gigante varias veces hace más creíble que nos haya tocado una moneda peligrosa. Observar muchas ausencias hace más creíble una moneda tranquila. No estamos cambiando la moneda: estamos aprendiendo cuál pudo ser. [TRIGGER_4] Esta diferencia es el corazón probabilístico del problema. Las apariciones son independientes si conocemos p; cuando p es desconocido y compartido, las observaciones de una hora cambian lo que podemos predecir de la siguiente."

## Descripcion Visual Detallada:

Duración orientativa: 01:00. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- NumberLine p∈[0,1] sin rótulos automáticos; curva de densidad uniforme MathTex(r"f_0(p)=1"); puntos ilustrativos 0.1,0.5,0.9 sin reemplazar el continuo.
- Un selector que entra en caja opaca y una sola moneda esquemática conectada a varias horas; Tex(r"\text{p fijo}") y Tex(r"\text{conocimiento cambiante}").

## Layout y disposicion:

- Eje p de x=-5.5 a 5.5, y=1.0; densidad en panel superior izquierdo de ancho 6.
- Caja de moneda en(0,-0.3,0); horas en x=-4,-2,0,2,4, y=-2; un único origen de flechas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Crear eje continuo y densidad plana; sombrear dos intervalos de igual longitud para mostrar igual probabilidad inicial, no asignar masa positiva a cada punto.
- [TRIGGER_2] **00:14–00:27:** Deslizar selector y ocultarlo dentro de caja. Conectar esa misma caja a todas las horas; no volver a sortear selector.
- [TRIGGER_3] **00:27–00:44:** Colocar una fila de apariciones y mover únicamente la representación de creencias hacia p altos; otra fila de ausencias lleva creencias a valores bajos. La caja del p real permanece inmóvil.
- [TRIGGER_4] **00:44–01:00:** Escribir independencia condicionada a p y dependencia al compartir p desconocido en dos tarjetas separadas. No dibujar una influencia causal de una aparición sobre la moneda.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para p oculto; ACCENT_CYAN para densidad de conocimiento; ACCENT_TERRACOTTA para observaciones; ACCENT_VINO para aparición del gigante, sin cambiar el parámetro real.

---

## Escena: 06

## Nombre: La trampa del cincuenta por ciento

## Descripcion Breve: Promediar p al inicio no autoriza a usar 1/2 para siempre.

## Objetivo Pedagogico: Motivar una actualización condicional y exhibir dependencia temporal.

## Voz en off:

> "[TRIGGER_1] Como al principio todos los valores de p son igualmente plausibles, la primera aparición tiene probabilidad un medio. Sería tentador usar ese mismo número en cada hora. [TRIGGER_2] Pero imaginemos que pasamos una hora escondidos y el gigante no aparece. Esa ausencia encaja mejor con probabilidades pequeñas que con probabilidades grandes. ¿De verdad seguimos igual de convencidos de que la próxima aparición vale un medio? [Pausa.] [TRIGGER_3] El problema se ve al calcular dos ausencias seguidas. Si p fuera conocido, su probabilidad sería uno menos p, al cuadrado. Como no lo conocemos, debemos promediar ese cuadrado sobre todos los valores posibles de p. [TRIGGER_4] El resultado es un tercio, no un cuarto. Promediar el peligro y después multiplicar pierde la relación entre ambas horas. Necesitamos conservar lo que la primera observación nos enseñó."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"\Pr(G_1)=\int_0^1p\,dp=1/2"); dos horas unidas a la misma p.
- MathTex(r"\Pr(\overline G_1,\overline G_2)=\int_0^1(1-p)^2\,dp=[-(1-p)^3/3]_0^1=1/3\ne1/4"); mostrar en dos líneas.

## Layout y disposicion:

- Primer promedio en y=1.8; dos horas en x=-2,2, y=0.6.
- Integral en y=-0.8 y evaluación en y=-1.8; comparación 1/3 frente 1/4 en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:13:** Write del primer promedio y sombrear área triangular bajo p; revelar 1/2.
- [TRIGGER_2] **00:13–00:32:** Mostrar ausencia observada y atenuar candidatas p altas. Dejar en pantalla la pregunta, sin escribir aún la probabilidad predictiva nueva.
- [TRIGGER_3] **00:32–00:49:** Construir dos factores 1-p desde la misma variable p, multiplicarlos y luego rodearlos con la integral. Contrastar con dos promedios separados como propuesta tachada.
- [TRIGGER_4] **00:49–01:03:** Evaluar explícitamente la primitiva en 1 y 0:0-(-1/3)=1/3. Marcar 1/4 como producto injustificado, no como error del valor inicial 1/2.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para área de promedio; ACCENT_INDIGO para p común; ACCENT_MINT para 1/3; ACCENT_VINO para producto incorrecto de medias.

---

## Escena: 07

## Nombre: El bosque de todos los futuros

## Descripcion Breve: El árbol de acciones y sucesos crece y contiene historias que podrían compartir futuro.

## Objetivo Pedagogico: Identificar la fuerza bruta y la pregunta sobre información suficiente.

## Voz en off:

> "[TRIGGER_1] Una salida sería dibujar todos los futuros: tres decisiones, los posibles ataques, los hallazgos, el veneno… y otra decisión después de cada resultado que permita seguir vivo. [TRIGGER_2] El árbol crece hora tras hora. Enumerarlo completo es exponencial. Y probar sólo secuencias fijas de acciones tampoco basta: una buena estrategia debe poder cambiar después de observar lo que pasó. [TRIGGER_3] Podríamos guardar una distribución entera de posibilidades para p en cada historia. Pero antes de inventar una cuadrícula de probabilidades y aproximar, hagamos una pregunta más útil. [TRIGGER_4] ¿Qué partes del pasado pueden cambiar realmente nuestras opciones futuras? Si dos historias nos dejan los mismos recursos y exactamente la misma información sobre el gigante, quizá no necesitemos resolver su futuro dos veces."

## Descripcion Visual Detallada:

Duración orientativa: 00:57. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Árbol de decisión con nodos Rectangle para elegir y Circle para azar, hojas de muerte Cross; tres capas explícitas y frontera de expansión sin valores inventados.
- Dos historias destacadas que convergen a dos tarjetas inicialmente sin fusionar; MathTex(r"3^N") rotulado sólo como secuencias fijas de acciones.

## Layout y disposicion:

- Árbol en x∈[-5.8,5.8], niveles y=2,0.8,-0.4; sólo rama activa desarrolla sucesos en zoom.
- Historias comparadas en(-3,-2.1,0),(3,-2.1,0). No mostrar 3^N como tamaño exacto del árbol adaptativo completo.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:13:** Expandir tres acciones desde la raíz y dos resultados ilustrativos desde cada una; formas distintas separan elegir de observar.
- [TRIGGER_2] **00:13–00:28:** Expandir otra capa de decisiones sobre ramas vivas; marcar la cuenta 3^N como insuficiente para planes adaptativos y la explosión del árbol como fenómeno mayor.
- [TRIGGER_3] **00:28–00:41:** Mostrar una curva de creencia junto a una hoja; proponer cuadrícula aproximada con puntos y retirarla para formular la pregunta sobre suficiencia, sin presentar una solución numérica adicional.
- [TRIGGER_4] **00:41–00:57:** Destacar dos hojas y transportar sus fichas de recursos y observaciones a tarjetas comparables. Dejar la fusión pendiente hasta demostrar qué información basta.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para decisiones; ACCENT_CYAN para azar; ACCENT_VINO para muerte; ACCENT_TERRACOTTA para historias candidatas a fusionarse.

---

## Escena: 08

## Nombre: Repartir credibilidad después de observar

## Descripcion Breve: Bayes repondera el continuo de valores p por la probabilidad de la observación.

## Objetivo Pedagogico: Derivar la forma de la posterior tras una aparición o una ausencia.

## Voz en off:

> "[TRIGGER_1] Para saber qué recordar, volvamos a una sola observación. Antes de verla, la densidad de p es plana. Si el gigante aparece, cada valor de p recibe un peso proporcional a la probabilidad de producir esa aparición: precisamente p. [TRIGGER_2] Por ejemplo, una aparición es nueve veces más probable con p igual a nueve décimas que con p igual a una décima. Eso compara verosimilitudes; no convierte esos dos puntos aislados en las únicas posibilidades. [TRIGGER_3] La recta p tiene área un medio. Para que los pesos vuelvan a sumar probabilidad uno, la multiplicamos por dos. Nuestra nueva densidad es dos p. [TRIGGER_4] Si observamos una ausencia, el peso es uno menos p. Su área también es un medio, y la densidad normalizada resulta dos veces uno menos p. Bayes aquí consiste en reponderar por lo observado y normalizar el área."

## Descripcion Visual Detallada:

Duración orientativa: 01:05. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Axes p de 0 a 1, densidad de 0 a 2.2, rótulos MathTex; curvas f 0=1, p,2 p,1-p,2(1-p) como VMobject exactos.
- MathTex(r"0.9/0.1=9"), MathTex(r"\int_0^1p\,dp=\int_0^1(1-p)\,dp=1/2"); leyendas Tex de peso sin normalizar y densidad posterior.

## Layout y disposicion:

- Gráfica en LEFT*2.5, ancho 6.2, alto 3.8, origen de ejes en(-5.5,-1.8,0).
- Ecuaciones a RIGHT*3.3, y=1.4,0.2,-1.0; normalización en y=-2.7. Mismo rango vertical en ambas observaciones.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Transform de densidad plana al peso p tras icono de aparición; sombrear área, rotulada todavía no normalizada.
- [TRIGGER_2] **00:18–00:34:** Marcar 0.1 y 0.9 con líneas verticales y comparar alturas. No sombrear cada punto como un evento de probabilidad positiva.
- [TRIGGER_3] **00:34–00:47:** Mostrar integral 1/2 y escalar verticalmente la recta por 2; verificar área final 1 con Brace o ecuación, no por altura máxima.
- [TRIGGER_4] **00:47–01:05:** Reiniciar a la misma densidad plana para un experimento distinto de ausencia; transformar a 1-p y después 2(1-p). No aplicar la ausencia después de la aparición anterior como si fueran dos observaciones acumuladas.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para densidad; ACCENT_TERRACOTTA para verosimilitud sin normalizar; ACCENT_MINT para área normalizada; ACCENT_INDIGO para eje p.

---

## Escena: 09

## Nombre: Predecir no es volver a empezar

## Descripcion Breve: Promediar p bajo cada posterior produce 2/3 o 1/3.

## Objetivo Pedagogico: Calcular la probabilidad siguiente como media posterior y conservar distinción entre p y estimación.

## Voz en off:

> "[TRIGGER_1] Para predecir la próxima aparición, cada posible p sigue siendo su probabilidad de ataque. Lo que cambió es el peso que le damos. Por eso promediamos p usando la nueva densidad. [TRIGGER_2] Después de una aparición, integramos p por dos p. Es dos veces la integral de p al cuadrado: dos tercios. El peligro real no aumentó; nuestra predicción cambió al aprender. [TRIGGER_3] Después de una ausencia, integramos p por dos veces uno menos p. Eso da dos veces un medio menos un tercio: un tercio. El próximo ataque se volvió menos creíble. [TRIGGER_4] Y así encajan las dos ausencias: la primera tiene probabilidad un medio. Después de verla, la segunda tiene probabilidad dos tercios. Multiplicamos un medio por dos tercios y recuperamos un tercio."

## Descripcion Visual Detallada:

Duración orientativa: 00:58. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"\Pr(G_{\mathrm{sig}}\mid\mathcal H)=\int_0^1p\,f(p\mid\mathcal H)\,dp").
- Dos evaluaciones completas MathTex(r"\int_0^1p(2p)\,dp=2[p^3/3]_0^1=2/3") y MathTex(r"\int_0^1p\,2(1-p)\,dp=2[p^2/2-p^3/3]_0^1=1/3"); árbol de ausencias con aristas 1/2 y 2/3.

## Layout y disposicion:

- Fórmula general y=2.1; curvas ponderadas 2 p² y 2 p(1-p) en dos paneles con centros(-3,0.2,0),(3,0.2,0), mismos ejes 0..1 y 0..2.2.
- Evaluaciones bajo cada panel y=-1.5; producto de ausencias en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Crear un multiplicador p que se aplica a la densidad posterior; distinguir gráficamente densidad y función integranda del promedio.
- [TRIGGER_2] **00:15–00:29:** Transform de 2 p a 2 p² y sombrear su área; revelar primitiva, evaluar extremos y obtener 2/3.
- [TRIGGER_3] **00:29–00:43:** Reiniciar al caso de ausencia; mostrar 2 p(1-p), su primitiva y evaluación 2(1/2-1/3)=1/3.
- [TRIGGER_4] **00:43–00:58:** Construir dos aristas de ausencia, primera 1/2 y segunda 1-1/3=2/3; multiplicar y reconciliar con el cálculo anterior. No multiplicar probabilidades de aparición por error.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para promedios; ACCENT_INDIGO para p real fijo; ACCENT_TERRACOTTA para condicionamiento; ACCENT_MINT para consistencia 1/3.

---

## Escena: 10

## Nombre: El pasado cabe en dos conteos

## Descripcion Breve: Historias con igual número de apariciones y ausencias tienen la misma verosimilitud.

## Objetivo Pedagogico: Demostrar que importa g y el tiempo, no el orden completo ni un sesgo adicional de supervivencia.

## Voz en off:

> "[TRIGGER_1] Antes de la hora i ya transcurrieron i menos una horas. Llamemos g al número de apariciones del gigante y a al número de ausencias. Así, a es i menos uno menos g. [TRIGGER_2] Una historia concreta tiene verosimilitud p elevado a g, por uno menos p elevado a a. Cambiar el orden de las observaciones no cambia ese producto: cada aparición aporta p y cada ausencia aporta uno menos p. [TRIGGER_3] En una historia que sigue viva conocemos esas observaciones. Escondidos, vemos si apareció. Fuera, sobrevivir demuestra que no apareció. Esa supervivencia ya cuenta como ausencia; no es otra evidencia adicional que debamos multiplicar otra vez. [TRIGGER_4] Las decisiones anteriores tampoco añaden un factor nuevo de p una vez fijada la historia observada. Los demás sucesos siguen las probabilidades independientes del modelo. Conservar los conteos basta para reconstruir nuestra información sobre el gigante."

## Descripcion Visual Detallada:

Duración orientativa: 01:06. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Fichas de historias 101 y 011, ambas de tres horas; MathTex(r"g=2,\ a=1,\ i=4"); MathTex(r"p^2(1-p)").
- MathTex(r"a=i-1-g,\qquad\mathcal L(p)=p^g(1-p)^a"); dos formas de observar ausencia: escondido o salir y sobrevivir.

## Layout y disposicion:

- Historias en y=1.5 y 0.5, fichas en x=-4,-2.8,-1.6; productos a x=2.4.
- Conteos en y=-0.7; ramas de observación en dos paneles y=-2.0. Rotular que 1 significa aparición y 0 ausencia, no victoria.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Crear calendario i-1 y partición en g apariciones, a ausencias. Fijar ejemplo de tres observaciones.
- [TRIGGER_2] **00:16–00:33:** Multiplicar explícitamente p·(1-p)·p y(1-p)·p·p; reordenar factores mediante TransformMatchingTex hacia p²(1-p). No añadir coeficiente binomial: son historias ordenadas concretas.
- [TRIGGER_3] **00:33–00:49:** Mostrar dos rutas que certifican ausencia y hacerlas desembocar en una sola ficha 0; impedir duplicar la ficha por haber sobrevivido.
- [TRIGGER_4] **00:49–01:06:** Encerrar la historia completa y marcar que la acción de cada hora ya estaba determinada por su pasado. Retirar factores independientes de p al normalizar; conservar sólo la verosimilitud del gigante.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_TERRACOTTA para conteos; ACCENT_INDIGO para productos de verosimilitud; ACCENT_CYAN para evidencia; ACCENT_VINO para presencia mortal sólo fuera del refugio.

---

## Escena: 11

## Nombre: De una curva a una probabilidad

## Descripcion Breve: La posterior general se normaliza y su media se expresa como cociente de integrales.

## Objetivo Pedagogico: Derivar la fórmula predictiva antes de simplificarla.

## Voz en off:

> "[TRIGGER_1] Con un prior uniforme, la forma de nuestra nueva densidad es ese mismo producto: p elevado a g por uno menos p elevado a a. Para convertirlo en densidad, dividimos entre el área total de la curva. [TRIGGER_2] Ahora queremos la probabilidad de una aparición más. Multiplicamos cada candidato p por su peso posterior y lo integramos. El denominador es la constante que normalizaba nuestros pesos. [TRIGGER_3] Queda un cociente de áreas. Arriba, la integral de p elevado a g más uno por uno menos p elevado a a. Abajo, la misma expresión, pero con exponente g en el primer factor. [TRIGGER_4] Parece que tendríamos que integrar una curva diferente en cada estado. Pero estas dos áreas están relacionadas de una forma exacta. Vamos a obtener esa relación, para reemplazar todas las integrales por una fracción pequeña."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"I=\int_0^1p^g(1-p)^a\,dp"), MathTex(r"f(p\mid\mathcal H)=p^g(1-p)^a/I").
- MathTex(r"J=\int_0^1p^{g+1}(1-p)^a\,dp"), MathTex(r"\alpha=\int_0^1p f(p\mid\mathcal H)\,dp=J/I"); para dibujo concreto g 2, a 1: peso p²(1-p), posterior 12 p²(1-p), integrando 12 p³(1-p).

## Layout y disposicion:

- Panel de curva a LEFT*3.0, ejes 0..1, densidad 0..2.3; fórmulas en RIGHT*2.7 divididas en tres líneas.
- Al pasar al cociente retirar gráfica y centrar J/I en y=0.6, definiciones de I y J en y=-0.6 y-1.7. Ningún texto principal bajo 24 pt.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Mostrar área I bajo el peso; dividir la altura de toda la curva por I y rotular área 1. Para ejemplo g 2, a 1 usar I=1/12, sin confundir peso con posterior.
- [TRIGGER_2] **00:17–00:31:** Transportar un factor p hacia el numerador de la media posterior, manteniendo I fuera de la integral por ser constante respecto a p.
- [TRIGGER_3] **00:31–00:47:** Destacar el cambio de exponente g→g+1 y definir J; escribir α=J/I. Aclarar visualmente que I>0 para g, a enteros no negativos.
- [TRIGGER_4] **00:47–01:03:** Mantener I y J como tarjetas de áreas; presentar un puente entre ellas aún sin valor para preparar la derivación siguiente, sin un salto de fórmula inexplicado.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para I; ACCENT_MINT para J y media; ACCENT_INDIGO para posterior; ACCENT_TERRACOTTA para exponente adicional.

---

## Escena: 12

## Nombre: La fracción escondida en las áreas

## Descripcion Breve: Una identidad de integrales produce (g+1)/(i+1) sin aproximación numérica.

## Objetivo Pedagogico: Explicar la simplificación exacta con extremos nulos e índices correctos.

## Voz en off:

> "[TRIGGER_1] Consideremos una curva auxiliar: p elevado a g más uno por uno menos p elevado a a más uno. Vale cero en ambos extremos. Por eso la integral de su derivada entre cero y uno es cero. [TRIGGER_2] Al derivar el producto aparecen dos términos. El primero aporta g más uno veces la integral de p elevado a g por uno menos p elevado a a más uno. El segundo resta a más uno veces nuestra integral J. [TRIGGER_3] La integral del primer término es I menos J, porque el factor adicional es uno menos p. Entonces, g más uno, multiplicado por la diferencia entre I y J, equivale a a más uno por J. Al distribuir y reagrupar, el producto de g más uno por I es igual al producto de g más a más dos por J. [TRIGGER_4] Al dividir, J sobre I es g más uno entre g más a más dos. Y como g más a es i menos uno, la probabilidad buscada es g más uno entre i más uno. En la primera hora obtenemos un medio; una aparición lleva a dos tercios y una ausencia a un tercio."

## Descripcion Visual Detallada:

Duración orientativa: 01:28. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"z(p)=p^{g+1}(1-p)^{a+1},\quad z(0)=z(1)=0").
- Derivación por líneas MathTex(r"0=(g+1)\int_0^1p^g(1-p)^{a+1}dp-(a+1)J"), MathTex(r"\int_0^1p^g(1-p)^{a+1}dp=I-J"), MathTex(r"(g+1)(I-J)=(a+1)J"), MathTex(r"(g+1)I=(g+a+2)J"), MathTex(r"\alpha_{i,g}=J/I=(g+1)/(i+1)").

## Layout y disposicion:

- Curva auxiliar pequeña con extremos en(-5,0,0),(-2,0,0), cabecera en y=2.2.
- Derivación central en panel x∈[-5.9,5.9], máximo tres líneas simultáneas y=1.1,0,-1.1; resultado final en y=-2.4. Sustituir líneas ya leídas por el siguiente paso.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Dibujar curva auxiliar con extremos cero; escribir integral de z′=z(1)-z(0)=0. Para una forma concreta puede usarse g=a=1, rotulada ejemplo, sin cambiar la derivación general.
- [TRIGGER_2] **00:17–00:36:** Aplicar regla del producto y cadena: mostrar factores g+1 y-(a+1) en colores distintos; integrar los dos términos y reconocer J en el segundo.
- [TRIGGER_3] **00:36–01:03:** Expandir(1-p) en la primera integral para mostrar I-J; sustituir y luego pasar-(g+1)J al otro lado. Agrupar los coeficientes(g+1)+(a+1)=g+a+2.
- [TRIGGER_4] **01:03–01:28:** Dividir por I positivo, sustituir g+a=i-1 y obtener denominador i+1. Comprobar(i, g)=(1,0),(2,1),(2,0) con resultados 1/2,2/3,1/3. Nota técnica: la posterior es Beta(g+1, i-g), pero su nombre no sustituye esta derivación.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para I; ACCENT_MINT para J; ACCENT_TERRACOTTA para coeficientes y signo de derivada; TEXT_MAIN para igualdad; ACCENT_INDIGO para probabilidad predictiva.

---

## Escena: 13

## Nombre: Cuatro números en vez de una biografía

## Descripcion Breve: El tiempo, las baterías, el hambre y las apariciones identifican un estado suficiente.

## Objetivo Pedagogico: Justificar la fusión de historias y distinguir p fijo de α actualizado.

## Voz en off:

> "[TRIGGER_1] Ya podemos volver al bosque de futuros. Una historia viva se resume con cuatro números: la hora i, las baterías s, el hambre h y las apariciones anteriores g. [TRIGGER_2] La hora dice qué probabilidades conocidas corresponden ahora. Baterías y hambre dicen qué podemos soportar. La hora y g reconstruyen nuestra predicción del gigante mediante la fracción que acabamos de demostrar. [TRIGGER_3] Dos historias que llegan a esos mismos cuatro números tienen las mismas opciones y la misma distribución de futuros. Por ejemplo, tres horas escondidos, con dos apariciones en distinto orden, dejan la misma información si también coinciden las reservas y el hambre. [TRIGGER_4] Así podemos fusionar sus ramas. No guardamos p, porque no lo conocemos; tampoco guardamos toda la curva, porque los conteos permiten recuperarla. Guardamos justo lo necesario para decidir desde aquí."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Tarjeta MathTex(r"(i,s,h,g)"); rangos MathTex(r"1\le i\le N,\ 0\le s\le K,\ 0\le h<H,\ 0\le g\le i-1").
- Historias 101 y 011 con tres escondites, H=4, S=2, mismo estado(4,2,3,2), MathTex(r"\alpha=3/5"); ramas fusionadas en nodo único.

## Layout y disposicion:

- Cuatro registros en x=-4.5,-1.5,1.5,4.5, y=1.4; glosas bajo cada uno.
- Historias en(-3,-0.5,0),(3,-0.5,0), nodo común(0,-2,0). Tomar N>=4 en ejemplo de fusión para que hora 4 exista.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Recuperar dos ramas del árbol y desarmarlas en cuatro fichas de estado.
- [TRIGGER_2] **00:14–00:29:** Conectar i a hoja de probabilidades, baterías a lámpara, hambre a contador, y(i, g) a α; no añadir una quinta coordenada para p.
- [TRIGGER_3] **00:29–00:49:** Mostrar 101 y 011 durante tres escondites con H=4; calcular explícitamente i=4, s=2, h=3, g=2 y α=3/5 en ambos casos.
- [TRIGGER_4] **00:49–01:03:** ReplacementTransform de ambos nodos hacia uno; sus futuros se dibujan una sola vez. Anotar que la igualdad exige coincidir los cuatro números, no sólo g.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para estado; ACCENT_CYAN para i y probabilidades; ACCENT_TERRACOTTA para h; ACCENT_MINT para fusión exacta.

---

## Escena: 14

## Nombre: Una probabilidad desde aquí

## Descripcion Breve: El valor F mide supervivencia futura condicionada al estado vivo.

## Objetivo Pedagogico: Definir bases, normalización de recursos y horizonte sin duplicar probabilidad de llegada.

## Voz en off:

> "[TRIGGER_1] En cada estado guardaremos una pregunta concreta: si ya llegué vivo hasta aquí, ¿cuál es la mayor probabilidad de sobrevivir las horas que faltan? Llamemos F a ese valor. [TRIGGER_2] No es la probabilidad de haber llegado. Esa parte de la historia ya está condicionada. Si una rama futura ocurre con cierta probabilidad, multiplicaremos por F del estado al que conduce, una sola vez. [TRIGGER_3] Al terminar las N horas, un estado todavía vivo tiene valor uno. Un estado que alcanza hambre H tiene valor cero. La comprobación de muerte va antes que el éxito de haber acabado el calendario. [TRIGGER_4] Para las transiciones usaremos una puerta de entrada común: si el hambre nueva es inválida, devuelve cero; si es válida, limita las baterías a K y consulta F en la hora siguiente. Así todas las acciones respetan las mismas reglas."

## Descripcion Visual Detallada:

Duración orientativa: 01:05. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"F(i,s,h,g)=\max\Pr(\text{sobrevivir hasta }N\mid\text{estado vivo actual})"); texto partido en dos objetos.
- Bases MathTex(r"h\ge H\Rightarrow0"), MathTex(r"i=N+1,\ h<H\Rightarrow1"); sucesor MathTex(r"D_i(s^{\prime},h^{\prime},g^{\prime})=0\ \text{si }h^{\prime}\ge H") y MathTex(r"D_i=F(i+1,\min(K,s^{\prime}),h^{\prime},g^{\prime})\ \text{si }h^{\prime}<H").

## Layout y disposicion:

- F actual en(0,1.8,0); historia pasada atenuada a izquierda y futuro a derecha.
- Puerta de validación en(0,-0.2,0), salida muerte en(-3,-1.6,0), siguiente capa en(3,-1.6,0). Definición D en y=-2.7 por dos líneas sucesivas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Encerrar estado actual con rótulo ya vivo; atenuar camino pasado, sin borrarlo como suceso ocurrido.
- [TRIGGER_2] **00:14–00:30:** Mostrar una arista de probabilidad w hacia un nodo con valor F′; producir contribución wF′. Tachar sólo una multiplicación adicional por probabilidad del pasado.
- [TRIGGER_3] **00:30–00:46:** Crear nodos terminales 0 y 1 y una compuerta de hambre delante del calendario final; estado h=H desemboca siempre en 0.
- [TRIGGER_4] **00:46–01:05:** Construir D_i como alias de lectura de sucesor, no como nueva dimensión de DP. Mostrar h inválida→0 y h válida→saturar s′→F siguiente. Sólo se invoca con s′>=0; las ramas sin baterías suficientes se eliminan antes.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para F; ACCENT_CYAN para aristas; ACCENT_MINT para terminal 1; ACCENT_VINO para 0 mortal; TEXT_MUTED para pasado condicionado.

---

## Escena: 15

## Nombre: Esconderse: dos futuros que sí podemos observar

## Descripcion Breve: El refugio preserva baterías, aumenta hambre y actualiza g según la aparición.

## Objetivo Pedagogico: Derivar ambas ramas de esconderse y su valor esperado completo.

## Voz en off:

> "[TRIGGER_1] Si nos escondemos, conservamos las baterías y pasamos una hora sin comer. El hambre aumenta en uno. El gigante puede aparecer o no; lo observamos y seguimos protegidos de él. [TRIGGER_2] Con probabilidad alfa aparece y el contador g aumenta en uno. Con probabilidad uno menos alfa no aparece y g se queda igual. En ambos casos avanzamos a la hora siguiente. [TRIGGER_3] El valor de esconderse es la suma de esas dos probabilidades por sus valores futuros. Si el hambre nueva alcanza H, ambos valores futuros son cero: estar a salvo del gigante no evita morir de hambre. [TRIGGER_4] La probabilidad del fotosensible no entra en esta cuenta. Dentro del refugio no necesitamos la lámpara. Esconderse puede conservar recursos y producir información, pero su valor también depende del tiempo que nos queda para comer."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Árbol raíz escondite→dos hojas; MathTex(r"\alpha=(g+1)/(i+1)").
- MathTex(r"A_{\rm hide}=\alpha D_i(s,h+1,g+1)+(1-\alpha)D_i(s,h+1,g)"); etiquetas de estado con i+1 en ambas hojas.

## Layout y disposicion:

- Raíz(0,1.5,0); hojas(-3.2,-0.2,0),(3.2,-0.2,0); probabilidades sobre aristas en y=0.8.
- Fórmula en dos sumandos y=-1.5,-2.25; compuerta común de hambre debajo de raíz para demostrar caso mortal sin borrar las probabilidades.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Mover avatar a refugio y actualizar fichas s→s, h→h+1. No consumir baterías por una aparición dentro.
- [TRIGGER_2] **00:14–00:29:** Crear rama α con g→g+1 y rama 1-α con g→g; actualizar i→i+1 en ambas.
- [TRIGGER_3] **00:29–00:46:** Multiplicar cada probabilidad por D de su hoja y sumar. Si h+1=H, transformar ambas hojas en 0 y obtener α·0+(1-α)·0=0.
- [TRIGGER_4] **00:46–01:02:** Retirar q_i y lámpara de este árbol mediante atenuación, indicando que se marginalizan sucesos sin efecto, no que q_i sea cero en el exterior.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para refugio; ACCENT_TERRACOTTA para h y g; ACCENT_CYAN para pesos; ACCENT_MINT para ramas protegidas del ataque, sin implicar supervivencia segura al hambre.

---

## Escena: 16

## Nombre: Salir: la rama que no tiene continuación

## Descripcion Breve: El gigante elimina las ramas exteriores y el fotosensible exige reserva inicial.

## Objetivo Pedagogico: Factorizar correctamente el riesgo sin renormalizar ramas supervivientes.

## Voz en off:

> "[TRIGGER_1] Al salir hay una separación inmediata en nuestro árbol de cálculo. Si aparece el gigante, morimos. Esa rama tiene probabilidad alfa y valor futuro cero. [TRIGGER_2] Sólo la ausencia del gigante, con probabilidad uno menos alfa, permite continuar. Dentro de esa rama consideramos al fotosensible: aparece con probabilidad q, y para defendernos necesitamos al menos dos baterías iniciales. [TRIGGER_3] Este orden del árbol organiza el cálculo; no inventa una cronología física entre encuentros y hallazgos. La restricción temporal que sí debemos respetar es que la lámpara usa las baterías que ya teníamos. [TRIGGER_4] Y cuando descartamos una rama mortal no repartimos su probabilidad entre las demás. Su contribución sigue siendo cero. El factor uno menos alfa debe permanecer multiplicando todo el valor de salir."

## Descripcion Visual Detallada:

Duración orientativa: 00:58. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Árbol gigante α→0, ausencia 1-α→fotosensible q/1-q; guarda MathTex(r"\mathbf1_{s\ge2}").
- MathTex(r"A_{\rm salir}=\alpha\cdot0+(1-\alpha)\,V_{\rm sin\ gigante}"); barras de masa probabilística con un segmento mortal conservado.

## Layout y disposicion:

- Raíz(-4.8,1.3,0); gigante(-1.8,2,0), ausencia(-1.8,0.4,0); fotosensible en(2,-0.2,0) y(2,1,0).
- Valor general en y=-1.7; barra de probabilidades en y=-2.6. Reservar x>4 para resultados de defensa, no para ramas de comida todavía.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:12:** Crear rama α que desemboca en 0; dejar su anchura visible como masa perdida.
- [TRIGGER_2] **00:12–00:27:** Crear rama 1-α y bifurcar en q y 1-q; si s<2 dirigir q a muerte, si s>=2 restar 2 de reserva.
- [TRIGGER_3] **00:27–00:43:** Mostrar rótulo árbol de probabilidades, no reloj de sucesos. Recuperar sello reserva inicial en la guarda s≥2.
- [TRIGGER_4] **00:43–00:58:** Sumar α·0 y(1-α)V; retirar sólo el término cero escrito, conservando su riesgo en el factor. No escalar las ramas restantes para que sumen 1 de forma incondicional.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_VINO para masa mortal; ACCENT_CYAN para probabilidades; ACCENT_TERRACOTTA para guarda inicial; ACCENT_INDIGO para nodo condicional.

---

## Escena: 17

## Nombre: Buscar batería: las cuatro hojas

## Descripcion Breve: Ausencia o presencia del fotosensible se combina con hallazgo o no hallazgo.

## Objetivo Pedagogico: Enumerar sin omisiones los cuatro sucesores vivos posibles.

## Voz en off:

> "[TRIGGER_1] Condicionados a que no apareció el gigante, buscar batería deja cuatro combinaciones. Sin fotosensible y con hallazgo, la reserva aumenta en uno, hasta K. Su probabilidad es uno menos q por b. [TRIGGER_2] Sin fotosensible y sin hallazgo, la reserva no cambia. La probabilidad es uno menos q por uno menos b. En las dos ramas el hambre aumenta: una batería no es comida. [TRIGGER_3] Con fotosensible y hallazgo, si empezamos con al menos dos baterías, gastamos dos y encontramos una: terminamos con s menos uno. El peso es q por b. [TRIGGER_4] Con fotosensible y sin hallazgo, terminamos con s menos dos y el peso es q por uno menos b. Esas dos ramas son mortales si empezamos con menos de dos. Todos los sucesores vivos mantienen g, porque ya sabemos que el gigante estuvo ausente."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Cuatro filas MathTex de pesos(1-q_i)b_i,(1-q_i)(1-b_i), q_i b_i, q_i(1-b_i).
- Estados por fila: MathTex(r"(\min(K,s+1),h+1,g)"),MathTex(r"(s,h+1,g)"),MathTex(r"(s-1,h+1,g)"),MathTex(r"(s-2,h+1,g)"); sello s≥2 en últimas dos.

## Layout y disposicion:

- Tabla visual cuatro filas y=1.5,0.55,-0.4,-1.35; columna resultado x=-4.8, peso x=-1.8, estado x=2.8.
- Cabecera en y=2.4 especifica sin gigante y todos avanzan a i+1. Pie con h+1<H en y=-2.65. No omitir filas con probabilidades cero.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Construir primera fila con iconos no ataque y hallazgo; actualizar s→min(K, s+1) y h→h+1.
- [TRIGGER_2] **00:15–00:30:** Construir segunda fila, conservar s y actualizar h. Sumar las dos masas del bloque sin ataque:(1-q)b+(1-q)(1-b)=1-q.
- [TRIGGER_3] **00:30–00:43:** Crear tercera fila con s≥2; animar s→s-2→s-1, manteniendo g. Mostrar peso qb.
- [TRIGGER_4] **00:43–01:03:** Crear cuarta fila con s→s-2. Aplicar guarda s≥2 a ambas filas de ataque y validador de hambre a las cuatro; no producir un registro con s negativo.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para baterías y pesos; ACCENT_TERRACOTTA para hambre; ACCENT_VINO para guardas incumplidas; ACCENT_INDIGO para columna de sucesores.

---

## Escena: 18

## Nombre: La fórmula de batería sale del diagrama

## Descripcion Breve: Las cuatro hojas se ponderan, se suman y se multiplican por la ausencia del gigante.

## Objetivo Pedagogico: Construir A_bat y mostrar por qué morir de hambre anula incluso hallazgos seguros.

## Voz en off:

> "[TRIGGER_1] Cada una de esas hojas tiene un valor de continuación. Multiplicamos su probabilidad por ese valor y sumamos. Primero las dos ramas sin fotosensible; después, si la reserva lo permite, las dos ramas con fotosensible. [TRIGGER_2] Todo el conjunto se multiplica por uno menos alfa, porque este árbol sólo era posible cuando no apareció el gigante. Así obtenemos el valor de buscar batería desde el estado actual. [TRIGGER_3] Observa qué ocurre si h vale H menos uno. Las cuatro hojas intentan pasar a hambre H. Nuestra puerta de validación las convierte en cero. Buscar una batería no puede salvarnos de una necesidad inmediata de comida. [TRIGGER_4] En cambio, con margen de hambre, una batería puede mejorar la supervivencia de horas posteriores. No la valoramos por el objeto en sí, sino por el futuro que permite alcanzar."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"B_0=b_iD_i(s+1,h+1,g)+(1-b_i)D_i(s,h+1,g)").
- MathTex(r"B_1=b_iD_i(s-1,h+1,g)+(1-b_i)D_i(s-2,h+1,g)"); MathTex(r"A_{\rm bat}=(1-\alpha)[(1-q_i)B_0+\mathbf1_{s\ge2}q_iB_1]").

## Layout y disposicion:

- B0 en y=1.5 y B1 en y=0.4, cada fórmula ancho máximo 11.7; si es necesario separar los dos términos en filas alineadas.
- Combinación final en y=-1.0; demostración hambre al límite en y=-2.3. Las referencias B0, B1 permanecen visibles al presentar combinación.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Transportar las cuatro hojas a los dos sumandos B0, B1, conservando etiquetas; no evaluar B1 con s<2: la guarda elimina ese bloque antes de leer estados.
- [TRIGGER_2] **00:16–00:31:** Agrupar bloques con 1-q yq, y envolverlos con 1-α. Indicar que D_i satura s+1 dentro de su definición.
- [TRIGGER_3] **00:31–00:48:** Sustituir h=H-1 y mostrar las cuatro lecturas D_i(..., H,...)=0; propagar ceros hacia A_bat=0 sin renormalizar.
- [TRIGGER_4] **00:48–01:02:** Restaurar h<H-1 y conectar una hoja de mayor reserva con un valor F futuro simbólico. No afirmar que buscar batería siempre sea mejor: eso depende de los valores calculados.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para valores F y D; ACCENT_CYAN para batería; ACCENT_TERRACOTTA para límite de hambre; ACCENT_MINT para sumas correctas.

---

## Escena: 19

## Nombre: Buscar comida: encontrar no basta

## Descripcion Breve: Cada búsqueda se divide en alimento seguro, alimento venenoso y ausencia de alimento.

## Objetivo Pedagogico: Distinguir tres resultados exhaustivos y su efecto sobre h.

## Voz en off:

> "[TRIGGER_1] La comida tiene una bifurcación extra. Con probabilidad c encontramos alimento. Dentro de esa rama, una fracción v es venenosa y una fracción uno menos v permite comer y seguir vivo. [TRIGGER_2] Por eso, encontrar comida segura pesa c por uno menos v. Su efecto es reiniciar el hambre a cero. Encontrar veneno pesa c por v y termina en muerte. [TRIGGER_3] Con probabilidad uno menos c no encontramos nada. No morimos por veneno, pero el hambre aumenta en uno y podría matarnos si llega al límite. [TRIGGER_4] Los tres pesos suman uno: comida segura, comida venenosa y ningún hallazgo. No existe una cuarta rama en la que encontramos veneno y simplemente seguimos con hambre. El enunciado dice que el veneno mata."

## Descripcion Visual Detallada:

Duración orientativa: 00:57. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Árbol hallazgo c→seguro 1-v/veneno v, y no hallazgo 1-c.
- MathTex(r"c_i(1-v_i)+c_iv_i+(1-c_i)=1"); sucesores h 0, h+1 y nodo 0 muerte.

## Layout y disposicion:

- Raíz(-4.8,0.8,0); hallazgo(-1.8,1.6,0), no hallazgo(-1.8,-0.7,0); tres hojas x=3.8, y=1.9,0.6,-0.9.
- Suma de masas en y=-2.1; aviso veneno no equivale a ayuno en y=-2.9. Sólo se desarrolla el hallazgo alimenticio, condicionado a superar ataques.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Crear bifurcación c/1-c y dividir únicamente la rama c en 1-v/v; no asignar veneno a no hallazgo.
- [TRIGGER_2] **00:15–00:29:** Construir peso c(1-v) y reset h→0; en la hoja venenosa escribir cv·0.
- [TRIGGER_3] **00:29–00:41:** Crear no hallazgo con peso 1-c y h→h+1; pasar por validador hambre antes de declarar supervivencia.
- [TRIGGER_4] **00:41–00:57:** Sumar pesos: c(1-v)+cv=c, luego c+1-c=1. Tachar una flecha hipotética veneno→h+1 para fijar la regla.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_MINT para alimento seguro; ACCENT_VINO para veneno; ACCENT_TERRACOTTA para hambre; ACCENT_CYAN para probabilidades.

---

## Escena: 20

## Nombre: Comida y ataques en la misma cuenta

## Descripcion Breve: Las tres salidas alimenticias se combinan con ambos resultados del fotosensible.

## Objetivo Pedagogico: Derivar las cuatro contribuciones vivas y todas las ramas mortales de A_food.

## Voz en off:

> "[TRIGGER_1] Ahora colocamos ese pequeño árbol detrás de cada resultado del fotosensible. Sin ataque, conservamos s: comida segura lleva a hambre cero; no encontrarla lleva a h más uno; el veneno lleva a cero supervivencia. [TRIGGER_2] Con ataque, sólo continuamos si había dos baterías iniciales. La reserva pasa a s menos dos. Comida segura reinicia el hambre; no encontrarla la aumenta; el veneno vuelve a ser mortal. [TRIGGER_3] Ponderamos el primer bloque por uno menos q y el segundo por q, cuando s lo permite. Y ambos por uno menos alfa: las apariciones del gigante fuera ya eran mortales. [TRIGGER_4] Quedan cuatro contribuciones potencialmente vivas y dos de veneno con valor cero. También valen cero las ramas sin defensa o con hambre inválida. La fórmula compacta no elimina esos riesgos: conserva sus pesos en los factores de supervivencia."

## Descripcion Visual Detallada:

Duración orientativa: 01:04. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Dos bloques completos de tres hojas cada uno; filas sin ataque:(s,0, g), muerte,(s, h+1, g); con ataque:(s-2,0, g), muerte,(s-2, h+1, g).
- MathTex(r"C_0=c_i(1-v_i)D_i(s,0,g)+(1-c_i)D_i(s,h+1,g)"); MathTex(r"C_1=c_i(1-v_i)D_i(s-2,0,g)+(1-c_i)D_i(s-2,h+1,g)"); MathTex(r"A_{\rm food}=(1-\alpha)[(1-q_i)C_0+\mathbf1_{s\ge2}q_iC_1]").

## Layout y disposicion:

- Bloques izquierdo y derecho centrados x=-3.1,3.1, y=0.8, anchos 5.5, altos 2.8; tres hojas de cada uno en filas y=1.3,0.35,-0.6.
- Primero mostrar árbol; después reemplazarlo por C0, C1 en y=1.4,0,-1.4 para fórmula exterior. Nunca comprimir seis hojas y tres ecuaciones simultáneas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Recrear tres hojas sin fotosensible con pesos c(1-v), cv,1-c, reserva s y actualización de hambre explícita.
- [TRIGGER_2] **00:16–00:31:** Recrear tres hojas con fotosensible, guarda s≥2, reserva s-2 y los mismos tres pesos alimenticios. Si guarda falla, todo ese bloque termina en 0.
- [TRIGGER_3] **00:31–00:46:** Añadir factores exteriores 1-q, q y 1-α. Transportar hojas vivas a C0, C1; mostrar primero términos veneno cv·0 antes de retirarlos de la escritura.
- [TRIGGER_4] **00:46–01:04:** Revelar A_food y relacionar cada uno de sus cuatro términos con su hoja. Señalar que D_i todavía elimina hambre H y que nunca se evalúan reservas negativas.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_MINT para h=0; ACCENT_CYAN para reserva y pesos; ACCENT_VINO para tres causas de muerte; ACCENT_INDIGO para valores futuros; ACCENT_TERRACOTTA para guardas.

---

## Escena: 21

## Nombre: Sumar el azar, elegir la acción

## Descripcion Breve: Los tres valores de acción se comparan después de sumar sus resultados.

## Objetivo Pedagogico: Formular Bellman respetando el orden de información.

## Voz en off:

> "[TRIGGER_1] Ya tenemos un número para cada acción: esconderse, buscar batería y buscar comida. Cada número resume todos los resultados posibles de esa acción y la mejor continuación después de observarlos. [TRIGGER_2] Como ahora debemos elegir una sola acción, nos quedamos con el mayor de los tres. Ése es F del estado actual. Sumamos dentro de cada árbol porque no controlamos el azar; tomamos un máximo entre árboles porque sí controlamos la decisión. [TRIGGER_3] La posición del máximo importa. No podemos escoger esconderse sólo en las ramas donde aparece el gigante y buscar comida sólo donde no aparece. Eso sería decidir después de conocer un suceso que todavía no observamos. [TRIGGER_4] Lo que sí podemos hacer es elegir una nueva acción en la hora siguiente, cuando ya conocemos el estado al que llegamos. Esa adaptación está incorporada en cada valor F de las hojas."

## Descripcion Visual Detallada:

Duración orientativa: 01:06. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Tres nodos cuadrados de decisión con etiquetas A_hide, A_bat, A_food y círculos de azar debajo; hojas F.
- MathTex(r"F(i,s,h,g)=\max\{A_{\rm hide},A_{\rm bat},A_{\rm food}\}"); dos capas temporalesi e i+1.

## Layout y disposicion:

- Tres columnas con centros x=-4.1,0,4.1; raíces y=1.6, azar 0.5, hojas-0.5.
- Máximo final en y=-1.6; eje temporal en y=-2.6. Sólo tres números simbólicos visibles, sin beneficios ficticios elegidos arbitrariamente.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Contraer cada árbol por separado en su suma ponderada A; mantener colores que permitan reconocer sus ramas.
- [TRIGGER_2] **00:14–00:33:** Crear selector máximo sobre las tres tarjetas A y depositar el resultado en F. Etiquetar círculos con suma y cuadrados con máximo.
- [TRIGGER_3] **00:33–00:50:** Dibujar un selector hipotético dentro del nodo de azar y Cross: conectaría la decisión actual a información futura. Mantener la fórmula correcta intacta.
- [TRIGGER_4] **00:50–01:06:** Señalar los cuadrados de decisión en la capa i+1 como adaptaciones válidas, distinguiéndolos del selector prohibido dentro de la misma hora.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para elegir; ACCENT_CYAN para azar; ACCENT_MINT para valor óptimo; ACCENT_VINO para anticipación ilegal.

---

## Escena: 22

## Nombre: Dos horas para ver el futuro hacia atrás

## Descripcion Breve: Una instancia pequeña permite resolver primero los estados de la última hora.

## Objetivo Pedagogico: Establecer la traza completa y calcular sus tres sucesores relevantes.

## Voz en off:

> "[TRIGGER_1] Hagamos una partida de dos horas. Tenemos dos baterías y capacidad para dos. El hambre mata al llegar a dos. Encontrar comida es seguro, no hay veneno ni fotosensibles, y fijamos también el hallazgo de batería como seguro. [TRIGGER_2] Empecemos por la última hora. Si llegamos con hambre cero, podemos escondernos: acabaremos con hambre uno y sobreviviremos con certeza. Salir no puede mejorar una probabilidad que ya vale uno. [TRIGGER_3] Si llegamos con hambre uno, esconderse o buscar batería mata de hambre. Hay que buscar comida. Sin apariciones previas del gigante, su probabilidad ahora es un tercio; sobrevivimos con probabilidad dos tercios. [TRIGGER_4] Si, en cambio, ya observamos una aparición, la probabilidad del gigante es dos tercios y sobrevivimos al buscar comida con un tercio. Mismos recursos, distinta información: cambia el valor de continuar."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Ficha MathTex(r"N=2,K=S=2,H=2;\ b_i=c_i=1,\ v_i=q_i=0\ (i=1,2)").
- Tres estados(2,2,0,0)→1,(2,2,1,0)→2/3,(2,2,1,1)→1/3; en cada uno pequeñas tarjetas de acciones con sus valores.

## Layout y disposicion:

- Parámetros en dos líneas y=2.2,1.7; estados en tres columnas x=-4.1,0,4.1, y=0.7.
- Valores de acciones en y=-0.4,-1.1,-1.8, alineados; final de hora 2 en y=-2.7. Se calcula hacia atrás sin que el agente conozca resultados futuros.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Write de todos los parámetros; apagar riesgos q yv por ser cero. Mantener gigante activo y p oculto.
- [TRIGGER_2] **00:18–00:32:** En estado(2,2,0,0), mostrar esconderse 1 y salir 1-α=2/3 para batería y comida; máximo 1.
- [TRIGGER_3] **00:32–00:47:** En(2,2,1,0), convertir hide y bat en 0 por hambre; calcular α=(0+1)/3=1/3 y food=2/3.
- [TRIGGER_4] **00:47–01:02:** En(2,2,1,1), mantener hide=bat=0 y calcular α=(1+1)/3=2/3, food=1/3. Conservar estos tres valores para las escenas 23 y 24.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_MINT para valores vivos; ACCENT_TERRACOTTA para h y g distintos; ACCENT_VINO para hambre mortal; ACCENT_INDIGO para estados.

---

## Escena: 23

## Nombre: Esconderse primero: aprender sin comer

## Descripcion Breve: Las dos observaciones al esconderse conducen a valores diferentes de la última hora.

## Objetivo Pedagogico: Calcular A_hide=1/2 mediante probabilidad total.

## Voz en off:

> "[TRIGGER_1] Volvamos al comienzo: primera hora, dos baterías, hambre cero y ninguna observación. La probabilidad inicial del gigante es un medio. [TRIGGER_2] Si nos escondemos y aparece, sobrevivimos al encuentro, pero llegamos con hambre uno y una aparición registrada. Ya calculamos que desde ahí la última hora se supera con probabilidad un tercio. [TRIGGER_3] Si nos escondemos y no aparece, llegamos también con hambre uno, pero con cero apariciones. Ese futuro vale dos tercios. [TRIGGER_4] Multiplicamos cada rama por su probabilidad: un medio por un tercio, más un medio por dos tercios. Un sexto más un tercio: un medio. Esconderse primero ofrece una probabilidad total de supervivencia de cincuenta por ciento."

## Descripcion Visual Detallada:

Duración orientativa: 00:52. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Raíz(1,2,0,0), ramas α=1/2 y 1-α=1/2 hacia(2,2,1,1) y(2,2,1,0).
- MathTex(r"A_{\rm hide}=\tfrac12\cdot\tfrac13+\tfrac12\cdot\tfrac23=\tfrac16+\tfrac13=\tfrac12").

## Layout y disposicion:

- Raízy=1.6; hojas x=-3,3, y=-0.1, con g rotulado.
- Contribuciones 1/6 y 1/3 debajo de hojas y=-1.25; suma en y=-2.4. Sin mostrar inicialmente la fórmula completa antes de construir ramas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:10:** Recuperar parámetros de escena 22 en una ficha pequeña y crear raíz con α1/2.
- [TRIGGER_2] **00:10–00:25:** Crear aparición con peso 1/2; incrementar h a 1, g a 1; copiar valor 1/3 desde tabla de última hora.
- [TRIGGER_3] **00:25–00:35:** Crear ausencia con peso 1/2; incrementar h a 1 y mantener g 0; copiar valor 2/3.
- [TRIGGER_4] **00:35–00:52:** Multiplicar pesos por continuaciones y sumar 1/6+1/3=1/2. No tratar los valores de hoja como probabilidades incondicionales ni normalizar nuevamente.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para esconderse; ACCENT_CYAN para pesos 1/2; ACCENT_TERRACOTTA para evidencia; ACCENT_MINT para cálculo final.

---

## Escena: 24

## Nombre: Comida, batería y la decisión inicial

## Descripcion Breve: Las otras dos acciones producen 1/2 y 1/3, y el óptimo inicial vale1/2.

## Objetivo Pedagogico: Completar la traza de todas las acciones y explicar un empate óptimo.

## Voz en off:

> "[TRIGGER_1] Si buscamos comida en la primera hora, una aparición del gigante nos mata. Si no aparece, encontramos comida segura y el hambre vuelve a cero. En la última hora podemos escondernos y sobrevivir. [TRIGGER_2] Por tanto, buscar comida vale un medio por cero más un medio por uno: un medio. Empata con esconderse primero, aunque los caminos que justifican ese valor son diferentes. [TRIGGER_3] Si buscamos batería, también necesitamos que no aparezca el gigante. La bolsa ya está llena, así que seguimos con dos baterías; el hambre sube a uno y g sigue en cero. Ese futuro vale dos tercios. El total es un medio por dos tercios: un tercio. [TRIGGER_4] Comparamos: esconderse, un medio; comida, un medio; batería, un tercio. La probabilidad óptima es un medio. Podemos elegir cualquiera de las dos acciones empatadas y después seguir la mejor decisión del estado que observemos."

## Descripcion Visual Detallada:

Duración orientativa: 01:07. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Dos árboles completos food y bat, cada uno con rama gigante 1/2→0 y ausencia 1/2→sucesor.
- MathTex(r"A_{\rm food}=\tfrac12\cdot0+\tfrac12\cdot1=\tfrac12"), MathTex(r"A_{\rm bat}=\tfrac12\cdot0+\tfrac12\cdot\tfrac23=\tfrac13"),MathTex(r"F(1,2,0,0)=\max\{1/2,1/3,1/2\}=1/2").

## Layout y disposicion:

- Árbol activo ocupa x∈[-5.5,5.5], raíz y=1.6, hojas y=0.2; se muestra uno por vez.
- Al final tabla de tres acciones en x=-4,0,4, y=-0.4; valor óptimo en y=-2.0. Orden de max rotulado hide, bat, food para evitar confundir 1/3 con comida.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Construir food: gigante→0; ausencia→(2,2,0,0)→1, mostrando reinicio h 0.
- [TRIGGER_2] **00:16–00:30:** Sumar 1/2·0+1/2·1. Guardar tarjeta food 1/2 junto a hide 1/2 de escena 23.
- [TRIGGER_3] **00:30–00:51:** Construir bat: gigante→0; ausencia→saturación min(2,3)=2, h 1, g 0→2/3. Ponderar y obtener 1/3.
- [TRIGGER_4] **00:51–01:07:** Reunir las tres tarjetas, encerrar ambas máximas y elegir una sin proclamar superioridad única. Mostrar que la política tiene acciones posteriores dependientes del estado.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_MINT para empate óptimo; ACCENT_CYAN para probabilidades; ACCENT_TERRACOTTA para hambre; ACCENT_INDIGO para futuro; ACCENT_VINO para gigante mortal.

---

## Escena: 25

## Nombre: El falso poder de mirar antes de elegir

## Descripcion Breve: Una política que conoce el suceso actual logra un valor imposible para el jugador real.

## Objetivo Pedagogico: Demostrar con números por qué no se intercambian máximo y esperanza.

## Voz en off:

> "[TRIGGER_1] Esta misma partida nos permite detectar una trampa. Imagina que alguien decide buscar comida cuando sabe que el gigante no aparecerá, y esconderse cuando sabe que sí aparecerá. [TRIGGER_2] En la mitad de los casos sin gigante, comería y después se escondería: esa rama vale uno. En la mitad con gigante, se escondería y afrontaría una última hora que vale un tercio. [TRIGGER_3] Esa cuenta da un medio más un sexto: dos tercios. Parece mejor que nuestro un medio, pero utilizó información prohibida. Eligió la acción después de conocer la aparición de la misma hora. [TRIGGER_4] Nuestro algoritmo no puede hacer eso. Primero compara los valores completos de las acciones y elige. Sólo después observa lo que ocurre. Un resultado demasiado bueno también puede revelar que resolvimos un problema diferente."

## Descripcion Visual Detallada:

Duración orientativa: 01:01. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Diagrama incorrecto azar de hora 1→selector de acción con etiquetasfood si no G, hide si G.
- MathTex(r"V_{\rm anticipado}=\tfrac12\cdot1+\tfrac12\cdot\tfrac13=\tfrac23>\tfrac12"); sello Tex(r"\text{Información no disponible}").

## Layout y disposicion:

- Diagrama incorrecto a LEFT*2.8, cronología correcta a RIGHT*3.0, ambos dentro de ancho 5.4.
- Cálculo en y=-1.6 y prohibición en y=-2.6. Rótulo permanente contrafactual para no presentar 2/3 como respuesta real.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Dibujar orden invertido observar→elegir y mantener desde el principio una etiqueta contrafactual.
- [TRIGGER_2] **00:14–00:30:** Asignar las dos continuaciones 1 y 1/3 a sus ramas; indicar que la primera decisión se apoya en un suceso aún no observado por el jugador real.
- [TRIGGER_3] **00:30–00:45:** Calcular 1/2+1/6=2/3 y compararlo con 1/2; colocar Cross en la flecha que lleva información desde resultado actual hacia decisión actual.
- [TRIGGER_4] **00:45–01:01:** Recuperar orden correcto elegir→azar→nueva decisión. Mantener 1/2 como valor del problema y retirar contrafactual, sin dejar dos respuestas ambiguas.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_VINO para anticipación ilegal; ACCENT_CYAN para cálculo de probabilidades; ACCENT_INDIGO para cronología correcta; ACCENT_MINT para valor válido.

---

## Escena: 26

## Nombre: Una hora, tres condiciones de supervivencia

## Descripcion Breve: El ejemplo de resultado1/8 combina gigante, fotosensible y veneno.

## Objetivo Pedagogico: Comprobar una transición alimenticia con riesgos simultáneos y H=1.

## Voz en off:

> "[TRIGGER_1] Probemos ahora una sola hora. H vale uno, así que necesitamos comer. Tenemos una batería, capacidad para doce, alimento seguro de encontrar y probabilidad un medio de que esté envenenado. El fotosensible también aparece con probabilidad un medio. [TRIGGER_2] Esconderse o buscar batería termina en hambre fatal. Sólo buscar comida puede servir. Primero necesitamos que no aparezca el gigante: al comienzo esa probabilidad es un medio. [TRIGGER_3] Además, no debe aparecer el fotosensible. Tenemos sólo una batería y no podemos defendernos. Esa ausencia aporta otro factor un medio. Finalmente, la comida encontrada no debe ser venenosa: otro un medio. [TRIGGER_4] Multiplicamos los tres factores, bajo el modelo de independencia correspondiente: un octavo, doce punto cinco por ciento. Llegar a la última hora no nos permite saltarnos ni la defensa ni el control del hambre."

## Descripcion Visual Detallada:

Duración orientativa: 01:02. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- MathTex(r"N=H=1,K=12,S=1,b_1=c_1=1,v_1=q_1=1/2").
- Árbol con tres filtros: no gigante 1/2, no fotosensible 1/2, no veneno 1/2; cada alternativa mortal termina en 0. MathTex(r"F(1,1,0,0)=(1/2)^3=1/8=0.125").

## Layout y disposicion:

- Parámetros arriba y=2.0 en dos líneas. Filtros en x=-4,0,4, y=0.8; salidas mortales hacia y=-0.7.
- Producto en y=-1.8; hide y bat con valor 0 en pequeñas tarjetas y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Escribir todos los parámetros y mostrar h 0 con umbral H1; una única batería visible.
- [TRIGGER_2] **00:18–00:31:** Eliminar hide y bat por hambre; abrir food y conservar únicamente ausencia del gigante con peso 1/2, dejando rama mortal visible.
- [TRIGGER_3] **00:31–00:46:** Añadir fotosensible y veneno como dos filtros sucesivos del cálculo, con ramas de muerte explícitas. Reafirmar que orden del árbol no es una cronología inventada.
- [TRIGGER_4] **00:46–01:02:** Multiplicar 1/2·1/2·1/2, convertir a 1/8 y 0.125. Mostrar que c=1 añade factor 1 y no un riesgo omitido.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_CYAN para factores; ACCENT_VINO para filtros mortales; ACCENT_TERRACOTTA para H=1 y reserva 1; ACCENT_MINT para 1/8.

---

## Escena: 27

## Nombre: Las reglas vistas desde sus extremos

## Descripcion Breve: Casos deterministas verifican hambre, batería, veneno y fronteras de probabilidad.

## Objetivo Pedagogico: Cerrar casos borde sin extrapolar una sola estrategia a todas las instancias.

## Voz en off:

> "[TRIGGER_1] Si el número de horas es menor que H, esconderse siempre garantiza escapar: nunca alcanzamos el límite de hambre. Pero si N es igual a H y jamás podemos encontrar comida, la supervivencia es cero. [TRIGGER_2] Si la bolsa sólo admite una batería, la lámpara nunca puede usarse. Cada aparición del fotosensible fuera es mortal. Eso no obliga a que toda la partida tenga probabilidad cero: todavía puede no aparecer, o podemos escondernos cuando convenga. [TRIGGER_3] Si el veneno es seguro, encontrar comida mata. No encontrarla puede permitir seguir vivo si aún queda margen de hambre. El algoritmo conserva esa diferencia, aunque buscar comida suene, intuitivamente, como una acción destinada a ayudar. [TRIGGER_4] Las probabilidades conocidas pueden valer cero o uno. No necesitamos logaritmos ni dividir entre ellas. Y la probabilidad predictiva del gigante siempre queda entre cero y uno en un estado válido: g está entre cero e i menos uno."

## Descripcion Visual Detallada:

Duración orientativa: 01:09. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Cuatro tarjetas de casos: MathTex(r"N<H\Rightarrow1"),MathTex(r"N=H,\ c_i=0\ \forall i\Rightarrow0"),MathTex(r"K=1\Rightarrow\text{sin defensa}"),MathTex(r"v_i=1\Rightarrow\text{hallazgo letal}").
- MathTex(r"0\le g\le i-1\Rightarrow0<(g+1)/(i+1)<1"); celdas de probabilidad 0 y 1 como valores legales.

## Layout y disposicion:

- Tarjetas en una cuadrícula 2×2 con centros (-3,1.0,0),(3,1.0,0),(-3,-0.8,0),(3,-0.8,0), cada una ancho 5.5.
- Cota de α en y=-2.6; mantener condiciones completas en cada tarjeta, no sólo las conclusiones 1 y 0.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Animar calendario N<Hsin llegar a H y luego caso N=Hcon todos c_i=0, alcanzando H; no suponer comida imposible sólo por elegir esconderse.
- [TRIGGER_2] **00:16–00:34:** Mostrar capacidad K=1 bloqueando segunda batería y una rama 1-q que todavía permite vivir fuera. Evitar colorear todo el estado como muerte segura.
- [TRIGGER_3] **00:34–00:51:** Separar v=1 con hallazgo→0 y no hallazgo→D(h+1); si h+1<H, mostrar futuro posible; en caso contrario, 0.
- [TRIGGER_4] **00:51–01:09:** Insertar probabilidades 0 y 1 en árboles sin división; verificar numerador de α entre 1 e i, y denominador i+1. Ningún estado utiliza g>i-1.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_MINT para supervivencia garantizada bajo su condición; ACCENT_VINO para muerte; ACCENT_TERRACOTTA para límites; ACCENT_CYAN para probabilidades extremas legales.

---

## Escena: 28

## Nombre: Por qué la mejor continuación produce la mejor política

## Descripcion Breve: La inducción hacia atrás demuestra la ecuación de Bellman.

## Objetivo Pedagogico: Justificar optimalidad, suficiencia de estado y que aleatorizar acciones no mejora el máximo.

## Voz en off:

> "[TRIGGER_1] Ya vimos la mecánica. Ahora la garantía. Al final del calendario sabemos exactamente qué vale cada resultado: uno si terminamos vivos, cero si morimos. Ésas son nuestras bases. [TRIGGER_2] Supongamos que conocemos las mejores probabilidades para todos los estados de la hora siguiente. Para una acción actual, sus ramas son excluyentes y cubren todos los resultados. Sumarlas con sus pesos da el mejor valor posible de esa acción. [TRIGGER_3] Comparar las tres acciones da el mejor valor actual. Y podemos alcanzarlo: elegimos una acción máxima y, al observar la rama real, seguimos la mejor política de su estado siguiente. Repitiendo el argumento hacia atrás llegamos al inicio. [TRIGGER_4] No ganamos nada sorteando entre acciones: una mezcla es un promedio de sus valores y no supera al mayor. Todo descansa en que los cuatro números del estado contienen la información relevante; por eso reutilizar un futuro no pierde ninguna oportunidad."

## Descripcion Visual Detallada:

Duración orientativa: 01:09. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Dos capas de nodos, i e i+1, con valores MathTex de F; terminales MathTex de 0 y 1; Circle para azar y Rectangle para decisión.
- MathTex(r"\sum_o P(o\mid a,\mathrm{estado})F(\mathrm{siguiente}(o))"),MathTex(r"F=\max_a A_a"),MathTex(r"\sum_a\lambda_a A_a\le\max_a A_a,\quad\lambda_a\ge0,\ \sum_a\lambda_a=1").

## Layout y disposicion:

- Terminales en (4.7,0.5,0), capa i+1 en (1.5,0.5,0) y capa i en (-2.4,0.5,0). Las flechas causales apuntan a la derecha; el halo que indica el orden de cálculo avanza a la izquierda.
- Ecuaciones centradas en y=-1.5 y y=-2.5, por fases, sin superponerse con los nodos.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** FadeIn de los terminales 0 y 1. Mover una ficha con hambre H hacia el terminal 0; la compuerta impide que entre al terminal de éxito.
- [TRIGGER_2] **00:14–00:32:** Create de una raíz de azar y sus sucesores. Write de los pesos y valores óptimos conocidos; TransformMatchingTex para sumar sus productos, incluyendo explícitamente las contribuciones mortales.
- [TRIGGER_3] **00:32–00:50:** Write del máximo en la capa i. Indicate de una acción que lo alcanza y de sus continuaciones óptimas. Mover el halo de cálculo hacia la izquierda; el personaje no retrocede en el tiempo.
- [TRIGGER_4] **00:50–01:09:** Crear una barra dividida en proporciones λ, con cada segmento rotulado mediante MathTex. TransformMatchingTex hacia la combinación convexa y su cota. Indicate de la tarjeta del estado suficiente que fundamenta la prueba.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para decisiones óptimas; ACCENT_CYAN para ley de probabilidad total; ACCENT_MINT para valores certificados; ACCENT_TERRACOTTA para dirección de cálculo.

---

## Escena: 29

## Nombre: Contar estados, no historias

## Descripcion Breve: La dimensión de apariciones genera un número triangular de pares(i,g).

## Objetivo Pedagogico: Derivar O(N²KH) y cuantificar el dominio máximo sin confundirlo con historias alcanzables.

## Voz en off:

> "[TRIGGER_1] ¿Cuánto trabajo queda después de fusionar historias? En la hora i, el contador g puede tomar i valores: desde cero hasta i menos uno. Las baterías tienen K más uno posibilidades y el hambre tiene H. [TRIGGER_2] Por tanto, esa hora tiene i, multiplicado por K más uno, multiplicado por H estados potenciales. Sumando las horas aparecen uno más dos más tres, hasta N: un número triangular. [TRIGGER_3] El total es N por N más uno, dividido entre dos, por K más uno y por H. Cada estado examina tres acciones y un número fijo de ramas. El tiempo queda en orden de N al cuadrado por K por H. [TRIGGER_4] Con quinientas horas y límites doce de batería y hambre son diecinueve millones quinientos treinta y nueve mil estados potenciales vivos. La información sobre el gigante cuesta una dimensión adicional, pero ya no almacenamos un árbol exponencial de historias."

## Descripcion Visual Detallada:

Duración orientativa: 01:09. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Cuadrícula triangular de pares (i, g): cinco filas de 1, 2, 3, 4 y 5 Square, con rótulos MathTex de i y g y una llave que indica extensión hasta N. Cada celda representa (K+1)H estados físicos.
- MathTex(r"\sum_{i=1}^Ni(K+1)H=\frac{N(N+1)}2(K+1)H\Rightarrow O(N^2KH)"); MathTex(r"125250\cdot13\cdot12=19\,539\,000").

## Layout y disposicion:

- Triángulo centrado en LEFT*3.0; filas en y=1.5,0.8,0.1,-0.6,-1.3. El eje g sólo enumera valores válidos.
- Panel de baterías por hambre centrado en (3.2,0.8,0). Fórmulas centradas en y=-2.2 y y=-3.0; mostrar por fases si el ancho exige partir una igualdad.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Create de las cinco filas, una tras otra, con longitudes de 1 a 5. Write de los rangos 0≤g≤i−1; el punto g=i queda fuera de cada fila.
- [TRIGGER_2] **00:17–00:31:** ReplacementTransform de una celda ampliada a una rejilla con índices s=0,…, K y h=0,…, H−1. Write del rótulo de estados potenciales: algunos pueden no alcanzarse desde una instancia inicial concreta.
- [TRIGGER_3] **00:31–00:51:** Crear una copia girada del triángulo y juntarla con el original para formar un rectángulo de N por N+1 celdas. TransformMatchingTex para dividir entre dos y multiplicar por (K+1)H. Indicate del número constante de ramas por estado.
- [TRIGGER_4] **00:51–01:09:** Sustituir N=500, K=12, H=12 mediante TransformMatchingTex y evaluar 125250×156=19539000. Mantener el rótulo de estados potenciales; la cifra no cuenta historias ni asegura que la recursión visite todos los estados.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para estados; ACCENT_TERRACOTTA para i yg; ACCENT_CYAN para ejes físicos; ACCENT_MINT para reducción del árbol.

---

## Escena: 30

## Nombre: Dos páginas de memoria

## Descripcion Breve: El cálculo hacia atrás permite guardar sólo la hora actual y la siguiente.

## Objetivo Pedagogico: Explicar compresión espacial, diferencia con el código original y precisión numérica.

## Voz en off:

> "[TRIGGER_1] La tabla completa guardaría valores de todas las horas. Pero cada transición sólo consulta la hora siguiente. Para calcular hacia atrás bastan dos páginas: la que estamos llenando y la que ya conocemos. [TRIGGER_2] Primero llenamos la página del final con unos para los estados vivos. Calculamos la hora N, intercambiamos las páginas y seguimos con N menos uno. Al reutilizarlas, la memoria baja a orden de N por K por H. [TRIGGER_3] El código original guarda tablas completas y ocupa alrededor de cuatrocientos veintinueve mebibytes en sus dos grandes arreglos. La versión de dos páginas necesita alrededor de uno punto diecinueve mebibytes para los valores, con los límites máximos. Esta versión calcula el valor óptimo inicial; no conserva la tabla completa de decisiones para consultar después toda la política. [TRIGGER_4] Las probabilidades se almacenan con precisión doble. La fórmula del aprendizaje se calcula directamente; no aproximamos p mediante una cuadrícula. La tolerancia absoluta es una milmillonésima: no necesitamos precisión arbitraria para representar respuestas muchísimo menores que ese umbral."

## Descripcion Visual Detallada:

Duración orientativa: 01:18. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Dos paneles con etiquetas MathTex(r"F_{i+1}") y MathTex(r"F_i"). Cada panel es un VGroup de mosaicos para g, con ejes s y h; no usar perspectiva que oculte celdas.
- MathTex(r"O(N^2KH)\longrightarrow O(NKH)"), MathTex(r"2(N+1)(K+1)H\cdot8\ \mathrm{bytes}\approx1.19\ \mathrm{MiB}"). Tarjeta separada con MathTex(r"449\,864\,100\ \mathrm{bytes}\approx429\ \mathrm{MiB}") para las dos tablas del código original; Tex para su leyenda.
- Tex para precisión doble y política no almacenada; MathTex(r"10^{-9}") para tolerancia y MathTex(r"0\le F\le1") para el rango de valores.

## Layout y disposicion:

- Página siguiente centrada en (3.1,0.4,0) y actual en (-3.1,0.4,0); ancho 5.3 y alto 3.1 cada una. Canal de lectura en x=0.
- Memoria en y=-2.1 y precisión en y=-3.0. La comparación de tamaños sustituye las matrices durante su lectura: no amontonar ambas composiciones.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** FadeIn de una pila de capas y Create de flechas que sólo unen i con i+1. Atenuar las capas que no intervienen y conservar dos paneles.
- [TRIGGER_2] **00:16–00:34:** Write de unos en los estados vivos de la capa N+1. Completar la capa N mediante lecturas desde la derecha; Swap de los paneles y actualización de rótulos para N−1. Indicate del filtro de hambre de D_i, que sigue convirtiendo estados inválidos en cero.
- [TRIGGER_3] **00:34–01:00:** TransformMatchingTex entre las expresiones de espacio y Write de ambas cifras con sus etiquetas de implementación. La reserva original tiene 49 984 900 doubles de 8 bytes y otros tantos bools de 1 byte; las dos capas usan 1 250 496 bytes. Mostrar que se conserva el valor, sin almacenar toda la política. La recursión original añade una pila O(N), que no forma parte de esos 429 MiB.
- [TRIGGER_4] **01:00–01:18:** Write de precisión doble y tolerancia 10⁻⁹. Atenuar una rejilla hipotética de valores de p para indicar que no se utiliza. Indicate de la fórmula cerrada de α: la recurrencia es exacta en el modelo, aunque la aritmética de almacenamiento sea finita.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para páginas; ACCENT_CYAN para lecturas; ACCENT_TERRACOTTA para intercambio; ACCENT_MINT para ahorro; TEXT_MUTED para capas descartadas.

---

## Escena: 31

## Nombre: Una máquina de decisiones, sin código en pantalla

## Descripcion Breve: El algoritmo completo se muestra como flujo entre calendario, estados, ramas y máximos.

## Objetivo Pedagogico: Conectar la implementación con el modelo y fijar la salida F(1,S,0,0).

## Voz en off:

> "[TRIGGER_1] Podemos describir toda la implementación como una máquina de decisiones. Carga las probabilidades de cada hora. Recorre el calendario hacia atrás y considera los estados válidos de esa hora. [TRIGGER_2] Para cada combinación de baterías, hambre y apariciones, calcula alfa. Construye los valores de esconderse, batería y comida usando la página siguiente, conserva el mayor y pasa a la siguiente casilla. [TRIGGER_3] Las comprobaciones son siempre las mismas: defensa con las baterías iniciales, hambre inválida hacia cero, reserva limitada por K. Una probabilidad óptima igual a cero es un resultado legítimo, no una casilla que debamos confundir con todavía no calculada. [TRIGGER_4] Cuando terminamos, leemos la primera hora con S baterías, hambre cero y ninguna aparición observada. Ésa es la respuesta solicitada: la mayor probabilidad de escapar, no una promesa de que una partida concreta saldrá bien."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Ocho tarjetas Rectangle con rótulos Tex: parámetros, base terminal, hora, estado válido, predicción, valores de acción, máximo y almacenamiento. Flechas Arrow y fichas móviles para el calendario y los registros MathTex de i, s, h, g.
- MathTex(r"\alpha=(g+1)/(i+1)"), MathTex(r"F(1,S,0,0)"). Dos celdas visualmente distintas: valor calculado 0 y casilla sin calcular; esta última usa contorno discontinuo y un rótulo Tex, no un cero.
- Tres sellos MathTex(r"s\ge2"), MathTex(r"h<H"), MathTex(r"\min(K,s^{\prime})") junto al lector D_i; barra NumberLine de 0 a 1.

## Layout y disposicion:

- Flujo en dos filas: centros x=-4.5,-1.5,1.5,4.5 con y=1.4 arriba; abajo, el orden se invierte con y=-0.3. Cada tarjeta mide 2.4 por 0.9; flechas por los espacios entre tarjetas.
- La salida F(1, S,0,0) aparece en (0,-2.3,0). Los sellos sustituyen temporalmente el flujo durante su explicación y rodean a D_i; no se colocan encima de ocho tarjetas ya visibles.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** FadeIn de las primeras cuatro etapas. Mover la ficha del calendario desde N hacia 1 para mostrar orden de cálculo, sin mover al personaje hacia el pasado.
- [TRIGGER_2] **00:14–00:29:** Crear las cuatro etapas restantes. Transform de los registros del estado; mover copias de α y de las lecturas de sucesores hacia los tres árboles, contraerlos en sus valores y enviar el máximo a una celda.
- [TRIGGER_3] **00:29–00:47:** Indicate de los tres sellos del lector. Comparar una celda con valor 0 y una sin calcular: el código original usa una marca separada de memoización; la versión iterativa conoce las dependencias por su orden de cálculo. El valor cero sigue siendo un resultado legítimo.
- [TRIGGER_4] **00:47–01:03:** Write de F(1, S,0,0) y mover una flecha de lectura a esa celda exacta. Crear una barra de probabilidad y, al lado, una sola trayectoria de juego; sus leyendas diferencian probabilidad óptima y resultado individual.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para memoria y decisión; ACCENT_CYAN para lecturas; ACCENT_TERRACOTTA para calendario; ACCENT_MINT para resultado; TEXT_MUTED para casilla sin calcular.

---

## Escena: 32

## Nombre: Sobrevivir también cambia lo que sabes

## Descripcion Breve: La puerta inicial reaparece junto al estado físico y el conocimiento aprendido.

## Objetivo Pedagogico: Cerrar con los dos descubrimientos: suficiencia bayesiana y decisiones por futuros compartidos.

## Voz en off:

> "[TRIGGER_1] Volvemos a la puerta. Las reglas no se hicieron menos peligrosas. Lo que cambió fue nuestra forma de pensar: dejar de tratar cada hora como una moneda nueva y escuchar lo que las anteriores nos enseñaron. [TRIGGER_2] El peligro desconocido se convirtió en una fracción que podemos actualizar con un conteo. Y el bosque de historias se convirtió en estados que comparten el mismo futuro cuando coinciden los recursos y la información. [TRIGGER_3] En cada estado, no adivinamos un desenlace. Sumamos todos los que no controlamos y elegimos entre las acciones que sí controlamos. Aprender del azar y decidir antes del siguiente suceso son partes de la misma estrategia. [TRIGGER_4] La pregunta inicial era cómo sobrevivir sin conocer el peligro. La respuesta empieza con otra: ¿qué necesito recordar para tomar la próxima decisión? [Pausa.] En Door 1, cuatro números bastan para aprovechar todo lo que sabemos."

## Descripcion Visual Detallada:

Duración orientativa: 01:08. Los intervalos siguientes se miden desde el inicio de esta escena.

## Objetos:

- Puerta y avatar de la apertura; cuatro fichas MathTex(r"i"), MathTex(r"s"), MathTex(r"h"), MathTex(r"g"); curva posterior y MathTex(r"(g+1)/(i+1)").
- Árbol de historias que se transforma en un grafo acíclico de estados. Tex(r"Recordar lo necesario para decidir mejor") y Tex(r"Door 1 --- Gran Premio de México 2026, primera fecha").

## Layout y disposicion:

- Puerta centrada en (-4.5,0,0), estado en (2.5,0,0) y título en (0,3.25,0).
- Frase final centrada en ORIGIN después de retirar los diagramas; cuatro fichas debajo en y=-1.2. Crédito en (0,-3.2,0), ancho máximo 11.8.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** FadeIn de la puerta y el avatar. Indicate de una sola moneda oculta que permanece fija mientras cambia la curva de creencias.
- [TRIGGER_2] **00:17–00:33:** ReplacementTransform de la curva en la fracción predictiva y del árbol en estados fusionados. Conservar por un instante las correspondencias de colores de los dos descubrimientos.
- [TRIGGER_3] **00:33–00:50:** Indicate de los círculos de azar al sumar y de los cuadrados de decisión al maximizar. Animar una flecha hacia la observación siguiente, respetando el orden de información.
- [TRIGGER_4] **00:50–01:08:** FadeOut de los diagramas y Write de la frase final con las cuatro fichas. Mantener dos segundos después de la pausa; FadeOut hacia BG_COLOR y aparición breve del crédito dentro de este mismo disparador.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto y ecuaciones `TEXT_MAIN`; contenido secundario `TEXT_MUTED`. ACCENT_INDIGO para estado y puerta; ACCENT_CYAN para aprendizaje; ACCENT_MINT para estrategia; ACCENT_TERRACOTTA para recursos; TEXT_MAIN para cierre.

---
