# Guion de Voz en Off: ICPC México 2026 (Segunda Parte)



------------------------- 
## 1.

Voz en off: 
¿Por qué los problemas de la ICPC son tan diferentes a lo que ves en la escuela? 

En clase, la estructura es clara: el problema viene con instrucciones directas y, por lo general, el nombre de la técnica que debes usar ya viene implícito o sugerido desde el inicio. Prácticamente sabes de antemano qué herramienta sacar de la caja.

// MANIM:
> **Especificación visual (Manim CE):** Pantalla dividida en dos. A la izquierda, ficha escolar con instrucción directa y caja de herramientas cuya técnica aparece sugerida; a la derecha, ficha ICPC con una historia sin técnica indicada. Replegar la primera y dejar la segunda como incógnita. Usar `RoundedRectangle`, `Tex` y `Transform`; no adjudicar aún una técnica al problema ICPC.

Pero en la ICPC la lógica cambia por completo. Aquí los problemas vienen disfrazados de historias, cuentos o situaciones cotidianas. Tu trabajo consiste en "pelar la cebolla": quitar capas de texto hasta descubrir el esqueleto matemático que hay debajo; ya sea un grafo oculto, una tabla de frecuencias o una estructura geométrica. La historia es solo un disfraz.

// MANIM 
> **Especificación visual (Manim CE):** Centrar la ficha narrativa y retirar capas sucesivas de texto. Debajo, mostrar tres ejemplos alternativos del “esqueleto”: grafo (nodos/aristas), frecuencias (tabla) y geometría (puntos/segmentos). Animar cada traducción por separado con `Transform`; dejar claro que son posibles estructuras ocultas, no tres estructuras simultáneas del mismo problema.

Y cuando abres ese enunciado por primera vez, con el timepo corriendo contra reloj, te enfrentas de golpe a un menú gigantesco de técnicas: y ninguna viene marcada. Tienes que adivinar el camino correcto entre decenas de opciones, muchas de las cuales tal vez ni siquiera conozcas.

// MANIM
> **Especificación visual (Manim CE):** Distribuir en tarjetas las técnicas nombradas y mantener un reloj visible. Ninguna tarjeta está marcada. Un cursor recorre varias opciones; las no elegidas quedan atenuadas, pero ninguna se presenta como solución correcta porque el guion no especifica un problema concreto. Animar el reloj y enfatizar “ninguna viene marcada”.


De hecho, una de las habilidades más críticas aquí no es saber resolverlo todo porque resolver el set completo es humanamente imposible, así está diseñado, hay que saber elegir tus batallas. Por ejemplo en esta final, los mejores equipos del país lograron resolver entre 8 y 9 problemas; muy pocos pasaron de ahí, mientras que la mediana para el resto de los equipos se quedó en apenas 4 problemas resueltos, moviéndose la gran mayoría en un rango de 2 a 6 problemas. Saber qué problema sí puedes atacar y cuál te va a hacer perder valiosas horas es la diferencia entre subir al podio o quedarte fuera.

------------------------- 
---

## 2

Voz en off: 
Para entenderlo mejor, veamos un ejemplo real. Este fue uno de mis favoritos del contest, el **Problema C: Clumsy Courier**. 
Explicarlo a fondo no es el objetivo, Les dejo el enunciado completo en pantalla para los más curiosos, y si les interesa, mi próximo video puede dedicarse enteramente a resolverlo paso a paso. Mi proceso de pensamiento, como llegue a una idea, como concrete y formalice la idea, y como lo implemente


// MANIM:  primero aparece el titulo, luygo todo el texto, si puediera dar el estilo que se esta leyendo una hoja, osea como que aprece una hoja con eso y se va subiendo, algo asi
> **Especificación visual (Manim CE):** Conservar el enunciado original en inglés y presentarlo en cuatro paneles legibles: (1) cuadrícula R×C, numeración y extremos (1,1)/(R,C); (2) movimientos ortogonales y límites; (3) exactamente U movimientos Up y L Left, permitiendo repetir vértices; (4) contar secuencias distintas módulo 998,244,353, más Input/Output. Mantener una mini cuadrícula con inicio/destino en cada panel. Usar `FadeIn` y desplazamiento vertical; no reducir todo el texto a una sola lámina ilegible ni omitir restricciones.
> **Problem C - Clumsy Courier**
> A courier must deliver a package across a city. The city's streets form a rectangular grid with $R$ horizontal streets and $C$ vertical streets. On the city map, the horizontal streets are numbered from $1$ to $R$ from top to bottom, and the vertical streets from $1$ to $C$ from left to right. Intersection $(r, c)$ is where horizontal street $r$ meets vertical street $c$. The courier starts at $(1, 1)$ and must deliver the package at $(R, C)$.
> 
> In one move, the courier can follow a street from $(r, c)$ to an adjacent intersection:
> - Down, to $(r + 1, c)$;
> - Up, to $(r - 1, c)$;
> - Right, to $(r, c + 1)$; or
> - Left, to $(r, c - 1)$.
> 
> The courier may only travel between intersections in this grid. The courier is in no hurry to finish the delivery. To make the trip last longer, they want to choose a route that includes exactly $U$ Up moves and exactly $L$ Left moves. The courier is willing to visit any intersection more than once, including the starting and ending intersections.
> 
> Count the number of different routes from $(1, 1)$ to $(R, C)$ that stay within the grid and contain exactly $U$ Up moves and exactly $L$ Left moves. Two routes are considered different if their sequences of moves are different.
> 
> **Input**
> The input consists of a single line that contains four integers $R, C, U$ and $L$ ($2 \le R, C \le 2000$ and $0 \le U, L \le 2000$), indicating respectively the number of horizontal streets, the number of vertical streets, the required number of Up moves, and the required number of Left moves.
> 
> **Output**
> Output a single line with an integer indicating the number of valid routes. Since this number can be large, output the remainder of dividing it by $998,244,353$.



// MANIM nueva escena // aparece una cuadricula 

En pocas palabreas para no perdernos en el texto: te quieres mover en una cuadrícula desde una esquina de arriba a la izquierda hasta la opuesta usando movimientos 

// MANIM resaltando salida y meta 

hacia la derecha y hacia abajo, pero con una trampa: te tienes que regresar obligatoriamente una cantidad fija de veces hacia arriba o hacia la izquierda ($U$ y $L$ movimientos específicos). 

// MANIM nueva escena cadricula 3x4 

Si pnemos de ejemplo una cuadricula de 3 x 5. Esto quiere decir que si tenemos 0 moviemintos U y cero moviemintos L el sigueinte es por ejemplo un camino valido

// MANIM aparece un camino valido, se difumina, luego otro, y asi

Por ejemplo con 1 movimienot arriba y 3 izquierda, este un camino valido, ... , este es otro, y este es uno dioferente,  ... , y aqui tenemos otro

Pero no se trata de encontrar uno, si no de contar cuantos hay, puede haber demasiados
 
// MANIM aparce uadricula de 2x2

Para que se animen a jugar un poco con el problema, comiencemos con ejemplos pequeños imaginen una cuadrícula pequeña de $2 \times 2$. 


Si queremos ir de la esquina superior izquierda a la inferior derecha usando cero movimientos hacia arriba y cero hacia la izquierda, ¿cuántos caminos válidos tenemos? Exacto, solo dos formas directas. 

// MANIM van aparece unc amino y leugo el toro

Exacto Ir derecha y luego abajo, o primero abajo y luego derecha


¿Y qué pasa si permitimos un movimiento hacia arriba y cero hacia la izquierda? Piénselo un par de segundos... Correcto, tendríamos cuatro caminos diferentes. 



Derecha Izquierda Derecha Abajo
// MANIM  aparece el camino y a la dercha o abajo o enalgun espacio vaio una flecha a rriba una copia de la caudricula en chicuqito con el nuevo camino

Derecha Izquierda Abajo Derecha
// MANIM  aparece el camino y a la dercha o abajo o enalgun espacio vaio una flecha a rriba una copia de la caudricula en chicuqito con el nuevo camino

Derecha Abajo Izquierda Derecha
// MANIM  aparece el camino y a la dercha o abajo o enalgun espacio vaio una flecha a rriba una copia de la caudricula en chicuqito con el nuevo camino
Abajo Derecha Izquierda Derecha
// MANIM  aparece el camino y a la dercha o abajo o enalgun espacio vaio una flecha a rriba una copia de la caudricula en chicuqito con el nuevo camino




Lo verdaderamente elegante y retador aquí no es probar a mano, sino diseñar un algoritmo eficiente que pueda contar estos trayectos para una cuadrícula gigante y para cualquier cantidad arbitraria de desvíos. Si quieren que armemos la solución completa de este problema, déjenlo en los comentarios.

// MANIM animacion de salidiaa de todo 


---

## 3

Voz en off: 
Mientras tanto, veamos cómo operan los equipos en la vida real. Aquí la programación no es un acto solitario; requiere una coordinación milimétrica. Mientras una persona debate la estrategia matemática en la pizarra, otra valida esquemas lógicos en la computadora y la tercera depura código. 

// CLIPS de los de la UADY

Como pueden aqui en la ICPC al reoslver problema se crea una combinacion unica de 
trabajo bajo presión extrem, pensamiento analítico profundo, y resiliencia.Y eso  es exactamente la razón por la cual las empresas tecnológicas más importantes de mexico y del mundo vienen aqui, no es por casualidaad, aqui se encuntrasn empresas como Google claude Jetbrains,Deep Main, Huawei  oracle, entre otras
 stán aquí buscando talento de élite. 



// CLIPS de reclutadores



---

## 4

Voz en off: 
Volviendo de lleno a la competencia: ¿Quiénes ganaron? Hagamos cuentas. 

// MANIM
> **Especificación visual (Manim CE):** Transicionar a un tablero vacío con encabezado “Final Mexicana 2026” y una indicación de que vienen los resultados. Mantener espacio para los conteos siguientes; no anticipar cifras en esta toma.

Iniciamos este camino con **509 equipos** compitiendo a lo largo de las tres fechas clasificatorias. De ese filtro brutal, solo **85 equipos** lograron ganarse un lugar presencial en esta gran final. De ellos, **20 equipos** consiguieron medalla. 

// MANIM
> **Especificación visual (Manim CE):** Mostrar tres niveles conectados: 509 equipos en las clasificatorias → 85 en la final presencial → 20 medallistas. Animar las cifras en ese orden y conservar siempre las etiquetas de cada conjunto. No inferir porcentajes ni hacer parecer que las 20 medallas son otro filtro de clasificación.

Aquí surge una duda muy común: si es una competencia, ¿por qué hay múltiples medallas de oro, plata y bronce en lugar de un solo campeón absoluto como en los Juegos Olímpicos? A diferencia de una competencia de velocidad, la ICPC mide el rendimiento de los equipos contra un estándar global de dificultad y distribución por porcentajes de participación, premiando a los bloques más destacados de la tabla general.

// MANIM
> **Especificación visual (Manim CE):** Presentar un tablero ordenado en bloques de oro, plata y bronce para contrastar múltiples medallas con un campeón único. Añadir una regla esquemática rotulada “estándar global de rendimiento” y una nota de “porcentajes de participación”. No inventar umbrales, porcentajes ni cantidades por medalla: el texto no los especifica. Transicionar de este esquema al tablero real.

Veamos cómo quedó el tablero de los mejores equipos del país en esta final:

// MANIM: tabla de los 25 mejores equipos de la final
> **Especificación visual (Manim CE):** Construir la tabla con puesto, institución, nombre, problemas resueltos y estatus de clasificación. Revelar filas 1–14 y 15–25 en dos paneles o mediante scroll para preservar legibilidad. Mantener el orden y los datos fuente; distinguir “Sí clasificó”, “No” y “No [Invitado / Guest]” con texto además de color. No completar nombres o estatus que la fuente deje incompletos.
1. **ESCOM IPN** — *Domain Expansion "Abraham échate un hint"* (10 problemas — **Sí clasificó**)
2. **CCM** — *Chatcito, Claudecito y Geminicito - Campeones OMI 2026* (10 problemas — **No [Invitado / Guest]**)
3. **U de Guanajuato** — *Soy malo y eso es bueno, yo jamás seré bueno y eso no es malo* (9 problemas — **Sí clasificó**)
4. **UP GDL** — *Prisioneros de Alcatraz* (8 problemas — **Sí clasificó**)
5. **ITESM Monterrey** — *Academia de Pilotaje Aerostático Manuel Doblado (Clases Privadas de Anatomía y Género $100/hr + 529993244386$)* (8 problemas — **Sí clasificó**)
6. **UP Bonaterra** — *The good, the bad and the ugly* (8 problemas — **Sí clasificó**)
7. **FC-UNAM** — *Oasis* (8 problemas — **Sí clasificó**)
8. **U de Guanajuato** — *ICAxiom* (8 problemas — **Sí clasificó**)
9. **IT Culiacan** — *Los guerreros más fuertes de wkoder* (8 problemas — **Sí clasificó**)
10. **UADY** — *Gauss N' Roses* (8 problemas — **Sí clasificó**)
11. **UANL** — *No te preocupes, mención honorífica también es buen resultado* (8 problemas — **Sí clasificó**)
12. **UADY** — *PEScapitalista* (8 problemas — **Sí clasificó**)
13. **Facultad de Ingeniería UNAM** — *:) * (8 problemas — **Sí clasificó**)
14. **UdG CUCEI** — *Adrián quería que nos pusiéramos un nombre largo por alguna razón, y como no decidimos cuál nombre era el mejor, intentamos pedirle al chatcito que nos generara una lista de nombres más atractivos para ICPC. Estos fueron los nombres que nos sugir* (8 problemas — **Sí clasificó**)
15. **ITESM GDA** — *Hijos del Puntero* (7 problemas — **No**)
16. **UADY** — *Tuntunsitos* (7 problems — **No**)
17. **ESCOM IPN** — *Las Chivas de Milito* (7 problemas — **No**)
18. **IT Culiacan** — *AD-HOCK* (7 problemas — **No**)
19. **U de Guanajuato** — *Mäthgic Crüe* (7 problemas — **No**)
20. **FC-UNAM** — *Claude Opus 4.6* (7 problemas — **No**)
21. **ITESM Monterrey** — *Data Divas* (6 problemas — **Sí clasificó**)
22. **ITESM Monterrey** — *ATCSUSMS (Alianza)* (6 problemas — **Sí clasificó**)
23. **UAM A** — *Seal++* (6 problemas — **Sí clasificó**)
24. **UASLP** — *Tacos de Schnauzer* (6 problemas — **Sí clasificó**)
25. **UAEH** — *CapyBaby's* (6 problemas — **Sí clasificó**)

---

## 5

Voz en off: 
Y bien, ¿quiénes avanzan a la siguiente etapa? El objetivo final es conformar a la delegación que representará a México en el **Campeonato Latinoamericano (LATAM Championship)**, donde se medirán las mejores mentes de toda la región. 


Por lógica, esperaríamos que pasen estrictamente los mejores posicionados en la tabla general.

// MANIM: resaltar en verde las filas/estatus de quienes avanzan, según la columna de clasificación.
> **Especificación visual (Manim CE):** Retomar la tabla y marcar en verde el estatus/columna de los equipos que sí avanzan, según los datos del guion. Atenuar el resto sin ocultarlo. Mantener puesto y problemas resueltos visibles y añadir una leyenda textual “clasificó”, de modo que la lectura no dependa solo del color.

Pero aquí nos topamos con una realidad logística: **no siempre es así**. 

Si observan con atención la tabla, se darán cuenta de que hay equipos ubicados entre los lugares 15 y 19 que, 
// MANIM: reslatar de negrita brevemente  (como efecto hover o click)
> **Especificación visual (Manim CE):** Aplicar foco tipo hover a las filas 15–19: contorno o fondo y negritas en la fila, con las demás atenuadas pero legibles. Mantener puesto y número de problemas visibles; retirar el foco antes del siguiente bloque. No atribuir aún una causa de exclusión a cada equipo.
a pesar de haber resuelto más problemas que equipos clasificados más abajo (como los lugares 20 a 25)
// MANIM: reslatar de negrita brevemente (como efecto hover o click)
> **Especificación visual (Manim CE):** Mover el foco a las filas 20–25 y compararlas con 15–19 mediante guías o llaves entre celdas de problemas y estatus, no con flechas de causalidad. Mantener los valores legibles; retirar ambos resaltados al final para enlazar con cuotas, cupos institucionales y sedes.
se quedaron fuera del boleto directo. 

En la ICPC no todo depende exclusivamente del mérito puro en una sola tabla nacional. Factores como cuotas regionales, cupos por institución y el estatus de sedes juegan un papel determinante; a veces, formar parte de una universidad con plazas asignadas te da una ventaja logística frente a equipos de otras sedes que tuvieron un desempeño superior. 

A pesar de estas asperezas reglamentarias, el mérito de cada competidor es innegable. Todos entregaron horas de esfuerzo absoluto sobre el teclado. Muchas felicidades a todos los participantes, y un reconocimiento especial y muchísimo éxito a los equipos que llevarán la bandera de México al LATAM Championship.

---

## 6. 

Voz en off: 
Para cerrar este recorrido, le preguntamos a varios competidores experimentados y entrenadores qué recomendación le darían a los chavos de preparatoria, secundaria o incluso primaria que ya muestran esa chispa por la programación y matematicas y en general las ciencias exactas

// CLIPS: de entrevistas y eso
