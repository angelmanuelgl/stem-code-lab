# Video 20: ¿La ecuación que simulamos tiene una respuesta?

Prueba guiada por Picard, Doob, isometría y Gronwall, con ejemplos que separan no unicidad y explosión.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 605 palabras (4.2–5 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Demostración bajo Lipschitz global y crecimiento lineal; extensión local explicada mediante paradas. S² es el espacio de procesos continuos adaptados con norma cuadrática del supremo.

## Bibliografía y decisiones matemáticas

Proba §§2.3–2.4 y §4.2 proporcionan bases de convergencia y condicionamiento. Consulta complementaria: [Zimmer, Stochastic Calculus, construcción y existencia](https://www.math.uchicago.edu/~may/VIGRE/VIGRE2011/REUPapers/Zimmer.pdf). Las estimaciones se explicitan en el episodio.

#### Escena: 01

##### Nombre: Una simulación puede dibujar algo que no resuelve nada

##### Descripcion Breve: Dos EDO dentro de la familia de EDE muestran problemas distintos.

##### Objetivo Pedagogico: Motivar existencia, unicidad y no explosión.

##### Voz en off:

> "[TRIGGER_1] Una computadora siempre puede intentar avanzar una ecuación. Eso no garantiza que el modelo tenga una solución global única. [TRIGGER_2] La ecuación x prima igual a x cuadrada, empezando en uno, explota en tiempo uno. La ecuación x prima igual a dos raíz del valor absoluto de x, empezando en cero, permite esperar y luego salir. [TRIGGER_3] Ambas son EDE con ruido cero. Antes de discretizar debemos distinguir explosión y falta de unicidad."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$x'=x^2,\ x(0)=1\Rightarrow x(t)=1/(1-t)$`.
- MathTex: `$x'=2\sqrt{|x|},\ x(0)=0:\quad x_a(t)=(t-a)_+^2$`.
- Dos paneles alternados: asíntota en t=1 y familia con a=0,0.5,1; etiqueta σ=0.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create solución explosiva.
- [TRIGGER_2]: Transform a familia con tiempos de espera.
- [TRIGGER_3]: Write tres preguntas: existe, es única, dura hasta T.

#### Escena: 02

##### Nombre: Un teorema que sí podemos usar

##### Descripcion Breve: Lipschitz global y crecimiento lineal controlan diferencias y tamaño.

##### Objetivo Pedagogico: Enunciar condiciones suficientes.

##### Voz en off:

> "[TRIGGER_1] En un horizonte finito T, suponemos coeficientes medibles, Lipschitz globales en el estado y con crecimiento a lo sumo lineal, uniformemente en tiempo. [TRIGGER_2] El valor inicial es medible al tiempo cero y tiene segundo momento finito; el Browniano lo es respecto de la filtración dada. [TRIGGER_3] Entonces existe una solución fuerte continua y adaptada, única hasta indistinguibilidad, con segundo momento del supremo finito. Son condiciones suficientes, no una clasificación de todos los modelos posibles."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$|b(t,x)-b(t,y)|+\|\sigma(t,x)-\sigma(t,y)\|\le L|x-y|$`.
- MathTex: `$|b(t,x)|^2+\|\sigma(t,x)\|^2\le K(1+|x|^2)$`.
- MathTex: `$\mathbb E|X_0|^2<\infty,\quad\mathbb E\sup_{t\le T}|X_t|^2<\infty$`.
- Tarjetas regularidad/diferencias/tamaño/condición inicial; conos de crecimiento ±C(1+|x|); constantes L,K,T visibles.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write Lipschitz y crecimiento.
- [TRIGGER_2]: Añadir filtración e inicial.
- [TRIGGER_3]: Mostrar conclusión de existencia y unicidad con regularidad.

#### Escena: 03

##### Nombre: Picard usa una trayectoria anterior

##### Descripcion Breve: Se define una secuencia por integrales con el mismo ruido.

##### Objetivo Pedagogico: Construir aproximaciones causales.

##### Voz en off:

> "[TRIGGER_1] Empezamos con el proceso constante igual a X cero. Para el siguiente intento, evaluamos los coeficientes en el intento anterior y calculamos sus dos integrales. [TRIGGER_2] Todas las iteraciones usan el mismo Browniano. Cambiar de ruido entre ellas impediría medir si se están acercando a una solución del mismo problema. [TRIGGER_3] Adaptación e integrabilidad permiten repetir la operación. La pregunta es si estas trayectorias aproximadas forman una sucesión convergente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X^{(0)}_t=X_0$`.
- MathTex: `$X^{(k+1)}_t=X_0+\int_0^tb(s,X^{(k)}_s)ds+\int_0^t\sigma(s,X^{(k)}_s)dW_s$`.
- Cadena de operadores Picard; una fuente W común a todas las iteraciones; tres curvas aproximadas esquemáticas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create proceso inicial.
- [TRIGGER_2]: Aplicar operador integral y dibujar primera iteración.
- [TRIGGER_3]: Repetir usando la misma fuente y marcar diferencias consecutivas.

#### Escena: 04

##### Nombre: Controlar el error de una iteración

##### Descripcion Breve: Cauchy-Schwarz, Doob e isometría llevan a una recurrencia integral.

##### Objetivo Pedagogico: Derivar el motor de la prueba.

##### Voz en off:

> "[TRIGGER_1] Restamos dos iteraciones consecutivas. La diferencia de derivas se controla con Cauchy-Schwarz temporal y Lipschitz. [TRIGGER_2] Para la integral estocástica usamos Doob y la isometría de Itô; Lipschitz convierte diferencias de coeficientes en diferencias de estados. [TRIGGER_3] Si D k mide el segundo momento del máximo de la diferencia, obtenemos D k de t menor o igual que una constante por la integral de D k menos uno. Esa constante solo depende de L y T."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$D_k(t)=\mathbb E\sup_{u\le t}|X^{(k+1)}_u-X^{(k)}_u|^2$`.
- MathTex: `$D_k(t)\le C_T\int_0^tD_{k-1}(s)ds,\quad C_T=2L^2(T+4)$`.
- Dos ramas de estimación: determinista con factor T y estocástica con factor 4; ambas terminan en la misma integral.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write diferencia y separar ramas usando |a+b|²≤2|a|²+2|b|².
- [TRIGGER_2]: Aplicar Cauchy-Schwarz y Doob-isometría.
- [TRIGGER_3]: Unir ramas y escribir constante admisible.

#### Escena: 05

##### Nombre: El factorial derrota al error

##### Descripcion Breve: Iterar la cota prueba Cauchy y permite pasar al límite.

##### Objetivo Pedagogico: Completar existencia.

##### Voz en off:

> "[TRIGGER_1] El crecimiento lineal da una cota finita A T para D cero en todo el intervalo. Iterar la desigualdad introduce potencias del tiempo divididas por factoriales. [TRIGGER_2] Las raíces de esas cotas forman una serie convergente. Por desigualdad triangular, las iteraciones son Cauchy en la norma del segundo momento del supremo. [TRIGGER_3] Su límite tiene una versión continua y adaptada. Lipschitz permite pasar al límite en ambas integrales, usando isometría para la estocástica. El límite satisface la EDE: existe solución."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$D_k(t)\le A_T\frac{(C_Tt)^k}{k!}$`.
- MathTex: `$\sum_{k\ge0}\sqrt{A_T(C_TT)^k/k!}<\infty$`.
- MathTex: `$X^{(k)}\to X\text{ en }S^2,\quad X=\Phi(X)$`.
- Escalera de integrales dando t,t²/2,t³/6; barras de errores; espacio S² con norma E sup |X|² y punto límite.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Iterar recurrencia y mostrar factorial.
- [TRIGGER_2]: Sumar distancias y Write Cauchy en S².
- [TRIGGER_3]: Pasar al límite en operador Φ y comprobar ecuación integral.

#### Escena: 06

##### Nombre: Gronwall impide dos respuestas al mismo ruido

##### Descripcion Breve: La diferencia de dos soluciones satisface una desigualdad cerrada.

##### Objetivo Pedagogico: Probar unicidad.

##### Voz en off:

> "[TRIGGER_1] Ahora supongamos dos soluciones con el mismo dato inicial y el mismo Browniano. Repetimos la estimación de diferencias. [TRIGGER_2] El error D de t queda acotado por la integral de sí mismo, sin término inicial. El lema determinista de Gronwall obliga a D igual a cero. [TRIGGER_3] Por tanto el supremo de la distancia es cero casi seguramente en [0,T]. Las soluciones son indistinguibles; no es una afirmación sobre trayectorias impulsadas por ruidos diferentes."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$D(t)=\mathbb E\sup_{u\le t}|X_u-Y_u|^2\le C_T\int_0^tD(s)ds$`.
- MathTex: `$D(0)=0\Rightarrow D(t)=0$`.
- MathTex: `$P(X_t=Y_t\ \forall t\le T)=1$`.
- Dos curvas bajo una sola fuente W; banda de diferencia; rótulo «Gronwall determinista».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create dos soluciones hipotéticas y fuente común.
- [TRIGGER_2]: Write desigualdad y aplicar Gronwall.
- [TRIGGER_3]: Colapsar banda a cero para todos los tiempos.

#### Escena: 07

##### Nombre: Localizar sin confundir crecimiento y Lipschitz

##### Descripcion Breve: Lipschitz local permite construir hasta salida; crecimiento controla explosión.

##### Objetivo Pedagogico: Precisar una extensión útil.

##### Voz en off:

> "[TRIGGER_1] Lipschitz local controla diferencias solo dentro de bolas. Podemos truncar coeficientes, resolver allí y pegar las soluciones hasta sus tiempos de salida. [TRIGGER_2] Para que esos tiempos tiendan a infinito necesitamos además control de tamaño, por ejemplo crecimiento lineal que produzca una cota de momentos. [TRIGGER_3] La probabilidad de salir de una bola de radio R antes de T queda acotada por una constante sobre R cuadrada. Al crecer R, desaparece. Lipschitz local por sí sola no habría descartado el ejemplo explosivo inicial."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\tau_R=\inf\{t:|X_t|\ge R\}$`.
- MathTex: `$\mathbb E\sup_{t\le T}|X_{t\wedge\tau_R}|^2\le C_T(1+\mathbb E|X_0|^2)$`.
- MathTex: `$P(\tau_R\le T)\le C_T(1+\mathbb E|X_0|^2)/R^2$`.
- Bolas de radio R=1,2,4; trayectoria detenida; cota uniforme en R; ejemplo x² fuera del cono lineal.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create solución detenida en bola.
- [TRIGGER_2]: Mostrar cota de momentos obtenida con crecimiento, Doob y Gronwall.
- [TRIGGER_3]: Aumentar R y reducir probabilidad de salida.

#### Escena: 08

##### Nombre: Existencia no certifica un algoritmo

##### Descripcion Breve: Se separa bien planteamiento de convergencia y estabilidad numérica.

##### Objetivo Pedagogico: Cerrar preparando Euler-Maruyama.

##### Voz en off:

> "[TRIGGER_1] Ya sabemos qué condiciones garantizan una solución del modelo y por qué el mismo ruido no produce dos respuestas distintas. [TRIGGER_2] Eso no prueba que cualquier paso de tiempo sea seguro ni que cualquier esquema converja. Un método explícito puede ser inestable con pasos demasiado grandes. [TRIGGER_3] Al simular tendremos tres trabajos: definir correctamente el modelo, justificar el método y medir el error. La existencia es el primer paso de esa cadena, no su final."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{modelo bien planteado}\longrightarrow\text{método consistente y estable}\longrightarrow\text{error controlado}$`.
- Tres cajas y una simulación gruesa que diverge frente a solución estable; referencia al OU con paso h excesivo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Restaurar conclusión del teorema.
- [TRIGGER_2]: Mostrar discretización gruesa sobre modelo estable con etiqueta ilustrativa.
- [TRIGGER_3]: Recorrer tres trabajos y cerrar en control de error.

