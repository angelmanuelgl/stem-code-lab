# Video 01: ¿Podemos asignarle probabilidad a cualquier conjunto?

Pregunta autónoma: elegir un punto al azar parece sencillo; exigir que cualquier conjunto tenga una longitud conduce a una contradicción. Se construye el lenguaje mínimo de un espacio de probabilidad.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 647 palabras (4.5–5.4 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Se demuestra la obstrucción de Vitali bajo el axioma de elección. No se afirma que toda medida en un conjunto no numerable sea imposible sobre su conjunto potencia.

## Bibliografía y decisiones matemáticas

Base: Probita, §§2.2–2.6 y §4.1, páginas impresas 24–45 y 81–87. La completación de Borel se distingue de Borel. Notación: λ para longitud y P para probabilidad normalizada.

#### Escena: 01

##### Nombre: Un punto imposible de acertar

##### Descripcion Breve: Un selector continuo enfrenta puntos y regiones.

##### Objetivo Pedagogico: Distinguir probabilidad cero de imposibilidad.

##### Voz en off:

> "[TRIGGER_1] Imagina elegir un punto uniformemente en esta barra. ¿Cuál es la probabilidad de acertar exactamente el centro? [Pausa.] Un punto tiene longitud cero, así que su probabilidad es cero. [TRIGGER_2] Ahora elige la mitad izquierda: su probabilidad es un medio. Todos sus puntos tenían probabilidad cero. La diferencia está en que hemos reunido una cantidad no numerable de puntos. [TRIGGER_3] La probabilidad suma sobre uniones numerables disjuntas. No promete sumar término por término una unión no numerable. Necesitamos decir con precisión qué estamos midiendo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Omega=[0,1],\quad P(\{1/2\})=0$`.
- MathTex: `$P([0,1/2])=\frac12$`.
- NumberLine [0,1] de longitud 5; Dot de radio 0.06 en 1/2; Rectangle de altura 0.35 sobre [0,1/2]; rótulo «selector ideal, continuo».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create la barra y FadeIn el punto; Write la primera ecuación y esperar 4 s.
- [TRIGGER_2]: Transform el punto en región, conservando una copia del punto; Write 1/2 y la etiqueta «longitud».
- [TRIGGER_3]: Write una tarjeta «numerable ≠ no numerable» y conectar con la barra mediante Arrow.

#### Escena: 02

##### Nombre: Eventos como preguntas

##### Descripcion Breve: Un dado define resultados, eventos e información.

##### Objetivo Pedagogico: Interpretar Ω, F y P por separado.

##### Voz en off:

> "[TRIGGER_1] Empecemos con algo finito: un dado. Omega contiene los seis resultados. El evento par contiene dos, cuatro y seis; una pregunta se convierte en un conjunto. [TRIGGER_2] Supongamos que solo tenemos un sensor de paridad. Puede distinguir pares e impares, pero no separar el dos del cuatro. Su colección de preguntas disponibles es una sigma álgebra pequeña. [TRIGGER_3] La medida asigna números a esas preguntas. El espacio muestral, la información y la probabilidad son tres componentes distintos; juntos forman el modelo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Omega=\{1,2,3,4,5,6\}$`.
- MathTex: `$\mathcal G=\{\varnothing,\Omega,\{2,4,6\},\{1,3,5\}\}$`.
- MathTex: `$(\Omega,\mathcal F,P)$`.
- Seis RoundedRectangle con numerales; dos recintos de paridad; tres tarjetas Ω, F, P; usar distribución de tarjetas 3×2.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: FadeIn las seis tarjetas; SurroundingRectangle alrededor de 2,4,6.
- [TRIGGER_2]: Agrupar pares e impares con dos recintos y Write G en dos líneas.
- [TRIGGER_3]: TransformFromCopy cada elemento hacia su símbolo; fijar las tres tarjetas en el pie.

#### Escena: 03

##### Nombre: Por qué una sigma álgebra

##### Descripcion Breve: Se construyen las operaciones lógicas admisibles.

##### Objetivo Pedagogico: Relacionar complemento y unión numerable con preguntas.

##### Voz en off:

> "[TRIGGER_1] Si podemos preguntar si ocurrió A, queremos preguntar también si no ocurrió A: ese es el complemento. Además, sabemos reconocer el conjunto de todos los resultados. [TRIGGER_2] Si podemos observar cada uno de una lista numerable de eventos, queremos observar si ocurrió al menos uno. Por eso cerramos nuestra colección bajo uniones numerables. [TRIGGER_3] Las intersecciones se recuperan usando complementos. Estas reglas forman una sigma álgebra. No exigen que todas las preguntas imaginables estén disponibles; exigen coherencia entre las que sí están."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Omega\in\mathcal F,\quad A\in\mathcal F\Rightarrow A^c\in\mathcal F$`.
- MathTex: `$A_n\in\mathcal F\Rightarrow\bigcup_{n=1}^{\infty}A_n\in\mathcal F$`.
- MathTex: `$\bigcap_n A_n=\left(\bigcup_n A_n^c\right)^c$`.
- Rectángulo Ω de 5×3; regiones A y A^c con tramas diferentes; fila de ocho intervalos representando una lista numerable, con rótulo «esquema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create Ω y región A; Transform una copia al complemento y Write primera regla.
- [TRIGGER_2]: LaggedStart las ocho regiones; mostrar llave de unión y símbolo de continuación matemática.
- [TRIGGER_3]: TransformMatchingTex la identidad de De Morgan; encerrar el nombre «σ-álgebra».

#### Escena: 04

##### Nombre: Una medida coherente

##### Descripcion Breve: La suma de masas se compara con una unión que se solapa.

##### Objetivo Pedagogico: Presentar axiomas y continuidad desde abajo.

##### Voz en off:

> "[TRIGGER_1] Una probabilidad nunca es negativa y la totalidad pesa uno. Si dos eventos no se solapan, sus probabilidades sí se suman. [TRIGGER_2] La misma regla vale para una lista numerable de eventos disjuntos. Si hay solapamiento, sumarlos directamente cuenta dos veces los puntos comunes. [TRIGGER_3] De estos axiomas sale una propiedad esencial: si unos eventos crecen hasta cubrir A, sus probabilidades crecen hasta la de A. Este será nuestro primer puente entre conjuntos y límites."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(\Omega)=1,\quad P(A)\ge0$`.
- MathTex: `$P\left(\bigsqcup_{n\ge1}A_n\right)=\sum_{n\ge1}P(A_n)$`.
- MathTex: `$A_n\uparrow A\Rightarrow P(A_n)\uparrow P(A)$`.
- Tres intervalos disjuntos con longitudes 0.2,0.3,0.1; segunda barra con intersección; intervalos [0,1−1/n] para n=2,4,8,16.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Animar barras disjuntas concatenándose y contador 0.6.
- [TRIGGER_2]: Superponer dos barras y tramar la intersección; escribir «no disjuntos».
- [TRIGGER_3]: ReplacementTransform los intervalos crecientes y enlazar cada longitud con 1−1/n.

#### Escena: 05

##### Nombre: Construir regiones medibles

##### Descripcion Breve: Intervalos generan Borel y la completación añade subconjuntos nulos.

##### Objetivo Pedagogico: Distinguir conjunto generado y potencia.

##### Voz en off:

> "[TRIGGER_1] En la recta empezamos con intervalos abiertos y cerramos bajo nuestras operaciones. La menor sigma álgebra que los contiene se llama Borel. [TRIGGER_2] Incluye mucho más que intervalos: puntos, racionales, conjuntos cerrados y construcciones numerables muy complicadas. Generar no significa enumerar todos sus elementos uno por uno. [TRIGGER_3] La medida de Lebesgue completa esta estructura incluyendo todos los subconjuntos de conjuntos borelianos nulos. Borel y Lebesgue medible no son sinónimos, aunque ambos bastan para muchos modelos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathcal B(\mathbb R)=\sigma(\{(a,b):a<b\})$`.
- MathTex: `$\lambda((a,b))=b-a$`.
- MathTex: `$\mathcal B([0,1])\subset\mathcal L([0,1])\subset 2^{[0,1]}$`.
- Árbol de operaciones con nodos intervalo, complemento, unión numerable; tres recintos anidados; punto y Q indicados como ejemplos, sin dibujar supuestas listas completas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create un intervalo y ramas de complemento/unión; Write definición de Borel.
- [TRIGGER_2]: Añadir nodos {x} y Q con fórmulas de construcción numerable.
- [TRIGGER_3]: Create recintos anidados y etiquetas; resaltar que la última inclusión aún plantea una pregunta.

#### Escena: 06

##### Nombre: El selector de Vitali

##### Descripcion Breve: Se agrupan puntos según diferencias racionales.

##### Objetivo Pedagogico: Entender la selección no constructiva.

##### Voz en off:

> "[TRIGGER_1] Vamos a suponer que toda parte de la barra tiene longitud compatible con traslaciones. Dos puntos serán equivalentes si su diferencia es racional. [TRIGGER_2] Esta relación divide la barra en clases. Usando el axioma de elección, elegimos un representante de cada clase y reunimos los representantes en V. [TRIGGER_3] El dibujo solo representa unas pocas clases: V no es una nube de puntos que podamos calcular y completar en pantalla. La prueba utiliza sus propiedades lógicas, no una imagen literal."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$x\sim y\iff x-y\in\mathbb Q$`.
- MathTex: `$V\subset[0,1]\quad\text{un representante por clase}$`.
- MathTex: `$V+q,\quad q\in\mathbb Q\cap[-1,1]$`.
- Cuatro filas de puntos etiquetadas «clases, esquema»; un punto seleccionado por fila; flechas de traslación racional; tarjeta explícita «axioma de elección».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create cuatro clases esquemáticas; Write la relación y mostrar diferencias racionales 1/2 y 1/3.
- [TRIGGER_2]: Indicate un representante por fila; agrupar copias bajo V.
- [TRIGGER_3]: Mover copia de V una distancia q y añadir aviso «no es una representación literal de V».

#### Escena: 07

##### Nombre: La contradicción de longitudes

##### Descripcion Breve: Traslaciones disjuntas cubren una unidad dentro de una región finita.

##### Objetivo Pedagogico: Probar la no medibilidad del selector.

##### Voz en off:

> "[TRIGGER_1] Las traslaciones racionales distintas de V son disjuntas. Si dos puntos trasladados coincidieran, sus representantes diferirían por un racional: pertenecerían a la misma clase y serían el mismo representante. [TRIGGER_2] Todas esas traslaciones cubren [0,1] y quedan dentro de [−1,2]. Si V tuviera medida cero, su unión numerable tendría cero; pero contiene un intervalo de longitud uno. [TRIGGER_3] Si V tuviera medida positiva, sumar infinitas copias iguales daría infinito; pero la unión está dentro de un intervalo de longitud tres. Ambas opciones fallan. Esa medida no puede existir con todas las propiedades exigidas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$[0,1]\subset U=\bigcup_{q\in\mathbb Q\cap[-1,1]}(V+q)\subset[-1,2]$`.
- MathTex: `$1\le\lambda(U)=\sum_q\lambda(V)\le3$`.
- MathTex: `$\lambda(V)=0\Rightarrow\lambda(U)=0;\quad\lambda(V)>0\Rightarrow\lambda(U)=\infty$`.
- NumberLine [-1,2]; tres cajas para inclusión, suma, contradicción; copias de V dibujadas como símbolos, no como intervalos de longitud positiva.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write igualdad v+q=w+r y transformar a v−w=r−q; concluir disjunción.
- [TRIGGER_2]: Create intervalo contenedor y Write cadena de inclusiones; activar rama λ(V)=0.
- [TRIGGER_3]: Activar rama positiva; cruzar ambas conclusiones incompatibles y mantener hipótesis de invariancia visible.

#### Escena: 08

##### Nombre: Qué se rompe y qué permanece

##### Descripcion Breve: Regreso al selector uniforme y cierre autónomo.

##### Objetivo Pedagogico: Formular el alcance exacto de la obstrucción.

##### Voz en off:

> "[TRIGGER_1] La probabilidad no se rompe por usar infinitos resultados. El selector uniforme en [0,1] funciona perfectamente sobre los conjuntos medibles adecuados. [TRIGGER_2] Lo incompatible era exigir simultáneamente medirlo todo, conservar la longitud bajo traslaciones y sumar numerablemente. Las sigma álgebras permiten construir un modelo coherente. [TRIGGER_3] Antes de calcular una probabilidad, podemos hacer tres preguntas: cuáles son los resultados, qué eventos podemos medir y qué peso tienen. Ya sabemos por qué cada componente del modelo tiene un trabajo indispensable."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$([0,1],\mathcal B([0,1]),\lambda)$`.
- MathTex: `$P([a,b])=b-a\quad(0\le a\le b\le1)$`.
- Reaparición de barra inicial y tarjetas Ω,F,P; checklist visual de tres preguntas; V queda fuera del recinto medible como símbolo abstracto.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Restaurar barra y seleccionar [0.2,0.7], mostrando 0.5.
- [TRIGGER_2]: Transform las tres exigencias en una tarjeta «incompatibilidad demostrada».
- [TRIGGER_3]: Indicate Ω,F,P al ritmo de las tres preguntas; cerrar con intervalo válido y su masa.

