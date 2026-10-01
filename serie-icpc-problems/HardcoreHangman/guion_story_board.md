# Guion Storyboard / Técnico: Hardcore Hangman

## Convenciones generales de producción

- **Alcance:** especificación narrativa y técnica; todavía no se implementan escenas ni se generan renders. Fuente conceptual: `guion_sol.md` de esta misma carpeta. Paleta comprobada en `/Users/amgl/stem-code-lab/styles/theme.py`.
- **Formato:** 16:9, frame lógico de ancho 128/9 y alto 8; centro `(0,0,0)`. Área segura: x entre -6.3 y 6.3, y entre -3.5 y 3.5. Fondo `BG_COLOR`. Títulos en y=3.25; cuando haya contador a la derecha, reservarle x entre 5.1 y 6.6 y limitar el título a ancho 9.0.
- **Tipografía:** todo texto visible, títulos, créditos, palabras, índices, rótulos y cifras se construye con `Tex` o `MathTex`. Letras y mensajes del protocolo con `Tex(r"\texttt{...}")`; variables, bits y ecuaciones con `MathTex`. No usar `Text`, `MarkupText` ni `Code`. Los rectángulos y otros objetos geométricos no contienen rótulos automáticos: añadir sus `Tex` explícitos.
- **Legibilidad:** títulos 36–40 pt, texto explicativo 27–30 pt, ecuaciones 30–36 pt, bits 26–30 pt e índices 22–24 pt. Ajustar frases mediante saltos LaTeX o separarlas en objetos; evitar reducir texto principal por debajo de 24 pt. Límites de ancho indicados para cada panel. Usar `VGroup` para mover letras, contornos e índices como unidades coherentes.
- **Sincronización:** los triggers reinician en 1 en cada escena. Su identidad completa es `(escena, trigger)`. La voz se reproduce literalmente desde el mismo bloque que `guion_voz.md`. Los tiempos indicados son ventanas locales estimadas a 145 palabras/minuto más pausas; no son mediciones de una grabación. Cada trigger se dispara al comenzar su frase; con la locución definitiva prevalece la marca verbal y se reajustan holds, nunca el contenido matemático.
- **Ritmo:** animaciones simples de 0.6–1.2 s y composiciones de 1.5–3 s dentro de la ventana del trigger; el resto se dedica a lectura y voz. `[Pausa.]` reserva unos 1.2 s sin incorporar palabras a la locución. No mantener movimiento ornamental mientras se explica una fórmula.
- **Roles:** las cadenas mostradas en laboratorio sólo las ve el espectador; el algoritmo recibe únicamente índices del juez. Rotular todos los experimentos como tales. Las escenas 02–08 no son una partida acumulativa. La estrategia oficial usa códigos 0–25 y siete mensajes; la variante definitiva usa 1–26 y seis. Reiniciar el contador al iniciar esta última en la escena 10.
- **Traza principal:** escenas 11–13 envían exactamente cinco consultas para `banana`; las escenas 14–18 son explicaciones con la conversación pausada. La escena 19 envía el sexto y último mensaje, `! banana`. Las respuestas del juez no gastan mensajes del programa. Los ejemplos auxiliares `ap`, `a` y `zzzz` no incrementan el contador de banana.
- **Bits:** escribir siempre b4,b3,b2,b1,b0 de izquierda a derecha, pesos 16,8,4,2,1. Consultar b0,b1,b2,b3,b4 en ese orden. El estado parcial cero no se decodifica como letra antes de completar las consultas. La letra monoespaciada `n` se distingue de la variable matemática de longitud n.
- **Colores reales disponibles:** `BG_COLOR=#181C24`, `TEXT_MAIN=#ECEFF4`, `TEXT_MUTED=#64748B`, `ACCENT_VINO=#C0392B`, `ACCENT_MINT=#2DD4BF`, `ACCENT_TERRACOTTA=#D97706`, `ACCENT_INDIGO=#6366F1`, `ACCENT_CYAN=#38BDF8`. No existe `COLOR_DANGER` en la paleta actual: usar `ACCENT_VINO` para exceso o contradicción. Una respuesta negativa o vacía es información válida y usa `TEXT_MUTED`, no rojo.
- **Transiciones:** limpiar los objetos que no se conservan explícitamente. Las escenas 11–13 comparten las coordenadas y estados de las máscaras. Si se renderizan por separado, la escena siguiente recreará exactamente el estado final anterior antes de animar. En el resto, mantener sólo fondo, título o rótulo indicados. No incluir música, efectos sonoros ni assets externos como requisito para comprender la solución.

#### Escena: 01
##### Nombre: Una palabra, siete mensajes
##### Descripcion Breve: Una caja oculta una cadena y siete fichas limitan la conversación.
##### Objetivo Pedagogico: Entender el desafío y que la respuesta final también consume un mensaje.
##### Voz en off:
> "[TRIGGER_1] Imagina que alguien esconde una palabra. Puede tener una letra… o diez mil. Tú no ves ninguna y tampoco sabes cuántas hay. [Pausa.] ¿Podrías descubrirla sin ir probando letra por letra? [TRIGGER_2] En Hardcore Hangman, un problema del concurso alemán GCPC de dos mil veintidós, tienes siete mensajes para conseguirlo. Y hay una condición importante: decir la respuesta también gasta uno. [TRIGGER_3] Parece un presupuesto ridículo. Hasta que descubrimos que una buena pregunta puede investigar miles de posiciones al mismo tiempo. [TRIGGER_4] Vamos a construir esas preguntas. No necesitaremos adivinar vocabulario: nuestra estrategia debe funcionar incluso si la palabra es una cadena de letras completamente absurda."

##### Descripcion Visual Detallada:
###### Objetos:
- Una RoundedRectangle opaca de ancho 7.2 y alto 1.35; Tex(r"	extbf{Cadena oculta}") y MathTex(r"1\le n\le10^4"). No dibujar un número de casillas que revele n.
- VGroup de siete Circle de radio 0.17; Tex(r"	ext{mensajes disponibles}") y Tex(r"	ext{La respuesta también cuenta}").
- Tex(r"	extbf{Hardcore Hangman}") y Tex(r"	ext{GCPC 2022}"); iconos hechos con Rectangle, Line y Arrow, sin imágenes externas.

###### Layout y disposicion:
- Caja en ORIGIN; etiqueta interna en ORIGIN; rango de longitud en DOWN*1.25.
- Siete fichas centradas en UP*2.25, con centros x=-1.5+0.5j para j=0,...,6. Nota del presupuesto en DOWN*2.15.
- Título en UP*3.25; crédito en DOWN*3.30. Reservar márgenes laterales |x|<=6.3.

##### Secuencia de animacion:
- Duración orientativa: 52 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–16 s: FadeIn de la caja cerrada; Write del rango. Mantener dos segundos tras la pregunta, sin convertir la caja en una palabra concreta.
- [TRIGGER_2] — 16–30 s: LaggedStart de FadeIn sobre las siete fichas; Circumscribe de la séptima al escribir la nota de la respuesta. No consumir ninguna: aún estamos presentando las reglas.
- [TRIGGER_3] — 30–40 s: Crear varios Arrow finos desde un único pequeño círculo de pregunta hacia puntos sin etiquetas dentro de la caja; indicarlos simultáneamente para anticipar el paralelismo.
- [TRIGGER_4] — 40–52 s: FadeOut de las flechas; mantener título, caja y fichas. La salida deja una caja cerrada que se transforma en el panel del juez de la escena 02.

##### Código Cromático y Estilo:
- BG_COLOR de fondo; TEXT_MAIN para reglas; ACCENT_INDIGO para caja; ACCENT_MINT para promesa de resolver; ACCENT_TERRACOTTA para ficha de respuesta.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 02
##### Nombre: Qué responde realmente el juez
##### Descripcion Breve: Una consulta de vocales revela posiciones, no las letras exactas.
##### Objetivo Pedagogico: Distinguir conjunto consultado, cantidad de resultados e índices de base uno.
##### Voz en off:
> "[TRIGGER_1] Para entender las reglas, hagamos un experimento. A ti te muestro la palabra banana; al algoritmo, no. Enviamos una pregunta que contiene las cinco vocales. [TRIGGER_2] El juez devuelve tres, dos, cuatro, seis. El primer número dice cuántas posiciones vienen después. Los otros tres son los índices donde encontró alguna vocal: la segunda, la cuarta y la sexta posición. [TRIGGER_3] Pero no nos dice qué vocal hay en cada sitio. En esas posiciones podría haber una a, una e, una i, una o o una u. La respuesta entrega pertenencia a un grupo, no identidad. [TRIGGER_4] Y los lugares que no aparecen también nos cuentan algo: allí no hay vocales. Cada pregunta reparte las posiciones entre un sí y un no. Guardemos esa idea."

##### Descripcion Visual Detallada:
###### Objetos:
- VGroup de seis RoundedRectangle de lado 0.72 con letras Tex(r"	exttt{b}"), Tex(r"	exttt{a}"), Tex(r"	exttt{n}"), etc.; índices MathTex(r"1"),...,MathTex(r"6").
- Tex(r"	ext{Laboratorio: la palabra sólo la ve el espectador}"); dos paneles Rectangle para algoritmo y juez, con rótulos Tex.
- Tex(r"	exttt{? aeiou}"); respuesta descompuesta en cuatro MathTex: 3,2,4,6; Brace sobre el primer número y Brace bajo los tres índices; rótulos Tex(r"	ext{cantidad}") y Tex(r"	ext{posiciones}").
- MathTex(r"\{a,e,i,o,u\}"); Tex(r"	ext{Sí: pertenece}") y Tex(r"	ext{No: no pertenece}").

###### Layout y disposicion:
- Rótulo de laboratorio en UP*2.55; fila de letras con centros x=-2.25+0.9j, y=1.20; índices en y=0.58.
- Algoritmo en LEFT*4.5+DOWN*0.85; juez en RIGHT*4.5+DOWN*0.85; consulta y respuesta alternan en el corredor central, |x|<=2.5.
- Desglose de respuesta en y=-2.10; etiquetas cantidad/posiciones en y=-2.90. No colocar llaves sobre el corredor de mensajes.

##### Secuencia de animacion:
- Duración orientativa: 58 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–12 s: ReplacementTransform de la caja en la fila de laboratorio. Write del rótulo de advertencia antes de revelar banana. Enviar la consulta con MoveAlongPath de izquierda a derecha.
- [TRIGGER_2] — 12–28 s: Escribir los cuatro números separados. Indicate del 3 y su Brace; después indicar 2,4,6 y colorear únicamente las casillas correspondientes.
- [TRIGGER_3] — 28–44 s: En el panel del algoritmo, sustituir una casilla de letra por el conjunto de cinco candidatos; mantener la palabra sólo en el área de laboratorio. No transferir la a real al algoritmo.
- [TRIGGER_4] — 44–58 s: Resaltar el contorno de posiciones 1,3,5 como respuesta negativa. Introducir ambos rótulos sí/no; FadeOut de mensajes y llaves al cerrar, manteniendo la distinción de roles.

##### Código Cromático y Estilo:
- ACCENT_CYAN para mensajes e índices; ACCENT_MINT para pertenencia; TEXT_MUTED para exclusión, nunca COLOR_DANGER; letras verdaderas en TEXT_MAIN y candidatas en ACCENT_INDIGO.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 03
##### Nombre: Preguntar de una en una
##### Descripcion Breve: La estrategia de consultar las 26 letras desborda el presupuesto.
##### Objetivo Pedagogico: Motivar preguntas colectivas sin confundir límite de consultas con longitud de la cadena.
##### Voz en off:
> "[TRIGGER_1] La receta más directa sería preguntar por la a, después por la b, después por la c… y seguir hasta conocer todo el alfabeto. [TRIGGER_2] Esa receta puede gastar veintiséis preguntas y un mensaje final. Veintisiete mensajes para un presupuesto de siete. Aunque la cadena fuera corta, esta forma de preguntar ya resulta demasiado cara. [TRIGGER_3] ¿Y si preguntamos por muchas letras juntas? El problema es que una respuesta afirmativa parece ambigua: sabemos que la letra está dentro del grupo, pero todavía no cuál es. [TRIGGER_4] La pregunta decisiva es otra: ¿podemos elegir varios grupos de manera que su combinación identifique cada letra sin confundirla con ninguna otra?"

##### Descripcion Visual Detallada:
###### Objetos:
- VGroup de 26 tarjetas pequeñas con Tex de letras minúsculas; únicamente seis consultas individuales visibles a la vez, seguidas de MathTex(r"\cdots").
- MathTex(r"26+1=27>7"); siete Circle de presupuesto como referencia, sin simular una interacción ilegal.
- Dos conjuntos de tarjetas en RoundedRectangle y un gran MathTex(r"?") entre ellos; Tex(r"	ext{Una pregunta aislada}") y Tex(r"	ext{Combinar preguntas}").

###### Layout y disposicion:
- Consultas individuales en una fila de ancho máximo 10, centrada en UP*1.30.
- Ecuación en ORIGIN; presupuesto en DOWN*1.05. Pregunta de grupos en dos paneles centrados en LEFT*2.9+DOWN*2.2 y RIGHT*2.9+DOWN*2.2.
- Título común en UP*3.25. Todos los elementos de la escena anterior salen antes de mostrar la cuenta.

##### Secuencia de animacion:
- Duración orientativa: 51 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–12 s: LaggedStart de Write de consultas individuales con ritmo inicialmente lento y después abreviado; detenerse en los puntos suspensivos, sin animar 26 ciclos completos.
- [TRIGGER_2] — 12–26 s: Write de 26+1=27 y después >7. Indicate en ACCENT_VINO sobre el exceso. Las fichas no se consumen: es una comparación de estrategias, no una partida.
- [TRIGGER_3] — 26–40 s: TransformFromCopy de varias tarjetas hacia un solo grupo; escribir la etiqueta de ambigüedad sin tachar la idea.
- [TRIGGER_4] — 40–51 s: Mover dos grupos de tarjetas hacia el centro y hacer aparecer un conector entre ellos. FadeOut de la cuenta roja para dar paso a una exploración útil.

##### Código Cromático y Estilo:
- ACCENT_VINO únicamente para exceso de mensajes; ACCENT_INDIGO para grupos; ACCENT_CYAN para su combinación; TEXT_MAIN para letras.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 04
##### Nombre: Cruzar pistas, también las negativas
##### Descripcion Breve: Dos respuestas se cruzan para reducir los candidatos de una posición.
##### Objetivo Pedagogico: Comprender la firma de pertenencia antes de introducir números binarios.
##### Voz en off:
> "[TRIGGER_1] Volvamos a la segunda posición de banana. La consulta de vocales nos dijo que estaba dentro del grupo a, e, i, o, u. Ahora preguntamos por a, b, c y d. [TRIGGER_2] La posición dos vuelve a aparecer. Su letra pertenece a los dos grupos. ¿Qué letra comparten? Sólo la a. Dos pistas ambiguas por separado se han convertido en una identificación exacta. [TRIGGER_3] En cambio, la primera posición no salió con las vocales y sí con el segundo grupo. Sus candidatas quedan reducidas a b, c y d. Todavía no sabemos cuál es, pero ya aprendimos algo. [TRIGGER_4] No necesitamos que cada pregunta encuentre una letra. Necesitamos que el historial de respuestas sea distinto para cada candidata. Un patrón de síes y noes puede funcionar como una firma."

##### Descripcion Visual Detallada:
###### Objetos:
- Dos VGroup de tarjetas Tex para a,e,i,o,u y a,b,c,d; copia de la fila banana marcada como laboratorio.
- MathTex(r"Q=\{a,e,i,o,u\}"), MathTex(r"P=\{a,b,c,d\}"); MathTex(r"Q\cap P=\{a\}") y MathTex(r"P\setminus Q=\{b,c,d\}").
- Dos fichas de posición MathTex(r"j=2") y MathTex(r"j=1"); pares de respuesta Tex(r"	ext{sí, sí}") y Tex(r"	ext{no, sí}").

###### Layout y disposicion:
- Grupos en LEFT*3.0+UP*0.8 y RIGHT*3.0+UP*0.8, cada uno dentro de ancho 4.8 y alto 1.6.
- Posición 2 y su intersección en y=-1.25; posición 1 y diferencia en y=-2.45; firmas a x=4.3 en esas mismas alturas.
- Fila de laboratorio pequeña en UP*2.55, ancho 4.2. No usar un diagrama de Venn con palabras superpuestas: transportar tarjetas a una zona central de resultados.

##### Secuencia de animacion:
- Duración orientativa: 60 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–15 s: Write de ambos grupos y destacar el índice 2. Enviar la segunda consulta sólo dentro del laboratorio, que no conserva un contador de partida.
- [TRIGGER_2] — 15–30 s: TransformFromCopy de las dos tarjetas a hacia una única tarjeta central; FadeToColor de las demás a TEXT_MUTED. Escribir la intersección.
- [TRIGGER_3] — 30–46 s: Cambiar foco al índice 1; excluir las vocales y transportar b,c,d a una fila de candidatas. Escribir la diferencia y su firma no/sí.
- [TRIGGER_4] — 46–60 s: Circumscribe de las dos firmas. Sustituir gradualmente las palabras sí/no por MathTex 1/0 en un pequeño ejemplo, con leyenda explícita; limpiar grupos para la escena siguiente.

##### Código Cromático y Estilo:
- ACCENT_MINT para pertenencia afirmativa; TEXT_MUTED para negativa; ACCENT_TERRACOTTA para índice activo; ACCENT_CYAN para transporte de pistas.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 05
##### Nombre: Un alfabeto de juguete
##### Descripcion Breve: Cuatro letras reciben firmas distintas de dos bits.
##### Objetivo Pedagogico: Descubrir la codificación binaria como diseño de preguntas, no como un truco memorizado.
##### Voz en off:
> "[TRIGGER_1] Hagamos el problema más pequeño. Sólo existen cuatro letras: a, b, c y d. Les asignamos estas firmas: cero cero, cero uno, uno cero y uno uno. [TRIGGER_2] La primera pregunta mira el bit de la derecha. Incluye b y d, que tienen un uno allí. La segunda mira el bit de la izquierda e incluye c y d. [TRIGGER_3] Si una posición aparece en ambas respuestas, su firma es uno uno: tiene una d. Si aparece sólo en la primera, su firma es cero uno: tiene una b. [TRIGGER_4] Y si no aparece en ninguna, sería una a… siempre que ya sepamos que esa posición existe. [Pausa.] Guarda esa condición: dentro de un momento va a ser importante."

##### Descripcion Visual Detallada:
###### Objetos:
- Tabla construida con VGroup de celdas Rectangle y entradas Tex de a,b,c,d; bits en MathTex separados por columna; cabeceras MathTex(r"b_1"), MathTex(r"b_0").
- MathTex(r"Q_0=\{b,d\}"), MathTex(r"Q_1=\{c,d\}"); dos Dot por firma y Tex(r"	ext{posición conocida}").
- Tex(r"	ext{Ejemplo reducido: cuatro letras}") y MathTex(r"00\leftrightarrow a,\quad01\leftrightarrow b,\quad10\leftrightarrow c,\quad11\leftrightarrow d").

###### Layout y disposicion:
- Tabla a LEFT*3.3, filas y=1.5,0.5,-0.5,-1.5; columna letra x=-4.2, b1 x=-3.15, b0 x=-2.25.
- Consultas en RIGHT*2.7+UP*1.15 y RIGHT*2.7+DOWN*0.05; decodificación activa a RIGHT*2.7+DOWN*1.45.
- Advertencia de posición conocida en DOWN*2.75. Orden escrito b1,b0; orden temporal de preguntas b0 y luego b1, señalado por flechas numeradas.

##### Secuencia de animacion:
- Duración orientativa: 57 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–13 s: Write de letras y asignar dos bits a cada fila con LaggedStart; enfatizar que todas las filas difieren.
- [TRIGGER_2] — 13–28 s: SurroundingRectangle sobre la columna derecha b0 y transportar b,d al primer conjunto. Mover el marco a b1 y formar c,d.
- [TRIGGER_3] — 28–42 s: Encender ambos bits de la fila d; luego mostrar b con sólo b0 encendido. Cada bit conserva su columna, sin invertir la palabra binaria.
- [TRIGGER_4] — 42–57 s: Mostrar la firma 00 y la tarjeta a junto a la advertencia de existencia. Indicate de esa advertencia, sin resolver aún la longitud.

##### Código Cromático y Estilo:
- ACCENT_TERRACOTTA para columna consultada; ACCENT_INDIGO para matriz; ACCENT_MINT para bits uno; TEXT_MUTED para cero; advertencia en ACCENT_VINO moderado.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 06
##### Nombre: Cuántas preguntas necesita una firma
##### Descripcion Breve: Las firmas se duplican con cada nueva pregunta hasta superar las 26 letras.
##### Objetivo Pedagogico: Justificar cinco bits y aclarar que una pregunta entrega un bit por posición.
##### Voz en off:
> "[TRIGGER_1] Cada nueva pregunta añade una decisión: sí o no. Con una pregunta tenemos dos firmas; con dos, cuatro; con tres, ocho. [TRIGGER_2] Cuatro preguntas producen dieciséis firmas. No alcanzan para distinguir veintiséis letras. Cinco producen treinta y dos. Ahora sí tenemos espacio para dar una identidad diferente a cada letra. [TRIGGER_3] Además, no estamos repitiendo esas cinco preguntas para cada casilla. El juez entrega todos los índices que cumplen la condición. La misma pregunta aporta un bit a cada posición de la cadena. [TRIGGER_4] Para una sola letra desconocida, cuatro respuestas de sí o no tampoco pueden distinguir las veintiséis posibilidades, aunque adaptemos las preguntas. Cinco es la cantidad necesaria para identificarla con este tipo de información."

##### Descripcion Visual Detallada:
###### Objetos:
- VGroup de tarjetas de firmas en disposiciones de 2,4,8,16,32 elementos; generar como pequeños Rectangle con bits MathTex sólo en las tarjetas destacadas.
- MathTex(r"2^4=16<26\le32=2^5"); Tex(r"	ext{Un bit por posición y por pregunta}").
- Pequeño árbol de decisiones de cuatro niveles con Line y Dot, hojas abreviadas con MathTex(r"\le16"); un conjunto de 26 candidatos representados por tarjetas.

###### Layout y disposicion:
- Zona de duplicación en centro, rectángulo útil x∈[-5.8,5.8], y∈[-0.9,1.9]; cuadrícula final de 8 columnas por 4 filas con pasos 1.25 y 0.65.
- Ecuación en DOWN*1.70 y leyenda en DOWN*2.65.
- Para el último trigger, retirar la cuadrícula y colocar árbol en LEFT*2.7+UP*0.2 y 26 candidatos abreviados en RIGHT*3.0+UP*0.2; mantener ecuación abajo.

##### Secuencia de animacion:
- Duración orientativa: 56 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–11 s: TransformFromCopy de cada tarjeta hacia dos descendientes; tres duplicaciones legibles, sin escribir todos los códigos pequeños.
- [TRIGGER_2] — 11–25 s: Completar 16 y luego 32 tarjetas; escribir desigualdad y reservar 26 posiciones con un marco, dejando seis sobrantes apagadas.
- [TRIGGER_3] — 25–40 s: Cambiar la cuadrícula por varias posiciones paralelas con una columna de bits sincronizada; encenderlas en el mismo play. Escribir la leyenda un bit por posición.
- [TRIGGER_4] — 40–56 s: FadeIn del árbol abreviado y sus dieciséis hojas máximas; contrastar con 26 candidatas. No afirmar aquí un óptimo universal contando posibles adivinanzas finales: la cota se refiere a identificar mediante consultas de conjuntos.

##### Código Cromático y Estilo:
- ACCENT_INDIGO para firmas; ACCENT_TERRACOTTA para exponentes; ACCENT_MINT para capacidad suficiente; ACCENT_VINO para 16 insuficiente; TEXT_MAIN para la cota.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 07
##### Nombre: La letra que desaparece
##### Descripcion Breve: Asignar el código cero oculta también la existencia de algunas posiciones.
##### Objetivo Pedagogico: Exponer el fallo de usar 0–25 cuando la longitud aún es desconocida.
##### Voz en off:
> "[TRIGGER_1] Ya parece resuelto: numeramos las letras del cero al veinticinco y preguntamos por sus cinco bits. Pero recuerda que tampoco conocemos la longitud. [TRIGGER_2] Si la a recibe cinco ceros, nunca entra en ninguna pregunta. Imagina que la cadena es una a. Todas las respuestas quedarían vacías. [TRIGGER_3] Ahora imagina tres aes. Las cinco respuestas también quedarían vacías. No sólo ignoramos la letra: ni siquiera podemos saber cuántas posiciones hay. [TRIGGER_4] El cero confunde dos situaciones diferentes: una posición que existe pero siempre responde no, y una posición que no existe. Necesitamos separar esas situaciones."

##### Descripcion Visual Detallada:
###### Objetos:
- MathTex(r"a\mapsto00000"); dos paneles de RoundedRectangle con Tex(r"	exttt{a}") y Tex(r"	exttt{aaa}").
- Cinco MathTex(r"arnothing") por panel; Tex(r"	ext{La misma conversación}").
- Tex(r"	ext{Existe, pero no aparece}") y Tex(r"	ext{No existe}"); signo MathTex(r"
e") inicialmente ausente y un conector de ambigüedad.

###### Layout y disposicion:
- Código cero en UP*2.35. Paneles a LEFT*3.15 y RIGHT*3.15, ancho 5.3 y alto 2.6.
- Palabras de ejemplo en y=0.7; secuencias de cinco vacíos en y=-0.3, repartidas en dos filas si superan ancho 4.8.
- Frase de ambigüedad en DOWN*2.2; dos situaciones en y=-2.9, x=-3.2 y 3.2. Etiqueta permanente de experimento con códigos 0–25.

##### Secuencia de animacion:
- Duración orientativa: 47 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–12 s: Write de a→00000 y rótulo de longitud desconocida. Desactivar visualmente los cinco bits sin borrar la letra del ejemplo.
- [TRIGGER_2] — 12–24 s: FadeIn del primer panel y cinco respuestas vacías con LaggedStart.
- [TRIGGER_3] — 24–35 s: TransformFromCopy de las respuestas al segundo panel, cuya palabra tiene tres letras. Circumscribe de ambas secuencias idénticas.
- [TRIGGER_4] — 35–47 s: Mostrar las dos situaciones bajo los paneles, conectadas a la misma salida vacía. Pausa para que se reconozca el fallo; FadeOut de los paneles al pasar a la solución oficial.

##### Código Cromático y Estilo:
- ACCENT_VINO para ambigüedad; TEXT_MUTED para ceros y vacíos; TEXT_MAIN para cadenas; ACCENT_INDIGO para paneles. No usar un vacío rojo como si fuera un error del juez.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 08
##### Nombre: Una solución que cabe en siete
##### Descripcion Breve: La consulta de todo el alfabeto permite usar firmas 0–25 sin ambigüedad.
##### Objetivo Pedagogico: Presentar la estrategia oficial completa y contabilizar la respuesta final.
##### Voz en off:
> "[TRIGGER_1] La solución oficial resuelve ese detalle con una pregunta inicial: enviar todo el alfabeto. Como cada carácter de la cadena es una de esas letras, el juez devuelve todas las posiciones. [TRIGGER_2] Ahora conocemos la longitud. Una casilla que no aparezca en ninguna de las cinco preguntas binarias ya no desaparece: sabemos que existe, así que podemos asignarle el código cero. [TRIGGER_3] El presupuesto queda así: una pregunta para la longitud, cinco para las firmas y un mensaje con la respuesta. Siete en total. Ya tenemos una solución válida. [TRIGGER_4] Pero podemos preguntarnos algo más: ¿es obligatorio gastar una pregunta sólo para saber cuántas posiciones existen? ¿Y si cambiamos las firmas para que todas dejen alguna señal?"

##### Descripcion Visual Detallada:
###### Objetos:
- Tex(r"	ext{Estrategia oficial: códigos 0 a 25}"); Tex(r"	exttt{? abcdefghijklmnopqrstuvwxyz}").
- MathTex(r"R(\Sigma)=\{1,2,\ldots,n\}"); MathTex(r"1+5+1=7").
- VGroup de siete fichas en tres grupos de tamaños 1,5,1; Brace y Tex para longitud, bits y respuesta. MathTex(r"00000\mapsto a") junto a casilla con índice conocido.

###### Layout y disposicion:
- Rótulo de estrategia en UP*2.55; consulta centrada en UP*1.5, ancho máximo 11.4; respuesta en UP*0.5.
- Fichas en y=-0.8, x=-3.0+j; etiquetas bajo sus Brace en y=-1.75; ecuación en DOWN*2.7.
- Casilla de código cero ocupa RIGHT*4.5+UP*0.4 sólo después de retirar la respuesta de posiciones para evitar solapamientos.

##### Secuencia de animacion:
- Duración orientativa: 55 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–15 s: Escribir consulta completa y transformar la respuesta en todas las posiciones, con elipsis para no insinuar una longitud conocida de antemano.
- [TRIGGER_2] — 15–29 s: Mostrar una casilla real con índice y código cero; Indicate del índice como certificado de existencia. Añadir a únicamente en esa casilla conocida.
- [TRIGGER_3] — 29–42 s: Crear grupos 1,5,1, sus llaves y la ecuación. Marcar la estrategia como válida con contorno ACCENT_MINT; no animar otra partida completa.
- [TRIGGER_4] — 42–55 s: Circumscribe de la ficha de longitud. Separarla ligeramente del resto y terminar en una pregunta visual, sin eliminarla todavía. Al salir, retirar todas las fichas: la siguiente estrategia reinicia desde cero.

##### Código Cromático y Estilo:
- ACCENT_CYAN para longitud; ACCENT_INDIGO para cinco bits; ACCENT_TERRACOTTA para respuesta; ACCENT_MINT para validez. El código cero no se marca como erróneo en esta estrategia.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 09
##### Nombre: Ninguna firma completamente apagada
##### Descripcion Breve: Los códigos 1–26 permiten recuperar letras y longitud con las mismas consultas.
##### Objetivo Pedagogico: Derivar la mejora a seis mensajes y probar la cobertura de todas las posiciones.
##### Voz en off:
> "[TRIGGER_1] En cinco bits hay treinta y dos firmas. Podemos dejar libre la formada sólo por ceros y todavía quedan treinta y una: suficientes para nuestras veintiséis letras. [TRIGGER_2] Ahora numeramos desde uno. La a vale uno; la b, dos; la n, catorce; la z, veintiséis. Cada letra tiene por lo menos un bit encendido. [TRIGGER_3] Eso significa que cada posición aparecerá en alguna respuesta. También la última. Al terminar las cinco preguntas, el mayor índice que hayamos visto será exactamente la longitud de la cadena. [TRIGGER_4] Así descubrimos las letras y la longitud a la vez. Cinco preguntas y la respuesta final: seis mensajes. A partir de aquí usaremos únicamente esta numeración, del uno al veintiséis."

##### Descripcion Visual Detallada:
###### Objetos:
- Cuadrícula de 32 tarjetas; una MathTex(r"00000") y 31 tarjetas no nulas representadas mediante puntos y ejemplos.
- Cuatro VGroup, cada uno con una letra monoespaciada Tex y su igualdad numérica MathTex: a junto a r"=1=00001", b junto a r"=2=00010", n junto a r"=14=01110" y z junto a r"=26=11010". La letra n no se representa como variable de longitud.
- MathTex(r"igcup_{b=0}^{4}R(Q_b)=\{1,\ldots,n\}"); MathTex(r"5+1=6\le7"); Tex(r"	ext{Nueva estrategia: códigos 1 a 26}").

###### Layout y disposicion:
- Cuadrícula abreviada a LEFT*3.6+UP*0.4, ancho 4.4; ejemplos de letras a RIGHT*2.4+UP*0.5, filas separadas 0.62.
- Unión de respuestas en DOWN*1.65; cuenta en DOWN*2.70. Nueva estrategia en UP*2.55.
- La letra n se muestra como glifo monoespaciado en su tarjeta, y la longitud n como símbolo matemático sólo en la ecuación de unión.

##### Secuencia de animacion:
- Duración orientativa: 54 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–13 s: Apagar y apartar únicamente la tarjeta 00000; contar las 31 restantes con una Brace y MathTex(r"31\ge26").
- [TRIGGER_2] — 13–26 s: Revelar las cuatro firmas representativas. Indicate de al menos un bit uno por fila; ninguna conserva el código de la estrategia anterior.
- [TRIGGER_3] — 26–40 s: Transportar índices desde cinco respuestas esquemáticas a una unión sin duplicados. Encerrar el mayor índice y escribir n a su lado sólo tras completar la unión.
- [TRIGGER_4] — 40–54 s: Write de 5+1=6≤7; mantener el rótulo códigos 1 a 26 como convenio de las escenas posteriores. FadeOut de cuadrícula y conservar las tarjetas a,b,n para la traza.

##### Código Cromático y Estilo:
- ACCENT_MINT para bits no nulos y cobertura; TEXT_MUTED para cero descartado; ACCENT_TERRACOTTA para mayor índice; ACCENT_INDIGO para estrategia.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 10
##### Nombre: Diseñar las cinco preguntas
##### Descripcion Breve: Cada columna de la tabla binaria define un conjunto fijo de letras.
##### Objetivo Pedagogico: Precisar orden de bits, conjuntos completos y carácter no adaptativo de las consultas.
##### Voz en off:
> "[TRIGGER_1] Escribimos cada código en cinco columnas. De izquierda a derecha pesan dieciséis, ocho, cuatro, dos y uno. Pero vamos a preguntar empezando por la columna de la derecha: uno, dos, cuatro, ocho y dieciséis. [TRIGGER_2] Para formar una pregunta, recorremos todo el alfabeto e incluimos las letras que tienen un uno en esa columna. La primera incluye a, c, e, g… y continúa con las demás que cumplen la misma regla. [TRIGGER_3] La segunda incluye b, c, f, g… Observa que una letra puede aparecer en varios grupos. No estamos repartiendo el alfabeto en cinco cajones: estamos leyendo cinco propiedades de cada letra. [TRIGGER_4] Las cinco preguntas quedan preparadas antes de recibir ninguna respuesta. Ahora sí, empezamos una conversación nueva con el juez. El contador vuelve a cero."

##### Descripcion Visual Detallada:
###### Objetos:
- Tabla de ejemplos a,b,c,n,z con Tex para letras y cinco MathTex por fila; cabeceras MathTex(r"16,8,4,2,1") como objetos separados.
- Cinco Tex monoespaciados: r"	exttt{? acegikmoqsuwy}", r"	exttt{? bcfgjknorsvwz}", r"	exttt{? defglmnotuvw}", r"	exttt{? hijklmnoxyz}", r"	exttt{? pqrstuvwxyz}"; etiquetas MathTex Q_0,...,Q_4.
- Tex(r"	ext{Tabla: sólo algunas filas}"); Tex(r"	ext{Consultas: alfabeto completo}"); contador MathTex(r"0/7") y Tex(r"	ext{Traza nueva}").

###### Layout y disposicion:
- Tabla a LEFT*3.65+UP*0.15, ancho 4.8 y alto máximo 3.6. Columna de letra x=-5.35; columnas de bits x=-4.5,-3.85,-3.2,-2.55,-1.9; cabeceras en y=1.8.
- Lista de consultas a RIGHT*3.0, filas y=1.5,0.7,-0.1,-0.9,-1.7; ancho máximo 5.8. Etiquetas de alcance sobre cada panel en y=2.5.
- Contador en RIGHT*5.85+UP*3.25, título alineado a LEFT*2.0+UP*3.25 con ancho máximo 9.0 para dejarlo libre.

##### Secuencia de animacion:
- Duración orientativa: 60 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–16 s: Write de cabeceras de pesos; recorrerlas con un marco desde x=-1.9 hacia x=-4.5. Flecha temporal explícita derecha→izquierda.
- [TRIGGER_2] — 16–33 s: Resaltar la columna peso 1 y formar Q0; aclarar con el rótulo que la tabla muestra sólo ejemplos, mientras la cadena consultada incluye todo el alfabeto correspondiente.
- [TRIGGER_3] — 33–48 s: Resaltar la columna peso 2 y mostrar Q1; destacar la c en ambas consultas. Completar Q2,Q3,Q4 sin ejecutar aún ninguna.
- [TRIGGER_4] — 48–60 s: FadeIn de contador 0/7 y rótulo Traza nueva. Retirar tabla; conservar lista como cola de preguntas, que pasa al panel lateral de la escena 11.

##### Código Cromático y Estilo:
- ACCENT_TERRACOTTA para columna activa; ACCENT_INDIGO para tabla y Q_b; ACCENT_CYAN para cadenas de consulta; TEXT_MAIN para letras; contador sin consumo en TEXT_MUTED.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 11
##### Nombre: Primera pregunta: encender el bit uno
##### Descripcion Breve: La primera respuesta establece las máscaras de las posiciones pares de banana.
##### Objetivo Pedagogico: Mostrar que se actualizan todas las posiciones devueltas y que cero aún significa información incompleta.
##### Voz en off:
> "[TRIGGER_1] La cadena del ejemplo vuelve a ser banana. Nosotros la vemos para comprobar el experimento; el algoritmo sigue sin recibirla. Empieza con todas sus máscaras en cero. [TRIGGER_2] Enviamos la pregunta correspondiente al peso uno. El juez responde con tres posiciones: dos, cuatro y seis. En cada una encendemos ese bit. [TRIGGER_3] Las máscaras quedan cero, uno, cero, uno, cero, uno. Los unos todavía no significan que podamos dar la respuesta completa: faltan cuatro preguntas que podrían encender otros bits. [TRIGGER_4] También anotamos el mayor índice recibido: seis. Por ahora es el mayor que hemos visto, no una prueba general de que ya conozcamos la longitud. Esa garantía llegará al completar las cinco preguntas."

##### Descripcion Visual Detallada:
###### Objetos:
- Fila de seis casillas de laboratorio para banana, separada de fila de seis máscaras MathTex(r"00000"). Índices 1–6 en MathTex; Tex(r"	ext{Vista parcial del arreglo de máscaras}").
- Tex(r"	exttt{? acegikmoqsuwy}"); respuesta MathTex(r"3\quad2\quad4\quad6"); MathTex(r"b=0,\quad2^b=1").
- MathTex(r"M=[0,1,0,1,0,1]"); MathTex(r"\mathrm{maxVisto}=6"); contador MathTex(r"1/7").

###### Layout y disposicion:
- Fila de laboratorio en y=2.0; fila de máscaras en y=0.55; centros x=-4.5+1.8j para j=0,...,5, cada máscara ancho máximo 1.35.
- Índices en y=1.1; consulta y respuesta alternan centradas en y=-0.75; arreglo decimal en y=-1.7; maxVisto en y=-2.6.
- Contador en RIGHT*5.85+UP*3.25. Rótulo de laboratorio en LEFT*3.5+UP*2.7; no mostrar borde final de un arreglo de longitud 6 como dato del algoritmo: es un recorte didáctico de posiciones conocidas al espectador.

##### Secuencia de animacion:
- Duración orientativa: 55 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–13 s: FadeIn del laboratorio rotulado y de máscaras cero. El área del algoritmo no recibe ninguna copia de las letras verdaderas.
- [TRIGGER_2] — 13–25 s: Enviar Q0, incrementar contador a 1/7 y recibir lista. Usar tres Indicate coordinados sobre índices 2,4,6; el primer 3 se marca como cantidad, nunca como índice.
- [TRIGGER_3] — 25–39 s: Transform de las máscaras pares a 00001; actualizar resumen decimal. Mantener el resto como estado parcial, sin decodificar ceros como letras.
- [TRIGGER_4] — 39–55 s: Actualizar maxVisto de 0 a 6; escribir Tex(r"	ext{Provisional}") junto al valor. Mantener fila y contador para continuidad con escena 12.

##### Código Cromático y Estilo:
- ACCENT_MINT para bits recién encendidos; ACCENT_TERRACOTTA para b y peso; ACCENT_CYAN para índices; ceros en TEXT_MUTED; palabra del laboratorio en TEXT_MAIN con opacidad reducida.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 12
##### Nombre: Segunda pregunta: la firma empieza a distinguir
##### Descripcion Breve: El segundo bit separa las posiciones con b o n de las que contienen a.
##### Objetivo Pedagogico: Leer el arreglo parcial como bits acumulados, sin sobrescribir los anteriores.
##### Voz en off:
> "[TRIGGER_1] La siguiente pregunta mira el peso dos. Esta vez aparecen las posiciones uno, tres y cinco. Encendemos el segundo bit en esas tres casillas. [TRIGGER_2] El arreglo pasa a dos, uno, dos, uno, dos, uno. Las aes conservan el bit que ya tenían: una actualización añade información, no borra la anterior. [TRIGGER_3] Por ahora la primera, la tercera y la quinta posición parecen iguales. Es normal. La b y la n comparten sus dos bits de menor peso. [TRIGGER_4] Pero sus firmas completas son diferentes. Aún quedan columnas por leer. No estamos buscando que cada pregunta separe todas las letras; buscamos que lo haga el conjunto de las cinco."

##### Descripcion Visual Detallada:
###### Objetos:
- Continuación exacta de las seis máscaras e índices de escena 11; Tex(r"	exttt{? bcfgjknorsvwz}"); MathTex(r"3\quad1\quad3\quad5").
- MathTex(r"M=[2,1,2,1,2,1]"); tarjetas Tex(r"	exttt{b}") con MathTex(r"00010") y Tex(r"	exttt{n}") con MathTex(r"01110"); contador MathTex(r"2/7").
- SurroundingRectangle sobre dos bits derechos de ambas firmas; Tex(r"	ext{Coinciden sólo en los bits consultados}").

###### Layout y disposicion:
- Conservar casillas x=-4.5+1.8j, y=0.55 e índices y=1.1; laboratorio y=2.0.
- Consulta/respuesta en y=-0.75; resumen decimal en y=-1.55; comparativa b,n en x=-2.4 y 2.4, y=-2.55.
- Retirar temporalmente maxVisto para liberar espacio, sin cambiar su valor almacenado. Contador fijo en esquina superior derecha.

##### Secuencia de animacion:
- Duración orientativa: 52 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–12 s: Enviar Q1 e incrementar contador de 1 a 2; resaltar índices 1,3,5 y el bit de peso dos.
- [TRIGGER_2] — 12–25 s: Transform de máscaras 1,3,5 a 00010; Indicate suave de las máscaras pares conservadas en 00001; actualizar resumen decimal.
- [TRIGGER_3] — 25–38 s: TransformFromCopy de firmas completas b y n al panel inferior. Encerrar sólo sus dos bits bajos, iguales a 10.
- [TRIGGER_4] — 38–52 s: Iluminar las columnas superiores aún sin preguntar en la firma de n, con contorno discontinuo, sin transferirlas todavía a las máscaras del algoritmo. Mantener estado para escena 13.

##### Código Cromático y Estilo:
- ACCENT_MINT para conocimiento acumulado; ACCENT_TERRACOTTA para bit nuevo; ACCENT_INDIGO para comparación b/n; información futura con contorno TEXT_MUTED, no relleno de bit conocido.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 13
##### Nombre: Tres preguntas para terminar la firma
##### Descripcion Breve: Los pesos cuatro y ocho identifican n; el peso dieciséis devuelve una lista vacía.
##### Objetivo Pedagogico: Completar la traza y mostrar que una respuesta vacía aporta ceros legítimos.
##### Voz en off:
> "[TRIGGER_1] Preguntamos por el peso cuatro. El juez devuelve las posiciones tres y cinco. Al encender ese bit, sus máscaras pasan de dos a seis. [TRIGGER_2] Con el peso ocho vuelven a aparecer esas mismas posiciones. Seis se convierte en catorce. Ahora sus bits encendidos pesan dos, cuatro y ocho: dos más cuatro más ocho son catorce. [TRIGGER_3] Falta el peso dieciséis. La respuesta es cero: no vienen índices después. No hay ningún problema. Ninguna letra de banana pertenece a ese grupo, así que todas conservan ese bit apagado. [TRIGGER_4] Ya completamos las cinco preguntas. Las máscaras finales son dos, uno, catorce, uno, catorce, uno. Ahora sí podemos leer las firmas completas."

##### Descripcion Visual Detallada:
###### Objetos:
- Tres consultas Tex: r"	exttt{? defglmnotuvw}", r"	exttt{? hijklmnoxyz}", r"	exttt{? pqrstuvwxyz}"; respuestas separadas MathTex(r"2\quad3\quad5"), MathTex(r"2\quad3\quad5"), MathTex(r"0").
- Máscaras variables 00010→00110→01110 para índices 3 y 5; MathTex(r"2+4+8=14"); resumen final MathTex(r"[2,1,14,1,14,1]").
- Contador 3/7→4/7→5/7; Tex(r"	ext{Lista vacía: ningún bit se enciende}").

###### Layout y disposicion:
- Conservar fila principal y laboratorio en las mismas coordenadas. Retirar comparativa inferior de la escena anterior.
- Mensaje activo en y=-0.7, resumen de estado en y=-1.55; explicación del bit o respuesta vacía en y=-2.5.
- Nunca apilar las tres consultas completas: reemplazar la anterior y guardar sólo su número en un registro lateral pequeño en x=6.0, y=1.9,1.3,0.7.

##### Secuencia de animacion:
- Duración orientativa: 53 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–12 s: Enviar Q2 y cambiar contador a 3/7; leer cantidad 2 e índices 3,5; transformar sólo esas máscaras de 00010 a 00110. Resumen decimal [2,1,6,1,6,1].
- [TRIGGER_2] — 12–27 s: ReplacementTransform del mensaje por Q3; contador 4/7; mismos índices; máscaras a 01110 y resumen [2,1,14,1,14,1]. Escribir 2+4+8=14.
- [TRIGGER_3] — 27–42 s: Enviar Q4, contador 5/7; recibir únicamente 0. Mostrar lista vacía y mantener las seis máscaras sin cambios; no iluminar ninguna casilla ni usar color de error.
- [TRIGGER_4] — 42–53 s: Circumscribe de los cinco bits completos de una máscara; presentar resumen final. El contador permanece en 5/7, porque aún no se ha enviado la respuesta.

##### Código Cromático y Estilo:
- ACCENT_TERRACOTTA para peso activo; ACCENT_MINT para bits confirmados; TEXT_MUTED para cero de respuesta vacía; ACCENT_CYAN para índices; sin rojo en consultas válidas.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 14
##### Nombre: Leer letras y certificar la longitud
##### Descripcion Breve: Las máscaras se decodifican y la cobertura certifica el máximo índice.
##### Objetivo Pedagogico: Separar reconstrucción de letras y prueba de longitud, incluyendo un índice que aparece tarde.
##### Voz en off:
> "[TRIGGER_1] Buscamos cada número en nuestro alfabeto: dos es b; uno es a; catorce es n. Al repetirlo posición por posición aparece banana, ahora reconstruida por el algoritmo. [TRIGGER_2] La longitud también queda certificada. Ninguna letra tiene código cero, así que todas las posiciones, incluida la última, tuvieron que aparecer en alguna respuesta. El mayor índice observado es seis. [TRIGGER_3] ¿Por qué esperamos hasta el final para afirmarlo? Piensa en la cadena a, p. La a aparece al preguntar por el peso uno; la p tiene código dieciséis y no aparece hasta la última pregunta. [TRIGGER_4] Si nos detuviéramos demasiado pronto, creeríamos haber visto sólo una posición. Al completar las cinco consultas, cada posición tiene su oportunidad de hacerse visible."

##### Descripcion Visual Detallada:
###### Objetos:
- Fila final de máscaras y nueva fila de letras reconstruidas con Tex; MathTex(r"2\mapsto b,\quad1\mapsto a,\quad14\mapsto n").
- MathTex(r"n=\maxigcup_{b=0}^{4}R(Q_b)=6"); Tex(r"	ext{Longitud certificada}").
- Panel de contraejemplo separado con Tex(r"	exttt{ap}"), MathTex(r"a:00001"), MathTex(r"p:10000"), MathTex(r"\mathrm{maxVisto}:1\longrightarrow2"); etiqueta Tex(r"	ext{Otro ejemplo; no son nuevas consultas de banana}").

###### Layout y disposicion:
- Máscaras en y=1.3 y letras recuperadas en y=0.2, centros x=-4.5+1.8j. Leyenda de equivalencia en y=-1.0.
- Ecuación de longitud en y=-2.1. Para el contraejemplo, FadeOut de estas filas y presentar panel ap en ORIGIN, ancho 8.8 y alto 3.2.
- Contador banana 5/7 permanece pequeño y atenuado en esquina; el panel ap lleva una etiqueta propia para no sumar mensajes a esa traza.

##### Secuencia de animacion:
- Duración orientativa: 55 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–13 s: TransformFromCopy de cada máscara hacia su letra mediante la tabla conocida; revelar la palabra del algoritmo con contorno sólido, distinto del laboratorio.
- [TRIGGER_2] — 13–27 s: Cambiar maxVisto provisional por n=6 certificado y escribir la unión. Indicate del mayor índice después de destacar que los códigos son no nulos.
- [TRIGGER_3] — 27–43 s: Entrar al panel ap; mostrar primera respuesta {1} y después la última {2}, con sus pesos 1 y 16. No ejecutar un contador de partida en este panel.
- [TRIGGER_4] — 43–55 s: Mover maxVisto de 1 a 2 al llegar al último bit. Cerrar el panel y recuperar discretamente el resumen banana y contador 5/7 para el cierre posterior.

##### Código Cromático y Estilo:
- ACCENT_MINT para letras ya reconstruidas y longitud certificada; ACCENT_TERRACOTTA para aparición tardía de índice 2; ACCENT_INDIGO para panel de contraejemplo; TEXT_MUTED para contador pausado.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 15
##### Nombre: Por qué no puede confundir dos letras
##### Descripcion Breve: Una equivalencia conecta respuesta, bit y código de cada posición.
##### Objetivo Pedagogico: Dar una demostración accesible de corrección y el invariante de acumulación.
##### Voz en off:
> "[TRIGGER_1] La demostración cabe en una pregunta: ¿cuándo aparece la posición j en la respuesta del bit b? Exactamente cuando la letra de esa posición pertenece al grupo que consultamos. [TRIGGER_2] Y construimos ese grupo incluyendo, precisamente, las letras cuyo código tiene ese bit encendido. Por tanto, el bit que registramos coincide con el bit verdadero de la letra oculta. [TRIGGER_3] Después de cada consulta tenemos correctos todos los bits que ya preguntamos. Después de cinco, tenemos el código completo. Como dos letras distintas nunca comparten código, la reconstrucción es única. [TRIGGER_4] Son dos garantías diferentes trabajando juntas: los códigos distintos identifican las letras; los códigos no nulos hacen visibles todas las posiciones. Así recuperamos tanto el contenido como la longitud."

##### Descripcion Visual Detallada:
###### Objetos:
- MathTex(r"j\in R(Q_b)\iff s_j\in Q_b\iff\operatorname{bit}_b(c(s_j))=1"), separada en tres fragmentos para revelado progresivo.
- Una máscara de cinco celdas y un marco para bits consultados; MathTex(r"M_j=c(s_j)") y Tex(r"	ext{al terminar las cinco consultas}").
- Dos tarjetas con MathTex(r"	ext{Códigos distintos}\Rightarrow	ext{letra única}") y MathTex(r"	ext{Códigos no nulos}\Rightarrow	ext{posición visible}").

###### Layout y disposicion:
- Equivalencia centrada en UP*1.3, ancho máximo 11.8; glosa de j como posición y b como bit en y=2.25.
- Máscara centrada en DOWN*0.15; igualdad final en DOWN*1.15.
- Tarjetas inferiores de ancho 5.3 en LEFT*3.0+DOWN*2.4 y RIGHT*3.0+DOWN*2.4. No superponer la prueba con el laboratorio.

##### Secuencia de animacion:
- Duración orientativa: 56 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–14 s: Write de los dos primeros fragmentos y flecha de equivalencia; resaltar j como índice y no como cantidad de resultados.
- [TRIGGER_2] — 14–28 s: Escribir el tercer fragmento; TransformFromCopy de un bit verdadero hacia el correspondiente bit de la máscara.
- [TRIGGER_3] — 28–42 s: Ampliar el marco de bits conocidos paso a paso hasta cubrir cinco celdas; reemplazar estado parcial por Mj=c(sj). Mostrar dos códigos distintos que difieren en al menos una columna.
- [TRIGGER_4] — 42–56 s: FadeIn de las dos tarjetas y conectarlas a contenido y longitud. Retirar fórmulas auxiliares, dejando ambas garantías como cierre de la prueba.

##### Código Cromático y Estilo:
- ACCENT_CYAN para equivalencias; ACCENT_TERRACOTTA para bit activo; ACCENT_MINT para igualdad demostrada; ACCENT_INDIGO para las dos garantías.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 16
##### Nombre: El algoritmo como un tablero de luces
##### Descripcion Breve: Un bitmask por posición acumula respuestas mediante OR.
##### Objetivo Pedagogico: Traducir la idea a estados de implementación sin mostrar un bloque de código.
##### Voz en off:
> "[TRIGGER_1] Para programarlo, cada posición necesita una pequeña máscara de cinco bits. Al principio están todos apagados. Preparamos las cinco preguntas y las enviamos una por una. [TRIGGER_2] En cada respuesta leemos primero la cantidad de índices. Luego recorremos exactamente esos índices y encendemos, en sus máscaras, el bit de la pregunta actual. Los demás bits se conservan. [TRIGGER_3] Esa operación se llama OR: añadir un uno donde corresponde sin apagar los anteriores. Por ejemplo, una máscara que vale seis se combina con el peso ocho y pasa a valer catorce. [TRIGGER_4] También actualizamos el mayor índice visto. Al terminar, traducimos los códigos a letras. Y, al hablar con el juez, cada mensaje debe enviarse de verdad: vaciamos el búfer antes de esperar su respuesta."

##### Descripcion Visual Detallada:
###### Objetos:
- VGroup de cinco celdas por máscara; MathTex(r"M_j\leftarrow M_j\mathbin{\mathrm{OR}}2^b"); MathTex(r"	ext{Preguntar}\ \longrightarrow\ 	ext{Leer}\ \longrightarrow\ 	ext{Acumular}").
- Columna de MathTex con operación alineada: 00110, 01000, 01110; etiquetas MathTex(r"6"), MathTex(r"8"), MathTex(r"14").
- Respuesta modelo MathTex(r"k\quad i_1\quad\cdots\quad i_k"); MathTex(r"\mathrm{maxVisto}\leftarrow\max(\mathrm{maxVisto},i_r)").
- Pequeño panel Rectangle de búfer con Tex(r"	exttt{flush}") y Arrow hacia juez; no usar Code, Text, MarkupText ni bloque C++.

###### Layout y disposicion:
- Flujo de tres etapas en y=2.0, centros x=-4.1,0,4.1; respuesta modelo en LEFT*3.3+UP*0.8.
- Máscara activa y operación OR en RIGHT*2.7+DOWN*0.35; cada columna binaria con paso 0.45, cifras decimales a su derecha.
- Actualización del máximo en LEFT*2.5+DOWN*1.3, ancho máximo 6; búfer y flecha en y=-2.5. Contador de banana pausado y atenuado: esta escena describe operaciones, no consultas nuevas.

##### Secuencia de animacion:
- Duración orientativa: 58 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–13 s: Crear flujo de tres etapas y una máscara cero; indicar el paso de preguntar sin incrementar el contador de la traza principal.
- [TRIGGER_2] — 13–27 s: Indicate de k; mover un pequeño Triangle puntero de i1 a ik; para cada índice, iluminar sólo la celda del bit b en su máscara. No leer números después de k=0.
- [TRIGGER_3] — 27–42 s: Write de la operación binaria vertical y Transform de 00110 a 01110 mediante OR con 01000. Alinear siempre pesos 16,8,4,2,1.
- [TRIGGER_4] — 42–58 s: Actualizar la ficha maxVisto y señalar conversión final. Animar salida del mensaje del búfer hacia juez al indicar flush; sólo después mostrar la flecha de respuesta. Evitar un retardo que parezca nueva condición matemática.

##### Código Cromático y Estilo:
- ACCENT_MINT para OR y bits conservados; ACCENT_CYAN para flujo y mensajes; ACCENT_TERRACOTTA para puntero; TEXT_MUTED para posiciones no visitadas; ACCENT_INDIGO para memoria.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 17
##### Nombre: Las pruebas que intentan romper la idea
##### Descripcion Breve: Una letra, letras repetidas y respuestas vacías comprueban la robustez.
##### Objetivo Pedagogico: Reforzar que la solución no depende de variedad de letras ni de longitud conocida.
##### Voz en off:
> "[TRIGGER_1] Probemos los extremos. Si la cadena tiene sólo una a, su código es uno: aparece en la primera pregunta y el mayor índice recibido es uno. Ya sabemos tanto la letra como la longitud. [TRIGGER_2] Si la cadena tiene cuatro zetas, todas comparten el código veintiséis. Las cuatro posiciones aparecen en las mismas preguntas, pero cada una mantiene su propia máscara. No se mezclan por tener la misma letra. [TRIGGER_3] Y si una pregunta devuelve una lista vacía, no hacemos ninguna actualización. Recibir cero posiciones es una respuesta válida; no significa que la cadena esté vacía. [TRIGGER_4] Lo que nunca puede ocurrir, con nuestras firmas, es que una posición real quede ausente de las cinco respuestas. Ésa es la garantía que necesitábamos cuando descartamos el código cero."

##### Descripcion Visual Detallada:
###### Objetos:
- Tres tarjetas con Tex(r"	exttt{a}"), Tex(r"	exttt{zzzz}") y MathTex(r"R(Q_b)=arnothing"); códigos MathTex(r"00001") y MathTex(r"11010").
- Cuatro máscaras independientes bajo zzzz y cuatro índices; MathTex(r"26=16+8+2"); Tex(r"	ext{Misma letra, posiciones distintas}").
- MathTex(r"n\ge1"); Tex(r"	ext{Una respuesta vacía no es una cadena vacía}"); cinco puntos de consulta con al menos uno encendido.

###### Layout y disposicion:
- Tarjetas de casos en centros x=-4.2,0,4.2, y=0.6, ancho máximo 3.7 y alto 3.4.
- Códigos dentro de cada tarjeta en y=0.1; máscaras repetidas en dos filas para mantener legibilidad; índices separados de bits.
- Conclusión en y=-2.25, ancho máximo 11.5. Rótulo Tex(r"	ext{Pruebas separadas}") en UP*2.5; no heredar contador 5/7 como si las pruebas fueran parte de esa conversación.

##### Secuencia de animacion:
- Duración orientativa: 59 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–16 s: Revelar tarjeta a; encender b0 y mostrar índice 1, sin generar tarjetas de consultas innecesarias.
- [TRIGGER_2] — 16–32 s: Revelar zzzz; encender bits b1,b3,b4 en cada máscara por separado. Subrayar cuatro índices distintos y mantener repetido el valor 26.
- [TRIGGER_3] — 32–45 s: Revelar tarjeta de respuesta vacía; mantener intacta su máscara y escribir la distinción respecto de cadena vacía.
- [TRIGGER_4] — 45–59 s: Encender al menos un punto de los cinco para cada posición de los dos ejemplos; Circumscribe de la garantía no nula. FadeOut de tarjetas, preparada la transición a costo.

##### Código Cromático y Estilo:
- ACCENT_MINT para casos que cumplen; TEXT_MUTED para respuesta vacía y bits cero; ACCENT_CYAN para índices diferentes; ACCENT_INDIGO para marcos; sin advertencias rojas artificiales.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 18
##### Nombre: Cinco preguntas no significan tiempo constante
##### Descripcion Breve: La cuenta de mensajes se separa del trabajo de procesar una cadena de longitud n.
##### Objetivo Pedagogico: Explicar O(n) tiempo y espacio, distinguiéndolos de las cinco consultas.
##### Voz en off:
> "[TRIGGER_1] Usamos cinco preguntas sin importar la longitud. Pero eso no significa que el programa haga trabajo constante. Si la cadena es larga, las respuestas también pueden traer muchos índices. [TRIGGER_2] En cada pregunta llegan como máximo n posiciones. A lo largo de cinco preguntas procesamos como máximo cinco n índices, y después recorremos las n posiciones para escribir la palabra. [TRIGGER_3] Como el alfabeto tiene siempre veintiséis letras, preparar los grupos cuesta una cantidad fija. El tiempo total crece linealmente con la longitud: orden de n. [TRIGGER_4] Guardamos una máscara por posición y la respuesta reconstruida: también orden de n en memoria. Pocas interacciones con el juez; trabajo proporcional a la información que tenemos que leer y producir."

##### Descripcion Visual Detallada:
###### Objetos:
- MathTex(r"5\ 	ext{consultas}"); MathTex(r"\sum_{b=0}^{4}|R(Q_b)|\le5n"); MathTex(r"O(5\cdot26+5n+n)=O(n)").
- Cinco barras Rectangle que representan tamaños de respuestas, todas acotadas por n; Brace con MathTex(r"n") y contador de índices procesados.
- Fila extensible de máscaras con MathTex(r"\cdots") y Tex(r"	ext{Una máscara por posición}"); MathTex(r"	ext{memoria}=O(n)").

###### Layout y disposicion:
- Cinco barras en LEFT*3.1, y=1.7,1.0,0.3,-0.4,-1.1; longitud máxima 4.5, alineadas a x=-5.5.
- Ecuaciones en RIGHT*2.8, y=1.6,0.3,-1.3; ancho máximo 5.7. Fila de memoria en y=-2.6, ancho máximo 11.
- Nota técnica sólo en storyboard: la referencia de guion_sol.md reserva 10001 enteros por la cota conocida; el O(n) describe la memoria suficiente para máscaras de las posiciones existentes. No presentar la reserva fija concreta como un arreglo cuyo tamaño depende del n recibido inicialmente.

##### Secuencia de animacion:
- Duración orientativa: 55 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–14 s: Escribir cinco consultas en la parte superior del panel; hacer crecer la longitud de las barras al aumentar n para separar número de mensajes de volumen de datos.
- [TRIGGER_2] — 14–28 s: Sumar visualmente las cinco longitudes con una Brace; mostrar límite 5n sin afirmar que todas las cadenas lo alcanzan.
- [TRIGGER_3] — 28–40 s: Write de la expresión de costo y TransformMatchingTex hacia O(n), manteniendo clara la hipótesis de alfabeto fijo.
- [TRIGGER_4] — 40–55 s: Extender la fila de máscaras con puntos suspensivos y escribir memoria O(n). Colorear el costo lineal como una solución válida, no como ineficiencia: también hay que producir n letras.

##### Código Cromático y Estilo:
- ACCENT_INDIGO para memoria y barras; ACCENT_CYAN para índices procesados; ACCENT_MINT para O(n) como costo apropiado; ACCENT_TERRACOTTA para n; no usar ACCENT_VINO sólo por ser lineal.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.

#### Escena: 19
##### Nombre: La respuesta y la idea que nos llevamos
##### Descripcion Breve: La conversación principal termina con banana y seis mensajes consumidos.
##### Objetivo Pedagogico: Cerrar el protocolo y condensar el aprendizaje transferible sobre diseño de consultas.
##### Voz en off:
> "[TRIGGER_1] Volvamos a nuestra conversación. Ya hicimos las cinco preguntas y reconstruimos banana. Enviamos la respuesta final; el contador pasa de cinco a seis. El juez confirma que es correcta y terminamos. [TRIGGER_2] Nos quedó un mensaje de margen. La solución oficial usa los siete: primero averigua la longitud. Nuestra variante integra esa información en las propias firmas, sin permitir códigos completamente apagados. [TRIGGER_3] La lección va más allá del ahorcado. Cuando puedes preguntar por grupos, no siempre conviene buscar un elemento a la vez. Puedes diseñar preguntas para que cada elemento deje una firma diferente. [TRIGGER_4] Una pregunta puede ser ambigua. Cinco preguntas, elegidas para complementarse, pueden revelar una cadena entera. [Pausa.] A veces, resolver un problema empieza por aprender a preguntarlo."

##### Descripcion Visual Detallada:
###### Objetos:
- Tex(r"	exttt{! banana}") y Tex(r"	exttt{correct}"); seis casillas reconstruidas, contador MathTex(r"5/7\longrightarrow6/7").
- Dos etiquetas MathTex(r"	ext{Oficial: }1+5+1=7") y MathTex(r"	ext{Sin código cero: }5+1=6").
- Una pequeña matriz de firmas y Tex(r"	ext{Preguntas que se complementan}"); crédito Tex(r"	ext{Hardcore Hangman — GCPC 2022}").

###### Layout y disposicion:
- Palabra reconstruida en UP*1.45; algoritmo/juez en x=-4.5 y 4.5, y=0.2; mensaje cruza corredor central.
- Contador en RIGHT*5.85+UP*3.25. Comparación de estrategias en y=-1.1 y -1.9, centrada.
- Cierre conceptual en ORIGIN tras retirar comparación; crédito en DOWN*3.25. Sólo una idea grande en pantalla durante la última frase.

##### Secuencia de animacion:
- Duración orientativa: 58 s. Tiempo local desde el inicio de esta escena; los holds se ajustan a la voz definitiva.
- [TRIGGER_1] — 00–15 s: Recuperar el estado de la traza banana en 5/7. Enviar ! banana con flush representado por salida efectiva; incrementar a 6/7 una sola vez. Recibir correct sin incrementar de nuevo: el veredicto del juez no es un mensaje del programa. Detener interacción.
- [TRIGGER_2] — 15–29 s: Mostrar comparación 7 frente a 6 con ambos resultados válidos en verde; dejar una ficha de margen sin usar. No anunciar que cinco mensajes totales bastan.
- [TRIGGER_3] — 29–44 s: TransformFromCopy de las cinco columnas a una pequeña matriz de firmas; encender patrones distintos y escribir el cierre conceptual.
- [TRIGGER_4] — 44–58 s: FadeOut de matriz y conservar únicamente la frase y el crédito; hold de dos segundos tras la pausa y FadeOut suave a BG_COLOR. No añadir una explicación técnica después del cierre.

##### Código Cromático y Estilo:
- ACCENT_MINT para correct y ambas estrategias válidas; ACCENT_CYAN para mensajes; ACCENT_TERRACOTTA para respuesta final; TEXT_MUTED para ficha sobrante; TEXT_MAIN para cierre.
- Textos con Tex/MathTex y fondo BG_COLOR; respetar las convenciones globales de contraste, área segura y orden de bits.
