# Análisis del historial para elegir problemas de la serie

## Resultado y alcance

Se reconstruyeron **23 bloques de concursos y 232 registros de problemas** del archivo `CONTEST Realizados.csv`. Aplicando las reglas de autoría indicadas, el conjunto de investigación contiene **112 candidatos y 6 casos de autoría dudosa**. Se separaron **37 registros por evidencia de autoría ajena** y **77 sin evidencia suficiente de resolución propia**.

Este informe aplica el perfil documentado en [como_elegir_problemas.md](como_elegir_problemas.md): una observación demostrable debe cambiar el modelo del problema y dejar una implementación subordinada a esa idea.

**La investigación documental no está cerrada para todos los candidatos.** Se buscaron fuentes para los 118 y se identificaron sus enunciados, pero **32 permanecen sin evaluación temática definitiva** porque no se pudo consultar una solución oficial. Para cinco problemas del campeonato latinoamericano de 2026 se leyó código del jurado, que se distingue de un editorial explicativo. No se presenta una deducción propia del enunciado como si estuviera confirmada por el editorial.

| Resultado provisional | Registros | Interpretación |
| --- | ---: | --- |
| Encaje fuerte | 42 | Uno tiene autoría dudosa: K Subsequences. Dos se apoyan en código del jurado: Booksort y Fun with Balls. |
| Reserva | 25 | Encaje introductorio, técnica más estándar o necesidad de mejorar la prueba/exposición. Incluye dos autorías dudosas. |
| Fuera del perfil | 14 | Predomina la implementación literal o una técnica estándar sin suficiente reducción conceptual. |
| Ya en la serie | 5 | Jenga Boom, GATA-CAT, Diabolic Doofenshmirtz, Hardcore Hangman y Door 1. |
| Pendiente de fuente de solución | 32 | Tema preliminar identificado; sin veredicto de inclusión o exclusión. Incluye tres autorías dudosas. |
| **Total investigado** | **118** | **112 candidatos + 6 dudas de autoría.** |

Huron Designs, el sexto problema del perfil original, no figura como tal entre estos candidatos. **Huron Airlines es otro problema**: no se sustituye uno por otro ni se cuenta como repetición de Designs.

## Cómo se interpretó el CSV

1. Se conservaron los bloques de `Contest`, incluyendo sus títulos, fechas, enlaces y notas. En este archivo algunas celdas no vacías de esa columna son metadatos del mismo concurso, no un concurso nuevo. El enlace del Gym y los nombres de los problemas resuelven las identificaciones.
2. `ACCEPT`, `Solo ideas` y `★` permiten entrar al conjunto candidato según tu regla, salvo evidencia explícita de resolución ajena. No equivalen por sí solos a prueba histórica de que inventaste personalmente la solución. Los casos sin anotación individual aparecen como **admisión por estado**, no como autoría conceptual confirmada.
3. Las notas donde aportaste la idea y un compañero implementó se admiten. Las ayudas solo de depuración, lectura o implementación no se convierten automáticamente en aporte conceptual principal. Cuando el registro no permite decidirlo, se conserva como duda y se investiga igualmente.
4. Las notas explícitas de autoría ajena prevalecen sobre `ACCEPT`. Para CERC 2010 se aplicó la nota general sobre Jorge; para São Paulo, la nota sobre no haber aportado durante el concurso. Es una interpretación conservadora, no una confirmación adicional tuya. Un upsolve propio posterior puede revertir una exclusión si está documentado.

El número de registro usado aquí corresponde al índice lógico de fila guardado al leer el CSV, incluyendo la cabecera en la numeración; no debe confundirse con la línea física de un archivo con campos multilínea. El CSV original no se modificó. `Tema` se conservó como referencia histórica y no se usó como sustituto del análisis.

Un upsolve con editorial sigue contando como aprendizaje/resolución propia bajo tus reglas: **Adjusting Drones** se incluye aunque también lo resolviera Jorge. **Erratic Lights**, **Coin** y **Door 1** se retienen por el upsolve posterior aunque la anotación del concurso describa ideas incompletas.

## Primera selección para preparar guiones

Esta es una prioridad editorial entre los problemas con fuentes de solución consultadas; no una clasificación de dificultad ni un listado exhaustivo de los que encajan. Todos aparecen de nuevo en el inventario con su evidencia y sus fuentes.

| Prioridad | Problema | Por qué desarrollarlo |
| ---: | --- | --- |
| 1 | [Jumbled Packets](https://codeforces.com/gym/106129/problem/J) | Diseño de información para recuperar un origen perdido. Continúa la vertiente de codificación de la serie. |
| 2 | [Jackpot](https://codeforces.com/gym/105465/problem/J) | Una cota aparentemente incompatible con la adyacencia resulta alcanzable. Ideal para enseñar a probar un greedy. |
| 3 | [Investigating Quadradômeda](https://codeforces.com/gym/106073/problem/I) | Reduce muchas variables geométricas a una sola; la prueba y el algoritmo avanzan juntos. |
| 4 | [Amusement Arcade](https://codeforces.com/gym/106167/problem/A) | Muestra cómo descubrir una estructura aritmética dentro de un proceso recursivo. |
| 5 | [Frangolino ali na mesa](https://codeforces.com/gym/106073/problem/F) | Buen contrapunto probabilístico a Door 1, con una representación mucho más pequeña. |
| 6 | [The Brega Game](https://codeforces.com/gym/106667/problem/J) | Permite enseñar dos reducciones sucesivas: del juego a una condición y de esta a información local. |
| 7 | [Prime Topology](https://codeforces.com/gym/106262/problem/H) | Una observación elemental restringe drásticamente las configuraciones posibles. |
| 8 | [Keyboard Chaos](https://codeforces.com/gym/105537/problem/K) | Un argumento de minimalidad convierte una búsqueda enorme en un conteo. |
| 9 | [Expansion Plan 2](https://codeforces.com/gym/106225/problem/E) | Ejemplo visual de caracterización necesaria y suficiente. Tu admisión se apoya en ACCEPT. |
| 10 | [Just Half is Enough](https://codeforces.com/gym/105537/problem/J) | Episodio corto sobre simetría y garantías constructivas. Tu admisión se apoya en ACCEPT. |

También destacan Congklak, Dreamcatcher, Erratic Lights, Foreign Postcards, Jewels Building y Billion Players Game. Conviene alternar geometría, juegos, probabilidad, construcciones y álgebra; el hilo conductor es la forma de razonar, no una lista fija de temas.

## Cuatro reglas de evaluación

Se mantiene el criterio de la primera fase:

1. **Reducción identificable:** poder explicar qué modelo aparente se reemplaza y qué propiedad lo permite.
2. **Prueba enseñable:** demostrar necesidad, suficiencia y límites relevantes; un patrón observado o un código aceptado no reemplazan esa prueba.
3. **Implementación subordinada:** las estructuras y algoritmos estándar pueden ayudar, pero no deben constituir la mayor parte de la dificultad o del guion.
4. **Aprendizaje transferible:** dejar una herramienta de pensamiento que sirva fuera del problema concreto.

**Fuerte** significa que hay material claro para desarrollar esas cuatro dimensiones; no significa que el guion, la prueba detallada y el código final estén ya preparados. **Reserva** señala una condición concreta para lograrlo. **Fuera** juzga el ajuste a esta serie, no el valor del problema para entrenar. **Pendiente** suspende ese juicio por falta de evidencia de solución.

## Inventario de los 118 candidatos investigados

En cada bloque, los enlaces de enunciado y solución son las fuentes para las filas siguientes. La columna de autoría reproduce las notas pertinentes del CSV; no atribuye la autoría del problema de concurso al usuario. Las técnicas de los bloques pendientes son identificaciones preliminares derivadas del enunciado.


### 1. Brasil 2025 · primera fase / GP México, tercera fecha

Fuentes: [Enunciados](https://codeforces.com/gym/106073/attachments/download/33160/statements-en.pdf) · [Editorial](https://scorelatam.naquadah.com.br/subbr-2025/editorial.pdf).

El mismo conjunto figura con el nombre de la tercera fecha mexicana y de la primera fase brasileña.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 3 · [A. A healthy menu](https://codeforces.com/gym/106073/problem/A) | Status: ACCEPT | Cota por clase: máximo de las preferencias; sumar esos mínimos. | **Reserva.** Buen ejercicio introductorio de cota alcanzable, breve para un episodio completo. |
| 4 · [C. Collatz polynomial](https://codeforces.com/gym/106073/problem/C) | Status: ACCEPT | Polinomios sobre GF(2), desplazamientos y XOR para simular el proceso. | **Reserva.** Necesita centrar la explicación en la terminación; la simulación sola aporta poco. |
| 5 · [D. Dominoes](https://codeforces.com/gym/106073/problem/D) | Status: Solo ideas; Durante: Yo; Upsolve: ★ | Camino euleriano para cada subconjunto y acumulación SOS DP. | **Reserva.** La modelación es valiosa, pero SOS y la enumeración pueden dominar la exposición. |
| 6 · [F. Frangolino ali na mesa](https://codeforces.com/gym/106073/problem/F) | Status: ACCEPT; Durante: Yo idea | Esperanza y recorrido inverso; acumular contribuciones futuras con descuento probabilístico. | **Fuerte.** La inversión temporal elimina la distribución completa de posiciones del robot. |
| 7 · [I. Investigating Quadradômeda](https://codeforces.com/gym/106073/problem/I) | Status: ACCEPT; Durante: Yo | Radios como funciones afines alternantes del primero; intersección de restricciones. | **Fuerte.** Una cadena geométrica se convierte en un intervalo de una sola variable. |
| 8 · [J. João João](https://codeforces.com/gym/106073/problem/J) | Status: ACCEPT | Contar cuáles de cuatro categorías no aparecen. | **Fuera.** No ofrece suficiente desarrollo conceptual para esta serie. |
| 9 · [K. Knockout, swiss and other kinds of tournaments](https://codeforces.com/gym/106073/problem/K) | Upsolve: ★ | Valuación en base dos de coeficientes binomiales y conteo de bits. | **Fuerte.** Combina una restricción de emparejamiento con aritmética; exige explicar la cota de búsqueda. |
| 11 · [M. Minas Gerais' walls](https://codeforces.com/gym/106073/problem/M) | Status: ACCEPT | Búsqueda binaria; el último segmento insuficiente determina dónde reforzar. | **Reserva.** El argumento de posición forzada es el centro; el resto es una plantilla habitual. |


### 2. SEERC 2023

Fuentes: [Enunciados](https://codeforces.com/gym/105465/attachments/download/27988/statements-seerc-2023.pdf) · [Editorial](https://codeforces.com/gym/105465/attachments/download/27986/tutorials-seerc-2023.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 15 · [B. Build Permutation](https://codeforces.com/gym/105465/problem/B) | Status: ACCEPT | Ordenar y emparejar extremos para obtener sumas iguales. | **Reserva.** Buena demostración de necesidad, pero de alcance introductorio. |
| 17 · [F. Fast XORting](https://codeforces.com/gym/105465/problem/F) | Status: Solo ideas; Durante: Yo; Upsolve: ★ | Agrupar los XOR; las inversiones se separan por el bit distinto más significativo. | **Fuerte.** Convierte una optimización global en decisiones independientes por bit. |
| 18 · [J. Jackpot](https://codeforces.com/gym/105465/problem/J) | Status: ACCEPT; Durante: Yo | Cota entre mitades ordenadas, alcanzable eliminando vecinos de clases opuestas. | **Fuerte.** La restricción de adyacencia desaparece mediante una prueba constructiva. |
| 19 · [K. $K$ Subsequences](https://codeforces.com/gym/105465/problem/K) | **Autoría dudosa.** Status: ACCEPT; Durante: ayudar | Distribución greedy de signos con invariantes sobre máximos de sufijos. | **Fuerte.** El argumento de equilibrio es afín; la autoría permanece por confirmar. |


### 3. NWERC 2022

Fuentes: [Enunciados](https://2022.nwerc.eu/main/problem-set.pdf) · [Editorial](https://chipcie.wisv.ch/archive/2022/nwerc/solutions.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 23 · [B. Bottle Flip](https://codeforces.com/gym/104875/problem/B) | Status: ACCEPT; Durante: Yo | Centro de masa como función de la altura; cancelar el radio y optimizar. | **Fuerte.** Modelación física y reducción algebraica directamente comparables con Jenga Boom. |
| 24 · [C. Circular Caramel Cookie](https://codeforces.com/gym/104875/problem/C) | Status: ACCEPT; Durante: Yo / Rolegio; Detalles: Rogelio me ayudo proque no salia, uso cosas de presiicion en bsuqueda bianria de reales, pero no hacia falta; Upsolve: ★; Observaciones: UPSOLVEADO | Simetría por cuadrantes, conteo de cuadrados completos y búsqueda del radio. | **Reserva.** Encaja si el conteo geométrico domina sobre el manejo de precisión. |
| 28 · [I. Interview Question](https://codeforces.com/gym/104875/problem/I) | Status: ACCEPT | Inferir períodos de Fizz y Buzz por separado a partir de sus apariciones. | **Reserva.** Reconstrucción inversa clara, con casos pequeños que limitan su profundidad. |


### 4. Kunming 2024

Fuentes: [Enunciados](https://codeforces.com/gym/105588/attachments/download/28813/1-statement-english.pdf) · [Editorial](https://codeforces.com/gym/105588/attachments/download/28803/tutorial.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 32 · [C. Coin](https://codeforces.com/gym/105588/problem/C) | Status: solo ideas; Durante: yo ideas, pero nada; Upsolve: ★ | Invertir la eliminación de posiciones y agrupar pasos con el mismo cociente. | **Fuerte.** La aceleración nace de entender el proceso; deben justificarse los saltos. |
| 34 · [G. GCD](https://codeforces.com/gym/105588/problem/G) | **Autoría dudosa.** Status: ACCEPT; Durante: Jorge, yo ayuda | Reducciones por máximo común divisor y búsqueda acotada con argumentos de paridad. | **Reserva.** No seleccionar sin una cota de ejecución explicable y sin aclarar tu aporte. |
| 35 · [H. Horizon Scanning](https://codeforces.com/gym/105588/problem/H) | Status: ACCEPT; Durante: Yo idea, / Roleglio implementacion | Orden angular y separación cíclica entre posiciones a distancia k. | **Fuerte.** Sustituye todas las orientaciones continuas por una condición finita. |


### 5. NCPC 2025

Fuentes: [Enunciados](https://codeforces.com/gym/106124/attachments/download/33915/ncpc2025problems_compressed.pdf) · [Editorial](https://codeforces.com/gym/106124/attachments/download/33916/ncpc25slides.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 41 · [A. Arithmetic Adaptation](https://codeforces.com/gym/106124/problem/A) | Status: ACCEPT | Construcción aritmética con restricciones pequeñas sobre los sumandos. | **Fuera.** Observación demasiado elemental para sostener el perfil actual. |
| 43 · [C. Crochet Competition](https://codeforces.com/gym/106124/problem/C) | Status: ACCEPT | Conversión de tiempo semanal y formato de la duración. | **Fuera.** Predominan las convenciones de entrada y salida. |
| 44 · [D. Dune Dash](https://codeforces.com/gym/106124/problem/D) | Status: ACCEPT | Encontrar un extremo por máxima distancia y ordenar desde él. | **Fuerte.** La propiedad geométrica permite reconstruir una ruta sin búsqueda combinatoria. |
| 45 · [E. Egyptian Equality](https://codeforces.com/gym/106124/problem/E) | Status: ACCEPT; Durante: Yo / Jorge; Detalles: Yo, jorge me ayudo un poco, al final creo que si dimos con la idea pero no daba tiempo estaba muy talachudo | Recorridos de la región triangular para construir dos zonas conexas equilibradas. | **Reserva.** Los casos geométricos y la construcción pueden absorber demasiado tiempo de implementación. |
| 46 · [G. Gotta Trade Some of 'Em](https://codeforces.com/gym/106124/problem/G) | Status: ACCEPT | Componentes conexas con suficiente tamaño; repartir todas las variantes en cada componente. | **Reserva.** La suficiencia es enseñable, aunque el mecanismo algorítmico es muy estándar. |
| 47 · [I. Instagraph](https://codeforces.com/gym/106124/problem/I) | Status: ACCEPT; Durante: Yo | Contar seguidores entrantes y descontar relaciones recíprocas. | **Fuera.** El cálculo reproduce directamente la definición. |
| 48 · [K. km/h](https://codeforces.com/gym/106124/problem/K) | Status: ACCEPT; Durante: Yo | Mantener una cota inferior del límite nacional y redondear al siguiente múltiplo de diez. | **Reserva.** Pequeño ejemplo de inferencia con información parcial. |


### 6. GCPC 2025

Fuentes: [Enunciados](https://2025.gcpc.nwerc.eu/contest.pdf) · [Editorial](https://2025.gcpc.nwerc.eu/solutions.pdf).

El enlace corresponde a GCPC 2025, aunque uno de los rótulos del CSV indica 2024.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 51 · [A. Around the Table](https://codeforces.com/gym/106129/problem/A) | Status: ACCEPT; Durante: Yo | Identificar pocas diferencias cíclicas posibles entre jugadores y descontar coincidencias. | **Fuerte.** Un proceso aparentemente interminable se reduce a clases de emparejamientos. |
| 53 · [C. Congklak](https://codeforces.com/gym/106129/problem/C) | Status: ACCEPT | Detectar un contador binario en los hoyos alternos y sus acarreos. | **Fuerte.** Excelente paso de simulación literal a representación numérica. |
| 54 · [D. Demand for Cycling](https://codeforces.com/gym/106129/problem/D) | Status: ACCEPT | Cota por proyecciones horizontales y verticales, alcanzada por el rectángulo envolvente. | **Fuerte.** Prueba geométrica breve con reducción considerable del problema. |
| 57 · [G. Generating Cool Passwords Company](https://codeforces.com/gym/106129/problem/G) | Status: ACCEPT | Codificar identificadores duplicados dentro de contraseñas válidas para asegurar distancia de edición. | **Reserva.** Construcción útil para una introducción a redundancia y separación de códigos. |
| 58 · [H. Happy Hookup](https://codeforces.com/gym/106129/problem/H) | Status: ACCEPT | Intersección de los conjuntos alcanzables desde dos vértices. | **Fuera.** Dos recorridos de grafo estándar constituyen casi toda la solución. |
| 60 · [J. Jumbled Packets](https://codeforces.com/gym/106129/problem/J) | Status: ACCEPT; Durante: Yo / Jorge; Detalles: Jorge me ayudo a rebotar ideas e implementar | Codificación ternaria con un marcador que permite deshacer una rotación desconocida. | **Fuerte.** Diseña información para romper una simetría, como Hardcore Hangman. |
| 63 · [M. Mex Hex](https://codeforces.com/gym/106129/problem/M) | Status: ACCEPT | Elegir qué valor eliminar y cubrir sus apariciones mediante intervalos greedy. | **Fuerte.** La inversión del objetivo mex evita optimizar directamente todas las secuencias de escudos. |


### 7. Northwestern Russia Regional 2024

Fuentes: [Enunciados](https://codeforces.com/gym/105537/attachments/download/28362/statements.pdf) · [Editorial](https://codeforces.com/gym/105537/attachments/download/38889/tutorial.pdf).

El conjunto corresponde al regional celebrado en 2024; el rótulo del CSV menciona 2025. El nombre oficial de K es Keyboard Chaos.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 66 · [A. Another Brick in the Wall](https://codeforces.com/gym/105537/problem/A) | Status: ACCEPT | Paridad de longitudes y construcción alternada de filas de ladrillos. | **Reserva.** Buena combinación de cota inferior y construcción elemental. |
| 68 · [F. False Alarm](https://codeforces.com/gym/105537/problem/F) | Status: ACCEPT; Durante: Yo | Buscar dos o tres alarmas cercanas; añadir las que falten. | **Fuera.** El análisis de casos es demasiado pequeño para el perfil de la serie. |
| 70 · [I. If I Could Turn Back Time](https://codeforces.com/gym/105537/problem/I) | Status: ACCEPT | Orden de alturas y monotonía de las pérdidas para reconstruir la erosión. | **Fuerte.** Las condiciones globales reemplazan una simulación de muchos años. |
| 71 · [J. Just Half is Enough](https://codeforces.com/gym/105537/problem/J) | Status: ACCEPT | Un orden y su reverso reparten todas las aristas dirigidas entre ambos. | **Fuerte.** Simetría que convierte una garantía existencial en una construcción inmediata. |
| 72 · [K. Keyboard Chao](https://codeforces.com/gym/105537/problem/K) | Status: ACCEPT; Durante: Yo | Reducir la palabra imposible más corta a repeticiones de una sola letra. | **Fuerte.** Una prueba de minimalidad elimina la búsqueda sobre todas las cadenas. |


### 9. Regional Latinoamericano 2025–2026

Fuentes: [Enunciados](https://scorelatam.naquadah.com.br/latam-2025/contest.pdf).

**Fuente incompleta.** El [anuncio del jurado](https://codeforces.com/blog/entry/148306) todavía anuncia el editorial como trabajo en curso. Se revisaron la página oficial y los paquetes BOCA: los paquetes F, J y K consultados incluyen enunciados y datos, pero no se encontró código de solución de referencia. Los comentarios de participantes no se reclasifican como editorial oficial.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 88 · [F. Fuzzy Factorization](https://codeforces.com/group/8JufKtWW7p/contest/106178/problem/F) | Status: ACCEPT; Durante: Yo idea, Jorge implementacion; Upsolve: ★ | Factorización aproximada de un entero enorme; posible reducción por cifras significativas. | **Pendiente.** Enunciado leído; no se recuperó editorial ni solución de referencia del paquete BOCA. |
| 92 · [J. Judgmental Crowd](https://codeforces.com/group/8JufKtWW7p/contest/106178/problem/J) | **Autoría dudosa.** Status: ACCEPT; Durante: Yo lei, jorge implementacion; Upsolve: ★ | Conteo de ocurrencias de tres patrones fijos con pesos. | **Pendiente.** Enunciado leído; editorial no localizado y aporte conceptual ambiguo. |
| 93 · [K. Kings Conquest](https://codeforces.com/group/8JufKtWW7p/contest/106178/problem/K) | Status: ACCEPT; Durante: Yo; Upsolve: ★ | Optimización de la caja envolvente al desplazar reyes en ocho direcciones. | **Pendiente.** Falta contrastar la técnica y la prueba completas con una solución oficial. |


### 10. NEERC 2016

Fuentes: [Enunciados](https://neerc.ifmo.ru/archive/2016/neerc-2016-statement.pdf) · [Editorial](https://neerc.ifmo.ru/archive/2016/neerc-2016-review.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 100 · [F. Foreign Postcards](https://codeforces.com/gym/101190/problem/F) | Status: ACCEPT; Durante: Yo | Esperanza sobre sufijos y reordenamiento de sumas para una recurrencia lineal. | **Fuerte.** Comprime un proceso aleatorio sin enumerar sus particiones. |
| 102 · [J. Jenga Boom](https://codeforces.com/gym/101190/problem/J) | Status: solo ideas; Durante: yo ideas, Rolegio ayudo un poco; Detalles: las dieas que dio Rogelio ssi se ocuparon pero unas cosillas dieron memoria excedida, al final cehche otra cosa, y de lo que yo dije habia que pulir unas cosas sobretodo lod el cm; Upsolve: ★ | Centro de masa y extremos del soporte por capa. | **Ya en serie.** Es uno de los seis problemas de referencia, no una propuesta nueva. |


### 11. Manila 2025

Fuentes: [Enunciados](https://codeforces.com/gym/106262/attachments/download/34830/main.pdf) · [Editorial](https://codeforces.com/blog/entry/149199).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 105 · [A. Alphabet Chocolate](https://codeforces.com/gym/106262/problem/A) | Status: ACCEPT | Paridad de la longitud y carácter central. | **Fuera.** La solución es prácticamente una lectura directa del proceso. |
| 106 · [E. Long Distance Examination](https://codeforces.com/gym/106262/problem/E) | Status: ACCEPT | BFS en el producto de las posiciones del héroe y su clon. | **Reserva.** La modelación del estado es útil; el recorrido estándar domina después. |
| 107 · [G. Max Cut Min Flow](https://codeforces.com/gym/106262/problem/G) | Status: ACCEPT | Elegir ganancias no negativas y, si hace falta, la pérdida mínima que bloquea el canal. | **Fuera.** El título sugiere flujo, pero el núcleo termina siendo un greedy muy breve. |
| 108 · [H. Prime Topology](https://codeforces.com/gym/106262/problem/H) | Status: ACCEPT; Durante: Yo | Paridad restringe los conjuntos con diferencias primas a pocos tamaños y patrones. | **Fuerte.** Una familia combinatoria grande colapsa por una propiedad elemental de los primos. |
| 109 · [J. Tic-Tac-Toe on a Graph](https://codeforces.com/gym/106262/problem/J) | Status: solo ideas; Durante: yo y rogelio ideas; Upsolve: ★ | Clasificar primeras jugadas mediante grados y amenazas en vecindarios pequeños. | **Fuerte.** Reemplaza el árbol completo del juego por condiciones locales demostrables. |
| 110 · [L. Trace of Product of Sparse Square Matrices](https://codeforces.com/gym/106262/problem/L) | Status: ACCEPT; Durante: Yo | Expandir tr(AB) y emparejar únicamente entradas con índices transpuestos. | **Fuerte.** El álgebra evita construir el producto matricial. |


### 12. NWERC 2025

Fuentes: [Enunciados](https://2025.nwerc.eu/problem-set.pdf) · [Editorial](https://2025.nwerc.eu/solutions.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 116 · [D. Dreamcatcher](https://codeforces.com/gym/106353/problem/D) | Status: ACCEPT; Durante: yo la idea, jorge implementacion | Longitud de cuerdas, órbitas modulares y elección de un salto coprimo. | **Fuerte.** Conecta geometría y aritmética para eliminar una búsqueda de configuraciones. |
| 117 · [E. Erratic Lights](https://codeforces.com/gym/106353/problem/E) | Status: solo ideas; Durante: trabaje en este pero no quedo; Upsolve: ★ | Estado por cantidades de colores; estrategia de eliminación y distribución binomial. | **Fuerte.** La simetría probabilística concentra la dificultad en justificar la estrategia óptima. |
| 118 · [F. Fair Share](https://codeforces.com/gym/106353/problem/F) | Status: ACCEPT | Una desigualdad por persona obtenida a partir del déficit total. | **Reserva.** Reducción algebraica válida, pero corta para un episodio independiente. |
| 119 · [J. Juggling Keys](https://codeforces.com/gym/106353/problem/J) | Status: ACCEPT | Identificar viajes que necesariamente requieren llave y comprobar disponibilidad temporal. | **Fuerte.** Pensar primero en las obligaciones futuras convierte la asignación en una verificación. |
| 120 · [K. KIT Finding](https://codeforces.com/gym/106353/problem/K) | Status: ACCEPT | Construcción de la cuadrícula separando letras para impedir apariciones adicionales de KIT. | **Reserva.** Interesante control de patrones; conviene comprobar que la exposición no sea una receta. |
| 121 · [L. Last Christmas](https://codeforces.com/gym/106353/problem/L) | Status: ACCEPT | Conteos por artista y desempates lexicográficos de frecuencias. | **Fuera.** Predomina la implementación de las reglas del enunciado. |


### 13. Latin America Championship 2026

Fuentes: [Enunciados](https://scorelatam.naquadah.com.br/pda26/contest.pdf).

**Contraste con jurado, no con editorial narrativo.** Se leyeron las soluciones de referencia `JA_reference/B_booksort.cpp`, `marcos_reference/E_eye_exam.cpp`, `roberto_reference/F_pyramid.cpp` y `moro-reference/J_platos.cpp` del [paquete oficial](https://scorelatam.naquadah.com.br/pda26/contest-packages.tar). GATA-CAT cuenta además con el análisis local de la primera fase. Estas evaluaciones conservan la salvedad de desarrollar la prueba, especialmente en Booksort y Jaime’s Palace.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 125 · [B. Booksort](https://codeforces.com/gym/106416/problem/B) | Status: ACCEPT | Fijar un prefijo ordenado promediando con el mínimo del sufijo; contracción de diferencias. | **Fuerte.** El código de referencia respalda la construcción; el guion debe demostrar el límite de operaciones. |
| 127 · [E. Eye Exam](https://codeforces.com/gym/106416/problem/E) | Status: ACCEPT | Cada comparación de lentes impone un semieje o un punto; intersectar intervalos enteros. | **Reserva.** Buen problema introductorio de transformar distancias en restricciones. |
| 128 · [F. Fun with Balls](https://codeforces.com/gym/106416/problem/F) | Status: ACCEPT | La colocación es forzada salvo al completar triángulos; enumerar esas decisiones y recorrer componentes. | **Fuerte.** El límite pequeño de bifurcaciones hace viable una búsqueda que parece exponencial en N. |
| 129 · [G. GATA-CAT](https://codeforces.com/gym/106416/problem/G) | Status: ACCEPT; Durante: Yo | Esqueleto AT fijo y conteo combinatorio de inserciones independientes. | **Ya en serie.** Ya forma parte de la serie; ahora también hay código del jurado disponible. |
| 131 · [J. Jaime's Palace](https://codeforces.com/gym/106416/problem/J) | Status: ACCEPT; Durante: Yo; Detalles: the easy | Incrementar los platos usados y reordenarlos para mantener los menos usados accesibles. | **Reserva.** El jurado respalda el greedy; falta desarrollar el argumento de intercambio para un guion. |


### 14. Dhaka 2025

Fuentes: [Enunciados](https://codeforces.com/gym/106270/attachments/download/34980/statements%20(1).pdf) · [Editorial](https://codeforces.com/gym/106270/attachments/download/35016/editorials.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 135 · [C. Gas Reservoir](https://codeforces.com/gym/106270/problem/C) | Status: ACCEPT | Componentes conexas tridimensionales y suma sin duplicados por columna de perforación. | **Fuera.** La solución es principalmente recorrido y contabilización estándar. |
| 137 · [F. Morning Walk](https://codeforces.com/gym/106270/problem/F) | Status: ACCEPT | Velocidad relativa y periodicidad de los encuentros en una circunferencia. | **Reserva.** Modelación física limpia, apropiada como episodio introductorio. |
| 138 · [H. Optimal Balancing Strategy](https://codeforces.com/gym/106270/problem/H) | Status: ACCEPT; Durante: Yo; Detalles: algo tartdado en implementar pero la idea esta masomenos facil | Separar costos por factores primos y ordenar las diferencias de dos opciones. | **Fuerte.** La transferencia de factores y el intercambio reducen una optimización aparentemente acoplada. |
| 139 · [J. C-Style String Length](https://codeforces.com/gym/106270/problem/J) | Status: ACCEPT; Durante: Yo | Decodificar escapes y detenerse ante el primer carácter nulo. | **Fuera.** Es análisis sintáctico y simulación de reglas. |


### 15. GCPC 2022

Fuentes: [Enunciados](https://2022.gcpc.nwerc.eu/problemset.pdf) · [Editorial](https://2022.gcpc.nwerc.eu/solutions.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 145 · [C. Chaotic Construction](https://codeforces.com/gym/104059/problem/C) | Status: ACCEPT; Durante: yo idea, Jorge implementar | Mantener posiciones bloqueadas y consultar ambos arcos de una circunferencia. | **Fuera.** La estructura ordenada y sus consultas constituyen el mecanismo principal. |
| 146 · [D. Diabolic Doofenshmirtz](https://codeforces.com/gym/104059/problem/D) | Status: ACCEPT; Durante: YO IDEA, jorge implementar; Detalles: idea pasadisima de webos, no se como lo hice, en verdad soy muy bueno | Consultas exponenciales para identificar el primer desbordamiento modular. | **Ya en serie.** Es uno de los seis problemas de referencia. |
| 150 · [H. Hardcore Hangman](https://codeforces.com/gym/104059/problem/H) | Status: ACCEPT; Durante: Yo IDEA, Rogelio Implementar; Detalles: idea pasadisima de webos, no se como lo hice, en verdad soy muy bueno | Firmas binarias de letras y reconstrucción a partir de consultas. | **Ya en serie.** Es uno de los seis problemas de referencia. |
| 153 · [K. K.O. Kids](https://codeforces.com/gym/104059/problem/K) | Status: ACCEPT; Durante: Yo | Contar igualdades entre placas consecutivas para contar eliminaciones. | **Fuerte.** Sustituye una simulación de jugadores por un estadístico del puente. |
| 154 · [L. Lots of Land](https://codeforces.com/gym/104059/problem/L) | Status: ACCEPT; Durante: Yo | Divisibilidad del área y distribución de factores para una partición rectangular uniforme. | **Fuerte.** La condición necesaria también es suficiente; la construcción materializa la prueba. |


### 16. GP México 2026 · primera fecha

Fuentes: [Enunciados](https://codeforces.com/gym/106495/problems).

**Editorial localizado, contenido no consultado.** El [anuncio oficial](https://codeforces.com/blog/entry/153330) enlaza el [video de soluciones](https://www.youtube.com/watch?v=Wcile2J530o). La página del video fue accesible, pero la consulta de sus subtítulos devolvió contenido vacío. Se suspende el veredicto de los seis candidatos nuevos; Door 1 conserva su condición de problema base por los materiales locales ya analizados.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 161 · [A. Anxiety at the restaurant](https://codeforces.com/gym/106495/problem/A) | Status: ACCEPT | Sumas y comparación con el costo más una propina del diez por ciento. | **Pendiente.** Enunciado leído; editorial localizado en video, pero sin transcripción recuperable. |
| 163 · [C. Cactus Simple Path Queries](https://codeforces.com/gym/106495/problem/C) | Upsolve: ★ | Consultas de caminos simples mínimos en cactus con pesos negativos. | **Pendiente.** Falta consultar el editorial en video; no se presume que una técnica estándar sea la oficial. |
| 164 · [D. Door 1](https://codeforces.com/gym/106495/problem/D) | Status: solo ideas vagas; Durante: Angel Idea; Upsolve: ★ | Actualización bayesiana y DP sobre un estado suficiente. | **Ya en serie.** Guion y código locales ya analizados; el video oficial fue localizado, no transcrito. |
| 165 · [E. Erasmus Valthron](https://codeforces.com/gym/106495/problem/E) | Status: ACCEPT | Orden lexicográfico de las factorizaciones primas de 1 a N. | **Pendiente.** Tema identificado en el enunciado; técnica oficial sin verificar. |
| 167 · [G. Gerald the mudcrab](https://codeforces.com/gym/106495/problem/G) | Status: ACCEPT | Contar valores ausentes, equivalentes al exceso de duplicados. | **Pendiente.** Enunciado leído; editorial en video sin transcripción recuperable. |
| 169 · [I. Inner Product](https://codeforces.com/gym/106495/problem/I) | Status: ACCEPT | Etiquetas mínimas que satisfacen desigualdades vecinas, con pesos positivos. | **Pendiente.** Posible compresión de igualdades y recorridos direccionales; falta contraste oficial. |
| 170 · [J. Just the right enchantment](https://codeforces.com/gym/106495/problem/J) | Status: ACCEPT | Conteo combinatorio de ternas por paridad. | **Pendiente.** Enunciado leído; editorial en video sin transcripción recuperable. |


### 17. GCPC 2021

Fuentes: [Enunciados](https://2021.gcpc.nwerc.eu/problemset_2021.pdf) · [Editorial](https://2021.gcpc.nwerc.eu/solution_2021.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 173 · [A. Amusement Arcade](https://codeforces.com/gym/106167/problem/A) | Status: ACCEPT; Durante: Yo lo pense, y di la idea, la impletacion era muy corta y sencilla, jorge lo implemento | Descomposición recursiva de intervalos que caracteriza longitudes mediante potencias de dos. | **Fuerte.** El proceso de elegir asientos se transforma en una condición aritmética. |
| 174 · [B. Brexiting and Brentering](https://codeforces.com/gym/106167/problem/B) | Status: ACCEPT | Encontrar la última vocal y sustituir el sufijo. | **Fuera.** Manipulación literal de texto, sin reducción conceptual relevante. |
| 175 · [C. Card Trading](https://codeforces.com/gym/106167/problem/C) | Status: ACCEPT | Ordenar precios y acumular oferta y demanda para maximizar la facturación. | **Reserva.** Puede enseñar por qué basta revisar ciertos precios, aunque el barrido es estándar. |
| 179 · [G. Grid Delivery](https://codeforces.com/gym/106167/problem/G) | Status: ACCEPT | Cobertura por recorridos monótonos mediante un greedy de rutas extremas. | **Fuerte.** La estructura de la cuadrícula permite evitar un enfoque genérico de emparejamiento. |
| 180 · [H. Hectic Harbour II](https://codeforces.com/gym/106167/problem/H) | Status: ACCEPT; Durante: Yo, me ayudo jorge cone structura | Unir conceptualmente ambas pilas y observar extracciones respecto del hueco central. | **Fuerte.** La representación transforma la simulación; evitar centrar el guion en listas enlazadas. |
| 181 · [I. Index Case](https://codeforces.com/gym/106167/problem/I) | **Autoría dudosa.** Durante: Idea: yp y jorge | Inversión de un autómata celular circular mediante DP de pares adyacentes. | **Reserva.** Compresión de estado interesante, pero ni la autoría ni la resolución constan claramente. |
| 183 · [K. Killjoys' Conference](https://codeforces.com/gym/106167/problem/K) | Status: ACCEPT; Durante: Yo | Bipartición por componentes, simetría entre salas y principio del palomar. | **Reserva.** La cuenta es elegante, aunque muy próxima a una aplicación estándar de bipartición. |
| 185 · [M. Monty's Hall](https://codeforces.com/gym/106167/problem/M) | Status: ACCEPT; Durante: Yo | Probabilidad condicional y distribución de elecciones entre puertas originales y nuevas. | **Fuerte.** Generaliza Monty Hall mediante un modelo compacto y una estrategia demostrable. |


### 18. GP México 2026 · segunda fecha

Fuentes: [Enunciados](https://codeforces.com/gym/106540/problems).

**Editorial localizado, contenido no consultado.** El [anuncio oficial](https://codeforces.com/blog/entry/154104) enlaza el [video de soluciones](https://www.youtube.com/watch?v=zRtVUkbxlMw). No se recuperó una transcripción utilizable. Los ocho candidatos quedan pendientes, incluso cuando el enunciado permite reconocer una técnica sencilla.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 187 · [A. A simple problem](https://codeforces.com/gym/106540/problem/A) | Upsolve: ★; Observaciones: upsolveado gracias a un hint que me dio Rogelio | Contar cadenas distintas concatenando prefijos; evitar multiplicidad de descomposiciones. | **Pendiente.** Enunciado leído; falta verificar la solución del editorial en video. |
| 188 · [B. Baus Stream](https://codeforces.com/gym/106540/problem/B) | Upsolve: ★ | Borrado de exactamente k nombres mediante grupos de prefijos. | **Pendiente.** Estructura de trie y optimización combinatoria; solución oficial no recuperada. |
| 189 · [C. Counting heroes](https://codeforces.com/gym/106540/problem/C) | Status: ACCEPT; Durante: Le ayude a Jorge, di la idea, el la implemento, no estaba dificil | Probabilidad de a+b=c condicionada a a<b<c, acumulada entre pruebas. | **Pendiente.** Enunciado leído; no se pudo consultar el contenido del video oficial. |
| 190 · [D. Dragon King's Palace](https://codeforces.com/gym/106540/problem/D) | Status: ACCEPT | Mayor segmento contenido en la unión de dos discos. | **Pendiente.** La geometría requiere una prueba completa; no basta inferir el tema por el nombre. |
| 191 · [E. Evil "Taquero"](https://codeforces.com/gym/106540/problem/E) | Status: ACCEPT | Sustitución de un patrón fijo dentro de una cadena. | **Pendiente.** Enunciado leído; editorial en video sin texto recuperable. |
| 193 · [G. Group forming](https://codeforces.com/gym/106540/problem/G) | **Autoría dudosa.** Status: ACCEPT; Durante: Le aydue a Rogelio | Emparejar vértices de distintas clases de equivalencia de amistad. | **Pendiente.** Falta contraste oficial y aclarar si tu ayuda incluyó la idea clave. |
| 194 · [H. Huron Airlines](https://codeforces.com/gym/106540/problem/H) | Durante: Con mas tiempo; Upsolve: ★ | Simulación optimizada del abordaje de pasajeros y sus bloqueos. | **Pendiente.** Hay código local de Huron Airlines, pero no editorial consultado; no confundir con Huron Designs. |
| 195 · [I. I don't have the name I was supposed to have](https://codeforces.com/gym/106540/problem/I) | Status: ACCEPT | Validación de una gramática restringida de texto y notación matemática. | **Pendiente.** Enunciado leído; editorial en video sin texto recuperable. |


### 19. SWERC 2025

Fuentes: [Enunciados](https://codeforces.com/gym/106225/attachments/download/34507/statements%20(1).pdf) · [Editorial](https://codeforces.com/gym/106225/attachments/download/34510/main%20(5).pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 199 · [A. Adjusting Drones](https://codeforces.com/gym/106225/problem/A) | Detalles: tambien lo upsolveao Jorge sin usar la editorial con idea propioa, yo lo upslovei con la solucion de la editorial; Upsolve: ★ | Ordenar, calcular la configuración terminal y reconstruir el estado tras t pasos. | **Fuerte.** Permite búsqueda por monotonía sin ejecutar cada operación; tu upsolve con editorial sí cuenta. |
| 200 · [B. Billion Players Game](https://codeforces.com/gym/106225/problem/B) | Upsolve: ★ | Pagos afines: peor caso en extremos; intercambios reducen las decisiones a cortes ordenados. | **Fuerte.** Buena combinación de optimización robusta y reducción de estrategias. |
| 202 · [D. Dungeon Equilibrium](https://codeforces.com/gym/106225/problem/D) | Status: ACCEPT | Contar frecuencias y decidir por separado las eliminaciones de cada valor. | **Fuera.** El greedy es demasiado directo para el perfil actual. |
| 203 · [E. Expansion Plan 2](https://codeforces.com/gym/106225/problem/E) | Status: ACCEPT | Expansiones conmutativas descritas por dos desigualdades y conteos de símbolos. | **Fuerte.** Un crecimiento infinito se vuelve una caracterización geométrica exacta. |
| 204 · [F. Factory Table](https://codeforces.com/gym/106225/problem/F) | Status: ACCEPT | Diferencias entre vecinos revelan filas y columnas de una tabla de multiplicar. | **Fuerte.** Reconstrucción inversa con información local, sin probar todas las tablas. |
| 208 · [J. Jewels Building](https://codeforces.com/gym/106225/problem/J) | Status: ACCEPT | Demostrar operaciones equivalentes más potentes y después usar DP de prefijos. | **Fuerte.** La reducción de las operaciones, no la plantilla de DP, contiene la idea central. |


### 21. Maratona Nordestina 2026

Fuentes: [Enunciados](https://codeforces.com/gym/106667/attachments/download/39164/statement-en.pdf) · [Editorial](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf).

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 226 · [B. Good Spotlights](https://codeforces.com/gym/106667/problem/B) | Status: ACCEPT | Ciclo de Gray de tres bits y rotación para elegir el inicio. | **Reserva.** Buen ejemplo introductorio; el tamaño fijo permite una solución inmediata. |
| 228 · [D. Crazy Decoder](https://codeforces.com/gym/106667/problem/D) | Status: ACCEPT; Durante: Yo idea, yo implementacion, me ayudo a debugear Jorge | Invertir XOR con desplazamiento resolviendo bits de menor a mayor. | **Fuerte.** Reconstrucción triangular que elimina una búsqueda entre enteros de 32 bits. |
| 229 · [E. The Scale Riddle](https://codeforces.com/gym/106667/problem/E) | Status: ACCEPT | Dividir candidatos en tres grupos y alcanzar la cota de información por pesaje. | **Fuerte.** Diseño de consultas y prueba de suficiencia; los dos platos deben tener igual tamaño. |
| 231 · [G. Queue Mischief](https://codeforces.com/gym/106667/problem/G) | Status: ACCEPT | Actualizar el número de pares AB mediante conteos de letras en los extremos. | **Reserva.** Una deque solo conserva el orden; el razonamiento de contribuciones es el aprendizaje. |
| 234 · [J. The Brega Game](https://codeforces.com/gym/106667/problem/J) | Status: ACCEPT; Durante: Yo idea, yo implementacion | La victoria depende de paridad y de si el máximo está en un extremo. | **Fuerte.** Los vecinos de mayor valor permiten verificar la condición sin una estructura de consultas de máximos. |
| 236 · [L. Lampions League](https://codeforces.com/gym/106667/problem/L) | Status: ACCEPT; Durante: Yo | Módulo dos convierte la diferencia alternante en la suma triangular. | **Reserva.** Invariante muy breve, útil como introducción a simplificación modular. |


### 22. XIII Maratona Mineira 2026

Fuentes: [Enunciados](https://codeforces.com/gym/106552/attachments/download/37926/contest-en_removed.pdf).

**Editorial no localizado.** Se consultaron el Gym y la [página de la prueba del organizador](https://mineira.sbc.org.br/maratonas-passadas/xiii-maratona-mineira-2026-prova), que enlaza problemas y resultados, pero no un editorial escrito en lo recuperado. No se afirma que no exista uno en otro lugar. El nombre oficial de B es Bario World.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 240 · [A. Ana, Hooray for Mariana!](https://codeforces.com/gym/106552/problem/A) | Status: ACCEPT | Contar números por estrofa y sumar una progresión aritmética. | **Pendiente.** Enunciado oficial leído; no se localizó editorial escrito en las páginas del organizador. |
| 241 · [B. Barrio World](https://codeforces.com/gym/106552/problem/B) | Status: ACCEPT; Durante: Yo di toda la idea, Jorge la implemento, la idea no estuvo trivial peor tampoco dificl | Saltos sobre huecos con energía acumulada al correr. | **Pendiente.** Tu autoría conceptual es explícita; falta verificar la estrategia óptima en una fuente de solución. |
| 242 · [C. Cards](https://codeforces.com/gym/106552/problem/C) | Status: ACCEPT | Ventana sin repetidos y máximo dinámico tras eliminaciones de prefijo. | **Pendiente.** Tema deducido del enunciado; falta editorial oficial consultable. |
| 243 · [D. Dubious Dates](https://codeforces.com/gym/106552/problem/D) | Status: ACCEPT; Detalles: SO EASY | Detectar ambigüedad al intercambiar día y mes. | **Pendiente.** Enunciado leído; falta editorial oficial consultable. |
| 244 · [E. Exploring the Terrain](https://codeforces.com/gym/106552/problem/E) | Status: ACCEPT | Simulación simultánea de vecindarios de extracción y cancelación de intersecciones. | **Pendiente.** Enunciado leído; falta editorial oficial consultable. |
| 246 · [G. Garment Groups](https://codeforces.com/gym/106552/problem/G) | Status: ACCEPT | Conteo de pinzas compartidas en grupos de camisetas. | **Pendiente.** Enunciado leído; falta editorial oficial consultable. |
| 248 · [I. Interlingual Intermediaries](https://codeforces.com/gym/106552/problem/I) | Status: ACCEPT | Caminos mínimos entre idiomas, con pocos idiomas y muchas consultas entre hablantes. | **Pendiente.** La reducción de entidades necesita contraste con la solución oficial y sus límites. |
| 249 · [J. Just the Betas](https://codeforces.com/gym/106552/problem/J) | Status: ACCEPT | Elegir un divisor que cubra la mayor cantidad de valores; conteo de múltiplos. | **Pendiente.** Tema derivado del enunciado; falta verificar el enfoque oficial. |
| 253 · [N. N-Checkers](https://codeforces.com/gym/106552/problem/N) | Status: ACCEPT | Búsqueda de secuencias de capturas en un tablero de damas. | **Pendiente.** No dar por eficiente una búsqueda exhaustiva sin la justificación del límite. |
| 254 · [O. Operations in Order](https://codeforces.com/gym/106552/problem/O) | Status: ACCEPT; Detalles: SO EASY | Componer sumas y multiplicaciones como una transformación afín. | **Pendiente.** Reducción derivada del enunciado; editorial no localizado para cerrar la evaluación. |


### 23. Brasil 2026 · primera fase / GP México, tercera fecha

Fuentes: [Enunciados](https://codeforces.com/gym/106679/attachments/download/39242/contest-en-onesided.pdf).

**Editorial no localizado.** Se consultaron el Gym, el enunciado y el [sitio oficial del concurso](https://scorelatam.naquadah.com.br/subbr-2026/). La evaluación de los cinco candidatos queda pendiente de una fuente de solución.

| Registro / problema | Evidencia en el CSV | Técnica subyacente | Encaje y razón |
| --- | --- | --- | --- |
| 255 · [A. High Frequency](https://codeforces.com/gym/106679/problem/A) | Status: ACCEPT | Sumas prefijas del desequilibrio entre compras y ventas. | **Pendiente.** Enunciado leído; no se localizó editorial oficial del concurso. |
| 257 · [C. Exchange Rate](https://codeforces.com/gym/106679/problem/C) | Status: ACCEPT; Detalles: so easy | Comparar precio local con precio convertido. | **Pendiente.** Enunciado leído; no se localizó editorial oficial del concurso. |
| 258 · [D. Dragons in Harmony](https://codeforces.com/gym/106679/problem/D) | **Autoría dudosa.** Status: ACCEPT; Detalles: ayduae a jorge con unas formulas y encontrar un error debugeando | Simetrías del rectángulo o cuadrado que conservan las celdas libres. | **Pendiente.** Editorial no localizado; tu aporte se describe como fórmulas y depuración, sin precisar la idea principal. |
| 263 · [I. Inside the Guinea Pig Playpen](https://codeforces.com/gym/106679/problem/I) | Status: ACCEPT | Resolver dependencias de asistencia y barrer intervalos ponderados de ocupación. | **Pendiente.** Enunciado leído; falta contraste con editorial oficial. |
| 265 · [K. Contingency](https://codeforces.com/gym/106679/problem/K) | Status: ACCEPT; Detalles: easy | Peor caso por el último tipo de pieza que alcanza su cuota. | **Pendiente.** Posible cota extremal directa; no se cierra la evaluación sin solución oficial consultada. |


## Precisiones que afectan a la selección

### The Brega Game: alternativa sin consultas generales de máximos

El editorial caracteriza la victoria del primer jugador: gana si la longitud es par o si el máximo del intervalo está en uno de sus extremos. Su implementación sugerida usa consultas de máximos. A partir de **esa condición**, se obtiene una alternativa propia más ajustada a la serie:

- `siguienteMayor[l] > r` equivale a que el extremo izquierdo sea el máximo de `[l,r]`.
- `anteriorMayor[r] < l` equivale a que lo sea el extremo derecho.

Los valores son distintos. Por tanto, basta encontrar el primer elemento mayor en cada dirección, con dos recorridos y pilas monótonas. El preprocesamiento cuesta O(N) y cada consulta O(1). La equivalencia anterior justifica el reemplazo: no se necesita conocer el máximo interior. Esta variante es una **deducción de este análisis**, no una atribución al editorial. Se comprobó contra la condición de máximos en todas las permutaciones de longitudes 1 a 8 y sus intervalos. La prueba del juego procede del [editorial oficial, problema J](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf).

### The Scale Riddle: la cota de información necesita una construcción válida

El argumento ternario requiere poner la misma cantidad de prendas en ambos platos; de lo contrario, el desequilibrio podría deberse al número de prendas. Se pueden elegir dos grupos iguales y dejar un tercero de tamaño parecido. Para m candidatos, tomar en cada plato `ceil((m-1)/3)` deja los tres tamaños a lo sumo `ceil(m/3)`. Así se sostiene la reducción y la cota de consultas. Esta precisión explicita un detalle necesario de la construcción del [editorial, problema E](https://codeforces.com/gym/106667/attachments/download/39179/editorial-en.pdf).

### No toda DP ni toda estructura auxiliar contradicen el perfil

Fast XORting, Jewels Building y Erratic Lights se retienen por la reducción que hace posible su algoritmo. Chaotic Construction se aparta porque el manejo de posiciones bloqueadas constituye casi toda la solución. El filtro tampoco prohíbe una deque o una pila monótona cuando solo implementan una observación ya demostrada.

### Los problemas pequeños no son automáticamente buenos episodios

Demand for Cycling y Just Half is Enough tienen implementaciones mínimas, pero contienen una prueba generalizable. João João o Alphabet Chocolate dejan muy poco espacio entre leer el enunciado y programarlo. La distinción es la densidad de razonamiento, no la longitud del código.

## Dudas de autoría que permanecen abiertas

| Registro | Problema | Qué falta aclarar |
| ---: | --- | --- |
| 19 | K Subsequences | «ayudar» no especifica si aportaste el invariante central. |
| 34 | GCD | «Jorge, yo ayuda» no distingue aporte conceptual de apoyo. |
| 92 | Judgmental Crowd | Leer el enunciado no acredita por sí solo la idea principal. |
| 181 | Index Case | «Idea: yp y jorge» parece una errata por «yo», pero no consta aceptación ni upsolve. |
| 193 | Group forming | «Le ayudé a Rogelio» no identifica el tipo de ayuda. |
| 258 | Dragons in Harmony | Hay ayuda con fórmulas y depuración; no queda claro quién desarrolló la clasificación de simetrías. |

Estos seis registros fueron investigados para no perder candidatos, pero no se presentan como resolución conceptual propia confirmada. K Subsequences no entra en la primera selección priorizada por esta razón.

## Registros excluidos por autoría

Las siguientes exclusiones son anteriores al filtro temático: no significan que el problema sea malo para la serie. Se conservan las notas para que la interpretación sea auditable.

| Registro | Concurso / problema | Evidencia y motivo |
| ---: | --- | --- |

| 20 | SEERC 2023 · M. Max Minus Min | Status: ACCEPT; Durante: Jorge |
| 36 | Kunming 2024 · J. Just another Sorting Problem | Status: ACCEPT; Durante: Rogelio |
| 38 | Kunming 2024 · M. Matrix Construction | Status: ACCEPT; Durante: Jorge y Rogelio |
| 56 | GCPC 2025 · F. Fair and Square | Status: ACCEPT; Durante: Rogelio; Detalles: solo le ayude a rebotar ideas |
| 61 | GCPC 2025 · K. Karlsruhe Skyline | Status: ACCEPT; Durante: Jorge |
| 62 | GCPC 2025 · L. Labour Laws | Status: ACCEPT; Durante: Rogelio; Detalles: Era yo pero no me salio asi que Rogelio hizo fuerza bruta |
| 76 | CERC 2010 · C. Casting Spells | Status: ACCEPT Nota general del bloque: «hasta donde sé este se lo hizo todito Jorge solo».  |
| 77 | CERC 2010 · D. Defense Line | Status: ACCEPT Nota general del bloque: «hasta donde sé este se lo hizo todito Jorge solo».  |
| 78 | CERC 2010 · E. Enter The Dragon | Status: ACCEPT Nota general del bloque: «hasta donde sé este se lo hizo todito Jorge solo».  |
| 79 | CERC 2010 · G. Game | Status: ACCEPT Nota general del bloque: «hasta donde sé este se lo hizo todito Jorge solo».  |
| 90 | Regional Latinoamericano 2025–2026 · H. Harder Horizons | Status: ACCEPT; Durante: rogelio; Upsolve: ★ |
| 97 | NEERC 2016 · A. Abbreviation | Status: ACCEPT; Durante: Jorge |
| 113 | NWERC 2025 · A. Arcade Crane | Status: solo ideas; Durante: Jorge, al final "le ayude" pero lo hizo solo |
| 143 | GCPC 2022 · A. Alternative Architecture | Status: ACCEPT; Durante: Rogelio creo |
| 147 | GCPC 2022 · E. Enjoyable Entree | Status: ACCEPT; Durante: Jorge |
| 151 | GCPC 2022 · I. Improving IT | Status: ACCEPT; Durante: Rogelio |
| 162 | GP México 2026 · primera fecha · B. Bad LaTeX | Status: ACCEPT; Durante: Rogellio |
| 166 | GP México 2026 · primera fecha · F. F(x,l,r) | Detalles: Upsolveado por Jorge |
| 168 | GP México 2026 · primera fecha · H. Hidden Symmetry of Valdris | Detalles: Upsolveado por Jorge |
| 171 | GP México 2026 · primera fecha · K. Kernel of the Disks | Status: WA, casi; Durante: Roegelio Idea, Jorge Idea; Detalles: La idea e implementacion de rogelio si estaban bien, solo hubo unos errorcitos |
| 172 | GP México 2026 · primera fecha · L. Legendary Sort | Status: La idea de jorge estaba correcta; Durante: Jorge idea; Detalles: La idea de Jorge si estaba bien |
| 177 | GCPC 2021 · E. Excursion to Porvoo | Status: ACCEPT; Durante: Jorge |
| 198 | GP México 2026 · segunda fecha · L. Landau's Fourth Problem | Detalles: upsolveado por Jorge (creo) |
| 211 | II SBC São Paulo Programming Marathon · A. After party in Campinas | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 212 | II SBC São Paulo Programming Marathon · B. Metro ticket | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 213 | II SBC São Paulo Programming Marathon · C. World capital of pizza | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 214 | II SBC São Paulo Programming Marathon · D. Drawing SP | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 218 | II SBC São Paulo Programming Marathon · H. Driving restriction schedule | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 219 | II SBC São Paulo Programming Marathon · I. Digit insertion | Status: ACCEPT Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 223 | II SBC São Paulo Programming Marathon · M. Multi-word | Upsolve: ★; Observaciones: la idea de la binaria con Hash salio de Jorge, yo solo hice posible el calculo de los hash, y le cambie el codigo a la binaria de Jorge Nota general del registro 212: «Básicamente no hice nada durante el contest».  Observaciones: la idea de la binaria con Hash salio de Jorge, yo solo hice posible el calculo de los hash, y le cambie el codigo a la binaria de Jorge |
| 224 | II SBC São Paulo Programming Marathon · N. Reactivity levels | Status: ACCEPT; Durante: lo hizo Rogelio, mi idea no funciono; Upsolve: ★ Nota general del registro 212: «Básicamente no hice nada durante el contest».  |
| 230 | Maratona Nordestina 2026 · F. Escaping the Sun | Status: ACCEPT; Durante: Rogelio |
| 235 | Maratona Nordestina 2026 · K. Karamelos at São João | Status: ACCEPT; Durante: Jorge |
| 245 | XIII Maratona Mineira 2026 · F. Food Blockade | Status: ACCEPT; Durante: Jorge lo hizo, le ayude a debugear |
| 259 | Brasil 2026 · primera fase / GP México, tercera fecha · E. Network Editing | Status: ACCEPT; Durante: ROGELIO |
| 260 | Brasil 2026 · primera fase / GP México, tercera fecha · F. Flower | Status: ACCEPT; Durante: ROGELIO |
| 267 | Brasil 2026 · primera fase / GP México, tercera fecha · M. Microwave | Status: ACCEPT; Durante: Jorge |

## Registros sin evidencia suficiente de resolución propia

Los siguientes 77 registros no entraron en el conjunto candidato: no reúnen las condiciones documentadas de resolución/idea propia ni una señal suficiente de upsolve. No se les asigna tema nuevo ni veredicto pedagógico. Si aparece evidencia adicional, deben pasar por la misma investigación de enunciado y solución.

| Concurso | Registros / problemas |
| --- | --- |

| Brasil 2025 · primera fase / GP México, tercera fecha | 10 · L. LLMs |
| SEERC 2023 | 16 · E. Eliminate Tree |
| NWERC 2022 | 25 · D. Delft Distance; 26 · G. Going in Circles; 27 · H. High-quality Tree; 29 · J. Justice Served |
| Kunming 2024 | 33 · E. Extracting Weights; 37 · L. Last Chance: Threads of Despai |
| NCPC 2025 | 42 · B. Bohemian Bookshelf |
| GCPC 2025 | 52 · B. Bustling Busride; 55 · E. Engineering Excellence; 59 · I. Island Urbanism |
| Northwestern Russia Regional 2024 | 67 · D. Defective Script; 69 · H. Hanoi Towers Reloaded; 73 · L. Longest Common Substring |
| CERC 2010 | 80 · I. Insults |
| Regional Latinoamericano 2025–2026 | 83 · A. Apple Pie; 84 · B. Balanced Balloons; 85 · C. Clean Streets; 86 · D. Displaying Decimals; 87 · E. Emergency Rations; 89 · G. Gridoland Power Gauge; 91 · I. Infiltration Route; 94 · L. Lonely Creatures |
| NEERC 2016 | 98 · B. Binary Code; 99 · E. Expect to Wait; 101 · H. Hard Refactoring |
| Manila 2025 | 111 · M. Web Delivery |
| NWERC 2025 | 114 · B. Bisecting Bargain; 115 · C. Canal Crossing |
| Latin America Championship 2026 | 124 · A. Ants on a Ring; 126 · D. Dropshipping; 130 · I. Inversion Game |
| Dhaka 2025 | 134 · A. Mission Hexa; 136 · E. Love Marriage |
| GCPC 2022 | 144 · B. Breeding Bugs; 148 · F. Formula Flatland; 149 · G. Guessing Game; 152 · J. Jesting Jabberwocky; 155 · M. Mirror Madness |
| GCPC 2021 | 176 · D. Decrypting Zodiac; 178 · F. Flappy Bird; 182 · J. Joined Sessions; 184 · L. Looking for Waldo; 186 · N. Natural Navigation |
| GP México 2026 · segunda fecha | 192 · F. Forever in love; 196 · J. Jorge likes "sum over all subarrays" problems; 197 · K. K Vertices |
| SWERC 2025 | 201 · C. Chamber of Secrets 2; 205 · G. Git Gud; 206 · H. Hyper Smawk Bros; 207 · I. Isaac's Queries; 209 · K. Keygen 3; 210 · L. LFS |
| II SBC São Paulo Programming Marathon | 215 · E. Space emergency; 216 · F. Farming Aura; 217 · G. Parade Management; 220 · J. Playing with intervals; 221 · K. Knight number; 222 · L. Left or right side |
| Maratona Nordestina 2026 | 225 · A. Arretada Removals; 227 · C. Youth Divisions; 232 · H. Cordel Stories; 233 · I. Incredible XORlandia; 237 · M. The World's Biggest São João; 238 · N. Did You See My Album?; 239 · O. Operation Mandacaru |
| XIII Maratona Mineira 2026 | 247 · H. Heritage Hunt; 250 · K. Kampo Minesweeper; 251 · L. Loading the Dish Rack; 252 · M. Moving Sticks |
| Brasil 2026 · primera fase / GP México, tercera fecha | 256 · B. Sequences; 261 · G. Genes; 262 · H. Traffic Lights; 264 · J. Phone Lines; 266 · L. Maze; 268 · N. Nlogônia's Keys |

## Qué falta para cerrar la investigación completa

| Bloque | Candidatos nuevos pendientes | Evidencia faltante |
| --- | ---: | --- |
| Regional Latinoamericano 2025–2026 | 3 | Editorial o soluciones de referencia de F, J y K. |
| México 2026, primera fecha | 6 | Contenido consultable del video oficial o solución escrita equivalente. |
| México 2026, segunda fecha | 8 | Contenido consultable del video oficial o solución escrita equivalente. |
| Mineira 2026 | 10 | Editorial o códigos oficiales que permitan contrastar técnica y complejidad. |
| Brasil 2026, primera fase | 5 | Editorial o soluciones del jurado. |
| **Total** | **32** | **No tienen aún veredicto temático definitivo.** |

Además, las cuatro propuestas nuevas contrastadas con código del jurado del campeonato latinoamericano de 2026 requieren desarrollar su prueba pedagógica: Booksort, Eye Exam, Fun with Balls y Jaime’s Palace. Para GATA-CAT esa explicación ya existe en la serie. La evidencia de jurado se conserva separada de la evidencia de editorial.

Se puede empezar a preparar los guiones de la primera selección con las fuentes ya consultadas. Los candidatos pendientes permanecen en el inventario para evitar que una dificultad de acceso documental se convierta en una exclusión temática arbitraria.
