# Video 19: Resolver una ecuación impulsada por ruido

Definición integral y nociones de solución, seguidas de derivación, verificación y momentos de GBM y Ornstein-Uhlenbeck.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 548 palabras (3.8–4.6 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Coeficientes constantes en ejemplos; x0 determinista; θ>0 en OU y x0>0 en GBM. Se distingue solución fuerte/débil de aproximación numérica.

## Bibliografía y decisiones matemáticas

Proba §4.2 y §5.2: condicionamiento y gaussianas. Consulta: [Goodman, semana 4](https://math.nyu.edu/~goodman/teaching/StochCalc2020/week4/Week4.pdf). Cálculos exactos y comprobaciones se desarrollan en cada escena.

#### Escena: 01

##### Nombre: Una ecuación con ruido no es una derivada ordinaria

##### Descripcion Breve: Una dinámica combina tendencia y fluctuación.

##### Objetivo Pedagogico: Definir el problema que se quiere resolver.

##### Voz en off:

> "[TRIGGER_1] Queremos describir una cantidad que sigue una tendencia pero recibe perturbaciones continuas. Escribimos una deriva b y una intensidad de ruido σ. [TRIGGER_2] La notación diferencial es compacta, pero el Browniano no tiene derivada ordinaria. La ecuación significa una igualdad entre un valor inicial y dos integrales. [TRIGGER_3] Resolverla es encontrar un proceso que satisfaga esa igualdad, con adaptación e integrabilidad adecuadas, no simplemente dibujar una curva irregular."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX_t=b(t,X_t)dt+\sigma(t,X_t)dW_t$`.
- MathTex: `$X_t=X_0+\int_0^tb(s,X_s)ds+\int_0^t\sigma(s,X_s)dW_s$`.
- Caja de estado X con entradas deriva y ruido; forma integral debajo; trayectoria y filtración.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create entradas y ecuación diferencial.
- [TRIGGER_2]: TransformMatchingTex a forma integral.
- [TRIGGER_3]: Resaltar adaptación e integrabilidad en tarjetas.

#### Escena: 02

##### Nombre: Fuerte y débil hablan del espacio probabilístico

##### Descripcion Breve: Se fija o se construye el ruido junto con la solución.

##### Objetivo Pedagogico: Separar dos nociones de solución.

##### Voz en off:

> "[TRIGGER_1] En una solución fuerte, el espacio probabilístico, la información y el Browniano ya están dados. Buscamos X usando ese ruido y los datos iniciales. [TRIGGER_2] En una solución débil, podemos construir también el espacio, la filtración y el Browniano como parte de la solución. [TRIGGER_3] Ninguna de estas palabras describe todavía el error de un método numérico. También hay que distinguir unicidad de trayectorias, usando el mismo ruido, y unicidad en ley."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{fuerte: }(\Omega,\mathcal F,(\mathcal F_t),P,W,X_0)\text{ dados}$`.
- MathTex: `$\text{débil: construir }(\Omega,\mathcal F,(\mathcal F_t),P,W,X)$`.
- Dos diagramas: caja fija con W→X y caja conjunta (W,X); cartel «distinto de error numérico».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create caja fuerte y ruido fijo.
- [TRIGGER_2]: Create caja débil que incluye el espacio.
- [TRIGGER_3]: Mostrar dos tarjetas de unicidad: indistinguibilidad / igualdad de leyes.

#### Escena: 03

##### Nombre: Crecimiento proporcional

##### Descripcion Breve: La ecuación geométrica modela fluctuaciones relativas.

##### Objetivo Pedagogico: Plantear GBM con hipótesis.

##### Voz en off:

> "[TRIGGER_1] Si el cambio relativo tiene deriva μ y ruido σ, la ecuación es μX dt más σX dW, con X cero inicial positivo. [TRIGGER_2] Para descubrir una solución, probamos transformar con logaritmo mientras X permanezca positiva. Itô introduce una resta de medio σ cuadrada. [TRIGGER_3] Integrar la ecuación del logaritmo sugiere una exponencial. Después verificaremos esa candidata directamente; así la positividad quedará garantizada por la fórmula."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX_t=\mu X_tdt+\sigma X_tdW_t,\quad X_0=x_0>0$`.
- MathTex: `$d\log X_t=(\mu-\sigma^2/2)dt+\sigma dW_t$`.
- Trayectorias de crecimiento relativo; curva log; μ=0.2,σ=0.6,x0=1 para ilustración.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write dinámica multiplicativa.
- [TRIGGER_2]: Aplicar derivadas del logaritmo en dominio positivo.
- [TRIGGER_3]: Integrar y mostrar candidata exponencial.

#### Escena: 04

##### Nombre: Verificar y distinguir media de mediana

##### Descripcion Breve: La exponencial satisface exactamente la EDE.

##### Objetivo Pedagogico: Comprobar solución y consecuencias.

##### Voz en off:

> "[TRIGGER_1] La candidata es x cero por exponencial de μ menos medio σ cuadrada, por t, más σW t. Aplicamos Itô a esa función de t y W. [TRIGGER_2] El término temporal y la corrección cuadrática se combinan para recuperar μX; el término de ruido es σX. La solución es positiva para todo tiempo. [TRIGGER_3] Su media es x cero e elevado a μt, pero su mediana tiene el ajuste negativo. Un promedio puede crecer aunque una trayectoria típica medida por la mediana decrezca."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_t=x_0e^{(\mu-\sigma^2/2)t+\sigma W_t}$`.
- MathTex: `$\mathbb EX_t=x_0e^{\mu t},\quad\operatorname{med}(X_t)=x_0e^{(\mu-\sigma^2/2)t}$`.
- MathTex: `$\operatorname{Var}(X_t)=x_0^2e^{2\mu t}(e^{\sigma^2t}-1)$`.
- Derivadas ft,fx,fxx de la candidata; haz de 128 trayectorias; líneas analíticas media y mediana; caso μ=0.1,σ=0.6.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write candidata y derivadas.
- [TRIGGER_2]: Sustituir en Itô y cancelar ajuste.
- [TRIGGER_3]: Dibujar media/mediana y distinguirlas de trayectorias individuales.

#### Escena: 05

##### Nombre: Un sistema que regresa a un nivel

##### Descripcion Breve: Ornstein-Uhlenbeck combina restauración y ruido aditivo.

##### Objetivo Pedagogico: Plantear un contraste con crecimiento geométrico.

##### Voz en off:

> "[TRIGGER_1] Pensemos ahora en una señal que tiende a regresar al nivel m. Si está arriba, la deriva la empuja abajo; si está abajo, la empuja arriba. [TRIGGER_2] Con intensidad θ positiva y ruido aditivo σ, obtenemos Ornstein-Uhlenbeck. [TRIGGER_3] A diferencia del modelo geométrico, puede cruzar cero y fluctuar alrededor de m. La naturaleza del coeficiente de ruido cambia tanto la dinámica como las soluciones posibles."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX_t=\theta(m-X_t)dt+\sigma dW_t,\quad\theta>0$`.
- Eje vertical X, nivel m; flechas restauradoras; θ=1.2,m=0.5,σ=0.4,x0=1.5.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create nivel y flechas.
- [TRIGGER_2]: Write ecuación y trayectorias.
- [TRIGGER_3]: Mostrar cruce del cero como permitido, sin truncar datos.

#### Escena: 06

##### Nombre: El factor integrante

##### Descripcion Breve: Una transformación temporal resuelve OU.

##### Objetivo Pedagogico: Derivar y verificar solución exacta.

##### Voz en off:

> "[TRIGGER_1] Restamos m y multiplicamos por e elevado a θt. La regla de producto cancela la deriva restauradora. [TRIGGER_2] Integramos el ruido transformado y despejamos X. Obtenemos un término inicial que decae y una integral con memoria exponencial. [TRIGGER_3] El kernel da mayor peso a perturbaciones recientes. Cada perturbación pasada sigue presente, pero su efecto disminuye exponencialmente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$d[e^{\theta t}(X_t-m)]=\sigma e^{\theta t}dW_t$`.
- MathTex: `$X_t=m+(x_0-m)e^{-\theta t}+\sigma\int_0^te^{-\theta(t-s)}dW_s$`.
- Kernel e^−θ(t−s) sobre s∈[0,t]; impulsos pasados con pesos; cálculo de producto sin covariación con factor determinista.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write cambio de variable.
- [TRIGGER_2]: Expandir producto y cancelar θ.
- [TRIGGER_3]: Integrar, despejar y animar pesos del kernel.

#### Escena: 07

##### Nombre: Distribución y transición exactas

##### Descripcion Breve: La integral con integrando determinista es gaussiana.

##### Objetivo Pedagogico: Obtener parámetros para validar simulaciones.

##### Voz en off:

> "[TRIGGER_1] La integral de OU es gaussiana porque se aproxima por combinaciones lineales de incrementos gaussianos. Su media es cero y la isometría da su varianza. [TRIGGER_2] Partiendo de x cero determinista, la media se acerca a m y la varianza a σ cuadrada sobre dos θ. [TRIGGER_3] En un paso h, conocemos una transición exacta con un ruido normal nuevo. Si iniciamos en la distribución límite independiente de incrementos futuros, el proceso es estacionario."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb EX_t=m+(x_0-m)e^{-\theta t}$`.
- MathTex: `$\operatorname{Var}(X_t)=\frac{\sigma^2}{2\theta}(1-e^{-2\theta t})$`.
- MathTex: `$X_{t+h}=m+(X_t-m)e^{-\theta h}+\sigma\sqrt{\frac{1-e^{-2\theta h}}{2\theta}}Z,\quad Z\sim N(0,1)$`.
- Curvas analíticas de media/varianza; densidad gaussiana que se estabiliza; Z independiente de Ft explícito.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Calcular integral de σ²e^−2θ(t−s).
- [TRIGGER_2]: Animar parámetros hacia límite.
- [TRIGGER_3]: Write transición exacta y condición de independencia.

#### Escena: 08

##### Nombre: Qué significa haber resuelto el modelo

##### Descripcion Breve: Dos fórmulas exactas sirven como bancos de prueba.

##### Objetivo Pedagogico: Cerrar con solución y validación.

##### Voz en off:

> "[TRIGGER_1] En el modelo geométrico encontramos una exponencial que responde al mismo Browniano. En OU encontramos una memoria lineal del ruido. [TRIGGER_2] Verificamos ecuaciones, valores iniciales, dominios y momentos. Estas comprobaciones convierten las fórmulas en referencias para métodos numéricos. [TRIGGER_3] Cuando no exista una solución explícita, seguiremos necesitando saber si existe una solución única. Y al simular, deberemos decidir si queremos aproximar trayectorias o estadísticas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{GBM: positiva y multiplicativa}\qquad\text{OU: gaussiana y restauradora}$`.
- Tabla visual de dos columnas: fórmula, media, varianza, dominio; preguntas existencia/unicidad/aproximación.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Restaurar ambas soluciones.
- [TRIGGER_2]: Indicate verificaciones y momentos.
- [TRIGGER_3]: Cerrar con las tres preguntas para el siguiente problema.

