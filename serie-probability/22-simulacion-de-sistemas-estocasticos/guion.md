# Video 22: El seminario: tres variables, dos ruidos y una simulación comprobable

Proyecto final autocontenido: OU vectorial 3×2 con parámetros, algoritmo, referencias analíticas, diseño visual y código de generación de datos.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 746 palabras (5.1–6.2 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Ejemplo lineal estable con ruido aditivo. Las proyecciones representan coordenadas de R³, no una supuesta visualización literal de espacios de dimensión arbitraria. Cholesky y raíz espectral son alternativas según la matriz.

## Bibliografía y decisiones matemáticas

Proba §§5.1–5.2: matrices de covarianzas y normal multivariada; §4.2: condicionamiento. Complemento: [Goodman, modelos de difusión](https://math.nyu.edu/~goodman/teaching/StochCalc2020/week4/Week4.pdf). Las referencias de momentos del OU vectorial se derivan aquí y se calculan de forma independiente al simulador.

#### Escena: 01

##### Nombre: Tres variables, solo dos fuentes de azar

##### Descripcion Breve: Tres señales acopladas pueden compartir perturbaciones.

##### Objetivo Pedagogico: Plantear un sistema concreto y autónomo.

##### Voz en off:

> "[TRIGGER_1] Vamos a construir un sistema de tres variables que vuelven hacia un equilibrio, pero reciben dos fuentes independientes de ruido. [TRIGGER_2] Tres variables no significan necesariamente tres ruidos. Una misma perturbación puede entrar en varias ecuaciones y generar correlación. [TRIGGER_3] Al terminar tendremos un modelo, una implementación vectorial y comprobaciones contra fórmulas exactas de media y covarianza. Cada pieza de la teoría tendrá un trabajo verificable."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_t\in\mathbb R^3,\quad B_t\in\mathbb R^2$`.
- Tres depósitos abstractos conectados; dos fuentes de perturbación; ejes de tres señales; rótulo «modelo matemático, unidades adimensionales».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create tres estados y dos fuentes.
- [TRIGGER_2]: Dibujar conexiones compartidas.
- [TRIGGER_3]: Mostrar tres objetivos: simular, visualizar, comprobar.

#### Escena: 02

##### Nombre: La caja de herramientas local

##### Descripcion Breve: Se recuerdan incrementos, matriz de difusión y lectura integral.

##### Objetivo Pedagogico: Permitir seguir el seminario sin episodios anteriores.

##### Voz en off:

> "[TRIGGER_1] Una EDE expresa el estado como valor inicial más una integral de deriva y otra de ruido. En un paso h, cada fuente browniana aporta raíz de h por una normal estándar. [TRIGGER_2] La matriz G transforma esas dos perturbaciones en tres incrementos de estado. Sus filas dicen cómo recibe ruido cada variable. [TRIGGER_3] Como las fuentes son independientes, la covarianza instantánea del estado es G G transpuesta. Esta es la cuenta que debe coincidir con nuestra implementación."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX=b(X)dt+G\,dB,\quad G\in\mathbb R^{3\times2}$`.
- MathTex: `$\Delta B=\sqrt hZ,\quad Z\sim N(0,I_2)$`.
- MathTex: `$\operatorname{Cov}(G\Delta B)=hGG^\top$`.
- Matriz 3×2 y vector 2×1; seis flechas ponderadas; caja de covarianza 3×3.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write igualdad integral junto a diferencial.
- [TRIGGER_2]: Multiplicar un vector de dos normales por G.
- [TRIGGER_3]: Calcular dimensiones de covarianza y resaltar h.

#### Escena: 03

##### Nombre: Elegir un modelo completamente especificado

##### Descripcion Breve: Un OU vectorial ofrece estabilidad y solución de momentos.

##### Objetivo Pedagogico: Fijar parámetros reproducibles.

##### Voz en off:

> "[TRIGGER_1] Usaremos deriva menos A por X menos m. La matriz A es simétrica y estrictamente diagonal dominante con diagonal positiva, por lo que es definida positiva. [TRIGGER_2] Esto hace que el sistema determinista regrese al equilibrio. La difusión rectangular distribuye dos ruidos entre las tres variables. [TRIGGER_3] Fijamos también condición inicial y horizonte. Ya no queda ningún coeficiente a elegir durante la implementación."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$A=\begin{pmatrix}1&-0.2&0\\-0.2&1.5&-0.1\\0&-0.1&2\end{pmatrix}$`.
- MathTex: `$G=\begin{pmatrix}0.4&0\\0.15&0.3\\0&0.25\end{pmatrix}$`.
- MathTex: `$m=(1,-0.5,0.25)^\top,\quad x_0=(0,0,0)^\top,\quad T=4$`.
- Matriz A con términos diagonales y acoplamientos diferenciados por etiquetas; matriz G; tres puntos iniciales; panel de parámetros fijo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write A y verificar dominancia por filas.
- [TRIGGER_2]: Write G y dibujar rutas de cada ruido.
- [TRIGGER_3]: Añadir m,x0,T y mantenerlos visibles.

#### Escena: 04

##### Nombre: Correlación de fuentes y factorización

##### Descripcion Breve: Cholesky es una opción para ruidos correlacionados, no un paso obligatorio duplicado.

##### Objetivo Pedagogico: Definir una extensión general segura.

##### Voz en off:

> "[TRIGGER_1] Nuestro ejemplo usa dos fuentes independientes. Si otro modelo pide covarianza R entre fuentes, podemos generar un normal estándar y multiplicarlo por un factor L con L L transpuesta igual a R. [TRIGGER_2] Cholesky funciona cuando R es definida positiva. Si es semidefinida positiva y singular, usamos una raíz espectral y comprobamos autovalores. [TRIGGER_3] La difusión efectiva pasa a G L. No debemos correlacionar las muestras y luego aplicar L una segunda vez: eso cambia la covarianza."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$R=LL^\top,\quad\Delta W=\sqrt h\,LZ$`.
- MathTex: `$G_{\rm efectiva}=GL,\quad a=GRG^\top$`.
- MathTex: `$R=U\Lambda U^\top,\quad L=U\sqrt\Lambda\quad(\Lambda\ge0)$`.
- R de ejemplo [[1,0.6],[0.6,1]] en panel separado; rutas independiente y correlacionada; caso singular ρ=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create R y factor Cholesky.
- [TRIGGER_2]: Llevar ρ a 1 y cambiar a raíz espectral.
- [TRIGGER_3]: Marcar difusión efectiva y volver al ejemplo principal R=I2.

#### Escena: 05

##### Nombre: Euler vectorial sin bucles sobre trayectorias

##### Descripcion Breve: Se actualiza una matriz de M estados simultáneamente.

##### Objetivo Pedagogico: Traducir dimensiones a código NumPy.

##### Voz en off:

> "[TRIGGER_1] Guardamos M trayectorias como filas de una matriz de tamaño M por tres. Generamos un bloque de M por dos normales en cada paso. [TRIGGER_2] La deriva por filas se calcula como menos X menos m, multiplicado por A transpuesta. El ruido es raíz de h por Z multiplicado por G transpuesta. [TRIGGER_3] Sumamos ambos incrementos al estado. La transposición no es un detalle cosmético: permite que las dimensiones y la covarianza coincidan con la formulación de columnas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_{\rm nuevo}=X-h(X-m)A^\top+\sqrt h\,ZG^\top$`.
- MathTex: `$X\in\mathbb R^{M\times3},\quad Z\in\mathbb R^{M\times2}$`.
- Ventana con actualización NumPy; bloques dimensionales M×3,M×2; resaltar broadcasting de m; M=6000,semilla=2201.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create matrices de estados y normales.
- [TRIGGER_2]: Mostrar multiplicaciones con dimensiones anotadas.
- [TRIGGER_3]: Resaltar línea de actualización y avanzar tres pasos.

#### Escena: 06

##### Nombre: La media exacta detecta errores de deriva

##### Descripcion Breve: El valor esperado obedece una ecuación lineal.

##### Objetivo Pedagogico: Construir la primera referencia analítica.

##### Voz en off:

> "[TRIGGER_1] La integral de ruido tiene media cero. Por eso la media satisface una EDO con la misma deriva lineal. [TRIGGER_2] Su solución usa la exponencial matricial: m más e elevado a menos A t multiplicado por x cero menos m. [TRIGGER_3] Compararemos esa curva con la media de la simulación y con la media discreta exacta de Euler. Así separaremos sesgo de discretización y fluctuación por muestreo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mu(t)=m+e^{-At}(x_0-m)$`.
- MathTex: `$\mu_{k+1}^{h}=m+(I-hA)(\mu_k^h-m)$`.
- Tres curvas analíticas μi(t), medias empíricas y bandas ±2 errores estándar; media discreta con trazo distinto.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Tomar esperanza en EDE y Write EDO.
- [TRIGGER_2]: Resolver con expm y dibujar referencia.
- [TRIGGER_3]: Añadir media discreta y empírica identificadas por etiquetas.

#### Escena: 07

##### Nombre: La covarianza verifica el ruido compartido

##### Descripcion Breve: Una ecuación de Lyapunov da la segunda referencia.

##### Objetivo Pedagogico: Comprobar matrices y correlaciones, no solo medias.

##### Voz en off:

> "[TRIGGER_1] Con condición inicial determinista, la covarianza comienza en cero. Su derivada es menos A C menos C A transpuesta más G G transpuesta. [TRIGGER_2] Como A es estable, la covarianza estacionaria resuelve A C infinito más C infinito A transpuesta igual a G G transpuesta. La covarianza temporal se obtiene restando una versión propagada de C infinito. [TRIGGER_3] Euler tiene otra recurrencia exacta para su covarianza. Si la muestra no coincide con esta dentro de incertidumbre razonable, el error puede estar en el código y no en la discretización."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$C'(t)=-AC-CA^\top+GG^\top,\quad C(0)=0$`.
- MathTex: `$AC_\infty+C_\infty A^\top=GG^\top,\quad C(t)=C_\infty-e^{-At}C_\infty e^{-A^\top t}$`.
- MathTex: `$C_{k+1}^h=(I-hA)C_k^h(I-hA)^\top+hGG^\top$`.
- Heatmaps 3×3 de covarianza continua, discreta y empírica con escala compartida; entradas fuera de diagonal visibles.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Derivar ecuación usando Itô para XiXj.
- [TRIGGER_2]: Write solución estacionaria y temporal.
- [TRIGGER_3]: Mostrar recurrencia discreta y comparar las tres matrices.

#### Escena: 08

##### Nombre: Visualizar tres dimensiones sin esconder información

##### Descripcion Breve: Proyecciones coordinadas muestran dinámica conjunta.

##### Objetivo Pedagogico: Diseñar una animación implementable.

##### Voz en off:

> "[TRIGGER_1] Mostraremos tres señales temporales y una nube en el plano X uno contra X dos. Una segunda proyección X dos contra X tres evitará depender de una sola vista. [TRIGGER_2] Las nubes usan el mismo instante y las mismas muestras; los cursores temporales están sincronizados. [TRIGGER_3] Añadimos el equilibrio y las elipses gaussianas de nivel construidas con la covarianza teórica proyectada. Las llamamos elipses de Mahalanobis, sin inventar un porcentaje de cobertura."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$(x-\mu_{12})^\top C_{12}^{-1}(x-\mu_{12})=4\quad(t>0)$`.
- En esta escena usar pantalla completa: tres trazas de altura 1.0 en x∈[−6.2,−0.3], centros y=2,0.6,−0.8; proyección 12 en RIGHT*3.2+UP*1.2 y 23 en RIGHT*3.2+DOWN*1.5; 32 trayectorias y 500 puntos como máximo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create trazas con escalas fijas.
- [TRIGGER_2]: Animar cursor y actualizar ambas nubes con índices idénticos.
- [TRIGGER_3]: Añadir medias y elipses; si t=0, mostrar punto inicial en lugar de invertir covarianza nula.

#### Escena: 09

##### Nombre: Cambiar la malla y contar dos errores

##### Descripcion Breve: Las fórmulas discretas permiten medir sesgo sin Monte Carlo.

##### Objetivo Pedagogico: Definir un experimento de convergencia reproducible.

##### Voz en off:

> "[TRIGGER_1] Ejecutaremos pasos uno sobre dieciséis, treinta y dos, sesenta y cuatro y ciento veintiocho. Calcularemos la discrepancia exacta de medias y covarianzas discretas respecto de las continuas. [TRIGGER_2] Al mismo tiempo compararemos la muestra con los momentos discretos, usando errores estándar para las medias. Aumentar M reduce error Monte Carlo, pero no arregla un paso grande. [TRIGGER_3] Si quisiéramos error fuerte entre resoluciones, habría que compartir incrementos. Dos ejecuciones con ruidos independientes no sirven para esa medida; este experimento principal valida estadísticas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$h\in\{1/16,1/32,1/64,1/128\}$`.
- MathTex: `$e_\mu(h)=\|\mu_N^h-\mu(T)\|_2,\quad e_C(h)=\|C_N^h-C(T)\|_F$`.
- MathTex: `$\operatorname{SE}(\widehat\mu_i)=\sqrt{\widehat C_{ii}/M}$`.
- Tabla h,error_media,error_cov,error_muestreo; gráfica log-log de sesgos deterministas; banda Monte Carlo separada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write lista de pasos y ejecutar recurrencias analíticas.
- [TRIGGER_2]: Añadir estimaciones empíricas y errores estándar.
- [TRIGGER_3]: Mostrar dos controles distintos h y M; rotular experimento débil/momentos.

#### Escena: 10

##### Nombre: Del modelo al resultado verificable

##### Descripcion Breve: Se integran teoría, código y evidencias del seminario.

##### Objetivo Pedagogico: Cerrar la serie de manera autónoma.

##### Voz en off:

> "[TRIGGER_1] Partimos de tres estados y dos fuentes, fijamos la deriva y la difusión, y comprobamos dimensiones antes de simular. [TRIGGER_2] Los promedios y covarianzas exactos nos dieron una referencia independiente. El código incluido guarda los datos que necesita la animación y reporta sus errores sin resultados prefabricados. [TRIGGER_3] Las convergencias, la información y el cálculo de Itô dejaron de ser capítulos aislados: ahora explican qué simula el programa, qué puede concluir y cómo comprobarlo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{modelo}\to\text{método}\to\text{datos}\to\text{verificación}\to\text{visualización}$`.
- Diagrama de cinco etapas; archivo de datos indicado como datos-seminario.npz; ventana de métricas reales al ejecutar; matrices A,G al costado.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Recorrer modelo y dimensiones.
- [TRIGGER_2]: Mostrar salidas del apéndice y referencias analíticas.
- [TRIGGER_3]: Cerrar diagrama completo junto a una proyección y su covarianza verificada.

## Apéndice de producción: simulador vectorial y referencias analíticas

Código autocontenido para Python con NumPy. La ejecución principal usa los parámetros exactos de las escenas. Guarda únicamente al ejecutarse un archivo de datos en el directorio de trabajo, con medias, covarianzas, trayectorias de muestra y nubes sincronizadas para Manim. Las simulaciones de distintas mallas validan estadísticas; no se usan para estimar error fuerte entre sí.

La ecuación de Lyapunov continua y la recurrencia discreta se calculan de forma independiente de las muestras. Las discrepancias entre ambas son sesgo de discretización; las discrepancias entre muestra y recurrencia discreta son fluctuación Monte Carlo o un posible error de implementación.

```python
import numpy as np

A = np.array([[1.0, -0.2, 0.0],
              [-0.2, 1.5, -0.1],
              [0.0, -0.1, 2.0]])
G = np.array([[0.4, 0.0],
              [0.15, 0.3],
              [0.0, 0.25]])
LEVEL = np.array([1.0, -0.5, 0.25])
X0 = np.zeros(3)
T = 4.0

def covariance_factor(R, tol=1e-12):
    R = np.asarray(R, dtype=float)
    if R.ndim != 2 or R.shape[0] != R.shape[1]:
        raise ValueError("La matriz debe ser cuadrada.")
    if not np.allclose(R, R.T, atol=tol, rtol=0):
        raise ValueError("La matriz debe ser simétrica.")
    values, vectors = np.linalg.eigh(R)
    if values.min() < -tol:
        raise ValueError("La matriz no es semidefinida positiva.")
    if values.min() > tol:
        return np.linalg.cholesky(R)
    # Solo se recortan autovalores negativos dentro de tolerancia de redondeo.
    return vectors @ np.diag(np.sqrt(np.maximum(values, 0.0)))

def continuous_moments(t):
    # Este cálculo espectral aprovecha que nuestra A es simétrica definida positiva.
    # No se debe reutilizar sin cambios para una matriz A general no simétrica.
    values, vectors = np.linalg.eigh(A)
    if not np.allclose(A, A.T) or np.any(values <= 0):
        raise ValueError("Esta referencia requiere A simétrica definida positiva.")
    Q = G @ G.T
    Q_basis = vectors.T @ Q @ vectors
    C_basis = Q_basis / (values[:, None] + values[None, :])
    Cinf = vectors @ C_basis @ vectors.T
    E = (vectors * np.exp(-values*t)) @ vectors.T
    mean = LEVEL + E @ (X0 - LEVEL)
    cov = Cinf - E @ Cinf @ E.T
    return mean, 0.5*(cov + cov.T)

def discrete_moments(h, N):
    F = np.eye(3) - h*A
    mean, cov = X0.copy(), np.zeros((3, 3))
    Q = h*(G @ G.T)
    for _ in range(N):
        mean = LEVEL + F @ (mean - LEVEL)
        cov = F @ cov @ F.T + Q
    return mean, 0.5*(cov + cov.T)

def simulate(h=1/128, M=6000, seed=2201, save_frames=65):
    if h <= 0 or M < 2 or save_frames < 2:
        raise ValueError("Se requieren h>0, M>=2 y al menos dos cuadros.")
    N = int(round(T/h))
    if not np.isclose(N*h, T, atol=1e-12, rtol=0):
        raise ValueError("h debe dividir T.")
    F = np.eye(3) - h*A
    if np.max(np.abs(np.linalg.eigvals(F))) >= 1:
        raise ValueError("Paso fuera del régimen estable de Euler.")
    rng = np.random.default_rng(seed)
    X = np.repeat(X0[None, :], M, axis=0)
    indices = np.unique(np.linspace(0, N, min(save_frames, N+1), dtype=int))
    wanted = set(indices.tolist())
    times, means, covs, paths, clouds = [], [], [], [], []

    def record(k):
        times.append(k*h)
        means.append(X.mean(axis=0))
        covs.append(np.cov(X, rowvar=False, ddof=1))
        paths.append(X[:min(M, 32)].copy())
        clouds.append(X[:min(M, 500)].copy())

    record(0)
    for k in range(1, N+1):
        Z = rng.standard_normal((M, 2))
        X += -h*((X - LEVEL) @ A.T) + np.sqrt(h)*(Z @ G.T)
        if k in wanted:
            record(k)

    empirical_mean = X.mean(axis=0)
    empirical_cov = np.cov(X, rowvar=False, ddof=1)
    mu_c, C_c = continuous_moments(T)
    mu_h, C_h = discrete_moments(h, N)
    se = np.sqrt(np.diag(empirical_cov)/M)
    report = dict(
        h=h, M=M, seed=seed,
        mean_bias=float(np.linalg.norm(mu_h-mu_c)),
        cov_bias=float(np.linalg.norm(C_h-C_c, ord="fro")),
        mean_sampling_error=float(np.linalg.norm(empirical_mean-mu_h)),
        cov_sampling_error=float(np.linalg.norm(empirical_cov-C_h, ord="fro")),
        mean_z_scores=(empirical_mean-mu_h)/se,
        empirical_mean=empirical_mean,
        exact_discrete_mean=mu_h,
        exact_continuous_mean=mu_c,
    )
    frame_times = np.asarray(times)
    reference = [continuous_moments(t) for t in frame_times]
    data = dict(
        times=frame_times, means=np.asarray(means), covs=np.asarray(covs),
        paths=np.asarray(paths), clouds=np.asarray(clouds),
        reference_means=np.array([r[0] for r in reference]),
        reference_covs=np.array([r[1] for r in reference]),
        A=A, G=G, level=LEVEL, x0=X0, h=h, M=M, seed=seed,
    )
    return report, data

if __name__ == "__main__":
    assert np.all(np.linalg.eigvalsh(A) > 0)
    R = np.array([[1.0, 0.6], [0.6, 1.0]])
    L = covariance_factor(R)
    assert np.allclose(L @ L.T, R)
    # Comprobación de la rama singular de la factorización.
    R_singular = np.ones((2, 2))
    L_singular = covariance_factor(R_singular)
    assert np.allclose(L_singular @ L_singular.T, R_singular)

    last_data = None
    for denominator in (16, 32, 64, 128):
        report, last_data = simulate(h=1/denominator)
        print(report)
    np.savez_compressed("datos-seminario.npz", **last_data)

```

Contrato de datos para Manim: `times` tiene longitud F; `paths` tiene forma `(F, min(M,32), 3)` y `clouds` forma `(F,min(M,500),3)`. Cada cuadro usa el mismo índice temporal en todas las vistas. `reference_covs[f]` es la covarianza continua; su submatriz con índices `[0,1]` o `[1,2]` determina la elipse proyectada. Para dibujar el nivel de Mahalanobis 2, diagonalizar esa submatriz y usar semiejes `2*sqrt(autovalores)` con orientación de sus autovectores. En t=0 dibujar solo el punto inicial. Mantener escalas comunes durante toda la animación y comprobar puntos fuera de cuadro antes del render.

Comprobaciones antes de producir: las 3 medias empíricas deben fluctuar alrededor de las medias discretas, con errores del orden de los SE reportados; ningún único resultado aleatorio constituye un criterio determinista de aceptación. La cota de estabilidad del paso se comprueba con el radio espectral de I−hA. Los errores analíticos de media y covarianza deben decrecer al refinar; el error de muestreo no tiene por qué decrecer monótonamente. El archivo de datos no contiene una simulación de trayectorias exactas: las referencias exactas corresponden a sus momentos.
