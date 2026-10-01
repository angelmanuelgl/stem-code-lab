# Guion de voz — GATA-CAT

## Escena 01: Un millón de gatos en una cadena de quinientas letras

> “[TRIGGER_1] Imagina que te entregan dos números y te piden fabricar una cadena de ADN. Uno cuenta cuántas veces podemos encontrar GATA. El otro, cuántas veces podemos encontrar CAT. Los números pueden llegar a un millón. Pero la cadena que construyamos no puede superar las quinientas letras. [Pausa.] ¿Cómo metemos un millón de gatos en un espacio tan pequeño?
> [TRIGGER_2] Tenemos cuatro letras disponibles: C, G, A y T. Podemos elegir su orden y repetirlas. Nos llegarán hasta mil solicitudes, y cada una trae primero el objetivo de GATA y después el de CAT. Los llamaré objetivo G y objetivo C; esos nombres se refieren a cantidades de apariciones, no a cuántas letras G o C vamos a escribir.
> [TRIGGER_3] No buscamos la cadena más corta del universo. Nos basta una cadena no vacía que acierte exactamente ambos números y tenga como máximo quinientos caracteres. Esa diferencia nos da libertad: podemos buscar una construcción fácil de controlar, aunque otra fuera un poco más breve.
> [TRIGGER_4] El truco que vamos a descubrir depende de una palabra: encontrar. Aquí no significa leer letras pegadas. Podemos saltarnos letras intermedias. Antes de construir nada, necesitamos entender cómo se cuentan esas elecciones. Porque una sola cadena puede esconder muchas más apariciones de las que parece.”

## Escena 02: La misma palabra, cuatro elecciones distintas

> “[TRIGGER_1] Miremos esta cadena: C, A, A, T, T. Numeramos sus posiciones del uno al cinco. Si exigimos letras consecutivas, no aparece CAT: después de C vienen dos aes. Pero si podemos saltarnos posiciones, la historia cambia. Tenemos una C, dos opciones para la A y dos opciones para la T.
> [TRIGGER_2] Primera elección: posiciones uno, dos y cuatro. Segunda elección: uno, dos y cinco. Escriben la misma palabra, CAT, pero usan una T diferente; por eso cuentan como dos apariciones. No estamos contando palabras distintas. Estamos contando maneras distintas de elegir posiciones en orden.
> [TRIGGER_3] Tercera elección: uno, tres y cuatro. Cuarta elección: uno, tres y cinco. Son todas: la C está fija, elegimos una de las dos aes y después una de las dos tes. Dos por dos: cuatro. Cada arco siempre avanza hacia la derecha; saltar está permitido, retroceder no.
> [TRIGGER_4] La regla formal para CAT pide tres índices estrictamente crecientes, con las letras C, A y T en esas posiciones. Estrictamente significa que una posición no se puede usar dos veces. Y esta es la primera pista: no necesitamos escribir una copia separada de cada gato. Muchas apariciones pueden compartir letras.”

## Escena 03: Las dos aes de GATA tienen papeles diferentes

> “[TRIGGER_1] Ahora probemos G, A, T, A, T, A. La G está en la posición uno. Para formar GATA necesitamos una A, luego una T y luego otra A. Las dos aes deben ocupar posiciones diferentes, y la segunda debe quedar después de la T. No basta con tomar cualquier par de aes.
> [TRIGGER_2] Si elegimos la T de la posición tres, antes de ella sólo podemos usar la A de la posición dos. Después tenemos dos opciones: la A de la posición cuatro o la de la seis. Obtenemos las elecciones uno, dos, tres, cuatro; y uno, dos, tres, seis.
> [TRIGGER_3] Si elegimos la T de la posición cinco, antes podemos tomar la A de la posición dos o la de la cuatro; después sólo queda la A de la seis. Aparecen uno, dos, cinco, seis; y uno, cuatro, cinco, seis. Dos más dos: cuatro apariciones.
> [TRIGGER_4] ¿Por qué no vale poner la A de la seis como primera A? [Pausa.] Porque ya no hay una T y otra A a su derecha. En CAT elegimos un par ordenado A, T. En GATA elegimos un triple ordenado A, T, A, después de la G inicial. Esa diferencia va a producir dos familias de números distintas.”

## Escena 04: Copiar gatos fabrica gatos que no habíamos pedido

> “[TRIGGER_1] El primer intento sería escribir una copia de CAT por cada aparición que queremos. Si pedimos dos, escribimos CATCAT. Son sólo seis letras. Parece perfecto. Pero nuestra definición permite saltar entre las copias. [Pausa.] ¿Cuántos gatos aparecen realmente?
> [TRIGGER_2] Desde la C de la posición uno podemos elegir A en dos y T en tres, o A en dos y T en seis, o A en cinco y T en seis. Son tres apariciones. Las dos últimas atraviesan la separación que nosotros imaginábamos entre las copias.
> [TRIGGER_3] Desde la C de la posición cuatro sólo queda A en cinco y T en seis. Una aparición más. En total, cuatro. Queríamos dos y obtuvimos cuatro. La cadena no conoce nuestras etiquetas de primera copia y segunda copia: sólo conoce el orden de sus posiciones.
> [TRIGGER_4] Y repetir una copia por unidad tampoco cabe cuando el objetivo llega a un millón. Tenemos dos obstáculos: demasiadas letras y apariciones que se mezclan. La construcción que buscamos tiene que multiplicar las elecciones sin perder el control de esos cruces. Necesitamos diseñar la interacción, no ignorarla.”

## Escena 05: El espacio de búsqueda crece, y el pasado importa

> “[TRIGGER_1] Podríamos probar todas las cadenas. En cada posición tenemos cuatro decisiones. Para longitud uno hay cuatro posibilidades; para longitud dos, dieciséis; para longitud tres, sesenta y cuatro. Cada nueva letra multiplica por cuatro. Para longitud L son cuatro elevado a L. Y verificar una candidata no elimina esa explosión.
> [TRIGGER_2] Otra tentación es buscar sobre los dos contadores: cuántos CAT llevo y cuántos GATA llevo. Hasta un millón en cada eje significa del orden de un billón de pares, diez elevado a doce. Pero incluso si tuviéramos esa memoria, esos dos números no describen todo lo que necesitamos saber.
> [TRIGGER_3] Compara los prefijos CA y CT. Ninguno contiene todavía CAT ni GATA: ambos tienen contadores cero, cero. Añadimos la misma letra T. CA se convierte en CAT y crea una aparición. CT se convierte en CTT y no crea ninguna. El mismo par de contadores y la misma acción producen resultados diferentes.
> [TRIGGER_4] Faltaba información sobre patrones incompletos, como CA, que una letra futura puede terminar. La pregunta cambia: ¿podemos elegir una familia de cadenas donde sepamos de antemano cuánto aporta cada letra especial? [Pausa.] En lugar de explorar cualquier secuencia, vamos a diseñar una estructura que podamos contar.”

## Escena 06: Un esqueleto y dos tipos de interruptores

> “[TRIGGER_1] Fijemos primero una cadena que sólo alterna A y T: A, T, A, T, A, T. Es nuestro esqueleto. Como no contiene C ni G, todavía no hay CAT ni GATA. Pero ya contiene pares A, T y triples A, T, A que una letra situada antes podría completar.
> [TRIGGER_2] Pon una C delante. Cada par A, T que pueda elegirse después se convierte en un CAT. Pon una G delante. Cada triple A, T, A que pueda elegirse después se convierte en un GATA. La C necesita dos elecciones posteriores; la G necesita tres.
> [TRIGGER_3] ¿Qué ocurre si insertamos también otras ces y ges entre los pares? [Pausa.] Al escoger A y T podemos saltarlas. No añaden nuevas aes ni nuevas tes. Si dejamos fijo el esqueleto, el repertorio de elecciones A, T y A, T, A no cambia por esas inserciones.
> [TRIGGER_4] No hemos resuelto el problema todavía. Falta saber cuánto vale una C o una G en cada hueco, y cómo combinar esos valores para llegar a cualquier objetivo. Empecemos por una sola C delante de i pares. Vamos a construir la fórmula a partir del dibujo.”

## Escena 07: Los gatos forman un triángulo

> “[TRIGGER_1] Etiquetemos los tres pares: A uno, T uno; A dos, T dos; A tres, T tres. Si la C está delante, una aparición de CAT queda completamente determinada al elegir una A y una T posteriores, con la A antes de la T.
> [TRIGGER_2] Fijemos T uno. Sólo A uno queda antes: una elección. Fijemos T dos. Podemos tomar A uno o A dos: dos elecciones. Fijemos T tres. Podemos tomar A uno, A dos o A tres: tres elecciones. No hemos contado nada dos veces, porque cada aparición tiene una T final única.
> [TRIGGER_3] Una más dos más tres: seis. Podemos dibujar una casilla por elección. La primera fila tiene una, la segunda dos y la tercera tres. Por eso aparece un triángulo. La cadena C, A, T, A, T, A, T tiene seis CAT, aunque sólo hemos escrito una C.
> [TRIGGER_4] Para i pares, la fila de T b contiene b elecciones. La condición es a menor o igual que b: A a está antes de T b incluso cuando a y b son iguales, porque dentro de cada par la A viene primero. Al sumar las filas, obtenemos uno más dos y así hasta i. Este será el peso T sub i de una C.”

## Escena 08: De un triángulo a una fórmula

> “[TRIGGER_1] Llamemos S a la suma uno más dos hasta i. Dibujamos una segunda copia del triángulo, la giramos y la encajamos con la primera. En cada fila, las dos cantidades suman i más uno. Hay i filas. Las dos copias juntas contienen i por i más uno casillas.
> [TRIGGER_2] Como juntamos dos triángulos iguales, dos S es i por i más uno. Dividimos entre dos. El peso de una C delante de i pares es i por i más uno, entre dos. Para tres pares obtenemos tres por cuatro entre dos: seis. Para uno obtenemos uno; para dos, tres; para cuatro, diez.
> [TRIGGER_3] Hay otra forma de ver el mismo número. Una elección A a, T b cumple a menor o igual que b. Cambiemos su etiqueta a la pareja a, b más uno. Ahora son dos números distintos en orden creciente, elegidos entre uno y i más uno. Al revés, si nos dan dos números u menor que v, recuperamos a igual a u y b igual a v menos uno.
> [TRIGGER_4] Esa correspondencia es exacta en los dos sentidos. Por eso también podemos escribir el binomial i más uno sobre dos: el número de maneras de elegir dos elementos distintos sin importar su orden. No es una fórmula decorativa. Es el mismo triángulo, visto como una colección de parejas.”

## Escena 09: Para GATA, la T queda entre dos elecciones

> “[TRIGGER_1] Sustituyamos la C inicial por una G. Necesitamos elegir A, T, A a su derecha. Fijar la T sigue siendo útil, pero ahora hay dos decisiones: una A antes y una A después. Probemos primero tres pares AT, que terminan en T tres.
> [TRIGGER_2] Para T uno, antes está A uno y después están A dos y A tres. Una opción por dos opciones: dos triples. Son A uno, T uno, A dos; y A uno, T uno, A tres. Para T dos, antes hay dos aes y después sólo A tres: otros dos triples, A uno, T dos, A tres; y A dos, T dos, A tres.
> [TRIGGER_3] T tres tiene tres aes anteriores, pero ninguna A después. Tres por cero: no añade nada. En total, dos más dos más cero: cuatro. La G inicial convierte esos cuatro ATA en cuatro GATA. El esqueleto solo no contiene GATA: contiene las continuaciones que una G puede completar.
> [TRIGGER_4] Con i pares, T b tiene b aes anteriores y i menos b aes posteriores. Su aporte es b por i menos b. Las condiciones son a menor o igual que b, y b estrictamente menor que c. Al sumar sobre la T elegida, el peso V sub i es la suma de b por i menos b, desde b igual a uno hasta i.”

## Escena 10: Un triple escondido detrás de cada GATA

> “[TRIGGER_1] La suma anterior se puede cerrar sin adivinar una identidad. A cada triple a, b, c que cumple a menor o igual que b y b menor que c, asignemos el triple a, b más uno, c más uno. Sus tres números son estrictamente crecientes y están entre uno e i más uno.
> [TRIGGER_2] Para nuestros tres pares, las cuatro elecciones se convierten en uno, dos, tres; uno, dos, cuatro; uno, tres, cuatro; y dos, tres, cuatro. Son justamente todas las maneras de elegir tres números del conjunto uno, dos, tres, cuatro. Ninguna elección se repite y ninguna falta.
> [TRIGGER_3] ¿Podemos volver? Sí. Si nos dan u menor que v menor que w, tomamos a igual a u, b igual a v menos uno y c igual a w menos uno. La primera desigualdad garantiza a menor o igual que b. La segunda garantiza b menor que c. Y w como máximo i más uno garantiza c como máximo i. La correspondencia no pierde información.
> [TRIGGER_4] Para elegir tres elementos distintos en orden arbitrario hay i más uno opciones para el primero, i para el segundo e i menos uno para el tercero. Cada grupo de tres aparece en sus seis órdenes posibles. Dividimos entre seis. Así obtenemos V sub i: i menos uno, por i, por i más uno, entre seis; o el binomial i más uno sobre tres.
> [TRIGGER_5] Para i igual a uno no hay tres números que elegir: el peso es cero. Para dos, el peso es uno. Para tres, cuatro. Para cuatro, diez. Ya tenemos las dos familias: los pesos de C crecen como triángulos, y los de G como elecciones de tres elementos. Una G bien colocada puede generar muchísimas apariciones.”

## Escena 11: Construir las tablas mirando el último par

> “[TRIGGER_1] Las fórmulas también se pueden descubrir haciendo crecer el esqueleto. Partimos de tres pares, con seis AT y cuatro ATA. Añadamos A cuatro, T cuatro. Los pares AT antiguos siguen existiendo. La nueva T cuatro puede combinarse con cualquiera de las cuatro aes: aparecen cuatro pares nuevos.
> [TRIGGER_2] Para los triples ATA, fíjate primero en la nueva A cuatro, antes de escribir la T cuatro. Puede cerrar cada uno de los seis pares AT del prefijo anterior. Nacen seis triples: A uno, T uno, A cuatro; A uno, T dos, A cuatro; A dos, T dos, A cuatro; A uno, T tres, A cuatro; A dos, T tres, A cuatro; y A tres, T tres, A cuatro.
> [TRIGGER_3] La T cuatro no cierra ningún ATA nuevo: todavía no hay una A después de ella. Por tanto, pasamos de seis a diez pares AT y de cuatro a diez triples ATA. El orden de llegada explica por qué en la segunda cuenta usamos los pares del prefijo anterior, no los del esqueleto ya ampliado.
> [TRIGGER_4] En general, T sub i es T sub i menos uno más i. Y V sub i es V sub i menos uno más T sub i menos uno, que vale i por i menos uno entre dos. Empezamos con ambas tablas en cero para el esqueleto vacío. Esas dos actualizaciones generan todos los pesos hasta el índice que decidamos usar.”

## Escena 12: Por qué las contribuciones se suman sin mezclarse

> “[TRIGGER_1] Probemos una cadena con varias letras especiales: C, G, A, T, C, A, T. La primera C tiene dos pares AT a su derecha y aporta tres CAT. La segunda C tiene un solo par y aporta uno. Las apariciones pueden compartir aes y tes, pero nunca pueden tener dos ces iniciales: cada CAT elige exactamente una.
> [TRIGGER_2] Clasifiquemos todas las apariciones por la posición de su C. En la primera caja están las elecciones uno, tres, cuatro; uno, tres, siete; y uno, seis, siete. En la segunda está cinco, seis, siete. Las cajas no se superponen. Tres más uno da cuatro.
> [TRIGGER_3] La G de la posición dos tiene dos pares AT a su derecha. Su único ATA es A en tres, T en cuatro, A en seis. Crea un GATA, con posiciones dos, tres, cuatro, seis. La C intermedia se salta. Agregar ces no inventa nuevos GATA, y agregar ges no inventa nuevos CAT.
> [TRIGGER_4] El argumento funciona para cualquier cantidad de inserciones. Toda aparición CAT pertenece a la caja de su única C inicial; toda aparición GATA, a la de su única G inicial. Otras ces y ges no modifican las elecciones de A y T de un sufijo. Por eso multiplicamos cada peso por el número de letras en su hueco y después sumamos. No hay un producto escondido entre cantidades de C y G.”

## Escena 13: Cambiar números por letras con peso

> “[TRIGGER_1] Los primeros pesos de C son uno, tres, seis, diez y quince. Los de G son cero, uno, cuatro, diez y veinte. El índice dice cuántos pares AT quedarán a la derecha de esa letra. Podemos usar varias letras en un mismo hueco: cada una repite la misma contribución.
> [TRIGGER_2] Miremos los objetivos que usaremos de ejemplo: G igual a cinco y C igual a ocho. Para ocho CAT podemos pagar seis y luego uno y uno. Para cinco GATA, cuatro y uno. Eso sugiere poner una C y una G donde queden tres pares; otra G donde queden dos; y dos ces donde quede uno.
> [TRIGGER_3] Nuestra regla será tomar el peso más grande que quepa en el residuo, usarlo tantas veces como quepa y seguir hacia pesos menores. La moneda de valor uno garantiza que al final se puede pagar cualquier resto. Pero todavía debemos demostrar que no escribimos demasiadas letras.
> [TRIGGER_4] Tampoco debemos atribuirle una propiedad que no necesita. Con los pesos de C, doce se paga de forma voraz como diez más uno más uno: tres letras. Sin embargo, seis más seis usa dos. El greedy no siempre minimiza el número de ces. Lo que queremos probar es exactitud y una longitud dentro de quinientos, no optimalidad.”

## Escena 14: Planear desde el sufijo y escribir de izquierda a derecha

> “[TRIGGER_1] Vamos a reservar hasta ciento cuarenta y cuatro pares AT. Ese número se justificará cuando midamos la longitud; por ahora es nuestra capacidad de trabajo. Recorremos los huecos desde el que dejaría ciento cuarenta y cuatro pares a la derecha hasta el que deja uno.
> [TRIGGER_2] En el hueco de índice i colocamos primero todas las ces que quepan con peso T sub i, después todas las ges que quepan con peso V sub i, y luego escribimos un par AT. Para las ges sólo usamos índices desde dos, porque con un par el peso es cero.
> [TRIGGER_3] Parece que estamos contando letras que todavía no existen. Pero quedan planificadas: después de una inserción en i escribiremos el par de ese paso y los de los pasos i menos uno hasta uno. Son exactamente i pares. Así la decisión actual tiene el sufijo que promete su peso.
> [TRIGGER_4] En nuestro ejemplo, los objetivos son cinco GATA y ocho CAT. Para todo índice desde ciento cuarenta y cuatro hasta cuatro, el peso de C es al menos diez y el de G también es al menos diez. No cabe ninguna letra. Como aún no hemos empezado, omitimos esos pares iniciales. La primera decisión útil estará en el índice tres.”

## Escena 15: Primer hueco: pagar seis y cuatro

> “[TRIGGER_1] Estamos en el índice tres. El peso de C es seis y el de G es cuatro. Quedan ocho CAT y cinco GATA por producir. Aún no hemos escrito nada, pero ya sabemos que después de las letras de este hueco habrá tres pares AT.
> [TRIGGER_2] Una C cuesta seis. Cabe una vez en ocho y deja residuo dos. No cabe una segunda, porque necesitaríamos otros seis. Escribimos C y anotamos que sus seis apariciones se confirmarán cuando terminemos el sufijo. Asignar una contribución no significa que ya esté completa en el prefijo.
> [TRIGGER_3] Ahora una G cuesta cuatro. Cabe una vez en cinco y deja residuo uno. Escribimos G después de la C. La G no aumenta el número de CAT asignados, y la C no aumenta el de GATA. Nuestros residuos quedan G igual a uno, C igual a dos.
> [TRIGGER_4] Escribimos el par AT de este paso. El prefijo es CGAT y ya contiene un CAT: C, A, T. Ese uno visible no son los seis que asignamos a la C; los otros llegarán al extender la cadena. Todavía no hay ningún GATA, porque falta una A posterior a la T. Para evitar confundir ambas cuentas, el marcador principal muestra contribuciones asignadas; el conteo del prefijo lleva una etiqueta diferente.”

## Escena 16: Segundo hueco: otra G y un par que no se puede saltar

> “[TRIGGER_1] Bajamos al índice dos. Una C valdría tres, pero su residuo es dos: no cabe. No escribimos ninguna C. Una G vale uno, y su residuo es uno: cabe exactamente una. Escribimos esa G y dejamos el residuo G en cero.
> [TRIGGER_2] La nueva G tendrá dos pares AT a la derecha: el que escribiremos ahora y el del último paso. Sus elecciones forman un único GATA. La G anterior sigue teniendo planeados sus tres pares; insertar otra G no cambia esa promesa.
> [TRIGGER_3] Escribimos A y T. El prefijo es ahora CGATGAT. Las contribuciones asignadas son cinco GATA y seis CAT. Los residuos son G igual a cero y C igual a dos. Aún quedan dos ces por escribir y el último par AT.
> [TRIGGER_4] Observa que escribimos el par aunque sólo uno de los dos objetivos haya recibido una letra en este hueco. Y si no hubiéramos insertado ninguna, también tendríamos que escribirlo después de haber empezado. Es parte del sufijo que ya prometimos a las letras anteriores.”

## Escena 17: Último hueco: dos ces de valor uno

> “[TRIGGER_1] Llegamos al índice uno. El peso de C es uno y todavía faltan dos CAT. Escribimos una C: el residuo baja de dos a uno. Escribimos otra C: baja de uno a cero. Cada una tendrá el mismo último par AT a la derecha, pero son posiciones iniciales distintas y por eso aportan una aparición cada una.
> [TRIGGER_2] Para G, el peso en este índice es cero. No hay un ATA dentro de un solo par AT. No intentamos dividir entre cero ni repetir una resta de cero. Esta estación simplemente no permite insertar G. Además, su residuo ya quedó en cero en el paso anterior.
> [TRIGGER_3] Escribimos el último A y el último T. La cadena completa es C, G, A, T, G, A, T, C, C, A, T: CGATGATCCAT. Tiene once letras. Cada promesa de sufijo se ha cumplido: tres pares para las primeras letras, dos para la segunda G y uno para las dos ces finales.
> [TRIGGER_4] Los residuos terminaron en cero. La cuenta asignada de CAT es seis más uno más uno, igual a ocho. La de GATA es cuatro más uno, igual a cinco. Ahora sí, las contribuciones asignadas corresponden a apariciones completas. Vamos a comprobarlas directamente sobre las posiciones, sin confiar sólo en nuestra contabilidad.”

## Escena 18: Ver los ocho CAT, uno por uno

> “[TRIGGER_1] Numeremos la cadena final del uno al once. La primera C está en uno. Las aes posteriores están en tres, seis y diez; las tes, en cuatro, siete y once. Si terminamos en T cuatro, sólo podemos elegir A tres: posiciones uno, tres, cuatro.
> [TRIGGER_2] Si terminamos en T siete, podemos elegir A tres o A seis. Aparecen uno, tres, siete; y uno, seis, siete. Si terminamos en T once, podemos elegir A tres, A seis o A diez. Aparecen uno, tres, once; uno, seis, once; y uno, diez, once. La primera C aporta las seis elecciones de nuestro triángulo.
> [TRIGGER_3] La C de la posición ocho sólo puede usar A diez y T once: ocho, diez, once. La C de la posición nueve usa ese mismo par y produce nueve, diez, once. Son dos elecciones distintas, porque tienen una C inicial diferente. Compartir el final no las vuelve la misma aparición.
> [TRIGGER_4] Ya están las ocho, sin ninguna escondida fuera de la lista. Todo CAT debe comenzar en una de las tres ces que acabamos de revisar, y para cada una enumeramos todos los pares A, T ordenados de su sufijo. Seis más uno más uno. La cadena acierta el objetivo C igual a ocho.”

## Escena 19: Ver los cinco GATA, uno por uno

> “[TRIGGER_1] Las ges están en las posiciones dos y cinco. Para la G de la posición dos, si elegimos T cuatro, la primera A tiene que estar en tres y la última puede estar en seis o diez. Obtenemos dos, tres, cuatro, seis; y dos, tres, cuatro, diez.
> [TRIGGER_2] Si esa misma G elige T siete, la primera A puede estar en tres o seis y la última debe estar en diez. Obtenemos dos, tres, siete, diez; y dos, seis, siete, diez. T once no sirve: no hay una A después. La primera G aporta exactamente cuatro.
> [TRIGGER_3] Para la G de la posición cinco sólo hay una elección: A seis, T siete, A diez. Sus posiciones completas son cinco, seis, siete, diez. Las ces de ocho y nueve quedan entre la T y la última A, pero las podemos saltar. La cadena no exige que las cuatro letras queden juntas.
> [TRIGGER_4] Todo GATA comienza en una de estas dos ges. Hemos revisado las dos, y para cada una todas las tes posibles y las aes que quedan a sus lados. Cuatro más uno: cinco. La misma cadena produce ocho CAT y cinco GATA. No concatenamos dos respuestas: los dos objetivos comparten el mismo esqueleto.”

## Escena 20: La contabilidad que no puede perder una aparición

> “[TRIGGER_1] Pasemos del ejemplo a cualquier solicitud. En el hueco con i pares posteriores, llamemos a sub i al número de ces y b sub i al número de ges. Como cada una aporta lo mismo, ese hueco asigna a sub i por T sub i al objetivo CAT y b sub i por V sub i al objetivo GATA.
> [TRIGGER_2] En cada momento mantenemos una igualdad: el objetivo original es lo ya asignado más lo que falta. Al insertar una C, la parte asignada aumenta T sub i y el residuo C disminuye exactamente T sub i. El total no cambia. Para G ocurre la misma conservación con V sub i.
> [TRIGGER_3] También podemos agrupar todas las letras iguales de un hueco en una decisión. Si el residuo C es r, tomamos el cociente entero de r entre T sub i. La cantidad asignada es ese cociente por el peso, y el nuevo residuo es r menos esa cantidad: está entre cero y el peso menos uno. Para G hacemos esa división sólo cuando i es al menos dos.
> [TRIGGER_4] Cuando termina la cadena, las asignaciones se vuelven contribuciones reales. Por la partición según la letra inicial, el total CAT es la suma de todos los a sub i por T sub i. El total GATA es la suma de los b sub i por V sub i. La conservación demuestra que acertamos los objetivos si los residuos terminan en cero; ahora falta asegurar ese último paso.”

## Escena 21: Empezar tarde, pero no abandonar el esqueleto

> “[TRIGGER_1] Hay un detalle pequeño que sostiene toda la construcción. Antes de insertar la primera C o G, podemos omitir los pares AT de índices altos. No hay ninguna letra especial anterior que los necesite. Omitirlos sólo acorta una región que no aporta a nuestros objetivos.
> [TRIGGER_2] Después de la primera inserción, la situación cambia. Supongamos que pedimos cero GATA y seis CAT. En el índice tres insertamos una C de peso seis y los residuos ya quedan en cero. Aun así debemos escribir el AT de tres, el de dos y el de uno. La salida correcta es CATATAT.
> [TRIGGER_3] ¿Qué pasaría si nos detuviéramos al ver los residuos cero, o si saltáramos los huecos donde no insertamos nada? [Pausa.] Nos quedaría CAT. Esa C sólo tendría un par a su derecha y aportaría uno, no seis. La contabilidad prometió tres pares, pero la cadena habría entregado uno.
> [TRIGGER_4] Por eso mantenemos un estado de dos posibilidades: todavía no empezamos, o ya empezamos. Pasa al segundo estado cuando aparece la primera C o G, y nunca vuelve atrás. En ese estado, todos los pasos restantes emiten su par AT, aunque sus multiplicidades sean cero. Planificar un sufijo exige terminarlo.”

## Escena 22: Exactitud: el último peso elimina cualquier residuo

> “[TRIGGER_1] Las ces tienen una última oportunidad en el índice uno, donde el peso vale uno. Si el residuo C es r, escribimos r ces y restamos r unidades. Queda cero. Para las ges, la última oportunidad es el índice dos: V dos también vale uno. Cualquier residuo G se consume ahí.
> [TRIGGER_2] Ninguna resta es mayor que el residuo, porque sólo insertamos una letra cuando su peso cabe. Los residuos nunca se vuelven negativos. Tampoco dependemos de que los pesos sean mágicos o de que el greedy use pocas monedas: el valor uno basta para la exactitud.
> [TRIGGER_3] La salida completa respeta el número de pares posteriores de cada hueco. La partición por C o G inicial convierte las contribuciones en sumas exactas. Y la conservación de objetivos más residuos, ahora con los dos residuos en cero, nos da exactamente el número pedido de CAT y de GATA.
> [TRIGGER_4] Eso prueba que fabricamos las cantidades correctas. Pero podríamos haber usado demasiadas letras de valor uno. La pregunta decisiva que queda es: ¿qué tan rápido se reduce el residuo al tomar pesos grandes? [Pausa.] Ahora vamos a demostrar que la misma construcción cabe holgadamente en quinientos caracteres.”

## Escena 23: Medir la cadena por sus tres ingredientes

> “[TRIGGER_1] Una respuesta tiene tres ingredientes: las aes y tes del esqueleto, las ces insertadas y las ges insertadas. Con ciento cuarenta y cuatro pares como máximo, el primer ingrediente cuesta dos por ciento cuarenta y cuatro: doscientas ochenta y ocho letras.
> [TRIGGER_2] Si empezamos en un índice menor, usamos menos pares. Para la prueba nos permitimos cobrar los ciento cuarenta y cuatro completos: una cota conservadora vale para cualquier punto de inicio. Reservar capacidad no obliga a usarla toda.
> [TRIGGER_3] Ahora necesitamos acotar cuántas ces y cuántas ges inserta el greedy para objetivos desde cero hasta un millón. No basta con encontrar muchos ejemplos que funcionan. Queremos una desigualdad que cubra todos los números del intervalo, incluidos los que dejan residuos difíciles de pagar.
> [TRIGGER_4] La clave es la distancia entre dos pesos consecutivos. Después de tomar el mayor peso que cabe, el residuo cae por debajo de esa distancia. En los pesos triangulares, la distancia crece mucho más lentamente que el peso. En los de G ocurre algo parecido. Esa caída nos va a permitir cerrar la cuenta sin recorrer un millón de casos en la demostración.”

## Escena 24: El residuo CAT cae por debajo del índice siguiente

> “[TRIGGER_1] En el hueco ciento cuarenta y cuatro, una C aporta diez mil cuatrocientos cuarenta. Noventa y cinco veces ese peso da novecientos noventa y un mil ochocientos. Noventa y seis veces ya supera un millón. Así que en ese hueco pueden aparecer como máximo noventa y cinco ces.
> [TRIGGER_2] Después de usar todas las que caben, el residuo queda estrictamente por debajo de diez mil cuatrocientos cuarenta. Esa afirmación también vale si el objetivo era pequeño y no usamos ninguna. Lo importante para el siguiente paso no es el objetivo original, sino esta cota del resto.
> [TRIGGER_3] Elijamos ahora el mayor índice j cuyo peso triangular cabe en el residuo r. Por ser el mayor, r está entre T j incluido y T j más uno excluido. Restamos una sola C de peso T j. Entonces el nuevo residuo es menor que T j más uno menos T j.
> [TRIGGER_4] Escribamos ambos pesos: j más uno por j más dos, entre dos, menos j por j más uno, entre dos. Sacamos el factor j más uno y queda dos entre dos: j más uno. Así, una inserción nos deja un residuo menor que j más uno. Puede requerirse otra C en el mismo hueco; la desigualdad sigue siendo válida para el siguiente residuo. Ahora encadenemos ese descenso.”

## Escena 25: Cuatro caídas y dos unidades: como máximo 101 ces

> “[TRIGGER_1] Con un residuo menor que diez mil cuatrocientos cuarenta, el mayor índice posible es ciento cuarenta y tres. Una C deja menos de ciento cuarenta y cuatro. No necesitamos que siempre elija ese índice; cualquier índice menor produce una cota todavía mejor.
> [TRIGGER_2] Si el residuo es menor que ciento cuarenta y cuatro, el mayor índice que puede caber es dieciséis: T dieciséis vale ciento treinta y seis, y T diecisiete vale ciento cincuenta y tres. Otra C deja menos de diecisiete. Si el residuo es menor que diecisiete, el índice máximo es cinco: quince cabe, veintiuno no. Otra C deja menos de seis.
> [TRIGGER_3] Con residuo menor que seis, el índice máximo es dos: T dos vale tres, T tres vale seis. Una C deja menos de tres. Como el residuo es entero y no negativo, sólo puede quedar cero, uno o dos. Esas últimas unidades se pagan con como máximo dos ces de peso uno.
> [TRIGGER_4] Después de la tanda inicial hemos usado como máximo cuatro ces para esas cuatro caídas, y como máximo dos para el final. Si el residuo llega antes a cero, no hacemos las inserciones restantes. Sumamos noventa y cinco, más cuatro, más dos: como máximo ciento una ces. Esta es una cota para cualquier objetivo C hasta un millón.”

## Escena 26: Las ges reducen un cubo a un triángulo

> “[TRIGGER_1] En el hueco ciento cuarenta y cuatro, una G aporta cuatrocientos noventa y siete mil seiscientos cuarenta. Dos ges aportan novecientos noventa y cinco mil doscientos ochenta; tres superarían un millón. Por tanto, el primer hueco usa como máximo dos ges y deja un residuo menor que cuatrocientos noventa y siete mil seiscientos cuarenta.
> [TRIGGER_2] Buscamos otra vez el mayor peso que cabe, ahora V j. El residuo está entre V j y V j más uno. Al restar una G, el nuevo resto queda por debajo de V j más uno menos V j. La idea de la prueba es la misma conservación de un intervalo, pero la diferencia tiene otro tamaño.
> [TRIGGER_3] Usamos las fórmulas que ya demostramos: j por j más uno por j más dos, entre seis, menos j menos uno por j por j más uno, entre seis. Factorizamos j por j más uno. Dentro queda j más dos menos j menos uno: tres. Dividimos tres entre seis y obtenemos j por j más uno entre dos.
> [TRIGGER_4] Esa es exactamente T j. Después de una G, un residuo gobernado por pesos cúbicos cae por debajo de un peso triangular. Es la misma relación que descubrimos al añadir una A al esqueleto: los nuevos triples se cuentan mediante pares. Ahora la usaremos para medir cuántas ges necesitamos.”

## Escena 27: Cinco caídas dejan veinte o menos

> “[TRIGGER_1] Con residuo menor que cuatrocientos noventa y siete mil seiscientos cuarenta, el índice máximo es ciento cuarenta y tres. La siguiente G deja menos de T ciento cuarenta y tres: diez mil doscientos noventa y seis.
> [TRIGGER_2] Con menos de diez mil doscientos noventa y seis, el índice máximo es treinta y nueve: V treinta y nueve vale nueve mil ochocientos ochenta, y V cuarenta vale diez mil seiscientos sesenta. Una G deja menos de T treinta y nueve, que es setecientos ochenta. Con menos de setecientos ochenta, el índice máximo es dieciséis: seiscientos ochenta cabe, ochocientos dieciséis no. Otra G deja menos de ciento treinta y seis.
> [TRIGGER_3] Con menos de ciento treinta y seis, el índice máximo es nueve: V nueve vale ciento veinte y V diez ciento sesenta y cinco. Una G deja menos de T nueve, cuarenta y cinco. Con menos de cuarenta y cinco, el índice máximo es seis: V seis vale treinta y cinco y V siete cincuenta y seis. Una G deja menos de T seis, veintiuno.
> [TRIGGER_4] Son cinco inserciones después de la tanda inicial. El residuo final es entero y menor que veintiuno: como máximo veinte. Si en cualquier momento llegó a cero, usamos menos. Falta cerrar ese último intervalo pequeño sin sumar máximos incompatibles. Vamos a revisar exactamente los pesos que pueden entrar ahí.”

## Escena 28: El residuo pequeño: cinco ges bastan

> “[TRIGGER_1] Para un residuo de cero a veinte, los pesos positivos que pueden importar son veinte, diez, cuatro y uno. Corresponden a cinco, cuatro, tres y dos pares posteriores. Si el residuo es veinte, usamos una G de peso veinte y terminamos.
> [TRIGGER_2] Si el residuo es de cero a nueve, sólo usamos cuatros y unos. Escríbelo como cuatro q más t, con t igual a cero, uno, dos o tres. Como el residuo no supera nueve, q no supera dos. Si q es dos, t sólo puede ser cero o uno: usamos como máximo tres letras. Si q es uno, usamos como máximo una de cuatro y tres de uno: cuatro letras. Si q es cero, como máximo tres.
> [TRIGGER_3] Si el residuo está entre diez y diecinueve, primero usamos una G de peso diez. Queda un número entre cero y nueve, que acabamos de demostrar que cuesta como máximo cuatro letras. Total: como máximo cinco. El caso diecisiete lo alcanza: diez más cuatro más uno más uno más uno.
> [TRIGGER_4] No podemos sumar sin más una moneda de diez, dos de cuatro y tres de uno: esa suma sería veintiuno, fuera del intervalo. Las cantidades máximas no ocurren simultáneamente. La tabla muestra todas las descomposiciones de cero a veinte; los casos anteriores prueban que ninguna usa más de cinco.
> [TRIGGER_5] Ahora cerramos la cuenta G completa: como máximo dos en el primer hueco, cinco durante las caídas y cinco en el resto pequeño. Dos más cinco más cinco: doce ges. Si algunos de esos grupos no se necesitan, la cadena se acorta. Esta cota basta para nuestro objetivo.”

## Escena 29: La garantía: 401 es menor que 500

> “[TRIGGER_1] Reunamos las tres piezas. El esqueleto usa como máximo doscientas ochenta y ocho letras. Las ces, ciento una. Las ges, doce. La longitud queda acotada por doscientas ochenta y ocho más ciento una más doce: cuatrocientas una. Menos que quinientas.
> [TRIGGER_2] Ahora sabemos por qué ciento cuarenta y cuatro pares es una elección válida para objetivos de hasta un millón. No lo tratamos como una constante que funcionó por casualidad. Los pesos grandes reducen las multiplicidades iniciales, y las diferencias entre pesos comprimen los residuos.
> [TRIGGER_3] La cota no dice que exista una salida de cuatrocientas una letras, ni que ésta sea la longitud mínima. Es un techo seguro. Si queremos una comprobación adicional, podemos revisar todos los objetivos de cero a un millón por separado: la familia C usa como máximo cien letras y la G como máximo diez. Eso da otro techo, doscientas ochenta y ocho más cien más diez: trescientas noventa y ocho.
> [TRIGGER_4] Esa auditoría finita sirve como control del dominio concreto. La demostración de cuatrocientas una ya basta por sí sola para el límite. Si aumentaran los objetivos o cambiáramos la reserva de pares, habría que revisar las cuentas: la garantía que acabamos de obtener corresponde a este dominio y a esta construcción.”

## Escena 30: Los ceros y las fronteras también forman parte de la solución

> “[TRIGGER_1] Si ambos objetivos son cero, el recorrido no inserta ninguna letra y omite todos los pares. Eso dejaría una cadena vacía, que no está permitida. Devolvemos CA. Tiene dos letras, no tiene T y tampoco G: por tanto no contiene CAT ni GATA. Cero, cero, con una respuesta válida y no vacía.
> [TRIGGER_2] Si sólo pedimos cinco GATA y cero CAT, la construcción produce GATGATAT. Tiene una G que aporta cuatro y otra que aporta uno, y no tiene C. Si pedimos cero GATA y ocho CAT, produce CATATCCAT: una C aporta seis y las dos últimas uno cada una; no tiene G. Ambos casos reutilizan las mismas reglas.
> [TRIGGER_3] En el último hueco, V uno vale cero. La estación G queda deshabilitada: no dividimos ni repetimos restas con ese peso. Y al leer una solicitud recordamos el orden: primero GATA, después CAT. En el ejemplo cinco, ocho, intercambiarlo cambiaría el problema que estamos resolviendo.
> [TRIGGER_4] Las fórmulas son enteras. Si ampliáramos los índices, sus productos intermedios podrían crecer; conviene usar una aritmética con capacidad suficiente, no decimales que redondeen. Y tampoco debemos construir por separado una respuesta CAT y otra GATA y pegarlas sin analizar los cruces: nuestra independencia depende de compartir el esqueleto y clasificar por la letra inicial.”

## Escena 31: El trabajo sigue a la salida, no al millón

> “[TRIGGER_1] ¿Cuánto trabajo hace el algoritmo? Primero calcula las dos tablas de pesos hasta B, que aquí vale ciento cuarenta y cuatro. Cada índice requiere una cantidad fija de operaciones: el preprocesamiento cuesta orden de B y se hace una sola vez para todas las solicitudes.
> [TRIGGER_2] Por solicitud recorremos B huecos. Esa parte cuesta orden de B. Dentro de un hueco puede parecer que hay una repetición peligrosa: imprimir muchas ces o ges. Pero cada vuelta escribe una letra real de la respuesta. El total de esas vueltas queda cargado a su longitud L, igual que escribir los pares AT.
> [TRIGGER_3] Así, el costo de un caso es orden de B más L. Un objetivo de un millón no implica un millón de pasos: cada letra de peso grande puede representar miles de apariciones. Si agrupamos las letras de un hueco mediante cocientes, la representación se vuelve explícita, pero escribir la salida sigue costando proporcionalmente a su longitud.
> [TRIGGER_4] Para Q solicitudes, sumamos el preprocesamiento B, el recorrido Q por B y las longitudes de todas las respuestas. Orden de B más Q por B más la suma de L sub q. Sólo escribir esas respuestas ya requiere al menos un trabajo proporcional a esa suma. No hemos probado que las respuestas sean las más cortas; hemos acotado el trabajo de esta construcción.”

## Escena 32: Guardar sólo lo que necesitamos

> “[TRIGGER_1] La memoria principal son las dos tablas de pesos: orden de B. Durante una solicitud sólo necesitamos los dos residuos, el índice del hueco y el estado de inicio, además de las cantidades que se insertan. Es un número fijo de valores.
> [TRIGGER_2] La implementación original puede escribir cada letra directamente a la salida. En ese esquema usa memoria adicional constante por caso: no necesita guardar la cadena completa. Las tablas siguen ocupando orden de B y se comparten entre solicitudes.
> [TRIGGER_3] Si preferimos comprobar la longitud o verificar la respuesta antes de imprimirla, guardamos la cadena en un búfer. Ese búfer ocupa orden de L. Entonces la memoria total es orden de B más L. Son dos modos de producir la misma construcción, no dos algoritmos matemáticos distintos.
> [TRIGGER_4] Y verificar no necesita enumerar todos los triples y cuádruples de posiciones. Podemos contar las apariciones con unos pocos acumuladores, leyendo la cadena una sola vez. Nos dará una comprobación independiente de la representación por pesos. Vamos a visualizar esos acumuladores, sin enseñar un bloque de código.”

## Escena 33: Un verificador que cuenta sin enumerar

> “[TRIGGER_1] Para verificar CAT, guardamos cuántas formas hay de escribir el prefijo vacío, C, CA y CAT con las letras leídas. Para GATA guardamos vacío, G, GA, GAT y GATA. El vacío empieza con una forma, y todos los demás acumuladores con cero.
> [TRIGGER_2] Cada nueva letra prolonga las coincidencias anteriores que puede completar. Una C añade el contador del vacío al de C. Una A añade C a CA; una T añade CA a CAT. En GATA, una G añade vacío a G; una T añade GA a GAT; y una A puede añadir GAT a GATA y G a GA. Recorremos los estados de mayor a menor longitud para que cada suma use información anterior a la nueva letra.
> [TRIGGER_3] Leamos el comienzo CGAT. La C crea un prefijo C. La G crea un prefijo G. La A crea un CA y un GA. La T completa un CAT y un GAT. Después llega otra G: ya hay dos prefijos G. La siguiente A aumenta CA de uno a dos, completa el primer GATA y aumenta GA de uno a tres.
> [TRIGGER_4] La T de la posición siete añade esos dos CA al contador CAT, que pasa de uno a tres, y esos tres GA al contador GAT, que pasa de uno a cuatro. Las ces de ocho y nueve elevan C de uno a dos y luego a tres; no cambian los acumuladores de GATA.
> [TRIGGER_5] La A de la posición diez añade tres a CA, que pasa de dos a cinco; añade los cuatro GAT al total GATA, que pasa de uno a cinco; y añade los dos G a GA, que pasa de tres a cinco. La T final añade los cinco CA a CAT: tres más cinco, ocho. También eleva GAT de cuatro a nueve, pero no hay otra A después. GATA permanece en cinco.
> [TRIGGER_6] Una lectura, ocho CAT y cinco GATA. Cada acumulador tiene una interpretación por posiciones: guardamos elecciones anteriores y las extendemos con la posición nueva, sin consumirlas. Para patrones de longitud fija, el verificador cuesta orden de L y memoria constante. Comprobamos además el alfabeto y que la longitud esté entre uno y quinientos.”

## Escena 34: Diseñar el espacio donde la dificultad desaparece

> “[TRIGGER_1] Al principio parecía que necesitábamos escribir un millón de copias de una palabra. Pero una aparición es una elección de posiciones. Un esqueleto alternante puede alojar muchas de esas elecciones, y una sola letra inicial puede activarlas todas.
> [TRIGGER_2] Descubrimos dos pesos: un triángulo para C y una elección de tres elementos para G. Clasificamos las apariciones por su primera letra, y eso separó los objetivos sin separarlos en dos cadenas. Después representamos los números con esos pesos y cumplimos cada promesa de sufijo.
> [TRIGGER_3] El ejemplo quedó en once letras, con ocho CAT y cinco GATA. Para cualquier solicitud del dominio, las cotas de residuos garantizan una respuesta de como máximo cuatrocientas una letras; y para cero, cero, una respuesta no vacía tan simple como CA. Cada requisito tiene ahora su argumento.
> [TRIGGER_4] La pregunta que podemos llevarnos es ésta: cuando varias condiciones parecen interferir, ¿puedo elegir una estructura donde cada decisión tenga una contribución exacta y controlable? [Pausa.] A veces la solución no aparece buscando más rápido entre todas las posibilidades. Aparece diseñando las posibilidades que merece la pena construir.”
