# Video 09: Por qué los promedios se estabilizan sin que el azar recuerde

Demostración autocontenida de la ley fuerte para variables iid de varianza finita, sin adelantar martingalas.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 592 palabras (4.1–4.9 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- La prueba maximal se incluye íntegra. Se enuncia por separado el alcance más general L1; no se atribuye su demostración al episodio.

## Bibliografía y decisiones matemáticas

Proba §2.3, ejemplo 2.4: ley débil. Probita §3.2: Borel-Cantelli. La desigualdad maximal de Kolmogorov y el argumento diádico son el complemento desarrollado aquí.

#### Escena: 01

##### Nombre: Una moneda no recuerda sus deudas

##### Descripcion Breve: Se contraponen frecuencia y compensación.

##### Objetivo Pedagogico: Evitar la falacia del jugador.

##### Voz en off:

> "[TRIGGER_1] Después de muchas caras, ¿la moneda debe producir cruces para compensar? Una moneda independiente no recuerda los resultados anteriores. [TRIGGER_2] Aun así, su frecuencia de caras se acerca a un medio. La compensación ocurre por dilución del pasado, no porque cambie la probabilidad del siguiente lanzamiento. [TRIGGER_3] Vamos a demostrar una versión de esta estabilización y a distinguir una garantía por etapas de una garantía para la historia completa."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(X_{n+1}=1\mid X_1,\ldots,X_n)=1/2$`.
- MathTex: `$\overline X_n=\frac1n\sum_{j=1}^nX_j$`.
- Fila de lanzamientos y curva de frecuencia; línea 1/2; mismo siguiente lanzamiento después de rachas distintas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create racha de caras y pregunta.
- [TRIGGER_2]: Write probabilidad condicional invariable.
- [TRIGGER_3]: Create frecuencia y mostrar cómo una racha fija pesa menos al crecer n.

#### Escena: 02

##### Nombre: El contrato de la prueba

##### Descripcion Breve: Se centran variables iid de varianza finita.

##### Objetivo Pedagogico: Declarar el alcance exacto.

##### Voz en off:

> "[TRIGGER_1] Trabajaremos con variables independientes e idénticamente distribuidas, media μ y varianza finita σ cuadrada. [TRIGGER_2] Restamos la media y llamamos S n a la suma de las variables centradas. Su media es cero y su varianza es n por σ cuadrada. [TRIGGER_3] Probaremos que S n sobre n converge a cero casi seguramente. La ley fuerte general solo necesita integrabilidad en el caso iid, pero nuestra prueba usa explícitamente segundo momento."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y_j=X_j-\mu,\quad S_n=\sum_{j=1}^nY_j$`.
- MathTex: `$\mathbb ES_n=0,\quad\mathbb ES_n^2=n\sigma^2$`.
- MathTex: `$S_n/n\to0\text{ c.s.}$`.
- Tarjetas independencia/idéntica ley/varianza finita; sumas centradas como barras con signos; objetivo visible.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write hipótesis.
- [TRIGGER_2]: Transform Xj en Yj y sumar varianzas sin términos cruzados.
- [TRIGGER_3]: Write objetivo y aclaración de alcance en pie.

#### Escena: 03

##### Nombre: La ley débil sale de Chebyshev

##### Descripcion Breve: Una cota 1/n controla un instante.

##### Objetivo Pedagogico: Demostrar convergencia en probabilidad.

##### Voz en off:

> "[TRIGGER_1] Chebyshev aplicado a la media da una probabilidad de error no mayor que σ cuadrada sobre n por épsilon cuadrada. [TRIGGER_2] Para cada tolerancia fija, esa cota tiende a cero. Hemos probado la ley débil. [TRIGGER_3] Pero sumar uno sobre n diverge. No podemos aplicar directamente el primer Borel-Cantelli a todos los instantes. La ley fuerte necesita controlar más que una fotografía."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(|S_n/n|>\varepsilon)\le\frac{\sigma^2}{n\varepsilon^2}$`.
- MathTex: `$\overline X_n\xrightarrow P\mu$`.
- MathTex: `$\sum_{n\ge1}\frac1n=\infty$`.
- Curva 1/n; contador n; tarjetas ley débil y obstáculo de sumabilidad.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write Chebyshev y reducir cota.
- [TRIGGER_2]: Encerrar conclusión en probabilidad.
- [TRIGGER_3]: Mostrar serie armónica y detener flecha directa hacia Borel-Cantelli.

#### Escena: 04

##### Nombre: Una cota para el máximo

##### Descripcion Breve: El primer cruce divide el evento en casos disjuntos.

##### Objetivo Pedagogico: Probar la desigualdad maximal de Kolmogorov.

##### Voz en off:

> "[TRIGGER_1] Sea A k el evento de que el primer cruce de nivel λ en valor absoluto sucede en k. Esos eventos son disjuntos y solo dependen del pasado hasta k. [TRIGGER_2] En A k, escribimos S n como S k más el resto futuro. Por independencia y media cero, el término cruzado tiene esperanza cero; el cuadrado del resto aporta una cantidad no negativa. [TRIGGER_3] Entonces la esperanza de S n cuadrado sobre A k es al menos λ cuadrada por su probabilidad. Sumamos en k y obtenemos la cota para el máximo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$A_k=\{|S_j|<\lambda\ (j<k),\ |S_k|\ge\lambda\}$`.
- MathTex: `$\mathbb E[S_n^2\mathbf1_{A_k}]\ge\mathbb E[S_k^2\mathbf1_{A_k}]\ge\lambda^2P(A_k)$`.
- MathTex: `$P(\max_{k\le n}|S_k|\ge\lambda)\le n\sigma^2/\lambda^2$`.
- Trayectoria discreta, barreras ±λ, primer cruce destacado; separación gráfica pasado/futuro; expansión del cuadrado en panel derecho.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barreras y Ak disjuntos.
- [TRIGGER_2]: Write expansión y cancelar término cruzado usando independencia, no por una cancelación visual arbitraria.
- [TRIGGER_3]: Sumar sobre k y reemplazar ES_n² por nσ².

#### Escena: 05

##### Nombre: Mirar en escalas dobles

##### Descripcion Breve: Los máximos hasta 2^r tienen cotas sumables.

##### Objetivo Pedagogico: Aplicar Borel-Cantelli.

##### Voz en off:

> "[TRIGGER_1] Ahora miramos todos los pasos hasta dos elevado a r, con umbral épsilon por dos elevado a r. [TRIGGER_2] La desigualdad maximal acota la probabilidad por una constante multiplicada por dos elevado a menos r. Esta serie sí converge. [TRIGGER_3] Borel-Cantelli implica que esos máximos normalizados acaban siendo pequeños casi seguramente. Aplicando el argumento a tolerancias uno sobre m, el máximo dividido entre dos elevado a r tiende a cero."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P\left(\max_{k\le2^r}|S_k|\ge\varepsilon2^r\right)\le\frac{\sigma^2}{\varepsilon^2\,2^r}$`.
- MathTex: `$\sum_r2^{-r}<\infty$`.
- MathTex: `$\frac{\max_{k\le2^r}|S_k|}{2^r}\to0\quad\text{c.s.}$`.
- Ventanas de longitud 2,4,8,16; barras geométricas de probabilidades; tolerancias numerables 1/m.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create ventanas y umbrales.
- [TRIGGER_2]: Write cota sumable y cola geométrica.
- [TRIGGER_3]: Mostrar Borel-Cantelli y unión numerable de excepciones nulas.

#### Escena: 06

##### Nombre: Rellenar los huecos

##### Descripcion Breve: Un máximo diádico controla todos los índices intermedios.

##### Objetivo Pedagogico: Completar la demostración fuerte.

##### Voz en off:

> "[TRIGGER_1] Para cualquier n entre dos elevado a r menos uno y dos elevado a r, su suma está acotada por el máximo de esa ventana. [TRIGGER_2] Además n es al menos la mitad del extremo derecho. El cociente queda acotado por dos veces el máximo normalizado. [TRIGGER_3] Ese máximo tiende a cero casi seguramente, así que también S n sobre n. Ya controlamos todos los índices y la media converge a μ casi seguramente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$2^{r-1}<n\le2^r$`.
- MathTex: `$\frac{|S_n|}{n}\le2\,\frac{\max_{k\le2^r}|S_k|}{2^r}\to0$`.
- MathTex: `$\overline X_n\to\mu\quad\text{c.s.}$`.
- Número n móvil dentro de una ventana diádica; desigualdad en dos pasos; sello «prueba completa bajo varianza finita».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mover n dentro de la ventana.
- [TRIGGER_2]: Write cota y resaltar factor 2.
- [TRIGGER_3]: Transform al límite de la media y encerrar c.s.

#### Escena: 07

##### Nombre: Lo que un casino sí puede afirmar

##### Descripcion Breve: Una ventaja positiva se convierte en promedio, no en invulnerabilidad.

##### Objetivo Pedagogico: Aplicar sin promesas falsas.

##### Voz en off:

> "[TRIGGER_1] Si las ganancias por jugada cumplen estas hipótesis y tienen media positiva, la ganancia media converge a esa ventaja. [TRIGGER_2] Eso no significa ganar cada partida ni evitar una racha de pérdidas. Tampoco elimina el riesgo de quedarse sin capital antes del horizonte asintótico. [TRIGGER_3] La ley explica estabilización de promedios en el modelo. Si hay dependencia, cambios de reglas o colas sin el momento requerido, hay que revisar la prueba y sus hipótesis."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb EX_1=\mu>0\Rightarrow \frac1n\sum_{j=1}^nX_j\to\mu\quad\text{c.s.}$`.
- Ganancia acumulada con pérdidas iniciales y media de largo plazo; línea de capital cero; etiquetas de hipótesis.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create trayectoria de ganancias ilustrativa.
- [TRIGGER_2]: Marcar pérdidas tempranas y posible cruce de capital.
- [TRIGGER_3]: Volver a tarjetas de hipótesis y la conclusión exacta.

#### Escena: 08

##### Nombre: Fotografías frente a una historia

##### Descripcion Breve: Se comparan ley débil y fuerte sobre el mismo experimento.

##### Objetivo Pedagogico: Resolver el gancho de la moneda.

##### Voz en off:

> "[TRIGGER_1] La ley débil dice que una media tomada muy tarde tiene pequeña probabilidad de error grande. La fuerte dice que casi toda historia termina respetando cada tolerancia para siempre. [TRIGGER_2] Nuestra prueba pasó de una cota de instante a una cota de máximos, después a una serie sumable y finalmente a todos los tiempos. [TRIGGER_3] La moneda nunca necesitó recordar sus deudas. Las fluctuaciones pierden peso frente al número de observaciones y ahora sabemos en qué sentido lo hacen."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{Chebyshev}\to\text{máximos}\to\text{Borel-Cantelli}\to\text{ley fuerte}$`.
- Dos paneles de frecuencia: corte fijo y trayectoria; cadena de demostración con cuatro nodos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mostrar corte fijo y su probabilidad.
- [TRIGGER_2]: Resaltar trayectoria y recorrer los cuatro nodos de prueba.
- [TRIGGER_3]: Cerrar con siguiente lanzamiento de probabilidad 1/2 independiente de la racha.

