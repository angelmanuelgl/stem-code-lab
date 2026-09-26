<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 


### Nombre: 


### Descripcion Breve:


### Objetivo Pedagogico:


### Voz en off:


### Descripcion Visual Detallda:

#### Objetos:

#### Layout y disposicion:s 


### Secuencia de animacion: 


### Código Cromático y Estilo:


<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
# Guion Técnico Completo: Exponenciación Binaria
## Sistema Visual y Paleta de Colores (Modern Flat - Dark Mode)

### Definición de Paleta Cromática para Manim

* **Fondo Principal (Background):** `#181C24` (Gris Pizarra Oscuro / Slate Dark Cold Gray)
* **Texto / Fórmulas Primarias:** `#ECEFF4` (Blanco Plata Suave)
* **Elementos Neutros / Secundarios:** `#64748B` (Gris Pizarra Medio)
* **Énfasis Naive / Advertencias / Overflow ($O(n)$):** `#C0392B` (Vino / Borgoña Profundo)
* **Énfasis Óptimo / Bits Activos ($O(\log n)$):** `#2DD4BF` (Verde Sabio / Menta Desaturado)
* **Exponentes / Llamadas de Atención:** `#D97706` (Naranja Terracota / Ámbar Cálido)
* **Bases / Variables de Control:** `#6366F1` (Azul Índigo Pizarra)
* **Contenedores / Módulo / Marcas:** `#38BDF8` (Cian Frío Suave)


<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 01


### Nombre: 01_gancho_imposible


### Descripcion Breve:

Presentación del problema inicial calculando 3^{1000000} y comparación entre la fuerza bruta de 1,000,000 de operaciones y la solución algorítmica en 21 pasos.


### Objetivo Pedagogico:

Capturar la atención del espectador exponiendo la ineficiencia del algoritmo ingenuo lineal e introducir la promesa del tiempo logarítmico.

 
### Voz en off:

¿Cómo podrías calcular tres elevado a la un millón... [TRIGGER_1] en tan solo 21 pasos? [TRIGGER_2] Si intentaras resolverlo multiplicando tres por tres, una y otra vez, la computadora tendría que realizar un millón de multiplicaciones individuales [TRIGGER_3]. Hoy descubriremos cómo la exponenciación binaria reduce ese proceso astronómico a un par de parpadeos [TRIGGER_4].


### Descripcion Visual Detallda:

#### Objetos:
* Texto LaTeX central principal: a^{n} = 3^{1000000}
* Contador numérico digital desbordante a la izquierda: Multiplicaciones: 0 -> 1,000,000
* Badge destacado a la derecha: Pasos con Exponenciación Binaria: 21
* Barra de progreso horizontal asociada al algoritmo ingenuo

#### Layout y disposicion:s 
* Expresión 3^{1000000} posicionada en UP * 1.5 en el centro
* Contador secuencial en LEFT * 3.5 + DOWN * 1.0
* Badge destacado en RIGHT * 3.5 + DOWN * 1.0


### Secuencia de animacion: 

1. [TRIGGER_1]: Aparece la expresión LaTeX 3^{1000000} mediante Write(). El exponente 1000000 se ilumina en Terracota (#D97706).
2. [TRIGGER_2]: Surge el cuadro del badge derecho "Pasos: 21" mediante un escalado dinámico FadeIn(scale=0.6) con borde Verde Sabio (#2DD4BF).
3. [TRIGGER_3]: A la izquierda, un contador rápido incrementa aceleradamente desde 1 hasta 1,000,000 acompañado por una barra de progreso que se llena en color Vino Borgoña (#C0392B).
4. [TRIGGER_4]: El contador en Vino se fragmenta y se desvanece con FadeOut(), mientras la fórmula central 3^{1000000} y el badge de 21 Pasos se reconfiguran al centro de la pantalla.


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Exponente principal: Naranja Terracota (#D97706)
* Énfasis ingenuo (O(n)): Vino Borgoña (#C0392B)
* Énfasis óptimo (O(log n)): Verde Sabio (#2DD4BF)
* Texto primario: Blanco Plata (#ECEFF4)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 02


### Nombre: 02_obstaculo_memoria


### Descripcion Breve:

Explicación del desbordamiento de memoria (overflow) comparando el tamaño en dígitos de 3^{1000000} con el número de átomos en el universo observable.


### Objetivo Pedagogico:

Demostrar que la fuerza bruta falla no solo por tiempo de cómputo, sino por imposibilidad física de almacenar un entero con más de 470,000 dígitos.


### Voz en off: vc 

Antes de buscar la velocidad, enfrentemos un problema aún peor: [TRIGGER_1] el resultado final de tres elevado a la un millón contiene más de cuatrocientos setenta mil dígitos [TRIGGER_2]. Para ponerlo en perspectiva, el número total de átomos en todo el universo observable [TRIGGER_3] es de apenas diez elevado a la ochenta, una cifra de solo ochenta dígitos [TRIGGER_4]. No existe memoria RAM en la Tierra capaz de almacenar este número completo de forma nativa [TRIGGER_5].


### Descripcion Visual Detallda:

#### Objetos:
* Bloque de dígitos desplazable simulando una secuencia masiva: 563... [477,121 dígitos] ...187
* Ilustración vectorial minimalista del Universo Observable (círculo estilizado con nodos astrales)
* Ecuaciones comparativas: \text{Dígitos } 3^{1000000} \approx 477,121 vs \text{Átomos Universo} \approx 10^{80}
* Ícono vectorial de Chip de Memoria con indicador de OVERFLOW

#### Layout y disposicion:s 
* Cadena flotante de dígitos en UP * 2.2
* Gráfico del universo a la izquierda en LEFT * 3.0 + DOWN * 0.8
* Cifras comparativas LaTeX a la derecha en RIGHT * 2.5 + DOWN * 0.8


### Secuencia de animacion: 

1. [TRIGGER_1]: Se despliega un bloque de texto denso lleno de dígitos que fluyen lateralmente saliendo de los bordes del encuadre.
2. [TRIGGER_2]: Aparece un recuadro de aviso en Vino Borgoña (#C0392B) con la leyenda "477,121 dígitos".
3. [TRIGGER_3]: Dibujo sutil mediante Create() de la ilustración del universo observable a la izquierda.
4. [TRIGGER_4]: Se escribe a la derecha en Cian Suave (#38BDF8) la cifra 10^{80} \text{ átomos}. Una línea punteada conecta y resalta la desproporción de escalas.
5. [TRIGGER_5]: El ícono del chip de memoria parpadea en Borgoña con un símbolo de advertencia y texto "OVERFLOW".


### Código Cromático it Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Cadena de dígitos: Gris Pizarra Medio (#64748B)
* Magnitud atómica: Cian Suave (#38BDF8)
* Alerta Overflow: Vino Borgoña (#C0392B)
* Marco de resaltado: Naranja Terracota (#D97706)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 03


### Nombre: 03_aritmetica_modular


### Descripcion Breve:

Introducción a la Aritmética Modular usando la analogía del reloj de 12 horas para acotar los resultados intermedios dentro del entero primo M = 10^9 + 7.


### Objetivo Pedagogico:

Comprender cómo el operador módulo mantiene todas las operaciones dentro de los límites de 64 bits sin perder la corrección del cálculo.


### Voz en off:

Por esta razón, en programación competitiva y criptografía usamos Aritmética Modular [TRIGGER_1]. Imagina un reloj circular [TRIGGER_2]. Si son las 9 y le sumas 7 horas, no dices que son las 16, sino las 4 [TRIGGER_3]. Encerraste el resultado en un reloj de 12 horas. De la misma forma, acotamos los números gigantes en un reloj con un número primo grande, como diez a la nueve más siete [TRIGGER_4], manteniendo cada multiplicación dentro de los límites seguros de un entero estándar [TRIGGER_5].


### Descripcion Visual Detallda:

#### Objetos:
* Reloj circular analógico minimalista con divisiones del 0 al 11
* Aguja indicadora vectorial giratoria
* Expresión matemática modular: (9 + 7) \pmod{12} = 4
* Transformación de la constante modular: M = 10^9 + 7 (1,000,000,007)
* Caja contenedora de seguridad con el límite de bits

#### Layout y disposicion:s 
* Reloj de aritmética circular centrado a la izquierda en LEFT * 2.8
* Ecuaciones LaTeX alineadas a la derecha en RIGHT * 2.2 + UP * 0.5
* Caja de rango seguro en RIGHT * 2.2 + DOWN * 1.8


### Secuencia de animacion: 

1. [TRIGGER_1]: Aparece el título superior "Aritmética Modular: Módulo M" en Azul Índigo (#6366F1).
2. [TRIGGER_2]: Se dibuja el dial circular del reloj con sus 12 posiciones usando ShowCreation().
3. [TRIGGER_3]: La aguja parte del número 9, gira 7 posiciones en sentido horario atravesando el origen y se detiene en el 4. En paralelo se escribe (9 + 7) \pmod{12} = 4.
4. [TRIGGER_4]: El reloj de 12 divisiones se transforma mediante ReplacementTransform() en un contenedor circular denotado como M = 10^9 + 7.
5. [TRIGGER_5]: Aparece un recuadro protector en Verde Sabio (#2DD4BF) rodeando la fórmula (A \times B) \pmod{10^9 + 7} con el texto "Límite de 64 bits Respetado".


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Dial del reloj / Contenedor M: Azul Índigo (#6366F1)
* Aguja / Indicador: Naranja Terracota (#D97706)
* Módulo Primo: Cian Suave (#38BDF8)
* Confirmación de seguridad: Verde Sabio (#2DD4BF)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 04


### Nombre: 04_algoritmo_naive


### Descripcion Breve:

Demostración de la ineficiencia del método iterativo lineal O(n) calculando 3^8 paso a paso mediante 7 multiplicaciones consecutivas.


### Objetivo Pedagogico:

Formalizar la relación entre el valor del exponente n y el número de multiplicaciones requeridas (n - 1) en el enfoque tradicional.


### Voz en off:

Analicemos la estrategia tradicional con un ejemplo más pequeño: tres elevado a la ocho [TRIGGER_1]. La definición básica nos dice que debemos multiplicar tres por sí mismo ocho veces [TRIGGER_2]. Contemos los pasos: comenzamos con 3 [TRIGGER_3]. Multiplicamos por 3 y llevamos 1 paso para obtener 3 al cuadrado [TRIGGER_4]... paso 2 para 3 al cubo... paso 3 para 3 a la cuarta... y así sucesivamente hasta el paso 7 para llegar a 3 a la octava [TRIGGER_5]. Para un exponente n, este método requiere n menos 1 multiplicaciones [TRIGGER_6].


### Descripcion Visual Detallda:

#### Objetos:
* Expresión expandida: 3^8 = 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3
* Tabla de progreso de pasos iterativos (Paso 1 a Paso 7)
* Contador dinámico de operaciones ejecutadas
* Etiqueta de complejidad temporal O(n)

#### Layout y disposicion:s 
* Expresión desplegada arriba en UP * 2.2
* Tabla de pasos descendente centrada en ORIGIN
* Etiqueta de complejidad en DOWN * 2.5


### Secuencia de animacion: 

1. [TRIGGER_1]: Surge la fórmula 3^8 centrada en pantalla mediante Write().
2. [TRIGGER_2]: El término 3^8 se descompone horizontalmente en una cadena de 8 treses multiplicados.
3. [TRIGGER_3]: Aparece la primera fila: "Paso 0: 3".
4. [TRIGGER_4]: Una llave inferior agrupa los dos primeros términos, mostrando "Paso 1: 3^2 = 9".
5. [TRIGGER_5]: Animación acelerada que despliega sucesivamente los renglones hasta llegar a "Paso 7: 3^8 = 6561".
6. [TRIGGER_6]: Todos los pasos se encierran en un recuadro de resaltado Vino Borgoña (#C0392B) con la etiqueta "Complejidad Lineal: O(n)".


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Cadena de factores: Blanco Plata (#ECEFF4)
* Pasos acumulativos: Naranja Terracota (#D97706)
* Contenedor de complejidad O(n): Vino Borgoña (#C0392B)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 05


### Nombre: 05_intuicion_central


### Descripcion Breve:

Explicación del salto conceptual clave: reutilizar resultados anteriores mediante elevación al cuadrado continua para calcular 3^8 en solo 3 pasos.


### Objetivo Pedagogico:

Inculcar la intuición del crecimiento exponencial de las potencias mediante autoproducto (3 -> 3^2 -> 3^4 -> 3^8).


### Voz en off:

¿Y si en lugar de avanzar de uno en uno, duplicáramos el exponente en cada paso? [TRIGGER_1] Observa esto: tres por tres nos da tres al cuadrado en un solo paso [TRIGGER_2]. Pero si ahora multiplicamos tres al cuadrado por tres al cuadrado, obtenemos tres a la cuarta inmediatamente [TRIGGER_3]. Y si multiplicamos tres a la cuarta por tres a la cuarta, ¡llegamos a tres a la octava! [TRIGGER_4] ¡Pasamos de 7 multiplicaciones a solo 3 pasos! [TRIGGER_5]


### Descripcion Visual Detallda:

#### Objetos:
* Cadena horizontal de nodos interconectados: 3 \xrightarrow{x^2} 3^2 \xrightarrow{x^2} 3^4 \xrightarrow{x^2} 3^8
* Flechas de transformación curvas superiores indicando autoproducto
* Badge comparativo de ahorro: "7 pasos vs 3 pasos"

#### Layout y disposicion:s 
* Cadena de potencias alineada horizontalmente en ORIGIN
* Flechas de elevación al cuadrado con radio superior en UP * 1.2
* Cuadro de comparación en RIGHT * 3.2 + DOWN * 2.0


### Secuencia de animacion: 

1. [TRIGGER_1]: Aparece el primer nodo con el valor "3" a la izquierda en LEFT * 4.5.
2. [TRIGGER_2]: Una flecha curva verde brota de 3 sobre sí mismo y genera mediante ReplacementTransform() el nodo "3^2 = 9" (Paso 1).
3. [TRIGGER_3]: Una segunda flecha conecta "3^2" con sí mismo para generar "3^4 = 81" (Paso 2).
4. [TRIGGER_4]: Una tercera flecha conecta "3^4" con sí mismo produciendo "3^8 = 6561" (Paso 3).
5. [TRIGGER_5]: Surge a la derecha una tarjeta de contraste en Verde Sabio (#2DD4BF) resaltando: "Reducción del 57% en operaciones".


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Nodos de potencias: Azul Índigo (#6366F1)
* Flechas de autoproducto (x^2): Verde Sabio (#2DD4BF)
* Destacado de optimización: Naranja Terracota (#D97706)
* Texto de resultado: Blanco Plata (#ECEFF4)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 06


### Nombre: 06_dilema_exponentes


### Descripcion Breve:

Planteamiento del conflicto al enfrentar un exponente que no es potencia exacta de 2, utilizando 3^{25} como caso de estudio.


### Objetivo Pedagogico:

Motivar la necesidad de un método de descomposición general cuando la duplicación directa no aterriza exactamente en el exponente objetivo.


### Voz en off:

Esta estrategia de elevación al cuadrado funciona perfecto para 2, 4, 8, 16, 32 o 1024... [TRIGGER_1] Pero, ¿qué ocurre si el exponente NO es una potencia exacta de dos? [TRIGGER_2] Por ejemplo, ¿cómo calculamos tres elevado a la 25? [TRIGGER_3] No podemos saltar directamente a 25 solo elevando al cuadrado [TRIGGER_4]. ¿Estamos atrapados o existe una forma de construir 25 combinando nuestras potencias cuadradas? [TRIGGER_5]


### Descripcion Visual Detallda:

#### Objetos:
* Recta numérica con marcas en potencias de dos: 1, 2, 4, 8, 16, 32
* Expresión objetivo destacada: 3^{25} con signo de interrogación
* Flecha de salto interrumpida que intenta alcanzar el punto 25 sobre la recta

#### Layout y disposicion:s 
* Lista de potencias exactas en la parte superior UP * 2.2
* Expresión 3^{25} en el centro del encuadre
* Recta numérica horizontal en DOWN * 1.5


### Secuencia de animacion: 

1. [TRIGGER_1]: Iluminación secuencial en la recta de los puntos 2 \to 4 \to 8 \to 16 \to 32 en Verde Sabio (#2DD4BF).
2. [TRIGGER_2]: Aparece una marca de advertencia en color Naranja Terracota (#D97706) sobre la posición 25.
3. [TRIGGER_3]: Escribir la expresión 3^{25} en el centro. El exponente 25 parpadea para llamar la atención.
4. [TRIGGER_4]: Una flecha curva intenta saltar desde el nodo 16 hacia el 25, pero se interrumpe a mitad de trayecto mostrando una "X" en Borgoña (#C0392B).
5. [TRIGGER_5]: Surge la pregunta en la parte superior: "¿Cómo construir 25 a partir de potencias de 2?" mediante FadeIn().


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Potencias exactas de 2: Verde Sabio (#2DD4BF)
* Exponente desalineado (25): Naranja Terracota (#D97706)
* Salto fallido: Vino Borgoña (#C0392B)
* Texto de pregunta: Blanco Plata (#ECEFF4)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 07


### Nombre: 07_secreto_binario


### Descripcion Breve:

Explicación de la descomposición binaria del exponente 25 en 11001_2 (16 + 8 + 1) y su aplicación mediante leyes de los exponentes.


### Objetivo Pedagogico:

Conectar la representación binaria con la propiedad de multiplicación de bases iguales a^{x+y} = a^x \cdot a^y.


### Voz en off:

La clave está en cómo las computadoras ven los números: en sistema binario [TRIGGER_1]. Cualquier entero puede expresarse como una suma única de potencias de dos [TRIGGER_2]. Si tomamos el exponente 25 y lo convertimos a binario, obtenemos 1 1 0 0 1 [TRIGGER_3]. Esto significa que 25 es igual a 16 más 8 más 1 [TRIGGER_4]. Por la ley de los exponentes, tres a la 25 es igual a tres a la 16, por tres a la 8, por tres a la 1 [TRIGGER_5]. ¡Solo necesitamos multiplicar las potencias donde el bit sea igual a 1! [TRIGGER_6]


### Descripcion Visual Detallda:

#### Objetos:
* Arreglo de casillas cuadradas para los bits: [1] [1] [0] [0] [1]
* Etiquetas superiores con los pesos posicionales: 2^4 (16), 2^3 (8), 2^2 (4), 2^1 (2), 2^0 (1)
* Ecuación algebraica: 3^{25} = 3^{16 + 8 + 1} = 3^{16} \cdot 3^8 \cdot 3^1
* Recuadros de selección activa en los bits en '1'

#### Layout y disposicion:s 
* Arreglo binario centrado en UP * 1.2
* Etiquetas de peso posicional en UP * 2.2
* Descomposición de exponentes en DOWN * 1.5


### Secuencia de animacion: 

1. [TRIGGER_1]: Aparece el número decimal "25" en el centro de la pantalla.
2. [TRIGGER_2]: El número 25 se divide mediante animación en sus componentes (16 + 8 + 1).
3. [TRIGGER_3]: Las celdas del arreglo binario emergen mostrando la secuencia [1] [1] [0] [0] [1].
4. [TRIGGER_4]: Debajo de las celdas se revelan los valores 16, 8, 4, 2, 1. Celdas con bit '1' se encienden en Verde Sabio (#2DD4BF), mientras que las celdas '0' permanecen en Gris Pizarra (#64748B).
5. [TRIGGER_5]: Se despliega la fórmula 3^{25} = 3^{16} \cdot 3^8 \cdot 3^1.
6. [TRIGGER_6]: Los factores 3^{16}, 3^8 y 3^1 reciben un borde en Naranja Terracota (#D97706).


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Bit '1' encendido: Verde Sabio (#2DD4BF)
* Bit '0' apagado: Gris Pizarra (#64748B)
* Factores seleccionados: Naranja Terracota (#D97706)
* Celdas contenedor: Azul Índigo (#6366F1)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 08


### Nombre: 08_traza_algoritmo


### Descripcion Breve:

Simulación interactiva paso a paso de la traza del algoritmo evaluando el acumulador `res` y la base cuadrática `base` en cada bit de 11001_2.


### Objetivo Pedagogico:

Visualizar la mecánica interna de mantener la variable `base` elevándose al cuadrado continuamente mientras `res` junta únicamente las potencias activas.


### Voz en off:

Ejecutemos el algoritmo paso a paso [TRIGGER_1]. Mantenemos una variable resultado en 1 y nuestra base inicial en 3 [TRIGGER_2]. Leemos los bits de derecha a izquierda:
* Bit 1 (peso 1): ¡Está encendido! Multiplicamos resultado por la base (1 x 3 = 3). Elevamos la base al cuadrado (3^2 = 9) [TRIGGER_3].
* Bit 2 (peso 2): Está en 0. Conservamos resultado, pero elevamos la base al cuadrado (9^2 = 81) [TRIGGER_4].
* Bit 3 (peso 4): Está en 0. Conservamos resultado, base pasa a 81^2 = 6561 [TRIGGER_5].
* Bit 4 (peso 8): ¡Encendido! Multiplicamos resultado por 6561. Elevamos base a 3^16 [TRIGGER_6].
* Bit 5 (peso 16): ¡Encendido! Multiplicamos resultado por 3^16 [TRIGGER_7]. ¡Listo! En solo 5 iteraciones calculamos 3^{25} [TRIGGER_8].


### Descripcion Visual Detallda:

#### Objetos:
* Arreglo binario horizontal con puntero móvil debajo: 1  1  0  0  1
* Panel de variables en tiempo real: `res` (acumulador), `base` (potencia actual)
* Registro lateral de operaciones aritméticas en ejecución
* Flecha indicadora de posición de bit procesado

#### Layout y disposicion:s 
* Arreglo binario superior en UP * 2.5
* Panel de variables a la izquierda en LEFT * 3.0 + DOWN * 0.5
* Log de operaciones ejecutadas a la derecha en RIGHT * 2.5 + DOWN * 0.5


### Secuencia de animacion: 

1. [TRIGGER_1]: Se estructuran los paneles de monitoreo de variables en pantalla.
2. [TRIGGER_2]: Se inicializan los valores `res = 1` y `base = 3`. El puntero se ubica bajo el bit 1 (extremo derecho).
3. [TRIGGER_3]: Bit 1 destella en Verde Sabio. `res` cambia a 3. `base` se eleva a 9. Puntero avanza a la izquierda.
4. [TRIGGER_4]: Bit 0 permanece en Gris. `res` se mantiene en 3. `base` se eleva a 81. Puntero avanza.
5. [TRIGGER_5]: Bit 0 permanece en Gris. `res` se mantiene en 3. `base` se eleva a 6561. Puntero avanza.
6. [TRIGGER_6]: Bit 1 destella. `res` realiza 3 \times 6561 = 19683. `base` pasa a 3^{16}. Puntero avanza.
7. [TRIGGER_7]: Bit 1 destella. `res` se multiplica por 3^{16} \pmod M.
8. [TRIGGER_8]: El puntero completa la lectura. Un resplandor en Verde Sabio (#2DD4BF) confirma la finalización exitosa.


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Variable `res`: Verde Sabio (#2DD4BF)
* Variable `base`: Azul Índigo (#6366F1)
* Puntero de lectura: Cian Suave (#38BDF8)
* Destacado de multiplicación: Naranja Terracota (#D97706)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 09


### Nombre: 09_codigo_complejidad


### Descripcion Breve:

Presentación del código fuente en C++/Python e ilustración gráfica de la curva de complejidad logarítmica O(log n) frente a la curva lineal O(n).


### Objetivo Pedagogico:

Relacionar la manipulación de bits a nivel de código (`b & 1`, `b >>= 1`) con la reducción de la complejidad temporal a escala logarítmica.


### Voz en off:

Traducir esto a código es sorprendentemente sencillo e intuitivo [TRIGGER_1]. Usamos un ciclo mientras el exponente sea mayor a cero [TRIGGER_2]. Si el bit menos significativo está encendido, multiplicamos nuestro resultado por la base actual [TRIGGER_3]. En cada paso, elevamos la base al cuadrado y desplazamos el exponente un bit a la derecha [TRIGGER_4]. Como la cantidad de bits de un número n es logaritmo base dos de n, la complejidad temporal es O de log n [TRIGGER_5].


### Descripcion Visual Detallda:

#### Objetos:
* Ventana de código con formato sintáctico:
```cpp
long long binpow(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}
```
* Gráfica comparativa de ejes cartesiano: Curva O(\log n) vs Recta O(n)

#### Layout y disposicion:s 
* Ventana de código a la izquierda en LEFT * 2.2
* Plano cartesiano de complejidad a la derecha en RIGHT * 3.0


### Secuencia de animacion: 

1. [TRIGGER_1]: Aparece la ventana de código con fondo oscuro (#181C24) mediante FadeIn().
2. [TRIGGER_2]: Se resalta la línea `while (b > 0)` con un fondo suave en Azul Índigo (#6366F1).
3. [TRIGGER_3]: Se ilumina la condición de verificación de bit `if (b & 1)`.
4. [TRIGGER_4]: Se iluminan en Naranja Terracota (#D97706) las líneas de actualización `a = (a * a) % m` y `b >>= 1`.
5. [TRIGGER_5]: En el gráfico de la derecha se traza la pared vertical roja de O(n) frente a la curva plana verde de O(\log n).


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Fondo de Código: #11141A
* Curva O(log n): Verde Sabio (#2DD4BF)
* Curva O(n): Vino Borgoña (#C0392B)
* Resaltado sintáctico: Cian Suave (#38BDF8)



<!-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -->
## Escena: 10


### Nombre: 10_conclusion_cierre


### Descripcion Breve:

Resumen del impacto algorítmico, retorno a la pregunta del gancho inicial y llamada a la acción (CTA).


### Objetivo Pedagogico:

Consolidar la comprensión del valor pragmático de los algoritmos logarítmicos y cerrar el ciclo narrativo del video.


### Voz en off:

Ahora entiendes el verdadero poder de la exponenciación binaria [TRIGGER_1]. Lo que a un enfoque ingenuo le tomaría un millón de multiplicaciones iterativas [TRIGGER_2], la representación binaria y la elevación al cuadrado lo resuelven en solo 20 operaciones dentro de cualquier procesador [TRIGGER_3]. La próxima vez que veas un exponente gigante, no le temas: solo descompónlo en bits [TRIGGER_4]. ¡Suscríbete para más algoritmos explicados con rigor visual!


### Descripcion Visual Detallda:

#### Objetos:
* Comparativa final en pantalla completa: 1,000,000 Pasos vs 20 Pasos
* Ecuación final resuelta: 3^{1000000} \pmod{10^9+7} = \text{Resultado}
* Tarjeta final CTA (Suscribirse / Video Recomendado)

#### Layout y disposicion:s 
* Módulo comparativo superior en UP * 1.5
* Fórmula final en el centro (ORIGIN)
* Elementos de CTA en DOWN * 2.2


### Secuencia de animacion: 

1. [TRIGGER_1]: Reaparece la expresión inicial 3^{1000000} \pmod{10^9+7} en el centro.
2. [TRIGGER_2]: Se muestra la cifra "1,000,000 de pasos" siendo cancelada por una marca "X" en Vino Borgoña (#C0392B).
3. [TRIGGER_3]: La cifra "20 Pasos" destella con destellos vectoriales en Verde Sabio (#2DD4BF).
4. [TRIGGER_4]: Transición suave mediante FadeOut() general para dar paso a la pantalla final de llamada a la acción y suscripción.


### Código Cromático y Estilo:

* Fondo: Gris Pizarra Oscuro (#181C24)
* Cifra cancelada: Vino Borgoña (#C0392B)
* Cifra ganadora: Verde Sabio (#2DD4BF)
* Destacado de conclusión: Naranja Terracota (#D97706)
* Texto de cierre: Blanco Plata (#ECEFF4)