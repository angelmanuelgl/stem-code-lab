# 42 sugerencias de problemas para la serie

Guía breve para revisar poco a poco los **42 problemas con encaje fuerte provisional** del [análisis del historial](/Users/amgl/stem-code-lab/serie-icpc-problems/analisis_historial_problemas.md).

Los enunciados son **resúmenes en español**, no transcripciones completas. Consulta el enlace del problema para restricciones, ejemplos y detalles. Las soluciones describen la idea central, sin desarrollar todas las pruebas.

Se mantienen dos salvedades: **K Subsequences** tiene autoría personal por confirmar; **Booksort** y **Fun with Balls** se contrastaron con código de referencia del jurado, no con un editorial explicativo. No se incluyen los 32 problemas cuya fuente de solución sigue pendiente.

## Índice

1. [Frangolino ali na mesa](#problema-1)
2. [Investigating Quadradômeda](#problema-2)
3. [Knockout, swiss and other kinds of tournaments](#problema-3)
4. [Fast XORting](#problema-4)
5. [Jackpot](#problema-5)
6. [K Subsequences](#problema-6)
7. [Bottle Flip](#problema-7)
8. [Coin](#problema-8)
9. [Horizon Scanning](#problema-9)
10. [Dune Dash](#problema-10)
11. [Around the Table](#problema-11)
12. [Congklak](#problema-12)
13. [Demand for Cycling](#problema-13)
14. [Jumbled Packets](#problema-14)
15. [Mex Hex](#problema-15)
16. [If I Could Turn Back Time](#problema-16)
17. [Just Half is Enough](#problema-17)
18. [Keyboard Chaos](#problema-18)
19. [Foreign Postcards](#problema-19)
20. [Prime Topology](#problema-20)
21. [Tic-Tac-Toe on a Graph](#problema-21)
22. [Trace of Product of Sparse Square Matrices](#problema-22)
23. [Dreamcatcher](#problema-23)
24. [Erratic Lights](#problema-24)
25. [Juggling Keys](#problema-25)
26. [Booksort](#problema-26)
27. [Fun with Balls](#problema-27)
28. [Optimal Balancing Strategy](#problema-28)
29. [K.O. Kids](#problema-29)
30. [Lots of Land](#problema-30)
31. [Amusement Arcade](#problema-31)
32. [Grid Delivery](#problema-32)
33. [Hectic Harbour II](#problema-33)
34. [Monty's Hall](#problema-34)
35. [Adjusting Drones](#problema-35)
36. [Billion Players Game](#problema-36)
37. [Expansion Plan 2](#problema-37)
38. [Factory Table](#problema-38)
39. [Jewels Building](#problema-39)
40. [Crazy Decoder](#problema-40)
41. [The Scale Riddle](#problema-41)
42. [The Brega Game](#problema-42)

<a id="problema-1"></a>
## 1. Frangolino ali na mesa

**Concurso:** Brasil 2025 · primera fase / GP México, tercera fecha · problema F.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106073/problem/F).

**Recursos:** [Editorial, apartado F](https://scorelatam.naquadah.com.br/subbr-2025/editorial.pdf) · [Enunciados](https://codeforces.com/gym/106073/attachments/download/33160/statements-en.pdf).

**Enunciado:** Un robot confunde aleatoriamente las órdenes de cambiar de mesa y registrar pedidos. Calcula cuántas milanesas se esperan en cada mesa.

**Solución:** Recorre las instrucciones al revés y acumula la contribución esperada de los pedidos futuros. La probabilidad de conservar la mesa actual introduce factores de un medio. Así evitas mantener una distribución completa sobre todas las posiciones del robot.

<a id="problema-2"></a>
## 2. Investigating Quadradômeda

**Concurso:** Brasil 2025 · primera fase / GP México, tercera fecha · problema I.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106073/problem/I).

**Recursos:** [Editorial, apartado I](https://scorelatam.naquadah.com.br/subbr-2025/editorial.pdf) · [Enunciados](https://codeforces.com/gym/106073/attachments/download/33160/statements-en.pdf).

**Enunciado:** Elige órbitas circulares de radio entero positivo alrededor de una secuencia de estrellas. Las órbitas consecutivas deben tocarse; maximiza el primer radio.

**Solución:** Si la distancia entre estrellas es dᵢ, entonces Rᵢ₊₁=dᵢ−Rᵢ. Cada radio queda expresado como ±R₁ más una constante. Convierte la positividad de todos los radios en restricciones sobre R₁, intersecta sus intervalos y toma el mayor entero factible.

<a id="problema-3"></a>
## 3. Knockout, swiss and other kinds of tournaments

**Concurso:** Brasil 2025 · primera fase / GP México, tercera fecha · problema K.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106073/problem/K).

**Recursos:** [Editorial, apartado K](https://scorelatam.naquadah.com.br/subbr-2025/editorial.pdf) · [Enunciados](https://codeforces.com/gym/106073/attachments/download/33160/statements-en.pdf).

**Enunciado:** En un torneo, se enfrentan jugadores con el mismo número de victorias y derrotas hasta alcanzar A victorias o B derrotas. Determina el mínimo tamaño inicial viable.

**Solución:** Cuenta cuántos jugadores llegan a cada marcador mediante coeficientes binomiales. Todos los grupos que aún deben jugar necesitan tamaño par. Traduce esas exigencias a valuaciones en base dos; las identidades con conteos de bits permiten encontrar la potencia de dos necesaria. El editorial justifica cómo acotar la búsqueda restante.

<a id="problema-4"></a>
## 4. Fast XORting

**Concurso:** SEERC 2023 · problema F.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105465/problem/F).

**Recursos:** [Editorial, apartado F](https://codeforces.com/gym/105465/attachments/download/27986/tutorials-seerc-2023.pdf) · [Enunciados](https://codeforces.com/gym/105465/attachments/download/27988/statements-seerc-2023.pdf).

**Enunciado:** Ordena una permutación usando intercambios adyacentes y operaciones que aplican el mismo XOR a todos sus valores, con el menor número de operaciones.

**Solución:** Todos los XOR pueden agruparse en uno. Después, el costo de ordenar es el número de inversiones. El orden de cada pareja depende de su bit distinto más significativo, de modo que cada bit de la máscara se optimiza por separado. Compara también con no aplicar XOR.

<a id="problema-5"></a>
## 5. Jackpot

**Concurso:** SEERC 2023 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105465/problem/J).

**Recursos:** [Editorial, apartado J](https://codeforces.com/gym/105465/attachments/download/27986/tutorials-seerc-2023.pdf) · [Enunciados](https://codeforces.com/gym/105465/attachments/download/27988/statements-seerc-2023.pdf).

**Enunciado:** Elimina parejas de elementos adyacentes y suma sus diferencias absolutas. Busca la máxima puntuación al vaciar el arreglo.

**Solución:** Una cota superior es la suma de la mitad mayor menos la de la mitad menor. Colorea los elementos según su mitad: mientras queden, existe una pareja adyacente de colores distintos. Eliminarla mantiene el equilibrio, por lo que la cota siempre se alcanza.

<a id="problema-6"></a>
## 6. K Subsequences

**Concurso:** SEERC 2023 · problema K.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105465/problem/K).

**Recursos:** [Editorial, apartado K](https://codeforces.com/gym/105465/attachments/download/27986/tutorials-seerc-2023.pdf) · [Enunciados](https://codeforces.com/gym/105465/attachments/download/27988/statements-seerc-2023.pdf).

**Nota:** El CSV indica «ayudar»; sigue pendiente confirmar si tu aporte fue la idea principal.

**Enunciado:** Divide una secuencia de +1 y −1 en k subsecuencias. Minimiza la mayor suma de subsegmento que aparezca dentro de cualquiera de ellas.

**Solución:** Mantén la máxima suma de sufijo de cada subsecuencia. Asigna cada +1 a una con valor mínimo y cada −1 a una con valor máximo. El invariante de equilibrio permite alcanzar ceil(M/k), donde M es la máxima suma de subsegmento de la secuencia original.

<a id="problema-7"></a>
## 7. Bottle Flip

**Concurso:** NWERC 2022 · problema B.

**Enlace:** [Abrir problema](https://codeforces.com/gym/104875/problem/B).

**Recursos:** [Editorial, apartado B](https://chipcie.wisv.ch/archive/2022/nwerc/solutions.pdf) · [Enunciados](https://2022.nwerc.eu/main/problem-set.pdf).

**Enunciado:** Decide cuánta agua poner en una botella cilíndrica para minimizar su centro de masa, considerando las densidades del agua y del aire.

**Solución:** Escribe el centro de masa como promedio ponderado de ambas regiones. El radio se cancela y solo queda una función de la altura del agua. Minimízala mediante derivación o búsqueda ternaria; lo esencial es construir correctamente el modelo físico.

<a id="problema-8"></a>
## 8. Coin

**Concurso:** Kunming 2024 · problema C.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105588/problem/C).

**Recursos:** [Editorial, apartado C](https://codeforces.com/gym/105588/attachments/download/28803/tutorial.pdf) · [Enunciados](https://codeforces.com/gym/105588/attachments/download/28813/1-statement-english.pdf).

**Enunciado:** Se eliminan repetidamente los piratas en posiciones 1, 1+k, 1+2k… de una fila. Encuentra la posición inicial del único superviviente.

**Solución:** Analiza cómo cambia el índice de un superviviente al deshacer una ronda: x pasa a x+ceil(x/(k−1)). La cantidad de piratas también tiene una recurrencia simple. Agrupa tramos donde los cocientes permanecen constantes para saltar muchas rondas, en vez de simularlas una a una.

<a id="problema-9"></a>
## 9. Horizon Scanning

**Concurso:** Kunming 2024 · problema H.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105588/problem/H).

**Recursos:** [Editorial, apartado H](https://codeforces.com/gym/105588/attachments/download/28803/tutorial.pdf) · [Enunciados](https://codeforces.com/gym/105588/attachments/download/28813/1-statement-english.pdf).

**Enunciado:** Un radar situado en el origen debe detectar al menos k islas, cualquiera que sea su orientación. Encuentra la mínima apertura angular necesaria.

**Solución:** Ordena los ángulos y duplica la secuencia sumando una vuelta. La apertura mínima queda determinada por la mayor separación cíclica entre ángulos distantes k posiciones: ese intervalo describe dónde podría orientarse el radar para detectar demasiado pocas islas.

<a id="problema-10"></a>
## 10. Dune Dash

**Concurso:** NCPC 2025 · problema D.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106124/problem/D).

**Recursos:** [Editorial, apartado D](https://codeforces.com/gym/106124/attachments/download/33916/ncpc25slides.pdf) · [Enunciados](https://codeforces.com/gym/106124/attachments/download/33915/ncpc2025problems_compressed.pdf).

**Enunciado:** Reconstruye la longitud de una ruta cuyos puntos están desordenados. Se garantiza una propiedad que hace a los extremos de cada terna los más separados.

**Solución:** Desde cualquier punto, uno de los más lejanos es un extremo de la ruta. Ordena todos los puntos por distancia a ese extremo y suma las distancias entre consecutivos. La propiedad dada garantiza que ese orden es el recorrido correcto.

<a id="problema-11"></a>
## 11. Around the Table

**Concurso:** GCPC 2025 · problema A.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106129/problem/A).

**Recursos:** [Editorial, apartado A](https://2025.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf).

**Enunciado:** Dos filas de jugadores intercambian golpes alrededor de una mesa durante un número enorme de turnos. Cuenta las parejas distintas que llegan a enfrentarse.

**Solución:** Representa a los jugadores mediante posiciones cíclicas. Solo unas pocas diferencias modulares pueden producir enfrentamientos. Cuenta esas clases y corrige las coincidencias entre ellas, sin simular el juego.

<a id="problema-12"></a>
## 12. Congklak

**Concurso:** GCPC 2025 · problema C.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106129/problem/C).

**Recursos:** [Editorial, apartado C](https://2025.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf).

**Enunciado:** Un juego redistribuye piedras entre hoyos mediante reglas de siembra y recogida. Calcula la configuración tras muchísimas partidas.

**Solución:** Observa un contador binario en los hoyos alternos; los restantes acumulan los acarreos. Procesa sus efectos por bloques y propaga cuántas partidas alcanzan los siguientes hoyos.

<a id="problema-13"></a>
## 13. Demand for Cycling

**Concurso:** GCPC 2025 · problema D.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106129/problem/D).

**Recursos:** [Editorial, apartado D](https://2025.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf).

**Enunciado:** Rodea una ciudad con una ciclovía de segmentos horizontales y verticales, de longitud total mínima.

**Solución:** Todo recorrido debe cubrir dos veces la amplitud horizontal y dos veces la vertical. El rectángulo envolvente alcanza esa cota; basta conocer las coordenadas extremas.

<a id="problema-14"></a>
## 14. Jumbled Packets

**Concurso:** GCPC 2025 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106129/problem/J).

**Recursos:** [Editorial, apartado J](https://2025.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf).

**Enunciado:** Codifica una cadena binaria en una ternaria de igual longitud, de modo que pueda recuperarse aunque llegue con una rotación circular desconocida.

**Solución:** Usa el tercer símbolo para marcar los ceros iniciales y el primer uno. Ese bloque identifica el comienzo tras la rotación y permite restaurar los bits originales. Trata aparte la cadena de puros ceros.

<a id="problema-15"></a>
## 15. Mex Hex

**Concurso:** GCPC 2025 · problema M.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106129/problem/M).

**Recursos:** [Editorial, apartado M](https://2025.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf).

**Enunciado:** Un escudo bloquea d ataques y luego necesita d ataques de recarga. Minimiza el mex de los valores de los ataques recibidos.

**Solución:** Para conseguir mex x, basta bloquear todas sus apariciones. Estudia cada valor por separado y coloca los intervalos de protección con un greedy que preserve espacio para los siguientes. Elige el menor valor factible.

<a id="problema-16"></a>
## 16. If I Could Turn Back Time

**Concurso:** Northwestern Russia Regional 2024 · problema I.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105537/problem/I).

**Recursos:** [Editorial, apartado I](https://codeforces.com/gym/105537/attachments/download/38889/tutorial.pdf) · [Enunciados](https://codeforces.com/gym/105537/attachments/download/28362/statements.pdf).

**Enunciado:** Cada año, todas las montañas que alcanzan cierto umbral pierden una unidad de altura. Decide si unas alturas antiguas pueden producir las actuales y en cuántos años como mínimo.

**Solución:** Ordena por altura actual, resolviendo empates con la antigua. Las alturas antiguas y las pérdidas deben respetar las monotonías del proceso, y ninguna pérdida puede ser negativa. Si se cumplen las condiciones, una construcción por umbrales alcanza el máximo de las pérdidas como número de años.

<a id="problema-17"></a>
## 17. Just Half is Enough

**Concurso:** Northwestern Russia Regional 2024 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105537/problem/J).

**Recursos:** [Editorial, apartado J](https://codeforces.com/gym/105537/attachments/download/38889/tutorial.pdf) · [Enunciados](https://codeforces.com/gym/105537/attachments/download/28362/statements.pdf).

**Enunciado:** Construye un orden de vértices que respete la dirección de al menos la mitad de las aristas, aunque el grafo tenga ciclos.

**Solución:** Toma cualquier orden y su reverso. Cada arista se respeta en exactamente uno de los dos. Cuenta las aristas respetadas y devuelve el mejor: necesariamente alcanza al menos la mitad.

<a id="problema-18"></a>
## 18. Keyboard Chaos

**Concurso:** Northwestern Russia Regional 2024 · problema K.

**Enlace:** [Abrir problema](https://codeforces.com/gym/105537/problem/K).

**Recursos:** [Editorial, apartado K](https://codeforces.com/gym/105537/attachments/download/38889/tutorial.pdf) · [Enunciados](https://codeforces.com/gym/105537/attachments/download/28362/statements.pdf).

**Enunciado:** Cada tecla recorre cíclicamente una cadena de letras. Encuentra la cadena más corta que no se puede escribir, o determina que todas son escribibles.

**Solución:** Demuestra que basta buscar una cadena formada por una sola letra. Para cada letra, suma los prefijos iniciales que las teclas pueden aportar antes de emitir otra. Una repetición adicional es imposible, salvo que exista una tecla compuesta exclusivamente de esa letra. Escoge la mejor opción.

<a id="problema-19"></a>
## 19. Foreign Postcards

**Concurso:** NEERC 2016 · problema F.

**Enlace:** [Abrir problema](https://codeforces.com/gym/101190/problem/F).

**Recursos:** [Editorial, apartado F](https://neerc.ifmo.ru/archive/2016/neerc-2016-review.pdf) · [Enunciados](https://neerc.ifmo.ru/archive/2016/neerc-2016-statement.pdf).

**Enunciado:** Una pila de postales se divide aleatoriamente en bloques; cada bloque se voltea según la orientación de su primera postal. Calcula cuántas quedan mal orientadas en esperanza.

**Solución:** Define una esperanza por sufijo y condiciona por el tamaño del siguiente bloque. La recurrencia directa es cuadrática, pero puedes reordenar sus sumas y mantener acumulados por orientación. Eso permite calcular todos los estados en tiempo lineal.

<a id="problema-20"></a>
## 20. Prime Topology

**Concurso:** Manila 2025 · problema H.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106262/problem/H).

**Recursos:** [Editorial, apartado H](https://codeforces.com/blog/entry/149199) · [Enunciados](https://codeforces.com/gym/106262/attachments/download/34830/main.pdf).

**Enunciado:** Cuenta los subconjuntos de tamaño k de {1,…,n} en los que toda diferencia entre dos elementos es prima.

**Solución:** Dos números de igual paridad solo pueden diferir en el primo 2. Esta restricción limita drásticamente los tamaños y patrones posibles. Clasifica esos patrones y cuenta sus desplazamientos válidos usando una criba y acumulados de primos; para tamaños suficientemente grandes no hay soluciones.

<a id="problema-21"></a>
## 21. Tic-Tac-Toe on a Graph

**Concurso:** Manila 2025 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106262/problem/J).

**Recursos:** [Editorial, apartado J](https://codeforces.com/blog/entry/149199) · [Enunciados](https://codeforces.com/gym/106262/attachments/download/34830/main.pdf).

**Enunciado:** Alice y Bob marcan vértices de un grafo; Alice busca completar tres vértices consecutivos propios. Determina qué primeras jugadas le garantizan ganar.

**Solución:** Analiza las amenazas alrededor del primer vértice. Su grado y las continuaciones disponibles en los vecinos permiten decidir si Alice puede crear dos amenazas que Bob no bloquee a la vez. Una clasificación local sustituye la exploración del árbol completo del juego.

<a id="problema-22"></a>
## 22. Trace of Product of Sparse Square Matrices

**Concurso:** Manila 2025 · problema L.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106262/problem/L).

**Recursos:** [Editorial, apartado L](https://codeforces.com/blog/entry/149199) · [Enunciados](https://codeforces.com/gym/106262/attachments/download/34830/main.pdf).

**Enunciado:** Dadas dos matrices cuadradas dispersas, calcula la traza de su producto sin construir una matriz densa.

**Solución:** Expande la definición: tr(AB)=Σᵢⱼ AᵢⱼBⱼᵢ. Solo contribuyen entradas con coordenadas transpuestas. Guarda las entradas no nulas en un mapa o empareja listas ordenadas y acumula sus productos con el módulo indicado.

<a id="problema-23"></a>
## 23. Dreamcatcher

**Concurso:** NWERC 2025 · problema D.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106353/problem/D).

**Recursos:** [Editorial, apartado D](https://2025.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.nwerc.eu/problem-set.pdf).

**Enunciado:** Une muescas de una rueda dando siempre el mismo salto, hasta volver al inicio. Elige el salto que maximiza la longitud total de hilo.

**Solución:** Un salto k visita n/gcd(n,k) muescas y fija la longitud de cada cuerda. El análisis permite buscar un salto coprimo con n cercano a media vuelta. La paridad de n conduce a una elección sencilla, sin probar todos los trazados.

<a id="problema-24"></a>
## 24. Erratic Lights

**Concurso:** NWERC 2025 · problema E.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106353/problem/E).

**Recursos:** [Editorial, apartado E](https://2025.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.nwerc.eu/problem-set.pdf).

**Enunciado:** Cada vez que tocas una bombilla, toma aleatoriamente uno de tres colores. Minimiza el número esperado de toques para dejar todas iguales.

**Solución:** La identidad de las bombillas no importa: basta contar cada color. La estrategia elimina primero el color menos frecuente; su redistribución sigue una binomial. Después se resuelve el caso de dos colores. El punto importante del editorial es justificar la optimalidad de esa estrategia.

<a id="problema-25"></a>
## 25. Juggling Keys

**Concurso:** NWERC 2025 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106353/problem/J).

**Recursos:** [Editorial, apartado J](https://2025.nwerc.eu/solutions.pdf) · [Enunciados](https://2025.nwerc.eu/problem-set.pdf).

**Enunciado:** Varias personas salen y regresan a un departamento con pocas llaves. Si está vacío, quien vuelve necesita una. Decide quién debe llevarla en cada viaje.

**Solución:** Reconstruye primero cuándo queda vacío el departamento. Los regresos a una vivienda vacía fuerzan que ciertos viajes lleven llave. Marca esas obligaciones y recorre los eventos comprobando la disponibilidad de llaves; los viajes no obligatorios pueden dejarla.

<a id="problema-26"></a>
## 26. Booksort

**Concurso:** Latin America Championship 2026 · problema B.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106416/problem/B).

**Recursos:** [Paquete oficial del jurado](https://scorelatam.naquadah.com.br/pda26/contest-packages.tar) · [Código de referencia local](/Users/amgl/.codex/.chatgpt-projects/g-p-6ab682c63f8c81919132a84a94757aff/analisis_contests/fuentes/g13_jury/B_booksort/solutions/JA_reference/B_booksort.cpp) · [Enunciados](https://scorelatam.naquadah.com.br/pda26/contest.pdf).

**Nota:** Recurso de solución: código del jurado. La prueba detallada debe desarrollarse al preparar el guion.

**Enunciado:** Ordena las cantidades de libros de varias pilas. Una operación reparte los libros de dos pilas en sus mitades inferior y superior; hay un límite de operaciones.

**Solución:** Fija el arreglo de izquierda a derecha. Mientras una posición supere el mínimo del sufijo, promedia ambas y deja la mitad menor a la izquierda. Mantén el mínimo con un conjunto ordenado. La contracción de diferencias permite justificar el límite de operaciones; el recurso disponible es código de referencia del jurado.

<a id="problema-27"></a>
## 27. Fun with Balls

**Concurso:** Latin America Championship 2026 · problema F.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106416/problem/F).

**Recursos:** [Paquete oficial del jurado](https://scorelatam.naquadah.com.br/pda26/contest-packages.tar) · [Código de referencia local](/Users/amgl/.codex/.chatgpt-projects/g-p-6ab682c63f8c81919132a84a94757aff/analisis_contests/fuentes/g13_jury/F_pyramid/solutions/roberto_reference/F_pyramid.cpp) · [Enunciados](https://scorelatam.naquadah.com.br/pda26/contest.pdf).

**Nota:** Recurso de solución: código del jurado. La prueba detallada debe desarrollarse al preparar el guion.

**Enunciado:** Añade bolas de colores formando una pila estable, siempre en el lugar más alto disponible. Maximiza el tamaño de una componente de bolas del mismo color.

**Solución:** Casi todas las colocaciones están forzadas. Solo al completar un triángulo aparece la decisión de crecer por un lado u otro. Enumera esas pocas bifurcaciones y, para cada configuración, busca componentes monocromáticas. La altura triangular acota el número real de decisiones.

<a id="problema-28"></a>
## 28. Optimal Balancing Strategy

**Concurso:** Dhaka 2025 · problema H.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106270/problem/H).

**Recursos:** [Editorial, apartado H](https://codeforces.com/gym/106270/attachments/download/35016/editorials.pdf) · [Enunciados](https://codeforces.com/gym/106270/attachments/download/34980/statements%20(1).pdf).

**Enunciado:** Transfiere factores entre números pagando el factor movido. Todos deben terminar como potencias de dos o como impares, respetando cuotas mínimas de ambos tipos.

**Solución:** Conviene mover factores primos por separado. Calcula, para cada número, el costo de eliminar sus factores impares y el de eliminar sus factores dos. Ordena por la diferencia de costos y prueba los cortes que satisfacen las cuotas; un argumento de intercambio justifica ese orden.

<a id="problema-29"></a>
## 29. K.O. Kids

**Concurso:** GCPC 2022 · problema K.

**Enlace:** [Abrir problema](https://codeforces.com/gym/104059/problem/K).

**Recursos:** [Editorial, apartado K](https://2022.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2022.gcpc.nwerc.eu/problemset.pdf).

**Enunciado:** Varios jugadores cruzan un puente de placas reales y falsas siguiendo una regla de alternancia y aprovechando lo aprendido por sus predecesores. Cuenta cuántos sobreviven.

**Solución:** Introduce una placa ficticia inicial para representar el lado de salida. Cada par de placas reales consecutivas del mismo lado ocasiona una eliminación. Cuenta esas coincidencias y réstalas del número de jugadores, con un mínimo de cero.

<a id="problema-30"></a>
## 30. Lots of Land

**Concurso:** GCPC 2022 · problema L.

**Enlace:** [Abrir problema](https://codeforces.com/gym/104059/problem/L).

**Recursos:** [Editorial, apartado L](https://2022.gcpc.nwerc.eu/solutions.pdf) · [Enunciados](https://2022.gcpc.nwerc.eu/problemset.pdf).

**Enunciado:** Divide un rectángulo de celdas en n rectángulos de igual área, con lados enteros, o informa que es imposible.

**Solución:** El área total debe ser divisible por n. Esa condición también permite una división uniforme en una cuadrícula de rectángulos: distribuye los factores entre alto y ancho, encuentra dimensiones compatibles y pinta los bloques resultantes.

<a id="problema-31"></a>
## 31. Amusement Arcade

**Concurso:** GCPC 2021 · problema A.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106167/problem/A).

**Recursos:** [Editorial, apartado A](https://2021.gcpc.nwerc.eu/solution_2021.pdf) · [Enunciados](https://2021.gcpc.nwerc.eu/problemset_2021.pdf).

**Enunciado:** Los visitantes eligen el asiento más alejado de los ocupados. Decide dónde sentarse primero para garantizar la configuración final deseada de asientos alternados.

**Solución:** Analiza cómo se parten los intervalos vacíos. Las longitudes que siempre terminan bien tienen una estructura de potencias de dos. El primer asiento debe dividir la fila en dos partes compatibles; comprobar esa descomposición reemplaza la simulación de todos los desempates.

<a id="problema-32"></a>
## 32. Grid Delivery

**Concurso:** GCPC 2021 · problema G.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106167/problem/G).

**Recursos:** [Editorial, apartado G](https://2021.gcpc.nwerc.eu/solution_2021.pdf) · [Enunciados](https://2021.gcpc.nwerc.eu/problemset_2021.pdf).

**Enunciado:** Recoge paquetes en una cuadrícula donde los vehículos solo pueden avanzar hacia el sur o el este. Minimiza el número de recorridos entre dos esquinas opuestas.

**Solución:** Construye recorridos extremos, atendiendo primero los paquetes que más restringen el avance. El greedy deja al resto rutas compatibles a su lado. La monotonía de la cuadrícula permite justificar la cobertura y recorrer las posiciones sin usar un emparejamiento general.

<a id="problema-33"></a>
## 33. Hectic Harbour II

**Concurso:** GCPC 2021 · problema H.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106167/problem/H).

**Recursos:** [Editorial, apartado H](https://2021.gcpc.nwerc.eu/solution_2021.pdf) · [Enunciados](https://2021.gcpc.nwerc.eu/problemset_2021.pdf).

**Enunciado:** Una grúa extrae contenedores numerados de dos pilas, moviendo los que estorban a la otra. Cuenta cuándo tu contenedor, sin número de extracción, queda accesible.

**Solución:** Concatena una pila con el reverso de la otra: los traslados conservan ese orden y solo desplazan la separación entre ambas. Elimina los contenedores por número, manteniendo vecinos. Después de cada extracción, comprueba si tu contenedor está junto a la separación y, por tanto, arriba de alguna pila.

<a id="problema-34"></a>
## 34. Monty's Hall

**Concurso:** GCPC 2021 · problema M.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106167/problem/M).

**Recursos:** [Editorial, apartado M](https://2021.gcpc.nwerc.eu/solution_2021.pdf) · [Enunciados](https://2021.gcpc.nwerc.eu/problemset_2021.pdf).

**Enunciado:** Eliges s puertas entre d; el presentador abre e puertas vacías que no elegiste. Puedes cambiar tu selección. Calcula la máxima probabilidad de ganar.

**Solución:** Separa la probabilidad que permanece en las puertas originales de la concentrada en las nuevas puertas cerradas. Conviene tomar tantas nuevas como permita el tamaño de la selección y conservar originales si hacen falta. Calcula la probabilidad total distinguiendo dónde estaba inicialmente el premio.

<a id="problema-35"></a>
## 35. Adjusting Drones

**Concurso:** SWERC 2025 · problema A.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106225/problem/A).

**Recursos:** [Editorial, apartado A](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf) · [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf).

**Enunciado:** En cada paso aumentan las copias repetidas de cada valor, salvo una. Calcula cuántos pasos hacen falta para que ninguna frecuencia supere k.

**Solución:** Ordena y calcula dónde termina cada elemento cuando todos son distintos. Su evolución puede reconstruirse sin simular todos los pasos. Como la frecuencia máxima no aumenta, usa una búsqueda binaria y verifica cada tiempo candidato a partir de esa representación.

<a id="problema-36"></a>
## 36. Billion Players Game

**Concurso:** SWERC 2025 · problema B.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106225/problem/B).

**Recursos:** [Editorial, apartado B](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf) · [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf).

**Enunciado:** Debes aceptar, rechazar o invertir varias apuestas sobre un valor desconocido dentro de un intervalo. Maximiza la ganancia garantizada.

**Solución:** Una estrategia fija produce una función afín, así que el peor caso está en un extremo. Ordena las ofertas: intercambios justifican un prefijo de un signo, un sufijo del otro y como mucho una oferta ignorada. Evalúa los cortes con sumas prefijas.

<a id="problema-37"></a>
## 37. Expansion Plan 2

**Concurso:** SWERC 2025 · problema E.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106225/problem/E).

**Recursos:** [Editorial, apartado E](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf) · [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf).

**Enunciado:** Una región de celdas crece por vecinos ortogonales o por los ocho vecinos. Para muchos fragmentos de órdenes, decide si alcanzan una coordenada.

**Solución:** Solo importan las cantidades a de órdenes ortogonales y b de órdenes de ocho vecinos. Se alcanza (x,y) exactamente si |x|+|y|≤a+2b y max(|x|,|y|)≤a+b. Obtén a y b mediante sumas prefijas.

<a id="problema-38"></a>
## 38. Factory Table

**Concurso:** SWERC 2025 · problema F.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106225/problem/F).

**Recursos:** [Editorial, apartado F](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf) · [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf).

**Enunciado:** Observas un fragmento consecutivo de una tabla de multiplicar aplanada por filas. Encuentra el menor tamaño de tabla que puede contenerlo.

**Solución:** Dos elementos consecutivos revelan su fila: dentro de ella, la diferencia es su índice; un salto de fila se reconoce por no aumentar. Recupera después las columnas por división. El mayor índice necesario de fila o columna determina el tamaño mínimo.

<a id="problema-39"></a>
## 39. Jewels Building

**Concurso:** SWERC 2025 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106225/problem/J).

**Recursos:** [Editorial, apartado J](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf) · [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf).

**Enunciado:** Puedes sustituir un bloque de valores iguales por su longitud. Decide si una secuencia puede transformarse en otra.

**Solución:** Demuestra primero que las operaciones permiten condensar cualquier bloque de longitud x en cualquier valor entre 1 y x. Con esa equivalencia, usa DP de prefijos para combinar elementos intactos y bloques condensados, recordando cuándo se permite absorber elementos sobrantes.

<a id="problema-40"></a>
## 40. Crazy Decoder

**Concurso:** Maratona Nordestina 2026 · problema D.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106667/problem/D).

**Recursos:** [Editorial, apartado D](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf) · [Enunciados](https://codeforces.com/gym/106667/attachments/download/39164/statement-en.pdf).

**Enunciado:** Una contraseña de 32 bits sufrió repetidamente la transformación X XOR (X desplazado k bits), truncada a 32 bits. Recupera la original.

**Solución:** En una transformación, los bits bajos se conservan. Luego reconstruye de menor a mayor: cada bit original es el XOR del bit recibido y un bit original ya recuperado. Repite la inversión tantas veces como indique el enunciado.

<a id="problema-41"></a>
## 41. The Scale Riddle

**Concurso:** Maratona Nordestina 2026 · problema E.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106667/problem/E).

**Recursos:** [Editorial, apartado E](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf) · [Enunciados](https://codeforces.com/gym/106667/attachments/download/39164/statement-en.pdf).

**Enunciado:** Identifica una prenda más pesada que las demás mediante una balanza, usando como máximo ocho pesajes.

**Solución:** Divide las candidatas en tres grupos de tamaños parecidos, con igual cantidad en los dos platos. El resultado conserva solo uno de los grupos. Cada pesaje ofrece tres resultados; la partición alcanza la cota de información logarítmica.

<a id="problema-42"></a>
## 42. The Brega Game

**Concurso:** Maratona Nordestina 2026 · problema J.

**Enlace:** [Abrir problema](https://codeforces.com/gym/106667/problem/J).

**Recursos:** [Editorial, apartado J](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf) · [Enunciados](https://codeforces.com/gym/106667/attachments/download/39164/statement-en.pdf).

**Enunciado:** Dos jugadores retiran cartas de los extremos de un intervalo. Gana quien obtiene la carta de mayor valor. Responde quién vence en muchas consultas.

**Solución:** El primer jugador gana si la longitud es par o el máximo está en un extremo. El editorial usa consultas de máximos; alternativamente, precalcula el vecino mayor en cada dirección con pilas monótonas. Así compruebas si un extremo es máximo en O(1) por consulta.
