# Video 15: La curva que se mueve infinitamente y acumula un tiempo finito

Se demuestra variación cuadrática browniana en L², casi segura en mallas diádicas y variación total infinita.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 522 palabras (3.6–4.3 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- T>0 fijo; particiones deterministas. No se identifican variación total y longitud de la gráfica. La tabla diferencial se presenta como abreviatura.

## Bibliografía y decisiones matemáticas

Proba §§2.3–2.4 y Probita §3.2 para tipos de convergencia y Borel-Cantelli. Consulta complementaria: [Lawler §2.8](https://www.math.uchicago.edu/~lawler/finbook.pdf). El cálculo de momentos gaussianos y la prueba están explicitados.

#### Escena: 01

##### Nombre: Dos contadores para una curva

##### Descripcion Breve: Se comparan sumas de incrementos absolutos y cuadrados.

##### Objetivo Pedagogico: Motivar variación total y cuadrática.

##### Voz en off:

> "[TRIGGER_1] Recorremos una trayectoria y sumamos cada cambio en valor absoluto. Después repetimos sumando sus cuadrados. [TRIGGER_2] Al refinar la malla, estos dos contadores se comportan de maneras muy distintas para el Browniano. [TRIGGER_3] No estamos midiendo simplemente el desplazamiento final: subir y bajar se cancelaría allí. Queremos medir la actividad que permanece aunque el proceso regrese al origen."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$V_\pi(X)=\sum_i|\Delta X_i|,\quad Q_\pi(X)=\sum_i(\Delta X_i)^2$`.
- Una trayectoria sobre T=1; mallas 8,32,128; dos contadores; incrementos verticales señalados, sin llamar a Vπ longitud euclidiana de la gráfica.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create recorrido e incrementos.
- [TRIGGER_2]: Calcular ambos contadores con la misma malla.
- [TRIGGER_3]: Mostrar desplazamiento final separado y señalar cancelaciones.

#### Escena: 02

##### Nombre: Una curva suave pierde sus cuadrados

##### Descripcion Breve: Variación finita y continuidad obligan a Qπ a cero.

##### Objetivo Pedagogico: Identificar qué falla en el caso browniano.

##### Voz en off:

> "[TRIGGER_1] Para una función continua de variación finita, cada cuadrado está acotado por el mayor incremento absoluto multiplicado por ese incremento absoluto. [TRIGGER_2] Al sumar, aparece máximo incremento por variación total. El primero tiende a cero por continuidad uniforme y el segundo permanece acotado. [TRIGGER_3] Por eso la variación cuadrática desaparece para curvas suaves. Ese es el hábito del cálculo ordinario que el Browniano va a romper."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Q_\pi(f)\le\left(\max_i|\Delta f_i|\right)\sum_i|\Delta f_i|$`.
- MathTex: `$f\text{ continua, }V(f)<\infty\Rightarrow Q_\pi(f)\to0$`.
- Curva f(t)=t²; malla refinándose; producto de una barra que decrece y otra acotada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create curva y cuadrados de incrementos.
- [TRIGGER_2]: Write cota factorizada.
- [TRIGGER_3]: Refinar malla y animar máximo hacia cero, manteniendo V=1.

#### Escena: 03

##### Nombre: El promedio de los cuadrados brownianos

##### Descripcion Breve: Cada incremento aporta su duración.

##### Objetivo Pedagogico: Calcular EQπ exactamente.

##### Voz en off:

> "[TRIGGER_1] En el Browniano, un incremento en un intervalo de longitud delta t es normal centrado con varianza delta t. [TRIGGER_2] Su cuadrado tiene esperanza delta t. Sumamos sobre una partición de cero a T y obtenemos exactamente T. [TRIGGER_3] Esto todavía es una afirmación de promedio. Necesitamos controlar cuánto fluctúa la suma alrededor de T para demostrar una convergencia."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Delta W_i\sim N(0,\Delta t_i),\quad\mathbb E(\Delta W_i)^2=\Delta t_i$`.
- MathTex: `$\mathbb E Q_\pi(W)=\sum_i\Delta t_i=T$`.
- Partición no uniforme [0,0.1,0.4,0.7,1]; rectángulos de duración y cuadrados esperados; contador total T=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create incrementos y varianzas.
- [TRIGGER_2]: Transform cada cuadrado esperado a duración.
- [TRIGGER_3]: Concatenar duraciones y Write EQπ=T, con rótulo «aún solo esperanza».

#### Escena: 04

##### Nombre: Las fluctuaciones también desaparecen

##### Descripcion Breve: Independencia y cuarto momento normal dan convergencia L2.

##### Objetivo Pedagogico: Demostrar Qπ→T.

##### Voz en off:

> "[TRIGGER_1] Para una normal centrada de varianza delta t, el cuarto momento es tres veces delta t cuadrada. La varianza de su cuadrado es entonces dos veces delta t cuadrada. [TRIGGER_2] Los incrementos son independientes, por lo que las varianzas de esos cuadrados se suman. [TRIGGER_3] Esa suma no supera dos T por el tamaño máximo de la malla. Al refinar, el error cuadrático medio tiende a cero: hemos demostrado convergencia en L dos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\operatorname{Var}((\Delta W_i)^2)=3(\Delta t_i)^2-(\Delta t_i)^2=2(\Delta t_i)^2$`.
- MathTex: `$\mathbb E|Q_\pi(W)-T|^2=2\sum_i(\Delta t_i)^2\le2T|\pi|\to0$`.
- Barras de varianza por intervalo; malla máxima |π| destacada; dispersión de Qπ sobre 2000 trayectorias, semilla 1501.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write cuarto momento y restar cuadrado de la media.
- [TRIGGER_2]: Sumar varianzas resaltando independencia.
- [TRIGGER_3]: Write cota y reducir |π|; histograma ilustrativo se concentra cerca de T.

#### Escena: 05

##### Nombre: De L2 a casi segura en mallas diádicas

##### Descripcion Breve: Una cota sumable permite usar Borel-Cantelli.

##### Objetivo Pedagogico: Precisar el sentido del límite por trayectoria.

##### Voz en off:

> "[TRIGGER_1] Sobre particiones diádicas, el error cuadrático tiene cota proporcional a dos elevado a menos n. Chebyshev convierte esto en una serie sumable de probabilidades de error. [TRIGGER_2] Borel-Cantelli da convergencia casi segura para cada tolerancia racional positiva y por tanto para todas. [TRIGGER_3] Así podemos escoger un mismo conjunto de trayectorias donde las sumas diádicas convergen a T. Para particiones arbitrarias no afirmamos automáticamente el mismo resultado casi seguro."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\pi_n=\{kT/2^n:0\le k\le2^n\}$`.
- MathTex: `$P(|Q_{\pi_n}-T|>\varepsilon)\le\frac{2T^2}{\varepsilon^2\,2^n}$`.
- MathTex: `$Q_{\pi_n}\to T\quad\text{c.s.}$`.
- Mallas diádicas anidadas y una trayectoria fija; serie geométrica de cotas; tarjeta de sentido de convergencia.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create mallas coherentes.
- [TRIGGER_2]: Write Chebyshev y sumar cotas.
- [TRIGGER_3]: Aplicar Borel-Cantelli y encerrar «diádicas, c.s.».

#### Escena: 06

##### Nombre: Por qué la variación total es infinita

##### Descripcion Breve: Continuidad y variación cuadrática positiva contradicen variación finita.

##### Objetivo Pedagogico: Probar rugosidad sin usar solo expectativas.

##### Voz en off:

> "[TRIGGER_1] Supongamos que una trayectoria browniana continua tuviera variación total finita en [0,T]. [TRIGGER_2] La desigualdad que demostramos para curvas de variación finita obligaría a que sus sumas cuadráticas diádicas tendieran a cero. [TRIGGER_3] Pero casi seguramente esas sumas tienden a T positivo. Contradicción: la variación total es infinita casi seguramente. Este argumento sí habla de trayectorias; que una esperanza creciera a infinito no habría bastado por sí solo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$T>0,\quad Q_{\pi_n}(W)\to T\text{ c.s.}$`.
- MathTex: `$V(W;[0,T])<\infty\Rightarrow Q_{\pi_n}(W)\to0$`.
- MathTex: `$V(W;[0,T])=\infty\quad\text{c.s.}$`.
- Dos rutas desde hipótesis V<∞ hacia límite 0 y desde Browniano hacia T; intersección del conjunto de continuidad y el de convergencia.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write hipótesis por contradicción.
- [TRIGGER_2]: Mostrar ruta de cota máximo×variación.
- [TRIGGER_3]: Contrastar 0 con T>0 y concluir fuera de un conjunto nulo.

#### Escena: 07

##### Nombre: Los términos mixtos desaparecen

##### Descripcion Breve: Tiempo y ruido tienen escalas diferentes.

##### Objetivo Pedagogico: Preparar la tabla de Itô con límites.

##### Voz en off:

> "[TRIGGER_1] La suma de los cuadrados de delta t tiende a cero. Los productos delta t por delta W también desaparecen: Cauchy-Schwarz los controla por las raíces de las dos sumas cuadráticas. [TRIGGER_2] Los cuadrados de delta W, en cambio, conservan T. [TRIGGER_3] La notación dW cuadrado igual a dt resume estas reglas de acumulación. No es una igualdad entre dos números infinitesimales ordinarios."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\sum_i(\Delta t_i)^2\le T|\pi|\to0$`.
- MathTex: `$\left|\sum_i\Delta t_i\Delta W_i\right|\le\sqrt{\sum_i(\Delta t_i)^2}\sqrt{\sum_i(\Delta W_i)^2}\to0$`.
- MathTex: `$(dt)^2=0,\quad dt\,dW=0,\quad(dW)^2=dt\quad\text{regla de cálculo}$`.
- Tres columnas tiempo², tiempo×ruido, ruido²; barras de sumas; etiqueta «abreviatura de límites».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write cota determinista.
- [TRIGGER_2]: Aplicar Cauchy-Schwarz a término mixto.
- [TRIGGER_3]: Transform resultados a tabla heurística y rotular su significado.

#### Escena: 08

##### Nombre: Una regla de cadena necesita una corrección

##### Descripcion Breve: La identidad para el cuadrado retiene un término adicional.

##### Objetivo Pedagogico: Cerrar con el origen del término de Itô.

##### Voz en off:

> "[TRIGGER_1] Para cualquier par de números, el cambio de un cuadrado es dos veces el valor anterior por el incremento, más el incremento al cuadrado. [TRIGGER_2] Al sumar sobre Browniano, el segundo término no desaparece: converge a T. [TRIGGER_3] Por eso el cálculo estocástico retiene una corrección que el cálculo suave descarta. La variación cuadrática nos explica qué hay que conservar antes de aprender una fórmula nueva."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_T^2-W_0^2=2\sum_iW_{t_i}\Delta W_i+\sum_i(\Delta W_i)^2$`.
- MathTex: `$\sum_iW_{t_i}\Delta W_i\to\frac12(W_T^2-T)$`.
- Áreas algebraicas de un cuadrado: dos rectángulos y cuadrado pequeño; sumatoria telescópica; resultado W_T²−T.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create identidad geométrica de (a+b)².
- [TRIGGER_2]: Sumar y telescopar los cambios de W².
- [TRIGGER_3]: Transform suma cuadrática a T y despejar la suma izquierda.

