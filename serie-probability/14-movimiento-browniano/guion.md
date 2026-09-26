# Video 14: Construir una curva continua hecha de azar

De caminatas reescaladas a un proceso gaussiano continuo: propiedades, construcción diádica, Donsker, autosimilitud y simulación.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 575 palabras (4–4.8 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- Los teoremas de construcción, Donsker y no diferenciabilidad se enuncian con su alcance. Se demuestran las propiedades algebraicas y se dan parámetros completos de simulación.

## Bibliografía y decisiones matemáticas

Proba §§1.3,3.5–3.6: vectores, gaussianas y TLC. Complementos de consulta: [MIT, Stochastic Processes II](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/3b97c6b0c282dd9dc024c4c7ffe3fba8_MIT18_S096F13_lecnote17.pdf); [Lawler, capítulo 2](https://www.math.uchicago.edu/~lawler/finbook.pdf).

#### Escena: 01

##### Nombre: Una caminata vista desde lejos

##### Descripcion Breve: Pasos aleatorios se refinan y reescalan.

##### Objetivo Pedagogico: Motivar el Browniano como límite de leyes de caminos.

##### Voz en off:

> "[TRIGGER_1] Un caminante da pasos independientes a derecha o izquierda. Si hacemos más pasos en el mismo tiempo, el recorrido crece. [TRIGGER_2] Reducimos el tamaño de cada paso a uno sobre raíz del número de pasos. Así la varianza acumulada en una unidad de tiempo permanece en uno. [TRIGGER_3] La curva se vuelve más fina sin hacerse lisa. Estamos buscando un objeto continuo que conserve esa escala de fluctuación."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W^{(n)}(t)=n^{-1/2}S_{\lfloor nt\rfloor}\quad\text{con interpolación lineal}$`.
- Caminatas n=16,64,256 en ejes t=[0,1],x=[−3,3]; saltos ±1/√n; etiqueta «leyes de aproximaciones».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create caminata gruesa.
- [TRIGGER_2]: Refinar malla y reescalar alturas.
- [TRIGGER_3]: Mostrar varianza al tiempo 1 igual a 1, sin afirmar coincidencia de trayectorias.

#### Escena: 02

##### Nombre: Cuatro propiedades que definen al proceso

##### Descripcion Breve: Se formula el Browniano estándar respecto de una filtración.

##### Objetivo Pedagogico: Dar un contrato matemático completo.

##### Voz en off:

> "[TRIGGER_1] Un Browniano empieza en cero y tiene trayectorias continuas casi seguramente. Sus incrementos sobre intervalos disjuntos son independientes. [TRIGGER_2] El incremento entre s y t es normal centrado con varianza t menos s. Respecto de su filtración, además es independiente de la información hasta s. [TRIGGER_3] Estas propiedades determinan sus leyes finito-dimensionales. Continuidad y adaptación describen cómo se ensamblan esas observaciones en un proceso."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_0=0,\quad W_t-W_s\sim N(0,t-s)$`.
- MathTex: `$W_t-W_s\perp\mathcal F_s,\quad W_t\text{ adaptado}$`.
- Trayectoria y tres intervalos disjuntos; campanas de incrementos de anchuras √Δt; cuatro tarjetas de propiedades.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write inicio y continuidad.
- [TRIGGER_2]: Resaltar intervalos y campanas independientes.
- [TRIGGER_3]: Create filtración hasta s y separar incremento futuro.

#### Escena: 03

##### Nombre: La covarianza recuerda el pasado compartido

##### Descripcion Breve: Dos tiempos comparten una parte del recorrido.

##### Objetivo Pedagogico: Calcular min(s,t).

##### Voz en off:

> "[TRIGGER_1] Para s menor que t, el valor W t contiene W s más un incremento nuevo independiente de media cero. [TRIGGER_2] Multiplicamos por W s y promediamos. El término nuevo desaparece; queda la varianza de W s, que vale s. [TRIGGER_3] Por tanto la covarianza entre dos tiempos es su mínimo. No confundamos valores independientes con incrementos independientes: los valores comparten historia."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_t=W_s+(W_t-W_s)$`.
- MathTex: `$\mathbb E[W_sW_t]=s\quad(s\le t)$`.
- MathTex: `$\operatorname{Cov}(W_s,W_t)=\min(s,t)$`.
- Dos marcadores temporales y segmento compartido; matriz de covarianzas para tiempos 1/4,1/2,1; los valores 1/4,1/2,1 explícitos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create descomposición del recorrido.
- [TRIGGER_2]: Write producto y cancelar término cruzado.
- [TRIGGER_3]: Construir matriz simétrica con mínimos.

#### Escena: 04

##### Nombre: Una construcción por puntos medios

##### Descripcion Breve: Condicionales gaussianas generan refinamientos coherentes.

##### Objetivo Pedagogico: Mostrar existencia constructiva sin fingir una prueba completa.

##### Voz en off:

> "[TRIGGER_1] Elegimos W uno normal estándar. Dados los extremos de un intervalo, el valor del punto medio es su promedio más un ruido normal de varianza igual a un cuarto de la longitud del intervalo. [TRIGGER_2] Repetimos usando ruidos nuevos independientes. Los valores ya fijados permanecen fijos; cada nivel añade detalles compatibles con las leyes gaussianas del Browniano. [TRIGGER_3] Un teorema de convergencia de esta construcción garantiza un límite continuo casi seguramente. Presentamos el mecanismo y el teorema, sin atribuir esa garantía a una animación finita."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W_1\sim N(0,1)$`.
- MathTex: `$W_{(a+b)/2}=\frac{W_a+W_b}{2}+\frac{\sqrt{b-a}}2Z,\quad Z\sim N(0,1)$`.
- Malla diádica hasta nivel 8, semilla 1401; puntos viejos fijos y nuevos medios; tarjeta «convergencia uniforme c.s.: resultado de construcción».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create extremos.
- [TRIGGER_2]: Añadir medios con desviación √(b−a)/2 y conectar linealmente.
- [TRIGGER_3]: Refinar hasta nivel 8 y mostrar teorema de límite continuo.

#### Escena: 05

##### Nombre: Donsker necesita un espacio de caminos

##### Descripcion Breve: El TLC funcional controla más que un tiempo fijo.

##### Objetivo Pedagogico: Precisar qué significa límite de caminatas.

##### Voz en off:

> "[TRIGGER_1] El teorema central del límite describe el caminante en un tiempo fijo. Para obtener un proceso necesitamos controlar una curva completa. [TRIGGER_2] Donsker afirma que las caminatas reescaladas e interpoladas convergen en distribución en el espacio de funciones continuas con distancia uniforme, sobre un intervalo compacto. [TRIGGER_3] Esa convergencia requiere control conjunto y tightness; no se obtiene solo mirando histogramas en varios tiempos. Tampoco promete que dos simulaciones independientes se acerquen punto por punto."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$W^{(n)}\Rightarrow W\quad\text{en }C([0,1]),\quad d(f,g)=\sup_{t\in[0,1]}|f(t)-g(t)$`.
- MathTex: `$\xi_j\text{ iid},\quad\mathbb E\xi_j=0,\quad\mathbb E\xi_j^2=1$`.
- Colección de curvas como puntos de un espacio abstracto; banda uniforme alrededor de una curva; rótulo «Donsker: teorema enunciado».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mostrar histograma a t=1 y luego curva completa.
- [TRIGGER_2]: Create banda uniforme y escribir espacio de funciones.
- [TRIGGER_3]: Separar convergencia de leyes de acoplamiento trayectoria a trayectoria.

#### Escena: 06

##### Nombre: Autosimilitud no significa la misma curva

##### Descripcion Breve: Escalar tiempo y espacio preserva la ley.

##### Objetivo Pedagogico: Interpretar igualdad en distribución de procesos.

##### Voz en off:

> "[TRIGGER_1] Si aceleramos el tiempo por c, la varianza crece por c. Dividir la altura entre raíz de c restaura la escala original. [TRIGGER_2] El proceso reescalado tiene la misma ley que un Browniano estándar: conserva continuidad, incrementos independientes y las varianzas correctas. [TRIGGER_3] La igualdad es de distribución, no una identidad entre dos segmentos de una misma realización. Un zoom puede parecer estadísticamente similar sin repetirse exactamente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$(W_{ct}/\sqrt c)_{t\ge0}\overset d=(W_t)_{t\ge0}$`.
- Dos ventanas t=[0,1] y t=[0,4] con ejes correctamente reescalados; c=4; histogramas de incrementos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create ventana ampliada temporal.
- [TRIGGER_2]: Dividir alturas entre 2 y verificar varianzas.
- [TRIGGER_3]: Write igualdad en ley con símbolo d destacado.

#### Escena: 07

##### Nombre: Continuo pero sin tangente

##### Descripcion Breve: Pendientes a escalas pequeñas crecen en dispersión.

##### Objetivo Pedagogico: Distinguir intuición de teorema de no diferenciabilidad.

##### Voz en off:

> "[TRIGGER_1] La pendiente sobre un paso h es el incremento dividido entre h. Su varianza es uno sobre h y crece al hacer zoom. [TRIGGER_2] Esto sugiere que las pendientes no se estabilizan como en una curva suave. Pero esa cuenta por sí sola no prueba no diferenciabilidad en todos los puntos. [TRIGGER_3] El teorema más fuerte dice que casi seguramente una trayectoria browniana no es diferenciable en ningún punto. La rugosidad está en todas las escalas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\frac{W_{t+h}-W_t}{h}\sim N(0,1/h)$`.
- MathTex: `$P(W\text{ es continua y no diferenciable en ningún punto})=1$`.
- Ventanas h=1/4,1/16,1/64 sobre malla refinada coherente; secantes; campanas de pendientes ensanchándose; tarjeta «resultado de regularidad».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create secantes con h decreciente.
- [TRIGGER_2]: Write varianza y mostrar dispersión, rotulada intuición.
- [TRIGGER_3]: Presentar teorema aparte y retirar falsa tangente límite.

#### Escena: 08

##### Nombre: Cómo simular lo que acabamos de definir

##### Descripcion Breve: Incrementos gaussianos exactos en malla y segmentos aproximados.

##### Objetivo Pedagogico: Cerrar con una receta honesta.

##### Voz en off:

> "[TRIGGER_1] En una malla uniforme generamos normales independientes Z k y usamos incrementos raíz de h por Z k. Acumularlos da exactamente la ley browniana en esos nodos. [TRIGGER_2] Las líneas que conectan los nodos son una interpolación, no la trayectoria continua completa. Para comparar resoluciones de la misma muestra debemos sumar incrementos finos o refinar mediante puentes. [TRIGGER_3] Ya tenemos una fuente de ruido temporal con información, escala y leyes precisas. El siguiente problema es medir cuánto se mueve."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\Delta W_k=\sqrt h\,Z_k,\quad W_{k+1}=W_k+\Delta W_k$`.
- MathTex: `$\Delta W^{\rm grueso}_j=\Delta W^{\rm fino}_{2j}+\Delta W^{\rm fino}_{2j+1}$`.
- Malla T=1,N=1024, semilla 1402; 256 trayectorias tenues y una principal; nodos exactos/segmentos interpolados con estilos distintos.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write receta y generar puntos.
- [TRIGGER_2]: Create segmentos punteados etiquetados interpolación.
- [TRIGGER_3]: Agrupar incrementos de dos en dos y superponer malla gruesa coherente.

