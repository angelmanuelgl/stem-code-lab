# Guion de voz — Jenga Boom

## Escena 01: El bloque que cambia el destino de una torre

> “[TRIGGER_1] Una torre de bloques parece firme. Quitamos una pieza y sigue en pie. Quitamos otra, y también. Pero una retirada más puede cambiarlo todo. [Pausa.] ¿Cómo podemos saber exactamente cuál será el primer movimiento que la vuelve inestable, sin tener que reconstruir toda la torre después de cada jugada?
> [TRIGGER_2] La torre tiene capas. En cada una hay el mismo número inicial de bloques, y la orientación gira noventa grados de una capa a la siguiente. Todas las piezas tienen la misma masa. Conocemos de antemano el orden de las retiradas y queremos el índice de la primera que provoca una caída.
> [TRIGGER_3] Los tamaños pueden ser grandes: hasta diez mil bloques por capa, cinco mil capas y cinco mil retiradas. Una torre puede empezar con cincuenta millones de bloques. La imagen que vamos a usar será pequeña, pero nuestro razonamiento tendrá que funcionar también para esa torre enorme.
> [TRIGGER_4] La pregunta no se responde contando cuántas piezas quedan. Hay que mirar dónde apoyan la masa de arriba. Vamos a descubrir cómo una regla que parece tridimensional termina dependiendo de un intervalo, una suma y un conteo. Antes, aprendamos qué significa estar estable en este problema.”

## Escena 02: Qué debe sostener cada capa

> “[TRIGGER_1] Elige una capa l y traza un corte justo encima de ella. La carga que debe sostener son todos los bloques de las capas superiores: l más uno, l más dos, hasta la cima. La propia capa l es el soporte; no la incluimos en esa carga.
> [TRIGGER_2] Reunimos toda esa masa y miramos su centro de masa desde arriba. Proyectamos el punto sobre el plano horizontal. Para que este corte sea estable, el punto debe quedar en el interior estricto de la envolvente convexa de las piezas que todavía están en la capa de apoyo.
> [TRIGGER_3] Si el punto llega exactamente al borde, el problema ya considera que cae. Si queda fuera, también. En cambio, si no queda ningún bloque por encima del corte, no hay carga que sostener y ese corte no puede provocar una caída, aunque su capa esté vacía.
> [TRIGGER_4] Debemos revisar todos los cortes después de cada retirada. Una sola sección que falle vuelve inestable la configuración. La respuesta es yes y el número de esa primera retirada, o no si todas conservan la estabilidad. El modelo geométrico proporciona la decisión; nuestra tarea es evaluarlo exactamente.”

## Escena 03: Conservar muchas piezas no basta

> “[TRIGGER_1] Imagina una capa con cinco tiras numeradas del uno al cinco y un centro de carga proyectado en la coordenada cinco. Dejamos sólo las tiras uno y cinco. Quedan dos bloques, muy separados, y su envolvente se extiende de cero a diez. El centro cinco está dentro.
> [TRIGGER_2] Ahora dejamos sólo las tiras cuatro y cinco. También quedan dos bloques, con la misma masa de apoyo. Pero su envolvente se extiende de seis a diez. El mismo centro cinco está fuera. El conteo de piezas no distingue estos dos casos, y la estabilidad sí.
> [TRIGGER_3] ¿Qué información geométrica cambia entre las dos capas? [Pausa.] La posición de la primera pieza presente y la de la última. No necesitamos saber cuántas piezas de apoyo rodean el centro: necesitamos conocer los límites del soporte convexo.
> [TRIGGER_4] Este experimento deja una segunda pregunta. Entre las tiras uno y cinco hay un hueco enorme. ¿Por qué lo tratamos como parte del soporte? Porque el enunciado usa una envolvente convexa. Entender esa palabra será lo que nos permita abandonar la geometría general.”

## Escena 04: El hueco está en la envolvente, no en la madera

> “[TRIGGER_1] Una región es convexa cuando contiene el segmento entre cualquier par de sus puntos. La envolvente convexa es la menor región convexa que contiene las piezas. Si dos tiras recorren toda la capa de frente a fondo, los segmentos entre ellas cubren también la franja que queda en medio.
> [TRIGGER_2] Tomemos las tiras dos y cuatro de una capa de cinco. Sus bordes exteriores están en dos y ocho. Cada una ocupa toda la longitud, de cero a diez en la otra dirección. El rectángulo entre esos bordes contiene las dos tiras y todos los segmentos que las conectan.
> [TRIGGER_3] También podemos demostrar que no hace falta una región mayor: todas las piezas presentes están dentro de ese rectángulo, y un rectángulo es convexo. Y no puede ser menor, porque las esquinas extremas de las tiras obligan a incluir los cuatro lados y su interior. Por ambos argumentos, esa es exactamente la envolvente.
> [TRIGGER_4] La madera sigue teniendo huecos. Lo que rellenamos es el objeto matemático que pide el criterio del problema. Por eso quitar una tira interna no cambia esta envolvente si los extremos permanecen. Pero esa pieza tiene masa: retirarla sí puede cambiar lo que tendrán que sostener las capas inferiores. Soporte y masa son dos cuentas distintas.”

## Escena 05: Elegir unidades que hagan desaparecer el ancho

> “[TRIGGER_1] En las unidades originales, cada bloque mide uno de alto, w de ancho y w por n de largo. La capa ocupa un cuadrado de lado w por n. En la dirección de las tiras, el bloque k va desde k menos uno por w hasta k por w; su centro está en k menos un medio por w.
> [TRIGGER_2] Multipliquemos todas las coordenadas horizontales por dos entre w. Los bordes pasan a dos por k menos uno y dos por k. El centro pasa a dos k menos uno. Así aparecen uno, tres, cinco, hasta dos n menos uno: centros impares entre bordes pares.
> [TRIGGER_3] La mitad del lado largo, w por n entre dos, se convierte en n. Y todo el cuadrado pasa de lado w por n a lado dos n. Como w es positivo, escalar ambos ejes conserva el orden y las desigualdades estrictas: interior, borde y exterior siguen siendo los mismos casos.
> [TRIGGER_4] También el centro de masa escala por ese mismo factor, porque la media de coordenadas escaladas es la escala por la media original. Por eso w deja de participar en las comprobaciones. La altura distingue qué bloques están arriba, pero el criterio utiliza únicamente su proyección horizontal.”

## Escena 06: Capas alternadas, coordenadas alternadas

> “[TRIGGER_1] Numeramos las capas desde abajo. En las impares, las tiras se reparten a lo largo de X y cada una recorre todo Y. El bloque k tiene centro X igual a dos k menos uno y centro Y igual a n.
> [TRIGGER_2] En las capas pares giramos noventa grados: todas las piezas tienen centro X igual a n, mientras su centro Y es dos k menos uno. Para n igual a cinco, una capa impar tiene centros uno, cinco; tres, cinco; cinco, cinco; siete, cinco; nueve, cinco.
> [TRIGGER_3] La capa par tiene cinco, uno; cinco, tres; cinco, cinco; cinco, siete; cinco, nueve. No cambiamos la numeración vertical al girar la orientación, ni cambiamos el significado de la operación l, k: identifica una pieza de una capa concreta.
> [TRIGGER_4] Podríamos intercambiar los nombres X e Y en toda la torre y obtendríamos el mismo algoritmo. Lo esencial es usar una convención global y mantenerla al retirar piezas, actualizar sumas y elegir el eje de soporte. Con estas coordenadas ya podemos escribir el rectángulo usando sólo sus extremos.”

## Escena 07: Dos extremos determinan el rectángulo

> “[TRIGGER_1] Llamemos L al índice del primer bloque presente y R al del último, en una capa no vacía. El borde izquierdo de la primera tira es el doble del índice anterior a L: dos multiplicado por la diferencia entre L y uno. El borde derecho de la última es dos R. Los paréntesis de la primera expresión son importantes.
> [TRIGGER_2] Por ejemplo, si n es cinco y quedan las tiras tres y cuatro, el soporte corto va de cuatro a ocho. Sus centros están en cinco y siete, pero el soporte lo determinan los bordes, no los centros. Usar cinco y siete como fronteras sería otro criterio.
> [TRIGGER_3] En la dirección larga, cada tira ocupa de cero a dos n. Para una capa impar, el rectángulo es cuatro a ocho en X y cero a diez en Y en este ejemplo. Para una capa par, esos papeles se intercambian: X completo, Y recortado.
> [TRIGGER_4] Si no queda ninguna tira, no existen extremos de soporte que debamos interpretar. Primero preguntaremos si hay masa arriba. Si la hay, una capa vacía falla; si no, ese corte se ignora. Esa decisión tendrá que ocurrir antes de usar L y R.”

## Escena 08: La otra coordenada siempre pasa la prueba

> “[TRIGGER_1] Cada centro de bloque tiene sus dos coordenadas entre uno y dos n menos uno. La coordenada fija n también pertenece a ese intervalo, incluso cuando n vale uno. Si arriba hay C bloques, podemos sumar esas cotas para cualquiera de los dos ejes.
> [TRIGGER_2] Cada coordenada aporta al menos uno y como máximo dos n menos uno. Por tanto la suma S está entre C y dos n menos uno por C. Dividimos entre C, que es positivo, y la media queda entre uno y dos n menos uno.
> [TRIGGER_3] Ahora compárala con los bordes de la dirección larga: cero y dos n. Como uno es mayor que cero y dos n menos uno es menor que dos n, la media está estrictamente dentro. Esto vale aunque falten muchísimos bloques o sus posiciones sean asimétricas.
> [TRIGGER_4] Así que para una capa impar sólo necesitamos revisar X, y para una par sólo Y. No es una aproximación ni estamos olvidando una fuerza lateral: demostramos que la otra desigualdad siempre se cumple bajo el criterio del problema. La envolvente bidimensional se ha reducido a un intervalo.”

## Escena 09: El centro de toda la masa de arriba

> “[TRIGGER_1] La fórmula general del centro de masa pesa cada posición por su masa. Aquí todos los bloques tienen la misma masa b. En X, el numerador es b por X uno, más b por X dos, y así para todos los bloques superiores; el denominador es b por la cantidad C.
> [TRIGGER_2] Sacamos b de la suma y lo cancelamos. Queda la suma de coordenadas X dividida entre C. En Y ocurre lo mismo. Los bloques son uniformes, así que sus posiciones representativas son los centros que ya calculamos.
> [TRIGGER_3] Llamemos S X a esa suma horizontal y S Y a la otra. El centro proyectado es S X entre C, S Y entre C. Sólo necesitamos tres números, aunque la torre superior contenga millones de piezas. Si cambia una pieza, esos números cambian por su contribución exacta.
> [TRIGGER_4] Y la palabra superior sigue siendo esencial: incluimos todos los bloques de las capas por encima de l, no sólo la capa siguiente y no la propia capa l. Si C es cero, la media no se define y tampoco hace falta: el corte no tiene ninguna carga que sostener.”

## Escena 10: Promediar capas puede esconder el peso real

> “[TRIGGER_1] Tomemos n igual a tres y un corte sobre la capa dos. La capa tres conserva sus tres bloques: todos tienen Y igual a tres, así que aporta cantidad tres y suma Y igual a nueve. La capa cuatro conserva sólo su bloque tres, cuyo centro Y es cinco: aporta cantidad uno y suma cinco.
> [TRIGGER_2] Si promediáramos los centros de las dos capas como si pesaran lo mismo, obtendríamos tres más cinco entre dos: cuatro. Pero la primera tiene tres bloques y la segunda sólo uno. El centro verdadero es nueve más cinco entre cuatro: tres y medio.
> [TRIGGER_3] Podemos verlo colocando tres fichas en la coordenada tres y una en cinco. El punto de equilibrio está más cerca de tres, donde hay más masa. Agrupar por capas es útil siempre que cada grupo conserve su suma y su cantidad.
> [TRIGGER_4] Esta es la razón de nuestros acumuladores. Para combinar capas, sumamos cantidades con cantidades y momentos con momentos. Dividimos una sola vez, si queremos dibujar el centro. El algoritmo ni siquiera necesitará hacer esa división para decidir estabilidad.”

## Escena 11: La frontera se decide con enteros

> “[TRIGGER_1] Sea a el borde izquierdo del soporte y b el derecho. Cuando hay C bloques arriba, la estabilidad pide a menor que S entre C, y S entre C menor que b. Como C es positivo, podemos multiplicar ambos lados sin cambiar el sentido: a C menor que S menor que b C.
> [TRIGGER_2] Sustituimos los bordes de nuestras tiras. A la izquierda está el doble de la diferencia entre L y uno, multiplicado por C; a la derecha, dos R multiplicado por C. La suma S debe quedar estrictamente entre ambos. S es la suma X en capas impares y la suma Y en pares. Todas esas cantidades son enteras.
> [TRIGGER_3] Con soporte de cuatro a ocho y tres bloques arriba, las fronteras de la comparación son doce y veinticuatro. Una suma dieciocho da centro seis y pasa. Una suma doce da centro cuatro y cae por el borde izquierdo. Una suma veinticuatro da centro ocho y cae por el derecho.
> [TRIGGER_4] Una suma nueve queda a la izquierda, y veintisiete a la derecha. También fallan. Los cinco casos se distinguen exactamente con las mismas dos desigualdades. No hay que decidir qué tolerancia usar para un decimal cercano al borde: la igualdad entera conserva el caso que el problema considera inestable.”

## Escena 12: Cinco datos por capa

> “[TRIGGER_1] Para cada capa guardamos cantidad de bloques, suma de sus centros X, suma de sus centros Y, extremo izquierdo y extremo derecho. Además, cada posición tiene una marca que recuerda si su bloque fue retirado. No guardamos una geometría nueva después de cada jugada: conservamos sus datos suficientes.
> [TRIGGER_2] Al principio hay n bloques y extremos uno y n. La coordenada variable recorre uno, tres, cinco, hasta dos n menos uno. Sumamos dos k menos uno desde k igual a uno hasta n: dos por n por n más uno entre dos, menos n. El resultado es n al cuadrado.
> [TRIGGER_3] La otra coordenada vale n en cada uno de los n bloques, así que también suma n al cuadrado. Por eso en todas las capas empezamos con ambas sumas iguales, aunque sus orientaciones sean diferentes. Para n igual a cinco, cantidad cinco y sumas veinticinco, veinticinco.
> [TRIGGER_4] Inicializamos todas las marcas como presentes. Los extremos están listos para describir el soporte; las sumas y el conteo, para alimentar la masa de los cortes inferiores. Estos dos usos comparten la capa, pero deben permanecer separados en nuestro dibujo y en el razonamiento.”

## Escena 13: Una retirada cambia una sola contribución

> “[TRIGGER_1] La operación l, k identifica el bloque retirado. Calculamos su centro con la paridad de l, restamos uno de la cantidad y restamos sus coordenadas de las dos sumas. Luego marcamos esa posición como retirada. Todas las demás capas conservan sus datos locales.
> [TRIGGER_2] Probemos n igual a cinco en una capa impar, retirando el bloque dos. Su centro es tres, cinco. La cantidad pasa de cinco a cuatro, suma X de veinticinco a veintidós y suma Y de veinticinco a veinte. Son exactamente los cuatro centros que permanecen.
> [TRIGGER_3] En una capa par, el mismo bloque dos tendría centro cinco, tres. Sus nuevas sumas serían veinte en X y veintidós en Y. La regla es la misma resta de una contribución; la orientación decide las coordenadas que restamos.
> [TRIGGER_4] El enunciado garantiza que las retiradas no repiten piezas. Cada marca cambia una sola vez y nunca descontamos dos veces la misma masa. Tras esta actualización todavía falta ajustar los extremos si quitamos uno de ellos, y volver a comprobar la torre: una modificación local puede afectar muchos cortes inferiores.”

## Escena 14: Los extremos caminan sobre las marcas

> “[TRIGGER_1] Los huecos internos no cambian los extremos mientras quede una pieza más allá de ellos. En cinco posiciones, retiramos primero dos y tres. L sigue en uno y R en cinco. Las marcas recuerdan los dos huecos aunque todavía no afectan el borde.
> [TRIGGER_2] Ahora retiramos uno. L estaba allí y debe avanzar: cruza uno, cruza dos, cruza tres y se detiene en cuatro, que está presente. R permanece en cinco. Las piezas restantes son cuatro y cinco, y sus extremos son exactamente cuatro y cinco.
> [TRIGGER_3] Retiramos cinco. R retrocede hasta cuatro. Finalmente retiramos cuatro: la cantidad llega a cero y ya no hay pieza donde detenerse. El recorrido protegido deja L mayor que R; no consultamos una posición fuera de la región ni usamos estos extremos como un soporte válido.
> [TRIGGER_4] L sólo avanza y R sólo retrocede. Una marca eliminada puede ser sobrepasada por cada extremo como máximo una vez. Esos saltos no se repiten desde el principio en cada retirada. Esta monotonicidad de los punteros será útil para el costo; no es una afirmación sobre la monotonicidad de la estabilidad.”

## Escena 15: Quitar una pieza interna sigue cambiando la torre

> “[TRIGGER_1] Volvamos a una capa impar completa de cinco bloques. Retiramos el bloque dos, cuyo centro X es tres. Los extremos siguen siendo uno y cinco: la envolvente todavía ocupa de cero a diez. Pero la suma X baja de veinticinco a veintidós, y la cantidad de cinco a cuatro.
> [TRIGGER_2] El centro de esa capa pasa de cinco a veintidós entre cuatro, cinco y medio. Ese cambio alimentará el centro de toda la masa que vean los cortes inferiores. Un soporte sin cambios no significa que toda la torre conserve su misma carga.
> [TRIGGER_3] Si en cambio retiramos el bloque central, con X igual a cinco, la nueva suma es veinte y la cantidad cuatro: el promedio sigue siendo cinco. Los agregados sí cambiaron, aunque el cociente no. Esto ocurrirá en la cuarta retirada de nuestro ejemplo principal.
> [TRIGGER_4] Por eso guardamos ambas clases de información. Los extremos describen lo que una capa puede sostener; las sumas y la cantidad describen lo que esa capa aporta a quienes están debajo. Una misma retirada tiene esos dos efectos, y cada corte utilizará sólo el que le corresponde.”

## Escena 16: Leer la torre desde arriba

> “[TRIGGER_1] Para revisar todos los cortes, bajamos desde la cima. Antes de comprobar la capa h, los acumuladores están en cero: no hay ninguna capa por encima. Por tanto ese primer corte no falla. Después agregamos las contribuciones de la capa h.
> [TRIGGER_2] Al llegar a h menos uno, el banco ya representa exactamente la capa superior. Comprobamos si esa carga cabe en su soporte. Sólo después agregamos la capa h menos uno. Así, al llegar a h menos dos, el banco reúne las dos capas superiores.
> [TRIGGER_3] La regla se repite con una identidad precisa: antes de revisar l, cantidad C y sumas S X, S Y describen las capas l más uno hasta h. Al terminar esa comprobación, sumamos los datos de l y el banco queda listo para revisar l menos uno.
> [TRIGGER_4] No reiniciamos una suma completa para cada corte. Cada capa entra una sola vez en el banco durante este recorrido. Y el orden importa: comprobar primero, agregar después. Si agregamos el propio soporte antes de comprobarlo, incluiremos masa que no pertenece a la carga superior.”

## Escena 17: Incluir el soporte puede esconder una caída

> “[TRIGGER_1] Veamos qué saldría mal. Hay dos capas y dos bloques por capa. Retiramos el bloque uno de la capa inferior. Sólo queda su bloque dos, cuyo soporte X va de dos a cuatro. La capa superior es par: ambos bloques tienen X igual a dos.
> [TRIGGER_2] La carga verdadera tiene cantidad dos y suma X cuatro. Su centro es cuatro entre dos, igual a dos: exactamente el borde izquierdo. El criterio dice caída. La comparación entera exige cuatro menor que cuatro, y eso es falso.
> [TRIGGER_3] Ahora cometamos el error de sumar también el bloque de apoyo. Su centro X es tres. La cantidad aparente pasa a tres y la suma a siete. El promedio siete tercios queda entre dos y cuatro. El dibujo diría estable, pero hemos cambiado la masa que la capa debía sostener.
> [TRIGGER_4] No es un detalle de redondeo. Es una selección incorrecta de objetos. El bloque de apoyo no puede mejorar artificialmente el centro de la carga poniéndose a sí mismo en el promedio. Nuestra secuencia comprobar y luego agregar impide exactamente ese error.”

## Escena 18: Tres ramas antes de cualquier desigualdad

> “[TRIGGER_1] Ya podemos describir la revisión de una capa con tres ramas. Primera pregunta: ¿hay bloques por encima? Si C es cero, el corte no falla y no calculamos ningún centro. Después agregamos la capa y seguimos bajando.
> [TRIGGER_2] Si C es positivo, preguntamos si queda alguna pieza en el soporte. Si su cantidad es cero, falla: existe una carga y no hay región que la sostenga. Aquí tampoco consultamos extremos ni dividimos nada.
> [TRIGGER_3] Si hay carga y soporte, elegimos X para capa impar o Y para par. Formamos los productos del borde izquierdo y del derecho por C. El corte pasa únicamente si la suma relevante queda estrictamente entre ellos. Si pasa, agregamos los datos locales y continuamos.
> [TRIGGER_4] Tras una retirada actualizamos su capa, ajustamos sus extremos y ejecutamos este descenso. Si falla cualquier corte, registramos ese número de operación. Si todos pasan, procesamos la siguiente retirada. Son los mismos tres casos para todas las capas, incluidas las vacías y la cima.”

## Escena 19: La torre del ejemplo: seis capas de cinco bloques

> “[TRIGGER_1] Pasemos al primer ejemplo oficial. Hay cinco bloques por capa, ancho dos y seis capas. Usaremos nuestras coordenadas normalizadas: el cuadrado va de cero a diez y los centros variables son uno, tres, cinco, siete y nueve.
> [TRIGGER_2] Vamos a seguir especialmente la capa cuatro. Es par, así que su intervalo corto está en Y. Al principio L es uno y R cinco: soporte de cero a diez. Arriba están las capas cinco y seis, con cinco bloques cada una.
> [TRIGGER_3] Cada capa completa aporta suma Y veinticinco. En la cinco, Y es fijo en cinco; en la seis, recorre uno, tres, cinco, siete y nueve. Juntas tienen cantidad diez y suma cincuenta. Su centro Y es cinco, en el interior del soporte.
> [TRIGGER_4] Las retiradas que vamos a comprobar son cuatro, uno; cuatro, dos; cuatro, cinco; cinco, tres; y cuatro, tres. No sabemos todavía cuál fallará. Conservaremos dos paneles: lo que queda del soporte en la capa cuatro y lo que pesa por encima de ella. Así veremos por qué dos jugadas diferentes pueden afectar cosas diferentes.”

## Escena 20: Retirada uno: se mueve el borde izquierdo

> “[TRIGGER_1] Primera retirada: bloque uno de la capa cuatro. Su centro es X igual a cinco, Y igual a uno. Sale del soporte, y sus datos locales cambian: quedan cuatro bloques, suma X veinte y suma Y veinticuatro.
> [TRIGGER_2] El extremo izquierdo avanza de uno a dos; el derecho sigue en cinco. El nuevo intervalo Y es de dos a diez. Pero este bloque no pertenecía a la carga por encima de cuatro: arriba siguen los diez bloques y suma Y cincuenta.
> [TRIGGER_3] El centro superior continúa en cinco. Multiplicamos las fronteras por diez: veinte menor que cincuenta menor que cien. El corte sobre cuatro sigue estable. No confundimos el cambio de masa local de cuatro con el banco de su carga superior.
> [TRIGGER_4] La capa cinco conserva soporte completo y sostiene la seis; las capas inferiores a cuatro también conservan sus soportes completos. Cualquier centro de carga permanece dentro de ese cuadrado completo por la cota que demostramos. Ningún corte falla en la primera retirada, así que avanzamos a la segunda.”

## Escena 21: Retirada dos: el margen se estrecha

> “[TRIGGER_1] Segunda retirada: bloque dos de la capa cuatro. Su centro Y es tres, y X sigue en cinco. La capa pasa a tres bloques, suma X quince y suma Y veintiuno. Los presentes son tres, cuatro y cinco.
> [TRIGGER_2] L avanza a tres. Calculamos el borde izquierdo como dos por la diferencia entre tres y uno: cuatro. El derecho sigue en diez. Arriba no retiramos nada: cantidad diez y suma Y cincuenta, centro cinco.
> [TRIGGER_3] La prueba ahora pide cuarenta menor que cincuenta menor que cien. Pasa, pero el centro quedó mucho más cerca del borde izquierdo. Ese margen visual no reemplaza la desigualdad: la decisión sigue siendo estricta y exacta.
> [TRIGGER_4] Los demás soportes siguen completos. La pérdida de masa de la capa cuatro cambia los bancos de cortes inferiores, pero todos sus centros siguen entre los bordes cero y diez. La segunda operación también deja estable toda la torre.”

## Escena 22: Retirada tres: también se mueve el borde derecho

> “[TRIGGER_1] Tercera retirada: el bloque cinco de la capa cuatro. Sus coordenadas son cinco, nueve. La cantidad local baja a dos, suma X a diez y suma Y a doce. Quedan los bloques tres y cuatro.
> [TRIGGER_2] El extremo derecho retrocede de cinco a cuatro. Su borde pasa de diez a ocho; el izquierdo sigue en cuatro. La envolvente es el rectángulo completo en X y recortado entre cuatro y ocho en Y.
> [TRIGGER_3] La carga superior todavía tiene diez bloques y suma Y cincuenta. La comparación es cuarenta menor que cincuenta menor que ochenta. El centro cinco sigue dentro, aunque la capa perdió tres de sus cinco piezas originales.
> [TRIGGER_4] Otra vez pasan los demás cortes, que conservan soporte completo. Hemos retirado desde ambos lados, y el conteo de piezas disminuyó mucho, pero el criterio responde a su ubicación y a la carga superior. La tercera retirada todavía es segura dentro del modelo.”

## Escena 23: Retirada cuatro: cambia la carga, no el soporte

> “[TRIGGER_1] La cuarta retirada es distinta: bloque tres de la capa cinco. Esta capa es impar, y la pieza central tiene coordenadas cinco, cinco. Quitamos una parte de la carga que sostiene cuatro; no tocamos ninguna de sus dos piezas de apoyo.
> [TRIGGER_2] La capa cinco queda con cuatro bloques y sumas veinte, veinte. La seis sigue con cinco y sumas veinticinco, veinticinco. Por encima de cuatro tenemos ahora cantidad nueve y sumas cuarenta y cinco en ambos ejes.
> [TRIGGER_3] El centro Y es cuarenta y cinco entre nueve: sigue siendo cinco. Retiramos una pieza situada justamente en el centro anterior; al reducir suma y cantidad en la misma proporción, el promedio no se mueve. El soporte de cuatro continúa entre cuatro y ocho.
> [TRIGGER_4] Multiplicamos ahora por nueve, no por diez. Treinta y seis menor que cuarenta y cinco menor que setenta y dos. Pasa. La capa cinco conserva sus extremos uno y cinco pese al hueco central, y los cortes inferiores tienen soporte completo. La cuarta retirada tampoco causa caída.”

## Escena 24: Retirada cinco: el soporte deja atrás al centro

> “[TRIGGER_1] Quinta retirada: bloque tres de la capa cuatro. Su centro es cinco, cinco. Sale otra pieza de apoyo y queda sólo el bloque cuatro, con centro cinco, siete. La cantidad local es uno, suma X cinco y suma Y siete.
> [TRIGGER_2] L avanza de tres a cuatro y R ya era cuatro. El soporte Y queda entre seis y ocho. La carga superior no cambia: nueve bloques, suma Y cuarenta y cinco, centro cinco. Esta vez el borde izquierdo se mueve a la derecha del centro.
> [TRIGGER_3] La comparación pide seis por nueve menor que cuarenta y cinco, y cuarenta y cinco menor que ocho por nueve. Es decir, cincuenta y cuatro menor que cuarenta y cinco menor que setenta y dos. La primera desigualdad es falsa. El centro está fuera, a la izquierda del soporte.
> [TRIGGER_4] Basta este corte para declarar inestabilidad. Las primeras cuatro retiradas fueron estables y la quinta falla, así que la respuesta es yes y cinco. No esperaremos a otra jugada ni buscaremos qué pasaría después de la caída: ya encontramos el primer instante que pedía el problema.”

## Escena 25: Auditar los seis cortes del ejemplo

> “[TRIGGER_1] Comprobemos el estado de la cuarta retirada con el recorrido completo. Antes de capa seis el banco está vacío. Antes de cinco contiene la seis: cantidad cinco y sumas veinticinco, veinticinco. Antes de cuatro reúne cinco y seis: cantidad nueve y sumas cuarenta y cinco, cuarenta y cinco.
> [TRIGGER_2] Agregamos las dos piezas de cuatro, con sumas diez y doce. Antes de tres hay once bloques, suma X cincuenta y cinco y suma Y cincuenta y siete. Agregamos la capa tres completa: antes de dos, dieciséis bloques y sumas ochenta, ochenta y dos. Agregamos la dos: antes de uno, veintiún bloques y sumas ciento cinco, ciento siete.
> [TRIGGER_3] En cinco se comprueba X, en cuatro Y, en tres X, en dos Y y en uno X. Para las capas con soporte completo, las pruebas son cero menor que veinticinco menor que cincuenta; cero menor que cincuenta y cinco menor que ciento diez; cero menor que ochenta y dos menor que ciento sesenta; y cero menor que ciento cinco menor que doscientos diez. Cuatro usa treinta y seis menor que cuarenta y cinco menor que setenta y dos. Todas pasan.
> [TRIGGER_4] Después de la quinta retirada, antes de cuatro el banco sigue siendo nueve, cuarenta y cinco, cuarenta y cinco, pero su soporte pasó a seis, ocho y falla. Si sólo para auditar siguiéramos sumando hacia abajo, los bancos serían diez, cincuenta, cincuenta y dos; quince, setenta y cinco, setenta y siete; veinte, cien, ciento dos. Sus soportes completos pasan. El algoritmo puede detener la comprobación en el primer corte fallido porque un fallo basta.”

## Escena 26: Por qué estas comprobaciones son suficientes

> “[TRIGGER_1] Primero, los datos locales son exactos al comienzo: contamos todas las piezas y sumamos sus centros. Cada retirada elimina una sola contribución y su marca. Los punteros se detienen en la primera y la última posición presentes, o reconocen que la capa está vacía. Por inducción, esos datos siguen describiendo exactamente la configuración.
> [TRIGGER_2] Segundo, el recorrido vertical empieza sin capas superiores. Antes de comprobar l, su banco contiene justamente las capas l más uno hasta h. Agregar l después de comprobarla conserva la misma afirmación para l menos uno. Por inducción, cada corte recibe exactamente su carga, sin piezas de más ni de menos.
> [TRIGGER_3] Tercero, cada decisión coincide con la regla geométrica: sin carga no hay fallo; con carga y sin soporte hay fallo. Con ambos presentes, la envolvente es el rectángulo de los extremos; el eje largo siempre pasa y el corto pasa exactamente cuando se cumplen los productos estrictos. Son equivalencias, así que no rechazamos un corte válido ni aceptamos uno inválido.
> [TRIGGER_4] Por último, procesamos las retiradas en su orden. Antes de anunciar un índice comprobamos todas las operaciones anteriores como estables, y en esa operación encontramos al menos un corte inestable. Por tanto es el primer instante. Si acabamos la lista sin ningún fallo, la respuesta no también queda demostrada.”

## Escena 27: Una geometría estable después no borra la primera caída

> “[TRIGGER_1] Hay una tentación: buscar la primera caída con búsqueda binaria. Eso exigiría que, una vez inestable una configuración, todas las configuraciones posteriores de la lista también fueran inestables. La caída física ya ocurrió, pero esa propiedad de la geometría abstracta no está garantizada.
> [TRIGGER_2] Tomemos dos bloques por capa y tres capas. Retiramos el bloque uno de la capa inferior. Su soporte X queda entre dos y cuatro. Arriba hay cuatro bloques con suma X ocho: el centro es dos, justo en el borde. La primera retirada causa caída.
> [TRIGGER_3] Sólo como experimento geométrico, continuemos retirando el bloque uno de la capa superior de esa misma configuración. Los centros X que quedan arriba son dos, dos y tres. Cantidad tres, suma siete, centro siete tercios. Está estrictamente entre dos y cuatro: seis menor que siete menor que doce.
> [TRIGGER_4] El otro corte también pasa: la capa intermedia tiene soporte Y completo de cero a cuatro y la única pieza superior tiene Y igual a dos. La cima no tiene carga. La geometría final parecería estable, aunque la primera retirada ya provocó la caída. Estable, inestable, estable: no hay una frontera monótona para buscar. Revisamos cronológicamente y conservamos el primer fallo.”

## Escena 28: Una capa vacía sólo falla si sostiene algo

> “[TRIGGER_1] Considera la torre más pequeña: una capa con un solo bloque. Lo retiramos. La capa queda vacía, pero no hay ninguna masa por encima ni otro corte que sostener. El criterio correcto da no. Vacío no significa por sí solo caída.
> [TRIGGER_2] Con un bloque por capa y dos capas, retiramos el bloque superior. La pieza inferior sigue sobre el suelo. Encima de la capa vacía no queda nada; encima de la inferior tampoco. La respuesta vuelve a ser no.
> [TRIGGER_3] Ahora hay tres capas de un bloque y quitamos la pieza intermedia. Sigue habiendo un bloque en la cima, pero no hay soporte en la capa dos. Aquí sí cae: cantidad superior positiva y soporte vacío. La respuesta es yes y uno.
> [TRIGGER_4] El análisis de la carpeta documenta que la copia J.cpp declara caída al vaciar cualquier capa antes de preguntar si hay masa encima. Por eso devuelve yes y uno en el primer contraejemplo, mientras la regla del enunciado y la referencia del jurado dan no. El arreglo conceptual es situar la pregunta sobre carga primero, y comprobar el soporte vacío sólo en su rama positiva. La geometría, no la procedencia de un archivo, decide qué condición debemos demostrar.”

## Escena 29: Mirar sólo la capa vecina también engaña

> “[TRIGGER_1] Otro error sería calcular sólo el centro de la capa inmediatamente superior. Usemos dos bloques por capa y tres capas, pero ahora cambiemos el orden de las retiradas: primero quitamos el bloque uno de la cima y después el bloque uno de la base.
> [TRIGGER_2] La primera retirada deja estable la torre: la capa intermedia conserva su soporte completo. En la segunda, la base queda con soporte X entre dos y cuatro. La capa vecina tiene dos bloques, ambos con X igual a dos. Si sólo la miramos, su centro dos toca el borde y parecería que cae.
> [TRIGGER_3] Pero también está la pieza que queda en la cima, con X igual a tres. La carga completa contiene los centros dos, dos y tres: su promedio es siete tercios. Cumple seis menor que siete menor que doce. La base sí pasa. En la capa intermedia, el centro Y de la pieza superior es dos, dentro de cero a cuatro.
> [TRIGGER_4] No estamos recuperando una torre después de una caída: estas dos retiradas, en este orden, mantienen la estabilidad. Lo que falló fue el diagnóstico basado sólo en el vecino. Cada bloque estrictamente superior cuenta, aunque haya varias capas entre él y el corte. Por eso sumamos desde arriba y conservamos el banco completo.”

## Escena 30: Contar trabajo: una pasada por capa, no por bloque

> “[TRIGGER_1] El método ingenuo volvería a inspeccionar todos los bloques después de cada retirada. Con los máximos, cinco mil retiradas por cinco mil capas por diez mil posiciones da doscientos cincuenta mil millones de inspecciones. Si además recomputamos cada torre superior por separado, repetimos todavía más sumas.
> [TRIGGER_2] Nuestra inicialización de marcas recorre h por n posiciones una vez: orden de h n. Los datos por capa se inicializan con fórmulas. En cada retirada restamos una contribución en tiempo constante y recorremos como máximo h capas, con un número fijo de operaciones por corte.
> [TRIGGER_3] Aparte están los punteros de extremos. L nunca retrocede y R nunca avanza. Cada marca eliminada se cruza como máximo una vez por extremo; como hay m retiradas distintas, el trabajo total de estos desplazamientos es orden de m, y también queda acotado por orden de h n. No multiplicamos todos esos cruces por el número de revisiones.
> [TRIGGER_4] Sumamos inicialización y recorridos: orden de h n más m h. En el peor tamaño son cincuenta millones de marcas inicializadas y veinticinco millones de comprobaciones de capas. Podemos detener un recorrido al hallar un fallo y detener el análisis geométrico después de la primera caída. Esta cota describe el algoritmo; no demuestra que sea el único método posible ni el óptimo asintótico.”

## Escena 31: La memoria recuerda huecos, no una física completa

> “[TRIGGER_1] Las marcas forman una matriz de h capas por n posiciones. Los cinco campos de cada capa y el banco del recorrido añaden una cantidad proporcional a h, más unos pocos acumuladores. La memoria total es orden de h n más h.
> [TRIGGER_2] La copia adjunta reserva cinco mil uno por diez mil uno marcas: cincuenta millones quince mil una posiciones. Si cada booleano ocupa un byte, eso son aproximadamente cuarenta y siete coma siete mebibytes. Es la reserva concreta del archivo, no una cantidad de bloques que se retiran.
> [TRIGGER_3] Una representación por bits puede guardar ocho marcas en un byte y reducir esa parte aproximadamente por ocho. También podría guardarse sólo el conjunto de retiradas de cada capa: la cantidad de información sería orden de h más m, a cambio de operaciones de consulta y mantenimiento de conjuntos.
> [TRIGGER_4] Para comprender esta solución no necesitamos esa alternativa. La matriz hace explícitas las consultas de presencia y los saltos de extremos. Los agregados son pequeños; y no guardamos todos los centros de cada bloque porque sus coordenadas se reconstruyen con l, k y la paridad.”

## Escena 32: Exactitud también significa usar enteros suficientemente grandes

> “[TRIGGER_1] Eliminar los decimales no basta si luego el entero se desborda. La cantidad de bloques por encima de un corte puede llegar a h por n, como máximo cincuenta millones. Cada frontera normalizada es como máximo dos n, veinte mil.
> [TRIGGER_2] Su producto puede llegar a veinte mil por cincuenta millones: un billón, diez elevado a doce. Las sumas de coordenadas también están acotadas por la cantidad de bloques multiplicada por la mayor coordenada. Son magnitudes que exceden la capacidad de un entero de treinta y dos bits.
> [TRIGGER_3] Por eso las sumas acumuladas y los productos se calculan con enteros de sesenta y cuatro bits. La multiplicación debe tener esa capacidad desde su primer paso; guardar después en una caja grande un resultado que ya se desbordó no repara la cuenta.
> [TRIGGER_4] Con esa capacidad, nuestras comparaciones siguen siendo exactas. Estar en el borde es igualdad, fuera es una desigualdad falsa y dentro son dos desigualdades verdaderas. No cambiamos los signos por comodidad y no introducimos tolerancias que conviertan una caída real en estabilidad.”

## Escena 33: Comprobar con otra forma de mirar la misma torre

> “[TRIGGER_1] Una comprobación útil no debe repetir a ciegas nuestras mismas actualizaciones. Para torres pequeñas podemos conservar la lista de piezas presentes y, después de cada retirada, reconstruir desde cero la masa sobre cada corte, con sus coordenadas y su centro.
> [TRIGGER_2] También reconstruimos los extremos del soporte desde las piezas que quedan en la capa, en lugar de confiar en los punteros mantenidos. Aplicamos la definición de envolvente y la comparación exacta. Este método lento es manejable en ejemplos pequeños y sirve para contrastar el método rápido.
> [TRIGGER_3] Debemos incluir casos que separen ideas: una sola capa, vaciar la cima, vaciar una capa intermedia, centro exactamente en un borde, huecos internos y una carga repartida entre varias capas. El ancho también puede variar: la normalización debería conservar el resultado. Y las retiradas no se repiten.
> [TRIGGER_4] Comparamos el estado de cada prefijo y el índice de la primera caída. Comparar sólo la configuración final podría pasar por alto el ejemplo estable, inestable, estable que vimos antes. La fuente documenta además contrastes locales con el jurado. Aquí las demostraciones siguen siendo el fundamento, y las comprobaciones buscan errores concretos de implementación o de nuestra traza.”

## Escena 34: La torre que aprendimos a leer

> “[TRIGGER_1] En el ejemplo, la quinta retirada era decisiva. El centro superior seguía en cinco, pero el apoyo se había estrechado hasta seis, ocho. Toda la complejidad visual de la torre terminó en una comparación: cincuenta y cuatro menor que cuarenta y cinco era falso.
> [TRIGGER_2] No llegamos a esa comparación por un truco aislado. Demostramos que las tiras extremas determinan una envolvente rectangular, que la dirección larga siempre pasa y que la masa superior se resume en dos sumas y un conteo. Elegimos coordenadas que hicieron enteros todos los centros y bordes.
> [TRIGGER_3] Después conservamos esos datos con cada retirada y los combinamos de arriba hacia abajo, comprobando antes de agregar el soporte. Los huecos, las capas vacías y el borde dejaron de ser excepciones improvisadas: cada uno encontró su lugar en la regla exacta.
> [TRIGGER_4] La pregunta que nos llevamos es: ¿qué parte de una estructura necesito conocer para decidir, y qué puedo resumir sin perder el argumento? [Pausa.] A veces entender una torre no exige seguir cada uno de sus bloques. Exige descubrir qué información sostienen, y en qué orden debemos reunirla.”
