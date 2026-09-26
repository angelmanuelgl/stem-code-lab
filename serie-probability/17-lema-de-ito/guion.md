# Video 17: El término que la regla de cadena no podía ver

La fórmula de Itô se deriva desde Taylor y variación cuadrática, con estructura de prueba, localización y tres aplicaciones calculadas.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 573 palabras (4–4.8 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Funciones C1,2 y procesos de Itô; la escena de restos explica el argumento estándar bajo localización. No usar Taylor formal como sustituto del control del error.

## Bibliografía y decisiones matemáticas

Proba: convergencia L² y dominada. Complementos: [Goodman, semana 4, §2](https://math.nyu.edu/~goodman/teaching/StochCalc2020/week4/Week4.pdf); [Lawler §§3.3–3.4](https://www.math.uchicago.edu/~lawler/finbook.pdf).

#### Escena: 01

##### Nombre: La regla de cadena pierde un tiempo

##### Descripcion Breve: Comparar W² con una integral ingenua produce una contradicción de esperanzas.

##### Objetivo Pedagogico: Motivar el término correctivo.

##### Voz en off:

> "[TRIGGER_1] Si aplicáramos la regla de cadena ordinaria a W cuadrada, escribiríamos que su cambio es dos W por dW. [TRIGGER_2] Pero la integral de ese término tiene esperanza cero, mientras W T cuadrada tiene esperanza T. Falta algo. [TRIGGER_3] No es un error de redondeo. Los cuadrados de los incrementos acumulan un tiempo completo, y vamos a seguirlos hasta encontrar la regla correcta."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[W_T^2]=T,\quad\mathbb E\left[2\int_0^TW_s\,dW_s\right]=0$`.
- Balanza de esperanzas 0 y T; fórmula ingenua tachada; trayectoria browniana T=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write regla ingenua con interrogación.
- [TRIGGER_2]: Mostrar diferencia de esperanzas.
- [TRIGGER_3]: Añadir casilla «corrección» junto al diferencial.

#### Escena: 02

##### Nombre: Taylor conserva dos órdenes

##### Descripcion Breve: Una expansión local distingue términos que sobreviven al sumar.

##### Objetivo Pedagogico: Explicar la intuición del cálculo.

##### Voz en off:

> "[TRIGGER_1] En un paso pequeño, Taylor aporta un término lineal en el incremento y otro cuadrático. Para una curva suave, este último desaparece al sumar y refinar. [TRIGGER_2] En Browniano, el incremento tiene escala raíz de h. Su cuadrado tiene escala h, justo la que acumula un tiempo finito. [TRIGGER_3] Esa cuenta de escalas guía la fórmula, pero la prueba necesita controlar los restos y los límites de las sumas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$f(x+\Delta x)-f(x)=f'(x)\Delta x+\frac12f''(x)(\Delta x)^2+r$`.
- MathTex: `$\Delta W\text{ tiene escala }\sqrt h,\quad(\Delta W)^2\text{ escala }h$`.
- Bloques Taylor lineal/cuadrático/resto; tabla de escalas; rótulo «motivación, aún no prueba».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write expansión.
- [TRIGGER_2]: Cambiar escala Δx de h a √h.
- [TRIGGER_3]: Mantener cuadrático y apartar resto para su control posterior.

#### Escena: 03

##### Nombre: La fórmula para Browniano

##### Descripcion Breve: Se presenta la versión temporal con derivadas correctas.

##### Objetivo Pedagogico: Enunciar Itô con regularidad.

##### Voz en off:

> "[TRIGGER_1] Para una función f con una derivada continua en tiempo y dos en espacio, el cambio de f de t,W t tiene tres contribuciones. [TRIGGER_2] La derivada temporal se integra contra dt; la espacial contra dW; y la mitad de la segunda derivada espacial también contra dt. [TRIGGER_3] La fórmula se entiende como una igualdad de integrales. Si los integrandos no son globalmente cuadrado integrables, se interpreta mediante localización."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$df(t,W_t)=\left(f_t+\frac12f_{xx}\right)(t,W_t)\,dt+f_x(t,W_t)\,dW_t$`.
- MathTex: `$f\in C^{1,2}$`.
- Superficie f(t,x) esquemática; recorrido (t,Wt); tres cajas de términos; símbolo integral visible debajo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create recorrido en superficie.
- [TRIGGER_2]: Write tres términos uno por uno.
- [TRIGGER_3]: Mostrar versión integrada de 0 a T y etiqueta C1,2.

#### Escena: 04

##### Nombre: Dónde queda el resto

##### Descripcion Breve: Se controla Taylor primero en una región compacta.

##### Objetivo Pedagogico: Dar la estructura rigurosa de prueba.

##### Voz en off:

> "[TRIGGER_1] Detenemos la trayectoria al salir de una región compacta. Allí las derivadas son uniformemente continuas y podemos acotar el resto espacial por un módulo de continuidad multiplicado por el incremento cuadrado. [TRIGGER_2] El máximo incremento tiende a cero y la suma cuadrática permanece controlada, de modo que los restos desaparecen. Las sumas lineales convergen por la construcción de Itô. [TRIGGER_3] Los cuadrados centrados, ponderados por valores del pasado, tienen varianza que tiende a cero. Finalmente ampliamos la región de parada. Es la justificación de la regla, no una manipulación literal de infinitesimales."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$|r_i|\le\omega_R(\max_j|\Delta W_j|)\,(\Delta W_i)^2,\quad\omega_R(\delta)\to0$`.
- MathTex: `$\sum_i f_{xx}(t_i,W_{t_i})[(\Delta W_i)^2-\Delta t_i]\xrightarrow P0$`.
- Caja compacta |W|≤R; bandas de continuidad de fxx; tres columnas de convergencia: lineal, cuadrática, resto; nota que restos temporales se controlan por continuidad de ft.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create tiempo de salida de caja R.
- [TRIGGER_2]: Write cota del resto y producto que tiende a cero; mostrar varianza de cuadrados centrados O(|π|) con pesos acotados.
- [TRIGGER_3]: Retirar localización aumentando R y encadenar las tres sumas límite.

#### Escena: 05

##### Nombre: Un proceso con deriva y difusión

##### Descripcion Breve: Itô incorpora μ y σ a los términos correspondientes.

##### Objetivo Pedagogico: Derivar la fórmula para una EDE escalar.

##### Voz en off:

> "[TRIGGER_1] Si X cambia por una deriva μ dt y un ruido σ dW, el término lineal usa ambos. [TRIGGER_2] Su variación cuadrática acumula σ cuadrada dt; los términos que contienen dt cuadrada o dt por dW desaparecen. [TRIGGER_3] Por eso la corrección es un medio de σ cuadrada por f xx. El cuadrado pertenece al coeficiente de ruido y no debe perderse al cambiar de variable."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX_t=\mu_tdt+\sigma_tdW_t$`.
- MathTex: `$df(t,X_t)=\left(f_t+\mu_tf_x+\frac12\sigma_t^2f_{xx}\right)dt+\sigma_tf_x\,dW_t$`.
- MathTex: `$[X]_t=\int_0^t\sigma_s^2ds$`.
- Dos flechas deriva/ruido entrando a X; tabla de productos; matriz de términos conservados.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write proceso de Itô.
- [TRIGGER_2]: Expandir (μdt+σdW)² y conservar σ²dt.
- [TRIGGER_3]: Sustituir en Taylor y encerrar corrección completa.

#### Escena: 06

##### Nombre: Dos ejemplos que verifican la regla

##### Descripcion Breve: El cuadrado y la exponencial producen identidades concretas.

##### Objetivo Pedagogico: Aplicar y comprobar términos.

##### Voz en off:

> "[TRIGGER_1] Para f de x igual a x cuadrada, recuperamos dos X por dX más su variación cuadrática. Con X igual a W, aparece el dt que faltaba. [TRIGGER_2] Para la exponencial de σW, la segunda derivada produce una deriva de un medio σ cuadrada. [TRIGGER_3] Restar ese crecimiento en el exponente construye la exponencial e elevado a σW menos un medio σ cuadrada t. En el Browniano estándar tiene esperanza uno y es martingala."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$d(W_t^2)=2W_t\,dW_t+dt$`.
- MathTex: `$d(e^{\sigma W_t})=\sigma e^{\sigma W_t}dW_t+\frac12\sigma^2e^{\sigma W_t}dt$`.
- MathTex: `$M_t=e^{\sigma W_t-\sigma^2t/2},\quad\mathbb EM_t=1$`.
- Dos tarjetas f=x² y f=e^σx; derivadas explícitas; σ=0.6, T=2; media analítica de exponencial, no solo media muestral.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Sustituir derivadas del cuadrado.
- [TRIGGER_2]: Sustituir exponencial y mostrar deriva extra.
- [TRIGGER_3]: Añadir factor e^−σ²t/2 y cancelar deriva; comprobar esperanza usando normalidad.

#### Escena: 07

##### Nombre: El logaritmo revela el ajuste

##### Descripcion Breve: Se transforma una dinámica multiplicativa positiva.

##### Objetivo Pedagogico: Anticipar solución geométrica.

##### Voz en off:

> "[TRIGGER_1] Supongamos que X es positiva y satisface dX igual a μX dt más σX dW. Para el logaritmo, las derivadas son uno sobre X y menos uno sobre X cuadrada. [TRIGGER_2] Sustituir en Itô cancela las X y deja deriva μ menos un medio σ cuadrada, junto a σ dW. [TRIGGER_3] La resta no es una penalización arbitraria. Es el efecto exacto de la curvatura del logaritmo sobre una señal con variación cuadrática."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$f'(x)=1/x,\quad f''(x)=-1/x^2$`.
- MathTex: `$d\log X_t=(\mu-\sigma^2/2)dt+\sigma\,dW_t\quad(X_t>0)$`.
- Curva log x en x>0; haz de trayectorias positivas; derivadas y cancelaciones de X; barrera x=0 marcada fuera de dominio.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create logaritmo y dominio.
- [TRIGGER_2]: Write derivadas y sustituir coeficientes.
- [TRIGGER_3]: Cancelar factores y destacar signo negativo de segunda derivada.

#### Escena: 08

##### Nombre: Una regla de cadena con memoria cuadrática

##### Descripcion Breve: Se regresa a la contradicción inicial.

##### Objetivo Pedagogico: Consolidar procedimiento de uso.

##### Voz en off:

> "[TRIGGER_1] La balanza inicial se equilibra cuando añadimos T: W T cuadrada es dos veces la integral de W más T. [TRIGGER_2] Para aplicar Itô, identifica la dinámica, calcula las derivadas, conserva la variación cuadrática y escribe la igualdad integral con sus condiciones. [TRIGGER_3] La regla ordinaria no estaba diseñada para estas trayectorias. Ahora sabemos qué término sobrevive, por qué aparece y cómo comprobarlo con un ejemplo exacto."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_T^2=2\int_0^TW_s\,dW_s+T$`.
- Balanza corregida; cuatro tarjetas dinámica/derivadas/variación/condiciones; ejemplo exacto junto a trayectoria inicial.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Restaurar balanza y añadir T.
- [TRIGGER_2]: Recorrer tarjetas con Indicate.
- [TRIGGER_3]: Cerrar sobre identidad exacta y mantener 5 s para lectura.

