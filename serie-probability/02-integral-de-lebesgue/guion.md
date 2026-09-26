# Video 02: Sumar valores sin recorrerlos uno por uno: la integral de Lebesgue

Pregunta autónoma: ¿cómo promediar una variable sobre un espacio que ni siquiera tiene un eje numérico? Se construye la esperanza desde funciones simples y se explican los límites bajo la integral.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 609 palabras (4.2–5.1 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Distinguir integrar sobre Ω e integrar respecto a la ley de X. Dar condiciones de existencia, convergencia monótona y dominada; no prometer intercambiar cualquier límite.

## Bibliografía y decisiones matemáticas

Probita, §§4.2 y 5.1–5.5, especialmente teoremas 5.5–5.11, páginas impresas 129–142. Desarrollo original basado en la construcción por aproximaciones simples.

#### Escena: 01

##### Nombre: El promedio de una ruleta desigual

##### Descripcion Breve: Premios y regiones de distinta probabilidad sustituyen el promedio aritmético.

##### Objetivo Pedagogico: Introducir ponderación por medida.

##### Voz en off:

> "[TRIGGER_1] Esta ruleta paga cero, dos o diez. ¿Su premio medio es cuatro? Solo lo sería si los tres premios fueran igualmente probables. [TRIGGER_2] La mitad de la rueda paga cero, un cuarto paga dos y el último cuarto paga diez. El promedio ponderado es tres. [TRIGGER_3] El truco es agrupar resultados que producen el mismo premio. Para cada grupo multiplicamos el valor por su probabilidad; esa idea seguirá funcionando aunque haya infinitos resultados."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(X=0)=1/2,\quad P(X=2)=P(X=10)=1/4$`.
- MathTex: `$\mathbb E[X]=0(1/2)+2(1/4)+10(1/4)=3$`.
- AnnularSector de ángulos π,π/2,π/2; etiquetas de premios; tres barras de masa; flechas desde sectores a sumandos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create ruleta y mostrar media ingenua (0+2+10)/3=4 con interrogación.
- [TRIGGER_2]: Transform los sectores en barras proporcionales; Write suma ponderada.
- [TRIGGER_3]: TransformMatchingTex el resultado 3 y conectar cada grupo con su premio.

#### Escena: 02

##### Nombre: Una variable transporta información

##### Descripcion Breve: Preimágenes conectan Ω con valores numéricos.

##### Objetivo Pedagogico: Definir medibilidad y ley imagen.

##### Voz en off:

> "[TRIGGER_1] Una variable aleatoria toma un resultado omega y devuelve un número. El resultado podría ser una secuencia de lanzamientos; no necesitamos que omega sea una coordenada real. [TRIGGER_2] Para preguntar si X cae en un intervalo, regresamos a los resultados que producen esos valores. Ese conjunto es la preimagen. [TRIGGER_3] Pedimos que todas las preimágenes de conjuntos borelianos sean eventos medibles. Así la distribución de X puede asignarles probabilidad y la pregunta numérica tiene sentido en el modelo original."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X:(\Omega,\mathcal F)\to(\mathbb R,\mathcal B(\mathbb R))$`.
- MathTex: `$P_X(B)=P(X^{-1}(B))$`.
- Rectángulo Ω con nueve símbolos de resultados; NumberLine de valores; nueve Arrow; selección B=[1,3] y preimagen marcada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: FadeIn resultados abstractos y animar flechas hacia valores.
- [TRIGGER_2]: SurroundingRectangle alrededor de B; recorrer flechas en sentido inverso.
- [TRIGGER_3]: Write fórmula de ley imagen y etiqueta «X medible».

#### Escena: 03

##### Nombre: Escalones que sabemos sumar

##### Descripcion Breve: Una función simple se integra exactamente.

##### Objetivo Pedagogico: Construir la integral desde particiones medibles.

##### Voz en off:

> "[TRIGGER_1] Una función simple tiene un número finito de valores. Dividimos omega en regiones disjuntas y asignamos una altura a cada región. [TRIGGER_2] Su integral es la suma de altura por probabilidad. Aquí probabilidad ocupa el papel que tenía la anchura en el cálculo elemental. [TRIGGER_3] Podemos dividir una región en dos sin cambiar el resultado, porque sus probabilidades se suman. La integral depende de la función y la medida, no del modo en que dibujamos sus escalones."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$s=\sum_{j=1}^m a_j\mathbf1_{A_j}$`.
- MathTex: `$\int_\Omega s\,dP=\sum_{j=1}^m a_jP(A_j)$`.
- MathTex: `$P(A_j)=P(B_j)+P(C_j)\quad(A_j=B_j\sqcup C_j)$`.
- Tres bloques con alturas 1,2,4 y masas 1/2,1/4,1/4; subdivisión del primer bloque en dos de masa 1/4.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create escalones y Write representación con indicadoras.
- [TRIGGER_2]: TransformFromCopy cada bloque a su sumando; obtener 2.
- [TRIGGER_3]: Split el primer bloque en dos; transformar 1·1/2 en 1·1/4+1·1/4 conservando el total.

#### Escena: 04

##### Nombre: Aproximar desde abajo

##### Descripcion Breve: Redondeo diádico convierte una función en escalones crecientes.

##### Objetivo Pedagogico: Explicar definición no negativa y límite.

##### Voz en off:

> "[TRIGGER_1] Para una función no negativa, redondeamos sus valores hacia abajo en pasos de un medio, un cuarto y un octavo. También ponemos un techo que irá creciendo. [TRIGGER_2] Los escalones suben hacia la función. Integramos cada aproximación y definimos la integral como el límite de esos valores; puede ser infinito. [TRIGGER_3] La construcción ocurre en los valores de salida. Sus bases son preimágenes medibles. No basta imaginar cortes horizontales: la medida de cada base es lo que permite sumar."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$s_n=2^{-n}\left\lfloor2^n\min(X,n)\right\rfloor$`.
- MathTex: `$0\le s_n\uparrow X,\quad\int X\,dP=\lim_n\int s_n\,dP$`.
- Axes x=[0,1],y=[0,3]; curva X(x)=3x²; escalones por niveles diádicos; contador n=1,2,3,4; rótulo «ejemplo Ω=[0,1]».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create curva y aproximación n=1; mostrar redondeo en un punto.
- [TRIGGER_2]: ReplacementTransform aproximaciones n=2,3,4 sin mover ejes.
- [TRIGGER_3]: Indicate preimágenes de una banda horizontal; conectar masa y altura antes del límite.

#### Escena: 05

##### Nombre: Signos e integrabilidad

##### Descripcion Breve: Parte positiva y negativa controlan la esperanza.

##### Objetivo Pedagogico: Evitar restar infinito menos infinito.

##### Voz en off:

> "[TRIGGER_1] Con pérdidas y ganancias separamos la parte positiva de la negativa. Ambas son funciones no negativas y sabemos integrarlas. [TRIGGER_2] La esperanza finita existe cuando el valor absoluto tiene integral finita. Si ambas partes suman infinito, su diferencia no está definida. [TRIGGER_3] Una simetría bonita no arregla ese problema. La distribución de Cauchy es simétrica, pero no tiene esperanza: cancelar colas de dos maneras distintas puede esconder la divergencia."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X=X^+-X^-,\quad |X|=X^++X^-$`.
- MathTex: `$X\in L^1\iff\mathbb E|X|<\infty$`.
- MathTex: `$f(x)=\frac1{\pi(1+x^2)},\quad\int_0^\infty xf(x)\,dx=\infty$`.
- Curva con regiones positivas/negativas separadas; tarjeta ∞−∞ no definido; para Cauchy, ejes x=[−5,5] con flechas de continuación de colas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Transform una curva firmada en dos paneles X+ y X−.
- [TRIGGER_2]: Write condición L1 y contrastar con tarjeta ∞−∞.
- [TRIGGER_3]: Create densidad Cauchy; mostrar integral truncada log(1+R²)/(2π) creciendo con R.

#### Escena: 06

##### Nombre: Cuándo atraviesa el límite la integral

##### Descripcion Breve: Pico móvil y teoremas de convergencia contrastan.

##### Objetivo Pedagogico: Mostrar la necesidad de hipótesis.

##### Voz en off:

> "[TRIGGER_1] Este rectángulo se estrecha y crece: altura n y anchura uno sobre n. Para cada punto positivo acaba desapareciendo, pero su área sigue siendo uno. [TRIGGER_2] Por eso convergencia puntual no basta para intercambiar límite y esperanza. La convergencia monótona sí lo permite para una sucesión creciente no negativa. [TRIGGER_3] La convergencia dominada usa otra garantía: un techo integrable común. Ese techo controla las colas y evita que la masa se esconda en picos cada vez más altos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=n\mathbf1_{(0,1/n)},\quad X_n\to0,\quad\mathbb E X_n=1$`.
- MathTex: `$0\le X_n\uparrow X\Rightarrow\mathbb E X_n\uparrow\mathbb E X$`.
- MathTex: `$X_n\to X\ {\rm c.s.},\ |X_n|\le Y\in L^1\Rightarrow\mathbb E X_n\to\mathbb E X$`.
- Picos n=2,4,8,16 con áreas rotuladas; panel secundario para techo Y; valores altos recortados solo mediante indicador explícito de escala.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Transform picos conservando área y Write dos límites distintos.
- [TRIGGER_2]: Sustituir por escalones crecientes de la escena 4 y mostrar hipótesis monótona.
- [TRIGGER_3]: Create curva techo Y y tres curvas dominadas; SurroundingRectangle en Y∈L1.

#### Escena: 07

##### Nombre: Un mismo promedio en dos espacios

##### Descripcion Breve: La ley imagen unifica suma discreta y densidad.

##### Objetivo Pedagogico: Explicar la fórmula de cambio de variable probabilístico.

##### Voz en off:

> "[TRIGGER_1] Podemos promediar sobre los resultados originales o sobre los valores que produce X. La ley de X transporta las probabilidades entre esos dos espacios. [TRIGGER_2] Si la ley es discreta, obtenemos una suma. Si tiene densidad, obtenemos la integral habitual de x por la densidad. [TRIGGER_3] Pero no toda ley tiene densidad. La integral respecto de la distribución también cubre masas puntuales y leyes singulares; ese es el lenguaje que las contiene a todas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[g(X)]=\int_\Omega g(X)\,dP=\int_\mathbb R g(x)\,P_X(dx)$`.
- MathTex: `$\mathbb E X=\sum_x xp_X(x)\quad\text{(discreta)}$`.
- MathTex: `$\mathbb E X=\int_\mathbb R xf_X(x)\,dx\quad\text{(con densidad)}$`.
- Dos recintos Ω y R unidos por X; ruleta discreta y densidad exponencial λ=1 en paneles alternados; tarjeta «ley singular: también cubierta».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create flecha de transporte y Write igualdad dividida en dos renglones.
- [TRIGGER_2]: Transform región R en puntos y después curva de densidad; reemplazar la fórmula correspondiente.
- [TRIGGER_3]: Restaurar integral respecto de P_X y añadir tres etiquetas: discreta, densidad, singular.

#### Escena: 08

##### Nombre: La herramienta que necesitábamos

##### Descripcion Breve: Se cierra con el ejemplo de ruleta y la construcción general.

##### Objetivo Pedagogico: Consolidar el papel de medida, medibilidad y límites.

##### Voz en off:

> "[TRIGGER_1] El promedio de la ruleta era tres porque agrupamos resultados por premio y pesamos cada grupo. Lebesgue conserva esa idea para funciones mucho más generales. [TRIGGER_2] Los escalones nos dieron una construcción; la medibilidad hizo legales sus bases; los teoremas de convergencia dijeron cuándo los límites respetan el promedio. [TRIGGER_3] La pregunta práctica ya no es solo qué fórmula integrar. También debemos preguntar respecto de qué medida y con qué hipótesis. Esa precisión será crucial cuando promediemos funciones aleatorias completas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E X=\int_\Omega X\,dP$`.
- MathTex: `$\text{funciones simples}\longrightarrow\text{aproximación}\longrightarrow\text{integral}$`.
- Ruleta original, escalones y símbolo de integral conectados; tres tarjetas «medida», «medibilidad», «límite autorizado».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: FadeIn ruleta y resultado 3.
- [TRIGGER_2]: TransformFromCopy ruleta a escalones; conectar con integral mediante Arrow.
- [TRIGGER_3]: Indicate tarjetas y dejar definición de esperanza en pantalla durante 5 s.

