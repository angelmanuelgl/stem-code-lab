Aquí tienes únicamente la extracción de las voces en off organizadas por escena:

**Escena 01:**
¿Cómo podrías calcular tres elevado a la un millón... en tan solo 21 pasos? Si intentaras resolverlo multiplicando tres por tres, una y otra vez, la computadora tendría que realizar un millón de multiplicaciones individuales. Hoy descubriremos cómo la exponenciación binaria reduce ese proceso astronómico a un par de parpadeos.

**Escena 02:**
Antes de buscar la velocidad, enfrentemos un problema aún peor: el resultado final de tres elevado a la un millón contiene más de cuatrocientos setenta mil dígitos. Para ponerlo en perspectiva, el número total de átomos en todo el universo observable es de apenas diez elevado a la ochenta, una cifra de solo ochenta dígitos. No existe memoria RAM en la Tierra capaz de almacenar este número completo de forma nativa.

**Escena 03:**
Por esta razón, en programación competitiva y criptografía usamos Aritmética Modular. Imagina un reloj circular tipico de 12 horas. Si son las 9 y le sumas 7 horas, no dices que son las 16, sino las 4. Encerraste el resultado en un reloj de 12 horas. De la misma forma, acotamos los números gigantes en un reloj con un número primo grande, como diez a la nueve más siete, manteniendo cada multiplicación dentro de los límites seguros de un entero estándar.

**Escena 04:**
Analicemos la estrategia tradicional con un ejemplo más pequeño: tres elevado a la ocho. La definición básica nos dice que debemos multiplicar tres por sí mismo ocho veces. Contemos los pasos: comenzamos con 3. Multiplicamos por 3 y llevamos 1 paso para obtener 3 al cuadrado... paso 2 para 3 al cubo... paso 3 para 3 a la cuarta... y así sucesivamente hasta el paso 7 para llegar a 3 a la octava. Para un exponente n, este método requiere n menos 1 multiplicaciones.

**Escena 05:**
Ahora si, como funciona la exponenciacion binaria, piensa en esto ¿Y si en lugar de avanzar de uno en uno, duplicáramos el exponente en cada paso? Observa esto: tres por tres nos da tres al cuadrado en un solo paso. Pero si ahora multiplicamos tres al cuadrado por tres al cuadrado, obtenemos tres a la cuarta inmediatamente. Y si multiplicamos tres a la cuarta por tres a la cuarta, ¡llegamos a tres a la octava! ¡Pasamos de 7 multiplicaciones a solo 3 pasos!

**Escena 06:**
Esta estrategia de elevación al cuadrado funciona perfecto para 2, 4, 8, 16, 32 o 1024... Pero, ¿qué ocurre si el exponente NO es una potencia exacta de dos? Por ejemplo, ¿cómo calculamos tres elevado a la 25? No podemos saltar directamente a 25 solo elevando al cuadrado. ¿Estamos atrapados o existe una forma de construir 25 combinando nuestras potencias cuadradas?  

**Escena 07:**
La clave está en cómo las computadoras ven los números: en sistema binario. Cualquier entero puede expresarse como una suma única de potencias de dos. Si tomamos el exponente 25 y lo convertimos a binario, obtenemos 1 1 0 0 1. Esto significa que 25 es igual a 16 más 8 más 1. Por la ley de los exponentes, tres a la 25 es igual a tres a la 16, por tres a la 8, por tres a la 1. ¡Solo necesitamos multiplicar las potencias donde el bit sea igual a 1!

**Escena 08:**
Ejecutemos el algoritmo paso a paso. Mantenemos una variable resultado en 1 y nuestra base inicial en 3. Leemos los bits de derecha a izquierda:

* Bit 1 (peso 1): ¡Está encendido! Multiplicamos resultado por la base (1 x 3 = 3). Elevamos la base al cuadrado (3^2 = 9).
* Bit 2 (peso 2): Está en 0. Conservamos resultado, pero elevamos la base al cuadrado (9^2 = 81).
* Bit 3 (peso 4): Está en 0. Conservamos resultado, base pasa a 81^2 = 6561.
* Bit 4 (peso 8): ¡Encendido! Multiplicamos resultado por 6561. Elevamos base a 3^16.
* Bit 5 (peso 16): ¡Encendido! Multiplicamos resultado por 3^16. ¡Listo! En solo 5 iteraciones calculamos 3^{25}.

**Escena 09:**
Traducir esto a código es sorprendentemente sencillo e intuitivo. Usamos un ciclo mientras el exponente sea mayor a cero. Si el bit menos significativo está encendido, multiplicamos nuestro resultado por la base actual. En cada paso, elevamos la base al cuadrado y desplazamos el exponente un bit a la derecha. Como la cantidad de bits de un número n es logaritmo base dos de n, la complejidad temporal es O de log n.

**Escena 10:**
Ahora entiendes el verdadero poder de la exponenciación binaria. Lo que a un enfoque ingenuo le tomaría un millón de multiplicaciones iterativas, la representación binaria y la elevación al cuadrado lo resuelven en solo 20 operaciones dentro de cualquier procesador. La próxima vez que veas un exponente gigante, no le temas: solo descompónlo en bits. ¡Suscríbete para más algoritmos explicados con rigor visual!