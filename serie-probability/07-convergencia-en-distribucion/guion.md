# Video 07: Cuando convergen las sombras, pero no las trayectorias

Dos variables pueden conservar la misma distribución mientras cambian completamente sus valores conjuntos. Se presenta convergencia débil, continuidad de CDF y funciones de prueba.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 519 palabras (3.6–4.3 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Convergencia de leyes en R. No requiere espacio común; cuando se comparan errores sí se especifica un acoplamiento. Helly se llama selección, no continuidad.

## Bibliografía y decisiones matemáticas

Proba §§2.6–2.8, teorema de Portmanteau; §3.1.1 selección de Helly; §3.3 funciones continuas acotadas y Skorokhod.

#### Escena: 01

##### Nombre: Dos películas con la misma sombra

##### Descripcion Breve: Cambiar X por −X conserva una ley simétrica.

##### Objetivo Pedagogico: Separar ley y acoplamiento.

##### Voz en off:

> "[TRIGGER_1] Elige una variable normal centrada X. En pasos pares mostramos X y en impares menos X. [TRIGGER_2] Todos los histogramas tienen exactamente la misma distribución. Pero una trayectoria con X distinto de cero alterna entre dos valores. [TRIGGER_3] La sombra estadística se mantiene mientras la película no converge. Vamos a definir una convergencia que observa esas sombras."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X\sim N(0,1),\quad X_n=(-1)^nX$`.
- MathTex: `$\mathcal L(X_n)=N(0,1)$`.
- Dos campanas idénticas y gráfico alternante de una realización x=1.2; rótulo «realización ilustrativa».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create campana y alternancia.
- [TRIGGER_2]: Transform histogramas superpuestos sin cambios.
- [TRIGGER_3]: Separar paneles ley/trayectoria y formular pregunta.

#### Escena: 02

##### Nombre: La distribución acumulada

##### Descripcion Breve: La CDF registra toda la ley.

##### Objetivo Pedagogico: Definir el objeto que converge.

##### Voz en off:

> "[TRIGGER_1] La función acumulada F de x mide la probabilidad de estar a la izquierda de x, incluyendo el punto. [TRIGGER_2] Es creciente, continua por la derecha y va de cero a uno. Sus saltos son masas puntuales. [TRIGGER_3] Conocer esta función determina la ley sobre los borelianos. Por eso basta estudiar cómo cambian estas curvas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$F_X(x)=P(X\le x)$`.
- MathTex: `$P(X=x)=F_X(x)-F_X(x-)$`.
- CDF Bernoulli con saltos en 0 y 1; selector vertical x; puntos abiertos/cerrados.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create masas y construir CDF.
- [TRIGGER_2]: Mover selector por saltos y mostrar tamaño.
- [TRIGGER_3]: Write propiedades en tres tarjetas y encerrar «determina la ley».

#### Escena: 03

##### Nombre: Los puntos donde no exigimos límite

##### Descripcion Breve: Un átomo que se desplaza revela la condición de continuidad.

##### Objetivo Pedagogico: Definir convergencia débil correctamente.

##### Voz en off:

> "[TRIGGER_1] Si X n vale uno sobre n, converge hacia cero. Sus acumuladas también se acercan, salvo precisamente en el salto de la distribución límite. [TRIGGER_2] En cero, todas las acumuladas anteriores valen cero, mientras la del límite vale uno. [TRIGGER_3] Por eso exigimos convergencia solo en los puntos donde F es continua. El requisito evita rechazar una aproximación perfectamente natural de un átomo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=1/n,\quad F_n(x)=\mathbf1_{[1/n,\infty)}(x)$`.
- MathTex: `$X_n\Rightarrow X\iff F_n(x)\to F(x)\ \forall x\in C(F)$`.
- CDF escalón con salto moviéndose de 1 a 0; línea x=0; valores F_n(0) y F(0).

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create escalón y mover salto.
- [TRIGGER_2]: Resaltar discrepancia en cero.
- [TRIGGER_3]: Write definición y marcar puntos x≠0 como permitidos.

#### Escena: 04

##### Nombre: Detectores continuos

##### Descripcion Breve: Funciones de prueba reemplazan preguntas abruptas.

##### Objetivo Pedagogico: Explicar equivalencia central.

##### Voz en off:

> "[TRIGGER_1] Podemos observar la ley mediante un detector continuo y acotado g. Su lectura media es la esperanza de g de X. [TRIGGER_2] La convergencia débil equivale a que todas esas lecturas converjan. Un detector abrupto justo sobre una masa puede fallar, como nuestro escalón. [TRIGGER_3] Acotado importa: una pequeña masa muy lejana puede conservar un promedio grande, aunque resulte casi invisible a cualquier detector acotado."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n\Rightarrow X\iff\mathbb E g(X_n)\to\mathbb E g(X),\quad g\in C_b(\mathbb R)$`.
- Curva detector g(x)=tanh(x); masas móviles; panel de promedio; tarjeta «equivalencia, teorema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create detector y masas.
- [TRIGGER_2]: Write equivalencia y transformar escalón abrupto en rampa continua.
- [TRIGGER_3]: Mostrar masa 1/n en n y restante en 0; comparar detector acotado con g=x.

#### Escena: 05

##### Nombre: Portmanteau y fronteras

##### Descripcion Breve: Abiertos y cerrados producen cotas de límites.

##### Objetivo Pedagogico: Interpretar continuidad de conjuntos.

##### Voz en off:

> "[TRIGGER_1] La masa puede acercarse a la frontera de un conjunto. Por eso no siempre converge su probabilidad exacta. [TRIGGER_2] Portmanteau da una cota superior para cerrados y una inferior para abiertos. [TRIGGER_3] Si el límite asigna probabilidad cero a la frontera, ambas cotas encajan y obtenemos convergencia. La frontera es el lugar donde una pregunta de sí o no puede cambiar bruscamente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\limsup_nP(X_n\in C)\le P(X\in C)\quad(C\text{ cerrado})$`.
- MathTex: `$\liminf_nP(X_n\in G)\ge P(X\in G)\quad(G\text{ abierto})$`.
- MathTex: `$P(X\in\partial A)=0\Rightarrow P(X_n\in A)\to P(X\in A)$`.
- Intervalo (−1,1), fronteras ±1; masas que se acercan desde fuera; etiquetas abierto/cerrado.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mover masas hacia frontera.
- [TRIGGER_2]: Write dos desigualdades y comparar inclusión del extremo.
- [TRIGGER_3]: Retirar masa de frontera y encajar cotas para A.

#### Escena: 06

##### Nombre: Helly no impide escapar

##### Descripcion Breve: Selección requiere controlar pérdida de masa para obtener una probabilidad.

##### Objetivo Pedagogico: Introducir tightness.

##### Voz en off:

> "[TRIGGER_1] Las acumuladas son monótonas y acotadas. El teorema de selección de Helly permite extraer subsecuencias con límites adecuados en puntos de continuidad. [TRIGGER_2] Pero si X n vale n, toda la masa huye hacia infinito. El límite puntual de las acumuladas en puntos finitos es cero y no es una distribución de probabilidad. [TRIGGER_3] La condición de tightness evita esa fuga: para cada margen de error, un intervalo compacto contiene casi toda la masa uniformemente en n."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=n,\quad F_n(x)\to0$`.
- MathTex: `$\forall\eta>0\ \exists R:\ \sup_nP(|X_n|>R)<\eta$`.
- Masa desplazándose fuera de ventana; flecha de salida; caja [−R,R] ajustable.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create sucesión de escalones y etiqueta Helly.
- [TRIGGER_2]: Mover masa a derecha; Write límite cero y falta de masa.
- [TRIGGER_3]: Create caja compacta y definición de tightness.

#### Escena: 07

##### Nombre: Qué sí implica y qué no

##### Descripcion Breve: Probabilidad implica ley; la recíproca falla salvo límite constante.

##### Objetivo Pedagogico: Conectar con otras convergencias.

##### Voz en off:

> "[TRIGGER_1] Si X n se acerca a X en probabilidad, también convergen sus leyes. Podemos acotar la acumulada entre versiones desplazadas de F más la probabilidad de error. [TRIGGER_2] La recíproca falla con la alternancia normal del inicio: las leyes coinciden, pero la distancia al X original no desaparece. [TRIGGER_3] Cuando el límite es constante c, sí hay equivalencia: la masa acaba concentrándose en cualquier vecindad de c. Allí ya no queda una distribución extendida que pueda ocultar el acoplamiento."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$F(x-\varepsilon)-P(|X_n-X|>\varepsilon)\le F_n(x)\le F(x+\varepsilon)+P(|X_n-X|>\varepsilon)$`.
- MathTex: `$X_n\xrightarrow P X\Rightarrow X_n\Rightarrow X$`.
- MathTex: `$X_n\Rightarrow c\iff X_n\xrightarrow P c$`.
- CDF y versiones desplazadas; bandas de error; alternancia normal y átomo c.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write cotas en renglones y enviar n→∞, luego ε↓0.
- [TRIGGER_2]: Restaurar alternancia y mostrar P(2|X|>ε)>0 en índices impares.
- [TRIGGER_3]: Concentrar masa en c y dibujar vecindad arbitraria.

#### Escena: 08

##### Nombre: La sombra como objetivo legítimo

##### Descripcion Breve: Distribuciones sirven para promedios y cuantiles.

##### Objetivo Pedagogico: Cerrar con alcance claro.

##### Voz en off:

> "[TRIGGER_1] A veces no queremos reproducir cada historia, sino la distribución de resultados de un experimento. [TRIGGER_2] La convergencia débil es exactamente adecuada para detectores continuos acotados y probabilidades de conjuntos con fronteras sin masa. [TRIGGER_3] Recordemos qué información conservó la sombra y cuál perdió. Una buena coincidencia de histogramas es evidencia sobre leyes; por sí sola no demuestra proximidad de trayectorias."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{leyes}\longrightarrow\text{observables continuos acotados}$`.
- Histograma y CDF sincronizados; película alternante en miniatura; lista de observables válidos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create dos distribuciones cercanas.
- [TRIGGER_2]: Indicate detector y conjunto de frontera nula.
- [TRIGGER_3]: Cerrar con ley y trayectoria en recintos distintos.

