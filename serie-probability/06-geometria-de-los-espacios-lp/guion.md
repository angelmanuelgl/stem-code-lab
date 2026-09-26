# Video 06: La distancia entre dos variables aleatorias

Un pronóstico puede acertar casi siempre y tener error cuadrático enorme. Se construyen las normas Lp, su geometría y el papel especial de L².

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 521 palabras (3.6–4.3 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- p≥1; variables identificadas por igualdad casi segura. Hilbert corresponde solo a p=2. Los dibujos vectoriales son esquemas de un espacio que puede ser infinito-dimensional.

## Bibliografía y decisiones matemáticas

Proba §§2.3,2.4,2.8; Probita §§5.3–5.4. Completitud y proyección en Hilbert se enuncian como herramientas, con prueba explícita de ortogonalidad en el ejemplo finito.

#### Escena: 01

##### Nombre: Un pronóstico casi perfecto

##### Descripcion Breve: Un fallo raro pero grande domina un promedio.

##### Objetivo Pedagogico: Distinguir frecuencia y severidad.

##### Voz en off:

> "[TRIGGER_1] Este predictor falla una vez entre mil. Parece excelente hasta que descubrimos que ese fallo tiene tamaño mil. [TRIGGER_2] La frecuencia de error es pequeña, pero su contribución cuadrática es mil. Contar fallos y medir su magnitud son preguntas diferentes. [TRIGGER_3] Necesitamos una distancia entre variables que incorpore cuánto duele equivocarse. El parámetro p decidirá cuánto castigar los errores grandes."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(E=1000)=10^{-3},\quad P(E=0)=1-10^{-3}$`.
- MathTex: `$\mathbb E E^2=1000$`.
- Mil casillas representadas por malla 25×40; una marcada; barra de error con escala explícita.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create malla y destacar una celda.
- [TRIGGER_2]: Write cálculo del segundo momento.
- [TRIGGER_3]: Transform malla a medidor de frecuencia y medidor de magnitud.

#### Escena: 02

##### Nombre: De vectores a variables

##### Descripcion Breve: Una distribución finita induce una norma ponderada.

##### Objetivo Pedagogico: Construir Lp.

##### Voz en off:

> "[TRIGGER_1] Una variable sobre tres resultados es un vector de tres valores. Sus probabilidades dan pesos a las coordenadas. [TRIGGER_2] Elevamos el valor absoluto a p, promediamos y tomamos raíz p. En un espacio general, esa suma se convierte en esperanza. [TRIGGER_3] L p contiene las variables con ese momento finito. La distancia entre X e Y es la norma de su diferencia."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\|X\|_p=(\mathbb E|X|^p)^{1/p}$`.
- MathTex: `$L^p=\{X:\mathbb E|X|^p<\infty\}/\sim$`.
- MathTex: `$d_p(X,Y)=\|X-Y\|_p$`.
- Tres coordenadas con probabilidades 1/2,1/4,1/4; calculadora de norma; símbolo de integral.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create vector y pesos.
- [TRIGGER_2]: Write suma ponderada y Transform a esperanza.
- [TRIGGER_3]: Mostrar X−Y y norma como distancia.

#### Escena: 03

##### Nombre: Ignorar diferencias nulas

##### Descripcion Breve: Dos funciones distintas puntualmente representan el mismo elemento.

##### Objetivo Pedagogico: Explicar cociente por igualdad c.s.

##### Voz en off:

> "[TRIGGER_1] Si dos variables difieren solo en un conjunto de probabilidad cero, su distancia L p es cero. [TRIGGER_2] Para que distancia cero signifique el mismo objeto, identificamos esas variables. Un punto aislado de probabilidad cero no crea una dirección nueva. [TRIGGER_3] Por eso los elementos de L p son clases de equivalencia. Podemos trabajar con representantes, pero las conclusiones se entienden casi seguramente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X\sim Y\iff P(X=Y)=1$`.
- MathTex: `$\|X-Y\|_p=0\iff X=Y\ {\rm c.s.}$`.
- Curvas iguales salvo en x=1/2; punto hueco/lleno; recinto «misma clase».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create dos curvas y diferencia puntual.
- [TRIGGER_2]: Write integral de diferencia cero.
- [TRIGGER_3]: Agrupar ambas bajo misma clase y encerrar c.s.

#### Escena: 04

##### Nombre: El salón de L dos

##### Descripcion Breve: Producto interno produce ángulos y Pitágoras.

##### Objetivo Pedagogico: Identificar estructura Hilbert.

##### Voz en off:

> "[TRIGGER_1] En L dos podemos definir un producto interno como la esperanza del producto. Cauchy-Schwarz garantiza que es finito. [TRIGGER_2] La norma correspondiente es la raíz del segundo momento. Si el producto interno es cero, hablamos de ortogonalidad y se cumple Pitágoras. [TRIGGER_3] Este espacio es completo: una sucesión de Cauchy tiene límite dentro de L dos. Enunciamos esta propiedad porque permitirá construir objetos nuevos mediante límites."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\langle X,Y\rangle=\mathbb E(XY)$`.
- MathTex: `$\langle X,Y\rangle=0\Rightarrow\|X+Y\|_2^2=\|X\|_2^2+\|Y\|_2^2$`.
- MathTex: `$L^2\text{ es completo}$`.
- Vectores en plano esquemático; triángulo rectángulo; tarjeta «completitud: teorema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create vectores y producto interno.
- [TRIGGER_2]: Rotate a posición ortogonal y Write Pitágoras.
- [TRIGGER_3]: Mostrar puntos de una sucesión Cauchy acercándose a un punto incluido.

#### Escena: 05

##### Nombre: Qué significa converger en Lp

##### Descripcion Breve: Un único número resume un error aleatorio.

##### Objetivo Pedagogico: Definir convergencia y comparar exponentes.

##### Voz en off:

> "[TRIGGER_1] Convergencia en L p significa que la distancia al límite tiende a cero: el momento p del error desaparece. [TRIGGER_2] En un espacio de probabilidad, controlar un exponente mayor controla uno menor. Jensen da que la norma L p no supera la L q cuando p es menor que q. [TRIGGER_3] Con Markov obtenemos además convergencia en probabilidad. El mismo error sirve para los dos puentes, pero cada uno mide algo distinto."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n\xrightarrow{L^p}X\iff\mathbb E|X_n-X|^p\to0$`.
- MathTex: `$1\le p\le q:\ \|Z\|_p\le\|Z\|_q$`.
- MathTex: `$P(|Z|>\varepsilon)\le\|Z\|_p^p/\varepsilon^p$`.
- Barras de momentos y flechas Lq→Lp→P; etiqueta P(Ω)=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write definición y animar barras.
- [TRIGGER_2]: Aplicar Jensen a |Z|p con exponente q/p.
- [TRIGGER_3]: Dibujar flecha a probabilidad usando Markov.

#### Escena: 06

##### Nombre: Los picos que sobreviven al promedio

##### Descripcion Breve: Convergencia puntual no controla las normas.

##### Objetivo Pedagogico: Probar una no implicación.

##### Voz en off:

> "[TRIGGER_1] Sobre el intervalo unidad, el pico de altura n y anchura uno sobre n converge a cero en cada punto, usando el intervalo abierto en cero. [TRIGGER_2] Sin embargo, su norma L uno vale uno. Para p mayor que uno, el momento p crece como n elevado a p menos uno. [TRIGGER_3] Las trayectorias pueden estabilizarse y aun así conservar o aumentar la energía promedio. Para pasar a L p necesitamos una condición adicional que controle las colas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=n\mathbf1_{(0,1/n)}$`.
- MathTex: `$\mathbb E|X_n|^p=n^{p-1}$`.
- Picos n=2,4,8,16; ejes con escala anotada; medidores L1 y momento p=2.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create picos y punto fijo ω=0.4.
- [TRIGGER_2]: Calcular área ponderada para p=1 y 2.
- [TRIGGER_3]: Write c.s. no implica Lp; mantener el pico como testigo.

#### Escena: 07

##### Nombre: La mejor predicción constante

##### Descripcion Breve: Minimizar error cuadrático produce la media.

##### Objetivo Pedagogico: Derivar proyección elemental.

##### Voz en off:

> "[TRIGGER_1] Queremos predecir X usando una constante a. Separaremos el error alrededor de su media. [TRIGGER_2] Al expandir el cuadrado, el término cruzado desaparece porque X menos su media tiene esperanza cero. [TRIGGER_3] Queda varianza más distancia cuadrática de a a la media. El mínimo ocurre en la media. Cuando permitamos información parcial, esta proyección se convertirá en esperanza condicional."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E(X-a)^2=\operatorname{Var}(X)+(a-\mathbb EX)^2$`.
- MathTex: `$\arg\min_{a\in\mathbb R}\mathbb E(X-a)^2=\mathbb EX$`.
- Parábola de riesgo en a; media marcada; vector X y subespacio de constantes.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create parábola y mover a.
- [TRIGGER_2]: Write expansión con término cruzado y cancelarlo.
- [TRIGGER_3]: Llevar a al mínimo y dibujar proyección al subespacio.

#### Escena: 08

##### Nombre: Construir por distancia

##### Descripcion Breve: Una sucesión Cauchy anticipa la integral estocástica.

##### Objetivo Pedagogico: Cerrar con utilidad del espacio.

##### Voz en off:

> "[TRIGGER_1] Una distancia adecuada no solo compara resultados. También permite definir objetos que todavía no sabemos calcular directamente. [TRIGGER_2] Si aproximaciones elementales son Cauchy en L dos, la completitud garantiza un límite y la distancia mide su error. [TRIGGER_3] Ese mecanismo construirá la integral de Itô. Antes de ver símbolos nuevos, ya conocemos su motor: aproximar, controlar el segundo momento y completar."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\|Z_n-Z_m\|_2\to0\Rightarrow\exists Z\in L^2:\|Z_n-Z\|_2\to0$`.
- Escalones abstractos Z1,Z2,Z3 y límite; cadena aproximar→controlar→completar.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create tres aproximaciones.
- [TRIGGER_2]: Write criterio Cauchy y punto límite.
- [TRIGGER_3]: Transform cadena hacia etiqueta «futura integral de Itô».

