# Guion Storyboard / Técnico: Diabolic Doofenshmirtz

### Convenciones de realización

- **Fuente y alcance:** exclusivamente `guion_sol.md` de la carpeta `DiabolicDoofenshmirtz`. Este documento diseña locución y animaciones; no contiene ni solicita implementación Manim, bloques de código fuente, renders ni recursos externos. Las instrucciones verbales y diagramas constituyen especificaciones para una futura implementación.
- **Duración y sincronía:** cada escena tiene cuatro triggers. Su identificador completo es escena más trigger; se reinician en1 en cada escena. Los bloques de voz son idénticos a los de `guion_voz.md`. Las ventanas de tiempo son estimaciones locales a140 palabras/minuto más pausas y holds, no timestamps de una grabación existente. El inicio de la frase marcada manda sobre el segundo estimado cuando exista locución. Cada trigger contiene un único bloque de animación sincronizado, que puede tener subpasos consecutivos detallados.
- **Lienzo:** 16:9, frame de128/9 por8 unidades; ORIGIN=(0,0,0); área segura x∈[-6.3,6.3], y∈[-3.5,3.5]. UP=(0,1,0), RIGHT=(1,0,0). Títulos en y=3.25. Si aparece contador, reservar x∈[5.1,6.3] para él y acotar título a9.5 unidades. Todas las coordenadas dadas son centros salvo indicación contraria.
- **Tipografía y texto:** todos los textos visibles, incluidas etiquetas, títulos, bits, números, mensajes y créditos, se crean con Tex o MathTex. Protocolo con Tex monoespaciado; matemáticas con MathTex. No usar Text, MarkupText, Code ni rótulos automáticos ajenos a LaTeX. NumberLine y ejes se crean sin números automáticos y se rotulan con MathTex. Títulos36–40pt, explicaciones27–30pt, ecuaciones30–36pt, índices24pt; no reducir textos esenciales por debajo de24pt: partirlos o secuenciar su aparición.
- **Paleta del proyecto ya conocida:** BG_COLOR=#181C24; TEXT_MAIN=#ECEFF4; TEXT_MUTED=#64748B; ACCENT_VINO=#C0392B; ACCENT_MINT=#2DD4BF; ACCENT_TERRACOTTA=#D97706; ACCENT_INDIGO=#6366F1; ACCENT_CYAN=#38BDF8. Usar sólo estos identificadores reales; no inventar COLOR_DANGER. Asignación persistente: tiempo/consulta en cyan, longitud y vueltas en indigo, residuo y garantías satisfechas en mint, frontera activa y conteo de vueltas en terracota. Vino señala una inferencia falsa o acción prohibida, no una respuesta útil diferente del tiempo.
- **Unidades:** t es tiempo en segundos; L y r son distancias en metros. A velocidad1m/s sus valores numéricos satisfacen t=qL+r. Se explica esta normalización en la narración antes de trabajar sólo con números. Las pistas circulares son esquemas: su radio en pantalla no codifica una longitud desconocida. Cuando se comparan longitudes por segmentos, se usa una escala lineal declarada para ese dibujo.
- **Dos ejes diferentes:** el eje de longitudes candidatas y el eje de tiempos consultados siempre llevan rótulos distintos. No transformar un intervalo de posibles L en una distancia física de Perry sin explicarlo. Para L conocido en laboratorio, punto del corredor en theta=PI/2-TAU*((t mod L)/L); salida arriba y sentido horario. Para L secreto, usar lectura digital y dominio de candidatos, sin ubicar al corredor en una fracción de vuelta que el algoritmo desconoce.
- **Laboratorios y conversación:** las escenas02,04,05,07,09,10,12 y19 contienen experimentos o ramas hipotéticas, rotulados como tales; no acumulan sus consultas en una sola conversación. La única traza principal comienza en la escena13 con contador0/42, continúa en14 y termina en15 con6 mediciones más1 respuesta. Las pruebas y comparaciones posteriores no reabren esa conversación. Las respuestas del juez no consumen mensajes del programa. Tras !42 se termina sin esperar un veredicto adicional.
- **Ritmo y continuidad:** animaciones simples0.6–1.2s; subpasos de derivación1.5–3s; resto de cada ventana para voz y lectura. [Pausa.] implica aproximadamente1.2s sin voz. No animar recorridos durante una desigualdad importante. FadeOut de elementos no conservados antes de ocupar su zona. Si dos escenas se renderizan separadas, recrear exactamente el estado heredado especificado al inicio. Las tablas largas son ayudas pedagógicas, no estructuras que el algoritmo deba almacenar.
- **Tratamiento del avance temporal:** los valores t son parámetros del problema; la animación usa tiempo pedagógico, no una escala de reproducción1:1 con t. Mostrar saltos entre mediciones sin inventar observaciones intermedias ni consumir consultas que no aparecen en el protocolo.
- **Prohibición de código en pantalla:** ninguna escena muestra C++ o Python, ni siquiera un bloque corto como sustituto del razonamiento. Las actualizaciones t←2t+1 y L←t−r son flechas entre registros o ecuaciones; el flujo se representa mediante nodos, intervalos y mensajes.

## Escena: 01
## Nombre: Un corredor que borra sus propias huellas
## Descripcion Breve: Perry recorre una pista cuya longitud permanece oculta.
## Objetivo Pedagogico: Plantear el misterio: conocer una distancia total a partir de una posición que se reinicia.
## Voz en off:
> "[TRIGGER_1] Perry corre alrededor de una pista. Siempre a la misma velocidad: un metro por segundo. Doofenshmirtz quiere saber cuánto tarda en completar una vuelta, pero hay un detalle incómodo: nadie le ha dicho cuánto mide la pista. [TRIGGER_2] Su invento puede localizar a Perry. Lo que no puede hacer es recordar las vueltas que ya terminó. Cada vez que cruza la salida, la lectura vuelve a cero. [TRIGGER_3] Imagina intentar medir un camino con un contador que borra una parte de la distancia recorrida. ¿Cómo recuperarías precisamente la parte que desapareció? [Pausa.] [TRIGGER_4] Ése es el misterio de Diabolic Doofenshmirtz, un problema del GCPC de dos mil veintidós. Vamos a resolverlo diseñando los momentos de las mediciones, hasta conseguir que una sola resta revele la vuelta completa."

## Descripcion Visual Detallada:
## Objetos:
- Circle de radio 1.65 como pista; Dot de radio 0.09 como Perry, sin asset externo; una pequeña línea radial como salida; Tex(r"	ext{Perry}") y Tex(r"	ext{Salida}").
- Panel RoundedRectangle de ancho 4.6 y alto 2.6 para medidor; Tex(r"	ext{Distancia en la vuelta actual}"); MathTex(r"L=?") y MathTex(r"v=1\ \mathrm{m/s}").
- Tex(r"	extbf{Diabolic Doofenshmirtz}") y Tex(r"	ext{GCPC 2022}").

## Layout y disposicion:
- Centro de pista C=(-3.35,0.35,0); salida en C+UP*1.65; medidor centrado en (3.0,0.35,0).
- Velocidad en (-3.35,-2.05,0); longitud desconocida en (3.0,-1.7,0); título en (0,3.25,0), ancho máximo 11.5; crédito en (0,-3.25,0).
- El círculo es un esquema, no una regla métrica: su radio no permite deducir L. No introducir marcas numéricas de longitud antes de fijar un ejemplo de laboratorio.

## Secuencia de animacion:
- Ventana total orientativa de escena: 62s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–18s: Create de pista y salida; FadeIn de Dot y rótulos. Mover al corredor en sentido horario sobre un Arc con centro C; escribir velocidad y longitud desconocida.
- [TRIGGER_2] — 18–32s: Completar una vuelta esquemática y hacer un breve destello en la salida; el medidor cambia de un valor simbólico cercano a L a cero, sin asignar todavía una longitud concreta.
- [TRIGGER_3] — 32–45s: Hacer aparecer una estela segmentada de vueltas pasadas detrás del panel y FadeOut de esa estela, manteniendo al corredor. Sostener la pregunta sin movimiento durante la pausa.
- [TRIGGER_4] — 45–62s: Write del título y crédito. Detener el corredor en la salida y conservar pista y medidor para el laboratorio siguiente; no mostrar aún la secuencia de consultas ni la fórmula final.

## Código Cromático y Estilo:
- BG_COLOR de fondo; ACCENT_INDIGO para pista; ACCENT_MINT para corredor; ACCENT_CYAN para medidor; ACCENT_TERRACOTTA para salida; TEXT_MAIN para textos y TEXT_MUTED para huellas perdidas.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 02
## Nombre: Lo que mide y lo que olvida
## Descripcion Breve: Una pista de seis metros muestra la diferencia entre tiempo total y residuo.
## Objetivo Pedagogico: Comprender el reinicio de la lectura antes de introducir el operador módulo.
## Voz en off:
> "[TRIGGER_1] Probemos primero con una pista que nosotros sí conocemos: seis metros. Este es nuestro laboratorio, no una pista cuya longitud haya recibido el algoritmo. Al comenzar, el tiempo es cero y la lectura también. [TRIGGER_2] A los dos segundos, Perry recorrió dos metros y el aparato marca dos. A los cinco segundos marca cinco. Hasta aquí, tiempo y lectura avanzan juntos. [TRIGGER_3] A los seis segundos cruza la salida. El tiempo sigue siendo seis, pero el aparato marca cero. Dos segundos después, el tiempo total es ocho y la lectura vuelve a ser dos. [TRIGGER_4] La lectura dos puede aparecer en momentos diferentes. El reloj acumula todo el recorrido; el medidor conserva sólo la distancia desde la última salida. Ésa será la diferencia que tenemos que aprender a interpretar."

## Descripcion Visual Detallada:
## Objetos:
- Pista heredada, ahora rotulada con MathTex(r"L=6\ \mathrm m") y Tex(r"	ext{Laboratorio: longitud conocida al espectador}").
- Dos registros independientes MathTex(r"t=0\ \mathrm s") y MathTex(r"r=0\ \mathrm m"); cinco parejas de lecturas (0,0),(2,2),(5,5),(6,0),(8,2) construidas con MathTex.
- Línea de tiempo NumberLine del 0 al 8, con etiquetas añadidas mediante MathTex; un puntero Triangle; Arc para el tramo de vuelta actual.

## Layout y disposicion:
- Mantener pista C=(-3.35,0.35,0), radio 1.65. Registros t y r en (3.0,1.0,0) y (3.0,-0.15,0), dentro del panel.
- Tiempo horizontal desde (-5.5,-2.55,0) hasta (5.5,-2.55,0); mapeo x=-5.5+11t/8. Etiqueta de laboratorio en y=2.55.
- Para cada instante, posición angular del corredor theta=PI/2-TAU*((t mod 6)/6); conservar dirección horaria. El salto de 5 a 6 debe alcanzar exactamente la salida, no un punto aproximado.

## Secuencia de animacion:
- Ventana total orientativa de escena: 63s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–17s: Write de la etiqueta de laboratorio y L=6; colocar corredor y puntero temporal en cero. Ambos registros muestran cero.
- [TRIGGER_2] — 17–30s: Animar t=0→2 y después 2→5; transformar registros a (2,2) y (5,5). Dibujar arco acumulado dentro de la vuelta en cada estado, sin flecha que una directamente posiciones por el interior del círculo.
- [TRIGGER_3] — 30–46s: Animar 5→6 y 6→8. En 6, retirar el arco completo y reiniciar r a cero; en 8, mostrar un tercio de vuelta y r=2. El reloj nunca retrocede.
- [TRIGGER_4] — 46–63s: TransformFromCopy de las dos lecturas r=2 a una pequeña comparación con tiempos 2 y 8. Enfatizar igualdad de residuos y diferencia de relojes. Cerrar el laboratorio sin trasladar L=6 al estado del algoritmo real.

## Código Cromático y Estilo:
- ACCENT_CYAN para t y eje temporal; ACCENT_MINT para r y arco actual; ACCENT_TERRACOTTA para cruces de salida; TEXT_MUTED para una vuelta completa ya olvidada.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 03
## Nombre: Cuarenta y dos mensajes, siempre hacia delante
## Descripcion Breve: Las restricciones convierten la medición en un problema de diseño de consultas.
## Objetivo Pedagogico: Fijar presupuesto, dominio entero y orden temporal estricto sin anticipar la estrategia.
## Voz en off:
> "[TRIGGER_1] Ahora escondemos otra vez la longitud. Sabemos que es un número entero de metros, desde uno hasta diez elevado a doce. Como Perry avanza un metro por segundo, una vuelta tarda numéricamente esa misma cantidad de segundos. [TRIGGER_2] Podemos preguntar por un instante entero. El aparato responde con la posición dentro de esa vuelta. Pero el siguiente instante tiene que ser mayor que el anterior: la máquina del tiempo se perdió. [TRIGGER_3] Además, tenemos cuarenta y dos mensajes en total. Cada medición gasta uno, y anunciar la longitud también. Por tanto, como máximo podemos gastar cuarenta y uno en medir. [TRIGGER_4] Los tiempos consultados deben ser menores que diez elevado a dieciocho. Tenemos muchísimo espacio para esperar dentro del modelo, pero muy pocas oportunidades de observar. La pregunta es cómo aprovechar cada una."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"L\in\mathbb Z,\quad1\le L\le10^{12}"); MathTex(r"0\le t<10^{18}"); MathTex(r"t_1<t_2<\cdots<t_q").
- Tex(r"	exttt{? t}") y Tex(r"	exttt{! L}") como mensajes de protocolo; dos paneles para algoritmo y medidor.
- 42 pequeños Rectangle organizados en dos filas de 21, más Brace y MathTex(r"q+1\le42"); la ficha de respuesta se distingue sin consumirla.

## Layout y disposicion:
- Límites de longitud en (0,2.0,0); algoritmo en (-4.6,0.5,0), medidor en (4.6,0.5,0), corredor de mensajes centrado en y=0.5.
- Orden temporal en (0,-0.8,0). Presupuesto en y=-1.9 y -2.25; centros x=-5.0+0.5j para j=0,...,20; fichas 0.28 por 0.20.
- Límite de tiempos y presupuesto numérico en y=-3.05, divididos en dos paneles de ancho 5.6. No intentar rotular cada una de las 42 fichas.

## Secuencia de animacion:
- Ventana total orientativa de escena: 64s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–18s: FadeOut del laboratorio y Write del intervalo de L; escribir explícitamente la unidad antes de pasar a cantidades numéricas en las escenas posteriores.
- [TRIGGER_2] — 18–34s: Enviar un mensaje simbólico ? t de izquierda a derecha; mostrar una flecha temporal sólo hacia la derecha y escribir la desigualdad estricta. Un candado gráfico impide volver hacia un instante ya usado.
- [TRIGGER_3] — 34–48s: Crear 42 fichas y distinguir una como respuesta final; escribir q+1≤42. Mostrar que quedan como máximo 41 para consultas, sin gastar ninguna.
- [TRIGGER_4] — 48–64s: Write de t<10^18 y comparar visualmente una línea temporal larga con pocas fichas de observación. La escala temporal es esquemática: no representa segundos reales de reproducción.

## Código Cromático y Estilo:
- ACCENT_CYAN para tiempo y consultas; ACCENT_TERRACOTTA para respuesta reservada; ACCENT_INDIGO para dominio; ACCENT_VINO sólo para movimiento temporal prohibido; TEXT_MAIN para reglas.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 04
## Nombre: La paciencia no alcanza
## Descripcion Breve: Consultar cada segundo resuelve una pista pequeña, pero agota el presupuesto en el caso grande.
## Objetivo Pedagogico: Motivar el salto entre consultas y distinguir pocas operaciones de grandes tiempos consultados.
## Voz en off:
> "[TRIGGER_1] La primera idea es medir en uno, dos, tres, cuatro… hasta que la lectura llegue a cero. Si observamos cada segundo, ese primer cero positivo ocurre justo al completar la primera vuelta. [TRIGGER_2] En una pista de seis metros, las lecturas serían uno, dos, tres, cuatro, cinco y cero. Funciona: seis mediciones y el mensaje final. [TRIGGER_3] Pero si la pista mide diez elevado a doce, necesitamos diez elevado a doce mediciones. El problema no es escribir un tiempo grande. El problema es gastar una pregunta por cada segundo. [TRIGGER_4] Necesitamos saltar. La tentación sería irnos a un instante enorme y medir allí. [Pausa.] ¿Conocer una posición muy lejos en el tiempo nos revela automáticamente cuánto mide una vuelta?"

## Descripcion Visual Detallada:
## Objetos:
- VGroup de seis celdas de tiempo MathTex 1,...,6 y seis lecturas MathTex 1,2,3,4,5,0; rótulo MathTex(r"	ext{Laboratorio: }L=6").
- MathTex(r"q=L"); MathTex(r"10^{12}\gg41"); un contador de consultas independiente del reloj.
- NumberLine conceptual con posiciones de consulta discretas y una Arrow larga hacia un marcador futuro; Tex(r"	ext{Saltar en el tiempo}").

## Layout y disposicion:
- Fila de tiempos en y=1.5 y residuos en y=0.6, centros x=-3.75+1.5j para j=0,...,5; etiquetas t,r a x=-5.6.
- Cuenta q=L en y=-0.4 y contraste con presupuesto en y=-1.3. Eje de salto desde x=-5.5 a 5.5, y=-2.55.
- No dibujar billones de marcas ni aumentar la tasa de cuadros para simularlas: representar la fórmula del conteo exacto y una banda que rebasa la capacidad 41.

## Secuencia de animacion:
- Ventana total orientativa de escena: 59s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–16s: Crear seis instantes consecutivos; mover puntero una posición por medición para mostrar el costo de cada consulta.
- [TRIGGER_2] — 16–28s: Revelar lecturas una a una, terminando con 0 en t=6; unir ese instante con L=6. Señalar que consultar t=0 no sería este primer cero positivo.
- [TRIGGER_3] — 28–44s: Transform de la cuenta seis hacia q=L y después al caso L=10^12; la banda de consumo rebasa el presupuesto y se marca en vino.
- [TRIGGER_4] — 44–59s: Retirar las consultas intermedias y dejar una flecha hacia un instante remoto. Mantener la pregunta de la voz durante la pausa; no mostrar todavía el valor de la longitud.

## Código Cromático y Estilo:
- ACCENT_VINO para cantidad de consultas inviable; ACCENT_CYAN para tiempo; ACCENT_MINT para la estrategia válida en el ejemplo pequeño; ACCENT_TERRACOTTA para salto propuesto.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 05
## Nombre: La trampa de una medición lejana
## Descripcion Breve: Una misma respuesta en t=20 es compatible con varias longitudes.
## Objetivo Pedagogico: Probar que t−r puede ser varias vueltas y que una consulta aislada puede ser ambigua.
## Voz en off:
> "[TRIGGER_1] Volvamos al laboratorio de seis metros. Preguntamos en el segundo veinte. Perry completó tres vueltas, que suman dieciocho metros, y avanzó dos metros más. El aparato responde dos. [TRIGGER_2] Si restamos veinte menos dos obtenemos dieciocho. Pero la pista no mide dieciocho: mide seis. La resta recuperó tres vueltas juntas. [TRIGGER_3] Y el mismo mensaje puede engañarnos de más de una manera. Una pista de tres, de nueve o de dieciocho metros también devolvería dos al consultar veinte. Cambia cuántas vueltas caben, pero no el sobrante. [TRIGGER_4] Así que la resta contiene información valiosa: una cantidad entera de vueltas. Lo que nos falta es controlar cuántas. ¿Podemos elegir la medición para que esa cantidad sea exactamente una?"

## Descripcion Visual Detallada:
## Objetos:
- Recta desplegada de recorrido 0–20; tres bloques de ancho correspondiente a 6 y un bloque residual de 2; MathTex(r"20=3\cdot6+2").
- MathTex(r"t-r=20-2=18=3L"); tres filas alternativas MathTex(r"20=6\cdot3+2"), MathTex(r"20=2\cdot9+2"), MathTex(r"20=1\cdot18+2").
- Cuatro tarjetas de candidatos MathTex(r"L=3"), MathTex(r"L=6"), MathTex(r"L=9"), MathTex(r"L=18"); MathTex(r"	ext{La misma respuesta: }r=2").

## Layout y disposicion:
- Bloques del ejemplo L=6 en x∈[-5.5,5.5], y=1.3; escala 11/20 por unidad; longitudes gráficas 3.3,3.3,3.3,1.1.
- Ecuación de la resta en y=0.1. Alternativas en y=-0.9,-1.65,-2.4, alineadas por el signo igual; candidatos al lado derecho sólo si quedan dentro de x<=6.2.
- Mostrar como máximo una fila de bloques físicos y tres ecuaciones: no encoger cuatro pistas completas en un solo cuadro.

## Secuencia de animacion:
- Ventana total orientativa de escena: 57s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–14s: Create de tres bloques de vuelta y un residual; animar un puntero hasta 20; revelar únicamente el bloque final como lectura 2.
- [TRIGGER_2] — 14–25s: FadeOut visual del residuo mediante una copia, sin borrar el original; Brace sobre los tres bloques restantes y escribir 18=3L. Señalar el error de llamar L a esa cantidad.
- [TRIGGER_3] — 25–42s: Revelar explícitamente las tres descomposiciones alternativas y las cuatro longitudes candidatas. Mantener r=2 en el mismo lugar para mostrar que la salida no distingue entre ellas.
- [TRIGGER_4] — 42–57s: Circumscribe del multiplicador 3 y reemplazarlo en una expresión genérica por q. Abrir un espacio visual para el objetivo q=1, todavía como pregunta y no como algoritmo.

## Código Cromático y Estilo:
- ACCENT_INDIGO para vueltas completas; ACCENT_MINT para resto; ACCENT_TERRACOTTA para número de vueltas; ACCENT_VINO para identificación falsa de 18 con L.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 06
## Nombre: Dos respuestas con significados distintos
## Descripcion Breve: La división en vueltas completas y resto explica las condiciones r=t y r<t.
## Objetivo Pedagogico: Derivar el modelo módulo y los dos casos que alimentarán el algoritmo.
## Voz en off:
> "[TRIGGER_1] Podemos describir cualquier recorrido con dos piezas: vueltas completas y el tramo que sobra. Si llamamos L a la longitud, t es una cantidad entera de vueltas de L, más un resto r menor que L. [TRIGGER_2] Antes de completar la primera vuelta no hay nada que descontar. Por eso el aparato devuelve exactamente el tiempo consultado: r es igual a t. Esa igualdad nos dice que L es mayor que t. [TRIGGER_3] Si la lectura es menor que el tiempo, ya hubo al menos una vuelta. Entonces L es menor o igual que t, pero la diferencia todavía podría reunir una, dos o muchas vueltas. [TRIGGER_4] Ésas son nuestras dos señales. Igualdad significa que aún falta pista. Diferencia significa que ya cruzamos la salida. El próximo paso será hacer que esa segunda señal también nos diga cuánto mide L."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"t=qL+r,\quad q=\lfloor t/Lfloor,\quad0\le r<L"); MathTex(r"r=tmod L").
- Dos paneles de estados con MathTex(r"r=t\iff t<L") y MathTex(r"r<t\iff L\le t"); bloques vacíos o completos para representar q=0 y q>=1.
- MathTex(r"t-r=qL"); Tex(r"	ext{Todavía no hay una vuelta}") y Tex(r"	ext{Al menos una vuelta}").

## Layout y disposicion:
- Descomposición general en y=2.1, ancho máximo 11.7; nombre módulo en y=1.3.
- Paneles de ancho 5.4 y alto 2.6 centrados en (-3.05,-0.5,0) y (3.05,-0.5,0). Ecuaciones principales en y=-0.2; interpretación en y=-1.05.
- Diferencia t-r=qL en y=-2.65. Mantener separadas las magnitudes: t se expresa numéricamente en segundos y r,L en metros; v=1 permite comparar sus valores numéricos.

## Secuencia de animacion:
- Ventana total orientativa de escena: 66s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–17s: Construir q bloques de longitud simbólica L y uno residual antes de escribir la ecuación. Añadir el límite r<L y el piso como conteo de vueltas completas, no como una operación misteriosa.
- [TRIGGER_2] — 17–34s: En el panel izquierdo retirar todos los bloques completos; transformar t=0·L+r en t=r y deducir t<L a partir de r<L.
- [TRIGGER_3] — 34–50s: En el panel derecho mostrar q>=1 y una Brace sobre al menos un bloque; derivar t>=L y r<t, dado L>0. Mantener q variable.
- [TRIGGER_4] — 50–66s: Indicate alternado de ambas señales; copiar t-r=qL al centro como pregunta pendiente sobre q. Terminar con los dos casos visibles sin sugerir todavía que toda diferencia sea L.

## Código Cromático y Estilo:
- ACCENT_CYAN para t; ACCENT_MINT para r; ACCENT_INDIGO para L; ACCENT_TERRACOTTA para q; TEXT_MAIN para equivalencias. Ambos casos son información útil, no éxito/fallo rojo-verde.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 07
## Nombre: Por qué no podemos buscar hacia atrás
## Descripcion Breve: Una búsqueda binaria convencional propone una consulta en un instante ya pasado.
## Objetivo Pedagogico: Identificar la restricción que impide aplicar sin cambios una herramienta familiar.
## Voz en off:
> "[TRIGGER_1] Saber si t es menor que L suena a búsqueda binaria. Preguntamos por un punto intermedio y decidimos qué mitad conservar. Una idea muy razonable… si pudiéramos consultar cualquier instante en cualquier orden. [TRIGGER_2] Por ejemplo, imaginemos longitudes entre uno y cien. Consultamos cincuenta y sabemos que la vuelta ya ocurrió. La búsqueda convencional querría volver a un instante menor, como veinticinco. [TRIGGER_3] Pero acabamos de consultar cincuenta. Veinticinco ya no es una pregunta legal. Podemos reducir nuestra incertidumbre, pero no podemos retroceder nuestro próximo tiempo. [TRIGGER_4] Necesitamos una estrategia que aprenda mientras avanza. No vamos a encerrar la respuesta saltando a ambos lados. Vamos a acercarnos desde abajo y cuidar cuánto nos pasamos cuando la crucemos."

## Descripcion Visual Detallada:
## Objetos:
- Eje de candidatos L de 1 a 100 con etiquetas MathTex; marcador de consulta t=50; banda restante [1,50].
- Segundo eje de tiempos consultables con una zona bloqueada t<=50; marcador propuesto 25 y Arrow hacia la izquierda.
- Tex(r"	ext{Búsqueda binaria convencional}"); MathTex(r"	ext{Consultas futuras: }t>50"); flecha de avance a la derecha.

## Layout y disposicion:
- Eje de longitudes candidatas de x=-5.5 a 5.5 en y=1.25; eje temporal separado en y=-1.05, con la misma escala sólo en este ejemplo.
- Encabezados Tex encima de cada eje, para no confundir longitud desconocida y tiempo elegido.
- Propuesta t=25 en (-2.85,-1.05,0) y consulta 50 en (-0.05,-1.05,0) con mapeo x=-5.5+11*(valor-1)/99; aviso en y=-2.45.

## Secuencia de animacion:
- Ventana total orientativa de escena: 57s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–16s: Mostrar eje superior y selección intermedia. No hacer aparecer una fórmula de búsqueda binaria ni código.
- [TRIGGER_2] — 16–30s: Marcar t=50 y una respuesta simbólica r<50; sombrear candidatas L<=50. Desplazar una copia de puntero hacia 25 como propuesta, sin enviarla al juez.
- [TRIGGER_3] — 30–42s: En el eje inferior, crear zona temporal prohibida hasta 50 y bloquear la copia en 25 con Cross. Subrayar que la violación es de protocolo, no un error de aritmética.
- [TRIGGER_4] — 42–57s: FadeOut de propuesta y Cross; trazar una nueva flecha a tiempos mayores y mantener una banda inferior de longitudes que irá creciendo en escenas posteriores. No afirmar que toda técnica binaria posible es imposible: se descarta este uso convencional.

## Código Cromático y Estilo:
- ACCENT_INDIGO para candidatos L; ACCENT_CYAN para tiempo; ACCENT_VINO para consulta prohibida; ACCENT_TERRACOTTA para límite aprendido.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 08
## Nombre: La ventana de una sola vuelta
## Descripcion Breve: El intervalo entre L y 2L permite recuperar L con una resta.
## Objetivo Pedagogico: Derivar visualmente la condición suficiente, incluyendo ambos extremos.
## Voz en off:
> "[TRIGGER_1] Volvamos al recorrido desplegado. Hay una región especial: desde el final de la primera vuelta hasta antes del final de la segunda. Si medimos ahí, sabemos que el contador olvidó exactamente una vuelta. [TRIGGER_2] En esa ventana, el tiempo total es una L completa más el resto que nos devuelve el aparato. Entonces L es t menos r. Ahora la resta sí significa una vuelta, porque ya controlamos el multiplicador. [TRIGGER_3] El borde izquierdo se puede incluir. Si preguntamos justo en L, la lectura es cero y la resta devuelve L. El borde derecho no: en dos L la lectura también es cero, pero la resta devuelve dos vueltas. [TRIGGER_4] Así aparece nuestro verdadero objetivo: encontrar un instante que sea al menos L y estrictamente menor que dos L. Parece circular, porque aún no conocemos L. Pero una respuesta anterior puede darnos justo la información que falta."

## Descripcion Visual Detallada:
## Objetos:
- Línea de recorrido con marcas 0,L,2L,3L, añadidas con MathTex; banda Rectangle para [L,2L). Dot relleno en L y Circle sin relleno en 2L.
- MathTex(r"L\le t<2L"); MathTex(r"t=L+r\quad\Longrightarrow\quad L=t-r").
- Dos fichas de borde MathTex(r"t=L\Rightarrow r=0,\ t-r=L") y MathTex(r"t=2L\Rightarrow r=0,\ t-r=2L").

## Layout y disposicion:
- Mapeo simbólico x= -5.4+3.6*(distancia/L); marcas 0,-5.4; L,-1.8; 2L,1.8; 3L,5.4 en y=0.7.
- Banda de ventana y=0.7, alto 0.5; etiqueta intervalo en y=1.7. Descomposición de t en y=-0.4.
- Fichas de extremos en (-3.1,-1.85,0) y (3.1,-1.85,0), ancho máximo 5.5. Pregunta pendiente sobre encontrar t en y=-2.9.

## Secuencia de animacion:
- Ventana total orientativa de escena: 69s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–16s: Desplegar dos vueltas como segmentos adyacentes; iluminar sólo la segunda franja temporal, entre L y 2L. Colocar t dentro de ella.
- [TRIGGER_2] — 16–33s: Brace desde 0 a L y otra desde L a t; etiquetar L y r. TransformMatchingTex de t=L+r hacia L=t-r, conservando colores semánticos.
- [TRIGGER_3] — 33–51s: Mover t al borde L y mostrar el primer caso; después al borde 2L y mostrar el segundo. Marcar punto izquierdo cerrado y derecho abierto de manera explícita; no usar una banda que sugiera ambos incluidos.
- [TRIGGER_4] — 51–69s: Recuperar t en el interior y escribir el intervalo. Oscurecer las etiquetas numéricas desconocidas y hacer aparecer un registro de la medición anterior: pista del próximo razonamiento.

## Código Cromático y Estilo:
- ACCENT_MINT para ventana correcta; ACCENT_INDIGO para L; ACCENT_CYAN para t; ACCENT_TERRACOTTA para extremos; ACCENT_VINO sólo en incluir incorrectamente 2L.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 09
## Nombre: Una respuesta que parece no decir nada
## Descripcion Breve: La igualdad en el tiempo siete excluye todas las longitudes de uno a siete.
## Objetivo Pedagogico: Convertir r=u en la cota entera L>=u+1.
## Voz en off:
> "[TRIGGER_1] Supongamos que nuestra última consulta fue en siete y el aparato respondió siete. Parece que no pasó nada. Pero esa igualdad descarta todas las pistas que ya habrían dado una vuelta para entonces. [TRIGGER_2] La longitud no puede ser uno, dos, tres, cuatro, cinco, seis ni siete. Tiene que ser mayor que siete. Y como es entera, la menor posibilidad que queda es ocho. [TRIGGER_3] Esa pista de ocho metros será nuestro caso más exigente para evitar dos vueltas. Cualquier pista más larga tarda todavía más en completar la segunda. [TRIGGER_4] En general, si preguntamos en u y recibimos u, sabemos que L es al menos u más uno. No hemos encontrado la longitud, pero ganamos una frontera desde la cual diseñar la próxima pregunta."

## Descripcion Visual Detallada:
## Objetos:
- Registros MathTex(r"u=7") y MathTex(r"r=7"); tarjetas de longitudes 1–12 con MathTex, más una flecha indicando continuidad del dominio.
- Cross sobre candidatas 1–7; MathTex(r"L>7\Rightarrow L\ge8"); un marco sobre tarjeta 8.
- MathTex(r"r(u)=u\Rightarrow L>u\Rightarrow L\ge u+1"); Tex(r"	ext{Menor longitud todavía posible}").

## Layout y disposicion:
- Registros en (-2.5,2.0,0) y (2.5,2.0,0). Tarjetas en dos filas de seis, x=-4.75+1.9j; fila 1–6 en y=0.9 y 7–12 en y=-0.1.
- Marco sobre 8 en (-2.85,-0.1,0). Frontera concreta en y=-1.2; fórmula general en y=-2.4.
- La flecha después de 12 no significa un límite superior nuevo; rotular con MathTex(r"\ldots,10^{12}") en un pequeño panel separado.

## Secuencia de animacion:
- Ventana total orientativa de escena: 61s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–16s: Leer ? 7 y respuesta 7 en un experimento independiente. Mostrar las candidatas sin revelar la longitud real.
- [TRIGGER_2] — 16–31s: Aplicar Cross a cada una de las siete primeras candidatas explícitamente; encerrar 8 y escribir L>7→L≥8. La inclusión de 8 depende de integridad, señalarlo con MathTex(r"L\in\mathbb Z").
- [TRIGGER_3] — 31–44s: TransformFromCopy de tarjeta 8 a una pista mínima esquemática; otras pistas se dibujan más largas como segmentos, mostrando que su segunda meta queda más lejos.
- [TRIGGER_4] — 44–61s: TransformMatchingTex de 7 y 8 hacia u y u+1. Mantener visible el registro de igualdad como premisa, no presentar la cota sin su condición.

## Código Cromático y Estilo:
- ACCENT_VINO para candidatos descartados; ACCENT_TERRACOTTA para mínimo restante; ACCENT_INDIGO para dominio; ACCENT_CYAN para medición; TEXT_MAIN para implicaciones.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 10
## Nombre: Quince es seguro; dieciséis, no siempre
## Descripcion Breve: La pista mínima de ocho metros determina el último instante anterior a una segunda vuelta.
## Objetivo Pedagogico: Comprender geométricamente por qué la siguiente consulta debe ser como máximo 2u+1.
## Voz en off:
> "[TRIGGER_1] Si la menor pista posible mide ocho, su segunda vuelta termina en dieciséis. Para estar seguros de no completar dos vueltas, tenemos que preguntar antes de dieciséis. El mayor instante entero permitido por esa condición es quince. [TRIGGER_2] Imagina primero que la pista sí mide ocho. En quince, la lectura sería siete. Quince menos siete recupera ocho: exactamente una vuelta. [TRIGGER_3] Si saltáramos hasta dieciséis, esa misma pista devolvería cero. La resta daría dieciséis y nos haría confundir dos vueltas con una. Un solo segundo extra rompe nuestra garantía. [TRIGGER_4] ¿Y si la pista mide más de quince? Entonces en quince todavía no hay una vuelta, y el aparato responde quince. Tampoco perdemos: esa respuesta nos permite elevar otra vez la frontera inferior."

## Descripcion Visual Detallada:
## Objetos:
- Recta de tiempo con marcas 7,8,15,16; dos vueltas de la pista mínima L=8; punto abierto de seguridad en 16 y punto candidato en 15.
- MathTex(r"L=8:\quad15mod8=7,\quad15-7=8"); MathTex(r"16mod8=0,\quad16-0=16
e8").
- Panel alternativo MathTex(r"L>15:\quad r(15)=15\Rightarrow L\ge16"); rótulos Tex(r"	ext{Prueba de seguridad}") y Tex(r"	ext{Nueva información}").

## Layout y disposicion:
- Recta del 0 al 16 desde x=-5.6 hasta x=5.6, y=1.0; mapeo x=-5.6+0.7t; ancho de cada vuelta 5.6.
- Comparación t=15 y t=16 en y=-0.35 y -1.30, ancho máximo 11.5. Alternativa de pista larga en y=-2.45.
- El marcador 15 en x=4.9 y 16 en x=5.6 deben tener sus etiquetas en diferentes alturas para evitar colisión. El punto 16 abierto representa límite estricto.

## Secuencia de animacion:
- Ventana total orientativa de escena: 59s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–18s: Construir pista mínima de dos segmentos; indicar segundo final en 16 y desplazar puntero al último entero anterior, 15.
- [TRIGGER_2] — 18–29s: En laboratorio L=8, mostrar una vuelta completa de 8 y residuo 7; escribir ambos resultados de la primera ecuación.
- [TRIGGER_3] — 29–43s: Mover una copia del puntero a 16, colorear dos bloques completos y residuo cero. Mostrar la falsa resta y Cross sobre la identificación con 8. No enviar esa consulta dentro de la estrategia real.
- [TRIGGER_4] — 43–59s: Cambiar a una pista de longitud simbólica mayor que 15; el puntero sigue antes de la primera meta. Escribir r=15 y nueva cota L≥16. Terminar con ambos resultados útiles de medir en 15, no con la consulta insegura.

## Código Cromático y Estilo:
- ACCENT_MINT para 15 seguro; ACCENT_VINO para el caso que rompe la garantía en 16; ACCENT_TERRACOTTA para frontera; ACCENT_CYAN para tiempo.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 11
## Nombre: Diseñar el salto, no adivinarlo
## Descripcion Breve: La cota L>=u+1 produce algebraicamente t=2u+1 y sus dos salidas posibles.
## Objetivo Pedagogico: Derivar la regla y demostrar que es el salto máximo bajo la garantía de menos de dos vueltas.
## Voz en off:
> "[TRIGGER_1] El mismo razonamiento funciona sin elegir números concretos. Tras una respuesta igual a u, la menor longitud posible es u más uno. Su segunda vuelta termina en dos veces la suma de u y uno; es decir, dos u más dos. [TRIGGER_2] Queremos quedarnos estrictamente antes de ese punto. Como los tiempos son enteros, el mayor que podemos elegir es dos u más uno. Ésa será nuestra siguiente consulta. [TRIGGER_3] Para cualquier longitud que siga siendo posible, ese tiempo cumple: dos u más uno es menor que el doble de la suma de u y uno, y esa cantidad es menor o igual que dos L. Por tanto, no podemos haber completado dos vueltas. [TRIGGER_4] Si aún no completamos ninguna, la respuesta vuelve a ser el propio tiempo y aprendemos una cota mejor. Si completamos alguna, tiene que ser exactamente una y la resta termina el problema. Ésa es toda la bifurcación."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"L\ge u+1"); MathTex(r"2L\ge2(u+1)=2u+2"); MathTex(r"t_{\mathrm{siguiente}}=2u+1").
- MathTex(r"t=2u+1<2(u+1)\le2L"); tres segmentos horizontales que representan t,2(u+1),2L.
- Diagrama de dos ramas: MathTex(r"r=t\Rightarrow L\ge t+1") y MathTex(r"r<t\Rightarrow L=t-r"); nodo central MathTex(r"	ext{Preguntar en }t").

## Layout y disposicion:
- Premisa en y=2.25, segunda meta mínima en y=1.45 y candidato t en y=0.65.
- Cadena de desigualdades en y=-0.2, ancho máximo 11.7; diagrama inferior con nodo en (0,-1.25,0), hojas en (-3.2,-2.4,0) y (3.2,-2.4,0).
- Segmentos visuales se muestran a la izquierda de la fórmula sólo durante su derivación; retirarlos antes de desplegar las ramas para no saturar.

## Secuencia de animacion:
- Ventana total orientativa de escena: 73s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–20s: TransformFromCopy de la cota hacia dos veces la longitud mínima; distribuir visualmente el factor dos sobre u y 1. Subrayar los paréntesis para distinguir 2(u+1) de 2u+1.
- [TRIGGER_2] — 20–34s: Retroceder una unidad desde la segunda meta mínima y escribir t=2u+1. Mostrar que 2u+2 permitiría dos vueltas cuando L=u+1; la maximización es bajo esta garantía, no una afirmación de optimalidad global entre todos los algoritmos.
- [TRIGGER_3] — 34–55s: Write secuencial de cada relación de la cadena t<2(u+1)≤2L; cada símbolo se conecta con la premisa que lo justifica. No sustituir < por ≤ en el primer paso.
- [TRIGGER_4] — 55–73s: Create de las dos ramas. En la izquierda, transportar una nueva cota al registro de conocimiento; en la derecha, transportar t-r al panel respuesta. Mantener ambas hojas como salidas exhaustivas, con q=0 y q=1 respectivamente.

## Código Cromático y Estilo:
- ACCENT_TERRACOTTA para u y frontera entera; ACCENT_CYAN para t; ACCENT_INDIGO para L; ACCENT_MINT para seguridad demostrada y ambas salidas útiles.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 12
## Nombre: La primera pregunta y la escalera
## Descripcion Breve: La longitud mínima uno permite iniciar en t=1 y construir los primeros cinco tiempos.
## Objetivo Pedagogico: Explicar la base del algoritmo y generar la secuencia mediante la misma regla.
## Voz en off:
> "[TRIGGER_1] Nos falta arrancar. Antes de medir nada sabemos que la longitud es al menos uno. Así que preguntamos en uno, que está estrictamente antes de dos veces cualquier longitud posible. [TRIGGER_2] Si la respuesta es cero, la pista mide uno y terminamos. Si responde uno, sabemos que la longitud es al menos dos; la siguiente consulta puede ser tres. [TRIGGER_3] Si tres responde tres, la longitud es al menos cuatro y consultamos siete. Si siete responde siete, la longitud es al menos ocho y consultamos quince. [TRIGGER_4] Si quince responde quince, la longitud es al menos dieciséis y consultamos treinta y uno. La escalera uno, tres, siete, quince, treinta y uno no viene de una ocurrencia: cada peldaño es el mayor salto que conserva nuestra garantía."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"L\ge1\Rightarrow1<2L"); nodo inicial MathTex(r"t=1"); dos respuestas posibles MathTex(r"r=0") y MathTex(r"r=1").
- Cinco tarjetas de tiempo MathTex 1,3,7,15,31; cuatro flechas con MathTex(r"2\cdot1+1"), MathTex(r"2\cdot3+1"), MathTex(r"2\cdot7+1"), MathTex(r"2\cdot15+1").
- Cuatro cotas MathTex(r"L\ge2"), MathTex(r"L\ge4"), MathTex(r"L\ge8"), MathTex(r"L\ge16"); Tex(r"	ext{Cada avance supone una respuesta igual al tiempo}").

## Layout y disposicion:
- Base en y=2.15 y nodo t=1 en (-5.0,0.75,0). Escalera de tiempos con x=-5.0+2.5j y y=0.75 para j=0,...,4.
- Flechas y expresiones en y=1.25 y 1.6, usando tamaño 25–27; cotas bajo cada destino en y=0.
- Rama de terminación para L=1 en (-4.7,-1.35,0); aviso condicional en (1.0,-2.45,0), ancho máximo 9.5. Retirar la rama inicial cuando la escalera ocupe todo el ancho.

## Secuencia de animacion:
- Ventana total orientativa de escena: 61s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–15s: Write de la premisa L≥1 y conexión al tiempo inicial 1; excluir consultar 0 con una breve ficha r(0)=0 para toda L, sin añadirlo al conteo de la estrategia.
- [TRIGGER_2] — 15–29s: Abrir las dos ramas iniciales: r=0 lleva a ! 1; r=1 construye L≥2 y después la tarjeta 3 mediante 2·1+1.
- [TRIGGER_3] — 29–42s: Construir explícitamente 3→7 con cota 4 y 7→15 con cota 8; no encadenar consultas si la respuesta no fuera igual al tiempo.
- [TRIGGER_4] — 42–61s: Construir 15→31 con cota 16; resaltar la regla compartida en las cuatro flechas. Mantener la escalera completa como anticipación de una traza real, sin añadir puntos suspensivos en lugar de explicar estos pasos.

## Código Cromático y Estilo:
- ACCENT_CYAN para tiempos; ACCENT_TERRACOTTA para cotas aprendidas; ACCENT_MINT para salida correcta; ACCENT_INDIGO para conexiones de regla.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 13
## Nombre: Una pista oculta: tres preguntas
## Descripcion Breve: Comienza una conversación completa con consultas en 1, 3 y 7.
## Objetivo Pedagogico: Seguir el estado del algoritmo sin usar la longitud secreta para elegir tiempos.
## Voz en off:
> "[TRIGGER_1] Vamos a probarlo con una pista cuya longitud no revelaremos todavía. Reiniciamos el contador. Primera pregunta: uno. El aparato responde uno. Sabemos que L es al menos dos; elegimos tres. [TRIGGER_2] Segunda pregunta: tres. La respuesta vuelve a ser tres. Ahora L es al menos cuatro; el siguiente instante será siete. [TRIGGER_3] Tercera pregunta: siete. Recibimos siete. Actualizamos la frontera a ocho y elegimos quince. No hemos medido en dos, cuatro, cinco ni seis: esas observaciones no eran necesarias. [TRIGGER_4] Cada respuesta que coincide con el tiempo parece repetitiva, pero está haciendo un trabajo concreto: descarta un tramo de longitudes y autoriza un salto mayor. Hasta ahora sólo usamos tres mediciones."

## Descripcion Visual Detallada:
## Objetos:
- Panel opaco de pista secreta Tex(r"L=?"); dos registros MathTex t y r; tabla de historia de tres filas con columnas consulta, respuesta, cota siguiente.
- Mensajes Tex(r"	exttt{? 1}"), Tex(r"	exttt{? 3}"), Tex(r"	exttt{? 7}"); respuestas MathTex 1,3,7; cotas MathTex(r"L\ge2"), MathTex(r"L\ge4"), MathTex(r"L\ge8").
- Contador MathTex(r"0/42") que avanza hasta 3/42; puntero de siguiente tiempo 3→7→15; Tex(r"	ext{Traza principal: longitud aún oculta}").

## Layout y disposicion:
- Panel secreto en (-4.75,1.4,0), ancho 2.5; registros en (0,1.4,0) y (3.8,1.4,0).
- Tabla desde x=-4.8 a 4.8, cabeceras en y=0.3, filas en y=-0.4,-1.1,-1.8; columnas x=-3.6,0,3.6.
- Contador en (5.7,3.25,0), con título de ancho máximo 9.5 alineado a (-1.3,3.25,0). Siguiente tiempo en y=-2.75. No dibujar posición real del corredor en un círculo: su fracción de vuelta todavía es desconocida.

## Secuencia de animacion:
- Ventana total orientativa de escena: 55s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–15s: Limpiar experimentos previos y mostrar contador 0/42. Enviar ? 1, incrementar a 1/42; recibir 1; registrar la primera fila (1,1,L≥2) y calcular siguiente=3.
- [TRIGGER_2] — 15–26s: Enviar ? 3, contador 2/42; recibir 3; añadir fila (3,3,L≥4), sin alterar ni reinterpretar la respuesta previa. Siguiente=7.
- [TRIGGER_3] — 26–40s: Enviar ? 7, contador 3/42; recibir 7; añadir fila (7,7,L≥8). Siguiente=15. Sobre un eje auxiliar mostrar los tiempos saltados en opacidad baja, sin contarlos como mensajes.
- [TRIGGER_4] — 40–55s: Indicate de la columna de cotas y de las tres fichas consumidas. La tabla es una ayuda visual, no memoria requerida por el algoritmo. Conservar las tres filas para la escena siguiente.

## Código Cromático y Estilo:
- ACCENT_CYAN para consulta; ACCENT_MINT para respuestas exactas; ACCENT_TERRACOTTA para cotas; ACCENT_INDIGO para panel secreto; TEXT_MUTED para tiempos no consultados.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 14
## Nombre: El instante en que los números se separan
## Descripcion Breve: Las consultas 15, 31 y 63 completan la traza; la última responde 21.
## Objetivo Pedagogico: Detectar el primer residuo distinto y usar la cota previa antes de calcular.
## Voz en off:
> "[TRIGGER_1] Cuarta pregunta: quince. La respuesta es quince. La longitud es al menos dieciséis, y avanzamos a treinta y uno. [TRIGGER_2] Quinta pregunta: treinta y uno. La respuesta también es treinta y uno. Ahora sabemos algo decisivo: la longitud es al menos treinta y dos. Elegimos sesenta y tres. [TRIGGER_3] Sexta pregunta: sesenta y tres. Esta vez el aparato responde veintiuno. [Pausa.] Los números se separaron. Ya hubo una vuelta. [TRIGGER_4] ¿Pudieron ser dos? No. Incluso la pista más corta que seguía siendo posible, de treinta y dos metros, termina su segunda vuelta en sesenta y cuatro. Nosotros medimos en sesenta y tres. Así que hubo una vuelta, y solamente una."

## Descripcion Visual Detallada:
## Objetos:
- Tabla completa de seis filas, manteniendo primeras tres: (1,1,2),(3,3,4),(7,7,8),(15,15,16),(31,31,32),(63,21,intervalo).
- Mensajes Tex(r"	exttt{? 15}"), Tex(r"	exttt{? 31}"), Tex(r"	exttt{? 63}"); respuestas MathTex 15,31,21; contador 4/42→5/42→6/42.
- MathTex(r"L\ge32\Rightarrow2L\ge64>63"); MathTex(r"21<63\Rightarrow L\le63"); intervalo MathTex(r"L\le63<2L").

## Layout y disposicion:
- Reorganizar tabla a panel izquierdo x∈[-6.0,-0.6], cabeceras y=2.1; seis filas y=1.45,0.85,0.25,-0.35,-0.95,-1.55; columnas x=-5.2,-3.5,-1.7.
- Medidor en (3.1,1.1,0), ancho 5.2 y alto 1.6; inferencias en y=-0.4,-1.2,-2.2, centradas en x=3.0 y con ancho máximo 5.8.
- Contador en (5.7,3.25,0). No revelar L=42 ni escribir 63-21 hasta la escena 15: dedicar el espacio a certificar que el cociente es uno.

## Secuencia de animacion:
- Ventana total orientativa de escena: 54s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–10s: Transform de la tabla a disposición compacta; enviar ?15, contador4/42, recibir15 y añadir fila con cota16. Siguiente31.
- [TRIGGER_2] — 10–24s: Enviar ?31, contador5/42, recibir31 y añadir fila con cota32. Enmarcar la cota32 y calcular siguiente63.
- [TRIGGER_3] — 24–35s: Enviar ?63, contador6/42, recibir21 y añadir última fila. Separar visualmente t=63 y r=21; sostener la pausa y escribir sólo que hubo al menos una vuelta.
- [TRIGGER_4] — 35–54s: TransformFromCopy de la cota32 a 2L≥64; situar un marcador63 inmediatamente antes de64 en un pequeño zoom. Combinar con L≤63 para escribir L≤63<2L. No atribuir la respuesta a múltiples vueltas por su tamaño.

## Código Cromático y Estilo:
- ACCENT_TERRACOTTA para cota32 y límite64; ACCENT_MINT para intervalo certificado; ACCENT_CYAN para tiempo63; respuesta21 en TEXT_MAIN para destacar el cambio sin marcarlo como fallo.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 15
## Nombre: La vuelta aparece al quitar el resto
## Descripcion Breve: La resta 63−21 revela 42 y termina la conversación principal.
## Objetivo Pedagogico: Conectar el cálculo final con su interpretación geométrica y cerrar el protocolo.
## Voz en off:
> "[TRIGGER_1] Ahora sí podemos restar. Sesenta y tres es una vuelta completa más los veintiún metros que todavía ve el aparato. Quitamos esos veintiuno y quedan cuarenta y dos. [TRIGGER_2] La pista mide cuarenta y dos metros. A un metro por segundo, Perry tarda cuarenta y dos segundos en completarla. El círculo y el recorrido desplegado cuentan ahora la misma historia. [TRIGGER_3] Enviamos el mensaje final con cuarenta y dos y terminamos inmediatamente. Fueron seis mediciones y una respuesta: siete mensajes. El límite era cuarenta y dos. [TRIGGER_4] Lo importante no es que cuarenta y dos haya salido de una resta. Lo importante es que elegimos una consulta para la cual esa resta tenía una sola interpretación posible: exactamente una vuelta."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"63=L+21\quad\Longrightarrow\quad L=63-21=42"); dos segmentos de longitudes proporcionales a42 y21.
- Circle de radio1.4, ahora rotulado L=42; Dot situado tras un residuo21, media vuelta desde salida; MathTex(r"T=42\ \mathrm s").
- Tex(r"	exttt{! 42}"); contador MathTex(r"7/42"); MathTex(r"6+1=7\le42"); nodo Tex(r"	ext{Terminar}").

## Layout y disposicion:
- Recorrido desplegado de0 a63 en x∈[-5.4,5.4], y=1.3: bloque L ancho7.2 y residual ancho3.6. Ecuación en y=2.25.
- Para contrastar círculo y recta, mover el recorrido a panel izquierdo de ancho6.2 y círculo a (3.65,0,0); indicar explícitamente el cambio de escala del dibujo.
- Mensaje final en y=-1.9, conteo en y=-2.7 y contador esquina superior derecha. No dibujar un mensaje de veredicto que el protocolo de este problema no exige leer después de responder.

## Secuencia de animacion:
- Ventana total orientativa de escena: 58s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–14s: Crear tramo total63; delimitar residuo21 con Brace y apartar una copia de ese tramo. Revelar medida42 en el segmento restante y completar ecuación.
- [TRIGGER_2] — 14–29s: Levantar la tapa del panel secreto y escribir L=42. Convertir el segmento de42 en una pista circular esquemática; ubicar punto al medio de la siguiente vuelta según r/L=1/2.
- [TRIGGER_3] — 29–42s: Enviar !42 y vaciar el búfer, incrementar contador de6 a7 una sola vez; activar nodo Terminar. La conversación principal queda cerrada y no recibe más consultas en escenas posteriores.
- [TRIGGER_4] — 42–58s: Volver a resaltar la ventana de una vuelta junto a la resta. Mantener la idea de interpretación única como transición hacia la demostración general.

## Código Cromático y Estilo:
- ACCENT_INDIGO para vuelta42; ACCENT_MINT para resto separado y respuesta correcta; ACCENT_CYAN para tiempo; ACCENT_TERRACOTTA para mensaje final.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 16
## Nombre: La garantía que viaja con cada consulta
## Descripcion Breve: Un invariante demuestra la corrección para cualquier longitud válida.
## Objetivo Pedagogico: Completar base, paso de continuación y salida con una prueba inductiva visual.
## Voz en off:
> "[TRIGGER_1] Un ejemplo no demuestra que siempre funcione. Nuestra garantía es ésta: cada vez que vamos a medir, el instante elegido está antes del final de la segunda vuelta, sea cual sea la longitud que aún pueda ser la verdadera. [TRIGGER_2] Al empezar medimos en uno. Como L es al menos uno, uno es menor que dos L. La garantía vale desde la primera pregunta. [TRIGGER_3] Si la respuesta coincide con el tiempo u, aprendemos L mayor o igual que u más uno. La siguiente consulta es dos u más uno, estrictamente menor que el doble de la suma de u y uno, y por tanto menor que dos L. La garantía se conserva. [TRIGGER_4] Si la respuesta ya no coincide, sabemos además que t es al menos L. Junto con la garantía t menor que dos L, eso obliga a haber completado exactamente una vuelta. Por eso nunca confundimos un múltiplo de L con L."

## Descripcion Visual Detallada:
## Objetos:
- Tarjeta persistente MathTex(r"t<2L") con Tex(r"	ext{Garantía antes de preguntar}").
- Tres nodos de prueba: MathTex(r"L\ge1\Rightarrow1<2L"), MathTex(r"r(u)=u\Rightarrow L\ge u+1"), MathTex(r"2u+1<2(u+1)\le2L").
- Rama final MathTex(r"r<t\Rightarrow L\le t<2L\Rightarrow\lfloor t/Lfloor=1\Rightarrow L=t-r").

## Layout y disposicion:
- Garantía en (0,2.3,0) dentro de RoundedRectangle de ancho6.2 y alto0.8.
- Base a (-3.2,0.9,0), conservación a (3.0,0.9,0), cada panel ancho5.6. Flecha curva de conservación de vuelta a garantía, sin cruzar texto.
- Cadena final partida en dos MathTex: L≤t<2L en y=-1.3 y piso=1⇒L=t-r en y=-2.2. No comprimir toda la cadena en una línea ilegible.

## Secuencia de animacion:
- Ventana total orientativa de escena: 74s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–19s: Presentar garantía como una tarjeta que acompañará al puntero de consulta; colocar una banda temporal anterior a2L.
- [TRIGGER_2] — 19–31s: Create del nodo base y conexión a garantía; destacar el uso de L≥1, no de una medición previa inexistente.
- [TRIGGER_3] — 31–54s: Desplegar nodo de igualdad y derivación del próximo tiempo; mover una copia de la tarjeta de garantía de una consulta a otra mediante flecha curva. Leer cada desigualdad durante su aparición.
- [TRIGGER_4] — 54–74s: Abrir rama distinta a igualdad y unir su cota inferior con la garantía superior; encerrar el intervalo [1,2) para t/L y después transformar su piso en1. Derivar la resta sin salto lógico. Las dos ramas cubren todas las respuestas válidas porque0≤r≤t.

## Código Cromático y Estilo:
- ACCENT_MINT para invariante conservado; ACCENT_CYAN para tiempos; ACCENT_INDIGO para L; ACCENT_TERRACOTTA para piso y número de vueltas. Ningún nodo representa código fuente.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 17
## Nombre: Por qué la escalera termina
## Descripcion Breve: Sumar uno a cada tiempo convierte la recurrencia en duplicaciones exactas.
## Objetivo Pedagogico: Derivar t_k=2^k−1 y el número exacto de mediciones necesarias.
## Voz en off:
> "[TRIGGER_1] Falta demostrar que no avanzamos para siempre sin cruzar la primera vuelta. Mira qué ocurre si sumamos uno a cada tiempo de nuestra secuencia. [TRIGGER_2] Uno, tres, siete, quince y treinta y uno se convierten en dos, cuatro, ocho, dieciséis y treinta y dos. Ahora cada cantidad es exactamente el doble de la anterior. En la medición k, el tiempo más uno es dos elevado a k. [TRIGGER_3] Así que el tiempo de la medición k es dos elevado a k, menos uno. La primera respuesta distinta aparece justo cuando ese tiempo alcanza o supera L. [TRIGGER_4] Necesitamos entonces dos elevado a k al menos L más uno. El menor entero k que lo cumple es el techo del logaritmo en base dos de L más uno. Al crecer exponencialmente los tiempos, el número de mediciones crece sólo de forma logarítmica."

## Descripcion Visual Detallada:
## Objetos:
- Dos filas VGroup: MathTex 1,3,7,15,31 y MathTex 2,4,8,16,32; cinco flechas verticales con MathTex(r"+1").
- MathTex(r"t_{k+1}+1=2(t_k+1)"); MathTex(r"t_1+1=2"); MathTex(r"t_k+1=2^k\Rightarrow t_k=2^k-1").
- MathTex(r"2^k-1\ge L\iff2^k\ge L+1"); MathTex(r"k=\lceil\log_2(L+1)ceil"); Tex(r"	ext{Primera medición que cruza}").

## Layout y disposicion:
- Filas numéricas y=1.45 y0.3, centros x=-5,-2.5,0,2.5,5. Flechas verticales pequeñas entre ellas.
- Derivación de recurrencia en y=-0.85. Al introducir la fórmula general, retirar filas y situar base y recurrencia arriba, fórmula en y=0.3 y condición de cruce en y=-1.2.
- Expresión de k en y=-2.45, ancho máximo10.5; un pequeño eje de enteros muestra que se redondea hacia arriba.

## Secuencia de animacion:
- Ventana total orientativa de escena: 67s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–12s: Presentar cinco tiempos explícitos y preparar flechas +1 sin activar aún la fila nueva.
- [TRIGGER_2] — 12–32s: TransformFromCopy de cada tiempo al valor aumentado; enlazar 2→4→8→16→32 con flechas de duplicación. Derivar t_{k+1}+1=2(t_k+1) desde t_{k+1}=2t_k+1.
- [TRIGGER_3] — 32–46s: Usar base2 y k-1 duplicaciones para obtener2^k; restar uno visualmente y escribir t_k=2^k-1. Colocar la condición de primer cruce t_k≥L.
- [TRIGGER_4] — 46–67s: TransformMatchingTex de2^k-1≥L a2^k≥L+1; aplicar log base2 preservando orden por su monotonía y mostrar techo porque k es entero. No añadir una medición extra al contar k: la primera ya corresponde a k=1.

## Código Cromático y Estilo:
- ACCENT_TERRACOTTA para exponentes y +1; ACCENT_CYAN para tiempos; ACCENT_MINT para cruce garantizado; ACCENT_INDIGO para L y ejes.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 18
## Nombre: El presupuesto, sin aproximaciones peligrosas
## Descripcion Breve: Los límites numéricos certifican 40 mediciones, 41 mensajes y tiempos legales.
## Objetivo Pedagogico: Verificar explícitamente el peor caso y separar consultas de respuesta final.
## Voz en off:
> "[TRIGGER_1] Comprobemos el peor caso permitido: una longitud de diez elevado a doce. Con treinta y nueve mediciones llegamos a dos elevado a treinta y nueve, menos uno: algo menos de quinientos cincuenta mil millones. Todavía estamos por debajo de la longitud máxima. No alcanza. [TRIGGER_2] Con cuarenta, el tiempo es dos elevado a cuarenta menos uno: ahora sí, un poco más de un billón. La comparación exacta está en pantalla: ese valor supera diez elevado a doce. Por tanto, cuarenta mediciones siempre bastan. [TRIGGER_3] Falta contar la respuesta final. Cuarenta más uno son cuarenta y un mensajes, y podemos usar hasta cuarenta y dos. Nos queda un mensaje de margen incluso en el peor caso. [TRIGGER_4] Además, el mayor tiempo consultado sigue siendo menor que diez elevado a dieciocho. Cumplimos las dos restricciones distintas: pocas preguntas y todos los tiempos dentro del rango permitido."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"2^{39}-1=549\,755\,813\,887<10^{12}"); MathTex(r"2^{40}-1=1\,099\,511\,627\,775>10^{12}").
- MathTex(r"q\le40,\qquad q+1\le41<42"); VGroup de42 fichas,40 de medición,1 de respuesta y1 sobrante.
- MathTex(r"t_{\max}=1\,099\,511\,627\,775<10^{18}"); dos tarjetas Tex(r"	ext{Cantidad de mensajes}") y Tex(r"	ext{Valor del tiempo}").

## Layout y disposicion:
- Comparaciones de potencias en y=1.75 y0.65, ancho máximo11.8; cada cantidad larga en su propia línea si la tipografía excede el ancho seguro.
- 42 fichas en dos filas de21, x=-5+0.5j, y=-0.6,-1.0; cuenta total en y=-1.65.
- Límite del tiempo en y=-2.65. Usar paneles separados para presupuesto y dominio; no representar10^18 con una barra lineal que haga invisibles10^12 y2^40.

## Secuencia de animacion:
- Ventana total orientativa de escena: 68s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–21s: Write de2^39-1 y su valor exacto en grupos de tres cifras; compararlo con10^12. Mantener quieta la pantalla durante la comparación; la voz describe la magnitud y la fórmula conserva el valor exacto, sin redondear la prueba.
- [TRIGGER_2] — 21–39s: ReplacementTransform de la atención a2^40-1; mostrar valor exacto y desigualdad. Indicate del40 como número de mediciones, no como exponente de la complejidad temporal.
- [TRIGGER_3] — 39–54s: Colorear40 fichas de consulta, luego una de respuesta y dejar una libre. Escribir40+1=41<42. Esta es una cota de peor caso, no nuevas consultas después de terminar la traza de42.
- [TRIGGER_4] — 54–68s: Mostrar en otra tarjeta el límite t<10^18 y comprobarlo con tmax. No afirmar que esperaremos ese número de segundos de tiempo de ejecución: se trata del parámetro t del problema.

## Código Cromático y Estilo:
- ACCENT_CYAN para tiempos; ACCENT_INDIGO para consultas; ACCENT_TERRACOTTA para respuesta final; ACCENT_MINT para desigualdades satisfechas; TEXT_MUTED para ficha sobrante.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 19
## Nombre: Los bordes que podrían romper la prueba
## Descripcion Breve: Longitudes 1, 7 y 8 muestran arranque, cruce exacto y residuo repetido.
## Objetivo Pedagogico: Verificar casos límite y aclarar que se compara r con su propio t, no con el residuo previo.
## Voz en off:
> "[TRIGGER_1] Veamos tres bordes concretos. Si L vale uno, la primera consulta en uno responde cero. Uno menos cero es uno. Una medición y la respuesta: dos mensajes. [TRIGGER_2] Si L vale siete, preguntamos uno, tres y siete. Las respuestas son uno, tres y cero. Caer exactamente en la meta funciona: siete menos cero devuelve siete. [TRIGGER_3] Si L vale ocho, preguntamos uno, tres, siete y quince. Recibimos uno, tres, siete y siete. La última lectura repite la anterior, pero no repite el tiempo actual: siete es distinto de quince. Restamos y obtenemos ocho. [TRIGGER_4] No buscamos que dos lecturas consecutivas sean diferentes. Comparamos cada lectura con el instante de su propia consulta. Y no necesitamos recibir cero: cualquier resto sirve cuando sabemos que se completó exactamente una vuelta."

## Descripcion Visual Detallada:
## Objetos:
- Tres paneles de laboratorio con MathTex(r"L=1"), MathTex(r"L=7"), MathTex(r"L=8"). Tablas explícitas t/r: [1]/[0], [1,3,7]/[1,3,0], [1,3,7,15]/[1,3,7,7].
- MathTex(r"1-0=1"), MathTex(r"7-0=7"), MathTex(r"15-7=8"); contadores de mensajes MathTex 2,4,5.
- En el último panel, flecha vertical de t=15 a r=7 y una conexión horizontal discontinua entre los dos residuos7; Tex(r"	ext{Comparar dentro de la misma consulta}").

## Layout y disposicion:
- Paneles se presentan uno por uno, cada uno centrado en ORIGIN, ancho10.8 y alto3.4. Al terminar, reducirlos a tres tarjetas de resultado en y=-2.35, x=-4.1,0,4.1.
- Tabla del caso activo: tiempos en y=1.1, residuos en y=0.15; para cuatro columnas usar x=-3.6,-1.2,1.2,3.6.
- Comparación local del caso L8 tiene marco en x=3.6, abarcando y=0.15 y1.1. Nunca reutilizar el contador de la traza principal, que ya terminó.

## Secuencia de animacion:
- Ventana total orientativa de escena: 63s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–14s: Crear casoL1, consulta1 y respuesta0; realizar resta y pasar a ficha de resultado con dos mensajes totales.
- [TRIGGER_2] — 14–28s: Crear casoL7; revelar las tres parejas (1,1),(3,3),(7,0) en ese orden, con un indicador de igualdad en las dos primeras y diferencia en la tercera. Realizar resta y contar cuatro mensajes.
- [TRIGGER_3] — 28–46s: Crear casoL8; revelar las cuatro parejas (1,1),(3,3),(7,7),(15,7). Unir los dos residuos iguales con línea tenue, pero enmarcar t15 frente a r7 como comparación decisiva; realizar resta y contar cinco mensajes.
- [TRIGGER_4] — 46–63s: Mantener el último marco y escribir regla local r=t frente a r<t. FadeOut del conector entre residuos para dejar claro que no decide la salida. Recuperar las tres tarjetas de resultados correctos.

## Código Cromático y Estilo:
- ACCENT_TERRACOTTA para pareja activa; ACCENT_CYAN para t; ACCENT_MINT para r y resultados; TEXT_MUTED para comparación irrelevante entre lecturas consecutivas.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 20
## Nombre: Dos registros y una bifurcación
## Descripcion Breve: El razonamiento se convierte en un diagrama de estado que actualiza tiempo o termina.
## Objetivo Pedagogico: Traducir a implementación visual, incluyendo flush, enteros de64 bits y terminación inmediata.
## Voz en off:
> "[TRIGGER_1] El programa sólo necesita conservar el tiempo que va a preguntar y la lectura que recibe. Empieza con el tiempo uno, envía la consulta y espera la respuesta. [TRIGGER_2] Si ambos valores son iguales, duplica el tiempo y suma uno. Regresa al punto de preguntar. Si son distintos, resta la lectura al tiempo, envía esa longitud y termina. No necesita guardar la lista de consultas anteriores. [TRIGGER_3] Hay dos detalles de implementación que sí importan. Estos números superan la capacidad habitual de treinta y dos bits, así que usamos enteros de sesenta y cuatro bits. No necesitamos aproximaciones decimales. [TRIGGER_4] Y cada mensaje debe salir del búfer antes de esperar al juez. Después de enviar la respuesta final, el programa se detiene; no manda otra consulta. La demostración decide qué hacer, y el protocolo asegura que el diálogo ocurra."

## Descripcion Visual Detallada:
## Objetos:
- Dos RoundedRectangle de registro con MathTex t y r; nodos Tex(r"	ext{Preguntar}") y Tex(r"	ext{Recibir}"); Diamond hecho con Polygon con MathTex(r"r=t?").
- Nodo MathTex(r"t\leftarrow2t+1") y nodo MathTex(r"L\leftarrow t-r"); mensajes Tex(r"	exttt{? t}") y Tex(r"	exttt{! L}"); Tex(r"	ext{Terminar}").
- Pequeñas celdas de memoria rotuladas Tex(r"	ext{64 bits}"); panel de búfer con Tex(r"	exttt{flush}"); salida lateral Tex(r"	ext{Sin respuesta: terminar}") para fin de entrada.

## Layout y disposicion:
- Registros en (-4.5,1.6,0) y (-4.5,0.6,0), ancho2.3. Flujo principal preguntar en(-0.8,1.7,0), recibir en(2.0,1.7,0), decisión en(2.0,0.1,0).
- Ramaigual a(-0.8,-1.3,0) con flecha de regreso por x=-2.4; rama distinta a(4.6,-1.3,0) y terminar en(4.6,-2.45,0).
- Detalles64bits yflush se muestran en panel inferior izquierdo x∈[-6,-2.6], y∈[-2.75,-1.2], uno por vez. Flechas bordean textos y no atraviesan los registros.

## Secuencia de animacion:
- Ventana total orientativa de escena: 67s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–14s: FadeIn de registros t=1 y r vacío; mover ficha de consulta a preguntar y después al juez, dejando r sin valor hasta recibir una respuesta.
- [TRIGGER_2] — 14–32s: Create de decisión y ambas ramas. Animar un token por la rama de igualdad y vuelta al inicio; después un token independiente por diferencia, resta y salida. Las expresiones son transformaciones de datos, no líneas de código.
- [TRIGGER_3] — 32–48s: Mostrar etiqueta64bits bajo ambos registros y la cota de tmax que excede2^31-1. Conservar los valores como enteros; no introducir punto flotante para calcular potencias: la actualización es duplicar y sumar.
- [TRIGGER_4] — 48–67s: Animar ficha retenida en búfer, luego su salida al indicarflush antes de la espera. Activar terminar al enviar !L; incluir salida por fin de entrada como ruta sin respuesta válida, sin inventar un código numérico de error del juez. Retirar diagrama al cerrar.

## Código Cromático y Estilo:
- ACCENT_INDIGO para registros; ACCENT_CYAN para flujo y comunicación; ACCENT_TERRACOTTA para decisión; ACCENT_MINT para salida válida; TEXT_MUTED para manejo de fin de entrada.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 21
## Nombre: Qué crece y qué permanece pequeño
## Descripcion Breve: La cantidad de consultas crece logarítmicamente y la memoria se mantiene constante.
## Objetivo Pedagogico: Explicar complejidad y delimitar los supuestos que sostienen el razonamiento exacto.
## Voz en off:
> "[TRIGGER_1] El tiempo que preguntamos puede ser enorme, pero cada paso del programa hace muy poco: comparar dos enteros y, si hace falta, duplicar uno y sumarle uno. El costo sigue el número de mediciones, no el valor del tiempo consultado. [TRIGGER_2] Como necesitamos el techo del logaritmo en base dos de L más uno, el costo es logarítmico en L. En este problema son, como máximo, cuarenta mediciones. La memoria auxiliar es constante: esos dos registros bastan. [TRIGGER_3] Nuestra certeza depende de las reglas. La longitud es entera y no cambia; la velocidad es conocida; las lecturas son exactas. En particular, pasar de L mayor que u a L al menos u más uno utiliza que no existen longitudes entre enteros. [TRIGGER_4] Si el aparato tuviera ruido, si cambiara la pista o si perdiéramos esa integridad, habría que revisar la garantía. Aquí no adivinamos ni estimamos: cada respuesta elimina posibilidades mediante una desigualdad exacta."

## Descripcion Visual Detallada:
## Objetos:
- MathTex(r"q=\lceil\log_2(L+1)ceil"); MathTex(r"	ext{tiempo}=O(\log L)"); MathTex(r"	ext{memoria auxiliar}=O(1)").
- Dos registros de tamaño constante y una sucesión de tiempos1,3,7,15,31 como tarjetas, sin código.
- Cuatro tarjetas Tex(r"	ext{Longitud entera}") con MathTex(r"L\in\mathbb Z"), Tex(r"	ext{Longitud fija}"), Tex(r"	ext{Velocidad conocida}"), Tex(r"	ext{Lecturas exactas}"); MathTex(r"L>u\Rightarrow L\ge u+1").

## Layout y disposicion:
- Complejidades en panel izquierdo centrado en(-3.0,0.8,0), ancho5.6; registros en(3.3,0.8,0).
- Para supuestos, retirar complejidades y mostrar cuatro tarjetas de ancho2.8 con centros x=-4.65,-1.55,1.55,4.65, y=0.7; implicación entera en y=-1.0.
- Última frase conceptual en y=-2.4, ancho máximo11.3. No usar gráficos sin escala que aparenten una comparación experimental de rendimiento.

## Secuencia de animacion:
- Ventana total orientativa de escena: 72s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–19s: Hacer crecer los valores dentro de los registros sin aumentar su número; un contador de pasos aumenta uno por actualización, no hasta t.
- [TRIGGER_2] — 19–36s: Write de q y TransformMatchingTex hacia O(log L); escribir O(1) junto a dos registros. Nota técnica del storyboard: estas cotas usan el modelo de enteros de máquina de64bits, como el análisis fuente.
- [TRIGGER_3] — 36–56s: FadeIn de las cuatro hipótesis. Conectar longitud entera con la implicación L>u⇒L≥u+1; conectar lecturas exactas con comparación r=t.
- [TRIGGER_4] — 56–72s: Mostrar versiones hipotéticas de ruido y longitud variable como trazos discontinuos con Tex(r"	ext{Fuera de este modelo}"), sin simular otra solución ni alterar la demostración. Retirarlas y recuperar las cuatro condiciones satisfechas.

## Código Cromático y Estilo:
- ACCENT_MINT para cotas eficientes y certeza; ACCENT_INDIGO para registros; ACCENT_TERRACOTTA para integridad; TEXT_MUTED para escenarios fuera del modelo; sin rojo para costo lineal inexistente.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.

## Escena: 22
## Nombre: La mejor pregunta controla su respuesta
## Descripcion Breve: La ventana de una vuelta reúne el misterio, el descubrimiento y su lección general.
## Objetivo Pedagogico: Cerrar con el valor de diseñar consultas cuya información tenga una interpretación inequívoca.
## Voz en off:
> "[TRIGGER_1] Al principio, una lectura parecía esconder más de lo que revelaba. Veíamos dónde estaba Perry, pero no cuántas veces había pasado por la salida. [TRIGGER_2] La idea decisiva fue controlar esa cantidad antes de medir. Avanzar lo suficiente para progresar, pero nunca tanto como para que dos vueltas se confundieran con una. [TRIGGER_3] Así construimos la escalera uno, tres, siete, quince, treinta y uno. Una igualdad nos autoriza a subir; la primera diferencia revela la longitud. No por suerte, sino porque conservamos la misma garantía en cada peldaño. [TRIGGER_4] En este problema, la parte más importante de la respuesta ocurrió antes de recibirla: al elegir la pregunta. [Pausa.] A veces, una buena estrategia no necesita observar más. Necesita decidir mejor cuándo observar."

## Descripcion Visual Detallada:
## Objetos:
- Pista esquemática inicial y medidor, seguidos por recta desplegada con ventana [L,2L).
- Cinco tarjetas de tiempos1,3,7,15,31; dos fichas MathTex(r"r=t") y MathTex(r"r<t"); MathTex(r"L=t-r") dentro de la ventana certificada.
- Tex(r"	ext{Elegir la pregunta para controlar su significado}"); crédito Tex(r"	ext{Diabolic Doofenshmirtz --- GCPC 2022}").

## Layout y disposicion:
- Pista en(-3.5,0.5,0) y medidor en(3.3,0.5,0), mismo convenio de apertura.
- La transformación a recta usa x∈[-5.4,5.4], y=0.8; escalera de tarjetas en y=-0.6. Frase final centrada en ORIGIN, ancho máximo11.5.
- Crédito en y=-3.25. No mostrar un nuevo contador ni enviar mensajes: la traza ya terminó en la escena15.

## Secuencia de animacion:
- Ventana total orientativa de escena: 60s. Los tiempos siguientes son locales, estimados y subordinados al inicio real de cada frase.
- [TRIGGER_1] — 00–12s: Recrear pista y medidor iniciales mediante FadeIn, sin una interacción nueva; dibujar una vuelta pasada como huella que desaparece.
- [TRIGGER_2] — 12–26s: Transform del recorrido a recta desplegada e iluminar ventana de una vuelta; el tramo perdido se convierte ahora en segmento recuperable L.
- [TRIGGER_3] — 26–43s: Revelar explícitamente las cinco tarjetas de la escalera y sus dos reglas de transición; unir la primera diferencia con L=t-r. Es una recapitulación conceptual, no omite ningún paso de la traza ya desarrollada.
- [TRIGGER_4] — 43–60s: FadeOut de diagramas dejando sólo frase final y crédito. Mantener un hold de2s después de la pausa de la voz; cerrar con FadeOut a BG_COLOR. No añadir código ni un epílogo que interrumpa la última pregunta conceptual.

## Código Cromático y Estilo:
- ACCENT_INDIGO para pista y longitud; ACCENT_MINT para ventana segura; ACCENT_CYAN para tiempos; ACCENT_TERRACOTTA para decisión de medir; TEXT_MAIN para cierre.
- Mantener Tex/MathTex, fondo BG_COLOR, márgenes y contraste de las convenciones generales; agrupar texto y geometría relacionados con VGroup.
