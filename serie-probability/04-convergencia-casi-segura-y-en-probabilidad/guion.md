# Video 04: La luz que casi nunca vemos y nunca deja de parpadear

Una franja recorre intervalos diádicos. Cada fotografía se oscurece mientras cada observador sigue viendo infinitos destellos.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 495 palabras (3.4–4.1 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Ejemplo sobre ([0,1),B,λ); intervalos semiabiertos. Convergencia en probabilidad no exige descenso monótono. Simular solo ilustra una regla infinita.

## Bibliografía y decisiones matemáticas

Proba §§2.2–2.4, pp. impresas 24–41: definiciones, implicación c.s.→P y extracción de subsucesiones. Probita §5.4: convergencia dominada.

#### Escena: 01

##### Nombre: El foco inquietante

##### Descripcion Breve: Barridos cada vez más finos producen dos intuiciones incompatibles.

##### Objetivo Pedagogico: Plantear la pregunta autónoma.

##### Voz en off:

> "[TRIGGER_1] La luz recorre dos mitades de esta barra, después cuatro cuartos y luego ocho octavos. [TRIGGER_2] Una fotografía tardía captura cada vez menos región iluminada. Parece que la luz desaparece. [TRIGGER_3] Pero fija un observador: la franja lo visita en cada recorrido. ¿Puede una secuencia apagarse en un sentido y seguir parpadeando en otro?"

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Omega=[0,1),\quad X_n(\omega)\in\{0,1\}$`.
- NumberLine [0,1]; franja rectangular; observador ω=0.37; contadores de nivel y paso.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barra y barrer mitades.
- [TRIGGER_2]: ReplacementTransform a cuartos y octavos conservando longitud total.
- [TRIGGER_3]: FadeIn observador y pulsar en cada visita; congelar pregunta.

#### Escena: 02

##### Nombre: Dos cortes de una tabla

##### Descripcion Breve: n y ω son dos direcciones distintas.

##### Objetivo Pedagogico: Distinguir etapa y trayectoria.

##### Voz en off:

> "[TRIGGER_1] Esta tabla organiza las variables: una columna fija el paso n y una fila fija omega. [TRIGGER_2] Leer una columna es tomar una fotografía y medir cuántos resultados presentan un error. [TRIGGER_3] Leer una fila es seguir una historia. Una región pequeña de errores en cada columna no garantiza que cada fila deje de equivocarse para siempre."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{etapa fija: }\omega\mapsto X_n(\omega)$`.
- MathTex: `$\text{resultado fijo: }n\mapsto X_n(\omega)$`.
- Matriz 16×16 evaluada en puntos medios de subintervalos; selectores horizontal y vertical; gráfico de pulsos de la fila.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create matriz con ejes rotulados.
- [TRIGGER_2]: Mover selector vertical y contar fracción iluminada.
- [TRIGGER_3]: Mover selector horizontal y TransformFromCopy a gráfico temporal.

#### Escena: 03

##### Nombre: Definir probabilidad

##### Descripcion Breve: Una tolerancia fija determina el evento de error.

##### Objetivo Pedagogico: Precisar todos los cuantificadores.

##### Voz en off:

> "[TRIGGER_1] Elegimos una tolerancia positiva y medimos la probabilidad de que el error la supere. [TRIGGER_2] La sucesión converge en probabilidad si ese número tiende a cero para cada tolerancia positiva. [TRIGGER_3] Los errores pueden trasladarse de un resultado a otro. También la probabilidad puede oscilar: la definición exige un límite cero, no un descenso monótono."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n\xrightarrow P X\iff\forall\varepsilon>0,\ \lim_nP(|X_n-X|>\varepsilon)=0$`.
- Axes ω contra error; umbral ε=1/2; medidor de masa del evento; gráfica de probabilidades por bloques.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create umbral y región de error.
- [TRIGGER_2]: Write definición en dos renglones.
- [TRIGGER_3]: Animar probabilidades por niveles y remarcar que cambian los puntos afectados.

#### Escena: 04

##### Nombre: Definir casi segura

##### Descripcion Breve: Las trayectorias convergen fuera de una excepción fija.

##### Objetivo Pedagogico: Entender permanencia eventual.

##### Voz en off:

> "[TRIGGER_1] Casi segura pide un conjunto fijo de resultados de probabilidad uno en el que cada historia converja. [TRIGGER_2] Para cada historia buena y cada tolerancia existe un momento desde el cual todos los errores son pequeños. Ese momento puede depender de omega y de la tolerancia. [TRIGGER_3] No basta volver muchas veces cerca del límite. Debemos acabar permaneciendo cerca, cualquiera que sea la precisión elegida."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(\{\omega:X_n(\omega)\to X(\omega)\})=1$`.
- MathTex: `$\forall\omega\notin N,\ \forall\varepsilon>0,\ \exists n_0,\ \forall n\ge n_0:\ |X_n(\omega)-X(\omega)|<\varepsilon$`.
- Tres trayectorias que entran permanentemente en una banda; n0 distintos; recinto de excepciones N con P(N)=0.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create recinto y trayectorias.
- [TRIGGER_2]: Dibujar bandas ε y marcar n0 por trayectoria.
- [TRIGGER_3]: Indicate ∀n≥n0 y mantener la banda fija.

#### Escena: 05

##### Nombre: La regla de los destellos

##### Descripcion Breve: Se formaliza la máquina de escribir.

##### Objetivo Pedagogico: Demostrar P sin c.s.

##### Voz en off:

> "[TRIGGER_1] Escribimos n como dos elevado a k más j. En ese nivel, iluminamos el intervalo j de longitud dos elevado a menos k. [TRIGGER_2] La probabilidad de superar un medio es esa longitud y tiende a cero. Tenemos convergencia en probabilidad a cero. [TRIGGER_3] Cada punto pertenece a una franja por nivel y queda fuera de las otras. Su límite superior es uno y el inferior cero: no converge, en ningún punto de nuestro espacio."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_{2^k+j}=\mathbf1_{[j2^{-k},(j+1)2^{-k})},\ 0\le j<2^k$`.
- MathTex: `$P(X_n>1/2)=2^{-k}\to0$`.
- MathTex: `$\limsup_nX_n=1,\quad\liminf_nX_n=0$`.
- Barrido k=1..5; extremos llenos/vacíos; historial del observador y contadores de anchura.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write regla y recorrer j.
- [TRIGGER_2]: Actualizar probabilidad 1/2,1/4,1/8,1/16,1/32.
- [TRIGGER_3]: Resaltar un destello y varios ceros por nivel; Write limsup y liminf.

#### Escena: 06

##### Nombre: La implicación válida

##### Descripcion Breve: Indicadoras dominadas prueban c.s.→P.

##### Objetivo Pedagogico: Dar una prueba completa breve.

##### Voz en off:

> "[TRIGGER_1] Si una trayectoria converge, la indicadora de error mayor que una tolerancia fija acaba siendo cero. [TRIGGER_2] Estas indicadoras están acotadas por uno, que es integrable. Podemos aplicar convergencia dominada. [TRIGGER_3] Sus esperanzas tienden a cero; esas esperanzas son las probabilidades de error. Hemos demostrado que casi segura implica probabilidad sin suponer independencia."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$I_n=\mathbf1_{\{|X_n-X|>\varepsilon\}}\to0\ {\rm c.s.}$`.
- MathTex: `$0\le I_n\le1,\quad\mathbb E1=1$`.
- MathTex: `$\mathbb EI_n=P(|X_n-X|>\varepsilon)\to0$`.
- Trayectoria buena y pulsos debajo; techo 1; cadena de tres pasos de prueba.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Transform errores en indicadoras.
- [TRIGGER_2]: Create techo y Write dominación.
- [TRIGGER_3]: TransformMatchingTex esperanza a probabilidad y dibujar flecha.

#### Escena: 07

##### Nombre: Seleccionar mejores pasos

##### Descripcion Breve: Una subsucesión usa probabilidades sumables.

##### Objetivo Pedagogico: Explicar un rescate parcial.

##### Voz en off:

> "[TRIGGER_1] Si convergemos en probabilidad, podemos escoger índices crecientes donde superar dos elevado a menos k tenga probabilidad a lo sumo dos elevado a menos k. [TRIGGER_2] La probabilidad de algún error seleccionado después de K está acotada por una cola geométrica que tiende a cero. [TRIGGER_3] Casi seguramente solo quedan finitos errores seleccionados. La subsucesión converge casi seguramente; los pasos descartados no reciben esa garantía."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(|X_{n_k}-X|>2^{-k})\le2^{-k}$`.
- MathTex: `$P\left(\bigcup_{k\ge K}\{|X_{n_k}-X|>2^{-k}\}\right)\le2^{1-K}$`.
- Fila de índices; seleccionados rodeados; barras geométricas y llave de cola.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Resaltar n1<n2<n3 y Write criterio.
- [TRIGGER_2]: Crear suma geométrica visual.
- [TRIGGER_3]: Mover K y mostrar desaparición de la cota; distinguir subsucesión de sucesión completa.

#### Escena: 08

##### Nombre: La respuesta depende de la cámara

##### Descripcion Breve: Se resuelve la paradoja inicial.

##### Objetivo Pedagogico: Consolidar significado y límite de simulaciones.

##### Voz en off:

> "[TRIGGER_1] La luz desaparece en las fotografías porque cada una contiene menos región iluminada. Las historias siguen parpadeando porque el barrido nunca termina. [TRIGGER_2] Así pueden coexistir convergencia en probabilidad y ausencia de convergencia casi segura. [TRIGGER_3] Una simulación finita ayuda a ver la regla, pero no comprueba qué ocurrirá infinitas veces. La prueba está en la anchura de las franjas y en que cada nivel vuelve a visitar todos los puntos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{c.s.}\Rightarrow P,\qquad P\not\Rightarrow\text{c.s.}$`.
- Pantalla dividida barra/historial; flecha válida y contraejemplo junto a recíproca tachada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Reproducir un nivel completo.
- [TRIGGER_2]: Congelar ambas vistas y Write implicaciones.
- [TRIGGER_3]: Indicate anchura y recurrencia; dejar pregunta «¿qué cámara observa el límite?».

