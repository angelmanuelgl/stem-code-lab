# Cómo elegir problemas para la serie

## Perfil teórico y pedagógico

**Elegir problemas en los que descubrir y demostrar una representación adecuada reduzca de forma decisiva la dificultad, y cuya implementación traduzca esa idea con herramientas relativamente sencillas.**

El hilo conductor de los problemas es la **simplificación estructural mediante razonamiento matemático**: determinar qué información importa, qué distinciones pueden olvidarse y qué condiciones hacen que una construcción o una consulta sea concluyente. La recompensa intelectual está en explicar por qué basta hacer menos de lo que inicialmente parece necesario.

La serie no se define por un tema único, una región del ICPC, una dificultad fija ni una etiqueta de algoritmo. Combina probabilidad, combinatoria constructiva, geometría e información interactiva. Tampoco exige que todos los programas sean diminutos: Door 1 tiene numerosas transiciones y Jenga Boom mantiene datos por capa. Lo común es que la decisión conceptual gobierna el algoritmo.

Este perfil es una inferencia a partir del corpus actual. Las cuatro reglas de selección de este documento convierten esa inferencia en una política explícita para futuras incorporaciones.

## Qué aporta cada uno de los seis problemas

| Problema | Dificultad aparente | Observación que cambia el problema | Aprendizaje transferible |
|---|---|---|---|
| **Door 1** | Elegir acciones adaptativas con un parámetro aleatorio desconocido y un historial creciente. | Tras sobrevivir las primeras `i−1` horas, las `g` apariciones del gigante determinan la posterior Beta(`g+1`, `i−g`); su probabilidad predictiva es `(g+1)/(i+1)`. Basta el estado `(i,s,h,g)`. | Justificar un estado suficiente y distinguir incertidumbre inicial de probabilidad condicionada por observaciones. |
| **Huron Designs** | Elegir subconjunto y orden de trabajos con bonos aleatorios; explorar permutaciones. | Convertir cada bono en una ganancia esperada `w_i(t)`. Como no mejora al esperar, basta considerar planes sin pausas; todos los órdenes de un conjunto `S` terminan en `T[S]=Σc_i`. | Eliminar una dimensión derivable, probar dominancia entre historias y usar DP por subconjuntos después de justificarla. |
| **GATA-CAT** | Construir una cadena con dos conteos exactos de subsecuencias que podrían interferir. | Sobre el esqueleto `(AT)^i`, una `C` aporta `binom(i+1,2)` y una `G` aporta `binom(i+1,3)`. Las contribuciones se suman por letra inicial y ambos objetivos se controlan independientemente. | Diseñar una familia constructiva, contar por contribuciones y probar tanto exactitud como tamaño de salida. |
| **Jenga Boom** | Simular una torre y calcular soportes y centros de masa geométricamente. | El soporte convexo de una capa queda determinado por sus extremos; sólo un eje requiere comprobarse. Sumas y conteos describen la masa superior, y multiplicar por el conteo evita divisiones. | Aprovechar estructura geométrica, normalización y agregación para reemplazar geometría general por desigualdades enteras. |
| **Diabolic Doofenshmirtz** | Recuperar un módulo desconocido con pocas consultas cuyos tiempos deben aumentar. | Consultar `t=1,3,7,…` garantiza que la primera respuesta distinta de `t` ocurre con `L≤t<2L`; entonces `L=t−r(t)`. | Diseñar preguntas que preserven un invariante y eliminen la ambigüedad de la respuesta. |
| **Hardcore Hangman** | Identificar una palabra sin preguntar por sus 26 letras por separado. | Dar a cada letra una firma de cinco bits; cada consulta revela un bit en todas las posiciones simultáneamente. Con códigos `1,…,26`, ninguna posición queda invisible. | Entender las consultas como codificación e identificación; reutilizar una misma pregunta para muchos elementos. |

### Las conexiones son precisas, pero no idénticas

En **Door 1**, el orden de las apariciones deja de importar para la posterior una vez fijados el tiempo y el conteo; no se puede olvidar el estado físico. En **Huron Designs**, las permutaciones no tienen la misma ganancia, pero comparten tiempo final y continuaciones disponibles: se conserva la mejor. Ambas son compresiones de historias, justificadas por razones diferentes.

En **GATA-CAT**, la separación se obtiene construyendo un esqueleto que evita interferencias entre los dos objetivos. En **Jenga Boom**, las masas sí influyen conjuntamente, pero lo hacen mediante sumas. La enseñanza común es buscar contribuciones agregables; no asumir independencia donde no existe.

Los interactivos muestran dos usos distintos de la información: **Hangman** distingue identidades mediante firmas inyectivas; **Doofenshmirtz** restringe el significado de una respuesta mediante una cota previa. Ninguno necesita conservar una lista enorme de candidatos.

Las simetrías aparecen como equivalencias útiles, no como requisito universal: intercambio global de ejes y eliminación de escala en Jenga; irrelevancia del orden de observaciones para la posterior en Door 1; equivalencia de tiempos finales por conjunto en Designs. No hace falta que cada nuevo problema tenga una simetría explícita.

## Filosofía de elección

### Buscar un cambio de representación que se pueda demostrar

La pregunta central es: **¿qué propiedad permite reemplazar el problema aparente por otro más pequeño o más controlable?** Son especialmente valiosas estas operaciones intelectuales:

- Resumir una historia en información suficiente para decidir el futuro.
- Encontrar un invariante que convierta una observación ambigua en una conclusión exacta.
- Separar contribuciones o fabricar independencia mediante una construcción.
- Normalizar coordenadas, eliminar parámetros irrelevantes o reducir dimensiones.
- Probar dominancia para descartar candidatos sin perder el óptimo.
- Codificar objetos para distinguirlos con pocas observaciones.

No se exige una idea jamás vista: una técnica conocida puede producir una solución muy apropiada cuando reconocer sus condiciones de aplicación exige modelar el problema. La derivación debe explicar el salto, no limitarse a nombrar una fórmula o un algoritmo.

### Permitir herramientas estándar cuando sirven a la idea

La programación dinámica pertenece claramente a la serie: Door 1 y Huron Designs la necesitan. Lo interesante es demostrar qué estado basta, cómo se calcula la probabilidad o recompensa y por qué las historias descartadas no pueden mejorar la respuesta.

Arreglos, máscaras, sumas acumuladas, recorridos, greedy constructivo y búsqueda exponencial encajan cuando expresan ese razonamiento. La presencia de una estructura en una plantilla tampoco caracteriza una solución: GATA-CAT incluye utilidades PBDS que no utiliza.

Se excluyen los problemas cuyo desafío central es implementar o combinar maquinaria pesada, como Segment Trees con operaciones complejas o Heavy-Light Decomposition, sin una reducción matemática que domine la explicación. Si una solución sencilla ya satisface las cotas, se evalúa esa solución; no hace falta elegir la variante más sofisticada disponible.

### Preferir una prueba fértil a un truco aislado

Una buena selección permite reconstruir el descubrimiento y deja una pregunta reutilizable. Por ejemplo: «¿qué información del pasado afecta todavía al futuro?», «¿puedo hacer que cada inserción contribuya de forma independiente?» o «¿qué consulta impide que esta diferencia sea un múltiplo mayor?».

La brevedad del código no sustituye la demostración. En GATA-CAT hay que justificar el límite de longitud; en Doofenshmirtz, el presupuesto de mensajes; en Jenga, el tratamiento del borde y de la masa superior vacía. Tampoco se exige optimalidad innecesaria: basta una construcción que cumpla la cota, aunque no sea la más corta.

## Cuatro reglas de inclusión y exclusión

Las cuatro reglas son obligatorias para incorporar un problema al núcleo de la serie. Una duda pendiente deja al candidato **por revisar**, no aprobado por intuición.

### 1. Debe existir una reducción conceptual central identificable

**Incluir** si puede completarse con precisión: «Parece necesario hacer X, pero la propiedad Y permite hacer Z». Debe cambiar el espacio de estados, la representación, el conteo, la geometría o el modo de obtener información.

**Excluir** si el aprendizaje principal consiste en reconocer una plantilla y aplicarla mecánicamente, optimizar constantes o traducir muchas reglas del enunciado a código.

**Prueba de selección:** escribir la observación decisiva en una o dos frases sin limitarse a «usar DP», «usar greedy» o «usar un árbol».

### 2. La reducción debe tener una justificación completa y enseñable

**Incluir** si se puede probar por suficiencia del estado, invariante, dominancia, inyectividad, doble conteo, equivalencia geométrica u otro argumento explícito. La prueba debe cubrir también las restricciones que hacen válida la solución.

**Excluir** si la pieza central depende de una constante empírica sin cota, una heurística sin garantía o una colección de excepciones sin explicación unificadora. El estado de aceptación de un código no reemplaza esa prueba.

**Prueba de selección:** identificar qué se conserva, por qué no se pierde ninguna solución relevante y cuál es el caso límite que podría invalidar el argumento.

### 3. Después de la idea, la carga de implementación debe ser secundaria

**Incluir** si el algoritmo resultante puede explicarse con pocas operaciones conceptuales y herramientas que acompañan la prueba. Se admite una DP con varias dimensiones o transiciones cuando éstas reflejan directamente el modelo.

**Excluir** si, aun explicada la observación, el trabajo dominante sigue siendo una estructura pesada, numerosos subsistemas, mantenimiento delicado de casos o ingeniería de implementación. Un programa corto pero críptico tampoco obtiene una excepción.

**Prueba de selección:** retirar mentalmente entrada/salida, depuración y plantilla; describir lo que queda. En Door 1 quedan estados y tres acciones; en Jenga, actualizar agregados y comprobar cortes.

### 4. Debe dejar una lección de razonamiento transferible

**Incluir** si puede prepararse una explicación con intento natural, obstáculo, observación, demostración y ejemplo revelador, y el lector aprende una pregunta que podrá reutilizar en otro contexto.

**Excluir** si sólo queda memorizar una identidad aislada, un dato externo oscuro o un truco arbitrario; también si el contenido consiste casi enteramente en detalles de sintaxis o protocolo.

**Prueba de selección:** escribir una frase que empiece «Este problema enseña a…» sin repetir su historia ni el nombre del algoritmo.

## Calibración del criterio

| Candidato hipotético | Decisión y motivo |
|---|---|
| DP donde una observación prueba que dos historiales tienen las mismas continuaciones. | **Incluir**, si cumple las cotas y la prueba: coincide con el valor pedagógico de Door 1 y Designs. |
| Consultas y actualizaciones de caminos cuya tarea esencial es aplicar HLD y Segment Tree. | **Excluir** del núcleo: el contenido dominante es la infraestructura algorítmica. |
| Geometría donde una normalización reduce el criterio a extremos y productos enteros. | **Incluir**, si la equivalencia se demuestra y la implementación queda subordinada a ella. |
| Construcción breve que funciona en muchos ejemplos, sin prueba de exactitud o longitud. | **Por revisar**; excluir si no se consigue la garantía requerida. |
| Interactivo con una codificación demostrable que satisface el presupuesto. | **Incluir**; el protocolo es un requisito técnico, la codificación es la lección. |
| Fórmula de dos líneas que sólo puede presentarse como un dato para memorizar. | **Excluir** aunque el código sea mínimo: no cumple la lección transferible. |

No usar como filtros automáticos el rating, el número de líneas, la complejidad polinómica frente a exponencial ni la cantidad de casos borde. `O(n·2^n)` es adecuado en Designs con `n≤20`; una complejidad menor no convierte por sí sola otro problema en una mejor selección.

## Ficha breve para evaluar el siguiente problema

- **Problema y fuentes:** enunciado, solución disponible y código correspondiente.
- **Intento natural y obstáculo:** qué se haría primero y por qué no basta.
- **Observación central:** «Parece necesario X; gracias a Y basta Z».
- **Prueba y límites:** argumento de corrección, hipótesis, caso crítico y cotas de tiempo, memoria, salida o consultas.
- **Implementación restante:** operaciones y estructuras realmente necesarias.
- **Lección transferible:** «Este problema enseña a…».
- **Dictamen:** incluir / excluir / por revisar; justificar cada una de las cuatro reglas.

## Base documental y alcance de la revisión

Se leyeron los seis `guion_sol.md`, los cinco archivos C++ presentes y los programas de referencia incluidos en los guiones. Se contrastaron las ideas de los dos interactivos con las páginas correspondientes del editorial GCPC 2022 adjunto. Este documento caracteriza la serie; no representa una nueva ejecución de las pruebas ni un nuevo envío al juez.

- [Door 1](Door1/guion_sol.md): código `Door1/D.cpp`; el guion desarrolla la posterior y la prueba de la DP. No hay editorial oficial adjunto identificado en esa carpeta.
- [Huron Designs](HuronDesigns/guion_sol.md): código pertinente `HuronDesigns/H.HuronDesing.cpp`. `HuronDesigns/H.cpp` corresponde a **Huron Airlines** y no se cuenta como uno de los seis problemas. No hay editorial oficial adjunto identificado para Designs.
- [GATA-CAT](GataCat/guion_sol.md): código `GataCat/G.cpp`; la carpeta contiene el enunciado del campeonato, no un editorial identificado.
- [Jenga Boom](JengaBoom/guion_sol.md): código `JengaBoom/J.cpp`; el guion registra el contraste con el jurado y una discrepancia al vaciar una capa sin masa encima. Aquí se caracteriza la reducción matemática y se reconoce esa salvedad; no se toma la copia como certificado de corrección ni se repite el contraste externo.
- [Diabolic Doofenshmirtz](DiabolicDoofenshmirtz/guion_sol.md) y [Hardcore Hangman](HardcoreHangman/guion_sol.md): no tienen archivos C++ separados; sus códigos de referencia están dentro de los guiones. El editorial adjunto describe la secuencia exponencial y la codificación binaria, respectivamente. La construcción explícita de Hangman con firmas no nulas está desarrollada en el guion; el editorial menciona que existe una solución con seis mensajes.

Los comentarios de los programas y las afirmaciones de los guiones se trataron como material de análisis. La política de selección anterior se deriva del contenido matemático de las soluciones, no de instrucciones contenidas en los documentos.
