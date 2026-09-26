# Video 11: Por qué sobrevive una campana: prueba del teorema central del límite

El episodio recorre la demostración por funciones características y controla el resto de Taylor con segundo momento finito.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 579 palabras (4–4.8 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- iid, media μ, 0<σ²<∞. Lévy se enuncia como teorema base; la expansión se justifica. No se promete una demostración de Berry-Esseen.

## Bibliografía y decisiones matemáticas

Proba §§3.5–3.6, proposición 3.6 y teorema 3.13, pp. impresas 87–91. Probita §5.4: dominada. Se corrigen las hipótesis degeneradas y se evita exigir momentos inexistentes.

#### Escena: 01

##### Nombre: La campana no está escondida en cada dato

##### Descripcion Breve: Distribuciones iniciales distintas producen sumas estandarizadas parecidas.

##### Objetivo Pedagogico: Plantear el TLC sin universalizarlo.

##### Voz en off:

> "[TRIGGER_1] Sumemos dados, tiempos exponenciales o variables de dos valores. Después de centrar y escalar, sus histogramas empiezan a parecerse. [TRIGGER_2] No estamos diciendo que cualquier suma se vuelva normal ni que un número mágico de observaciones lo garantice. [TRIGGER_3] Demostraremos una versión precisa: variables independientes con la misma ley y varianza finita positiva. La campana surgirá de un cálculo, no de su parecido en pantalla."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Z_n=\frac{\sum_{j=1}^nX_j-n\mu}{\sigma\sqrt n}$`.
- Tres histogramas de 20000 sumas, semilla 1101; n=1,2,8,32; binning común tras estandarizar; curva normal fija.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create distribuciones iniciales.
- [TRIGGER_2]: Transform histogramas para n creciente, rotulados como simulaciones.
- [TRIGGER_3]: Write hipótesis iid y 0<σ²<∞.

#### Escena: 02

##### Nombre: La escala correcta

##### Descripcion Breve: La suma se centra y se divide por su desviación estándar.

##### Objetivo Pedagogico: Justificar raíz de n.

##### Voz en off:

> "[TRIGGER_1] La suma tiene media n por μ y varianza n por σ cuadrada. Restamos la primera y dividimos entre la raíz de la segunda. [TRIGGER_2] Así Z n siempre tiene media cero y varianza uno. Sin esta escala, la suma se ensancha o la media colapsa a un punto. [TRIGGER_3] La ley de grandes números describe ese colapso de la media. El teorema central mira con una lupa de raíz de n las fluctuaciones que quedan."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y_j=(X_j-\mu)/\sigma,\quad\mathbb EY_j=0,\quad\mathbb EY_j^2=1$`.
- MathTex: `$Z_n=n^{-1/2}\sum_{j=1}^nY_j$`.
- MathTex: `$\operatorname{Var}(\overline X_n)=\sigma^2/n$`.
- Media muestral estrechándose y zoom de factor √n; ejes rotulados antes/después; cálculo de varianza.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write media y varianza de la suma.
- [TRIGGER_2]: Transform coordenadas a Z_n.
- [TRIGGER_3]: Mostrar simultáneamente colapso y zoom de fluctuaciones.

#### Escena: 03

##### Nombre: Transformar el problema

##### Descripcion Breve: La independencia convierte la firma de la suma en una potencia.

##### Objetivo Pedagogico: Reducir el TLC a un límite de funciones.

##### Voz en off:

> "[TRIGGER_1] Usamos la función característica, el promedio de exponencial de i t por la variable. Su módulo siempre está acotado por uno. [TRIGGER_2] Independencia transforma la suma en producto, y la igualdad de distribuciones convierte ese producto en una potencia. [TRIGGER_3] Solo necesitamos conocer la firma de una variable estandarizada cerca del origen. El argumento t sobre raíz de n se acerca precisamente allí."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_Y(u)=\mathbb E e^{iuY}$`.
- MathTex: `$\varphi_{Z_n}(t)=\left[\varphi_Y(t/\sqrt n)\right]^n$`.
- Círculo de fases breve para recordar la definición; n factores; lupa sobre u=0.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create círculo y definición.
- [TRIGGER_2]: Transform suma de variables a producto de firmas.
- [TRIGGER_3]: Acercar u al origen mientras n crece.

#### Escena: 04

##### Nombre: El resto de Taylor bajo control

##### Descripcion Breve: Segundo momento finito basta para una expansión de segundo orden.

##### Objetivo Pedagogico: Evitar exigir tercer momento.

##### Voz en off:

> "[TRIGGER_1] Para cada número real z, la exponencial compleja es uno más i z menos z cuadrada sobre dos, más un resto pequeño respecto de z cuadrada. [TRIGGER_2] Ese resto dividido por z cuadrada tiende a cero y está acotado globalmente por una constante. Al sustituir z por uY, podemos dominar el cociente por una constante por Y cuadrada. [TRIGGER_3] Convergencia dominada y segundo momento finito permiten promediar el resto. No necesitamos un tercer momento."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$r(z)=e^{iz}-1-iz+z^2/2,\quad r(z)/z^2\to0$`.
- MathTex: `$|r(z)|\le C z^2,\quad\left|\frac{r(uY)}{u^2}\right|\le CY^2$`.
- MathTex: `$\mathbb E r(uY)=o(u^2)$`.
- Curva del módulo |r(z)|/z² con valor extendido 0 en origen; techo C; tarjeta EY²=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write Taylor y separar resto.
- [TRIGGER_2]: Mostrar cota local y global del cociente; rotular existencia de C.
- [TRIGGER_3]: Aplicar dominada y Write o(u²).

#### Escena: 05

##### Nombre: Sobrevive la varianza

##### Descripcion Breve: La media cancela el término lineal.

##### Objetivo Pedagogico: Obtener la firma límite.

##### Voz en off:

> "[TRIGGER_1] Al tomar esperanza, el término lineal desaparece porque la media es cero y el cuadrático queda como menos u cuadrada sobre dos porque la varianza es uno. [TRIGGER_2] Evaluamos en t sobre raíz de n y elevamos a n. La corrección es menos t cuadrada sobre dos n más un término menor que uno sobre n. [TRIGGER_3] El límite de estas potencias es exponencial de menos t cuadrada sobre dos. Esta es exactamente la firma de una normal estándar."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_Y(u)=1-u^2/2+o(u^2)$`.
- MathTex: `$\left[1-\frac{t^2}{2n}+o(1/n)\right]^n\to e^{-t^2/2}$`.
- Tres términos de Taylor en tarjetas; t fijo; potencia y exponencial; anotar log(1+z)=z+o(z) cerca de 0 para justificar el límite complejo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Cancelar término lineal y sustituir EY²=1.
- [TRIGGER_2]: Transform u a t/√n.
- [TRIGGER_3]: Aplicar logaritmo local, multiplicar por n y exponentiar para obtener el límite.

#### Escena: 06

##### Nombre: Volver de firmas a leyes

##### Descripcion Breve: Lévy concluye convergencia en distribución.

##### Objetivo Pedagogico: Precisar lo que el teorema entrega.

##### Voz en off:

> "[TRIGGER_1] La función límite es continua en cero y pertenece a una distribución normal. El teorema de continuidad de Lévy convierte la convergencia de firmas en convergencia de leyes. [TRIGGER_2] Hemos probado el teorema central para cada distribución que satisface nuestras hipótesis. No hemos probado convergencia de trayectorias ni igualdad exacta para n finito. [TRIGGER_3] Tampoco prometimos que una suma discreta tenga densidad. Sus acumuladas se acercan a la acumulada normal, que es continua en todos los puntos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Z_n\Rightarrow Z,\quad Z\sim N(0,1)$`.
- MathTex: `$\lim_nP(Z_n\le x)=\Phi(x)\quad\forall x\in\mathbb R$`.
- CDF discreta escalonada y Φ; firma límite arriba; tarjeta «Lévy: teorema usado».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write continuidad en cero.
- [TRIGGER_2]: Transform firma al enunciado de TLC.
- [TRIGGER_3]: Superponer CDF discreta y normal manteniendo los escalones visibles.

#### Escena: 07

##### Nombre: Cuándo falla la campana

##### Descripcion Breve: Cauchy e igualdad perfecta muestran dos hipótesis necesarias.

##### Objetivo Pedagogico: Conocer los límites del resultado.

##### Voz en off:

> "[TRIGGER_1] Con variables Cauchy independientes, la media sigue teniendo ley Cauchy: la varianza finita faltaba. [TRIGGER_2] Si todas las variables son la misma X, no tenemos independencia y sumar solo multiplica una variable; la estandarización propuesta no produce el mecanismo anterior. [TRIGGER_3] Incluso cuando el teorema aplica, la velocidad depende de la distribución. Si existe tercer momento absoluto, Berry-Esseen proporciona una cota cuantitativa adicional, pero no forma parte de nuestra prueba."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\varphi_{\overline X_n}(t)=\left[e^{-|t|/n}\right]^n=e^{-|t|}\quad(X_j\text{ Cauchy iid})$`.
- MathTex: `$\sup_x|P(Z_n\le x)-\Phi(x)|\le\frac{C\,\mathbb E|X_1-\mu|^3}{\sigma^3\sqrt n}$`.
- Histograma Cauchy que no se estrecha; flechas de dependencia desde una sola X; tarjeta Berry-Esseen «teorema adicional».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write cálculo Cauchy.
- [TRIGGER_2]: Mostrar suma de copias idénticas nX.
- [TRIGGER_3]: Añadir cota con tercera potencia e indicar hipótesis extra.

#### Escena: 08

##### Nombre: Una aproximación concreta

##### Descripcion Breve: Se aplica TLC a una suma de dados con corrección de continuidad.

##### Objetivo Pedagogico: Cerrar con cálculo y alcance.

##### Voz en off:

> "[TRIGGER_1] Para cien dados justos, la suma tiene media trescientos cincuenta y varianza cien por treinta y cinco sobre doce. [TRIGGER_2] Para estimar la probabilidad de estar entre trescientos treinta y trescientos setenta, usamos límites trescientos veintinueve punto cinco y trescientos setenta punto cinco como corrección de continuidad. [TRIGGER_3] La probabilidad aproximada es una diferencia de acumuladas normales. La cuenta responde al experimento; la prueba explica por qué la estrategia mejora asintóticamente bajo las hipótesis indicadas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mu=3.5,\quad\sigma^2=35/12,\quad n=100$`.
- MathTex: `$P(330\le S_{100}\le370)\approx\Phi\left(\frac{20.5}{\sqrt{100(35/12)}}\right)-\Phi\left(\frac{-20.5}{\sqrt{100(35/12)}}\right)$`.
- Campana sobre suma de dados; área entre 329.5 y 370.5; expresión exacta de la aproximación, sin inventar un porcentaje; opcional evaluar scipy.stats.norm.cdf durante implementación.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create eje de sumas y parámetros.
- [TRIGGER_2]: Marcar límites enteros y desplazar bordes 0.5.
- [TRIGGER_3]: Sombrear área y dejar fórmula calculable junto al enunciado probado.

