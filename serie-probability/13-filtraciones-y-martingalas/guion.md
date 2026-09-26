# Video 13: Juegos justos, información y el momento de parar

Se desarrolla el lenguaje de procesos, filtraciones y martingalas mediante apuestas causales, con ejemplos y límites de parada opcional.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 580 palabras (4–4.8 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Tiempo discreto para demostraciones; extensión continua explícita con regularidad. Doob L² se enuncia. Se evita equiparar martingala con independencia o Markov.

## Bibliografía y decisiones matemáticas

Proba §4.2: esperanza condicional y torre. Complemento de consulta: [Lawler, capítulos 1 y 2](https://www.math.uchicago.edu/~lawler/finbook.pdf). Ejemplos y demostraciones de este guion se calculan desde la definición.

#### Escena: 01

##### Nombre: Mirar el futuro cambia el juego

##### Descripcion Breve: Dos estrategias difieren en la información usada.

##### Objetivo Pedagogico: Motivar adaptación.

##### Voz en off:

> "[TRIGGER_1] Jugamos con incrementos de más uno o menos uno, equiprobables e independientes. Elegir una apuesta antes de cada tirada parece justo. [TRIGGER_2] Si alguien puede ver la siguiente tirada y elegir después el signo de su apuesta, gana siempre. El experimento aleatorio es el mismo; cambió el acceso a la información. [TRIGGER_3] Para hablar de juegos justos debemos incluir explícitamente qué sabe cada estrategia y cuándo lo sabe."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(\xi_k=\pm1)=1/2,\quad S_n=\sum_{k=1}^n\xi_k$`.
- Moneda siguiente oculta tras cortina; estrategia causal y estrategia que mira detrás; ganancias Hkξk.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create tiradas y cortina.
- [TRIGGER_2]: Revelar trampa Hk=ξk y ganancia 1.
- [TRIGGER_3]: Restaurar cortina y escribir «información disponible antes de actuar».

#### Escena: 02

##### Nombre: Filtración y proceso

##### Descripcion Breve: La información crece mientras las variables se indexan por tiempo.

##### Objetivo Pedagogico: Definir los objetos básicos.

##### Voz en off:

> "[TRIGGER_1] Un proceso es una familia de variables aleatorias indexadas por el tiempo. Fijar el tiempo da una variable; fijar el resultado da una trayectoria. [TRIGGER_2] Una filtración es una familia creciente de sigma álgebras: todo lo que sabíamos antes sigue disponible después. [TRIGGER_3] Un proceso adaptado tiene su valor actual medible con la información actual. Para una apuesta del siguiente paso, exigimos que el coeficiente sea conocido antes del nuevo incremento."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathcal F_n=\sigma(\xi_1,\ldots,\xi_n),\quad\mathcal F_n\subset\mathcal F_{n+1}$`.
- MathTex: `$X_n\text{ adaptado}\iff X_n\text{ es }\mathcal F_n\text{-medible}$`.
- MathTex: `$H_k\text{ es }\mathcal F_{k-1}\text{-medible}$`.
- Matriz tiempo/resultado; cajas de información anidadas; línea Hk antes de ξk.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create matriz y dos cortes.
- [TRIGGER_2]: Create cajas de filtración.
- [TRIGGER_3]: Colocar Hk a la izquierda de ξk y Write condición de predictibilidad discreta.

#### Escena: 03

##### Nombre: Martingala es un promedio condicional

##### Descripcion Breve: La condición de juego justo se expresa con toda la historia disponible.

##### Objetivo Pedagogico: Dar la definición y un ejemplo probado.

##### Voz en off:

> "[TRIGGER_1] Una martingala es adaptada, integrable en cada tiempo y satisface que su valor futuro esperado dada la información presente coincide con su valor presente. [TRIGGER_2] La caminata simétrica cumple esto: los incrementos futuros son independientes del pasado y tienen media cero. [TRIGGER_3] La definición condiciona respecto de toda la información F n, no solo respecto del número S n. Una martingala no tiene por qué ser un proceso de Markov."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E|M_n|<\infty,\quad\mathbb E[M_m\mid\mathcal F_n]=M_n\ (m\ge n)$`.
- MathTex: `$\mathbb E[S_m\mid\mathcal F_n]=S_n+\sum_{k=n+1}^m\mathbb E[\xi_k\mid\mathcal F_n]=S_n$`.
- Árbol de futuros desde un nodo; promedio de hojas sobre posición actual; tarjeta «toda F_n».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create árbol y posición actual.
- [TRIGGER_2]: Write cálculo de caminata y cancelar medias futuras.
- [TRIGGER_3]: Resaltar F_n y separar etiqueta martingala de etiqueta Markov.

#### Escena: 04

##### Nombre: Tres direcciones del promedio

##### Descripcion Breve: Submartingalas y supermartingalas permiten tendencias condicionales.

##### Objetivo Pedagogico: Distinguir media condicional de monotonía de trayectorias.

##### Voz en off:

> "[TRIGGER_1] Si el promedio futuro es al menos el presente, hablamos de submartingala; si es a lo sumo, supermartingala. [TRIGGER_2] Eso no obliga a cada trayectoria a subir o bajar. La condición es sobre una esperanza condicionada. [TRIGGER_3] Para la caminata simétrica, S n cuadrada menos n es martingala: cada nuevo incremento añade una unidad de segundo momento. La fluctuación tiene un coste cuadrático acumulativo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[M_{n+1}\mid\mathcal F_n]\ge M_n\quad\text{submartingala}$`.
- MathTex: `$\mathbb E[M_{n+1}\mid\mathcal F_n]\le M_n\quad\text{supermartingala}$`.
- MathTex: `$\mathbb E[S_{n+1}^2\mid\mathcal F_n]=S_n^2+1$`.
- Tres árboles con centros de masa por encima/igual/debajo; expansión (Sn+ξ)²; trayectorias que fluctúan en todos los casos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create árboles y medias.
- [TRIGGER_2]: Mostrar una trayectoria descendente dentro de submartingala.
- [TRIGGER_3]: Expandir cuadrado y Write Sn²−n martingala.

#### Escena: 05

##### Nombre: Cuándo se puede decidir parar

##### Descripcion Breve: El primer cruce usa información disponible.

##### Objetivo Pedagogico: Definir tiempo de parada y contrastar con anticipación.

##### Voz en off:

> "[TRIGGER_1] Un tiempo de parada permite decidir si ya ocurrió usando únicamente lo observado hasta el momento. El primer instante en que alcanzamos una barrera cumple esto. [TRIGGER_2] El último máximo antes de un horizonte normalmente no: para saber si este fue el último, necesitamos mirar lo que queda. [TRIGGER_3] La condición formal pide que el evento de haber parado antes de n pertenezca a F n. Esa condición será indispensable al detener procesos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\tau=\inf\{n:S_n\ge3\},\quad\{\tau\le n\}\in\mathcal F_n$`.
- MathTex: `$\tau\text{ tiempo de parada}\iff\{\tau\le n\}\in\mathcal F_n\ \forall n$`.
- Trayectoria revelada progresivamente; barrera 3; candidato a último máximo oculto por cortina.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create primer cruce y congelar al alcanzarlo.
- [TRIGGER_2]: Mostrar dos futuros compatibles que cambian el último máximo.
- [TRIGGER_3]: Write criterio medible junto al reloj detenido.

#### Escena: 06

##### Nombre: Parar no fabrica ganancias sin condiciones

##### Descripcion Breve: Un horizonte acotado conserva esperanza, uno ilimitado exige cuidado.

##### Objetivo Pedagogico: Enunciar parada opcional con alcance.

##### Voz en off:

> "[TRIGGER_1] Para una martingala y un tiempo de parada acotado por N, la esperanza al parar coincide con la inicial. Se ve escribiendo la suma de incrementos multiplicados por la indicadora de no haber parado. [TRIGGER_2] Esa indicadora depende del pasado, así que cada término tiene esperanza cero. [TRIGGER_3] Si quitamos la cota N, no podemos pasar al límite sin una condición adicional, por ejemplo integrabilidad uniforme de la familia detenida. Las estrategias de duplicar apuestas esconden precisamente ese problema."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$M_\tau=M_0+\sum_{k=1}^N\mathbf1_{\{\tau\ge k\}}(M_k-M_{k-1})$`.
- MathTex: `$\tau\le N\Rightarrow\mathbb EM_\tau=\mathbb EM_0$`.
- Suma de ganancias hasta parada; compuertas indicadoras; tarjeta horizonte acotado; escalera de apuestas 1,2,4,8.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write suma detenida.
- [TRIGGER_2]: Mostrar cada compuerta conocida en F_{k−1} y cancelar su esperanza.
- [TRIGGER_3]: Extender escalera de apuestas y marcar que desaparece la hipótesis acotada.

#### Escena: 07

##### Nombre: La desigualdad de Doob mira todo el recorrido

##### Descripcion Breve: Una martingala L2 tiene máximo controlado por su valor terminal.

##### Objetivo Pedagogico: Preparar estimaciones de procesos.

##### Voz en off:

> "[TRIGGER_1] Controlar el valor final no parece controlar todos los picos anteriores. La estructura de martingala permite hacerlo mediante la desigualdad de Doob. [TRIGGER_2] Para una martingala cuadrado integrable, la esperanza del máximo cuadrado hasta T no supera cuatro veces el segundo momento terminal. En tiempo continuo usamos una versión regular, por ejemplo continua. [TRIGGER_3] Aquí enunciamos el teorema; lo utilizaremos para controlar diferencias entre aproximaciones. Su trabajo es convertir una estimación terminal en una estimación de trayectorias completas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E\left[\sup_{0\le t\le T}|M_t|^2\right]\le4\mathbb E|M_T|^2$`.
- Trayectoria con máximo y final distintos; rótulo «Doob L²: teorema»; barras de segundos momentos, no una desigualdad trayectoria a trayectoria.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create trayectoria y máximo.
- [TRIGGER_2]: Write desigualdad bajo esperanza y subrayar el promedio.
- [TRIGGER_3]: Conectar segundo momento terminal con control del supremo.

#### Escena: 08

##### Nombre: Apuestas predecibles e integración

##### Descripcion Breve: Las sumas de ganancias preservan la martingala.

##### Objetivo Pedagogico: Tender puente hacia integral de Itô.

##### Voz en off:

> "[TRIGGER_1] Si H k es conocido antes del incremento y está acotado, la suma de H k por los incrementos de una martingala vuelve a ser martingala. [TRIGGER_2] La prueba repite nuestra idea inicial: sacar lo conocido fuera de la esperanza condicional y usar que el incremento promedia cero. [TRIGGER_3] Al pasar a tiempo continuo construiremos integrales con esa misma regla de información. El extremo izquierdo importa porque representa una decisión tomada antes de recibir el nuevo ruido."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$G_n=\sum_{k=1}^nH_k(M_k-M_{k-1})$`.
- MathTex: `$\mathbb E[H_k\Delta M_k\mid\mathcal F_{k-1}]=H_k\,\mathbb E[\Delta M_k\mid\mathcal F_{k-1}]=0$`.
- Escalones Hk y trayectoria Mk alineados; compuertas de tiempo; flecha discreto→continuo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create coeficientes anteriores a cada incremento.
- [TRIGGER_2]: Write cálculo condicional.
- [TRIGGER_3]: Refinar malla sin usar información futura y cerrar sobre pregunta de integral continua.

