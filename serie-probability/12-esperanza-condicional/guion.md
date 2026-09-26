# Video 12: La mejor predicción con la información disponible

Un dado observado por paridad conduce a la definición por sigma álgebras, Radon-Nikodym y proyección L².

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 576 palabras (4–4.8 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Definición general para X∈L1; optimización cuadrática para X∈L2. La igualdad y la unicidad se entienden casi seguramente.

## Bibliografía y decisiones matemáticas

Proba §§4.1–4.2, pp. impresas 97–112, especialmente proposición 4.1, particiones numerables y propiedad de torre. La identidad de proyección se deriva de la definición.

#### Escena: 01

##### Nombre: Adivinar con una pista

##### Descripcion Breve: Un dado observado solo por paridad cambia la predicción.

##### Objetivo Pedagogico: Motivar una esperanza que depende del resultado.

##### Voz en off:

> "[TRIGGER_1] Lanzamos un dado justo y debes predecir su valor. Sin pistas, el mejor pronóstico cuadrático es tres y medio. [TRIGGER_2] Te digo únicamente si salió par. Si fue par, los valores posibles son dos, cuatro y seis y su promedio es cuatro. Si fue impar, el promedio es tres. [TRIGGER_3] Antes de recibir la pista, tu nuevo pronóstico es una variable aleatoria: vale cuatro o tres según la información que aparezca."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X\in\{1,2,3,4,5,6\},\quad\mathbb EX=3.5$`.
- MathTex: `$\mathbb E[X\mid\mathcal G]=4\mathbf1_{\rm par}+3\mathbf1_{\rm impar}$`.
- Seis caras; agrupaciones par/impar; dos tarjetas de pronóstico; caja de información que revela solo paridad.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create dado y pronóstico 3.5.
- [TRIGGER_2]: Dividir en grupos y calcular ambos promedios.
- [TRIGGER_3]: Mantener las dos salidas como una función dependiente del grupo.

#### Escena: 02

##### Nombre: La información es una sigma álgebra

##### Descripcion Breve: Una partición determina qué preguntas podemos responder.

##### Objetivo Pedagogico: Distinguir G de un subespacio vectorial.

##### Voz en off:

> "[TRIGGER_1] La información disponible no es una lista de números que ya conocemos, sino una colección de eventos distinguibles. Para la paridad, solo distinguimos pares, impares, todo y nada. [TRIGGER_2] Una variable medible respecto de esa información debe ser constante dentro de cada grupo indistinguible. [TRIGGER_3] G es una sigma álgebra. El subespacio vectorial de predicciones será L dos de G, no G misma; distinguir ambos objetos evita una metáfora geométrica engañosa."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathcal G=\{\varnothing,\Omega,A,A^c\},\quad A=\{2,4,6\}$`.
- MathTex: `$L^2(\mathcal G)=\{Y\in L^2:Y\text{ es }\mathcal G\text{-medible}\}$`.
- Dos recintos de resultados; rótulos evento/variable; plano abstracto etiquetado L²(G).

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create partición y Write G.
- [TRIGGER_2]: Mostrar que un pronóstico no puede distinguir 2 de 4.
- [TRIGGER_3]: Introducir plano L²(G) y separar etiquetas de objetos.

#### Escena: 03

##### Nombre: La definición general

##### Descripcion Breve: Medibilidad y conservación de integrales caracterizan el pronóstico.

##### Objetivo Pedagogico: Dar la definición rigurosa L1.

##### Voz en off:

> "[TRIGGER_1] Para X integrable buscamos una variable Y integrable y medible con la información disponible. [TRIGGER_2] Además, en cada evento G que esa información puede reconocer, Y debe conservar el promedio acumulado de X. Escribimos esa condición como igualdad de integrales. [TRIGGER_3] Estas dos exigencias definen la esperanza condicional, salvo cambios en conjuntos de probabilidad cero. No necesitamos dividir entre la probabilidad de cada resultado individual."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y=\mathbb E[X\mid\mathcal G],\quad Y\in L^1,\ Y\text{ }\mathcal G\text{-medible}$`.
- MathTex: `$\int_GY\,dP=\int_GX\,dP\quad\forall G\in\mathcal G$`.
- Barras X y Y sobre grupos; balanzas de sumas ponderadas por cada grupo; cuadro de definición.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write requisitos de Y.
- [TRIGGER_2]: Transform barras a promedios de grupo manteniendo suma ponderada.
- [TRIGGER_3]: Encerrar igualdad para todos los G y marcar unicidad c.s.

#### Escena: 04

##### Nombre: De dónde sale: Radon-Nikodym

##### Descripcion Breve: Una medida inducida por X tiene densidad respecto de P restringida.

##### Objetivo Pedagogico: Explicar existencia con hipótesis.

##### Voz en off:

> "[TRIGGER_1] Si X es no negativa e integrable, definimos una medida ν sobre la información disponible integrando X en cada evento. [TRIGGER_2] Cuando P de un evento vale cero, ν también vale cero. Radon-Nikodym garantiza una densidad medible de ν respecto de P; esa densidad es nuestra Y. [TRIGGER_3] Para X con signos aplicamos la construcción a las partes positiva y negativa y restamos. Su integrabilidad impide la indeterminación infinito menos infinito."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\nu(G)=\int_GX\,dP,\quad\nu\ll P|_{\mathcal G}$`.
- MathTex: `$Y=\frac{d\nu}{d(P|_{\mathcal G})}$`.
- MathTex: `$X=X^+-X^-$`.
- Dos columnas de medidas P y ν sobre los mismos grupos; densidad Y como factor local; etiqueta «Radon-Nikodym: teorema de existencia».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create ν con X≥0.
- [TRIGGER_2]: Mostrar P(G)=0⇒ν(G)=0 y escribir densidad.
- [TRIGGER_3]: Dividir X en partes y reconstruir esperanza condicional.

#### Escena: 05

##### Nombre: Calcular con una partición

##### Descripcion Breve: La definición recupera el promedio por celdas.

##### Objetivo Pedagogico: Verificar un ejemplo completo.

##### Voz en off:

> "[TRIGGER_1] Si la información separa omega en celdas A j de probabilidad positiva, el pronóstico en una celda es la integral de X allí dividida por su probabilidad. [TRIGGER_2] En el dado, la celda par tiene probabilidad un medio y suma ponderada dos, así que el valor es cuatro. La celda impar da tres. [TRIGGER_3] Si una celda tiene probabilidad cero, el valor asignado allí es irrelevante para la clase casi segura; podemos escoger cero."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[X\mid\mathcal G]=\sum_j\frac{\mathbb E[X\mathbf1_{A_j}]}{P(A_j)}\mathbf1_{A_j}\quad(P(A_j)>0)$`.
- MathTex: `$\mathbb E[X\mathbf1_A]=(2+4+6)/6=2$`.
- Tabla de resultados, masas 1/6, sumas por paridad; columna de predicción; ejemplo de celda nula separado.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write fórmula por celdas.
- [TRIGGER_2]: Calcular ambos grupos y verificar integrales.
- [TRIGGER_3]: Añadir celda de masa cero y nota de elección arbitraria.

#### Escena: 06

##### Nombre: La torre de información

##### Descripcion Breve: Más información seguida de menos reproduce el pronóstico grueso.

##### Objetivo Pedagogico: Probar propiedad de torre.

##### Voz en off:

> "[TRIGGER_1] Supongamos que G uno contiene menos información que G dos. Podemos predecir con detalle y después borrar parte de ese detalle. [TRIGGER_2] El resultado coincide con predecir directamente usando G uno. Para probarlo, integramos sobre cualquier evento de G uno y aplicamos dos veces la definición. [TRIGGER_3] También, si ya conocemos X, condicionarla no la cambia. Estas identidades permiten actualizar pronósticos sin inventar información futura."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathcal G_1\subset\mathcal G_2\Rightarrow\mathbb E[\mathbb E(X\mid\mathcal G_2)\mid\mathcal G_1]=\mathbb E(X\mid\mathcal G_1)$`.
- MathTex: `$X\text{ }\mathcal G\text{-medible}\Rightarrow\mathbb E(X\mid\mathcal G)=X$`.
- Partición fina en seis celdas, intermedia paridad y gruesa única; flechas de promedios; integrales de prueba.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create particiones anidadas.
- [TRIGGER_2]: Transform promedios en dos rutas y escribir igualdad sobre G∈G1.
- [TRIGGER_3]: Mostrar X conocido y su pronóstico idéntico.

#### Escena: 07

##### Nombre: La proyección que minimiza error

##### Descripcion Breve: Ortogonalidad produce una descomposición de riesgos.

##### Objetivo Pedagogico: Demostrar interpretación L2.

##### Voz en off:

> "[TRIGGER_1] Ahora suponemos X en L dos. El pronóstico Y también está en L dos por Jensen condicional y su error es ortogonal a toda variable Z de L dos medible con G. [TRIGGER_2] Al expandir el cuadrado de X menos Z, el término cruzado desaparece. Queda el error de Y más la distancia cuadrática de Y a Z. [TRIGGER_3] Así Y minimiza el error cuadrático entre todos los pronósticos permitidos. Esta geometría necesita L dos; la definición anterior solo requería L uno."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[(X-Y)Z]=0\quad\forall Z\in L^2(\mathcal G)$`.
- MathTex: `$\mathbb E(X-Z)^2=\mathbb E(X-Y)^2+\mathbb E(Y-Z)^2$`.
- Plano L²(G), vector X, proyección Y y alternativa Z; triángulo ortogonal; anotar extensión de indicadores a Z por aproximación L².

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create proyección y Write ortogonalidad primero para indicadoras.
- [TRIGGER_2]: Extender por linealidad y aproximación; Write Pitágoras.
- [TRIGGER_3]: Mover Z en el plano y mostrar riesgo mínimo en Y.

#### Escena: 08

##### Nombre: Condicionar a un valor no es dividir por cero

##### Descripcion Breve: Se interpreta E[X|Y=y] mediante una función de Y.

##### Objetivo Pedagogico: Cerrar y preparar filtraciones.

##### Voz en off:

> "[TRIGGER_1] Cuando condicionamos por una variable Y, en realidad usamos la información sigma de Y. La respuesta puede escribirse como una función h de Y. [TRIGGER_2] Para variables continuas, cada evento Y igual a y puede tener probabilidad cero. No definimos el condicionamiento dividiendo directamente por esa probabilidad. [TRIGGER_3] La función h queda determinada casi por doquier respecto de la ley de Y. Con este lenguaje podemos describir cómo cambia una predicción al acumular información en el tiempo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[X\mid Y]=\mathbb E[X\mid\sigma(Y)]=h(Y)$`.
- Eje Y continuo; curva h(y); punto individual con masa cero; secuencia de cajas de información creciente.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write sigma(Y) y función h.
- [TRIGGER_2]: Mostrar P(Y=y)=0 y descartar cociente elemental.
- [TRIGGER_3]: Transform cajas de información en una línea temporal que anticipa filtración.

