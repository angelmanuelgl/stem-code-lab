# Guion Storyboard / Técnico: Huron Designs

**Fuente y alcance.** Basado en `guion_sol.md` de la carpeta `HuronDesigns`. La narración desarrolla el problema de diseños, Gym 105873, primera fecha del Gran Premio de México 2025. Las referencias al código del usuario corresponden a `H.HuronDesing.cpp`, según el análisis fuente. Se especifican guiones y animaciones; todavía no se implementan ni renderizan escenas de Manim.

**Lienzo y legibilidad.** Formato 16:9, ancho 128/9 y alto 8 unidades de Manim. Fondo `BG_COLOR`. Área útil x∈[−6.3,6.3], y∈[−3.5,3.5]. Todas las posiciones dadas son centros con z=0; `LEFT*3` equivale a (−3,0,0). Título habitual en (0,3.25,0). Tamaños orientativos: título 36, texto 28, fórmulas 30 puntos. Partir una igualdad en líneas alineadas antes de reducirla por debajo de 24 puntos. Al ampliar tablas, retirar temporalmente las otras fórmulas: la legibilidad tiene prioridad sobre mostrar todos los objetos simultáneamente.

**Tipografía obligatoria.** Todo contenido visible —títulos, cifras, leyendas, estados, nombres de funciones, índices, créditos y etiquetas de ejes— utiliza `Tex` o `MathTex`, con soporte LaTeX de español y acentos. Los objetos descritos como tarjetas o registros contienen esos rótulos, no objetos `Text`, `Code` ni `DecimalNumber`. Los ejes se crean sin numeración automática y reciben etiquetas `MathTex`. Las fórmulas mencionadas en prosa se transcriben en LaTeX: α como `\alpha`, ≤ como `\le`, conjuntos con llaves escapadas y máscaras con subíndice 2. Los nombres de funciones son etiquetas textuales cortas en `Tex`; no se muestran bloques de código fuente.

**Geometría y gramática visual.** `Rectangle`, `Square`, `Circle`, `Dot`, `Line`, `Arrow`, `Brace`, `Cross`, `Underline`, `Axes`, `NumberLine` y `VGroup` bastan para construir las escenas. La longitud de cada bloque temporal es proporcional a su duración dentro de una misma agenda. Toda ruptura de escala se señala expresamente. Un segmento de umbrales representa posibles valores de Y, no horas de trabajo consumidas. Una densidad continua no asigna masa a un punto; el umbral degenerado se representa como masa puntual con etiqueta 1. Una casilla de DP es un conjunto, no un orden: el orden se visualiza en las agendas que proponen valores a esa casilla.

**Estados y símbolos.** `DP[S]` designa siempre la versión estricta: realizar exactamente S con una agenda factible. Su inviabilidad se escribe `-\infty`, separada del cero factible. `A[M]` designa siempre el arreglo original inicializado en cero; no se intercambian los nombres. Los trabajos del ejemplo oficial son A y B, con subíndices cuando corresponda; el arreglo original A sólo se introduce después de ese ejemplo y siempre se escribe con corchetes. Para el contraejemplo de inviabilidad se usan U y V. Los bits se muestran de mayor a menor índice; para A,B,C la fila es C,B,A, y para dos trabajos A,B es B,A. El tiempo de un conjunto es T[S]; la recompensa de terminar i en t es w_i(t). La fecha obligatoria d y el umbral de bono Y siempre tienen etiquetas diferentes.

**Continuidad probabilística.** La factorización del bono usa independencia entre X e Y, como en la interpretación de la solución fuente. La suma de esperanzas no necesita independencia entre trabajos distintos. Las decisiones comparan ganancias esperadas de agendas; el storyboard no introduce aprendizaje, observación anticipada de sorteos ni políticas adaptativas ajenas al modelo. La curva w es no creciente en su dominio, mientras d limita qué entregas son admisibles: no se dibuja una tarea tardía como una alternativa válida de beneficio cero.

**Sincronización.** Cada escena contiene cuatro disparadores locales `[TRIGGER_1]` a `[TRIGGER_4]`. Su identificador completo es el par (escena, disparador); se reinician en la siguiente escena. La locución se copia literalmente de `guion_voz.md`. Los tiempos son orientativos, estimados a 140 palabras por minuto con margen de lectura y pausas; se ajustarán a la grabación, no representan una pista de audio ya medida. Todas las acciones de una viñeta pertenecen a ese disparador y siguen el orden de sus frases en la voz. Mantener la composición durante una pausa. La retirada de elementos y la preparación del siguiente panel ocurren dentro del disparador que las describe; no añadir transiciones narrativas sin marca.

**Operaciones.** «Escribir» o revelar texto se ejecuta con `Write`; crear geometría con `Create` o `FadeIn`; actualizar ecuaciones con `TransformMatchingTex`; reemplazar diagramas con `ReplacementTransform`; mover fichas con `.animate.move_to`; destacar con `Indicate`; retirar con `FadeOut`. `Cross` sólo invalida la alternativa indicada, no borra una condición válida. Operaciones típicas de 0.6–1.2 segundos, seguidas de tiempo de lectura dentro del intervalo. Las secuencias indican los objetos concretos y el orden de cada transformación. Ningún árbol esquemático sustituye los cálculos exhaustivos de los ejemplos pequeños.

**Paleta semántica de `styles.theme` / `theme.py`.** `BG_COLOR=#181C24`; `TEXT_MAIN=#ECEFF4`; `TEXT_MUTED=#64748B`; `ACCENT_INDIGO=#6366F1` para agendas, máscaras y DP; `ACCENT_CYAN=#38BDF8` para incertidumbre y propuestas; `ACCENT_MINT=#2DD4BF` para ganancias y certificados válidos; `ACCENT_TERRACOTTA=#D97706` para tiempo y límites; `ACCENT_VINO=#C0392B` para inviabilidad o hipótesis rechazadas. Usar `ACCENT_VINO` para peligro o error: no se presupone un símbolo `COLOR_DANGER`. El color siempre se acompaña de etiquetas, contornos o símbolos. Los colores particulares de los trabajos se mantienen al cambiar de orden; un trabajo rechazado conserva su identidad y recibe una Cross adicional.


## Escena: 01

## Nombre: Una agenda que pierde dinero mientras espera

## Descripcion Breve: Los encargos compiten por el tiempo de una sola persona.

## Objetivo Pedagogico: Plantear el misterio: aceptar más trabajo puede producir menos ganancia.

## Voz en off:

> "[TRIGGER_1] Te ofrecen dos encargos. Los dos pagan, los dos parecen convenientes y, con el orden adecuado, puedes entregar ambos a tiempo. ¿Aceptarías los dos? [Pausa.] En este problema, esa decisión puede hacerte ganar menos que aceptar uno solo. [TRIGGER_2] La razón está en las bonificaciones. El reloj no sólo decide si una entrega es válida: también cambia cuánto dinero esperamos recibir. Y ni siquiera conocemos de antemano el importe exacto del bono ni su fecha límite. [TRIGGER_3] Tony tiene que elegir qué diseños aceptar y en qué orden realizarlos. Huron Designs, de la primera fecha del Gran Premio de México de dos mil veinticinco, convierte esa agenda en un problema de decisiones bajo incertidumbre. [TRIGGER_4] Vamos a construir la solución desde dos preguntas: ¿cómo ponemos un precio al azar? Y, cuando el orden parece multiplicar las posibilidades sin límite, ¿qué podemos olvidar sin perder la mejor respuesta?"

## Descripcion Visual Detallada:

Duración orientativa: 01:08. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Puerta de estudio hecha con Rectangle; avatar Dot; dos tarjetas de encargos con Tex; reloj circular con Line como aguja. MathTex(r"\text{¿Más trabajos}\Rightarrow\text{más ganancia?}"). Dos medidores sin cifras, uno de tiempo y otro de recompensa esperada.

## Layout y disposicion:

- Título en (0,3.25,0); agenda en (-3,0.5,0), ancho 5; tarjetas en (2.9,1,0) y (2.9,-0.4,0), ancho 4.8. Pregunta en (0,-2.4,0).

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:19:** FadeIn de las dos tarjetas y Create de una línea de tiempo. Escribir la pregunta y mantenerla durante la pausa; no mostrar aún la respuesta numérica.
- [TRIGGER_2] **00:19–00:36:** Mover la aguja del reloj y reducir la altura de un medidor de bono. Revelar signos de interrogación MathTex sobre importe y umbral.
- [TRIGGER_3] **00:36–00:53:** Write del nombre del problema y procedencia. Colocar las tarjetas en una agenda de una sola fila para representar un único trabajador.
- [TRIGGER_4] **00:53–01:08:** Separar dos paneles Tex: valorar el azar y organizar el trabajo. Encender el primero; mantener el segundo atenuado como pregunta pendiente.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para agenda; ACCENT_TERRACOTTA para tiempo; ACCENT_MINT para recompensa; ACCENT_CYAN para incertidumbre.

---

## Escena: 02

## Nombre: Dos fechas que no significan lo mismo

## Descripcion Breve: Cada encargo tiene duración, fecha obligatoria, base y bono aleatorio.

## Objetivo Pedagogico: Definir el modelo y separar factibilidad de recompensa.

## Voz en off:

> "[TRIGGER_1] Cada trabajo i tarda c unidades de tiempo. Si lo aceptamos, debemos terminarlo antes o exactamente en su fecha obligatoria d. A cambio recibimos una base p. No podemos realizar dos trabajos a la vez. [TRIGGER_2] Además hay un importe de bono X, uniforme entre sus dos extremos. Y un umbral Y, también uniforme en su intervalo. Recibimos X sólo cuando nuestra finalización t es menor o igual que Y. [TRIGGER_3] Atención a las dos fechas: superar Y puede quitarnos el bono; superar d hace que ese trabajo no sea una entrega válida. No se arregla una entrega tardía cobrando solamente la base. [TRIGGER_4] Podemos descartar encargos. Para una secuencia sin pausas, cada finalización es la suma de las duraciones que la preceden, incluida la propia. Buscamos la secuencia cuya suma de recompensas tenga la mayor esperanza."

## Descripcion Visual Detallada:

Duración orientativa: 01:03. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Ficha con MathTex(r"c_i,d_i,p_i"), MathTex(r"X_i\sim U[lx_i,rx_i]"), MathTex(r"Y_i\sim U[ly_i,ry_i]"). Línea temporal con marcador t y dos marcas distintas para Y y d. MathTex(r"p_i+X_i\mathbf1\{t\le Y_i\}"), MathTex(r"F_{\pi_j}=\sum_{r=1}^{j}c_{\pi_r}\le d_{\pi_j}").

## Layout y disposicion:

- Ficha izquierda centrada en (-3.2,0.4,0), ancho 5.5; línea temporal derecha de (0.4,0.4,0) a (5.9,0.4,0). Fórmula de recompensa en y=-1.6 y de finalización en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Write de duración, base y fecha obligatoria; colocar un bloque de longitud c en la agenda y un candado de entrega en d.
- [TRIGGER_2] **00:16–00:32:** Create de los dos intervalos aleatorios, con rótulos X e Y. Mostrar el indicador activándose cuando t≤Y, sin asignar todavía una realización concreta.
- [TRIGGER_3] **00:32–00:47:** Transform del diagrama en dos casos: Y<t≤d conserva base, t>d se marca con Cross. Usar una leyenda permanente para cada límite.
- [TRIGGER_4] **00:47–01:03:** Mover una tarjeta a una bandeja de rechazados; concatenar las aceptadas y construir sus sumas acumuladas con Brace. Write de la función objetivo como esperanza de la suma.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para X e Y; ACCENT_VINO para d violado; ACCENT_TERRACOTTA para c y t; ACCENT_MINT para base y bono.

---

## Escena: 03

## Nombre: La regla intuitiva que falla

## Descripcion Breve: Ordenar por fecha obligatoria puede destruir un bono temprano.

## Objetivo Pedagogico: Descartar un criterio voraz mediante un contraejemplo completo.

## Voz en off:

> "[TRIGGER_1] Quizá baste ordenar por la fecha obligatoria: primero lo que vence antes. Probemos dos trabajos, U y V. Ambos duran una unidad y pagan una de base. Sus fechas obligatorias son diez y once, respectivamente. [TRIGGER_2] U no ofrece bono. V ofrece cien adicionales si termina antes o exactamente en el instante uno. Su importe y su umbral son fijos: también caben como intervalos de un solo punto. [TRIGGER_3] Si hacemos U primero, termina en uno y cobra uno. V termina en dos: cumple su fecha once, pero pierde el bono. Ganamos dos. Si hacemos V primero, cobra ciento uno en el instante uno; U termina en dos y cobra uno. Total: ciento dos. [TRIGGER_4] Los dos órdenes cumplen las fechas obligatorias. La diferencia está en cuándo capturamos el valor de cada trabajo. Una regla que sólo mira d no ve esa diferencia; necesitamos comparar agendas que consideran también los bonos."

## Descripcion Visual Detallada:

Duración orientativa: 01:09. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos filas de bloques U,V y V,U; MathTex(r"c_U=c_V=1,\ p_U=p_V=1,\ d_U=10,\ d_V=11"); MathTex(r"X_U=0,\ X_V=100,\ Y_V=1"); sumas MathTex(r"1+1=2"), MathTex(r"101+1=102").

## Layout y disposicion:

- Parámetros en y=2.1 y y=1.5. Filas centradas en y=0.3 y y=-1.1; cada unidad ocupa 1.5 de Manim, origen x=-3.5. Resultados en x=3.8; conclusión en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Write de los datos y Create de las dos agendas vacías; marcar instantes 0,1,2 con MathTex.
- [TRIGGER_2] **00:16–00:31:** Revelar el bono fijo de V y su corte en 1. Dibujar el límite obligatorio lejos del final de ambos bloques, con una ruptura de escala explícita.
- [TRIGGER_3] **00:31–00:52:** Llenar U→V y calcular 1+1; después llenar V→U y calcular 101+1. Indicate del mismo instante de finalización de la agenda y de los bonos diferentes.
- [TRIGGER_4] **00:52–01:09:** Encerrar ambas etiquetas de factibilidad y contrastar las ganancias. Cross únicamente sobre la afirmación de que ordenar por d maximiza el dinero.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para U; ACCENT_CYAN para V; ACCENT_MINT para bono cobrado; ACCENT_TERRACOTTA para umbral temprano.

---

## Escena: 04

## Nombre: Separar el tamaño del premio de la posibilidad de cobrarlo

## Descripcion Breve: La independencia dentro del bono permite factorizar su esperanza.

## Objetivo Pedagogico: Derivar la ganancia esperada a una hora fija.

## Voz en off:

> "[TRIGGER_1] Fijemos una hora de finalización t. El bono es una cantidad aleatoria multiplicada por un interruptor: uno si llegamos a tiempo para cobrarlo, cero si no. Lo que buscamos es la media de ese producto. [TRIGGER_2] En el modelo que utiliza la solución, importe y umbral se sortean de manera independiente. Saber si el bono se activa no cambia la distribución de su importe. Por eso la media del producto es la media del importe por la probabilidad de activación. [TRIGGER_3] La media de un importe uniforme es el punto medio de su intervalo: extremo izquierdo más extremo derecho, dividido entre dos. Llamémosla mu. La probabilidad de activación será q de t. [TRIGGER_4] Entonces el trabajo vale, en promedio, p más mu por q de t. Todavía debemos exigir t menor o igual que d. Hemos separado la pregunta en dos: cuánto paga un bono que se activa y con qué probabilidad se activa."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"\mathbb E[X_i\mathbf1\{t\le Y_i\}]=\mathbb E[X_i]\Pr(Y_i\ge t)"); barra de importe [lx,rx] con punto medio; MathTex(r"\mu_i=(lx_i+rx_i)/2"), MathTex(r"w_i(t)=p_i+\mu_iq_i(t),\quad t\le d_i"). Interruptor geométrico con dos estados 0 y 1.

## Layout y disposicion:

- Importe a LEFT*3.1 e interruptor a RIGHT*3.1, ambos y=0.8; ecuación de independencia en y=-0.8, dividida en dos líneas si excede ancho 11.8. Ganancia en y=-2.4.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Create de barra e interruptor; Write del producto aleatorio antes de sustituirlo por su esperanza.
- [TRIGGER_2] **00:16–00:36:** Separar los dos factores con TransformMatchingTex y Write de una etiqueta Tex de independencia dentro del bono. No presentar la factorización como propiedad universal de productos.
- [TRIGGER_3] **00:36–00:51:** Mover dos copias de los extremos al punto medio y construir μ mediante TransformMatchingTex. Etiquetar el interruptor con q(t).
- [TRIGGER_4] **00:51–01:10:** Añadir la base p y cerrar la fórmula w. Colocar una compuerta t≤d antes del valor: fuera de ella la tarea es inviable, no una tarea de valor cero.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para probabilidad; ACCENT_MINT para importe; ACCENT_INDIGO para w; ACCENT_VINO para inviabilidad.

---

## Escena: 05

## Nombre: La probabilidad es la parte del intervalo que queda

## Descripcion Breve: Un segmento uniforme se recorta por la finalización t.

## Objetivo Pedagogico: Obtener las tres ramas de q(t) geométricamente.

## Voz en off:

> "[TRIGGER_1] Dibujemos todos los valores posibles de Y sobre una recta. Si t queda antes o exactamente en el extremo izquierdo, cualquiera de esos umbrales permite cobrar. La probabilidad es uno. [TRIGGER_2] Si t queda dentro del intervalo, sólo sirven los umbrales situados a su derecha. La parte favorable mide extremo derecho menos t; la longitud total mide extremo derecho menos extremo izquierdo. Dividimos esas longitudes. [TRIGGER_3] Cuando t supera el extremo derecho, no queda ningún umbral favorable y la probabilidad es cero. Para un intervalo de anchura positiva, la gráfica permanece en uno, baja en línea recta y después permanece en cero. [TRIGGER_4] Al multiplicar esa probabilidad por mu y añadir p, obtenemos la curva de recompensa esperada: una meseta alta, una rampa descendente y la base. Entregar más tarde nunca mejora esta curva. Esa observación será decisiva para organizar la agenda."

## Descripcion Visual Detallada:

Duración orientativa: 01:05. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- NumberLine de umbrales con etiquetas MathTex; segmentos [ly,ry] y [t,ry]; Brace para sus longitudes. MathTex(r"q_i(t)=\frac{ry_i-t}{ry_i-ly_i}\quad(ly_i<t<ry_i)"). Axes de q frente a t, con tramos q=1, recta descendente y q=0; segunda escala para w=p+μq.

## Layout y disposicion:

- Recta en y=1.5 con ly en x=-3 y ry en x=3; t se mueve de x=-4 a x=4. Gráfica en panel centrado (0,-0.6,0), ancho 9 y alto 2.3; fórmula en y=-2.7. El eje de tiempo del dibujo es esquemático y se rotula.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** Create del intervalo completo y mover t a la izquierda; colorear toda la longitud favorable y Write de q=1.
- [TRIGGER_2] **00:14–00:30:** Mover t al interior; recortar el segmento favorable con Transform y crear dos Brace. TransformMatchingTex de cociente de longitudes a la fórmula.
- [TRIGGER_3] **00:30–00:47:** Mover t más allá de ry y reducir el segmento favorable a vacío. Construir explícitamente los tres tramos de la gráfica, incluida la continuidad en los extremos para ly<ry.
- [TRIGGER_4] **00:47–01:05:** Transform de la escala vertical para pasar de q a w. Dibujar flechas horizontales de avance del tiempo y mostrar que ninguna aumenta la altura; no mezclar esta curva con la restricción d.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para segmento favorable y q; TEXT_MUTED para intervalo total; ACCENT_MINT para w; ACCENT_TERRACOTTA para t.

---

## Escena: 06

## Nombre: El extremo que cambia de significado

## Descripcion Breve: Una uniforme continua y un umbral fijo se comportan distinto en el extremo derecho.

## Objetivo Pedagogico: Resolver igualdad, degeneración y división por cero.

## Voz en off:

> "[TRIGGER_1] Hay una sutileza en la igualdad. Si el intervalo tiene anchura positiva y terminamos exactamente en su extremo derecho, sólo serviría ese punto. En una distribución continua, un punto aislado tiene probabilidad cero. El bono esperado es cero. [TRIGGER_2] Pero si los dos extremos coinciden en a, ya no tenemos un intervalo continuo de posibilidades: el umbral es exactamente a. Terminar en a sí cobra el bono con probabilidad uno. Terminar después no lo cobra. [TRIGGER_3] La receta debe comprobar primero si t es menor o igual que el extremo izquierdo. Después puede descartar los tiempos que llegan al extremo derecho o lo superan. Sólo en el interior de un intervalo realmente ancho necesitamos dividir. [TRIGGER_4] Así resolvemos el caso de anchura cero sin hacer una división imposible. Y no confundamos este extremo del bono con d: terminar exactamente en la fecha obligatoria siempre es válido, aunque el bono resulte cero."

## Descripcion Visual Detallada:

Duración orientativa: 01:09. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos paneles: intervalo continuo [1,8] con marcador t=8 y masa puntual Y=8 con t=8. MathTex(r"\Pr(Y\ge8)=0\quad\text{si }Y\sim U[1,8]"), MathTex(r"\Pr(Y\ge8)=1\quad\text{si }Y=8"). Diagrama de tres pruebas: t≤ly; t≥ry; cociente interior.

## Layout y disposicion:

- Paneles centrados en (-3.1,0.7,0) y (3.1,0.7,0), ancho 5.5. Comparación en y=-0.8; flujo de pruebas en y=-2.1 con nodos x=-4,0,4. Cada rama de flujo recibe etiqueta sí/no Tex.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Sombrear el intervalo [1,8] y reducir la región favorable al punto 8; Write de probabilidad cero. Mantener el punto visible sin darle área.
- [TRIGGER_2] **00:18–00:35:** En el otro panel, crear Dot en 8 y una etiqueta MathTex de masa 1. Indicate de t=8 y Write de probabilidad uno.
- [TRIGGER_3] **00:35–00:53:** Construir el flujo en el orden indicado. Recorrerlo con ly=ry=t=8: sale por la primera condición y nunca llega al denominador.
- [TRIGGER_4] **00:53–01:09:** Mostrar un segundo recorrido con t>8 y salida cero; después destacar una tarjeta independiente t=d, entrega válida. La compuerta de fecha obligatoria no cambia con estas probabilidades.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para continuo; ACCENT_INDIGO para masa puntual; ACCENT_MINT para igualdad válida; ACCENT_VINO para división inválida tachada.

---

## Escena: 07

## Nombre: Lo que promediamos y lo que no

## Descripcion Breve: La integral del indicador y la linealidad justifican la transformación determinista.

## Objetivo Pedagogico: Evitar reemplazar el umbral aleatorio por su media o imponer independencia innecesaria.

## Voz en off:

> "[TRIGGER_1] Esta geometría también es una integral. El indicador vale uno donde y es mayor o igual que t y cero en el resto. Integrarlo contra la densidad uniforme cuenta exactamente la longitud favorable dividida entre la longitud total. [TRIGGER_2] Si Y es uniforme entre seis y diez y terminamos en siete, quedan tres unidades favorables de cuatro: probabilidad tres cuartos. Sustituir Y por su media, ocho, diría que cobramos siempre. No es la misma pregunta. [TRIGGER_3] Para un bono medio de veinticinco, el valor esperado del bono es dieciocho punto setenta y cinco, no veinticinco. La independencia entre importe y umbral es la que permite multiplicar esos dos factores; conocer sólo sus distribuciones por separado no bastaría si estuvieran correlacionados. [TRIGGER_4] Finalmente sumamos las ganancias esperadas de los trabajos aceptados. La esperanza de una suma es la suma de las esperanzas, incluso sin independencia entre trabajos distintos. Ahora cada agenda tiene un valor determinista que podemos comparar, aunque su pago real siga siendo aleatorio."

## Descripcion Visual Detallada:

Duración orientativa: 01:15. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"\mathbb E[\mathbf1\{t\le Y\}]=\int\mathbf1\{t\le y\}\,dF_Y(y)"); MathTex(r"\int_7^{10}\frac{1}{10-6}\,dy=\frac34"); MathTex(r"25\cdot\frac34=18.75\ne25"); MathTex(r"\mathbb E[\sum_i R_i]=\sum_i\mathbb E[R_i]"). Histograma continuo con densidad 1/4 en [6,10].

## Layout y disposicion:

- Gráfica en LEFT*3, centro y=0.6, ancho 5.4 y alto 2.5; fórmulas en RIGHT*3, y=1.5,0.1,-1.3, por fases. Linealidad centrada en y=-2.7.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Write de la integral del indicador. Sombrear la región donde vale uno y dejar sin sombrear la parte donde vale cero.
- [TRIGGER_2] **00:18–00:35:** Marcar 6,7,8,10; sombrear [7,10] y evaluar la integral. Crear una hipótesis Y=8 y Cross sobre el salto a probabilidad uno.
- [TRIGGER_3] **00:35–00:55:** Multiplicar 25 por 3/4 y revelar 18.75. Indicate de la etiqueta de independencia X,Y; mantener separada la advertencia sobre correlación de la operación de sumar trabajos.
- [TRIGGER_4] **00:55–01:15:** Crear tres tarjetas de recompensas genéricas y mover sus esperanzas a una suma. Write de linealidad y de una etiqueta Tex de valor esperado, sin prometer que cada ejecución pague exactamente esa cantidad.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para área y probabilidad; ACCENT_MINT para esperanza; ACCENT_VINO para sustitución incorrecta por la media; ACCENT_INDIGO para suma.

---

## Escena: 08

## Nombre: Quitar los huecos sin perder nada

## Descripcion Breve: Toda pausa puede eliminarse desplazando los trabajos posteriores a la izquierda.

## Objetivo Pedagogico: Demostrar que existe un óptimo sin tiempos ociosos.

## Voz en off:

> "[TRIGGER_1] Antes de explorar órdenes, resolvamos otra posibilidad: ¿conviene esperar sin trabajar? Imagina una agenda con un hueco de dos unidades entre dos encargos. Desplacemos hacia la izquierda todo lo que viene después. [TRIGGER_2] Ninguna finalización aumenta. Por tanto, ninguna fecha obligatoria que se cumplía deja de cumplirse: todos esos límites dicen terminar a más tardar, nunca esperar hasta una fecha mínima. [TRIGGER_3] Y cada recompensa esperada es no creciente con el tiempo. Adelantar una entrega conserva o mejora su base más bono esperado. El trabajo anterior al hueco no cambia; los posteriores no pierden dinero. [TRIGGER_4] Eliminamos cada pausa de esta manera. Existe una agenda óptima que empieza en cero y trabaja sin huecos entre sus encargos. Así, el tiempo que consume un conjunto es exactamente la suma de sus duraciones."

## Descripcion Visual Detallada:

Duración orientativa: 01:01. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos líneas temporales, agenda con hueco y agenda compactada; tres bloques de duraciones 2,3,1 con pausa de 2 tras el primero. MathTex(r"(F_1,F_2,F_3)=(2,7,8)\to(2,5,6)"), MathTex(r"t'\le t\Rightarrow w_i(t')\ge w_i(t)"). Marcadores de fechas sobre cada bloque.

## Layout y disposicion:

- Ejes de x=-5.4 a 5.4; unidad de tiempo 1.1; agenda original y=1, compactada y=-0.6. Origen temporal x=-4.4; desigualdades en y=-2.1 y y=-2.8.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Create de los bloques y un rectángulo discontinuo para la pausa. Duplicar la agenda en la fila inferior.
- [TRIGGER_2] **00:15–00:29:** Mover los dos bloques posteriores dos unidades de tiempo a la izquierda. Conservar los marcadores de d fijos; indicar las finalizaciones menores.
- [TRIGGER_3] **00:29–00:45:** Transportar cada nuevo tiempo a una curva w no creciente y comparar alturas con Indicate. El primer bloque permanece inmóvil.
- [TRIGGER_4] **00:45–01:01:** FadeOut del hueco; escribir las dos desigualdades y la suma de duraciones. Mostrar que el mismo argumento elimina una pausa inicial desplazando todos los trabajos, sin desarrollar una hipótesis nueva.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. TEXT_MUTED para espera; ACCENT_TERRACOTTA para desplazamiento temporal; ACCENT_MINT para recompensa no menor; ACCENT_INDIGO para agenda.

---

## Escena: 09

## Nombre: El árbol que no cabe en el reloj

## Descripcion Breve: Las secuencias crecen factorialmente y el tiempo numérico también es demasiado grande.

## Objetivo Pedagogico: Motivar una compresión que no dependa del horizonte temporal.

## Voz en off:

> "[TRIGGER_1] Podríamos probar todos los órdenes y todos los subconjuntos. Para elegir k trabajos distintos y ordenarlos hay n factorial dividido entre n menos k factorial posibilidades. Sumamos desde k igual a cero hasta n. [TRIGGER_2] Eso crece en orden factorial. Sólo las permutaciones de veinte trabajos ya son aproximadamente dos punto cuarenta y tres por diez a la dieciocho. Evaluar cada agenda no es una opción razonable. [TRIGGER_3] Otra idea sería guardar la mejor ganancia para cada instante. Pero las duraciones pueden llegar a mil millones y hay hasta veinte trabajos: sus sumas alcanzan veinte mil millones. El reloj numérico tampoco ofrece una tabla pequeña. [TRIGGER_4] Necesitamos otra pregunta. Si dos agendas distintas ya completaron exactamente los mismos trabajos, ¿qué diferencias entre ellas todavía pueden afectar al futuro? [Pausa.] No todo lo que cambia el pasado tiene que conservarse en el estado."

## Descripcion Visual Detallada:

Duración orientativa: 01:06. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Árbol de secuencias con ramas de aceptar trabajos diferentes; MathTex(r"\sum_{k=0}^{n}\frac{n!}{(n-k)!}=\Theta(n!)"), MathTex(r"20!\approx2.43\cdot10^{18}"), MathTex(r"\sum c_i\le2\cdot10^{10}"). Dos hojas con igual conjunto destacado.

## Layout y disposicion:

- Árbol en panel superior, x∈[-5.8,5.8], niveles y=2,1,0. Fórmulas en y=-1.2 y y=-2.3 por fases; comparación de hojas sustituye el árbol en el último disparador.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Expandir tres elecciones de primer trabajo y sus opciones restantes; incluir el plan vacío como hoja válida. Write de la suma por longitudes k.
- [TRIGGER_2] **00:16–00:31:** TransformMatchingTex hacia la cifra de 20!, rotulada como sólo órdenes completos, no como total exacto de todas las secuencias.
- [TRIGGER_3] **00:31–00:48:** ReplacementTransform del árbol por una recta temporal con ruptura de escala y extremo 2·10¹⁰. Marcar que una tabla indexada por cada instante sería enorme.
- [TRIGGER_4] **00:48–01:06:** Recuperar dos hojas con los mismos identificadores y distinto orden. Alinear sus bloques para comparar tiempo final, dejando su recompensa todavía separada.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para secuencias; ACCENT_TERRACOTTA para tamaño; ACCENT_CYAN para conjunto compartido; TEXT_MUTED para ramas sin expandir del esquema.

---

## Escena: 10

## Nombre: Distinto pasado, la misma hora

## Descripcion Breve: Permutar un conjunto conserva su duración total, aunque cambie su ganancia.

## Objetivo Pedagogico: Descubrir T[S] sin confundirlo con equivalencia de órdenes completos.

## Voz en off:

> "[TRIGGER_1] Tomemos tres trabajos que duran dos, tres y una unidades. En el orden A, B, C sus finalizaciones son dos, cinco y seis. En el orden B, C, A son tres, cuatro y seis. Las entregas individuales cambian. [TRIGGER_2] Pero los dos planes terminan en seis. Y cualquier orden de esos mismos tres trabajos suma dos más tres más uno. Para un conjunto S, llamemos T de S a esa suma. [TRIGGER_3] Eso no significa que los órdenes ganen lo mismo ni que todos sean factibles. Una fecha temprana puede invalidar uno, y un bono puede hacer mejor al otro. La coincidencia aparece en la hora desde la que continuamos. [TRIGGER_4] Además quedan exactamente los mismos trabajos sin utilizar. Si ambos prefijos son factibles, cualquier lista que añadamos después empieza a la misma hora. Ahí está la información que sus futuros comparten."

## Descripcion Visual Detallada:

Duración orientativa: 01:06. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos agendas ABC y BCA con duraciones 2,3,1; marcas de finalización (2,5,6) y (3,4,6). MathTex(r"T[S]=\sum_{i\in S}c_i"). Bandeja de trabajos restantes idéntica junto a cada agenda; etiquetas de ganancia v₁ y v₂ sin asignar cifras.

## Layout y disposicion:

- Agendas en y=1 y y=-0.4, origen x=-5, escala 1.15 por unidad. Línea vertical común de fin x=1.9; bandejas en x=4.4. Fórmula en y=-2.1; aclaración de factibilidad en y=-2.8.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:18:** Create de ABC y BCA y Write de cada finalización, no sólo la última. Mantener el color de cada trabajo al cambiar de posición.
- [TRIGGER_2] **00:18–00:33:** Alinear sus extremos con una línea vertical y construir T[S]=2+3+1=6. Encerrar el conjunto {A,B,C} en ambas filas.
- [TRIGGER_3] **00:33–00:51:** Revelar v₁ y v₂ como valores potencialmente diferentes. Mostrar un marcador de fecha simbólico y una leyenda de que la factibilidad debe verificarse; no inventar que ambos órdenes siempre cumplen.
- [TRIGGER_4] **00:51–01:06:** Duplicar una misma continuación en ambas filas desde t=6 y alinear sus finalizaciones. Conectar las dos bandejas restantes mediante una llave de igualdad.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. Colores estables A=ACCENT_INDIGO, B=ACCENT_CYAN, C=ACCENT_TERRACOTTA; ACCENT_MINT para tiempo final común.

---

## Escena: 11

## Nombre: Conservar el mejor pasado

## Descripcion Breve: Un prefijo peor con el mismo conjunto no puede mejorar ninguna continuación.

## Objetivo Pedagogico: Demostrar dominancia, el fundamento de la compresión.

## Voz en off:

> "[TRIGGER_1] Supongamos ahora que esos dos prefijos sí son factibles. El primero ha ganado, en esperanza, v uno; el segundo, v dos, con v dos mayor o igual. Los dos usan S y terminan en T de S. [TRIGGER_2] Añadamos la misma continuación a ambos. Sus trabajos empiezan y terminan en los mismos instantes, así que cumplen las mismas fechas y añaden exactamente la misma ganancia esperada, llamémosla delta. [TRIGGER_3] El primer total es v uno más delta y el segundo es v dos más delta. La desigualdad se conserva. Ninguna continuación puede rescatar la inferioridad del primer prefijo. [TRIGGER_4] Podemos descartarlo y guardar sólo el mejor valor de S. No estamos diciendo que el orden no importe: lo comparamos y conservamos su mejor resultado. Lo que dejamos de guardar es la historia completa una vez que ya conocemos su valor y su conjunto."

## Descripcion Visual Detallada:

Duración orientativa: 01:05. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos tarjetas de prefijos factibles con MathTex(r"v_1\le v_2"), tiempo común T[S], misma continuación C. MathTex(r"v_1+\Delta\le v_2+\Delta"). Nodo fusionado etiquetado DP[S].

## Layout y disposicion:

- Prefijos en (-3.8,1,0) y (-3.8,-0.8,0); continuaciones en (1,1,0) y (1,-0.8,0), ancho 4.4. Desigualdad en y=-2.4; nodo fusionado en (0,0,0) tras retirar las filas.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Write de valores, factibilidad y tiempo común. Indicate de la condición v₁≤v₂.
- [TRIGGER_2] **00:17–00:31:** Copiar una continuación bloque por bloque a ambas filas, con idénticas marcas de tiempo. Crear Brace para su misma ganancia Δ.
- [TRIGGER_3] **00:31–00:45:** TransformMatchingTex de la desigualdad original a la desigualdad de totales. Atenuar únicamente el prefijo inferior, no sus trabajos como si estuvieran prohibidos.
- [TRIGGER_4] **00:45–01:05:** ReplacementTransform de las dos tarjetas a DP[S], conservando el mayor valor. Write de una leyenda Tex: el conjunto fija el futuro disponible; el valor resume el mejor pasado.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para valor dominante; TEXT_MUTED para prefijo descartado; ACCENT_CYAN para continuación idéntica; ACCENT_INDIGO para DP.

---

## Escena: 12

## Nombre: Un conjunto cabe en una fila de interruptores

## Descripcion Breve: Una máscara binaria representa qué trabajos ya se usaron.

## Objetivo Pedagogico: Hacer intuitivo el estado por subconjuntos y sus operaciones.

## Voz en off:

> "[TRIGGER_1] Con veinte trabajos, un conjunto puede representarse con veinte interruptores. Encendido significa incluido; apagado significa disponible. Esa fila es una máscara de bits, una dirección para nuestra tabla. [TRIGGER_2] Con tres trabajos A, B y C, asignamos A al bit cero, B al uno y C al dos. Escribimos los bits de C a A: la máscara uno cero uno en binario contiene A y C. Su duración es c de A más c de C. [TRIGGER_3] Añadir B cambia el bit central de cero a uno: pasamos de uno cero uno a uno uno uno. Quitar C de uno cero uno deja cero cero uno. El dibujo del conjunto y el número binario describen la misma operación. [TRIGGER_4] Hay dos opciones por interruptor y n interruptores: dos elevado a n conjuntos. Para veinte son un millón cuarenta y ocho mil quinientos setenta y seis. Sigue siendo mucho, pero es un universo manejable frente al factorial de los órdenes."

## Descripcion Visual Detallada:

Duración orientativa: 01:14. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tres Square con etiquetas superiores MathTex(r"C\ (2),B\ (1),A\ (0)"); filas MathTex(r"101_2=5"), MathTex(r"111_2=7"), MathTex(r"001_2=1"). MathTex(r"T[101_2]=c_A+c_C"), MathTex(r"2^{20}=1\,048\,576").

## Layout y disposicion:

- Interruptores en x=-2,0,2 y y=0.8, lado 1.1. Conjunto escrito en y=-0.7 y duración en y=-1.7. Contador de máscaras en y=-2.8; rótulo de convención de bits en y=2.2.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:14:** FadeIn de interruptores y sus etiquetas. Encender y apagar uno para vincular pertenencia y disponibilidad.
- [TRIGGER_2] **00:14–00:36:** Fijar 101₂, iluminar A y C y construir su duración. Leer la secuencia binaria como uno cero uno, sin interpretarla como el decimal ciento uno.
- [TRIGGER_3] **00:36–00:55:** Transform de una copia a 111₂ al añadir B; transformar otra copia a 001₂ al quitar C. Conservar la fila original para comparar las operaciones.
- [TRIGGER_4] **00:55–01:14:** Crear un árbol de dos opciones por bit y contraerlo a 2ⁿ. Sustituir n=20 y escribir la cifra exacta de máscaras.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para bits encendidos; TEXT_MUTED para apagados; ACCENT_CYAN para bit añadido; ACCENT_TERRACOTTA para bit retirado.

---

## Escena: 13

## Nombre: Qué promete cada casilla

## Descripcion Breve: La DP estricta distingue conjuntos factibles e inviables.

## Objetivo Pedagogico: Definir el invariante antes de usar transiciones.

## Voz en off:

> "[TRIGGER_1] Definamos la tabla con cuidado: DP de S es la máxima ganancia esperada de una agenda factible que realiza exactamente los trabajos de S. La palabra exactamente es parte del contrato. [TRIGGER_2] El conjunto vacío tarda cero y gana cero. Un conjunto para el que no existe ningún orden válido necesita una marca de inviabilidad, que matemáticamente escribimos como menos infinito. No es lo mismo que una ganancia legítima de cero. [TRIGGER_3] Por ejemplo, un trabajo que tarda dos y vence en uno es imposible incluso si empieza primero. Su conjunto de un elemento no tiene valor cero como agenda realizada: no tiene ninguna agenda válida. [TRIGGER_4] Tampoco basta conocer T de S para certificar factibilidad. Si dos trabajos duran uno y ambos vencen en uno, cada uno cabe solo, pero juntos alguno terminará en dos. La duración total se calcula; la posibilidad de ejecutar todo el conjunto se demuestra mediante transiciones válidas."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tabla de máscaras con casillas de valor y de inviabilidad; MathTex(r"DP[\varnothing]=0"), MathTex(r"DP[S]=-\infty\ \text{si }S\text{ es inviable}"). Ejemplos separados: (c,d)=(2,1); dos tareas (1,1),(1,1). Tex para la palabra exactamente.

## Layout y disposicion:

- Tabla izquierda centrada en (-3,0.3,0), ancho 5.2; ejemplos a derecha, centro (3.1,0.3,0). Bases en y=2.2 y condición de exactitud en y=-2.6.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Write del contrato y subrayar exactamente con Underline. Crear una casilla asociada al conjunto, sin presentarla como conjunto de opciones elegibles.
- [TRIGGER_2] **00:15–00:33:** Rellenar la máscara vacía con 0 y una inviable con −∞. Dar al cero un contorno sólido y a la inviabilidad una Cross para que el color no sea la única diferencia.
- [TRIGGER_3] **00:33–00:49:** Animar el trabajo de duración 2 rebasando la fecha 1. Enviar su casilla a −∞, no al cero inicial.
- [TRIGGER_4] **00:49–01:10:** Mostrar los dos órdenes posibles de las tareas unitarias con fecha 1; marcar la segunda entrega como tardía en ambos. Escribir T=2 junto a una casilla inviable para separar los conceptos.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para cero factible; ACCENT_VINO para inviabilidad; ACCENT_INDIGO para casillas; ACCENT_TERRACOTTA para fecha límite.

---

## Escena: 14

## Nombre: Una flecha que añade un encargo

## Descripcion Breve: Extender un prefijo factible produce la transición fundamental.

## Objetivo Pedagogico: Construir la recurrencia sin ocultar guardas ni tiempo de evaluación.

## Voz en off:

> "[TRIGGER_1] Partimos de un conjunto S que sí tiene valor factible. Elegimos un trabajo j que todavía no está incluido. Si lo colocamos al final, termina en T de S más c de j. Ésa es la hora que usamos para todo el cálculo. [TRIGGER_2] Primero comprobamos que esa hora no supere d de j. Si la supera, rechazamos la flecha. Si no, los trabajos anteriores siguen terminando donde terminaban: añadir algo al final no perjudica sus entregas. [TRIGGER_3] Calculamos entonces la ganancia esperada de j en esa nueva hora y la sumamos al valor de S. La casilla destino es S unido con j. Puede haber recibido otra propuesta desde otro orden, así que conservamos la mayor. [TRIGGER_4] Esta flecha decide a la vez la selección y el orden. Añadir j significa aceptarlo después de ese prefijo; no añadirlo sigue siendo una opción porque también podremos terminar nuestra agenda en el conjunto actual."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Dos nodos de estado S y S∪{j}; tarjeta de trabajo j; MathTex(r"t=T[S]+c_j"), MathTex(r"t\le d_j"), MathTex(r"DP[S\cup\{j\}]\gets\max\{DP[S\cup\{j\}],DP[S]+w_j(t)\}"). Dos entradas al mismo destino con valores simbólicos.

## Layout y disposicion:

- Nodo S en (-4.6,0.4,0), compuerta en (0,0.4,0), destino en (4.4,0.4,0). Tiempo en y=1.8, recompensa en y=-1 y actualización dividida en dos líneas en y=-2.2 y -2.9.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:20:** Mover una ficha j apagada a la salida de S y construir t con TransformMatchingTex. Mostrar que j no pertenece a S antes de encender el bit.
- [TRIGGER_2] **00:20–00:36:** Bifurcar la compuerta en t>d_j, con Cross, y t≤d_j, con flecha al destino. Mantener inmóviles las finalizaciones previas.
- [TRIGGER_3] **00:36–00:54:** Transportar t al evaluador w_j, sumar el resultado al valor fuente y comparar con la propuesta ya almacenada. Indicate del máximo y actualizar sólo esa casilla.
- [TRIGGER_4] **00:54–01:10:** Crear un marcador de posible final de agenda en S y otro en el destino. Ambos participan en el máximo global; no forzar otra extensión.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para transición; ACCENT_VINO para guarda fallida; ACCENT_MINT para candidato ganador; ACCENT_INDIGO para tabla.

---

## Escena: 15

## Nombre: Por qué no se nos escapa ninguna agenda

## Descripcion Breve: Separar el último trabajo permite probar exhaustividad y optimalidad.

## Objetivo Pedagogico: Dar la inducción completa de la DP estricta.

## Voz en off:

> "[TRIGGER_1] La construcción sólo produce agendas válidas: parte del vacío y cada flecha añade un trabajo disponible que cumple su fecha. Su valor suma exactamente la recompensa esperada que corresponde a cada finalización. [TRIGGER_2] Ahora tomemos cualquier agenda óptima no vacía y separemos su último trabajo j. Lo anterior realiza un conjunto S sin j y termina en T de S. Nuestra tabla considera precisamente la flecha que vuelve a añadir j. [TRIGGER_3] Si el prefijo elegido no fuera el mejor de S, podríamos sustituirlo por el mejor. Terminaría a la misma hora, conservaría la validez de j y no reduciría el dinero. Ésta es la dominancia que ya demostramos. [TRIGGER_4] El vacío inicia la prueba. Suponiendo correctos todos los conjuntos más pequeños, la flecha correcta alcanza el mejor valor de cada conjunto mayor. Y como podemos elegir cualquier subconjunto de encargos, la respuesta final es el mayor valor de toda la tabla."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Agenda óptima con último bloque j separable; prefijo S y valor DP[S]; MathTex(r"U=S\cup\{j\}"), MathTex(r"\mathrm{OPT}=\max_{S\subseteq\{1,\ldots,n\}}DP[S]"). Niveles de conjuntos por cardinalidad 0,1,2,3.

## Layout y disposicion:

- Agenda en y=1.3 desde x=-5 hasta x=5; corte del último bloque en x=2.2. Niveles de inducción en y=-0.2; fórmula global en y=-2.3. La sustitución del prefijo ocupa el panel central durante su disparador.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Create de un camino desde el vacío y resaltar cada compuerta válida. Write de una etiqueta de validez de todas las agendas generadas.
- [TRIGGER_2] **00:15–00:33:** Separar el último bloque j con un desplazamiento corto y dibujar una llave sobre S. Write de su hora final y de la flecha incluida por la recurrencia.
- [TRIGGER_3] **00:33–00:50:** ReplacementTransform del prefijo por una tarjeta de su mejor orden, manteniendo fijo el extremo T[S]. Indicate de j, que conserva hora y recompensa.
- [TRIGGER_4] **00:50–01:10:** Encender sucesivamente los niveles de cardinalidad y escribir el máximo sobre todas las máscaras. Distinguir esta prueba por cardinalidad del orden numérico usado al implementar.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para validez y óptimo; ACCENT_INDIGO para inducción; ACCENT_CYAN para último trabajo; ACCENT_TERRACOTTA para tiempo conservado.

---

## Escena: 16

## Nombre: Un ejemplo donde el borde importa

## Descripcion Breve: El trabajo A del ejemplo oficial termina exactamente en el extremo de su umbral continuo.

## Objetivo Pedagogico: Iniciar la traza con parámetros completos y el valor de A.

## Voz en off:

> "[TRIGGER_1] Veamos el segundo ejemplo del enunciado. A dura ocho, vence en diez y paga quince de base. Su bono vale cincuenta, pero el umbral es uniforme entre uno y ocho. B dura siete, vence en veinte y paga uno; su bono va de veinte a treinta y su umbral de seis a diez. [TRIGGER_2] Empezamos con la máscara vacía: tiempo cero, valor cero. Si aceptamos sólo A, termina en ocho. Su fecha obligatoria es diez, así que esa entrega es válida. [TRIGGER_3] ¿Y el bono? Termina exactamente en el extremo derecho de una uniforme continua entre uno y ocho. La región favorable tiene longitud cero. No cobramos cincuenta en esperanza: el bono esperado es cero. [TRIGGER_4] Por tanto, la casilla de sólo A guarda quince y su tiempo es ocho. El primer paso ya muestra por qué necesitábamos distinguir una fecha obligatoria de un umbral de bono y una distribución continua de un punto fijo."

## Descripcion Visual Detallada:

Duración orientativa: 01:11. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tabla completa con columnas trabajo,d,p,c,[lx,rx],[ly,ry]; filas A=(10,15,8,[50,50],[1,8]), B=(20,1,7,[20,30],[6,10]). MathTex(r"T[00_2]=0,DP[00_2]=0"), MathTex(r"T[01_2]=8,DP[01_2]=15"). Segmento [1,8] de A.

## Layout y disposicion:

- Tabla en (0,1.5,0), ancho máximo 11.8, filas separadas 0.7; panel de máscara izquierda (-3,-0.7,0); intervalo de A derecha (2.8,-0.7,0); cálculo en y=-2.4. Bits escritos B,A.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:24:** Write de los siete datos de cada fila y fijar la convención B,A para dos bits. No omitir los intervalos degenerados de importe.
- [TRIGGER_2] **00:24–00:37:** Encender 00₂ con valor cero; añadir A y avanzar el reloj a 8. Indicate de 8≤10.
- [TRIGGER_3] **00:37–00:53:** Mover t al extremo 8 del intervalo [1,8] y reducir la parte favorable a longitud cero. Write de 50·0=0.
- [TRIGGER_4] **00:53–01:11:** Sumar 15+0 y depositar 15 en 01₂. Mantener la tabla de datos disponible como tarjeta reducida para las tres escenas siguientes.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para A; ACCENT_CYAN para B; ACCENT_MINT para ganancias; ACCENT_TERRACOTTA para tiempo y umbral.

---

## Escena: 17

## Nombre: Tres cuartos de un bono

## Descripcion Breve: El trabajo B solo produce una ganancia esperada de 19.75.

## Objetivo Pedagogico: Desarrollar cada operación de la segunda rama inicial.

## Voz en off:

> "[TRIGGER_1] Volvamos al vacío y aceptemos sólo B. Su duración es siete, así que termina en siete y cumple la fecha veinte. Todavía estamos dentro del intervalo de umbrales, que va de seis a diez. [TRIGGER_2] La longitud total es cuatro. Los umbrales favorables van de siete a diez y suman tres. La probabilidad de cobrar el bono es tres cuartos. [TRIGGER_3] El importe medio es veinte más treinta, dividido entre dos: veinticinco. Multiplicamos veinticinco por tres cuartos y obtenemos dieciocho punto setenta y cinco de bono esperado. [TRIGGER_4] Añadimos la base, que es uno. El valor de sólo B es diecinueve punto setenta y cinco y su tiempo es siete. Ya supera a sólo A, pero todavía tenemos que comprobar si añadir el otro trabajo puede mejorar la respuesta."

## Descripcion Visual Detallada:

Duración orientativa: 01:00. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Máscaras 00₂ y 10₂; segmento [6,10] con corte en 7. MathTex(r"q_B(7)=\frac{10-7}{10-6}=\frac34"), MathTex(r"\mu_B=\frac{20+30}{2}=25"), MathTex(r"w_B(7)=1+25\cdot\frac34=19.75").

## Layout y disposicion:

- Tabla de datos reducida arriba y=2.3; segmento de x=-4 a x=4 en y=0.8, escala 2 por unidad. Cálculos en y=-0.5,-1.5,-2.5, presentados progresivamente. Estado destino a x=4.7,y=1.8.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Crear la flecha 00₂→10₂, mover el reloj a 7 y comprobar 7≤20.
- [TRIGGER_2] **00:16–00:28:** Create de Brace de longitud 4 y de longitud 3. TransformMatchingTex de sus longitudes a 3/4.
- [TRIGGER_3] **00:28–00:41:** Construir el punto medio 25 y multiplicarlo por 3/4; Write de 18.75 como bono, no como ganancia total.
- [TRIGGER_4] **00:41–01:00:** Añadir 1 y actualizar DP[10₂]=19.75. Colocar un halo provisional de mejor valor, sin descartar aún las extensiones.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para B y probabilidad; ACCENT_MINT para esperanza; ACCENT_TERRACOTTA para corte en 7; ACCENT_INDIGO para casilla.

---

## Escena: 18

## Nombre: Dos órdenes, dos resultados distintos

## Descripcion Breve: A→B es válido y vale 16; B→A incumple la fecha de A.

## Objetivo Pedagogico: Completar todas las transiciones del conjunto de dos trabajos.

## Voz en off:

> "[TRIGGER_1] Si hacemos A y después B, A termina en ocho y conserva sus quince. B termina en quince. Sigue antes de su fecha veinte, pero ya pasó su umbral máximo de bono, diez. [TRIGGER_2] B añade únicamente su base, uno. El total de ese orden es dieciséis. Ésa es una propuesta válida para la máscara que contiene ambos trabajos. [TRIGGER_3] En el otro orden, B termina en siete y A terminaría en quince. Pero A tenía fecha obligatoria diez. Esta flecha se rechaza antes de añadir su recompensa; no podemos dar por válida la agenda y cobrar una base tardía. [TRIGGER_4] Así, el conjunto de ambos tiene valor dieciséis. Su tiempo total es quince en los dos órdenes, pero sólo uno era factible. La máscara conserva el mejor orden válido, no un promedio entre órdenes ni una suma de sus beneficios."

## Descripcion Visual Detallada:

Duración orientativa: 01:06. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Agendas A→B y B→A; MathTex(r"8+7=15"), MathTex(r"DP[11_2]=15+1=16"), MathTex(r"15>d_A=10"). Grafo de cuatro máscaras con las dos aristas que llegan a 11₂, una válida y otra tachada.

## Layout y disposicion:

- Agendas en y=1 y y=-0.5, origen x=-5.5, escala 0.6 por unidad temporal. Cálculos en x=4.5; grafo sustituye agendas al final, con 00₂ arriba, 01₂/10₂ al centro y 11₂ abajo.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Crear A→B con finalizaciones 8 y 15. Comparar 15 con d_B=20 y después con ry_B=10; los dos controles tienen resultados distintos.
- [TRIGGER_2] **00:16–00:28:** Write de bono cero y base uno para B; sumar 15+1 y enviar 16 a 11₂.
- [TRIGGER_3] **00:28–00:47:** Crear B→A y mover la finalización de A a 15. Cross sobre 15≤10 y sobre la arista 10₂→11₂, sin evaluar una entrega inválida como recompensa admisible.
- [TRIGGER_4] **00:47–01:06:** Mostrar T[11₂]=15 junto a DP[11₂]=16. Encerrar el candidato válido y mantener la ruta rechazada visible como evidencia de que el tiempo no certifica la factibilidad.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para A; ACCENT_CYAN para B; ACCENT_VINO para arista inválida; ACCENT_MINT para candidato 16.

---

## Escena: 19

## Nombre: La mejor agenda no llena la tabla

## Descripcion Breve: El máximo entre subconjuntos supera al valor de la máscara completa.

## Objetivo Pedagogico: Cerrar la traza y explicar por qué aceptar más no siempre conviene.

## Voz en off:

> "[TRIGGER_1] Ya calculamos todas las posibilidades de este ejemplo: nada vale cero; sólo A vale quince; sólo B vale diecinueve punto setenta y cinco; ambos valen dieciséis. [TRIGGER_2] La respuesta es el mayor de esos cuatro números: diecinueve punto setenta y cinco. Tony debe hacer únicamente B para alcanzar ese valor esperado. Aunque existe un orden válido con ambos encargos, gana menos. [TRIGGER_3] Aceptar A obliga a colocar B más tarde en el único orden factible. Ese desplazamiento pierde dieciocho punto setenta y cinco de bono esperado en B y añade quince por A. La pérdida neta es tres punto setenta y cinco. [TRIGGER_4] Por eso actualizamos una respuesta global mientras recorremos todas las máscaras. La casilla de todos los trabajos responde otra pregunta: cuánto vale realizarlos exactamente a todos, si es posible. El problema nos permite escoger."

## Descripcion Visual Detallada:

Duración orientativa: 01:04. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tabla de máscaras 00₂,01₂,10₂,11₂ con tiempos 0,8,7,15 y valores 0,15,19.75,16. MathTex(r"\max(0,15,19.75,16)=19.75"), MathTex(r"18.75-15=3.75"). Registro separado de mejor respuesta.

## Layout y disposicion:

- Tabla centrada en (0,0.7,0), ancho 9.5; registro de respuesta en (0,-1.3,0); comparación marginal en y=-2.5. No ordenar filas por ganancia: mantener orden numérico de máscaras.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:13:** Write de las cuatro filas completas, incluyendo tiempos y valores. Colocar un cursor de lectura al inicio.
- [TRIGGER_2] **00:13–00:29:** Recorrer los valores con un registro máximo: 0→15→19.75→19.75. Indicate de la fila 10₂ como decisión final.
- [TRIGGER_3] **00:29–00:48:** Separar la pérdida del bono de B y la ganancia de A en dos barras; TransformMatchingTex hacia 18.75−15=3.75.
- [TRIGGER_4] **00:48–01:04:** Encerrar el registro global y la máscara completa con rótulos distintos. Mantener el valor 16 de la máscara completa sin sustituirlo por 19.75.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para mejor respuesta; ACCENT_TERRACOTTA para coste de oportunidad; ACCENT_INDIGO para tabla; TEXT_MUTED para candidatos inferiores.

---

## Escena: 20

## Nombre: La misma agenda vista desde el último trabajo

## Descripcion Breve: La implementación original quita un bit para elegir la última tarea.

## Objetivo Pedagogico: Relacionar ambas direcciones de transición y el orden de evaluación.

## Voz en off:

> "[TRIGGER_1] Podemos construir una agenda añadiendo el siguiente trabajo, como hicimos, o preguntar cuál fue el último. Para una máscara M y un trabajo i incluido, el prefijo es M sin i y la finalización de i es T de M. [TRIGGER_2] La propuesta toma el valor del prefijo y añade la ganancia de i en ese tiempo, siempre que T de M no supere su fecha. Esa es la dirección que usa el archivo del usuario. [TRIGGER_3] En el ejemplo, al calcular la máscara uno uno, probar A como último se rechaza porque quince supera diez. Probar B como último usa el valor de sólo A, quince, y añade uno: dieciséis. [TRIGGER_4] Quitar un bit encendido siempre reduce el número de la máscara. Por eso recorrerlas en orden numérico creciente deja preparado cada prefijo antes de consultarlo. Aunque la función se llame dpfunc, aquí no se llama recursivamente: lee una casilla ya calculada."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"P=M\setminus\{i\},\quad t=T[M]"), MathTex(r"DP[M]=\max_{i\in M,\ T[M]\le d_i}\{DP[M\setminus\{i\}]+w_i(T[M])\}") para la versión estricta, con candidatos de prefijo factible. Diagrama 11₂→10₂ al quitar A y 11₂→01₂ al quitar B; tarjetas Tex de tiempoNecesario, valEsperadoGanancia y dpfunc.

## Layout y disposicion:

- Máscara M en (0,1.4,0); prefijos en (-3,-0.1,0),(3,-0.1,0). Fórmula en dos líneas en y=-1.5 y -2.4. Los nombres de función aparecen como pequeñas etiquetas Tex, nunca como bloque de código.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:19:** Despegar cada posible último bloque y apagar su bit en una copia de M; mostrar el prefijo correspondiente.
- [TRIGGER_2] **00:19–00:35:** Crear una flecha de lectura desde cada prefijo y una tarjeta de recompensa evaluada en T[M]. Rotular que la fórmula mostrada exige prefijo factible para conservar la semántica estricta.
- [TRIGGER_3] **00:35–00:51:** Evaluar ambas candidaturas de 11₂: A falla la fecha; B usa 15+1=16. Conservar la comparación completa.
- [TRIGGER_4] **00:51–01:10:** Mostrar una fila 00₂,01₂,10₂,11₂ y mover el cursor de izquierda a derecha. Las flechas de dependencia apuntan a casillas anteriores; escribir iteración, sin pila recursiva.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para lectura de prefijos; ACCENT_TERRACOTTA para bit retirado; ACCENT_MINT para candidato válido; ACCENT_INDIGO para orden numérico.

---

## Escena: 21

## Nombre: El cero que cambia el significado

## Descripcion Breve: El código original inicializa todas las máscaras con cero.

## Objetivo Pedagogico: Exhibir por qué su arreglo no representa subconjuntos exactos.

## Voz en off:

> "[TRIGGER_1] Pero hay una diferencia importante. El código original empieza con cero en todas las máscaras, incluso cuando no existe un orden que realice sus trabajos. Llamemos A a su arreglo para no confundirlo con nuestra DP estricta. [TRIGGER_2] Probemos un trabajo U que tarda dos, vence en uno y paga cien, sin bono. Es imposible. Otro trabajo V tarda uno, vence en diez y paga siete, también sin bono. El arreglo original da cero a sólo U y siete a sólo V. [TRIGGER_3] Para la máscara de ambos, puede tomar el cero de U y añadir V, evaluándolo en el tiempo total tres. Guarda siete, aunque no existe ninguna agenda que ejecute ambos trabajos. La tabla estricta marca ese conjunto como inviable. [TRIGGER_4] Sin embargo, el máximo global sigue siendo siete, y sí podemos ganarlo realizando solamente V en el instante uno. Esto no se justifica diciendo que ambas tablas son iguales. Necesitamos demostrar por qué esos valores artificiales no inflan la respuesta final."

## Descripcion Visual Detallada:

Duración orientativa: 01:14. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"A[M]=\max(\{0\}\cup\{A[M\setminus\{i\}]+w_i(T[M]):i\in M,\ T[M]\le d_i\})"). Tabla comparativa para 00₂,01₂,10₂,11₂: A=(0,0,7,7), DP=(0,−∞,7,−∞); bits V,U. Datos U=(c=2,d=1,p=100), V=(1,10,7), bonos cero.

## Layout y disposicion:

- Datos en y=2.2; tabla comparativa centrada (0,0.5,0), ancho 10; transición artificial debajo en y=-1.5; testigo real V en y=-2.7. La fórmula general sustituye la tabla durante el primer disparador.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:17:** Write de la recurrencia A con el cero incluido y destacar ese término. Cambiar el nombre visible del arreglo a A antes de mostrar valores.
- [TRIGGER_2] **00:17–00:37:** Construir las dos máscaras unitarias y las dos columnas de tabla. Cross sobre la entrega imposible de U; mostrar 0 en A y −∞ en DP.
- [TRIGGER_3] **00:37–00:55:** Crear la lectura de A[01₂]=0 y añadir 7 para 11₂ a tiempo 3. Marcar que ese valor no certifica la ejecución de U; mantener DP[11₂]=−∞.
- [TRIGGER_4] **00:55–01:14:** Crear una agenda real con sólo V, fin 1 y ganancia 7. Conectar ese testigo al máximo global y dejar visible la diferencia entre columnas.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para DP estricta; ACCENT_CYAN para A original; ACCENT_VINO para inviabilidad; ACCENT_MINT para testigo factible.

---

## Escena: 22

## Nombre: Primera mitad de la garantía

## Descripcion Breve: Toda agenda factible está representada por la recurrencia original.

## Objetivo Pedagogico: Demostrar que el máximo de A no queda por debajo del óptimo.

## Voz en off:

> "[TRIGGER_1] La primera desigualdad dice que el arreglo original no pierde la mejor agenda. En el vacío, tanto A como la tabla estricta valen cero. Ésa es la base de la comparación. [TRIGGER_2] Tomemos un conjunto factible M y un último trabajo i de su mejor orden. Su prefijo P también es factible. Si A de P es al menos el valor estricto del prefijo, añadir la misma recompensa conserva esa desigualdad. [TRIGGER_3] La transición aparece en A porque la última entrega cumple su fecha. Y A toma un máximo que incluye esa propuesta. Por inducción sobre el tamaño del conjunto, A de M es al menos DP de M para todos los conjuntos factibles. [TRIGGER_4] Por tanto, el máximo de A es al menos el óptimo verdadero. Eso todavía no prueba que sea correcto: podría ser demasiado grande. Para descartar esa posibilidad, vamos a construir una agenda real detrás de cada valor que A almacena."

## Descripcion Visual Detallada:

Duración orientativa: 01:12. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"A[\varnothing]=DP[\varnothing]=0"), MathTex(r"A[P]\ge DP[P]"), MathTex(r"A[P]+w_i(T[M])\ge DP[P]+w_i(T[M])"), MathTex(r"\max_M A[M]\ge\mathrm{OPT}"). Dos filas paralelas A y DP con la misma última tarea.

## Layout y disposicion:

- Filas A y DP en y=1 y y=-0.4; prefijos en x=-3, recompensa en x=0.5, resultado en x=4.1. Base en y=2.2; desigualdad global en y=-2.5.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Write de la igualdad base y crear las dos filas con etiquetas inequívocas.
- [TRIGGER_2] **00:15–00:33:** Copiar la misma última tarea a ambas filas y la misma recompensa. TransformMatchingTex para sumar el mismo término a la desigualdad del prefijo.
- [TRIGGER_3] **00:33–00:53:** Crear el selector máximo en la fila A y escribir que su valor es al menos el candidato considerado. Encender una cadena de cardinalidades para expresar la inducción.
- [TRIGGER_4] **00:53–01:12:** Write de la primera cota y dejar abierto un espacio para la cota contraria. No rodear aún el máximo con una igualdad a OPT.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para A; ACCENT_INDIGO para DP; ACCENT_MINT para desigualdad demostrada; ACCENT_TERRACOTTA para prueba pendiente.

---

## Escena: 23

## Nombre: Una agenda real detrás de cada valor artificial

## Descripcion Breve: Los trabajos fantasma sólo introducen tiempo que puede eliminarse.

## Objetivo Pedagogico: Demostrar mediante testigos que A nunca supera el óptimo global.

## Voz en off:

> "[TRIGGER_1] Afirmemos algo más preciso: para cada máscara M existe una agenda factible que usa un subconjunto de M, termina a más tardar en T de M y gana al menos A de M. Si A eligió el cero inicial, la agenda vacía es ese testigo. [TRIGGER_2] Si A eligió una transición desde P, por inducción ya existe un testigo de P. Puede omitir trabajos, así que termina en un tiempo t de P menor o igual que T de P. Añadimos i al final; no estaba usado porque no pertenece a P. [TRIGGER_3] La nueva entrega termina en t de P más c de i, que es menor o igual que T de M. La transición había comprobado T de M menor o igual que d de i, así que la entrega real también cumple. Y terminar antes no reduce su recompensa: w en la hora real es al menos w en T de M. [TRIGGER_4] El testigo ampliado gana al menos A de P más esa recompensa calculada: al menos A de M. Todo valor almacenado queda por debajo de alguna agenda real, y por tanto del óptimo. El máximo de A no puede superar OPT; junto con la desigualdad anterior, queda demostrada la igualdad."

## Descripcion Visual Detallada:

Duración orientativa: 01:33. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Plan testigo R⊆P con tiempo t_P; hueco discontinuo hasta T[P]; nuevo bloque i. MathTex(r"t_P+c_i\le T[P]+c_i=T[M]\le d_i"), MathTex(r"w_i(t_P+c_i)\ge w_i(T[M])"), MathTex(r"\operatorname{ganancia}(R+i)\ge A[P]+w_i(T[M])=A[M]"), MathTex(r"\max_M A[M]=\mathrm{OPT}").

## Layout y disposicion:

- Agenda testigo en y=1.2, origen x=-5.5, fin real x=-1.5 y fin nominal x=1.2; i se muestra primero tras el fin real y después como copia nominal. Cadena temporal en y=-0.3, recompensa en y=-1.3 y conclusión en y=-2.5. Los tiempos del dibujo son simbólicos, no valores de un caso nuevo.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:21:** Create de un contenedor M y de un subconjunto testigo dentro. Mostrar el caso base de una agenda vacía que obtiene 0 y termina en 0≤T[M].
- [TRIGGER_2] **00:21–00:42:** Construir el testigo de P y el hueco hasta su tiempo nominal. Añadir i a la agenda real; Indicate de i∉P para impedir repetición de tareas.
- [TRIGGER_3] **00:42–01:10:** Alinear fin real y nominal y Write de toda la cadena de desigualdades. Llevar ambos tiempos a una curva no creciente w y comparar sus alturas.
- [TRIGGER_4] **01:10–01:33:** Sumar la cota del prefijo y la nueva recompensa. TransformMatchingTex hacia A[M]≤OPT para cada máscara y después hacia la igualdad de máximos usando ambas cotas, no una igualdad casilla por casilla.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para testigo real; TEXT_MUTED para espera ficticia; ACCENT_CYAN para A; ACCENT_TERRACOTTA para desigualdades temporales.

---

## Escena: 24

## Nombre: Qué permite esa prueba y dónde termina

## Descripcion Breve: La igualdad de máximos no convierte cada máscara original en un plan exacto.

## Objetivo Pedagogico: Delimitar reconstrucción, respuesta global y monotonicidad.

## Voz en off:

> "[TRIGGER_1] La prueba nos autoriza a usar el máximo global del arreglo original. No autoriza a interpretar cada máscara como una agenda que realiza todos sus trabajos, ni a reconstruirlos sin comprobar qué testigo los justifica. [TRIGGER_2] Tampoco basta consultar la máscara completa. En nuestro ejemplo oficial, su valor era dieciséis y la respuesta era diecinueve punto setenta y cinco. El máximo entre subconjuntos sigue siendo indispensable en las dos versiones. [TRIGGER_3] La garantía de los ceros depende de que adelantar una tarea no reduzca su recompensa. Si estuviéramos en otro problema donde esperar aumentara el pago, eliminar las esperas ficticias podría empeorar la agenda real y este argumento dejaría de funcionar. [TRIGGER_4] Para diseñar una tabla fácil de interpretar, podemos usar el estado estricto y una marca de inviabilidad. Para explicar el código original, conservamos su verdadero invariante: cada valor no supera la ganancia de algún plan factible que quizá usa menos trabajos."

## Descripcion Visual Detallada:

Duración orientativa: 01:10. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tres tarjetas Tex: máximo global, máscara exacta, reconstrucción; ecuaciones MathTex(r"\max A=\max DP"), MathTex(r"A[M]\not\equiv DP[M]"). Curva no creciente válida y curva creciente contrafactual, claramente rotulada otro problema.

## Layout y disposicion:

- Tarjetas en x=-4,0,4, y=1.1; ecuaciones en y=-0.2; curvas comparadas en (-3,-1.7,0) y (3,-1.7,0), ancho 4.6 y alto 1.5. Conclusión en y=-3.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:16:** Indicate de máximo global con marca de validez; poner advertencias geométricas sobre exactitud y reconstrucción, sin afirmar que el resultado del código esté mal.
- [TRIGGER_2] **00:16–00:32:** Recuperar las dos casillas 11₂=16 y 10₂=19.75. Mover el cursor global hacia 19.75 y mantener ambas entradas intactas.
- [TRIGGER_3] **00:32–00:51:** Mostrar adelanto en una curva decreciente y luego en la creciente contrafactual. Cross sobre la desigualdad w(antes)≥w(después) únicamente en el segundo panel.
- [TRIGGER_4] **00:51–01:10:** Cerrar la curva contrafactual y escribir los dos contratos de estado lado a lado. Enfatizar que comparten respuesta global pero requieren pruebas distintas.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para garantía válida; ACCENT_VINO para uso injustificado; ACCENT_CYAN para A; ACCENT_INDIGO para DP.

---

## Escena: 25

## Nombre: Construir el reloj de cada máscara

## Descripcion Breve: Quitar un bit permite precalcular todas las duraciones.

## Objetivo Pedagogico: Explicar T[M], operaciones seguras y orden topológico.

## Voz en off:

> "[TRIGGER_1] Para la versión estricta podemos preparar los tiempos de todas las máscaras una sola vez. El vacío vale cero. En cada máscara no vacía elegimos un bit encendido j, lo apagamos y añadimos su duración al tiempo de esa máscara menor. [TRIGGER_2] Con duraciones dos, tres y una para A, B y C, obtenemos los tiempos de las máscaras de cero a siete: cero, dos, tres, cinco, uno, tres, cuatro y seis. Cada suma toma una duración ya disponible. [TRIGGER_3] También podemos recorrer la tabla de ganancias en orden numérico. Añadir un bit apagado aumenta el número de la máscara; quitar uno encendido lo disminuye. Todas las dependencias apuntan en la dirección correcta, aunque la cantidad de bits no aumente fila por fila. [TRIGGER_4] El detector de un bit encendido sólo se usa sobre una máscara no vacía. Y los tiempos se suman en enteros de sesenta y cuatro bits: una máscara puede sumar veinte mil millones aunque luego resulte inviable por sus fechas."

## Descripcion Visual Detallada:

Duración orientativa: 01:15. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tabla binaria 000₂…111₂ con T=(0,2,3,5,1,3,4,6); MathTex(r"T[M]=T[M\setminus\{j\}]+c_j\quad(j\in M)"). Flechas de dependencia; selector móvil de bit; MathTex(r"2\cdot10^{10}>2^{31}-1").

## Layout y disposicion:

- Tabla de ocho columnas en x=-5.6+1.6k, k=0,…,7, y=0.7; bits arriba y T debajo. Fórmula en y=2.2, flechas de suma en y=-0.5 y nota de tipos en y=-2.5. Sólo una dependencia se ilumina a la vez.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:19:** Escribir T[000₂]=0. Encender un bit de una máscara no vacía y unir su prefijo al resultado mediante una flecha más c_j.
- [TRIGGER_2] **00:19–00:36:** Completar explícitamente: T[001]=0+2; T[010]=0+3; T[011]=3+2; T[100]=0+1; T[101]=1+2; T[110]=1+3; T[111]=4+2. Usar siempre el bit menos significativo encendido en esta traza.
- [TRIGGER_3] **00:36–00:56:** Mover el cursor de 000 a 111 y superponer una flecha de añadir y otra de retirar. Destacar que 011 precede a 100 aunque tenga más bits encendidos: el orden es numérico.
- [TRIGGER_4] **00:56–01:15:** Bloquear el selector sobre 000 y escribir que ese caso es base. Mostrar un registro de 64 bits con capacidad suficiente para la cota temporal; no representar un tiempo desbordado como un estado válido.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_TERRACOTTA para tiempos; ACCENT_CYAN para bit seleccionado; ACCENT_INDIGO para dependencia; ACCENT_VINO para operación sobre máscara vacía tachada.

---

## Escena: 26

## Nombre: La implementación como una máquina de propuestas

## Descripcion Breve: El flujo conecta máscaras, fechas, esperanza y máximo.

## Objetivo Pedagogico: Traducir la teoría a estados visibles sin bloques de código.

## Voz en off:

> "[TRIGGER_1] La máquina comienza leyendo, para cada encargo, fecha obligatoria, base, duración y los dos intervalos. Prepara los tiempos, marca el vacío como factible y deja las demás ganancias estrictas como inviables. [TRIGGER_2] El cursor visita una máscara. Si es inviable, no la extiende. Si es válida, primero compara su valor con la respuesta global y después considera cada trabajo cuyo bit sigue apagado. [TRIGGER_3] Cada propuesta pasa por cuatro estaciones: sumar la duración, comprobar la fecha, evaluar base más bono esperado y comparar con el valor de la máscara destino. El cálculo del bono distingue probabilidad uno, probabilidad cero y fracción interior. [TRIGGER_4] El código original organiza estas piezas en funciones para tiempo, ganancia y elección del último trabajo. Su marca de calculado es redundante en el recorrido actual: cada máscara se visita una sola vez. Lo esencial son las dependencias ya listas y el máximo global; el nombre de una función no convierte la iteración en recursión."

## Descripcion Visual Detallada:

Duración orientativa: 01:13. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Flujo de ocho Rectangle con Tex: datos, tiempos, máscara, factibilidad, nuevo trabajo, fecha, ganancia, máximo. Registros MathTex de M,j,t,w,DP,ans. Etiquetas Tex de las funciones originales; casilla de marca calculada separada de la ganancia.

## Layout y disposicion:

- Dos filas de cuatro tarjetas, centros x=-4.5,-1.5,1.5,4.5; y=1.2 arriba y y=-0.6 abajo, recorrido serpenteante. Cada tarjeta 2.5×0.9. Registro ans en (0,-2.6,0).

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:15:** Crear estaciones de entrada y escribir el orden d,p,c,lx,rx,ly,ry. Animar la inicialización estricta con 0 sólo en el vacío y −∞ en el resto.
- [TRIGGER_2] **00:15–00:30:** Mover un cursor a una máscara inviable y saltarla; después a una válida, leer su valor en ans y seleccionar un bit apagado.
- [TRIGGER_3] **00:30–00:48:** Transportar una ficha de propuesta por las cuatro estaciones. Una compuerta rechaza t>d; la otra ruta calcula q, luego w y finalmente un máximo, en ese orden.
- [TRIGGER_4] **00:48–01:13:** Sustituir temporalmente las estaciones por las tres funciones originales y flechas de lectura a máscaras anteriores. Atenuar la marca de calculado como redundante, sin editar ni proponer cambios de código en este documento.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_INDIGO para estado y memoria; ACCENT_CYAN para propuesta; ACCENT_VINO para rechazo; ACCENT_MINT para máximo; ACCENT_TERRACOTTA para reloj.

---

## Escena: 27

## Nombre: Contar flechas, no permutaciones

## Descripcion Breve: Cada trabajo aparece como posible extensión en la mitad de las máscaras.

## Objetivo Pedagogico: Derivar tiempo y memoria con cifras concretas de ambas implementaciones.

## Voz en off:

> "[TRIGGER_1] Tenemos dos elevado a n máscaras. Para contar las extensiones, fijemos un trabajo j. Está ausente en exactamente la mitad de los conjuntos: los otros n menos uno bits son libres. Hay dos elevado a n menos uno oportunidades para añadirlo. [TRIGGER_2] Sumando los n trabajos son n por dos elevado a n menos uno flechas potenciales. Para veinte, diez millones cuatrocientas ochenta y cinco mil setecientas sesenta. Cada flecha requiere operaciones constantes; el tiempo total es de orden n por dos elevado a n. [TRIGGER_3] El código original vuelve a recorrer los n trabajos para sumar duraciones y para elegir el último. Son dos recorridos por máscara: cuarenta y un millones novecientas cuarenta y tres mil cuarenta iteraciones con n igual a veinte. Conserva el mismo orden de complejidad, aunque haga más trabajo por máscara. [TRIGGER_4] La referencia guarda tiempos y ganancias, unos dieciséis mebibytes con un entero de ocho bytes y un double por máscara. La copia original reserva dos arreglos de doubles con dos elevado a veintiuna entradas cada uno: treinta y dos mebibytes en total. Su marca de calculado también es double; no es un arreglo de booleanos."

## Descripcion Visual Detallada:

Duración orientativa: 01:27. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- MathTex(r"n2^{n-1}=10\,485\,760\quad(n=20)"), MathTex(r"O(n2^n)"), MathTex(r"2n2^n=41\,943\,040"), MathTex(r"2\cdot2^{20}\cdot8=16\ \mathrm{MiB}"), MathTex(r"2\cdot2^{21}\cdot8=32\ \mathrm{MiB}"). Cubo de subconjuntos de tres bits para ilustrar aristas por dimensión; dos paneles de memoria.

## Layout y disposicion:

- Cubo esquemático centrado en (-3,0.4,0), ancho 5; fórmulas a derecha en x=3,y=1.6,0.3,-1. El último disparador sustituye todo por paneles de memoria en x=-3.1 y 3.1; totales en y=-2.3.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:19:** Fijar una dimensión j del cubo e iluminar sólo las máscaras con ese bit apagado; contar 2ⁿ⁻¹ y después añadirlo en cada una.
- [TRIGGER_2] **00:19–00:39:** Repetir el conteo algebraico sobre n dimensiones, sin expandir millones de nodos. Evaluar la cifra para 20 y rotular flechas potenciales, algunas descartadas por inviabilidad o fecha.
- [TRIGGER_3] **00:39–01:02:** Mostrar dos barridos de n posiciones por cada máscara del original y evaluar 2n2ⁿ. Distinguir iteraciones de bucle y transiciones efectivamente aceptadas.
- [TRIGGER_4] **01:02–01:27:** Crear los paneles de memoria con tipo, número de entradas y bytes por entrada. Convertir bytes a MiB con divisor 2²⁰; mostrar O(2ⁿ+n) de espacio y aclarar que los parámetros ocupan un añadido pequeño.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_CYAN para flechas; ACCENT_INDIGO para memoria; ACCENT_TERRACOTTA para operaciones; ACCENT_MINT para reducción frente al factorial.

---

## Escena: 28

## Nombre: Los bordes también forman parte de la solución

## Descripcion Breve: Tipos numéricos, casos imposibles y precisión completan el diseño.

## Objetivo Pedagogico: Revisar limitaciones concretas y cerrar con la idea de estado suficiente.

## Voz en off:

> "[TRIGGER_1] Si todos los trabajos tardan más de lo que permite su fecha, la mejor agenda es la vacía y la respuesta es cero. Si una entrega termina exactamente en d, es válida. Si un intervalo de importe se reduce a un punto, su media sigue siendo ese importe. [TRIGGER_2] Los tiempos requieren sesenta y cuatro bits. Las ganancias pueden sumar hasta cuarenta mil millones y contienen fracciones, por lo que usamos precisión real. Double es suficiente para la tolerancia del problema; long double es una elección conservadora. No truncamos a entero la división que calcula una probabilidad. [TRIGGER_3] El problema pide el valor esperado óptimo. Guardar predecesores para reconstruir un orden es opcional y ocupa otra tabla; con la versión estricta, cada predecesor corresponde a una transición factible. Ni el valor esperado promete un pago exacto ni el número de trabajos mide por sí solo la calidad de la agenda. [TRIGGER_4] Al principio parecían competir todas las permutaciones. El descubrimiento fue que un conjunto fija la hora desde la que miramos al futuro, y que sólo necesitamos conservar su mejor pasado. [Pausa.] En Huron Designs, aprender qué historia podemos olvidar convierte una agenda imposible de enumerar en una tabla que sí podemos recorrer."

## Descripcion Visual Detallada:

Duración orientativa: 01:33. Tiempos locales medidos desde el inicio de esta escena.

## Objetos:

- Tarjetas MathTex(r"c_i>d_i\ \forall i\Rightarrow\mathrm{OPT}=0"), MathTex(r"t=d_i\Rightarrow\text{entrega válida}"), MathTex(r"lx_i=rx_i\Rightarrow\mu_i=lx_i"), MathTex(r"\sum w_i\le4\cdot10^{10}"). Registro de probabilidad fraccionaria 3/4 frente a cero por truncamiento tachado. Árbol de órdenes que se fusiona en tabla de máscaras y frase Tex de cierre.

## Layout y disposicion:

- Casos borde en cuadrícula 2×2 con centros (±3,1.2,0),(±3,-0.3,0), ancho 5.5. Precisión y reconstrucción sustituyen la cuadrícula en sus disparadores. Cierre centrado en ORIGIN con T[S] debajo en y=-1.4 y crédito en y=-3.2.

## Secuencia de animacion:

- [TRIGGER_1] **00:00–00:22:** Revelar las tres reglas de borde con ejemplos geométricos mínimos: entrega imposible, entrega en igualdad y un importe puntual. Mantener el vacío como alternativa real de valor cero.
- [TRIGGER_2] **00:22–00:44:** Escribir cotas numéricas y mostrar 3/4=0.75 frente a la división entera truncada, tachada. Etiquetar tolerancia absoluta o relativa 10⁻⁶; no afirmar precisión decimal exacta.
- [TRIGGER_3] **00:44–01:08:** Crear flechas opcionales de predecesor sobre la tabla estricta y una leyenda de memoria adicional O(2ⁿ). Separar una tarjeta de esperanza óptima de otra de pago realizado, sin inventar un resultado concreto.
- [TRIGGER_4] **01:08–01:33:** ReplacementTransform del árbol en una tabla de máscaras; Write de la frase: Conservar el mejor pasado que comparte el mismo futuro. Mantener la pausa, luego FadeOut de diagramas y crédito del problema dentro de este disparador.

## Código Cromático y Estilo:

- Fondo `BG_COLOR`; texto principal `TEXT_MAIN`; elementos secundarios `TEXT_MUTED`. ACCENT_MINT para casos válidos y cierre; ACCENT_VINO para errores de factibilidad o truncamiento; ACCENT_INDIGO para tabla; ACCENT_TERRACOTTA para límites numéricos.

---
