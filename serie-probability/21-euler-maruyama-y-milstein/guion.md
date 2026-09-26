# Video 21: Discretizar el ruido y medir lo que perdemos

Euler-Maruyama y Milstein se comparan en GBM con ruido acoplado, referencia exacta y control explícito de error Monte Carlo.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 662 palabras (4.6–5.5 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Coeficientes autónomos para el enunciado fuerte; regularidad adicional para débil y Milstein. El código del apéndice produce datos, no resultados prefabricados.

## Bibliografía y decisiones matemáticas

Convergencias: Proba §§2.3–2.7. Referencia numérica complementaria: [Higham, An Algorithmic Introduction, SIAM Review](https://epubs.siam.org/doi/abs/10.1137/S0036144500378302). Ejemplo, momentos discretos y protocolo de comparación desarrollados aquí.

#### Escena: 01

##### Nombre: Aproximar una ecuación que no podemos resolver a mano

##### Descripcion Breve: Una integral se convierte en actualizaciones locales.

##### Objetivo Pedagogico: Motivar Euler-Maruyama.

##### Voz en off:

> "[TRIGGER_1] Tenemos una EDE con deriva b y difusión σ. Aunque no conozcamos su solución exacta, podemos intentar avanzar en intervalos pequeños. [TRIGGER_2] Congelamos ambos coeficientes al inicio del paso: la deriva aporta b por h y el ruido aporta σ por el incremento browniano. [TRIGGER_3] Este es Euler-Maruyama. La regla parece sencilla; la parte delicada será comprobar qué aproxima y cómo medir su error."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$dX_t=b(X_t)dt+\sigma(X_t)dW_t$`.
- MathTex: `$Y_{k+1}=Y_k+b(Y_k)h+\sigma(Y_k)\Delta W_k$`.
- Trayectoria parcial, punto Yk y dos flechas de actualización; malla T=1; etiqueta coeficientes congelados en tk.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create punto y flecha de deriva.
- [TRIGGER_2]: Añadir flecha aleatoria desde el extremo de deriva.
- [TRIGGER_3]: Write esquema y repetir cuatro pasos.

#### Escena: 02

##### Nombre: El ruido tiene escala raíz del paso

##### Descripcion Breve: Generar incrementos correctos preserva la varianza acumulada.

##### Objetivo Pedagogico: Evitar el error hZ.

##### Voz en off:

> "[TRIGGER_1] Un incremento browniano de duración h es normal centrado con varianza h. Por eso generamos raíz de h por una normal estándar. [TRIGGER_2] Si multiplicáramos por h, la varianza total de N pasos sería T por h y desaparecería al refinar. Estaríamos cambiando el modelo. [TRIGGER_3] Usamos normales independientes entre intervalos y registramos la semilla. La reproducibilidad facilita comparar algoritmos, pero no reemplaza el análisis de error."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Delta W_k=\sqrt h\,Z_k,\quad Z_k\overset{\rm iid}\sim N(0,1)$`.
- MathTex: `$N\operatorname{Var}(\sqrt hZ)=T,\quad N\operatorname{Var}(hZ)=Th$`.
- Dos acumuladores de ruido, correcto e incorrecto; gráfica varianza contra h; semilla 2101.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write distribución de incremento.
- [TRIGGER_2]: Comparar sumas de varianzas para √h y h.
- [TRIGGER_3]: Mostrar semilla y generación de normales en malla.

#### Escena: 03

##### Nombre: La misma tormenta en dos resoluciones

##### Descripcion Breve: Incrementos gruesos se obtienen sumando incrementos finos.

##### Objetivo Pedagogico: Definir un acoplamiento para error fuerte.

##### Voz en off:

> "[TRIGGER_1] Para comparar dos trayectorias necesitamos que reciban la misma realización del ruido. Dos simulaciones independientes pueden quedar lejos aunque ambas sean exactas. [TRIGGER_2] Generamos una malla fina y sumamos bloques de incrementos para las mallas gruesas. Así cada resolución observa la misma tormenta. [TRIGGER_3] En el modelo geométrico conocemos la solución exacta al tiempo final usando el mismo W T. Eso nos permite medir error sin introducir otra trayectoria de referencia aproximada."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Delta W^{(h)}_k=\sum_{j=kr}^{(k+1)r-1}\Delta W^{(h/r)}_j$`.
- MathTex: `$X_T=x_0e^{(\mu-\sigma^2/2)T+\sigma W_T}$`.
- Malla fina N=1024 y agrupaciones r=2,4,8; brackets de sumas; fórmula exacta GBM con x0=1,μ=0.2,σ=0.6,T=1.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create incrementos finos una sola vez.
- [TRIGGER_2]: Agrupar sin regenerar normales.
- [TRIGGER_3]: Superponer valores finales numérico y exacto del mismo ruido.

#### Escena: 04

##### Nombre: Convergencia fuerte

##### Descripcion Breve: La raíz del error cuadrático medio mide proximidad bajo acoplamiento.

##### Objetivo Pedagogico: Distinguir orden del error y de su cuadrado.

##### Voz en off:

> "[TRIGGER_1] Definimos error fuerte terminal como la raíz de la esperanza de la diferencia al cuadrado entre solución y aproximación, usando el mismo Browniano. [TRIGGER_2] Bajo condiciones estándar de Lipschitz global y crecimiento lineal, para coeficientes autónomos, Euler-Maruyama tiene cota de orden un medio. [TRIGGER_3] Si dividimos h entre cuatro, esperamos reducir aproximadamente a la mitad ese error en régimen asintótico. El error cuadrático sin raíz tiene orden uno; no confundamos ambas pendientes."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$e_{\rm fuerte}(h)=\left(\mathbb E|X_T-Y_N|^2\right)^{1/2}\le C h^{1/2}$`.
- MathTex: `$\mathbb E|X_T-Y_N|^2=O(h)$`.
- Gráfica log-log con puntos de RMSE para h=1/16,...,1/1024; referencia √h; barras de incertidumbre por remuestreo opcional.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write definición y mostrar diferencias pareadas.
- [TRIGGER_2]: Presentar teorema con hipótesis visibles.
- [TRIGGER_3]: Dibujar pendiente 1/2 para RMSE y 1 para MSE en panel alternado.

#### Escena: 05

##### Nombre: Convergencia débil

##### Descripcion Breve: Promedios de observables pueden acercarse más rápido.

##### Objetivo Pedagogico: Precisar clase de funciones e hipótesis.

##### Voz en off:

> "[TRIGGER_1] La convergencia débil numérica compara la esperanza de una función de la solución con la de su aproximación. No exige comparar una trayectoria con otra. [TRIGGER_2] Con suficiente suavidad de coeficientes y observables y control de momentos, Euler-Maruyama alcanza orden uno. En nuestro banco de prueba geométrico usaremos f de x igual a x cuadrada. [TRIGGER_3] Este orden no vale automáticamente para cualquier función discontinua ni para cualquier coeficiente irregular. Y es una noción distinta de solución débil de una EDE."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$e_f(h)=|\mathbb E f(X_T)-\mathbb E f(Y_N)|$`.
- MathTex: `$f(x)=x^2,\quad e_f(h)=O(h)$`.
- Dos histogramas y función observable x²; medidores de expectativas; tarjeta «orden 1 bajo regularidad».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create histogramas y evaluaciones de f.
- [TRIGGER_2]: Write diferencia de expectativas.
- [TRIGGER_3]: Dibujar referencia h y señalar condiciones de regularidad.

#### Escena: 06

##### Nombre: Medir sesgo sin confundir Monte Carlo

##### Descripcion Breve: El segundo momento de Euler geométrico se calcula exactamente.

##### Objetivo Pedagogico: Separar discretización y muestreo.

##### Voz en off:

> "[TRIGGER_1] Para GBM, Euler multiplica por uno más μh más σ raíz de h por Z. La independencia permite calcular su segundo momento como una potencia. [TRIGGER_2] Así obtenemos el sesgo débil exacto de la discretización y podemos comparar la estimación Monte Carlo con él. [TRIGGER_3] El error Monte Carlo decrece como uno sobre raíz del número de trayectorias. Si su incertidumbre es mayor que el sesgo, una gráfica empírica no puede revelar fiablemente la pendiente débil."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\mathbb E Y_N^2=x_0^2[(1+\mu h)^2+\sigma^2h]^N$`.
- MathTex: `$\mathbb E X_T^2=x_0^2e^{(2\mu+\sigma^2)T}$`.
- MathTex: `$\operatorname{SE}(\overline D)=s_D/\sqrt M,\quad D=Y_N^2-X_T^2$`.
- Curva de sesgo exacto y estimaciones pareadas con barras ±2SE; M=8000; h en potencias de dos; no fijar resultados numéricos antes de ejecutar.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Derivar recurrencia de EY².
- [TRIGGER_2]: Write diferencia exacta de momentos.
- [TRIGGER_3]: Superponer estimación y bandas; señalar puntos cuyo sesgo queda cubierto por incertidumbre.

#### Escena: 07

##### Nombre: Milstein retiene un término más

##### Descripcion Breve: Una corrección usa la derivada de la difusión.

##### Objetivo Pedagogico: Comparar un método escalar de orden fuerte uno.

##### Voz en off:

> "[TRIGGER_1] La expansión estocástica sugiere conservar una corrección que Euler omite: medio σ por σ prima, multiplicado por incremento browniano cuadrado menos h. [TRIGGER_2] En una EDE escalar con regularidad suficiente, Milstein alcanza orden fuerte uno. Para GBM, σ de x es sigma por x y la corrección se calcula directamente. [TRIGGER_3] En varias dimensiones pueden aparecer integrales iteradas y áreas de Lévy. No trasladaremos esta fórmula escalar como si resolviera automáticamente todos los sistemas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y_{k+1}=Y_k+b(Y_k)h+\sigma(Y_k)\Delta W_k+\frac12\sigma(Y_k)\sigma'(Y_k)[(\Delta W_k)^2-h]$`.
- MathTex: `$\text{GBM: corrección }=\frac12\sigma^2Y_k[(\Delta W_k)^2-h]$`.
- Euler y Milstein sobre mismo ruido; panel de corrección centrada; gráfica RMSE con referencias h^1/2 y h.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write corrección y mostrar su esperanza cero.
- [TRIGGER_2]: Sustituir difusión geométrica.
- [TRIGGER_3]: Comparar errores pareados y marcar restricción escalar.

#### Escena: 08

##### Nombre: Un paso grande puede romper una dinámica estable

##### Descripcion Breve: OU permite calcular estabilidad y sesgo de varianza de Euler.

##### Objetivo Pedagogico: Advertir con un ejemplo matemático concreto.

##### Voz en off:

> "[TRIGGER_1] En OU centrado, Euler multiplica el estado anterior por uno menos θh. Para conservar estabilidad de segundo momento necesitamos valor absoluto de ese factor menor que uno. [TRIGGER_2] Cuando cero es menor que θh y θh menor que dos, su varianza estacionaria es σ cuadrada dividida entre dos θ menos θ cuadrada h. [TRIGGER_3] Esa varianza supera la exacta salvo en el límite. Un modelo bien planteado no convierte cualquier malla en una aproximación buena; el paso también altera estadísticas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$Y_{k+1}=(1-\theta h)Y_k+\sigma\sqrt hZ_k$`.
- MathTex: `$0<\theta h<2,\quad V_h=\frac{\sigma^2}{2\theta-\theta^2h}$`.
- MathTex: `$V_{\rm exacta}=\sigma^2/(2\theta)$`.
- Slider θh de 0.1 a 2.2; coeficiente autorregresivo; curva de varianza y umbral de estabilidad.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write recurrencia OU.
- [TRIGGER_2]: Resolver V=a²V+σ²h.
- [TRIGGER_3]: Mover slider cerca y fuera del umbral; rotular inestabilidad numérica.

#### Escena: 09

##### Nombre: Un experimento que otro puede repetir

##### Descripcion Breve: Se describe el código incluido y sus salidas.

##### Objetivo Pedagogico: Cerrar con un protocolo verificable.

##### Voz en off:

> "[TRIGGER_1] El código de este guion genera un único banco de incrementos finos, construye mallas anidadas y compara Euler y Milstein contra GBM exacto. [TRIGGER_2] Reporta RMSE, sesgo débil analítico y estimación pareada con error estándar. Cada tabla lleva semilla, número de trayectorias y paso. [TRIGGER_3] La prueba respalda los órdenes bajo hipótesis; el experimento comprueba nuestra implementación y muestra cuándo entramos en el régimen asintótico. Conservar ambas cosas evita convertir una línea bonita en una garantía."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{mismo ruido}+\text{referencia exacta}+\text{incertidumbre reportada}$`.
- Ventana de código del apéndice; tabla de columnas h,rmse_em,rmse_milstein,weak_exact,weak_mc,se; diagramas de datos hacia gráficas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mostrar constantes y generación de incrementos del código.
- [TRIGGER_2]: Resaltar columnas y asociarlas a definiciones.
- [TRIGGER_3]: Cerrar con protocolo de reproducción y limitaciones del ajuste de pendientes.

## Apéndice de producción: experimento reproducible

Este código genera la tabla de las escenas 4–7 y 9. Requiere Python y NumPy. Se puede copiar a un archivo de trabajo y ejecutarlo; no depende de Manim. Las gráficas se construyen con los valores devueltos, sin introducir pendientes o resultados a mano. Memoria principal: M × N_fine números de doble precisión. Con los valores por defecto, el banco ocupa aproximadamente 66 MB.

El error fuerte se mide contra la solución exacta del mismo Browniano. Para el sesgo débil se reporta tanto el valor analítico como una diferencia pareada. Las barras ±2SE son orientativas; no son un intervalo exacto de cobertura garantizada.

```python
import numpy as np

def experimento(M=8000, N_fine=1024, seed=2101):
    if M < 2 or N_fine < 16 or N_fine & (N_fine - 1):
        raise ValueError("M >= 2 y N_fine potencia de dos >= 16.")
    T, x0, mu, sigma = 1.0, 1.0, 0.2, 0.6
    rng = np.random.default_rng(seed)
    dW = np.sqrt(T / N_fine) * rng.standard_normal((M, N_fine))
    WT = dW.sum(axis=1)
    exact = x0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * WT)
    exact_second = x0**2 * np.exp((2 * mu + sigma**2) * T)
    rows = []

    for N in [2**k for k in range(4, int(np.log2(N_fine)) + 1)]:
        h = T / N
        stride = N_fine // N
        increments = dW.reshape(M, N, stride).sum(axis=2)
        em = np.full(M, x0)
        mil = np.full(M, x0)
        for k in range(N):
            z = increments[:, k]
            em *= 1 + mu * h + sigma * z
            mil *= 1 + mu * h + sigma * z + 0.5 * sigma**2 * (z*z - h)

        diff_weak = em**2 - exact**2
        em_second = x0**2 * ((1 + mu*h)**2 + sigma**2*h)**N
        rows.append({
            "h": h,
            "rmse_em": float(np.sqrt(np.mean((em - exact)**2))),
            "rmse_milstein": float(np.sqrt(np.mean((mil - exact)**2))),
            "weak_exact": float(abs(em_second - exact_second)),
            "weak_mc_signed": float(np.mean(diff_weak)),
            "weak_mc_se": float(np.std(diff_weak, ddof=1) / np.sqrt(M)),
        })

    metadata = dict(M=M, N_fine=N_fine, seed=seed, T=T,
                    x0=x0, mu=mu, sigma=sigma)
    return metadata, rows

if __name__ == "__main__":
    metadata, rows = experimento()
    print(metadata)
    print("h rmse_em rmse_milstein weak_exact weak_mc_signed weak_mc_se")
    for row in rows:
        print(" ".join(f"{value:.8g}" for value in row.values()))
    h = np.array([r["h"] for r in rows])
    for key in ("rmse_em", "rmse_milstein", "weak_exact"):
        error = np.array([r[key] for r in rows])
        slope = np.polyfit(np.log(h[-4:]), np.log(error[-4:]), 1)[0]
        print(f"Pendiente observada ({key}, últimas 4 mallas): {slope:.4f}")

```

Controles de implementación: el banco de incrementos se genera una sola vez; cada malla gruesa suma bloques del mismo banco; el tiempo final exacto usa la misma suma WT. No usar una realización independiente como referencia fuerte. No ajustar una pendiente al valor absoluto del sesgo Monte Carlo cuando sus barras de incertidumbre incluyen cero. Para la visualización, etiquetar las pendientes como observadas y conservar las referencias teóricas por separado.
