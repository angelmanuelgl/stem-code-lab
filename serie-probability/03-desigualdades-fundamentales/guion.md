# Video 03: Lo que sabemos sin conocer la distribución

De facturas impredecibles a errores de simulación: cinco desigualdades convierten pocos momentos conocidos en conclusiones verificables.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 532 palabras (3.7–4.4 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Markov requiere no negatividad; Chebyshev varianza finita; Jensen convexidad; Hölder exponentes conjugados. Cada condición permanece visible.

## Bibliografía y decisiones matemáticas

Probita §5.3: monotonía y linealidad de esperanza. Proba §2.3: Markov y Chebyshev. Jensen, Cauchy-Schwarz y Hölder se desarrollan con pruebas elementales complementarias.

#### Escena: 01

##### Nombre: El promedio limita una cola

##### Descripcion Breve: Una factura media de cien restringe gastos extremos.

##### Objetivo Pedagogico: Motivar una cota universal.

##### Voz en off:

> "[TRIGGER_1] Si el gasto medio es cien, ¿podría la mitad de la población gastar más de mil? [TRIGGER_2] Con gastos no negativos, esa mitad aportaría por sí sola más de quinientos al promedio. Tenemos una contradicción sin conocer la distribución. [TRIGGER_3] Vamos a formalizar esta idea. No encontraremos la probabilidad exacta de una factura enorme, pero sí un límite que cualquier distribución compatible debe respetar."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X\ge0,\quad\mathbb EX=100$`.
- MathTex: `$P(X\ge1000)\le0.1$`.
- Diez barras de gasto; umbral 1000; contador de media; etiqueta «esquema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barras y umbral.
- [TRIGGER_2]: Elevar cinco barras hasta 1000 y escribir contribución ≥500.
- [TRIGGER_3]: Write cota 0.1 y subrayar X≥0.

#### Escena: 02

##### Nombre: Markov

##### Descripcion Breve: Una indicadora queda debajo de la variable.

##### Objetivo Pedagogico: Demostrar la cota.

##### Voz en off:

> "[TRIGGER_1] Donde X alcanza el umbral a, el producto de a por la indicadora vale a y no supera X. [TRIGGER_2] Fuera del evento, ese producto vale cero. Tomamos esperanza en la desigualdad puntual y usamos monotonía. [TRIGGER_3] La esperanza de la indicadora es la probabilidad del evento. Dividiendo entre a positivo obtenemos Markov. Su fuerza está en necesitar únicamente un primer momento."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$a\mathbf1_{\{X\ge a\}}\le X$`.
- MathTex: `$aP(X\ge a)\le\mathbb EX$`.
- MathTex: `$P(X\ge a)\le\mathbb EX/a,\quad a>0$`.
- Columnas no negativas y escalón de altura a solo bajo las que cruzan el umbral; rótulos de cada operación.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create escalón y comparar alturas.
- [TRIGGER_2]: TransformMatchingTex a esperanzas.
- [TRIGGER_3]: Sustituir esperanza de indicadora; dividir y encerrar a>0.

#### Escena: 03

##### Nombre: Chebyshev

##### Descripcion Breve: El error cuadrático permite usar Markov.

##### Objetivo Pedagogico: Controlar desviaciones a ambos lados.

##### Voz en off:

> "[TRIGGER_1] Para medir distancia a la media usamos el cuadrado del error. Siempre es no negativo. [TRIGGER_2] Aplicamos Markov a ese cuadrado; su esperanza es la varianza. Así controlamos ambas colas con una sola desigualdad. [TRIGGER_3] Si la varianza es finita y positiva, la probabilidad de alejarse tres desviaciones estándar no supera un noveno. No hemos supuesto una distribución normal."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y=(X-\mu)^2,\quad\mathbb EY=\sigma^2$`.
- MathTex: `$P(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$`.
- MathTex: `$P(|X-\mu|\ge3\sigma)\le1/9$`.
- Distribución discreta asimétrica; barreras μ±ε; flechas desde ambas colas al eje de cuadrados.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barreras y distancias.
- [TRIGGER_2]: Write Markov sobre Y y transformar a Chebyshev.
- [TRIGGER_3]: Mover barreras a 3σ y Write 1/9; dejar σ²<∞ visible.

#### Escena: 04

##### Nombre: Jensen

##### Descripcion Breve: Una recta soporte explica la convexidad.

##### Objetivo Pedagogico: Distinguir promedio de transformación y transformación de promedio.

##### Voz en off:

> "[TRIGGER_1] Con una función convexa, transformar después de promediar produce un valor no mayor que promediar los valores transformados. [TRIGGER_2] La prueba usa una recta soporte en la media. La curva queda encima y el término lineal promedia cero. [TRIGGER_3] Suponemos X integrable, valores en el intervalo de convexidad y expectativas bien definidas. Para el cuadrado obtenemos que el segundo momento domina al cuadrado de la media."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi(x)\ge\varphi(\mu)+m(x-\mu)$`.
- MathTex: `$\varphi(\mathbb EX)\le\mathbb E\varphi(X)$`.
- MathTex: `$(\mathbb EX)^2\le\mathbb EX^2$`.
- Axes x=[−2,2], y=[0,4]; parábola; dos masas iguales en −1 y 2; recta soporte en μ=1/2.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create curva, masas y promedio.
- [TRIGGER_2]: Create soporte y Write desigualdad; cancelar E(X−μ).
- [TRIGGER_3]: TransformMatchingTex a Jensen y al caso cuadrático.

#### Escena: 05

##### Nombre: Cauchy-Schwarz

##### Descripcion Breve: La esperanza de un cuadrado no puede ser negativa.

##### Objetivo Pedagogico: Demostrar una cota para productos.

##### Voz en off:

> "[TRIGGER_1] Dos variables con segundo momento finito tienen un producto cuyo promedio está limitado por sus tamaños. [TRIGGER_2] Expandimos la esperanza del cuadrado de X menos t por Y. Es una parábola no negativa para todo t, de modo que su discriminante no puede ser positivo. [TRIGGER_3] Eso da Cauchy-Schwarz. La igualdad corresponde a variables proporcionales casi seguramente, incluyendo los casos nulos. Esta será la geometría de nuestro espacio L dos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E(X-tY)^2=\mathbb EX^2-2t\mathbb E(XY)+t^2\mathbb EY^2\ge0$`.
- MathTex: `$|\mathbb E(XY)|^2\le\mathbb EX^2\,\mathbb EY^2$`.
- Parábola en t; vectores esquemáticos X,Y; etiqueta «producto interno E(XY)».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create vectores con tamaños rotulados.
- [TRIGGER_2]: Write expansión en tres líneas y Create parábola sobre cero.
- [TRIGGER_3]: Mostrar discriminante ≤0; Transform a cota y alinear vectores para igualdad.

#### Escena: 06

##### Nombre: Hölder

##### Descripcion Breve: Exponentes conjugados equilibran dos variables.

##### Objetivo Pedagogico: Extender la cota de producto.

##### Voz en off:

> "[TRIGGER_1] Podemos combinar otros momentos: orden tres para una variable y tres medios para la otra. [TRIGGER_2] Normalizamos las variables por sus normas y aplicamos Young: a por b no supera a elevado a p sobre p más b elevado a q sobre q. [TRIGGER_3] Al integrar, el lado derecho vale uno. Desnormalizar da Hölder. Si una norma es cero, la variable es cero casi seguramente y la desigualdad es inmediata."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$1/p+1/q=1,\quad p,q>1$`.
- MathTex: `$ab\le a^p/p+b^q/q$`.
- MathTex: `$\mathbb E|XY|\le\|X\|_p\|Y\|_q$`.
- Tarjetas p=3,q=3/2; cadena normalizar→Young→integrar; flechas hacia p=q=2.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write exponentes y comprobar sus inversos.
- [TRIGGER_2]: Mostrar a=|X|/||X||p,b=|Y|/||Y||q debajo de Young.
- [TRIGGER_3]: Integrar, restaurar normas y especializar a p=q=2.

#### Escena: 07

##### Nombre: Hipótesis que hacen trabajo

##### Descripcion Breve: Tres usos incorrectos se corrigen.

##### Objetivo Pedagogico: Evitar fórmulas fuera de contexto.

##### Voz en off:

> "[TRIGGER_1] Si X vale cien o menos cien con igual probabilidad, su media es cero. Una falsa aplicación de Markov diría que nunca alcanza cien. [TRIGGER_2] La no negatividad faltaba. De manera parecida, varianza infinita deja sin cota útil a Chebyshev y una función cóncava invierte Jensen. [TRIGGER_3] Antes de calcular, identifica qué cantidad es no negativa, qué momentos existen y cuál es la curvatura. Las hipótesis son parte del mecanismo de la prueba."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(X=100)=P(X=-100)=1/2$`.
- MathTex: `$\mathbb EX=0,\quad P(X\ge100)=1/2$`.
- MathTex: `$\psi\ \text{cóncava}\Rightarrow\mathbb E\psi(X)\le\psi(\mathbb EX)$`.
- Dos masas ±100; tres tarjetas de requisitos; curva raíz para concavidad.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create masas y media; mostrar falsa cota tachada.
- [TRIGGER_2]: Indicate X≥0,σ²<∞ y convexidad por turnos.
- [TRIGGER_3]: Transform parábola a raíz y cambiar dirección de Jensen.

#### Escena: 08

##### Nombre: Del momento a la probabilidad

##### Descripcion Breve: Markov aplicado al error produce convergencia.

##### Objetivo Pedagogico: Cerrar con una aplicación central.

##### Voz en off:

> "[TRIGGER_1] Si el error elevado a p tiene esperanza que tiende a cero, ¿puede seguir siendo probable un error grande? [TRIGGER_2] Markov dice que su probabilidad está acotada por ese momento dividido por la tolerancia elevada a p. [TRIGGER_3] Para tolerancia fija, el denominador no cambia y el numerador desaparece. Así convertimos cercanía promedio en cercanía en probabilidad. Esa es la clase de puente que estas desigualdades permiten construir."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(|X_n-X|>\varepsilon)\le\frac{\mathbb E|X_n-X|^p}{\varepsilon^p}$`.
- MathTex: `$\mathbb E|X_n-X|^p\to0\Rightarrow X_n\xrightarrow P X$`.
- Barras de error, umbral fijo ε y flecha «momento→cola».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barras y umbral.
- [TRIGGER_2]: Write cota y resaltar denominador fijo.
- [TRIGGER_3]: Reducir numerador; Transform a implicación final.

