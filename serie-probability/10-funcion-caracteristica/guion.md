# Video 10: La huella digital de una distribución

Una explicación geométrica y algebraica de la función característica, con independencia, transformaciones, momentos y convergencia.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 562 palabras (3.9–4.7 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- La unicidad y continuidad de Lévy se enuncian como teoremas. No se afirma que todas las distribuciones posean momentos.

## Bibliografía y decisiones matemáticas

Proba §§3.1,3.5–3.6, pp. impresas 63–71 y 87–91. Cauchy sirve como contraejemplo al uso incondicional de momentos.

#### Escena: 01

##### Nombre: La distribución como una orquesta

##### Descripcion Breve: Cada valor produce una fase de un círculo.

##### Objetivo Pedagogico: Motivar una transformación que conserve toda la ley.

##### Voz en off:

> "[TRIGGER_1] Imagina asignar a cada resultado una flecha sobre un círculo. Los valores deciden el ángulo y sus probabilidades deciden el peso. [TRIGGER_2] Al promediar esas flechas obtenemos un número complejo. Repetimos con distintas velocidades de giro y aparece una firma de la distribución. [TRIGGER_3] Esa firma convierte sumar variables independientes en multiplicar funciones. Vamos a construirla sin suponer que existen todos los momentos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$e^{itx}=\cos(tx)+i\sin(tx)$`.
- Circle de radio 1.6; flechas para x=−1,0,2 con pesos 1/4,1/2,1/4; slider t; vector promedio.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create círculo y flechas.
- [TRIGGER_2]: Añadir pesos y vector promedio.
- [TRIGGER_3]: Mover t entre 0 y 3 conservando los valores x.

#### Escena: 02

##### Nombre: Definir la firma

##### Descripcion Breve: Se integra una función compleja acotada.

##### Objetivo Pedagogico: Mostrar existencia universal.

##### Voz en off:

> "[TRIGGER_1] La función característica de X es la esperanza de exponencial de i por t por X. [TRIGGER_2] Toda flecha tiene longitud uno, así que esta esperanza siempre existe y su módulo no supera uno. En t igual a cero todas apuntan a la derecha y el promedio vale uno. [TRIGGER_3] Esta garantía la distingue de la función generadora de momentos, que puede divergir. Solo necesitamos una distribución de probabilidad."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_X(t)=\mathbb E[e^{itX}]=\int e^{itx}\,P_X(dx)$`.
- MathTex: `$|\varphi_X(t)|\le1,\quad\varphi_X(0)=1$`.
- Círculo unidad y trayectoria del promedio dentro del disco; panel con partes real e imaginaria.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write definición y descomponer coseno/seno.
- [TRIGGER_2]: Encerrar promedio dentro del disco mediante desigualdad triangular.
- [TRIGGER_3]: Llevar t a cero y unir todas las flechas.

#### Escena: 03

##### Nombre: Dos ejemplos que podemos calcular

##### Descripcion Breve: Bernoulli y una variable simétrica producen firmas explícitas.

##### Objetivo Pedagogico: Hacer tangible el promedio complejo.

##### Voz en off:

> "[TRIGGER_1] Si X vale cero o uno con probabilidades uno menos p y p, la firma es uno menos p más p por exponencial de i t. [TRIGGER_2] Si X vale menos uno o uno con igual probabilidad, los senos se cancelan y queda coseno de t. [TRIGGER_3] Las curvas pueden ser negativas o complejas. No son densidades: codifican probabilidades, pero sus valores no son probabilidades."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_{\mathrm{Bern}(p)}(t)=1-p+pe^{it}$`.
- MathTex: `$P(X=\pm1)=1/2\Rightarrow\varphi_X(t)=\cos t$`.
- Dos diagramas de flechas; gráficos real/imaginaria para p=0.3; curva cos t cruzando cero.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create Bernoulli y Write suma ponderada.
- [TRIGGER_2]: Transform a dos flechas simétricas y cancelar senos.
- [TRIGGER_3]: Resaltar región negativa y tarjeta «no es una densidad».

#### Escena: 04

##### Nombre: Las sumas se vuelven productos

##### Descripcion Breve: Independencia permite factorizar una esperanza.

##### Objetivo Pedagogico: Derivar la propiedad principal.

##### Voz en off:

> "[TRIGGER_1] La exponencial de una suma se separa en producto de exponenciales. Ese paso es puramente algebraico. [TRIGGER_2] Para separar la esperanza del producto sí necesitamos independencia. Entonces la firma de X más Y es el producto de sus firmas. [TRIGGER_3] Si repetimos variables independientes con la misma ley, la firma de la suma es una potencia. Aquí está la puerta de entrada a los teoremas límite."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$e^{it(X+Y)}=e^{itX}e^{itY}$`.
- MathTex: `$X\perp Y\Rightarrow\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$`.
- MathTex: `$\varphi_{\sum_{j=1}^nX_j}(t)=\varphi_X(t)^n\quad\text{iid}$`.
- Dos ruedas de fases; caja «independencia» entre expectativa del producto y producto de expectativas; convolución de masas en panel izquierdo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write identidad algebraica.
- [TRIGGER_2]: Activar caja independencia y factorizar.
- [TRIGGER_3]: Duplicar a n factores y TransformMatchingTex a potencia.

#### Escena: 05

##### Nombre: Escalar, trasladar y derivar

##### Descripcion Breve: La firma registra transformaciones y momentos existentes.

##### Objetivo Pedagogico: Corregir la idea de que toda ley tiene todos los momentos.

##### Voz en off:

> "[TRIGGER_1] Multiplicar X por a reemplaza t por a t; sumar b multiplica la firma por una fase. [TRIGGER_2] Si el momento absoluto de orden k es finito, podemos derivar k veces y evaluar en cero: aparece i elevado a k por el momento. [TRIGGER_3] La condición es importante. Cauchy tiene firma exponencial de menos valor absoluto de t, pero no tiene esperanza. La firma existe aunque las derivadas o los momentos fallen."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$`.
- MathTex: `$\mathbb E|X|^k<\infty\Rightarrow\varphi_X^{(k)}(0)=i^k\mathbb E[X^k]$`.
- MathTex: `$X\sim\mathrm{Cauchy}(0,1)\Rightarrow\varphi_X(t)=e^{-|t|}$`.
- Slider a,b; fase global; gráfico e^−|t| con esquina en cero; condición de integrabilidad fija.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Transform ejes al escalar y fase al trasladar.
- [TRIGGER_2]: Write derivada bajo la esperanza y condición.
- [TRIGGER_3]: Create esquina Cauchy y marcar ausencia de derivada en cero.

#### Escena: 06

##### Nombre: Por qué la firma identifica la ley

##### Descripcion Breve: Una suavización gaussiana permite interpretar la inversión.

##### Objetivo Pedagogico: Explicar unicidad sin prometer una prueba omitida.

##### Voz en off:

> "[TRIGGER_1] Un teorema de unicidad dice que dos leyes con la misma función característica son iguales. La intuición viene de invertir Fourier. [TRIGGER_2] Si añadimos un ruido gaussiano independiente pequeño, las firmas se multiplican por un factor que decae y permite una inversión bien comportada. [TRIGGER_3] Firmas iguales dan leyes suavizadas iguales; al retirar el ruido, recuperamos las leyes originales. Enunciamos el teorema de inversión usado, sin confundir esta ruta conceptual con todos sus detalles analíticos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_{X+\varepsilon Z}(t)=\varphi_X(t)e^{-\varepsilon^2t^2/2},\quad Z\sim N(0,1)$`.
- MathTex: `$\varphi_X=\varphi_Y\Rightarrow\mathcal L(X)=\mathcal L(Y)$`.
- Dos distribuciones suavizadas por campanas pequeñas; multiplicador gaussiano en frecuencia; etiqueta «inversión: teorema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mostrar dos firmas iguales.
- [TRIGGER_2]: Aplicar suavización gaussiana y señalar decaimiento.
- [TRIGGER_3]: Reducir ε y Write unicidad de la ley.

#### Escena: 07

##### Nombre: Continuidad de Lévy

##### Descripcion Breve: La convergencia puntual de firmas necesita continuidad en el origen.

##### Objetivo Pedagogico: Enunciar el criterio exacto.

##### Voz en off:

> "[TRIGGER_1] Si las leyes convergen débilmente, sus funciones características convergen en cada t. Esto sigue probando coseno y seno, funciones continuas acotadas. [TRIGGER_2] En la otra dirección, si las firmas tienen límite puntual y ese límite es continuo en cero, existe una ley con esa firma y las leyes convergen hacia ella. [TRIGGER_3] Sin continuidad en cero puede escaparse la masa. Para normales de varianza n, el límite vale cero fuera del origen y uno en el origen."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_n(t)\to\varphi(t)\ \forall t,\quad\varphi\text{ continua en }0\Rightarrow X_n\Rightarrow X$`.
- MathTex: `$X_n\sim N(0,n):\quad\varphi_n(t)=e^{-nt^2/2}$`.
- Curvas gaussianas en frecuencia estrechándose; punto aislado 1 en origen del límite; masas espaciales ensanchándose.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write dirección directa con cos y sin.
- [TRIGGER_2]: Presentar recíproca con continuidad resaltada.
- [TRIGGER_3]: Animar varianza n creciente y discontinuidad del límite.

#### Escena: 08

##### Nombre: La firma prepara una campana

##### Descripcion Breve: Se conecta escalamiento y potencia con una suma normalizada.

##### Objetivo Pedagogico: Cerrar con una herramienta utilizable.

##### Voz en off:

> "[TRIGGER_1] Para estudiar una suma centrada dividida entre raíz de n, evaluamos una firma cerca de cero y la elevamos a n. [TRIGGER_2] La conducta local de esa función decide la forma global del límite. Con media cero y varianza uno, su término principal después de la constante es menos t cuadrada sobre dos. [TRIGGER_3] Ya tenemos las piezas: independencia, escalamiento y continuidad de Lévy. El siguiente cálculo explicará por qué sobrevive precisamente una firma gaussiana."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_{\frac1{\sqrt n}\sum_{j=1}^nX_j}(t)=\left[\varphi_X(t/\sqrt n)\right]^n$`.
- MathTex: `$\varphi_X(u)=1-u^2/2+o(u^2)\quad(\mathbb EX=0,\ \mathbb EX^2=1)$`.
- Zoom al origen de una firma; n factores; campana normal como pregunta final, no como prueba visual.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write firma de suma normalizada.
- [TRIGGER_2]: Hacer zoom en u=t/√n y resaltar término cuadrático.
- [TRIGGER_3]: Conectar potencia con silueta de firma e^−t²/2.

