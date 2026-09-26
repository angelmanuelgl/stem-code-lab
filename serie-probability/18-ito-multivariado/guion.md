# Video 18: Cuando las fuentes de ruido se hablan

Correlación, covariación y fórmula multivariada de Itô, con dimensiones explícitas y dos ejemplos comprobables.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 558 palabras (3.8–4.7 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- B estándar m-dimensional con componentes independientes; para W correlacionado usar matriz R constante semidefinida positiva. No se usa rho fuera de [−1,1].

## Bibliografía y decisiones matemáticas

Proba §§1.3,5.1–5.2: vectores y covarianzas. Complemento: [Lawler §§3.6–3.7](https://www.math.uchicago.edu/~lawler/finbook.pdf). Las fórmulas de producto y energía se derivan en pantalla.

#### Escena: 01

##### Nombre: Dos sensores oyen parte del mismo ruido

##### Descripcion Breve: Se comparan nubes independientes y correlacionadas.

##### Objetivo Pedagogico: Motivar covariación.

##### Voz en off:

> "[TRIGGER_1] Dos sensores pueden moverse al mismo tiempo porque comparten una perturbación. Si los tratamos como independientes, calculamos mal el riesgo conjunto. [TRIGGER_2] Una nube circular de incrementos se convierte en una elipse cuando introducimos correlación. [TRIGGER_3] En varias dimensiones, la corrección de Itô debe recordar no solo cuánto fluctúa cada componente, sino cómo fluctúan juntos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\operatorname{Cov}(\Delta W_1,\Delta W_2)=\rho\,\Delta t$`.
- Dos trazas y nube de 3000 incrementos, semilla 1801; slider ρ=0,0.7,−0.7; ejes con misma escala.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create trazas y nube circular.
- [TRIGGER_2]: Transform con correlación positiva y negativa usando las mismas normales base.
- [TRIGGER_3]: Write covarianza y marcar inclinación de elipse.

#### Escena: 02

##### Nombre: Construir ruidos correlacionados

##### Descripcion Breve: Una combinación lineal de Wiener independientes produce la correlación.

##### Objetivo Pedagogico: Dar una receta verificable.

##### Voz en off:

> "[TRIGGER_1] Tomemos B uno y B dos independientes. Definimos W uno como B uno y W dos como rho por B uno más raíz de uno menos rho cuadrada por B dos. [TRIGGER_2] Cada W tiene varianza t y la covarianza entre ambos es rho t. La matriz resultante debe ser semidefinida positiva, de modo que valor absoluto de rho no exceda uno. [TRIGGER_3] En los extremos, una fuente deja de aportar: los dos movimientos quedan perfectamente ligados."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_1=B_1,\quad W_2=\rho B_1+\sqrt{1-\rho^2}B_2$`.
- MathTex: `$R=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\succeq0,\quad|\rho|\le1$`.
- Dos fuentes B entrando a mezclador; pesos ρ y √(1−ρ²); elipse que colapsa a recta cuando |ρ|=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create mezclador.
- [TRIGGER_2]: Calcular varianzas y covarianza.
- [TRIGGER_3]: Mover ρ a extremos y mostrar pérdida de rango.

#### Escena: 03

##### Nombre: La suma de productos cruzados

##### Descripcion Breve: La covariación es el límite de productos de incrementos.

##### Objetivo Pedagogico: Definir el término que faltaba.

##### Voz en off:

> "[TRIGGER_1] Además de sumar cuadrados, sumamos el producto del incremento de una componente por el de otra. [TRIGGER_2] Para Brownianos correlacionados esa suma converge en L dos a rho por T sobre particiones deterministas cuya malla tiende a cero. [TRIGGER_3] Con fuentes independientes, el límite es cero; con una fuente consigo misma, vuelve a ser T. La regla dW i por dW j igual a R i j dt resume esos límites."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$[W_i,W_j]_T=\lim_{|\pi|\to0}\sum_k\Delta W_{i,k}\Delta W_{j,k}=R_{ij}T$`.
- MathTex: `$dW_i\,dW_j=R_{ij}\,dt$`.
- Productos cruzados por intervalo como barras positivas/negativas; contador; líneas objetivo ρT; nota varianza de suma O(|π|).

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create productos y contador con ρ=0.7.
- [TRIGGER_2]: Refinar malla coherente y Write límite.
- [TRIGGER_3]: Cambiar a ρ=0 y a i=j para comparar.

#### Escena: 04

##### Nombre: El estado y las fuentes tienen tamaños distintos

##### Descripcion Breve: Una matriz rectangular transforma m ruidos en n variables.

##### Objetivo Pedagogico: Fijar dimensiones y covarianza efectiva.

##### Voz en off:

> "[TRIGGER_1] Nuestro estado X tiene n componentes y el Browniano B tiene m fuentes independientes. La matriz de difusión G tiene n filas y m columnas. [TRIGGER_2] El incremento aleatorio es G por dB y su matriz de covariación es G por G transpuesta, multiplicada por dt. [TRIGGER_3] Si usamos ruidos correlacionados con matriz R, aparece G R G transpuesta. No confundamos la matriz de difusión con la covarianza del estado."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX=b\,dt+G\,dB,\quad G\in\mathbb R^{n\times m}$`.
- MathTex: `$d[X_i,X_j]_t=(GG^\top)_{ij}\,dt$`.
- MathTex: `$a=GRG^\top\quad\text{si }d[W]_t=R\,dt$`.
- Bloques dimensionales n×m, m×1 y n×1; producto GGᵀ; ejemplo n=3,m=2 en diagrama.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write dimensiones en cada bloque.
- [TRIGGER_2]: Multiplicar dX por su transpuesta y conservar ruido².
- [TRIGGER_3]: Sustituir identidad por R y mostrar covarianza efectiva.

#### Escena: 05

##### Nombre: La Hessiana recoge todas las curvaturas

##### Descripcion Breve: Taylor multivariado conduce a la fórmula de Itô.

##### Objetivo Pedagogico: Presentar fórmula completa sin perder factores.

##### Voz en off:

> "[TRIGGER_1] Una función escalar de varias variables tiene gradiente y matriz Hessiana. Su Taylor de segundo orden contiene pares de incrementos. [TRIGGER_2] Sustituimos cada producto dX i dX j por a i j dt y sumamos todos los pares. La corrección es un medio de la traza de a por la Hessiana. [TRIGGER_3] La parte aleatoria es el gradiente transpuesto por G dB. Esta fórmula permite estudiar observables de un sistema multidimensional sin resolver toda su distribución."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$df(t,X_t)=\left(f_t+\nabla f^\top b+\frac12\operatorname{tr}(aD^2f)\right)dt+\nabla f^\top G\,dB_t$`.
- MathTex: `$\frac12\operatorname{tr}(aD^2f)=\frac12\sum_{i,j}a_{ij}f_{x_ix_j}$`.
- Superficie f(x,y); vector gradiente y cuadrícula de Hessiana; matriz a con entradas alineadas; f∈C1,2 visible.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create superficie y Taylor de segundo orden.
- [TRIGGER_2]: Emparejar entradas de a y Hessiana.
- [TRIGGER_3]: Write fórmula en tres renglones y destacar factor 1/2.

#### Escena: 06

##### Nombre: El producto revela la correlación

##### Descripcion Breve: f(x,y)=xy da un término cruzado explícito.

##### Objetivo Pedagogico: Verificar la fórmula con un observable simple.

##### Voz en off:

> "[TRIGGER_1] Para f igual a x por y, las segundas derivadas puras son cero y las dos derivadas cruzadas son uno. [TRIGGER_2] El medio de la fórmula se cancela con esas dos contribuciones iguales. Obtenemos d del producto igual a W dos dW uno más W uno dW dos más rho dt. [TRIGGER_3] Al tomar esperanza, los términos de Itô desaparecen y el promedio del producto vale rho t. La corrección reproduce exactamente la covarianza conocida."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$d(W_1W_2)=W_2\,dW_1+W_1\,dW_2+\rho\,dt$`.
- MathTex: `$\mathbb E[W_1(t)W_2(t)]=\rho t$`.
- Hessiana [[0,1],[1,0]]; dos términos cruzados rotulados; gráfico promedio del producto y línea ρt.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write derivadas explícitas.
- [TRIGGER_2]: Contar los dos términos y cancelar el medio.
- [TRIGGER_3]: Integrar y verificar esperanza ρt.

#### Escena: 07

##### Nombre: Energía de un sistema

##### Descripcion Breve: La norma cuadrada relaciona deriva y difusión.

##### Objetivo Pedagogico: Preparar estabilidad y existencia.

##### Voz en off:

> "[TRIGGER_1] Para la energía f igual a la norma cuadrada de X, el gradiente es dos X y la Hessiana dos veces la identidad. [TRIGGER_2] La corrección resulta ser la traza de G G transpuesta, es decir la norma de Frobenius de G al cuadrado. [TRIGGER_3] Esto separa disipación por la deriva e inyección de variabilidad por el ruido. Será útil para comprobar si un modelo mantiene controlados sus segundos momentos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$d\|X\|^2=(2X^\top b+\|G\|_F^2)dt+2X^\top G\,dB$`.
- MathTex: `$b=-\theta X,\ G=\sigma I_n\Rightarrow\frac{d}{dt}\mathbb E\|X\|^2=-2\theta\mathbb E\|X\|^2+n\sigma^2$`.
- Partícula 2D atraída al origen; círculo de energía; barras disipación y ruido; θ=1,σ=0.5,n=2.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create partícula y norma cuadrada.
- [TRIGGER_2]: Sustituir derivadas y calcular traza.
- [TRIGGER_3]: Mostrar balance de energía con valores indicados.

#### Escena: 08

##### Nombre: Evitar contar dos veces la correlación

##### Descripcion Breve: Dos representaciones equivalentes deben producir la misma covarianza.

##### Objetivo Pedagogico: Cerrar con una comprobación de implementación.

##### Voz en off:

> "[TRIGGER_1] Podemos usar ruidos independientes y una difusión que ya mezcle las fuentes, o ruidos correlacionados y una difusión separada. [TRIGGER_2] Si generamos ruido correlacionado y además multiplicamos por el mismo factor de correlación otra vez, cambiamos el modelo. [TRIGGER_3] La prueba más simple es calcular la covarianza efectiva a. Si las dimensiones y a coinciden, las dos representaciones describen el mismo ruido gaussiano instantáneo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$R=LL^\top,\quad G\,dW=GL\,dB$`.
- MathTex: `$(GL)(GL)^\top=GRG^\top$`.
- Dos rutas de cálculo: B→L→W→G→X y B→GL→X; salida a idéntica; ruta doble L tachada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create ambas rutas.
- [TRIGGER_2]: Multiplicar covarianzas y comprobar igualdad.
- [TRIGGER_3]: Mostrar error de doble L y cerrar con matriz a como control.

