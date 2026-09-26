# Video 16: Cómo integrar una curva que no tiene derivada

Construcción de la integral de Itô desde procesos elementales hasta integrandos predecibles de energía finita, con isometría y ejemplo exacto.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 554 palabras (3.8–4.6 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Browniano respecto de una filtración usual. Espacio H² predecible; integrandos continuos adaptados incluidos. Densidad, Doob y completitud son teoremas identificados.

## Bibliografía y decisiones matemáticas

Proba §§2.3,2.8 y §4.2: L² y condicionamiento. Consulta: [Lawler §§3.1–3.2](https://www.math.uchicago.edu/~lawler/finbook.pdf). Se desarrolla la derivación elemental y la extensión por isometría en el guion.

#### Escena: 01

##### Nombre: La posición del punto cambia el resultado

##### Descripcion Breve: Dos sumas con el mismo integrando browniano difieren.

##### Objetivo Pedagogico: Motivar una nueva definición de integral.

##### Voz en off:

> "[TRIGGER_1] Queremos integrar W respecto de sus propios cambios. Si multiplicamos cada incremento por el valor anterior, obtenemos una suma. Si usamos el posterior, obtenemos otra. [TRIGGER_2] La diferencia entre ambas es exactamente la suma de los incrementos al cuadrado, que converge al tiempo transcurrido. [TRIGGER_3] En una curva suave esa diferencia desaparecería. Aquí la convención de muestreo forma parte del objeto que estamos definiendo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$L_\pi=\sum_iW_{t_i}\Delta W_i,\quad R_\pi=\sum_iW_{t_{i+1}}\Delta W_i$`.
- MathTex: `$R_\pi-L_\pi=\sum_i(\Delta W_i)^2\to T$`.
- Trayectoria T=1,N=1024, semilla 1601; mallas anidadas; marcadores izquierdos/derechos y dos contadores de suma.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create malla y suma izquierda.
- [TRIGGER_2]: Duplicar para suma derecha con mismos incrementos.
- [TRIGGER_3]: Restar término a término y Write límite T.

#### Escena: 02

##### Nombre: No mirar antes de decidir

##### Descripcion Breve: Un proceso elemental usa valores conocidos al inicio del intervalo.

##### Objetivo Pedagogico: Definir integrandos causales.

##### Voz en off:

> "[TRIGGER_1] Tomamos una malla y elegimos un coeficiente H i usando solo la información disponible en t i. Lo mantenemos durante el intervalo siguiente. [TRIGGER_2] La integral de ese proceso elemental es la suma de coeficiente por incremento browniano. [TRIGGER_3] Pedimos segundo momento finito para los coeficientes. La posición temporal importa: H i puede depender del pasado, pero no del incremento futuro que va a multiplicar."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$H_s=\sum_iH_i\mathbf1_{(t_i,t_{i+1}]}(s),\quad H_i\in L^2(\mathcal F_{t_i})$`.
- MathTex: `$I_T(H)=\sum_iH_i(W_{t_{i+1}}-W_{t_i})$`.
- Escalones H con marcadores al inicio; Browniano debajo; flechas del pasado al coeficiente, cortina en futuro.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create coeficientes y sus intervalos.
- [TRIGGER_2]: Write suma integral elemental.
- [TRIGGER_3]: Mostrar intento H_i=ΔW_i como anticipación no permitida en esta definición.

#### Escena: 03

##### Nombre: La esperanza es cero

##### Descripcion Breve: Condicionar en el inicio elimina cada ganancia futura.

##### Objetivo Pedagogico: Mostrar propiedad de martingala para integrandos simples.

##### Voz en off:

> "[TRIGGER_1] Dado el pasado, H i ya está decidido y el incremento browniano tiene media cero. Por eso el producto tiene esperanza condicional cero. [TRIGGER_2] Los incrementos de la integral mantienen esta propiedad. La integral acumulada es una martingala cuadrado integrable. [TRIGGER_3] No significa que cada trayectoria gane cero. Significa que el promedio futuro, dada la información presente, coincide con el valor actual."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[H_i\Delta W_i\mid\mathcal F_{t_i}]=H_i\,\mathbb E[\Delta W_i\mid\mathcal F_{t_i}]=0$`.
- MathTex: `$\mathbb E[I_t(H)\mid\mathcal F_s]=I_s(H),\quad s\le t$`.
- Árbol de futuros desde ti; coeficiente fijo en cada nodo; ganancias positivas y negativas; suma acumulada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write esperanza condicional y sacar Hi.
- [TRIGGER_2]: Cancelar media del incremento.
- [TRIGGER_3]: Create varios futuros y centro de masa en valor actual de la integral.

#### Escena: 04

##### Nombre: La isometría de Itô

##### Descripcion Breve: Los términos cruzados desaparecen y las varianzas se acumulan.

##### Objetivo Pedagogico: Demostrar identidad L2 para simples.

##### Voz en off:

> "[TRIGGER_1] Elevamos la suma al cuadrado. Para dos intervalos distintos, condicionamos en el inicio del posterior: todo lo anterior es conocido y el incremento nuevo tiene media cero. [TRIGGER_2] Los términos cruzados desaparecen. En los diagonales, la independencia del incremento da esperanza H i cuadrada por duración del intervalo. [TRIGGER_3] La suma es la integral temporal del segundo momento de H. Esta identidad convierte aproximar integrandos en aproximar integrales."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E[I_T(H)^2]=\sum_i\mathbb E[H_i^2]\,\Delta t_i$`.
- MathTex: `$\mathbb E\left|\int_0^T H_s\,dW_s\right|^2=\mathbb E\int_0^T|H_s|^2\,ds$`.
- Matriz de productos i,j; diagonal retenida y cruzados atenuados; barras de energía de Hi.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Expandir cuadrado en matriz.
- [TRIGGER_2]: Cancelar cruzados mediante condicionamiento y escribir diagonales.
- [TRIGGER_3]: Transform suma diagonal a integral temporal.

#### Escena: 05

##### Nombre: Completar el espacio

##### Descripcion Breve: La isometría garantiza un límite independiente de la aproximación.

##### Objetivo Pedagogico: Construir la integral general.

##### Voz en off:

> "[TRIGGER_1] Trabajamos con integrandos predecibles cuya energía esperada en [0,T] es finita. Los procesos elementales son densos en ese espacio bajo la norma de energía. [TRIGGER_2] Elegimos una aproximación elemental H n. La isometría hace que sus integrales sean Cauchy en L dos, así que tienen un límite. [TRIGGER_3] Dos aproximaciones del mismo H producen el mismo límite porque la diferencia de sus energías tiende a cero. Esa es la definición de integral de Itô."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\|H\|_{\mathcal H^2}^2=\mathbb E\int_0^T|H_s|^2ds<\infty$`.
- MathTex: `$\|I_T(H^{(n)})-I_T(H^{(m)})\|_2=\|H^{(n)}-H^{(m)}\|_{\mathcal H^2}$`.
- MathTex: `$I_T(H)=L^2\!-\!\lim_n I_T(H^{(n)})$`.
- Dos secuencias de escalones convergiendo al mismo H; dos secuencias de integrales al mismo punto; tarjeta «densidad de elementales: teorema».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write espacio predecible y energía.
- [TRIGGER_2]: Conectar distancia entre integrandos a distancia entre integrales.
- [TRIGGER_3]: Unir ambos límites y encerrar independencia de aproximación.

#### Escena: 06

##### Nombre: De valores terminales a proceso continuo

##### Descripcion Breve: Doob controla toda la trayectoria de aproximación.

##### Objetivo Pedagogico: Precisar regularidad e integrandos admisibles.

##### Voz en off:

> "[TRIGGER_1] La definición anterior da un valor terminal. Para construir todos los tiempos a la vez, aplicamos Doob a la diferencia de dos integrales elementales. [TRIGGER_2] El error esperado del supremo queda acotado por cuatro veces la energía de la diferencia. Así obtenemos una versión continua de la integral y preservamos su propiedad de martingala. [TRIGGER_3] Un proceso continuo adaptado es predecible. Decir solamente adaptado, sin medibilidad temporal ni integrabilidad, no alcanza para esta construcción."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E\sup_{t\le T}|I_t(H^{(n)})-I_t(H^{(m)})|^2\le4\|H^{(n)}-H^{(m)}\|_{\mathcal H^2}^2$`.
- Dos procesos integrales y banda de error uniforme; tarjetas continuidad/adaptación/predictibilidad/energía.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create diferencias en todos los tiempos.
- [TRIGGER_2]: Write Doob e isometría encadenadas.
- [TRIGGER_3]: Mostrar versión continua y condiciones admisibles; rotular versión como resultado de completitud.

#### Escena: 07

##### Nombre: Calcular la integral de W

##### Descripcion Breve: La identidad del cuadrado da un resultado exacto.

##### Objetivo Pedagogico: Vincular definición y variación cuadrática.

##### Voz en off:

> "[TRIGGER_1] El Browniano cumple la condición de energía: la integral de E W s cuadrada entre cero y T vale T cuadrada sobre dos. [TRIGGER_2] La identidad telescópica del cuadrado dice que dos veces la suma izquierda es W T cuadrada menos la suma cuadrática. [TRIGGER_3] Al tomar límites obtenemos un medio de W T cuadrada menos T. Su esperanza es cero, como exige la construcción; omitir T produciría una contradicción."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E\int_0^TW_s^2ds=T^2/2$`.
- MathTex: `$2\sum_iW_{t_i}\Delta W_i=W_T^2-\sum_i(\Delta W_i)^2$`.
- MathTex: `$\int_0^TW_s\,dW_s=\frac12(W_T^2-T)$`.
- Cuadrado algebraico; contador de suma izquierda del gancho; valor exacto calculado de la misma trayectoria.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write energía finita.
- [TRIGGER_2]: Telescopar incrementos del cuadrado.
- [TRIGGER_3]: Sustituir Qπ→T y comprobar esperanza cero.

#### Escena: 08

##### Nombre: Itô y Stratonovich

##### Descripcion Breve: Promediar extremos modifica la integral mediante covariación.

##### Objetivo Pedagogico: Cerrar sin confundir convenciones.

##### Voz en off:

> "[TRIGGER_1] Para este ejemplo, promediar los valores de W en ambos extremos hace que la suma sea exactamente un medio de W T cuadrada. [TRIGGER_2] Ese es el resultado de Stratonovich. En condiciones de semimartingala, la relación general añade a Itô la mitad de la covariación del integrando con W. [TRIGGER_3] Ambas convenciones pueden ser útiles, pero corresponden a definiciones diferentes. El método de Itô conserva la decisión basada en el pasado y nos proporciona una isometría para construirla."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\sum_i\frac{W_{t_i}+W_{t_{i+1}}}{2}\Delta W_i=\frac12W_T^2$`.
- MathTex: `$\int H\circ dW=\int H\,dW+\frac12[H,W]_T$`.
- Tres contadores izquierda/derecha/promedio de extremos; resultados (W²−T)/2,(W²+T)/2,W²/2; no identificar sin condiciones el promedio de extremos con evaluar en el punto medio temporal.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create tercer contador con promedio de extremos.
- [TRIGGER_2]: Write corrección de covariación y su hipótesis semimartingala.
- [TRIGGER_3]: Concluir comparación de resultados con las mismas muestras.

