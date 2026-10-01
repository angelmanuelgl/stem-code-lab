# Guion storyboard / técnico — GATA-CAT

## Convenciones generales de producción

- **Alcance y fuente:** narrativa y especificación visual exclusivamente de GATA-CAT. Fuente conceptual única: `guion_sol.md` de esta carpeta. La paleta se contrastó con el módulo global `styles/theme.py`. No se implementan escenas Python ni se producen renders en esta entrega.
- **Arco:** misterio y definición por posiciones → intentos que fallan → esqueleto AT → derivaciones de los pesos → independencia → construcción y traza → prueba de exactitud → prueba analítica de longitud → fronteras, costos y verificación → cierre. Las demostraciones se desarrollan antes de usarlas como garantía.
- **Formato:** 16:9; frame lógico de Manim de ancho 128/9 y alto 8, centro `(0,0,0)`. Área segura ordinaria: x entre −6.3 y 6.3, y entre −3.5 y 3.5. Fondo `BG_COLOR`. Título de escena en `(0,3.18,0)`, ancho máximo 11.7 y alto máximo 0.65; partir títulos largos en dos líneas y reducir sólo el título a 30–34 pt cuando sea necesario. La zona del título se reserva y no contiene arcos ni datos.
- **Tipografía:** construir todo texto visible con `Tex` o `MathTex`: títulos, índices, palabras, contadores, créditos y etiquetas. Letras y cadenas con `Tex` monoespaciado; índices y ecuaciones con `MathTex`. Texto principal de 28–34 pt, ecuaciones de 30–36 pt, letras de casillas de 32–38 pt, índices de 24 pt. En las tablas densas se permiten 23–24 pt con paneles suficientemente anchos y una fila activa ampliada. No usar bloques de código, capturas de terminal, listados de pseudocódigo ni el objeto `Code`.
- **Objetos Manim:** fichas como `VGroup` de `RoundedRectangle`, letra `Tex` e índice `MathTex`; rutas como `CurvedArrow` o `Arrow` por encima de casillas; huecos con `Circle`; punteros con `Triangle`; llaves con `Brace`; marcos con `SurroundingRectangle`; tablas como grupos de celdas y textos. Separar flechas y textos para que ningún conector atraviese un rótulo. Los constructores se especifican como recursos de implementación posterior, no como código visible al espectador.
- **Paleta real:** `BG_COLOR=#181C24`, `TEXT_MAIN=#ECEFF4`, `TEXT_MUTED=#64748B`, `ACCENT_VINO=#C0392B`, `ACCENT_MINT=#2DD4BF`, `ACCENT_TERRACOTTA=#D97706`, `ACCENT_INDIGO=#6366F1`, `ACCENT_CYAN=#38BDF8`. No introducir nombres de color inexistentes. C conserva cian, G índigo, A verde y T terracota a lo largo del video. Diferenciar contadores, grupos y estados mediante rótulos y bordes además del color. Rojo se reserva para un desacuerdo demostrado o una restricción incumplida; un cero válido no es un error.
- **Significado de las letras:** cada ficha representa una posición física de la cadena; no se consume al seleccionarla para una aparición. Posiciones originales se numeran desde 1. Índices a,b,c designan números de pares del esqueleto y se distinguen de índices físicos de la cadena. En las escenas 18 y 19 todas las rutas utilizan posiciones originales del 1 al 11.
- **Nombres de cantidades:** G y C de la entrada son objetivos de patrones. En la prueba usar `G_0,C_0` para objetivos originales y `r_G,r_C` para residuos. `T_i` es el peso CAT de una C y `V_i` el peso GATA de una G, definidos por el sufijo con i pares; no son cantidades de letras T o G. Cantidades de letras insertadas: `a_i,b_i`; totales de letras: `n_C,n_G`. En el verificador `w_j` cuenta elecciones para un prefijo de patrón de longitud j.
- **Peso GATA:** el esqueleto `(AT)^i` contiene ATA, pero no GATA porque no tiene G. `V_i` cuenta esos ATA y, de manera equivalente, los GATA que crea una G anterior. No repetir el comentario incorrecto del código de referencia que asigna GATA a una cadena sin G.
- **Sincronización:** cada escena reinicia su numeración de triggers en 1. La identidad completa es `(número de escena, número de trigger)`. Cada bloque de voz de este storyboard es una copia literal del correspondiente bloque de `guion_voz.md`. Ninguna transición, cambio de contador, ruta nueva o fórmula nueva aparece sin el trigger que se especifica. Los triggers son marcas verbales; las ventanas temporales siguientes son estimaciones locales a 145 palabras por minuto más pausas y lectura, y se reajustan a la grabación final.
- **Ritmo:** interpretar `[Pausa.]` como unos 1.5 s de silencio, sin pronunciar la indicación. Animaciones simples de 0.5–1 s y transformaciones de 1–1.5 s; secuencias de enumeración se escalonan según se nombran sus elementos. Mantener las fórmulas quietas mientras se explica su significado. Los tiempos de cada trigger incluyen holds; si una acción no cabe, alargar su ventana, sin acelerar la locución ni omitir pasos.
- **Transiciones y continuidad:** la primera acción de cada escena retira objetos no heredados y crea la composición especificada. Toda limpieza y cambio de título pertenece al primer trigger, no a una transición sin marca. Las escenas 15–17 heredan cadena y contabilidad; si se renderizan por separado, recrean exactamente el estado final previo. Las escenas 18–19 usan la misma cadena y coordenadas. Los recorridos de enumeración se apagan entre elecciones, pero sus tarjetas permanecen como inventario. En la traza no añadir pares aún no emitidos como si fueran letras reales: los futuros se representan con contorno punteado.
- **Escalas:** las barras de longitud de la escena 29 sí son proporcionales a la cota 500. Los números de apariciones y objetivos se muestran como cantidades simbólicas sin una falsa escala espacial. Multiplicidades muy grandes se representan con grupos y llaves rotulados; todos los casos pequeños anunciados como completos se enumeran íntegramente.
- **Rigor del greedy:** garantiza representación exacta y una cota de tamaño para este dominio. No garantiza mínima longitud, ni mínimo número de C/G. Las cotas 101,12 y 401 son conservadoras, no máximos afirmados como alcanzados. La comprobación finita adicional 100,10 y 398 se identifica separadamente y no sustituye la prueba analítica.
- **Accesibilidad:** cada función del color tiene un rótulo, índice o contorno asociado. Texto indispensable usa `TEXT_MAIN`; `TEXT_MUTED` se reserva para referencias secundarias y objetos inactivos. Los índices físicos permanecen legibles en las enumeraciones. No depender de audio, música o assets externos para comunicar los argumentos.

## Escena: 01

## Nombre: Un millón de gatos en una cadena de quinientas letras

## Descripcion Breve: Dos contadores enormes deben surgir de una secuencia muy pequeña.

## Objetivo Pedagogico: Crear el misterio de una construcción combinatoria y establecer exactamente qué se pide.

## Voz en off:

> “[TRIGGER_1] Imagina que te entregan dos números y te piden fabricar una cadena de ADN. Uno cuenta cuántas veces podemos encontrar GATA. El otro, cuántas veces podemos encontrar CAT. Los números pueden llegar a un millón. Pero la cadena que construyamos no puede superar las quinientas letras. [Pausa.] ¿Cómo metemos un millón de gatos en un espacio tan pequeño?
> [TRIGGER_2] Tenemos cuatro letras disponibles: C, G, A y T. Podemos elegir su orden y repetirlas. Nos llegarán hasta mil solicitudes, y cada una trae primero el objetivo de GATA y después el de CAT. Los llamaré objetivo G y objetivo C; esos nombres se refieren a cantidades de apariciones, no a cuántas letras G o C vamos a escribir.
> [TRIGGER_3] No buscamos la cadena más corta del universo. Nos basta una cadena no vacía que acierte exactamente ambos números y tenga como máximo quinientos caracteres. Esa diferencia nos da libertad: podemos buscar una construcción fácil de controlar, aunque otra fuera un poco más breve.
> [TRIGGER_4] El truco que vamos a descubrir depende de una palabra: encontrar. Aquí no significa leer letras pegadas. Podemos saltarnos letras intermedias. Antes de construir nada, necesitamos entender cómo se cuentan esas elecciones. Porque una sola cadena puede esconder muchas más apariciones de las que parece.”

## Descripcion Visual Detallada:

## Objetos:

- Título con Tex; dos tarjetas MathTex para objetivos G y C; cuatro fichas Tex monoespaciadas C, G, A, T; regla horizontal de capacidad con extremos 1 y 500.
- Cadena inicial de 12 casillas vacías y dos contadores independientes; MathTex con 0≤G,C≤10^6 y Q≤1000; crédito pequeño Tex: GATA-CAT · ICPC Latin America Championship 2026.
- Todos los contadores de patrones llevan el patrón completo en el rótulo. Las cantidades de letras, que aparecerán después, se rotulan por separado.

## Layout y disposicion:

- Título en (0,3.15,0), ancho máximo 11.8. Tarjeta G en (-3.2,1.8,0) y tarjeta C en (3.2,1.8,0), cada una de 4.6×1.15.
- Cuatro fichas centradas en x=-2.25,-0.75,0.75,2.25 e y=0.15. Regla de longitud de x=-5.8 a 5.8 en y=-1.55; texto de restricciones en (0,-2.55,0). Crédito en (0,-3.25,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:28:** Crear las dos tarjetas en cero y transformar sus números hasta 10^6, sin representarlos como un conteo ya logrado. Crear la regla 500 y una llave que abarque las 12 casillas de muestra, rotuladas como maqueta. Mantener inmóvil el contraste durante la pregunta y la pausa.
- **[TRIGGER_2] — 00:28–00:55:** Reemplazar la maqueta por las cuatro fichas del alfabeto. Indicar primero la tarjeta G y luego la C mediante dos pulsos sucesivos; escribir las cotas y Q. No convertir el número de solicitudes en letras de la cadena.
- **[TRIGGER_3] — 00:55–01:16:** Añadir bajo la regla la desigualdad 1≤L≤500 y un sello de condición suficiente. La regla conserva su longitud fija: no sugerir que el resultado deba ocupar las 500 posiciones.
- **[TRIGGER_4] — 01:16–01:37:** Transformar las cuatro fichas en una pequeña cadena con huecos. Trazar un arco que salta una casilla intermedia, aún sin asignarle un conteo. Retirar tarjetas y regla al final del trigger; conservar título y preparar la cadena CAATT de la escena siguiente.

- **Duración orientativa de la escena:** 01:37. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- C en ACCENT_CYAN, G en ACCENT_INDIGO, A en ACCENT_MINT y T en ACCENT_TERRACOTTA. Cotas y crédito en TEXT_MAIN/TEXT_MUTED; BG_COLOR constante. No usar rojo para números grandes que son objetivos válidos.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 02

## Nombre: La misma palabra, cuatro elecciones distintas

## Descripcion Breve: CAATT contiene cuatro CAT como subsecuencias y ninguna CAT contigua.

## Objetivo Pedagogico: Distinguir posiciones, subsecuencias y subcadenas mediante una enumeración completa.

## Voz en off:

> “[TRIGGER_1] Miremos esta cadena: C, A, A, T, T. Numeramos sus posiciones del uno al cinco. Si exigimos letras consecutivas, no aparece CAT: después de C vienen dos aes. Pero si podemos saltarnos posiciones, la historia cambia. Tenemos una C, dos opciones para la A y dos opciones para la T.
> [TRIGGER_2] Primera elección: posiciones uno, dos y cuatro. Segunda elección: uno, dos y cinco. Escriben la misma palabra, CAT, pero usan una T diferente; por eso cuentan como dos apariciones. No estamos contando palabras distintas. Estamos contando maneras distintas de elegir posiciones en orden.
> [TRIGGER_3] Tercera elección: uno, tres y cuatro. Cuarta elección: uno, tres y cinco. Son todas: la C está fija, elegimos una de las dos aes y después una de las dos tes. Dos por dos: cuatro. Cada arco siempre avanza hacia la derecha; saltar está permitido, retroceder no.
> [TRIGGER_4] La regla formal para CAT pide tres índices estrictamente crecientes, con las letras C, A y T en esas posiciones. Estrictamente significa que una posición no se puede usar dos veces. Y esta es la primera pista: no necesitamos escribir una copia separada de cada gato. Muchas apariciones pueden compartir letras.”

## Descripcion Visual Detallada:

## Objetos:

- Cinco fichas Tex de CAATT, índices MathTex 1 a 5, dos arcos por selección y cuatro tarjetas con ternas (1,2,4), (1,2,5), (1,3,4), (1,3,5).
- Dos ventanas de tres caracteres contiguos y luego una tercera, para revisar CAA, AAT y ATT; fórmula MathTex N_CAT=4 y condición i<j<k.

## Layout y disposicion:

- Fichas en x=-4,-2,0,2,4 e y=1.45; índices debajo en y=0.85. Arcos en la franja y=1.8 a 2.75, sin invadir el título.
- Tarjetas de ternas en (-3.2,-0.65,0),(3.2,-0.65,0),(-3.2,-1.6,0),(3.2,-1.6,0). Condición y resultado en (0,-2.8,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Limpiar la composición anterior al inicio y crear las cinco fichas numeradas. Mover una ventana de tres casillas por los inicios 1,2,3; escribir cada bloque observado y apagarlo. Crear dos pequeñas llaves que señalen las dos opciones A y las dos opciones T.
- **[TRIGGER_2] — 00:23–00:43:** Iluminar y recorrer exactamente 1→2→4; copiar sus índices a la primera tarjeta. Apagar los arcos y recorrer 1→2→5; llenar la segunda tarjeta. Las letras originales permanecen, porque una elección no consume la cadena.
- **[TRIGGER_3] — 00:43–01:05:** Recorrer 1→3→4 y 1→3→5, cada uno con su tarjeta. Encender las cuatro tarjetas y transformar las llaves de dos opciones en 2·2=4. Mantener un borde distinto para cada selección, incluso cuando la palabra leída coincide.
- **[TRIGGER_4] — 01:05–01:29:** Escribir i<j<k y la definición abreviada por posiciones debajo del resultado. TransformFromCopy de la misma C y una misma T hacia dos tarjetas para enfatizar que pueden compartirse entre apariciones diferentes. Retirar arcos, conservar por un instante la cadena y fundirla al siguiente ejemplo.

- **Duración orientativa de la escena:** 01:29. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Mantener el color de cada letra. Arcos en ACCENT_CYAN y tarjetas en TEXT_MAIN; selecciones activas con borde ACCENT_TERRACOTTA. Las ventanas contiguas sin coincidencia se atenúan en TEXT_MUTED: no son errores del espectador.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 03

## Nombre: Las dos aes de GATA tienen papeles diferentes

## Descripcion Breve: GATATA permite enumerar cuatro GATA y ver la exigencia de orden.

## Objetivo Pedagogico: Entender a≤b<c antes de introducir el esqueleto y evitar contar combinaciones fuera de orden.

## Voz en off:

> “[TRIGGER_1] Ahora probemos G, A, T, A, T, A. La G está en la posición uno. Para formar GATA necesitamos una A, luego una T y luego otra A. Las dos aes deben ocupar posiciones diferentes, y la segunda debe quedar después de la T. No basta con tomar cualquier par de aes.
> [TRIGGER_2] Si elegimos la T de la posición tres, antes de ella sólo podemos usar la A de la posición dos. Después tenemos dos opciones: la A de la posición cuatro o la de la seis. Obtenemos las elecciones uno, dos, tres, cuatro; y uno, dos, tres, seis.
> [TRIGGER_3] Si elegimos la T de la posición cinco, antes podemos tomar la A de la posición dos o la de la cuatro; después sólo queda la A de la seis. Aparecen uno, dos, cinco, seis; y uno, cuatro, cinco, seis. Dos más dos: cuatro apariciones.
> [TRIGGER_4] ¿Por qué no vale poner la A de la seis como primera A? [Pausa.] Porque ya no hay una T y otra A a su derecha. En CAT elegimos un par ordenado A, T. En GATA elegimos un triple ordenado A, T, A, después de la G inicial. Esa diferencia va a producir dos familias de números distintas.”

## Descripcion Visual Detallada:

## Objetos:

- Seis fichas GATATA con índices 1..6; cuatro tarjetas con cuaternas (1,2,3,4),(1,2,3,6),(1,2,5,6),(1,4,5,6).
- Un puntero triangular sobre la T activa; llaves de opciones A anteriores y posteriores; rótulo MathTex i<j<k<l.

## Layout y disposicion:

- Fichas en x=-5,-3,-1,1,3,5 e y=1.25; índices en y=0.65. Puntero en y=2.05.
- Tarjetas en dos columnas de ancho 5.2 centradas en x=-3.1 y 3.1; filas y=-0.6 y -1.5. Regla de orden y total en y=-2.65.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Recrear sólo fondo y título; escribir cadena e índices. Marcar con dos subrayados diferentes los papeles primera A y última A, sin cambiar el color intrínseco de la letra. Crear las cuatro tarjetas vacías.
- **[TRIGGER_2] — 00:24–00:46:** Mover puntero a T de índice 3. Dibujar llave izquierda que contiene sólo índice 2 y llave derecha con 4 y 6. Trazar las dos rutas completas desde 1 y llenar las dos primeras tarjetas.
- **[TRIGGER_3] — 00:46–01:07:** Mover puntero a T de índice 5; actualizar llaves a {2,4} y {6}. Trazar las dos rutas restantes y llenar las otras tarjetas. Escribir 2+2=4 sin duplicar ni fusionar selecciones.
- **[TRIGGER_4] — 01:07–01:35:** Llevar un pequeño selector a A de índice 6; mostrar vacía la región posterior y suspenderlo durante la pausa. Restaurar las cuatro rutas válidas, escribir la desigualdad estricta y separar visualmente los papeles AT y ATA para la transición.

- **Duración orientativa de la escena:** 01:35. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- G en ACCENT_INDIGO; A y T conservan sus colores. Diferenciar primera/última A mediante subrayados y rótulos, no mediante dos significados incompatibles del color verde. Región sin opciones en TEXT_MUTED.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 04

## Nombre: Copiar gatos fabrica gatos que no habíamos pedido

## Descripcion Breve: CATCAT produce cuatro CAT, no dos, por elecciones que cruzan la frontera.

## Objetivo Pedagogico: Mostrar la interferencia de concatenar construcciones independientes.

## Voz en off:

> “[TRIGGER_1] El primer intento sería escribir una copia de CAT por cada aparición que queremos. Si pedimos dos, escribimos CATCAT. Son sólo seis letras. Parece perfecto. Pero nuestra definición permite saltar entre las copias. [Pausa.] ¿Cuántos gatos aparecen realmente?
> [TRIGGER_2] Desde la C de la posición uno podemos elegir A en dos y T en tres, o A en dos y T en seis, o A en cinco y T en seis. Son tres apariciones. Las dos últimas atraviesan la separación que nosotros imaginábamos entre las copias.
> [TRIGGER_3] Desde la C de la posición cuatro sólo queda A en cinco y T en seis. Una aparición más. En total, cuatro. Queríamos dos y obtuvimos cuatro. La cadena no conoce nuestras etiquetas de primera copia y segunda copia: sólo conoce el orden de sus posiciones.
> [TRIGGER_4] Y repetir una copia por unidad tampoco cabe cuando el objetivo llega a un millón. Tenemos dos obstáculos: demasiadas letras y apariciones que se mezclan. La construcción que buscamos tiene que multiplicar las elecciones sin perder el control de esos cruces. Necesitamos diseñar la interacción, no ignorarla.”

## Descripcion Visual Detallada:

## Objetos:

- Cadena CATCAT numerada, separador punteado entre índices 3 y 4, rótulos copia 1 y copia 2 y cuatro rutas completas.
- Contadores objetivo 2 y resultado 4; barras MathTex 3·10^6 y límite 500 para el intento de una copia por unidad.

## Layout y disposicion:

- Seis fichas en x=-5,-3,-1,1,3,5 e y=1.2. Separador en x=0, desde y=0.45 hasta 2.4. Rótulos de copias en (-3,2.45,0) y (3,2.45,0).
- Rutas resumidas como ternas en x=-3.2, y=-0.7,-1.3,-1.9 y x=3.2,y=-0.7. Comparación de objetivos en (3.2,-2.2,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear dos copias separadas, acercarlas y conservar el separador de referencia. Escribir objetivo 2; durante la pregunta dejar contador resultado en signo de interrogación.
- **[TRIGGER_2] — 00:19–00:41:** Fijar C de índice 1 y animar rutas 1→2→3, 1→2→6 y 1→5→6. Cada una suma exactamente una unidad al contador y llena su tarjeta; las rutas que cruzan x=0 reciben un breve halo ACCENT_VINO.
- **[TRIGGER_3] — 00:41–01:03:** Fijar C de índice 4 y animar 4→5→6. Llevar contador a 4; retirar el separador y las etiquetas de copias para evidenciar que no restringen las subsecuencias.
- **[TRIGGER_4] — 01:03–01:25:** Retirar cadena y mostrar una barra de longitud 3·10^6 enfrentada a 500 mediante dos rótulos, sin escala engañosa: indicar comparación simbólica. Encerrar los dos obstáculos en tarjetas breves y fundir hacia un árbol de opciones.

- **Duración orientativa de la escena:** 01:25. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- ACCENT_VINO sólo en el desacuerdo 4 frente a 2 y en la longitud que viola la cota. Letras y rutas válidas conservan sus colores; el separador imaginario en TEXT_MUTED.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 05

## Nombre: El espacio de búsqueda crece, y el pasado importa

## Descripcion Breve: La fuerza bruta y dos contadores aislados no proporcionan una búsqueda manejable.

## Objetivo Pedagogico: Motivar la restricción a una familia construible y demostrar que los objetivos no resumen un prefijo.

## Voz en off:

> “[TRIGGER_1] Podríamos probar todas las cadenas. En cada posición tenemos cuatro decisiones. Para longitud uno hay cuatro posibilidades; para longitud dos, dieciséis; para longitud tres, sesenta y cuatro. Cada nueva letra multiplica por cuatro. Para longitud L son cuatro elevado a L. Y verificar una candidata no elimina esa explosión.
> [TRIGGER_2] Otra tentación es buscar sobre los dos contadores: cuántos CAT llevo y cuántos GATA llevo. Hasta un millón en cada eje significa del orden de un billón de pares, diez elevado a doce. Pero incluso si tuviéramos esa memoria, esos dos números no describen todo lo que necesitamos saber.
> [TRIGGER_3] Compara los prefijos CA y CT. Ninguno contiene todavía CAT ni GATA: ambos tienen contadores cero, cero. Añadimos la misma letra T. CA se convierte en CAT y crea una aparición. CT se convierte en CTT y no crea ninguna. El mismo par de contadores y la misma acción producen resultados diferentes.
> [TRIGGER_4] Faltaba información sobre patrones incompletos, como CA, que una letra futura puede terminar. La pregunta cambia: ¿podemos elegir una familia de cadenas donde sepamos de antemano cuánto aporta cada letra especial? [Pausa.] En lugar de explorar cualquier secuencia, vamos a diseñar una estructura que podamos contar.”

## Descripcion Visual Detallada:

## Objetos:

- Árbol de decisiones de profundidad 3; sólo desplegar cuatro ramas completas del primer nivel y multiplicidades de los siguientes, rotuladas 4,16,64. Fórmula 4^L.
- Plano simbólico de contadores con ejes 0..10^6 y etiqueta (10^6+1)^2; dos carriles CA y CT con contador común (0,0).

## Layout y disposicion:

- Panel árbol en x=-3.4, ancho 5.4, y=-1.8..2.1. Panel de contadores en x=3.2, ancho 5.2, y=-1.8..2.1.
- Para el experimento, sustituir ambos paneles por carriles centrados en (-2.6,1.0,0) y (-2.6,-0.7,0); nueva T en x=0.6; resultados en x=3.4. Pregunta final en (0,-2.65,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Crear raíz y cuatro ramas C,G,A,T. Desplegar progresivamente niveles con contadores 4,16,64 y después sustituirlos por 4^L. Los niveles plegados son grupos rotulados, no hojas pretendidamente enumeradas.
- **[TRIGGER_2] — 00:23–00:46:** Crear el plano de dos objetivos, marcar su lado 10^6+1 y producto exacto; transformar ese producto en aproximación de orden 10^12. Mantener explícita la diferencia entre valor exacto y orden de magnitud.
- **[TRIGGER_3] — 00:46–01:10:** Retirar planos; crear CA y CT, ambos con (0,0). Copiar una misma ficha T al final de cada carril. Iluminar C→A→T sólo en el superior y actualizar sus contadores a (G,C)=(0,1); el inferior queda (0,0).
- **[TRIGGER_4] — 01:10–01:33:** Subrayar CA como patrón incompleto relevante. Formular la pregunta en pantalla, dejar pausa inmóvil y luego convertir las fichas A/T en los primeros tres pares del esqueleto alternante.

- **Duración orientativa de la escena:** 01:33. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Árbol y malla en ACCENT_INDIGO/ACCENT_CYAN. Costos inviables con borde ACCENT_VINO. En el contraejemplo cero no es fracaso: usar TEXT_MUTED; nueva información CA en ACCENT_TERRACOTTA.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 06

## Nombre: Un esqueleto y dos tipos de interruptores

## Descripcion Breve: Se fija el orden alternante AT y se reservan huecos para insertar C y G.

## Objetivo Pedagogico: Separar la estructura de soporte de las letras que activan cada patrón.

## Voz en off:

> “[TRIGGER_1] Fijemos primero una cadena que sólo alterna A y T: A, T, A, T, A, T. Es nuestro esqueleto. Como no contiene C ni G, todavía no hay CAT ni GATA. Pero ya contiene pares A, T y triples A, T, A que una letra situada antes podría completar.
> [TRIGGER_2] Pon una C delante. Cada par A, T que pueda elegirse después se convierte en un CAT. Pon una G delante. Cada triple A, T, A que pueda elegirse después se convierte en un GATA. La C necesita dos elecciones posteriores; la G necesita tres.
> [TRIGGER_3] ¿Qué ocurre si insertamos también otras ces y ges entre los pares? [Pausa.] Al escoger A y T podemos saltarlas. No añaden nuevas aes ni nuevas tes. Si dejamos fijo el esqueleto, el repertorio de elecciones A, T y A, T, A no cambia por esas inserciones.
> [TRIGGER_4] No hemos resuelto el problema todavía. Falta saber cuánto vale una C o una G en cada hueco, y cómo combinar esos valores para llegar a cualquier objetivo. Empecemos por una sola C delante de i pares. Vamos a construir la fórmula a partir del dibujo.”

## Descripcion Visual Detallada:

## Objetos:

- Tres pares AT en casillas agrupadas con VGroup; cuatro huecos marcados por pequeños círculos; dos fichas móviles C y G.
- Rótulo de sufijo MathTex (AT)^i y dos entradas simbólicas: C+(AT)^i→CAT, G+(AT)^i→GATA; contadores iniciales cero.

## Layout y disposicion:

- Esqueleto en y=0.8 con seis fichas x=-2.8,-1.7,-0.6,0.5,1.6,2.7. Huecos en x=-3.6,-1.15,1.05,3.45; señales de hueco por debajo de la fila en y=0.15.
- C y G esperan en (-5.4,1.5,0) y (-5.4,-0.5,0); paneles de patrón en (0,-1.25,0) y (0,-2.25,0), ancho máximo 10.8.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Crear pares y brace (AT)^3. Mostrar contadores cero y atenuar sus rótulos. Señalar que pares y triples internos existen iluminando una ruta AT y una ATA, sin contar aún todas.
- **[TRIGGER_2] — 00:23–00:44:** Mover C al hueco inicial y prolongar una ruta AT con su inicio C. Retirarla; mover G al mismo hueco y prolongar una ruta ATA. Mantener distintas las dos tarjetas de patrón.
- **[TRIGGER_3] — 00:44–01:07:** Insertar C entre par 1 y 2 y G entre par 2 y 3, conservando los tres pares AT como grupos con identidad estable. Hacer pasar una ruta AT por encima de ambas letras extra. Después proyectar la fila sobre sus posiciones A/T y comprobar que coincide con la original.
- **[TRIGGER_4] — 01:07–01:29:** Retirar las inserciones auxiliares; dejar C inicial y tres pares. Transformar brace 3 en i sólo como rótulo general de la familia, manteniendo el ejemplo i=3 visible en una etiqueta pequeña. Transición hacia agrupación por T.

- **Duración orientativa de la escena:** 01:29. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Esqueleto con A verde y T terracota; letras extra C cian y G índigo. Huecos en TEXT_MUTED. Flechas que vinculan prefijos con patrones en ACCENT_CYAN; no representar C o G como operadores que consumen AT.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 07

## Nombre: Los gatos forman un triángulo

## Descripcion Breve: Para tres pares, las T ofrecen una, dos y tres opciones de A anterior.

## Objetivo Pedagogico: Derivar el peso CAT agrupando cada elección por su T final.

## Voz en off:

> “[TRIGGER_1] Etiquetemos los tres pares: A uno, T uno; A dos, T dos; A tres, T tres. Si la C está delante, una aparición de CAT queda completamente determinada al elegir una A y una T posteriores, con la A antes de la T.
> [TRIGGER_2] Fijemos T uno. Sólo A uno queda antes: una elección. Fijemos T dos. Podemos tomar A uno o A dos: dos elecciones. Fijemos T tres. Podemos tomar A uno, A dos o A tres: tres elecciones. No hemos contado nada dos veces, porque cada aparición tiene una T final única.
> [TRIGGER_3] Una más dos más tres: seis. Podemos dibujar una casilla por elección. La primera fila tiene una, la segunda dos y la tercera tres. Por eso aparece un triángulo. La cadena C, A, T, A, T, A, T tiene seis CAT, aunque sólo hemos escrito una C.
> [TRIGGER_4] Para i pares, la fila de T b contiene b elecciones. La condición es a menor o igual que b: A a está antes de T b incluso cuando a y b son iguales, porque dentro de cada par la A viene primero. Al sumar las filas, obtenemos uno más dos y así hasta i. Este será el peso T sub i de una C.”

## Descripcion Visual Detallada:

## Objetos:

- C inicial y fichas A_1,T_1,A_2,T_2,A_3,T_3; matriz triangular de celdas (a,b) para 1≤a≤b≤3.
- Seis tarjetas pequeñas de pares (1,1),(1,2),(2,2),(1,3),(2,3),(3,3); MathTex T_3=1+2+3=6 y T_i=Σ_{b=1}^i b.

## Layout y disposicion:

- Cadena en y=1.65: C en x=-5.5 y seis fichas desde x=-3.8 con separación 1.45. Índices de par en y=1.05.
- Triángulo a la izquierda: filas b=1,2,3 en y=-0.15,-0.85,-1.55; celdas desde x=-4.9 con separación 0.75. Fórmulas en (2.45,-0.5,0) y (2.45,-1.75,0). Regla a≤b en (0,-2.85,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Recrear la cadena, índices y el triángulo vacío. Dibujar una ruta general C→A_a→T_b, y desvanecerla antes de contar.
- **[TRIGGER_2] — 00:20–00:43:** Puntero a T_1: encender (1,1) y llenar fila 1. Puntero a T_2: encender (1,2),(2,2) y fila 2. Puntero a T_3: encender (1,3),(2,3),(3,3) y fila 3. Crear cada celda sólo cuando su ruta se muestra.
- **[TRIGGER_3] — 00:43–01:05:** Agrupar las seis celdas mediante brace y escribir 1+2+3=6. TransformFromCopy de C hacia el rótulo peso de una C, conservando claro que no hay seis ces.
- **[TRIGGER_4] — 01:05–01:34:** Escribir a≤b y destacar la diagonal a=b con tres halos; cada halo enlaza A_b con T_b del mismo par. Extender el triángulo simbólicamente con fila b y label b elecciones, y escribir la suma general. Los puntos suspensivos representan una regla demostrada, no rutas omitidas del ejemplo i=3.

- **Duración orientativa de la escena:** 01:34. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Filas con borde ACCENT_CYAN y la T que las identifica en ACCENT_TERRACOTTA. Diagonal en ACCENT_MINT; fórmulas en TEXT_MAIN, índice activo en terracota.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 08

## Nombre: De un triángulo a una fórmula

## Descripcion Breve: Dos copias del triángulo forman un rectángulo y también codifican pares distintos.

## Objetivo Pedagogico: Probar T_i=i(i+1)/2 y explicar la notación binomial sin memorizarla.

## Voz en off:

> “[TRIGGER_1] Llamemos S a la suma uno más dos hasta i. Dibujamos una segunda copia del triángulo, la giramos y la encajamos con la primera. En cada fila, las dos cantidades suman i más uno. Hay i filas. Las dos copias juntas contienen i por i más uno casillas.
> [TRIGGER_2] Como juntamos dos triángulos iguales, dos S es i por i más uno. Dividimos entre dos. El peso de una C delante de i pares es i por i más uno, entre dos. Para tres pares obtenemos tres por cuatro entre dos: seis. Para uno obtenemos uno; para dos, tres; para cuatro, diez.
> [TRIGGER_3] Hay otra forma de ver el mismo número. Una elección A a, T b cumple a menor o igual que b. Cambiemos su etiqueta a la pareja a, b más uno. Ahora son dos números distintos en orden creciente, elegidos entre uno y i más uno. Al revés, si nos dan dos números u menor que v, recuperamos a igual a u y b igual a v menos uno.
> [TRIGGER_4] Esa correspondencia es exacta en los dos sentidos. Por eso también podemos escribir el binomial i más uno sobre dos: el número de maneras de elegir dos elementos distintos sin importar su orden. No es una fórmula decorativa. Es el mismo triángulo, visto como una colección de parejas.”

## Descripcion Visual Detallada:

## Objetos:

- Triángulo de i=4, duplicado para formar rectángulo de 4×5 celdas; MathTex 2S=i(i+1), S=i(i+1)/2.
- Diagrama de bijección (a,b)↔(a,b+1) y recta con 1..5 para i=4; tabla i=1,2,3,4 con T=1,3,6,10.

## Layout y disposicion:

- Panel geométrico en x=-3.0, y=-0.9..1.75; celdas de 0.48, rectángulo final ancho 2.4 y alto 1.92. Ecuaciones en (3.0,1.0,0),(3.0,0,0).
- Para la bijección, recta de etiquetas 1..5 en y=0.5, x=-3.2,-1.6,0,1.6,3.2; mapeo en y=-1.1; binomial en (0,-2.3,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Reconstruir triángulo i=4; copiarlo, rotar sólo la distribución de casillas sin voltear textos y encajarlo. Encender fila a fila los pares de longitudes 1+4,2+3,3+2,4+1; crear brace i filas y brace i+1 columnas.
- **[TRIGGER_2] — 00:22–00:46:** Escribir 2S=i(i+1) y TransformMatchingTex a S=i(i+1)/2. Sustituir i=3 y completar seis; luego crear los otros tres valores de la tabla uno a uno, con sus sustituciones visibles.
- **[TRIGGER_3] — 00:46–01:17:** Retirar rectángulo y tabla. Mostrar ejemplo (a,b)=(2,3)→(2,4), y ejemplo diagonal (3,3)→(3,4). Dibujar flecha inversa (u,v)→(u,v−1) con la condición u<v, sin perder los casos a=b.
- **[TRIGGER_4] — 01:17–01:39:** Mostrar conjunto de parejas de 1..i+1 mediante arco entre dos marcas distintas. Escribir T_i=binom(i+1,2)=i(i+1)/2. Conservar la fórmula como tarjeta de peso para las escenas futuras; retirar las demás piezas.

- **Duración orientativa de la escena:** 01:39. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Primer triángulo en ACCENT_CYAN y segundo en ACCENT_INDIGO; textos de celdas en TEXT_MAIN. Variables activas en ACCENT_TERRACOTTA. La tarjeta T_i lleva una pequeña C cian para no confundir T_i con cantidad de letras T.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 09

## Nombre: Para GATA, la T queda entre dos elecciones

## Descripcion Breve: Cada T_b aporta b(i−b) triples ATA en el sufijo.

## Objetivo Pedagogico: Contar las contribuciones GATA con dos lados de una T y enumerar el caso i=3.

## Voz en off:

> “[TRIGGER_1] Sustituyamos la C inicial por una G. Necesitamos elegir A, T, A a su derecha. Fijar la T sigue siendo útil, pero ahora hay dos decisiones: una A antes y una A después. Probemos primero tres pares AT, que terminan en T tres.
> [TRIGGER_2] Para T uno, antes está A uno y después están A dos y A tres. Una opción por dos opciones: dos triples. Son A uno, T uno, A dos; y A uno, T uno, A tres. Para T dos, antes hay dos aes y después sólo A tres: otros dos triples, A uno, T dos, A tres; y A dos, T dos, A tres.
> [TRIGGER_3] T tres tiene tres aes anteriores, pero ninguna A después. Tres por cero: no añade nada. En total, dos más dos más cero: cuatro. La G inicial convierte esos cuatro ATA en cuatro GATA. El esqueleto solo no contiene GATA: contiene las continuaciones que una G puede completar.
> [TRIGGER_4] Con i pares, T b tiene b aes anteriores y i menos b aes posteriores. Su aporte es b por i menos b. Las condiciones son a menor o igual que b, y b estrictamente menor que c. Al sumar sobre la T elegida, el peso V sub i es la suma de b por i menos b, desde b igual a uno hasta i.”

## Descripcion Visual Detallada:

## Objetos:

- G inicial y tres pares AT con índices de par; puntero T_b; llaves izquierda/derecha con cantidades b e i−b.
- Cuatro tarjetas de triples (a,b,c)=(1,1,2),(1,1,3),(1,2,3),(2,2,3); fila de aportes 1·2,2·1,3·0; MathTex V_i=Σ b(i−b).

## Layout y disposicion:

- Cadena en y=1.6, G en x=-5.5; pares en las posiciones de la escena triangular. Llaves laterales bajo la cadena en y=0.6.
- Tarjetas en x=-3.0 y 3.0, filas y=-0.6,-1.4. Fila de productos en y=-2.15, suma general en y=-2.95.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Recrear G y los tres pares, mantener pequeña tarjeta T_i arriba a la izquierda. Puntero a T_1; abrir espacios para las dos llaves sin contar todavía.
- **[TRIGGER_2] — 00:20–00:49:** Marcar A_1 a la izquierda y A_2,A_3 a la derecha de T_1. Animar las dos rutas ATA y crear sus tarjetas. Mover a T_2, marcar A_1,A_2 y A_3; animar las otras dos rutas y completar tarjetas restantes.
- **[TRIGGER_3] — 00:49–01:11:** Mover a T_3; mostrar llave derecha vacía y 3·0=0. Agrupar cuatro tarjetas y escribir V_3=4. Destacar que el número corresponde a ATA después de G; el rótulo del contador completo sigue siendo GATA.
- **[TRIGGER_4] — 01:11–01:40:** Transformar las cantidades de llaves a b e i−b, y escribir a≤b<c. Escribir la suma general con los límites completos. Conservar cuatro tarjetas para establecer la correspondencia combinatoria en la escena siguiente.

- **Duración orientativa de la escena:** 01:40. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- G en ACCENT_INDIGO; regiones izquierda y derecha diferenciadas por contornos cian e índigo, manteniendo A en verde. Cero final en TEXT_MUTED. Tarjeta V_i con G índigo; no escribir GATA dentro de un sufijo sin G.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 10

## Nombre: Un triple escondido detrás de cada GATA

## Descripcion Breve: La condición a≤b<c equivale a elegir tres números distintos entre 1 e i+1.

## Objetivo Pedagogico: Probar la fórmula cúbica de V_i mediante una bijección reversible y el factor 3!.

## Voz en off:

> “[TRIGGER_1] La suma anterior se puede cerrar sin adivinar una identidad. A cada triple a, b, c que cumple a menor o igual que b y b menor que c, asignemos el triple a, b más uno, c más uno. Sus tres números son estrictamente crecientes y están entre uno e i más uno.
> [TRIGGER_2] Para nuestros tres pares, las cuatro elecciones se convierten en uno, dos, tres; uno, dos, cuatro; uno, tres, cuatro; y dos, tres, cuatro. Son justamente todas las maneras de elegir tres números del conjunto uno, dos, tres, cuatro. Ninguna elección se repite y ninguna falta.
> [TRIGGER_3] ¿Podemos volver? Sí. Si nos dan u menor que v menor que w, tomamos a igual a u, b igual a v menos uno y c igual a w menos uno. La primera desigualdad garantiza a menor o igual que b. La segunda garantiza b menor que c. Y w como máximo i más uno garantiza c como máximo i. La correspondencia no pierde información.
> [TRIGGER_4] Para elegir tres elementos distintos en orden arbitrario hay i más uno opciones para el primero, i para el segundo e i menos uno para el tercero. Cada grupo de tres aparece en sus seis órdenes posibles. Dividimos entre seis. Así obtenemos V sub i: i menos uno, por i, por i más uno, entre seis; o el binomial i más uno sobre tres.
> [TRIGGER_5] Para i igual a uno no hay tres números que elegir: el peso es cero. Para dos, el peso es uno. Para tres, cuatro. Para cuatro, diez. Ya tenemos las dos familias: los pesos de C crecen como triángulos, y los de G como elecciones de tres elementos. Una G bien colocada puede generar muchísimas apariciones.”

## Descripcion Visual Detallada:

## Objetos:

- Dos columnas de cuatro tarjetas: (1,1,2)↔(1,2,3), (1,1,3)↔(1,2,4), (1,2,3)↔(1,3,4), (2,2,3)↔(2,3,4).
- Recta 1..i+1; fórmulas de mapeo inverso; seis tarjetas de orden de tres símbolos u,v,w: uvw,uwv,vuw,vwu,wuv,wvu.
- MathTex V_i=binom(i+1,3)=(i−1)i(i+1)/6, y tabla V_1=0,V_2=1,V_3=4,V_4=10.

## Layout y disposicion:

- Columnas de correspondencia centradas en x=-3.5 y 3.5; filas y=1.65,0.8,-0.05,-0.9; flechas a través de x=-1.4..1.4.
- Después, mapeo directo en y=1.75 e inverso en y=0.65; seis órdenes en una cuadrícula de 3 columnas x=-3.2,0,3.2 y 2 filas y=0.5,-0.5. Fórmula final en y=-2.35; tabla en y=-3.1.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Conservar las cuatro tarjetas de la escena anterior y alinearlas a la izquierda. Escribir la regla (a,b,c)→(a,b+1,c+1); mover visualmente las etiquetas b y c una unidad, sin mover las letras originales de su orden.
- **[TRIGGER_2] — 00:24–00:45:** Crear las cuatro tarjetas de la derecha mediante cuatro TransformFromCopy separados; indicar las cuatro selecciones de 3 de 4. Encender cada correspondencia cuando se pronuncia su triple.
- **[TRIGGER_3] — 00:45–01:14:** Retirar la lista concreta; mostrar (u,v,w)→(u,v−1,w−1) y transformar una por una u<v a u≤v−1, v<w a v−1<w−1 y w≤i+1 a w−1≤i. Conservar las tres condiciones verificadas.
- **[TRIGGER_4] — 01:14–01:43:** Crear tres ranuras de selección con contadores i+1,i,i−1; agruparlas como producto. Mostrar los seis órdenes explícitos de u,v,w y aplicar una llave que los identifica como un solo grupo sin orden. TransformMatchingTex del producto dividido por 6 hacia el binomial y la fórmula desarrollada.
- **[TRIGGER_5] — 01:43–02:09:** Sustituir i=1,2,3,4 uno por uno y escribir los cuatro valores. V_1=0 lleva un símbolo de ausencia de triples, no una indicación de división. Conservar las tarjetas T_i y V_i juntas al final.

- **Duración orientativa de la escena:** 02:09. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Correspondencia en ACCENT_CYAN, triples ordenados en ACCENT_INDIGO, desplazamientos +1/−1 en ACCENT_TERRACOTTA. Fórmulas válidas en TEXT_MAIN y marcas de reversibilidad en ACCENT_MINT.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 11

## Nombre: Construir las tablas mirando el último par

## Descripcion Breve: Al añadir A_iT_i, el nuevo T aporta i pares y el nuevo A cierra T_{i−1} triples.

## Objetivo Pedagogico: Explicar las recurrencias y el papel temporal de A antes de T en cada nuevo par.

## Voz en off:

> “[TRIGGER_1] Las fórmulas también se pueden descubrir haciendo crecer el esqueleto. Partimos de tres pares, con seis AT y cuatro ATA. Añadamos A cuatro, T cuatro. Los pares AT antiguos siguen existiendo. La nueva T cuatro puede combinarse con cualquiera de las cuatro aes: aparecen cuatro pares nuevos.
> [TRIGGER_2] Para los triples ATA, fíjate primero en la nueva A cuatro, antes de escribir la T cuatro. Puede cerrar cada uno de los seis pares AT del prefijo anterior. Nacen seis triples: A uno, T uno, A cuatro; A uno, T dos, A cuatro; A dos, T dos, A cuatro; A uno, T tres, A cuatro; A dos, T tres, A cuatro; y A tres, T tres, A cuatro.
> [TRIGGER_3] La T cuatro no cierra ningún ATA nuevo: todavía no hay una A después de ella. Por tanto, pasamos de seis a diez pares AT y de cuatro a diez triples ATA. El orden de llegada explica por qué en la segunda cuenta usamos los pares del prefijo anterior, no los del esqueleto ya ampliado.
> [TRIGGER_4] En general, T sub i es T sub i menos uno más i. Y V sub i es V sub i menos uno más T sub i menos uno, que vale i por i menos uno entre dos. Empezamos con ambas tablas en cero para el esqueleto vacío. Esas dos actualizaciones generan todos los pesos hasta el índice que decidamos usar.”

## Descripcion Visual Detallada:

## Objetos:

- Esqueleto de 3 pares más dos fichas nuevas A_4,T_4; contadores AT=6 y ATA=4; cuatro rutas nuevas AT y seis tarjetas de triples terminados en A_4.
- Dos diagramas de actualización de memoria: T_{i−1}→T_i con +i, V_{i−1}→V_i con +T_{i−1}; MathTex T_0=V_0=0.

## Layout y disposicion:

- Ocho fichas en y=1.5, x=-5.4+1.45k para k=0..7. A_4 y T_4 entran desde y=2.35. Contadores en x=-3.1 y 3.1, y=0.35.
- Seis tarjetas de triples en 3 columnas x=-3.8,0,3.8 y 2 filas y=-0.9,-1.65. Recurrencias sustituyen tarjetas en y=-1.1 y -2.15.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Recrear los tres pares; añadir primero A_4 y reservar T_4 en su lugar con contorno sin relleno. Después iluminar las cuatro rutas hacia T_4 y actualizar AT de 6 a 10, rotulando claramente cuenta final de pares.
- **[TRIGGER_2] — 00:22–00:53:** Pausar la fila final y abrir un recuadro del estado justo después de A_4 y antes de T_4. Dibujar las seis rutas anteriores hacia A_4, en el orden completo de la locución, y crear las seis tarjetas. Mantener 6 pares previos como rótulo del recuadro.
- **[TRIGGER_3] — 00:53–01:18:** Cerrar el recuadro, escribir que T_4 no tiene A posterior y actualizar ATA de 4 a 10 con +6. Los contadores AT y ATA permanecen separados aunque ambos terminan en 10.
- **[TRIGGER_4] — 01:18–01:46:** Transformar los contadores en dos carriles de memoria con flechas +i y +i(i−1)/2. Escribir recurrencias e inicializaciones. Conservar sólo las tarjetas generales; toda flecha nueva aparece dentro de este trigger.

- **Duración orientativa de la escena:** 01:46. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- A nueva en ACCENT_MINT y T nueva en ACCENT_TERRACOTTA; agregados AT en ACCENT_CYAN y ATA en ACCENT_INDIGO. Recuadro de estado anterior con borde TEXT_MUTED para evitar mezclar tiempos.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 12

## Nombre: Por qué las contribuciones se suman sin mezclarse

## Descripcion Breve: Cada subsecuencia tiene una única letra inicial C o G que permite clasificarla.

## Objetivo Pedagogico: Demostrar aditividad e independencia sobre un esqueleto compartido.

## Voz en off:

> “[TRIGGER_1] Probemos una cadena con varias letras especiales: C, G, A, T, C, A, T. La primera C tiene dos pares AT a su derecha y aporta tres CAT. La segunda C tiene un solo par y aporta uno. Las apariciones pueden compartir aes y tes, pero nunca pueden tener dos ces iniciales: cada CAT elige exactamente una.
> [TRIGGER_2] Clasifiquemos todas las apariciones por la posición de su C. En la primera caja están las elecciones uno, tres, cuatro; uno, tres, siete; y uno, seis, siete. En la segunda está cinco, seis, siete. Las cajas no se superponen. Tres más uno da cuatro.
> [TRIGGER_3] La G de la posición dos tiene dos pares AT a su derecha. Su único ATA es A en tres, T en cuatro, A en seis. Crea un GATA, con posiciones dos, tres, cuatro, seis. La C intermedia se salta. Agregar ces no inventa nuevos GATA, y agregar ges no inventa nuevos CAT.
> [TRIGGER_4] El argumento funciona para cualquier cantidad de inserciones. Toda aparición CAT pertenece a la caja de su única C inicial; toda aparición GATA, a la de su única G inicial. Otras ces y ges no modifican las elecciones de A y T de un sufijo. Por eso multiplicamos cada peso por el número de letras en su hueco y después sumamos. No hay un producto escondido entre cantidades de C y G.”

## Descripcion Visual Detallada:

## Objetos:

- Cadena CGATCAT, índices 1..7, cajas de clasificación C en 1 y C en 5, más caja G en 2.
- Tarjetas CAT con ternas (1,3,4),(1,3,7),(1,6,7),(5,6,7), y tarjeta GATA (2,3,4,6); fórmulas N_CAT=3+1=4 y N_GATA=1.

## Layout y disposicion:

- Siete fichas en y=1.5, x=-5.4+1.8k para k=0..6; índices en y=0.9. Cajas C en (-3.65,-1.0,0) de 3.8×2.2 y (0.2,-1.0,0) de 2.8×2.2; caja G en (4.0,-1.0,0) de 3.2×2.2.
- Dentro de la primera caja, tres ternas en y=-0.45,-1.05,-1.65; segunda y tercera con una tarjeta en y=-1.0. Totales en y=-2.65.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:26:** Crear cadena e índices; señalar las C iniciales posibles mediante dos anillos. Abrir sus cajas con rótulo posición de inicio y mostrar pesos 3 y 1 según los pares posteriores.
- **[TRIGGER_2] — 00:26–00:47:** Trazar las tres rutas desde C_1 y mover una tarjeta de cada ruta a su caja. Trazar la ruta desde C_5 y llenar la otra caja. Agrupar las cuatro tarjetas sin fusionarlas; escribir 3+1=4.
- **[TRIGGER_3] — 00:47–01:11:** Abrir caja G_2, trazar 2→3→4→6 por encima de C_5 y escribir V_2=1. Proyectar el sufijo de G sobre A/T para comprobar que la C omitida no cambia sus elecciones. Señalar G_2 como letra irrelevante para CAT sin borrar sus rutas anteriores.
- **[TRIGGER_4] — 01:11–01:43:** Transformar las cajas concretas en familias rotuladas C en hueco i y G en hueco i. Escribir contribuciones a_iT_i y b_iV_i, separadas por patrón. Una llave de partición se cierra sobre cada familia; no dibujar flechas multiplicativas entre C y G. Fundir hacia las tablas de pesos.

- **Duración orientativa de la escena:** 01:43. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Cajas CAT con borde ACCENT_CYAN y cajas GATA con borde ACCENT_INDIGO. Rutas con el color de su caja; letras A/T mantienen el suyo. Resultado exacto en ACCENT_MINT; texto partición en TEXT_MAIN.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 13

## Nombre: Cambiar números por letras con peso

## Descripcion Breve: Los objetivos se representan como sumas de pesos triangulares y binomiales.

## Objetivo Pedagogico: Presentar el greedy como una representación exacta con una garantía de tamaño pendiente.

## Voz en off:

> “[TRIGGER_1] Los primeros pesos de C son uno, tres, seis, diez y quince. Los de G son cero, uno, cuatro, diez y veinte. El índice dice cuántos pares AT quedarán a la derecha de esa letra. Podemos usar varias letras en un mismo hueco: cada una repite la misma contribución.
> [TRIGGER_2] Miremos los objetivos que usaremos de ejemplo: G igual a cinco y C igual a ocho. Para ocho CAT podemos pagar seis y luego uno y uno. Para cinco GATA, cuatro y uno. Eso sugiere poner una C y una G donde queden tres pares; otra G donde queden dos; y dos ces donde quede uno.
> [TRIGGER_3] Nuestra regla será tomar el peso más grande que quepa en el residuo, usarlo tantas veces como quepa y seguir hacia pesos menores. La moneda de valor uno garantiza que al final se puede pagar cualquier resto. Pero todavía debemos demostrar que no escribimos demasiadas letras.
> [TRIGGER_4] Tampoco debemos atribuirle una propiedad que no necesita. Con los pesos de C, doce se paga de forma voraz como diez más uno más uno: tres letras. Sin embargo, seis más seis usa dos. El greedy no siempre minimiza el número de ces. Lo que queremos probar es exactitud y una longitud dentro de quinientos, no optimalidad.”

## Descripcion Visual Detallada:

## Objetos:

- Tabla de cinco columnas i=1..5 y dos filas T_i=1,3,6,10,15; V_i=0,1,4,10,20; fichas de peso con letra C o G en el centro.
- Dos carriles de residuos: C:8→2→1→0, G:5→1→0; comparación 12=10+1+1 frente a 12=6+6.

## Layout y disposicion:

- Tabla centrada en (0,1.2,0), ancho 10.8, filas y=1.95,1.05,0.15. Carriles C y G en y=-1.2,-2.2, x=-4.8..4.8.
- Comparación de 12 sustituye carriles: ecuaciones en (-2.8,-1.0,0) y (2.8,-1.0,0), contador de letras debajo en y=-2.0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Crear tabla con fórmulas T_i y V_i en el margen izquierdo. Llenar las diez celdas una a una; V_1=0 se dibuja como casilla deshabilitada. Añadir encima de cada columna el rótulo pares posteriores.
- **[TRIGGER_2] — 00:23–00:49:** Mover ficha C de peso 6 al carril ocho y actualizar a dos; fichas C de peso 1 actualizan dos→uno→cero. En carril G, ficha de peso 4 actualiza cinco→uno y ficha de peso 1 a cero. Conectar cada ficha con su columna i.
- **[TRIGGER_3] — 00:49–01:11:** Crear puntero que recorre pesos de mayor a menor. Una compuerta matemática peso≤residuo permite pasar fichas, y un contador marca multiplicidad. Añadir una tarjeta garantía pendiente: longitud; no usar un sello de aprobación antes de probarla.
- **[TRIGGER_4] — 01:11–01:37:** Retirar carriles y mostrar 12=10+1+1 con tres C frente a 12=6+6 con dos C. El mismo resultado recibe color de validez en ambos lados; rodear sólo los contadores de letras diferentes. Escribir metas: exactitud y L≤500. Conservar esa distinción para la prueba posterior.

- **Duración orientativa de la escena:** 01:37. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Fichas C cian y G índigo; residuo activo terracota. Ambas representaciones de 12 en ACCENT_MINT. No marcar el greedy como incorrecto por usar una letra más; V_1 en TEXT_MUTED.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 14

## Nombre: Planear desde el sufijo y escribir de izquierda a derecha

## Descripcion Breve: El índice descendente fija cuántos pares futuros verá cada inserción.

## Objetivo Pedagogico: Resolver la aparente contradicción entre planificar el sufijo y emitir el prefijo.

## Voz en off:

> “[TRIGGER_1] Vamos a reservar hasta ciento cuarenta y cuatro pares AT. Ese número se justificará cuando midamos la longitud; por ahora es nuestra capacidad de trabajo. Recorremos los huecos desde el que dejaría ciento cuarenta y cuatro pares a la derecha hasta el que deja uno.
> [TRIGGER_2] En el hueco de índice i colocamos primero todas las ces que quepan con peso T sub i, después todas las ges que quepan con peso V sub i, y luego escribimos un par AT. Para las ges sólo usamos índices desde dos, porque con un par el peso es cero.
> [TRIGGER_3] Parece que estamos contando letras que todavía no existen. Pero quedan planificadas: después de una inserción en i escribiremos el par de ese paso y los de los pasos i menos uno hasta uno. Son exactamente i pares. Así la decisión actual tiene el sufijo que promete su peso.
> [TRIGGER_4] En nuestro ejemplo, los objetivos son cinco GATA y ocho CAT. Para todo índice desde ciento cuarenta y cuatro hasta cuatro, el peso de C es al menos diez y el de G también es al menos diez. No cabe ninguna letra. Como aún no hemos empezado, omitimos esos pares iniciales. La primera decisión útil estará en el índice tres.”

## Descripcion Visual Detallada:

## Objetos:

- Fila de huecos planeados con índices 144,143,4,3,2,1, separaciones rotuladas por intervalos; tarjetas de fórmula de pesos y cursor descendente.
- Un hueco ampliado i, ficha C, ficha G y un par AT sólido seguido de i−1 pares futuros representados por un grupo con brace exacta.
- Contadores r_G=5,r_C=8; prueba universal i≥4⇒T_i≥T_4=10 y V_i≥V_4=10.

## Layout y disposicion:

- Fila planeada en y=1.6, x=-5.4..5.4; últimos huecos 3,2,1 en x=1.4,3.2,5.0. Panel de ampliación en y=-0.65, ancho 11.
- Contadores en (-3.7,2.65,0) y (3.7,2.65,0), bajo título que se limita a ancho 9.4. Prueba del intervalo en (0,-2.55,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear la reserva con borde punteado y etiqueta plan, no salida. Posar cursor sobre 144 y escribir B=144. La cadena realmente emitida permanece vacía en un carril separado.
- **[TRIGGER_2] — 00:21–00:45:** Ampliar hueco i y mostrar secuencia de acciones C, luego G si i≥2, luego AT. Activar guardia i≥2 ante G. No escribir un bloque de instrucciones ni código; usar tres estaciones con flechas.
- **[TRIGGER_3] — 00:45–01:08:** Iluminar el par del paso i y la brace sobre los i−1 futuros; escribir 1+(i−1)=i. En el ejemplo i=3 desplegar explícitamente AT de pasos 3,2,1. Volver a la vista global conservando el sentido izquierda→derecha de salida.
- **[TRIGGER_4] — 01:08–01:35:** Escribir las dos desigualdades para todo i≥4 y señalar monotonicidad de las tablas. Tachar con atenuación el intervalo completo 144..4 como sin inserción; no fingir una enumeración de 141 pasos. Mostrar que todos quedan justificados por una misma desigualdad y mover cursor a 3. Mantener los contadores intactos.

- **Duración orientativa de la escena:** 01:35. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Plan futuro en TEXT_MUTED y contorno ACCENT_INDIGO; salida real en colores de letras. Cursor y r_G/r_C en ACCENT_TERRACOTTA, intervalo descartado en TEXT_MUTED. No usar rojo para omisiones válidas.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 15

## Nombre: Primer hueco: pagar seis y cuatro

## Descripcion Breve: En i=3 se insertan C y G y se emite el primer AT.

## Objetivo Pedagogico: Relacionar cada emisión con el residuo y el sufijo prometido.

## Voz en off:

> “[TRIGGER_1] Estamos en el índice tres. El peso de C es seis y el de G es cuatro. Quedan ocho CAT y cinco GATA por producir. Aún no hemos escrito nada, pero ya sabemos que después de las letras de este hueco habrá tres pares AT.
> [TRIGGER_2] Una C cuesta seis. Cabe una vez en ocho y deja residuo dos. No cabe una segunda, porque necesitaríamos otros seis. Escribimos C y anotamos que sus seis apariciones se confirmarán cuando terminemos el sufijo. Asignar una contribución no significa que ya esté completa en el prefijo.
> [TRIGGER_3] Ahora una G cuesta cuatro. Cabe una vez en cinco y deja residuo uno. Escribimos G después de la C. La G no aumenta el número de CAT asignados, y la C no aumenta el de GATA. Nuestros residuos quedan G igual a uno, C igual a dos.
> [TRIGGER_4] Escribimos el par AT de este paso. El prefijo es CGAT y ya contiene un CAT: C, A, T. Ese uno visible no son los seis que asignamos a la C; los otros llegarán al extender la cadena. Todavía no hay ningún GATA, porque falta una A posterior a la T. Para evitar confundir ambas cuentas, el marcador principal muestra contribuciones asignadas; el conteo del prefijo lleva una etiqueta diferente.”

## Descripcion Visual Detallada:

## Objetos:

- Panel i=3,T_3=6,V_3=4; contadores residuos (G,C)=(5,8); ledger asignado CAT=0,GATA=0.
- Carril de salida vacío con cuatro ranuras; tres pares futuros punteados; tarjetas de decisión 8=1·6+2 y 5=1·4+1; rótulo separado N_CAT(prefijo)=1 y N_GATA(prefijo)=0.

## Layout y disposicion:

- Salida y=0.55, posiciones finales x=-5.5,-4.4,-3.3,-2.2 para C,G,A,T. Futuros dos pares en x=-1.1,0,1.1,2.2, punteados.
- Residuos en (-3.3,2.0,0), pesos en (3.3,2.0,0); ledger de asignaciones en y=-1.0 y conteo del prefijo en y=-2.2. Fórmulas de decisión en x=-3.0 y 3.0,y=-3.0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear panel de pesos y tres pares planeados. Inicializar ledger asignado en cero y residuos en (5,8). Mantener ambos registros con sus rótulos completos.
- **[TRIGGER_2] — 00:21–00:43:** Mover una C real a la primera ranura; restar seis al residuo C y añadir seis al ledger CAT asignado en la misma animación. Mostrar 8=1·6+2. Intentar una segunda ficha con una compuerta 6≤2 falsa y devolverla al almacén, sin emitirla.
- **[TRIGGER_3] — 00:43–01:05:** Mover G a segunda ranura; restar cuatro a residuo G y añadir cuatro a ledger GATA asignado. Mostrar 5=1·4+1. Iluminar (G,C)=(1,2) y mantener distintos los registros.
- **[TRIGGER_4] — 01:05–01:36:** Solidificar A y T del primer par, obteniendo CGAT; trazar C_1→A_3→T_4 y contar un CAT del prefijo en un pequeño registro secundario, que se distingue del seis asignado. Mostrar GATA(prefijo)=0 y señalar que falta una A posterior. Al final mantener salida y residuos para i=2.

- **Duración orientativa de la escena:** 01:36. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Asignaciones CAT cian y GATA índigo; residuos terracota. Conteo del prefijo con borde TEXT_MUTED y letras TEXT_MAIN. Fichas futuras sin relleno; ninguna contribución asignada se presenta como conteo ya existente.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 16

## Nombre: Segundo hueco: otra G y un par que no se puede saltar

## Descripcion Breve: En i=2 sólo se inserta G, y el prefijo queda CGATGAT.

## Objetivo Pedagogico: Mostrar decisiones diferentes para los dos objetivos y conservar los pares previstos.

## Voz en off:

> “[TRIGGER_1] Bajamos al índice dos. Una C valdría tres, pero su residuo es dos: no cabe. No escribimos ninguna C. Una G vale uno, y su residuo es uno: cabe exactamente una. Escribimos esa G y dejamos el residuo G en cero.
> [TRIGGER_2] La nueva G tendrá dos pares AT a la derecha: el que escribiremos ahora y el del último paso. Sus elecciones forman un único GATA. La G anterior sigue teniendo planeados sus tres pares; insertar otra G no cambia esa promesa.
> [TRIGGER_3] Escribimos A y T. El prefijo es ahora CGATGAT. Las contribuciones asignadas son cinco GATA y seis CAT. Los residuos son G igual a cero y C igual a dos. Aún quedan dos ces por escribir y el último par AT.
> [TRIGGER_4] Observa que escribimos el par aunque sólo uno de los dos objetivos haya recibido una letra en este hueco. Y si no hubiéramos insertado ninguna, también tendríamos que escribirlo después de haber empezado. Es parte del sufijo que ya prometimos a las letras anteriores.”

## Descripcion Visual Detallada:

## Objetos:

- Estado heredado CGAT; panel i=2,T_2=3,V_2=1; ficha G en índice final 5 y par A_6T_7; último AT futuro punteado.
- Compuerta 3≤2 falsa para C y 1≤1 verdadera para G; ledger asignado CAT=6,GATA=5; residuos (0,2).

## Layout y disposicion:

- Conservar coordenadas de las primeras cuatro fichas: x=-5.5,-4.4,-3.3,-2.2, y=0.55. Nuevas fichas G,A,T en x=-1.1,0,1.1; último par provisional en x=2.2,3.3.
- Pesos, residuos y ledger en las posiciones de la escena anterior; brace dos pares posteriores desde x=-0.45 hasta 3.8 en y=1.35.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Recrear exactamente CGAT y registros finales anteriores si se renderiza por separado. Actualizar panel a i=2. Mostrar C de peso 3 ante residuo 2 y devolverla. Desplazar los dos pares futuros punteados 1.1 unidades a la derecha: pasan a x=0,1.1,2.2,3.3 y abren la ranura x=-1.1. Emitir allí G y actualizar residuo G a cero, ledger GATA a cinco. El desplazamiento cambia posiciones planeadas, no el número de pares.
- **[TRIGGER_2] — 00:19–00:38:** Crear brace de dos pares AT futuros a la derecha de G_5; distinguir el primer par, que se emitirá ahora, del último. Reproyectar el sufijo de G_2 mostrando tres pares previstos y saltando G_5.
- **[TRIGGER_3] — 00:38–00:57:** Solidificar A_6,T_7, mantener el último AT punteado. Escribir el prefijo completo CGATGAT e índices 1..7. Actualizar ledger a (GATA,CAT)=(5,6) y mantener residuos (0,2).
- **[TRIGGER_4] — 00:57–01:18:** Iluminar el par recién escrito y conectar su compromiso con ambas letras del hueco anterior. Añadir rótulo una vez iniciada, conservar todos los pares restantes. No adelantar la inserción de las dos C finales; transición con el cursor a i=1.

- **Duración orientativa de la escena:** 01:18. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- C que no cabe en TEXT_MUTED con borde terracota, sin dramatización roja. Residuo G cero en ACCENT_MINT; G recién emitida índigo. Compromisos futuros en cian y contornos punteados.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 17

## Nombre: Último hueco: dos ces de valor uno

## Descripcion Breve: En i=1 se consumen dos unidades CAT y se completa CGATGATCCAT.

## Objetivo Pedagogico: Cerrar la construcción y tratar explícitamente el peso GATA igual a cero.

## Voz en off:

> “[TRIGGER_1] Llegamos al índice uno. El peso de C es uno y todavía faltan dos CAT. Escribimos una C: el residuo baja de dos a uno. Escribimos otra C: baja de uno a cero. Cada una tendrá el mismo último par AT a la derecha, pero son posiciones iniciales distintas y por eso aportan una aparición cada una.
> [TRIGGER_2] Para G, el peso en este índice es cero. No hay un ATA dentro de un solo par AT. No intentamos dividir entre cero ni repetir una resta de cero. Esta estación simplemente no permite insertar G. Además, su residuo ya quedó en cero en el paso anterior.
> [TRIGGER_3] Escribimos el último A y el último T. La cadena completa es C, G, A, T, G, A, T, C, C, A, T: CGATGATCCAT. Tiene once letras. Cada promesa de sufijo se ha cumplido: tres pares para las primeras letras, dos para la segunda G y uno para las dos ces finales.
> [TRIGGER_4] Los residuos terminaron en cero. La cuenta asignada de CAT es seis más uno más uno, igual a ocho. La de GATA es cuatro más uno, igual a cinco. Ahora sí, las contribuciones asignadas corresponden a apariciones completas. Vamos a comprobarlas directamente sobre las posiciones, sin confiar sólo en nuestra contabilidad.”

## Descripcion Visual Detallada:

## Objetos:

- Cadena de 11 fichas CGATGATCCAT con índices 1..11; panel i=1,T_1=1,V_1=0; dos fichas C y el AT final.
- Ledger CAT 6→7→8, GATA 5; residuos C 2→1→0, G 0; sello L=11; braces de sufijos con 3,2,1 pares.

## Layout y disposicion:

- Para mantener una fila completa legible, las fichas finales usan x=-5.5+1.1k para k=0..10 y y=0.55. C_8,C_9,A_10,T_11 ocupan x=2.2,3.3,4.4,5.5.
- Panel de pesos en y=2.1; índice y=-0.15. Ledgers en y=-1.3, residuos en y=-2.2; resultado en (0,-3.0,0). Braces de pares previstos en y=1.35 cuando se destaque cada letra, de forma sucesiva.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:26:** Recrear las siete fichas anteriores y registros, mover cursor a uno. Desplazar el último par futuro punteado desde x=2.2,3.3 hasta x=4.4,5.5 para abrir dos ranuras, conservando un único par AT. Emitir C_8 en x=2.2 y actualizar residuo/ledger de manera simultánea; después emitir C_9 en x=3.3 y repetir la actualización. Ambas fichas conservan identidad independiente; no superponerlas con las fichas del par futuro.
- **[TRIGGER_2] — 00:26–00:48:** Atenuar estación G; mostrar V_1=0 con un pequeño diagrama AT sin A posterior. La compuerta i≥2 está cerrada; no dibujar cociente g/0 ni una animación que repita cero.
- **[TRIGGER_3] — 00:48–01:12:** Solidificar A_10,T_11 y borrar los contornos futuros. Escribir índice completo y L=11. Iluminar sucesivamente las braces de sufijos de C_1/G_2, G_5 y C_8/C_9, comprobando 3,2,1 pares.
- **[TRIGGER_4] — 01:12–01:36:** Transformar ledgers en ecuaciones 6+1+1=8 y 4+1=5; añadir residuos finales cero. Tras un hold de lectura, retirar paneles superiores y reservar la fila numerada para la enumeración independiente de CAT.

- **Duración orientativa de la escena:** 01:36. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Dos C finales cian; V_1=0 y estación deshabilitada en TEXT_MUTED. Cerros de residuos y resultado válido en ACCENT_MINT. La longitud once es válida sin compararla aún con una pretendida longitud óptima.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 18

## Nombre: Ver los ocho CAT, uno por uno

## Descripcion Breve: Las tres C de la cadena final particionan exactamente ocho elecciones.

## Objetivo Pedagogico: Auditar la traza completa con las posiciones originales y el conteo triangular.

## Voz en off:

> “[TRIGGER_1] Numeremos la cadena final del uno al once. La primera C está en uno. Las aes posteriores están en tres, seis y diez; las tes, en cuatro, siete y once. Si terminamos en T cuatro, sólo podemos elegir A tres: posiciones uno, tres, cuatro.
> [TRIGGER_2] Si terminamos en T siete, podemos elegir A tres o A seis. Aparecen uno, tres, siete; y uno, seis, siete. Si terminamos en T once, podemos elegir A tres, A seis o A diez. Aparecen uno, tres, once; uno, seis, once; y uno, diez, once. La primera C aporta las seis elecciones de nuestro triángulo.
> [TRIGGER_3] La C de la posición ocho sólo puede usar A diez y T once: ocho, diez, once. La C de la posición nueve usa ese mismo par y produce nueve, diez, once. Son dos elecciones distintas, porque tienen una C inicial diferente. Compartir el final no las vuelve la misma aparición.
> [TRIGGER_4] Ya están las ocho, sin ninguna escondida fuera de la lista. Todo CAT debe comenzar en una de las tres ces que acabamos de revisar, y para cada una enumeramos todos los pares A, T ordenados de su sufijo. Seis más uno más uno. La cadena acierta el objetivo C igual a ocho.”

## Descripcion Visual Detallada:

## Objetos:

- Fila fija CGATGATCCAT con índices; tres cajas de clasificación C_1,C_8,C_9; ocho tarjetas de ternas: (1,3,4),(1,3,7),(1,6,7),(1,3,11),(1,6,11),(1,10,11),(8,10,11),(9,10,11).
- Puntero a T final y contador CAT 0..8; brace 6+1+1.

## Layout y disposicion:

- Fila en x=-5.5+1.1k,y=1.65; índices y=1.1. Caja C_1 centrada en (-2.7,-1.0,0), ancho 6.5, alto 2.6; tarjetas en dos columnas x=-4.1,-1.4 y filas y=-0.25,-1.0,-1.75.
- Cajas C_8 y C_9 en (3.55,-0.55,0) y (3.55,-1.7,0), ancho 3.6, alto 0.9. Fórmula en (0,-2.95,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Recrear fila final en la nueva altura antes de contar. Abrir cajas y dejar ocho tarjetas vacías; contador cero. Trazar 1→3→4, llenar primera tarjeta y subir contador a uno.
- **[TRIGGER_2] — 00:21–00:46:** Puntero a T_7: trazar 1→3→7 y 1→6→7, llenando dos tarjetas y llevando contador a tres. Puntero a T_11: trazar 1→3→11,1→6→11,1→10→11, llenar las otras tres y llevar contador a seis. Cada ruta se apaga antes de la siguiente, salvo su tarjeta.
- **[TRIGGER_3] — 00:46–01:10:** Iluminar C_8 y trazar 8→10→11, contador siete. Iluminar C_9 y trazar 9→10→11, contador ocho. Unir las dos tarjetas sólo mediante brace, sin fundirlas.
- **[TRIGGER_4] — 01:10–01:34:** Señalar las tres únicas posiciones C en la fila; crear una flecha de partición hacia sus cajas. Escribir 6+1+1=8 y sello objetivo CAT. Mantener por dos segundos el inventario de ocho; retirar cajas para pasar a GATA, conservando la cadena.

- **Duración orientativa de la escena:** 01:34. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Cajas y arcos CAT en ACCENT_CYAN, T final activa terracota. Resultado en ACCENT_MINT. Las tarjetas usan TEXT_MAIN y 27 pt; índices de cadena 24 pt. Nunca reemplazar la lista por una indicación de repetir el resto.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 19

## Nombre: Ver los cinco GATA, uno por uno

## Descripcion Breve: Las G en posiciones 2 y 5 producen cuatro y una elecciones.

## Objetivo Pedagogico: Auditar el segundo objetivo y comprobar que las C intermedias no interfieren.

## Voz en off:

> “[TRIGGER_1] Las ges están en las posiciones dos y cinco. Para la G de la posición dos, si elegimos T cuatro, la primera A tiene que estar en tres y la última puede estar en seis o diez. Obtenemos dos, tres, cuatro, seis; y dos, tres, cuatro, diez.
> [TRIGGER_2] Si esa misma G elige T siete, la primera A puede estar en tres o seis y la última debe estar en diez. Obtenemos dos, tres, siete, diez; y dos, seis, siete, diez. T once no sirve: no hay una A después. La primera G aporta exactamente cuatro.
> [TRIGGER_3] Para la G de la posición cinco sólo hay una elección: A seis, T siete, A diez. Sus posiciones completas son cinco, seis, siete, diez. Las ces de ocho y nueve quedan entre la T y la última A, pero las podemos saltar. La cadena no exige que las cuatro letras queden juntas.
> [TRIGGER_4] Todo GATA comienza en una de estas dos ges. Hemos revisado las dos, y para cada una todas las tes posibles y las aes que quedan a sus lados. Cuatro más uno: cinco. La misma cadena produce ocho CAT y cinco GATA. No concatenamos dos respuestas: los dos objetivos comparten el mismo esqueleto.”

## Descripcion Visual Detallada:

## Objetos:

- Fila final heredada; cajas G_2 y G_5; cinco tarjetas: (2,3,4,6),(2,3,4,10),(2,3,7,10),(2,6,7,10),(5,6,7,10).
- Contador GATA 0..5; etiquetas sufijos con 3 y 2 pares; resultados N_CAT=8 y N_GATA=5.

## Layout y disposicion:

- Cadena conserva x=-5.5+1.1k,y=1.65. Caja G_2 en (-2.15,-1.0,0), tamaño 7.4×2.55; sus tarjetas en x=-4.0,-0.3 y filas y=-0.45,-1.5.
- Caja G_5 en (4.0,-1.0,0), tamaño 3.2×2.55; única tarjeta en y=-1.0, dividida en dos líneas si supera ancho 2.9. Totales en y=-2.95.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Crear cajas G y contador cero; señalar G_2. Trazar 2→3→4→6 y 2→3→4→10, crear sus tarjetas y llevar contador a dos.
- **[TRIGGER_2] — 00:22–00:44:** Trazar 2→3→7→10 y 2→6→7→10, llevar contador a cuatro. Señalar T_11 y mostrar su región posterior vacía; no crear una tarjeta adicional para ese caso.
- **[TRIGGER_3] — 00:44–01:08:** Señalar G_5 y trazar 5→6→7→10 con arco que pasa sobre las C_8,C_9. Crear última tarjeta y llevar contador a cinco. Atenuar sólo durante el recorrido las letras omitidas, restaurando sus colores al terminar.
- **[TRIGGER_4] — 01:08–01:32:** Mostrar partición por las dos G, escribir 4+1=5 y recuperar la tarjeta CAT=8. Crear una brace común del esqueleto A/T compartido; cerrar ambas verificaciones. Retirar la cadena para generalizar con sumas y residuos.

- **Duración orientativa de la escena:** 01:32. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Cajas GATA y rutas principales en ACCENT_INDIGO, conectores cian. A/T conservan sus colores; C omitidas en TEXT_MUTED durante el paso. Ambos resultados en ACCENT_MINT.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 20

## Nombre: La contabilidad que no puede perder una aparición

## Descripcion Breve: Objetivo, contribuciones asignadas y residuo se conservan en cada inserción.

## Objetivo Pedagogico: Formalizar el invariante de residuos y las multiplicidades sin código.

## Voz en off:

> “[TRIGGER_1] Pasemos del ejemplo a cualquier solicitud. En el hueco con i pares posteriores, llamemos a sub i al número de ces y b sub i al número de ges. Como cada una aporta lo mismo, ese hueco asigna a sub i por T sub i al objetivo CAT y b sub i por V sub i al objetivo GATA.
> [TRIGGER_2] En cada momento mantenemos una igualdad: el objetivo original es lo ya asignado más lo que falta. Al insertar una C, la parte asignada aumenta T sub i y el residuo C disminuye exactamente T sub i. El total no cambia. Para G ocurre la misma conservación con V sub i.
> [TRIGGER_3] También podemos agrupar todas las letras iguales de un hueco en una decisión. Si el residuo C es r, tomamos el cociente entero de r entre T sub i. La cantidad asignada es ese cociente por el peso, y el nuevo residuo es r menos esa cantidad: está entre cero y el peso menos uno. Para G hacemos esa división sólo cuando i es al menos dos.
> [TRIGGER_4] Cuando termina la cadena, las asignaciones se vuelven contribuciones reales. Por la partición según la letra inicial, el total CAT es la suma de todos los a sub i por T sub i. El total GATA es la suma de los b sub i por V sub i. La conservación demuestra que acertamos los objetivos si los residuos terminan en cero; ahora falta asegurar ese último paso.”

## Descripcion Visual Detallada:

## Objetos:

- Dos barras de contabilidad, objetivo original fijo = asignado + residuo; fichas de contribución que pasan del residuo al asignado.
- MathTex C_0=Σa_iT_i+r_C, G_0=Σb_iV_i+r_G; cocientes a_i=⌊r_C/T_i⌋ y b_i=⌊r_G/V_i⌋ para i≥2; rangos 0≤r_nuevo<peso.
- Fórmulas finales N_CAT=Σ_{i=1}^{144}a_iT_i y N_GATA=Σ_{i=2}^{144}b_iV_i. C_0,G_0 denotan objetivos originales; r_C,r_G residuos, sin reutilizar nombres ambiguos.

## Layout y disposicion:

- Barra CAT en y=1.65 y GATA en y=0.1, de x=-5.6 a 5.6. Objetivo fijo al margen izquierdo, asignado en x=-1.8 y residuo en x=3.3.
- Fórmulas de conservación en y=-1.3,-2.3. Para cocientes, sustituir barras por dos tarjetas de ancho 5.5 centradas en x=-3.0 y 3.0, y=0.6; condición inferior en y=-2.5.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:27:** Crear hueco genérico con a_i fichas C y b_i fichas G representadas por brace de multiplicidad; mostrar los productos a_iT_i,b_iV_i. Los grupos rotulados son cantidades simbólicas, no una omisión del ejemplo ya enumerado.
- **[TRIGGER_2] — 00:27–00:51:** Crear dos barras con total fijo; mover una ficha de peso del residuo al asignado en CAT y después en GATA. Mantener la longitud total de cada barra y escribir igualdades; residuo no baja de cero.
- **[TRIGGER_3] — 00:51–01:21:** Mostrar esquema r=q·peso+r_nuevo y división entera mediante grupos completos de fichas de valor. Para C usar ejemplo r=8,peso=6; para G r=5,peso=4, ambos ya conocidos. Escribir rangos y guardia i≥2 antes del cociente G.
- **[TRIGGER_4] — 01:21–01:51:** Transformar asignado en las sumas con límites completos. Añadir debajo condición r_C=r_G=0 con contorno aún abierto, para señalar que será probada en la siguiente escena. No usar sello de corrección antes de cerrarla.

- **Duración orientativa de la escena:** 01:51. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Asignado CAT en cian y GATA en índigo; residuo en terracota. Objetivos originales en TEXT_MAIN y límites en TEXT_MUTED; guardia i≥2 con borde ACCENT_INDIGO.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 21

## Nombre: Empezar tarde, pero no abandonar el esqueleto

## Descripcion Breve: Omitir pares antes de la primera inserción es válido; omitirlos después destruye pesos.

## Objetivo Pedagogico: Justificar la bandera de inicio mediante un ejemplo que expone el compromiso futuro.

## Voz en off:

> “[TRIGGER_1] Hay un detalle pequeño que sostiene toda la construcción. Antes de insertar la primera C o G, podemos omitir los pares AT de índices altos. No hay ninguna letra especial anterior que los necesite. Omitirlos sólo acorta una región que no aporta a nuestros objetivos.
> [TRIGGER_2] Después de la primera inserción, la situación cambia. Supongamos que pedimos cero GATA y seis CAT. En el índice tres insertamos una C de peso seis y los residuos ya quedan en cero. Aun así debemos escribir el AT de tres, el de dos y el de uno. La salida correcta es CATATAT.
> [TRIGGER_3] ¿Qué pasaría si nos detuviéramos al ver los residuos cero, o si saltáramos los huecos donde no insertamos nada? [Pausa.] Nos quedaría CAT. Esa C sólo tendría un par a su derecha y aportaría uno, no seis. La contabilidad prometió tres pares, pero la cadena habría entregado uno.
> [TRIGGER_4] Por eso mantenemos un estado de dos posibilidades: todavía no empezamos, o ya empezamos. Pasa al segundo estado cuando aparece la primera C o G, y nunca vuelve atrás. En ese estado, todos los pasos restantes emiten su par AT, aunque sus multiplicidades sean cero. Planificar un sufijo exige terminarlo.”

## Descripcion Visual Detallada:

## Objetos:

- Diagrama de dos estados no iniciada e iniciada, con única transición por insertar C/G y lazo AT en iniciada; cadena correcta CATATAT y alternativa truncada CAT.
- Solicitud (G,C)=(0,6), tres compromisos de pares y contadores prometido 6, real truncado 1.

## Layout y disposicion:

- Diagrama de estados en x=-3.4,y=1.1, nodos en (-4.6,1.1,0) y (-1.5,1.1,0), radio 0.8; transición a y=1.6.
- Carril correcto en y=-0.8,x=-5.4..2.4 y carril truncado en y=-2.05,x=-5.4..-3.2; resultados en x=4.0. La fila superior de compromiso ocupa x=0.5..5.7,y=1.1.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear diagrama en estado no iniciada y una reserva AT sin letras especiales. Eliminar sólo los pares antes de la primera inserción, con rótulo ningún compromiso pendiente.
- **[TRIGGER_2] — 00:21–00:45:** Introducir solicitud (0,6); insertar C en i=3 y marcar tres pares obligatorios. Emitir AT de pasos 3,2,1 aunque los dos últimos tengan cero inserciones. Completar CATATAT y mostrar seis.
- **[TRIGGER_3] — 00:45–01:08:** Duplicar construcción en carril de experimento; quitar pares de pasos 2 y 1. Escribir CAT y actualizar conteo real a uno, manteniendo seis como promesa incumplida. Durante la pausa, un arco muestra los dos pares que faltan.
- **[TRIGGER_4] — 01:08–01:31:** Retirar experimento fallido. Activar estado iniciada con flecha única C/G y lazo emitir AT para todo paso restante. Escribir que el estado no se desactiva cuando los residuos llegan a cero. Conservar sólo el diagrama como recordatorio breve.

- **Duración orientativa de la escena:** 01:31. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Estado activo con borde ACCENT_MINT; reserva en TEXT_MUTED; incumplimiento 1 frente a 6 en ACCENT_VINO. Diagrama de control con flechas ACCENT_CYAN; las letras mantienen su paleta.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 22

## Nombre: Exactitud: el último peso elimina cualquier residuo

## Descripcion Breve: T_1=1 y V_2=1 cierran la representación para ambos objetivos.

## Objetivo Pedagogico: Completar la prueba de corrección para todo el dominio, separada de la prueba de tamaño.

## Voz en off:

> “[TRIGGER_1] Las ces tienen una última oportunidad en el índice uno, donde el peso vale uno. Si el residuo C es r, escribimos r ces y restamos r unidades. Queda cero. Para las ges, la última oportunidad es el índice dos: V dos también vale uno. Cualquier residuo G se consume ahí.
> [TRIGGER_2] Ninguna resta es mayor que el residuo, porque sólo insertamos una letra cuando su peso cabe. Los residuos nunca se vuelven negativos. Tampoco dependemos de que los pesos sean mágicos o de que el greedy use pocas monedas: el valor uno basta para la exactitud.
> [TRIGGER_3] La salida completa respeta el número de pares posteriores de cada hueco. La partición por C o G inicial convierte las contribuciones en sumas exactas. Y la conservación de objetivos más residuos, ahora con los dos residuos en cero, nos da exactamente el número pedido de CAT y de GATA.
> [TRIGGER_4] Eso prueba que fabricamos las cantidades correctas. Pero podríamos haber usado demasiadas letras de valor uno. La pregunta decisiva que queda es: ¿qué tan rápido se reduce el residuo al tomar pesos grandes? [Pausa.] Ahora vamos a demostrar que la misma construcción cabe holgadamente en quinientos caracteres.”

## Descripcion Visual Detallada:

## Objetos:

- Dos embudos de residuos con salidas T_1=1 y V_2=1; fichas unitarias multiplicadas mediante brace r; MathTex r−r·1=0.
- Tres tarjetas enlazadas: sufijos cumplidos, partición de apariciones, residuos cero; dos resultados finales N_CAT=C_0,N_GATA=G_0.
- Regla de longitud 500 reaparece con espacio de uso todavía desconocido.

## Layout y disposicion:

- Embudo CAT centrado en (-3.2,1.0,0) y GATA en (3.2,1.0,0), cada uno ancho 4.8. Igualdades unitarias en y=-0.6.
- Tarjetas de prueba en x=-4.3,0,4.3,y=-1.7; resultados en y=-2.6. Para el cierre, la regla ocupa x=-5.8..5.8,y=-1.2 y pregunta en y=0.75.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear dos residuos simbólicos distintos r_C y r_G; enviar cada uno al peso uno correcto. Dibujar r fichas mediante multiplicidad exacta y actualizar ambos a cero con la igualdad de resta.
- **[TRIGGER_2] — 00:24–00:45:** Crear la guardia peso≤residuo en ambos canales y escribir no negatividad. Separar visualmente tarjeta exactitud de tarjeta número de letras, dejando esta última pendiente.
- **[TRIGGER_3] — 00:45–01:08:** Encadenar las tres tarjetas de prueba en el orden sufijos→partición→conservación. Escribir ambos resultados y cerrar sus contornos con sello válido. No añadir una afirmación de longitud mínima.
- **[TRIGGER_4] — 01:08–01:31:** Retirar tarjetas, recuperar regla 500 y poner bajo ella tres sumandos vacíos: letras A/T, letras C, letras G. Formular pregunta y sostener pausa; preparar el límite del esqueleto.

- **Duración orientativa de la escena:** 01:31. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Prueba completada en ACCENT_MINT; canales CAT cian y GATA índigo. Pregunta sobre tamaño en terracota; cota aún no probada sin sello verde.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 23

## Nombre: Medir la cadena por sus tres ingredientes

## Descripcion Breve: La longitud se separa en esqueleto, C y G con cotas independientes.

## Objetivo Pedagogico: Plantear una prueba uniforme para todos los objetivos y fijar el alcance de B=144.

## Voz en off:

> “[TRIGGER_1] Una respuesta tiene tres ingredientes: las aes y tes del esqueleto, las ces insertadas y las ges insertadas. Con ciento cuarenta y cuatro pares como máximo, el primer ingrediente cuesta dos por ciento cuarenta y cuatro: doscientas ochenta y ocho letras.
> [TRIGGER_2] Si empezamos en un índice menor, usamos menos pares. Para la prueba nos permitimos cobrar los ciento cuarenta y cuatro completos: una cota conservadora vale para cualquier punto de inicio. Reservar capacidad no obliga a usarla toda.
> [TRIGGER_3] Ahora necesitamos acotar cuántas ces y cuántas ges inserta el greedy para objetivos desde cero hasta un millón. No basta con encontrar muchos ejemplos que funcionan. Queremos una desigualdad que cubra todos los números del intervalo, incluidos los que dejan residuos difíciles de pagar.
> [TRIGGER_4] La clave es la distancia entre dos pesos consecutivos. Después de tomar el mayor peso que cabe, el residuo cae por debajo de esa distancia. En los pesos triangulares, la distancia crece mucho más lentamente que el peso. En los de G ocurre algo parecido. Esa caída nos va a permitir cerrar la cuenta sin recorrer un millón de casos en la demostración.”

## Descripcion Visual Detallada:

## Objetos:

- Regla de capacidad 500 y barra apilada provisional con segmento A/T=288 y segmentos C,G sin valor; MathTex L≤2B+n_C+n_G, B=144.
- Contorno de dominio 0≤G,C≤10^6 y tarjeta prueba para todo el intervalo; vista de dos pesos consecutivos con diferencia destacada.

## Layout y disposicion:

- Regla x=-5.8..5.8,y=0.7. Segmento esqueleto ocupa exactamente 288/500 de la regla; segmentos C/G se dibujan inicialmente fuera de la barra como tarjetas de ancho no proporcional, rotuladas pendiente.
- Ecuación de longitud en (0,2.0,0); dominio en (0,-0.4,0); pesos consecutivos en x=-2.7 y 2.7,y=-1.75, diferencia en y=-2.7.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear fórmula L y colorear sus tres términos según ingrediente. Solidificar el segmento de 288 con brace 144 pares, cada uno de dos letras. No crear 288 fichas individuales ilegibles; la multiplicidad está escrita.
- **[TRIGGER_2] — 00:19–00:37:** Duplicar una barra más corta con inicio menor y alinearla al mismo origen. Mostrar ≤288, no igualdad para todas las salidas. Retirar barra auxiliar.
- **[TRIGGER_3] — 00:37–00:58:** Encerrar el dominio completo y poner una lupa sobre varios residuos simbólicos, sin presentar una muestra como prueba. Rotular garantía analítica y mantener pendientes los sumandos C/G.
- **[TRIGGER_4] — 00:58–01:27:** Mostrar pesos w_j y w_{j+1}, residuo r entre ambos y la operación r−w_j. Dibujar la caída hasta una ventana de altura w_{j+1}−w_j. Preparar la especialización triangular.

- **Duración orientativa de la escena:** 01:27. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- A/T representadas juntas por segmento terracota con etiqueta esqueleto; C cian y G índigo. Dominio en TEXT_MAIN, cuantificador para todo en ACCENT_MINT, pendientes en TEXT_MUTED.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 24

## Nombre: El residuo CAT cae por debajo del índice siguiente

## Descripcion Breve: La primera tanda cuesta como máximo 95 C y el resto se contrae usando T_{j+1}−T_j=j+1.

## Objetivo Pedagogico: Probar el mecanismo de contracción antes de aplicar la cadena de cotas.

## Voz en off:

> “[TRIGGER_1] En el hueco ciento cuarenta y cuatro, una C aporta diez mil cuatrocientos cuarenta. Noventa y cinco veces ese peso da novecientos noventa y un mil ochocientos. Noventa y seis veces ya supera un millón. Así que en ese hueco pueden aparecer como máximo noventa y cinco ces.
> [TRIGGER_2] Después de usar todas las que caben, el residuo queda estrictamente por debajo de diez mil cuatrocientos cuarenta. Esa afirmación también vale si el objetivo era pequeño y no usamos ninguna. Lo importante para el siguiente paso no es el objetivo original, sino esta cota del resto.
> [TRIGGER_3] Elijamos ahora el mayor índice j cuyo peso triangular cabe en el residuo r. Por ser el mayor, r está entre T j incluido y T j más uno excluido. Restamos una sola C de peso T j. Entonces el nuevo residuo es menor que T j más uno menos T j.
> [TRIGGER_4] Escribamos ambos pesos: j más uno por j más dos, entre dos, menos j por j más uno, entre dos. Sacamos el factor j más uno y queda dos entre dos: j más uno. Así, una inserción nos deja un residuo menor que j más uno. Puede requerirse otra C en el mismo hueco; la desigualdad sigue siendo válida para el siguiente residuo. Ahora encadenemos ese descenso.”

## Descripcion Visual Detallada:

## Objetos:

- Tarjeta T_144=10440; bloques 95·10440=991800 y 96·10440=1002240; cota r<10440.
- Recta de intervalo T_j≤r<T_{j+1}; flecha de resta T_j; desarrollo MathTex T_{j+1}−T_j=((j+1)(j+2)−j(j+1))/2=j+1.

## Layout y disposicion:

- Cálculos superiores en x=-3.0 y 3.0,y=1.4; tarjeta T_144 en (0,2.35,0). Residuo en y=0.35.
- Recta x=-5.0..5.0,y=-0.8; desigualdad de reducción en y=-1.65; desarrollo algebraico en y=-2.55, ancho máximo 11.6 con fuentes 30 pt.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Escribir T_144 y los dos productos completos. Relacionar 991800≤10^6<1002240 mediante una llave y fijar n_C inicial≤95. El segundo producto recibe borde de exceso, no se emite.
- **[TRIGGER_2] — 00:22–00:44:** Mover la cantidad pagada a un contenedor asignado y mantener una ventana de resto rotulada r<10440. Mostrar caso de cero monedas con la misma ventana válida; no afirmar que todo objetivo deja el mismo residuo.
- **[TRIGGER_3] — 00:44–01:08:** Crear recta con marcas T_j,T_{j+1} y r situado en intervalo semiabierto. Trasladar r a r−T_j; transformar la ventana en 0≤r_nuevo<T_{j+1}−T_j. Destacar que se analiza una inserción.
- **[TRIGGER_4] — 01:08–01:38:** Desarrollar diferencia en tres transformaciones: numerador factorizado, factor (j+1)·2/2 y j+1. Conservar esta fórmula como lema de contracción CAT, junto con el presupuesto inicial 95. Ningún cambio de fórmula queda fuera del trigger.

- **Duración orientativa de la escena:** 01:38. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Lema CAT con borde ACCENT_CYAN; r y j activos en ACCENT_TERRACOTTA. Producto que excede el dominio en ACCENT_VINO; cota válida en ACCENT_MINT. Signos < y ≤ se conservan exactamente.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 25

## Nombre: Cuatro caídas y dos unidades: como máximo 101 ces

## Descripcion Breve: La cadena r<10440→r<144→r<17→r<6→r<3 concluye en dos C de valor uno.

## Objetivo Pedagogico: Demostrar todas las cotas numéricas y sumar el presupuesto de C sin una constante empírica.

## Voz en off:

> “[TRIGGER_1] Con un residuo menor que diez mil cuatrocientos cuarenta, el mayor índice posible es ciento cuarenta y tres. Una C deja menos de ciento cuarenta y cuatro. No necesitamos que siempre elija ese índice; cualquier índice menor produce una cota todavía mejor.
> [TRIGGER_2] Si el residuo es menor que ciento cuarenta y cuatro, el mayor índice que puede caber es dieciséis: T dieciséis vale ciento treinta y seis, y T diecisiete vale ciento cincuenta y tres. Otra C deja menos de diecisiete. Si el residuo es menor que diecisiete, el índice máximo es cinco: quince cabe, veintiuno no. Otra C deja menos de seis.
> [TRIGGER_3] Con residuo menor que seis, el índice máximo es dos: T dos vale tres, T tres vale seis. Una C deja menos de tres. Como el residuo es entero y no negativo, sólo puede quedar cero, uno o dos. Esas últimas unidades se pagan con como máximo dos ces de peso uno.
> [TRIGGER_4] Después de la tanda inicial hemos usado como máximo cuatro ces para esas cuatro caídas, y como máximo dos para el final. Si el residuo llega antes a cero, no hacemos las inserciones restantes. Sumamos noventa y cinco, más cuatro, más dos: como máximo ciento una ces. Esta es una cota para cualquier objetivo C hasta un millón.”

## Descripcion Visual Detallada:

## Objetos:

- Tabla completa con filas: r<10440,j≤143,r_nuevo<144; r<144,j≤16,r_nuevo<17; r<17,j≤5,r_nuevo<6; r<6,j≤2,r_nuevo<3.
- Celdas de evidencia T_143=10296,T_144=10440; T_16=136,T_17=153; T_5=15,T_6=21; T_2=3,T_3=6.
- Tres terminales de resto 0,1,2 y fichas unitarias; MathTex n_C≤95+4+2=101.

## Layout y disposicion:

- Tabla de ancho 11.8, cabecera y=2.1 y cuatro filas y=1.25,0.4,-0.45,-1.3. Columnas residuo x=-4.6, índice x=-1.6, evidencia x=1.65, nuevo residuo x=4.75.
- Terminales 0,1,2 en x=-2.4,0,2.4,y=-2.2; suma final en y=-3.1. Evidencias se parten en dos líneas de MathTex de 24 pt, sin comprimir texto principal.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear tabla con primera fila y conectar lema r_nuevo<j+1 con j≤143. Escribir explícitamente los pesos que fijan el límite 143. Encender una ficha de gasto adicional.
- **[TRIGGER_2] — 00:20–00:48:** Crear segunda fila con 136≤r posible y 153>cota; aplicar j+1≤17. Después crear tercera con pesos 15 y 21 y nueva cota seis. Añadir una ficha de gasto por cada fila, sin asumir que cada entrada alcanza su cota máxima.
- **[TRIGGER_3] — 00:48–01:12:** Crear cuarta fila con pesos 3 y 6, producir r<3. Desplegar tres terminales: cero usa ninguna ficha, uno usa una, dos usa dos. Rotular esta última rama como máximo dos.
- **[TRIGGER_4] — 01:12–01:38:** Encerrar las cuatro filas con brace cuatro inserciones como máximo. Escribir 95+4+2=101 y conectar el resultado con el segmento C pendiente de la regla. Si se quiere mostrar terminación temprana, desactivar una rama con r=0 sin crear nuevas cifras fuera del trigger.

- **Duración orientativa de la escena:** 01:38. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Filas y fichas C en ACCENT_CYAN; umbrales activos terracota. Terminación temprana en ACCENT_MINT y filas no usadas en TEXT_MUTED. La suma 101 se rotula cota superior, no máximo alcanzado.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 26

## Nombre: Las ges reducen un cubo a un triángulo

## Descripcion Breve: Dos G iniciales bastan en i=144 y la diferencia V_{j+1}−V_j es T_j.

## Objetivo Pedagogico: Derivar una cota GATA comparable a la triangular con todas las desigualdades.

## Voz en off:

> “[TRIGGER_1] En el hueco ciento cuarenta y cuatro, una G aporta cuatrocientos noventa y siete mil seiscientos cuarenta. Dos ges aportan novecientos noventa y cinco mil doscientos ochenta; tres superarían un millón. Por tanto, el primer hueco usa como máximo dos ges y deja un residuo menor que cuatrocientos noventa y siete mil seiscientos cuarenta.
> [TRIGGER_2] Buscamos otra vez el mayor peso que cabe, ahora V j. El residuo está entre V j y V j más uno. Al restar una G, el nuevo resto queda por debajo de V j más uno menos V j. La idea de la prueba es la misma conservación de un intervalo, pero la diferencia tiene otro tamaño.
> [TRIGGER_3] Usamos las fórmulas que ya demostramos: j por j más uno por j más dos, entre seis, menos j menos uno por j por j más uno, entre seis. Factorizamos j por j más uno. Dentro queda j más dos menos j menos uno: tres. Dividimos tres entre seis y obtenemos j por j más uno entre dos.
> [TRIGGER_4] Esa es exactamente T j. Después de una G, un residuo gobernado por pesos cúbicos cae por debajo de un peso triangular. Es la misma relación que descubrimos al añadir una A al esqueleto: los nuevos triples se cuentan mediante pares. Ahora la usaremos para medir cuántas ges necesitamos.”

## Descripcion Visual Detallada:

## Objetos:

- Tarjeta V_144=497640; productos 2·497640=995280 y 3·497640=1492920; residuo r<497640.
- Intervalo V_j≤r<V_{j+1}; derivación V_{j+1}−V_j=j(j+1)((j+2)−(j−1))/6=j(j+1)/2=T_j.
- Conector conceptual recurrencia V_{j+1}=V_j+T_j.

## Layout y disposicion:

- Tarjeta superior en y=2.35; productos en x=-3.1 y 3.1,y=1.3. Ventana de residuo en y=0.25.
- Intervalo y=-0.8 y desarrollo en y=-1.7,-2.6, con ancho máximo 11.8. Usar dos líneas para la factorización, evitando expresiones de más de 12 unidades de ancho.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:25:** Crear V_144, mostrar productos por dos y tres y fijar n_G inicial≤2. Encerrar 995280≤10^6<1492920 y crear ventana de residuo estricta.
- **[TRIGGER_2] — 00:25–00:51:** Crear intervalo V_j,V_{j+1}; representar r y trasladarlo por −V_j. Escribir r_nuevo<V_{j+1}−V_j. No reemplazar el signo estricto por ≤ durante la transformación.
- **[TRIGGER_3] — 00:51–01:17:** Mostrar las dos fórmulas desarrolladas, factorizar j(j+1)/6 y simplificar el paréntesis (j+2)−(j−1)=3, con paréntesis visibles. Transformar a j(j+1)/2 y finalmente T_j.
- **[TRIGGER_4] — 01:17–01:40:** Conectar T_j con la tarjeta de pesos CAT anterior y con la recurrencia de triples. Mantener letra G como dueña de la inserción: T_j es sólo la cota del residuo posterior, no el peso pagado por esa G. Preparar la tabla de cinco caídas.

- **Duración orientativa de la escena:** 01:40. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Lema GATA en ACCENT_INDIGO; diferencia triangular con pequeño acento cian. Productos excesivos en ACCENT_VINO. La letra G no cambia a C durante el reconocimiento de T_j.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 27

## Nombre: Cinco caídas dejan veinte o menos

## Descripcion Breve: Las cotas del residuo G pasan por 10296,780,136,45 y 21.

## Objetivo Pedagogico: Demostrar cada índice máximo y contar exactamente cinco inserciones adicionales como cota.

## Voz en off:

> “[TRIGGER_1] Con residuo menor que cuatrocientos noventa y siete mil seiscientos cuarenta, el índice máximo es ciento cuarenta y tres. La siguiente G deja menos de T ciento cuarenta y tres: diez mil doscientos noventa y seis.
> [TRIGGER_2] Con menos de diez mil doscientos noventa y seis, el índice máximo es treinta y nueve: V treinta y nueve vale nueve mil ochocientos ochenta, y V cuarenta vale diez mil seiscientos sesenta. Una G deja menos de T treinta y nueve, que es setecientos ochenta. Con menos de setecientos ochenta, el índice máximo es dieciséis: seiscientos ochenta cabe, ochocientos dieciséis no. Otra G deja menos de ciento treinta y seis.
> [TRIGGER_3] Con menos de ciento treinta y seis, el índice máximo es nueve: V nueve vale ciento veinte y V diez ciento sesenta y cinco. Una G deja menos de T nueve, cuarenta y cinco. Con menos de cuarenta y cinco, el índice máximo es seis: V seis vale treinta y cinco y V siete cincuenta y seis. Una G deja menos de T seis, veintiuno.
> [TRIGGER_4] Son cinco inserciones después de la tanda inicial. El residuo final es entero y menor que veintiuno: como máximo veinte. Si en cualquier momento llegó a cero, usamos menos. Falta cerrar ese último intervalo pequeño sin sumar máximos incompatibles. Vamos a revisar exactamente los pesos que pueden entrar ahí.”

## Descripcion Visual Detallada:

## Objetos:

- Tabla de cinco filas: r<497640,j≤143,r_nuevo<10296; r<10296,j≤39,r_nuevo<780; r<780,j≤16,r_nuevo<136; r<136,j≤9,r_nuevo<45; r<45,j≤6,r_nuevo<21.
- Evidencias consecutivas V_143=487344,V_144=497640; V_39=9880,V_40=10660; V_16=680,V_17=816; V_9=120,V_10=165; V_6=35,V_7=56.
- Columna de diferencias T_143=10296,T_39=780,T_16=136,T_9=45,T_6=21; cinco fichas G de gasto.

## Layout y disposicion:

- Tabla ancho 12, cabecera y=2.45 y filas y=1.65,0.9,0.15,-0.6,-1.35. Columnas residuo x=-4.7, índice x=-1.6, dos pesos x=1.65 y nuevo residuo x=4.8.
- Brace cinco inserciones en x=-6.1 con rótulo corto vertical o tarjeta debajo; conclusión 0≤r≤20 en (0,-2.65,0). Filas de evidencia de 23–24 pt; filas activas pueden ampliarse en un recuadro inferior y después volver.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:17:** Crear primera fila con los dos pesos consecutivos, aplicar j≤143 al lema r_nuevo<T_j y completar 10296. Encender primera ficha G de gasto.
- **[TRIGGER_2] — 00:17–00:49:** Crear segunda fila con 9880 y 10660; señalar su cota triangular 780. Crear tercera con 680 y 816 y completar 136. Encender una ficha por cada inserción, manteniendo la tabla anterior visible.
- **[TRIGGER_3] — 00:49–01:18:** Crear cuarta fila con 120 y 165, completar 45; crear quinta con 35 y 56, completar 21. Cada fórmula T_j se muestra antes de su valor numérico, aunque pueda caber en el mismo trigger.
- **[TRIGGER_4] — 01:18–01:41:** Cerrar brace de cinco pasos y transformar r<21 junto con r entero no negativo en 0≤r≤20. Conservar presupuesto G inicial≤2 y adicional≤5 en dos tarjetas; retirar tabla para estudiar la cola exacta.

- **Duración orientativa de la escena:** 01:41. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Filas G en índigo, diferencias T_j cian y r activo terracota. Cotizaciones y comparaciones en TEXT_MAIN. Tabla completa legible, sin usar una fila de puntos suspensivos para los cinco pasos.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 28

## Nombre: El residuo pequeño: cinco ges bastan

## Descripcion Breve: Los pesos 20,10,4,1 representan todos los residuos 0..20 con como máximo cinco G.

## Objetivo Pedagogico: Cerrar rigurosamente la cola del greedy mediante casos exhaustivos y restricciones compatibles.

## Voz en off:

> “[TRIGGER_1] Para un residuo de cero a veinte, los pesos positivos que pueden importar son veinte, diez, cuatro y uno. Corresponden a cinco, cuatro, tres y dos pares posteriores. Si el residuo es veinte, usamos una G de peso veinte y terminamos.
> [TRIGGER_2] Si el residuo es de cero a nueve, sólo usamos cuatros y unos. Escríbelo como cuatro q más t, con t igual a cero, uno, dos o tres. Como el residuo no supera nueve, q no supera dos. Si q es dos, t sólo puede ser cero o uno: usamos como máximo tres letras. Si q es uno, usamos como máximo una de cuatro y tres de uno: cuatro letras. Si q es cero, como máximo tres.
> [TRIGGER_3] Si el residuo está entre diez y diecinueve, primero usamos una G de peso diez. Queda un número entre cero y nueve, que acabamos de demostrar que cuesta como máximo cuatro letras. Total: como máximo cinco. El caso diecisiete lo alcanza: diez más cuatro más uno más uno más uno.
> [TRIGGER_4] No podemos sumar sin más una moneda de diez, dos de cuatro y tres de uno: esa suma sería veintiuno, fuera del intervalo. Las cantidades máximas no ocurren simultáneamente. La tabla muestra todas las descomposiciones de cero a veinte; los casos anteriores prueban que ninguna usa más de cinco.
> [TRIGGER_5] Ahora cerramos la cuenta G completa: como máximo dos en el primer hueco, cinco durante las caídas y cinco en el resto pequeño. Dos más cinco más cinco: doce ges. Si algunos de esos grupos no se necesitan, la cadena se acorta. Esta cota basta para nuestro objetivo.”

## Descripcion Visual Detallada:

## Objetos:

- Tabla exhaustiva de residuos y descomposición voraz: 0=0; 1=1; 2=1+1; 3=1+1+1; 4=4; 5=4+1; 6=4+1+1; 7=4+1+1+1; 8=4+4; 9=4+4+1; 10=10; 11=10+1; 12=10+1+1; 13=10+1+1+1; 14=10+4; 15=10+4+1; 16=10+4+1+1; 17=10+4+1+1+1; 18=10+4+4; 19=10+4+4+1; 20=20.
- Columnas de cantidad de letras: 0,1,2,3,1,2,3,4,2,3,1,2,3,4,2,3,4,5,3,4,1 respectivamente. Tarjetas V_5=20,V_4=10,V_3=4,V_2=1.
- Diagrama de casos r∈[0,9],r∈[10,19],r=20; fórmula n_G≤2+5+5=12.

## Layout y disposicion:

- Dos paneles de tabla centrados en (-3.1,0.3,0) y (3.1,0.3,0), ancho 5.7; diez filas r=0..9 a la izquierda y diez r=10..19 a la derecha, y=2.25−0.46k. Caso 20 en (0,-2.8,0).
- Columnas por panel: r al extremo izquierdo, descomposición al centro, número de G al extremo derecho; texto 23–24 pt. Para demostrar q,t, sustituir tabla por tres tarjetas q=0,1,2 en x=-3.9,0,3.9,y=0.4; restaurar tabla al terminar.
- Presupuesto final en y=-3.2 sólo después de retirar el caso 20; no superponer ambos textos.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear tarjetas de pesos y caso 20=20 con una G. Las filas restantes de la tabla se mantienen vacías; no usar la conclusión antes de los casos.
- **[TRIGGER_2] — 00:19–00:53:** Mostrar r=4q+t y desplegar q=0 con t≤3, q=1 con t≤3, q=2 con t≤1. Escribir costos máximos 3,4,3. Restaurar tabla y llenar las diez descomposiciones 0..9, cada una con el contador de letras indicado, mediante una secuencia escalonada de 0.25 s dentro del trigger.
- **[TRIGGER_3] — 00:53–01:16:** Copiar cada residuo 0..9 hacia su fila 10..19 añadiendo ficha de 10 y una letra al contador. Completar las diez filas y destacar r=17 con cinco fichas explícitas, preservando 20 como caso separado.
- **[TRIGGER_4] — 01:16–01:39:** Mostrar temporalmente 10+4+4+1+1+1=21 con borde de fuera del dominio; devolver esas fichas y no contarlas en ningún resultado. Encerrar las 21 filas/casos y máximo cinco, sin omitir residuos de la tabla.
- **[TRIGGER_5] — 01:39–02:01:** Retirar tabla tras un hold de lectura y mostrar tres presupuestos 2,5,5 como grupos de G; sumarlos a 12. Añadir rótulo cota superior y conectar al segmento G de la regla de longitud.

- **Duración orientativa de la escena:** 02:01. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Pesos G en ACCENT_INDIGO; contador de letras en TEXT_MAIN, r=17 activo terracota. Caso imposible de 21 en ACCENT_VINO; máximo cinco y n_G≤12 en ACCENT_MINT. Cero usa cero monedas, no una moneda de peso cero.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 29

## Nombre: La garantía: 401 es menor que 500

## Descripcion Breve: Se suman 288 letras de esqueleto, 101 C y 12 G.

## Objetivo Pedagogico: Concluir la cota analítica y distinguirla de una comprobación finita más ajustada.

## Voz en off:

> “[TRIGGER_1] Reunamos las tres piezas. El esqueleto usa como máximo doscientas ochenta y ocho letras. Las ces, ciento una. Las ges, doce. La longitud queda acotada por doscientas ochenta y ocho más ciento una más doce: cuatrocientas una. Menos que quinientas.
> [TRIGGER_2] Ahora sabemos por qué ciento cuarenta y cuatro pares es una elección válida para objetivos de hasta un millón. No lo tratamos como una constante que funcionó por casualidad. Los pesos grandes reducen las multiplicidades iniciales, y las diferencias entre pesos comprimen los residuos.
> [TRIGGER_3] La cota no dice que exista una salida de cuatrocientas una letras, ni que ésta sea la longitud mínima. Es un techo seguro. Si queremos una comprobación adicional, podemos revisar todos los objetivos de cero a un millón por separado: la familia C usa como máximo cien letras y la G como máximo diez. Eso da otro techo, doscientas ochenta y ocho más cien más diez: trescientas noventa y ocho.
> [TRIGGER_4] Esa auditoría finita sirve como control del dominio concreto. La demostración de cuatrocientas una ya basta por sí sola para el límite. Si aumentaran los objetivos o cambiáramos la reserva de pares, habría que revisar las cuentas: la garantía que acabamos de obtener corresponde a este dominio y a esta construcción.”

## Descripcion Visual Detallada:

## Objetos:

- Barra apilada proporcional a 500 con tramos 288,101,12 y espacio libre 99; ecuación L≤288+101+12=401<500.
- Panel secundario de auditoría unidimensional 0..10^6 para C y G, máximos de multiplicidad 100 y 10; cota L≤398, rotulada comprobación finita adicional.
- Tarjeta de alcance B=144,0≤G,C≤10^6, con aviso revisar si cambia el dominio.

## Layout y disposicion:

- Regla de capacidad desde x=-5.8 a 5.8 en y=1.0. Límites de segmentos en x=-5.8,0.8816,3.2248,3.5032,5.8 para 0,288,389,401,500 respectivamente.
- Etiquetas de segmentos centradas sobre cada tramo en y=1.75; el tramo G estrecho se rotula con una flecha hacia (4.1,2.2,0), para evitar un texto ilegible. Ecuación principal en y=-0.3.
- Auditoría secundaria en dos tarjetas x=-3.0,3.0,y=-1.55; cota 398 en y=-2.4 y alcance en y=-3.15.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear regla proporcional y llenar tramos en orden 288,101,12 con sus valores. Escribir suma y marcar posición 401; señalar espacio libre 99 y límite 500. La escala es de longitud, no de apariciones.
- **[TRIGGER_2] — 00:19–00:40:** Conectar B=144 con las tres pruebas anteriores mediante tres pequeñas flechas. Mostrar fórmula de pesos y diferencias como rótulos breves del argumento; mantener 401 en primer plano.
- **[TRIGGER_3] — 00:40–01:11:** Crear panel adicional de dos ejes independientes de objetivos; rótulos 100 y 10 se identifican como máximos de número de letras, no máximos de patrones. Escribir 288+100+10=398 como cota adicional. No afirmar que todos los pares del cuadrado 10^6×10^6 fueron enumerados ni que 398 es una longitud máxima alcanzada.
- **[TRIGGER_4] — 01:11–01:35:** Atenuar auditoría secundaria, conservar garantía analítica y encerrar dominio/B. Añadir flecha de dependencia hacia prueba de longitud: cambiar parámetros exige recalcular. Retirar barra después de un hold y preparar los casos de frontera.

- **Duración orientativa de la escena:** 01:35. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Esqueleto terracota, segmento C cian y G índigo; área libre sin relleno en TEXT_MUTED. Garantía 401<500 verde. Auditoría finita en un panel secundario de menor contraste, sin presentarla como prueba indispensable.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 30

## Nombre: Los ceros y las fronteras también forman parte de la solución

## Descripcion Breve: Se resuelven la salida vacía, los objetivos individuales y el peso cero de G.

## Objetivo Pedagogico: Cubrir los casos borde y las precauciones de interpretación sin mostrar código.

## Voz en off:

> “[TRIGGER_1] Si ambos objetivos son cero, el recorrido no inserta ninguna letra y omite todos los pares. Eso dejaría una cadena vacía, que no está permitida. Devolvemos CA. Tiene dos letras, no tiene T y tampoco G: por tanto no contiene CAT ni GATA. Cero, cero, con una respuesta válida y no vacía.
> [TRIGGER_2] Si sólo pedimos cinco GATA y cero CAT, la construcción produce GATGATAT. Tiene una G que aporta cuatro y otra que aporta uno, y no tiene C. Si pedimos cero GATA y ocho CAT, produce CATATCCAT: una C aporta seis y las dos últimas uno cada una; no tiene G. Ambos casos reutilizan las mismas reglas.
> [TRIGGER_3] En el último hueco, V uno vale cero. La estación G queda deshabilitada: no dividimos ni repetimos restas con ese peso. Y al leer una solicitud recordamos el orden: primero GATA, después CAT. En el ejemplo cinco, ocho, intercambiarlo cambiaría el problema que estamos resolviendo.
> [TRIGGER_4] Las fórmulas son enteras. Si ampliáramos los índices, sus productos intermedios podrían crecer; conviene usar una aritmética con capacidad suficiente, no decimales que redondeen. Y tampoco debemos construir por separado una respuesta CAT y otra GATA y pegarlas sin analizar los cruces: nuestra independencia depende de compartir el esqueleto y clasificar por la letra inicial.”

## Descripcion Visual Detallada:

## Objetos:

- Tarjetas de casos (G,C)=(0,0)→CA; (5,0)→GATGATAT; (0,8)→CATATCCAT; conteos exactos y longitudes 2,8,9.
- Guardia i≥2 ante estación G; bandeja de entrada con ranuras G,C; tarjeta de productos enteros y flecha de concatenación con rutas cruzadas.
- Nota de producción: la fuente recomienda enteros de 64 bits al generalizar. No convertir esta cautela en un bloque de sintaxis C++ ni atribuir desbordamiento a los valores actuales.

## Layout y disposicion:

- Tres tarjetas de casos en filas y=1.8,0.25,-1.3, ancho 11.8; objetivo en x=-4.3, cadena en x=0.4 y resultado en x=4.6. La cadena de nueve letras usa fichas de ancho 0.43 y paso 0.48.
- Para guardias, retirar tarjetas y crear estación G en (-3.3,0.8,0), bandeja (G,C) en (3.3,0.8,0), productos en (-3.3,-1.5,0) y concatenación en (3.3,-1.5,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear primer caso; mostrar salida vacía provisional con L=0 y condición no cumplida. Sustituir por CA; comprobar ausencia de T y G con proyección de letras y marcar conteos cero, longitud dos.
- **[TRIGGER_2] — 00:24–00:50:** Crear segundo caso y marcar sus G en posiciones 1 y 4 con sufijos de 3 y 2 pares; escribir 4+1=5 y C ausente. Crear tercer caso y marcar C con sufijos 3,1,1, escribir 6+1+1=8 y G ausente. Todas las cadenas se escriben completas.
- **[TRIGGER_3] — 00:50–01:11:** Retirar casos, crear estación G cerrada cuando i=1 y bandeja rotulada primero G, después C. Enviar fichas numéricas 5 y 8 a las ranuras correctas; mostrar el intercambio sólo como ejemplo de lectura incorrecta, sin emitir otra respuesta.
- **[TRIGGER_4] — 01:11–01:36:** Crear productos exactos sin decimales y tarjeta capacidad entera. Recordar la concatenación con dos grupos de letras y un arco que cruza la frontera; conectar al argumento de independencia ya demostrado. No presentar utilidades de plantilla ni comentarios erróneos del código como parte del algoritmo.

- **Duración orientativa de la escena:** 01:36. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Casos válidos y ceros finales en ACCENT_MINT; salida vacía inválida y lectura invertida en ACCENT_VINO. Guardia G índigo, productos terracota. No marcar ausencia de C o G como fracaso.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 31

## Nombre: El trabajo sigue a la salida, no al millón

## Descripcion Breve: Preprocesar cuesta O(B), y cada solicitud cuesta O(B+L).

## Objetivo Pedagogico: Justificar el costo de los recorridos y las repeticiones con una contabilidad de acciones.

## Voz en off:

> “[TRIGGER_1] ¿Cuánto trabajo hace el algoritmo? Primero calcula las dos tablas de pesos hasta B, que aquí vale ciento cuarenta y cuatro. Cada índice requiere una cantidad fija de operaciones: el preprocesamiento cuesta orden de B y se hace una sola vez para todas las solicitudes.
> [TRIGGER_2] Por solicitud recorremos B huecos. Esa parte cuesta orden de B. Dentro de un hueco puede parecer que hay una repetición peligrosa: imprimir muchas ces o ges. Pero cada vuelta escribe una letra real de la respuesta. El total de esas vueltas queda cargado a su longitud L, igual que escribir los pares AT.
> [TRIGGER_3] Así, el costo de un caso es orden de B más L. Un objetivo de un millón no implica un millón de pasos: cada letra de peso grande puede representar miles de apariciones. Si agrupamos las letras de un hueco mediante cocientes, la representación se vuelve explícita, pero escribir la salida sigue costando proporcionalmente a su longitud.
> [TRIGGER_4] Para Q solicitudes, sumamos el preprocesamiento B, el recorrido Q por B y las longitudes de todas las respuestas. Orden de B más Q por B más la suma de L sub q. Sólo escribir esas respuestas ya requiere al menos un trabajo proporcional a esa suma. No hemos probado que las respuestas sean las más cortas; hemos acotado el trabajo de esta construcción.”

## Descripcion Visual Detallada:

## Objetos:

- Dos tablas de B casillas representadas por extremos y brace B; reloj de preprocesamiento único.
- Carril de B huecos y otro carril con las 11 letras de la traza; ficha de costo por hueco y por letra; MathTex O(B),O(B+L),O(B+QB+ΣL_q),Ω(ΣL_q).
- Diagrama de bloque de multiplicidad que se expande en caracteres reales, sin código fuente.

## Layout y disposicion:

- Tablas centradas en x=-3.0 y 3.0,y=1.3. Carril huecos de x=-5.7..5.7,y=0.1; carril salida con 11 casillas en y=-1.1.
- Ecuación de un caso en y=-2.15 y total en y=-3.05. Para cuatro términos largos, separar el total en dos MathTex alineados en x=0, sin disminuir de 28 pt.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear tablas con dos operaciones por índice representadas por flechas de recurrencia. Encerrar reloj único y escribir O(B); el reloj no se duplica por solicitud.
- **[TRIGGER_2] — 00:21–00:46:** Crear carril de huecos, cursor y brace B. Cada hueco recibe una ficha de gasto fijo. Crear carril de salida y añadir una ficha de gasto por cada letra emitida de CGATGATCCAT; no cobrar un millón de fichas por sus apariciones.
- **[TRIGGER_3] — 00:46–01:12:** Agrupar fichas fijas y de salida para escribir O(B+L). Mostrar un grupo de n_C letras como multiplicidad que debe expandirse al escribir; relacionar el costo con número de caracteres, no con valor del contador.
- **[TRIGGER_4] — 01:12–01:41:** Crear Q tarjetas de solicitudes mediante brace simbólica y sumar tiempos con límites completos Σ_{q=1}^Q L_q. Escribir costo total y cota inferior de escritura, manteniendo ambos rótulos distintos. Retirar relojes para examinar memoria.

- **Duración orientativa de la escena:** 01:41. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Recorrido y tablas índigo, costo de salida cian. L activo terracota, complejidades en TEXT_MAIN y garantía proporcional en verde. O(L) no se colorea como ineficiencia: es el trabajo necesario para producir letras.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 32

## Nombre: Guardar sólo lo que necesitamos

## Descripcion Breve: Las tablas ocupan O(B); emitir directamente o guardar la cadena cambia la memoria adicional.

## Objetivo Pedagogico: Distinguir memoria persistente, estado por caso y búfer de respuesta.

## Voz en off:

> “[TRIGGER_1] La memoria principal son las dos tablas de pesos: orden de B. Durante una solicitud sólo necesitamos los dos residuos, el índice del hueco y el estado de inicio, además de las cantidades que se insertan. Es un número fijo de valores.
> [TRIGGER_2] La implementación original puede escribir cada letra directamente a la salida. En ese esquema usa memoria adicional constante por caso: no necesita guardar la cadena completa. Las tablas siguen ocupando orden de B y se comparten entre solicitudes.
> [TRIGGER_3] Si preferimos comprobar la longitud o verificar la respuesta antes de imprimirla, guardamos la cadena en un búfer. Ese búfer ocupa orden de L. Entonces la memoria total es orden de B más L. Son dos modos de producir la misma construcción, no dos algoritmos matemáticos distintos.
> [TRIGGER_4] Y verificar no necesita enumerar todos los triples y cuádruples de posiciones. Podemos contar las apariciones con unos pocos acumuladores, leyendo la cadena una sola vez. Nos dará una comprobación independiente de la representación por pesos. Vamos a visualizar esos acumuladores, sin enseñar un bloque de código.”

## Descripcion Visual Detallada:

## Objetos:

- Dos bancos de memoria T,V con brace B; registro por caso de r_C,r_G,i,iniciada,a_i,b_i; flecha directa a salida.
- Modo alternativo con búfer de L casillas y verificador de dos patrones; fórmulas memoria extra O(1) o O(L), total O(B) u O(B+L).

## Layout y disposicion:

- Bancos de memoria en (-3.3,1.35,0) y (3.3,1.35,0); registro de seis campos en (0,-0.2,0), ancho 10.8.
- Salida directa en (-3.1,-1.85,0), búfer en (3.1,-1.85,0); verificador debajo del búfer en y=-2.8. Fórmula superior se coloca en (0,2.55,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear bancos de pesos y seis registros rotulados, no líneas de código. Mostrar que sólo un caso ocupa el registro y que el siguiente lo reinicia sin copiar las tablas.
- **[TRIGGER_2] — 00:20–00:38:** Conectar registros con una tubería de salida directa; las letras emitidas desaparecen del almacenamiento de trabajo. Escribir total O(B) y extra O(1) por caso, con rótulos precisos.
- **[TRIGGER_3] — 00:38–01:00:** Crear segundo carril como alternativa explícita, introducir búfer y conservar L fichas allí antes de salida. Escribir total O(B+L), extra O(L); evitar dibujar ambos modos como si el original los ejecutara a la vez.
- **[TRIGGER_4] — 01:00–01:22:** Conectar búfer al verificador y crear sus dos bancos pequeños de acumuladores. Retirar modo directo y tablas, conservando sólo la cadena de 11 letras y esos bancos para la escena siguiente.

- **Duración orientativa de la escena:** 01:22. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Tablas y bancos en ACCENT_INDIGO; tuberías cian; memoria por caso con borde TEXT_MUTED; cadena con colores de letras. Ambas opciones válidas sin usar rojo para guardar O(L).
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 33

## Nombre: Un verificador que cuenta sin enumerar

## Descripcion Breve: Acumuladores de prefijos cuentan CAT y GATA al procesar las once letras.

## Objetivo Pedagogico: Mostrar una verificación independiente, completa, con actualizaciones desde el patrón largo al corto.

## Voz en off:

> “[TRIGGER_1] Para verificar CAT, guardamos cuántas formas hay de escribir el prefijo vacío, C, CA y CAT con las letras leídas. Para GATA guardamos vacío, G, GA, GAT y GATA. El vacío empieza con una forma, y todos los demás acumuladores con cero.
> [TRIGGER_2] Cada nueva letra prolonga las coincidencias anteriores que puede completar. Una C añade el contador del vacío al de C. Una A añade C a CA; una T añade CA a CAT. En GATA, una G añade vacío a G; una T añade GA a GAT; y una A puede añadir GAT a GATA y G a GA. Recorremos los estados de mayor a menor longitud para que cada suma use información anterior a la nueva letra.
> [TRIGGER_3] Leamos el comienzo CGAT. La C crea un prefijo C. La G crea un prefijo G. La A crea un CA y un GA. La T completa un CAT y un GAT. Después llega otra G: ya hay dos prefijos G. La siguiente A aumenta CA de uno a dos, completa el primer GATA y aumenta GA de uno a tres.
> [TRIGGER_4] La T de la posición siete añade esos dos CA al contador CAT, que pasa de uno a tres, y esos tres GA al contador GAT, que pasa de uno a cuatro. Las ces de ocho y nueve elevan C de uno a dos y luego a tres; no cambian los acumuladores de GATA.
> [TRIGGER_5] La A de la posición diez añade tres a CA, que pasa de dos a cinco; añade los cuatro GAT al total GATA, que pasa de uno a cinco; y añade los dos G a GA, que pasa de tres a cinco. La T final añade los cinco CA a CAT: tres más cinco, ocho. También eleva GAT de cuatro a nueve, pero no hay otra A después. GATA permanece en cinco.
> [TRIGGER_6] Una lectura, ocho CAT y cinco GATA. Cada acumulador tiene una interpretación por posiciones: guardamos elecciones anteriores y las extendemos con la posición nueva, sin consumirlas. Para patrones de longitud fija, el verificador cuesta orden de L y memoria constante. Comprobamos además el alfabeto y que la longitud esté entre uno y quinientos.”

## Descripcion Visual Detallada:

## Objetos:

- Fila completa CGATGATCCAT con cursor; bancos CAT rotulados ∅,C,CA,CAT y GATA rotulados ∅,G,GA,GAT,GATA; iniciales (1,0,0,0) y (1,0,0,0,0).
- Tabla de estados completos por posición, CAT: 1:C→(1,1,0,0); 2:G→(1,1,0,0); 3:A→(1,1,1,0); 4:T→(1,1,1,1); 5:G→(1,1,1,1); 6:A→(1,1,2,1); 7:T→(1,1,2,3); 8:C→(1,2,2,3); 9:C→(1,3,2,3); 10:A→(1,3,5,3); 11:T→(1,3,5,8).
- Tabla de estados completos por posición, GATA: 1:C→(1,0,0,0,0); 2:G→(1,1,0,0,0); 3:A→(1,1,1,0,0); 4:T→(1,1,1,1,0); 5:G→(1,2,1,1,0); 6:A→(1,2,3,1,1); 7:T→(1,2,3,4,1); 8:C→(1,2,3,4,1); 9:C→(1,2,3,4,1); 10:A→(1,2,5,4,5); 11:T→(1,2,5,9,5).
- Actualización genérica MathTex w_{j+1}←w_{j+1}+w_j si p_j=x, recorriendo j=k−1 hasta 0. Representarla por transferencias de fichas y etiquetas, no como un listado de instrucciones.
- Nota de rigor: no afirmar que un recorrido ascendente necesariamente falla para estos dos patrones. Ninguno tiene letras idénticas adyacentes. El recorrido descendente es una regla general segura; las dos A de GATA cumplen papeles distintos y deben visualizarse como dos transiciones independientes.

## Layout y disposicion:

- Cadena en x=-5.5+1.1k,y=2.05, índice y=1.5. Banco CAT: cuatro registros en x=-4.5,-1.5,1.5,4.5,y=0.25; banco GATA: cinco registros en x=-4.8,-2.4,0,2.4,4.8,y=-1.5.
- Etiqueta de lectura descendente junto a cada banco en y=0.95 y -0.8; total verificado en y=-2.8. No mostrar simultáneamente toda la tabla de 11 filas: el estado completo de ambos bancos aparece tras cada posición y se guarda en tarjetas de historial accesibles en el storyboard.
- Transferencias por debajo de cada banco, altura máxima 0.35; cursor de patrón recorre de derecha a izquierda. El cursor de cadena recorre de izquierda a derecha. Sus rótulos los distinguen explícitamente.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear fila y dos bancos; escribir una forma para ∅ y cero para los demás. Cada registro muestra patrón parcial y número en objetos separados. Mantener cursor de cadena antes de la posición uno.
- **[TRIGGER_2] — 00:20–00:54:** Demostrar las cinco clases de actualización con fichas copiadas del origen al destino. En A para GATA recorrer primero GAT→GATA y después G→GA. Mostrar fórmula genérica pequeña y dirección descendente; no reutilizar la misma ficha de posición como dos letras de una única elección.
- **[TRIGGER_3] — 00:54–01:22:** Procesar posiciones 1,2,3,4,5,6 con estados exactos de las tablas: en C_1 cambia C; en G_2 cambia G; en A_3 cambian CA y GA; en T_4 cambian CAT y GAT; en G_5 cambia G a 2; en A_6 actualizar primero GATA 0→1, después GA 1→3, y CA 1→2. Tras cada posición hacer hold de al menos 0.5 s, y resaltar sólo registros modificados.
- **[TRIGGER_4] — 01:22–01:47:** Procesar T_7: CAT 1→3 y GAT 1→4. Procesar C_8 y C_9 por separado: C 1→2→3. Mostrar ambos bancos completos después de cada paso y mantener GATA en uno; ningún registro cambia por una letra que no coincide con su transición.
- **[TRIGGER_5] — 01:47–02:19:** Procesar A_10: GATA 1→5, GA 3→5 y CA 2→5; sus sumas usan los estados anteriores a esa A. Procesar T_11: CAT 3→8 y GAT 4→9. Mostrar bancos finales (1,3,5,8) y (1,2,5,9,5); encerrar sólo estados completos CAT=8,GATA=5, sin confundir GAT=9 con GATA.
- **[TRIGGER_6] — 02:19–02:43:** Crear tres sellos de control: letras∈{C,G,A,T}, 1≤L=11≤500, objetivos exactos (G,C)=(5,8). Escribir O(L) para la lectura y O(1) para acumuladores de patrones fijos; la cadena guardada, si existe, mantiene su memoria O(L). Retirar bancos para el cierre narrativo.

- **Duración orientativa de la escena:** 02:43. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Banco CAT cian y GATA índigo; posición nueva terracota y destino actualizado verde. Prefijo vacío con TEXT_MUTED; patrones incompletos en TEXT_MAIN, resultados finales en ACCENT_MINT. Nueve GAT no se presenta como error.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---

## Escena: 34

## Nombre: Diseñar el espacio donde la dificultad desaparece

## Descripcion Breve: El cierre vuelve al misterio inicial y deja una pregunta transferible.

## Objetivo Pedagogico: Condensar el aprendizaje después de completar todas las pruebas, sin añadir una explicación pendiente.

## Voz en off:

> “[TRIGGER_1] Al principio parecía que necesitábamos escribir un millón de copias de una palabra. Pero una aparición es una elección de posiciones. Un esqueleto alternante puede alojar muchas de esas elecciones, y una sola letra inicial puede activarlas todas.
> [TRIGGER_2] Descubrimos dos pesos: un triángulo para C y una elección de tres elementos para G. Clasificamos las apariciones por su primera letra, y eso separó los objetivos sin separarlos en dos cadenas. Después representamos los números con esos pesos y cumplimos cada promesa de sufijo.
> [TRIGGER_3] El ejemplo quedó en once letras, con ocho CAT y cinco GATA. Para cualquier solicitud del dominio, las cotas de residuos garantizan una respuesta de como máximo cuatrocientas una letras; y para cero, cero, una respuesta no vacía tan simple como CA. Cada requisito tiene ahora su argumento.
> [TRIGGER_4] La pregunta que podemos llevarnos es ésta: cuando varias condiciones parecen interferir, ¿puedo elegir una estructura donde cada decisión tenga una contribución exacta y controlable? [Pausa.] A veces la solución no aparece buscando más rápido entre todas las posibilidades. Aparece diseñando las posibilidades que merece la pena construir.”

## Descripcion Visual Detallada:

## Objetos:

- Cadena final de 11 letras, contadores CAT=8,GATA=5; tarjetas T_i=binom(i+1,2),V_i=binom(i+1,3); regla corta 401<500.
- Pregunta final en Tex, dividida en tres líneas; crédito GATA-CAT · ICPC Latin America Championship 2026 · Problema de Humberto Díaz Suárez, Puerto Rico.
- Nota de créditos: datos tomados del contexto documentado en guion_sol.md; no atribuir el desarrollo de estas demostraciones a un editorial oficial, pues el archivo fuente señala que fueron reconstruidas a partir del enunciado y el código.

## Layout y disposicion:

- Cadena en y=1.1, índices retirados, mismas x=-5.5+1.1k. Contadores en (-3.0,-0.1,0) y (3.0,-0.1,0). Tarjetas de pesos en y=-1.35, centros x=-3.1,3.1.
- Garantía en (0,-2.4,0); pregunta final sustituye todo y ocupa área x=-5.8..5.8,y=-0.6..1.0 con texto de 34 pt. Crédito en (0,-3.25,0), 20–22 pt, sin solapamientos.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:18:** Recuperar cadena y mostrar una breve ruta CAT y otra GATA ya verificadas; ponerlas dentro de dos marcos de elecciones, sin añadir nuevas apariciones al contador.
- **[TRIGGER_2] — 00:18–00:39:** Crear tarjetas de los dos pesos y conectarlas a C/G de la cadena. Iluminar el esqueleto A/T compartido y después las contribuciones asignadas; no abrir un tema matemático nuevo.
- **[TRIGGER_3] — 00:39–01:01:** Mostrar contadores finales, L=11 y garantía 401<500 como dos hechos diferentes: ejemplo y cota universal. Introducir una pequeña ficha CA para el caso cero y retirarla al acabar la frase.
- **[TRIGGER_4] — 01:01–01:24:** Desvanecer cadena, pesos y cotas; escribir únicamente la pregunta transferible. Mantener pausa de 1.5 s y, tras la última frase, hold de 2 s. Añadir crédito y FadeOut suave a BG_COLOR. No insertar fórmulas o instrucciones después del cierre.

- **Duración orientativa de la escena:** 01:24. Ventanas locales estimadas; la grabación definitiva fija los holds.

## Código Cromático y Estilo:

- Cierre en TEXT_MAIN, palabra contribución con acento terracota; contadores válidos verde y pesos cian/índigo. Crédito en TEXT_MUTED. Sin música ni assets externos necesarios para comprender el argumento.
- Fondo BG_COLOR; rótulos con Tex/MathTex. Respetar las convenciones globales de tamaño, contraste, identidad de posiciones y sincronización.

---
