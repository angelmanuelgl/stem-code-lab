# Video 05: Los monos infinitos y las alarmas que regresan

Una palabra al azar sirve para preguntar cuándo unos eventos ocurren infinitas veces. Se prueban ambos lemas y se aplican a errores de aproximación.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 496 palabras (3.4–4.1 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- BCI no necesita independencia; BCII se presenta para eventos mutuamente independientes. Los intentos de escritura son bloques disjuntos.

## Bibliografía y decisiones matemáticas

Probita §3.2, pp. impresas 67–70: lema de Borel-Cantelli y ley 0–1 de Borel. Proba §§2.3–2.4: aplicaciones a convergencia.

#### Escena: 01

##### Nombre: Una palabra diminutamente probable

##### Descripcion Breve: Un teclado aleatorio plantea un evento infinito.

##### Objetivo Pedagogico: Separar probabilidad pequeña de imposibilidad.

##### Voz en off:

> "[TRIGGER_1] Un teclado escoge entre veintisiete símbolos. ¿Escribirá PROBA alguna vez? ¿Y una infinidad de veces? [TRIGGER_2] Separamos el texto en bloques disjuntos de cinco letras. Cada bloque es independiente y tiene probabilidad veintisiete elevado a menos cinco de acertar. [TRIGGER_3] La pregunta no es qué veremos en diez segundos. Queremos entender qué cambia al permitir intentos sin límite."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$p=27^{-5},\quad A_n=\{\text{bloque }n=\text{PROBA}\}$`.
- Seis bloques de cinco casillas; símbolos con semilla fija; tarjeta p; si se muestra un éxito construido, rotular «ejemplo».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create teclado y bloques.
- [TRIGGER_2]: Dibujar separadores y Write p.
- [TRIGGER_3]: Extender línea temporal con flecha y pregunta «infinitas veces».

#### Escena: 02

##### Nombre: Escribir infinitas veces como conjunto

##### Descripcion Breve: Uniones de colas e intersección expresan recurrencia.

##### Objetivo Pedagogico: Definir limsup.

##### Voz en off:

> "[TRIGGER_1] Que haya infinitos éxitos significa que después de cualquier inicio todavía aparece alguno. [TRIGGER_2] La unión de eventos desde N significa al menos un éxito posterior. Intersectar sobre todos los N exige que ninguna cola quede vacía de éxitos. [TRIGGER_3] Ese conjunto es el límite superior de los eventos. No exige éxitos consecutivos ni ausencia de fracasos intermedios."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\limsup_nA_n=\bigcap_{N\ge1}\bigcup_{n\ge N}A_n=\{A_n\ {\rm i.o.}\}$`.
- Línea con éxitos en 2,5,9,14; ventana de cola; árbol de unión e intersección.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mover N entre éxitos.
- [TRIGGER_2]: Write unión y después intersección.
- [TRIGGER_3]: Resaltar fracasos intermedios y etiqueta «infinitas veces ≠ siempre desde cierto momento».

#### Escena: 03

##### Nombre: Primera dirección

##### Descripcion Breve: Una serie convergente controla la unión de una cola.

##### Objetivo Pedagogico: Demostrar BCI.

##### Voz en off:

> "[TRIGGER_1] Supongamos que la suma de las probabilidades es finita. La probabilidad de algún evento después de N no supera la suma de esa cola. [TRIGGER_2] Las colas de una serie convergente tienden a cero. El evento de infinitas ocurrencias está contenido en cada una de esas uniones. [TRIGGER_3] Su probabilidad debe ser cero. Observa que no utilizamos independencia: la sumabilidad bastó."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\sum_nP(A_n)<\infty$`.
- MathTex: `$P(\limsup A_n)\le\sum_{n\ge N}P(A_n)\to0$`.
- Barras 2^−n; llave de cola; contador 2^(1−N); tarjeta «sin independencia».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create barras y condición.
- [TRIGGER_2]: Mover llave y Write cota por unión.
- [TRIGGER_3]: Encerrar probabilidad cero y revelar tarjeta.

#### Escena: 04

##### Nombre: Una falsa recíproca

##### Descripcion Breve: Un único lanzamiento determina todos los eventos.

##### Objetivo Pedagogico: Mostrar que divergencia sola no basta.

##### Voz en off:

> "[TRIGGER_1] Haz una sola tirada de moneda y define todos los eventos como que salió cara. Cada probabilidad es un medio y la suma diverge. [TRIGGER_2] Si sale cara, ocurren todos. Si sale cruz, ninguno. La probabilidad de infinitas ocurrencias es un medio. [TRIGGER_3] La suma diverge pero el resultado no es uno. La dependencia puede convertir infinitas oportunidades aparentes en una sola decisión."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$A_n=A,\quad P(A)=1/2$`.
- MathTex: `$\sum_nP(A_n)=\infty,\quad P(\limsup A_n)=1/2$`.
- Moneda conectada a todas las casillas; fila completa de unos y fila completa de ceros.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create moneda y conexiones.
- [TRIGGER_2]: Mostrar dos filas con peso 1/2.
- [TRIGGER_3]: Write cálculo y tachar recíproca sin independencia.

#### Escena: 05

##### Nombre: Segunda dirección

##### Descripcion Breve: Un producto de fracasos cae a cero.

##### Objetivo Pedagogico: Demostrar BCII.

##### Voz en off:

> "[TRIGGER_1] Ahora sí suponemos independencia. No ver ningún evento entre N y M tiene probabilidad igual al producto de sus probabilidades de fracaso. [TRIGGER_2] Uno menos x está acotado por exponencial de menos x. Si la suma de probabilidades diverge, ese producto tiende a cero. [TRIGGER_3] Así, después de cada N hay un éxito con probabilidad uno. Intersectamos estas afirmaciones numerablemente y obtenemos infinitos éxitos casi seguramente."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P\left(\bigcap_{n=N}^MA_n^c\right)=\prod_{n=N}^M(1-P(A_n))$`.
- MathTex: `$\prod_{n=N}^M(1-P(A_n))\le e^{-\sum_{n=N}^MP(A_n)}\to0$`.
- MathTex: `$P(\limsup A_n)=1$`.
- Producto de tarjetas independientes; curva e^−s; intersección numerable rotulada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write producto con «independientes» encima.
- [TRIGGER_2]: Transform a exponencial y mover suma s hacia infinito.
- [TRIGGER_3]: Cambiar no éxito a algún éxito y Write conclusión para todo N.

#### Escena: 06

##### Nombre: Infinitud no significa rapidez

##### Descripcion Breve: La geométrica calcula cuánto esperar.

##### Objetivo Pedagogico: Aplicar sin exagerar el resultado.

##### Voz en off:

> "[TRIGGER_1] Nuestros bloques tienen probabilidad positiva constante, por lo que la suma diverge: PROBA aparecerá infinitas veces casi seguramente. [TRIGGER_2] El número de bloques hasta el primer éxito es geométrico. Su esperanza es uno sobre p. [TRIGGER_3] Para una palabra de longitud L, la espera media es veintisiete elevado a L. Una certeza asintótica puede coexistir con una espera completamente impráctica."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(T>m)=(1-p)^m,\quad\mathbb ET=1/p$`.
- MathTex: `$p=27^{-L},\quad\mathbb ET=27^L$`.
- Gráfico de probabilidad de éxito 1−(1−p)^m; eje m logarítmico; slider L.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Restaurar bloques y aplicar BCII.
- [TRIGGER_2]: Create curva y marcador m=1/p.
- [TRIGGER_3]: Mover L=1..5 y actualizar espera; no fabricar tiempos físicos.

#### Escena: 07

##### Nombre: De eventos a límites

##### Descripcion Breve: Errores por tolerancia forman familias de eventos.

##### Objetivo Pedagogico: Probar un criterio de convergencia casi segura.

##### Voz en off:

> "[TRIGGER_1] Un evento puede representar que una aproximación falla por más de uno sobre m. Si las probabilidades de esos errores son sumables, solo ocurren finitos casi seguramente. [TRIGGER_2] Aplicamos esto para cada entero m. La unión de las excepciones nulas continúa siendo nula. [TRIGGER_3] Fuera de ella, cada tolerancia acaba respetándose. Esa es precisamente la convergencia casi segura."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$A_n^{(m)}=\{|X_n-X|>1/m\}$`.
- MathTex: `$\forall m:\ \sum_nP(A_n^{(m)})<\infty\Rightarrow X_n\to X\ {\rm c.s.}$`.
- Matriz con filas m y columnas n; última alarma por fila; recinto de excepciones Nm.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create primera fila y marcar finitud.
- [TRIGGER_2]: Añadir filas y Write unión de Nm.
- [TRIGGER_3]: Indicate tiempos finales distintos y transformar a definición c.s.

#### Escena: 08

##### Nombre: El umbral de las alarmas

##### Descripcion Breve: n^−α resume los dos regímenes.

##### Objetivo Pedagogico: Consolidar sumabilidad y dependencia.

##### Voz en off:

> "[TRIGGER_1] Con alarmas independientes de probabilidad n elevado a menos alfa, aparece una frontera en alfa igual a uno. [TRIGGER_2] Por encima, la serie converge y solo hay finitas alarmas casi seguramente. Entre cero y uno, incluida la unidad, ocurren infinitas. [TRIGGER_3] En este último caso cada alarma es cada vez menos probable, pero el número de oportunidades sigue ganando. Hemos encontrado la lógica detrás de muchos focos que nunca dejan de parpadear."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$P(A_n)=n^{-\alpha},\quad\alpha>0$`.
- MathTex: `$\alpha>1\Rightarrow P({\rm i.o.})=0$`.
- MathTex: `$0<\alpha\le1,\ \text{indep.}\Rightarrow P({\rm i.o.})=1$`.
- Slider α; barras y suma parcial; dos tarjetas de conclusión y rótulo de independencia.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mostrar α=2 y cola sumable.
- [TRIGGER_2]: Mover α a 1 y después 1/2; destacar divergencia.
- [TRIGGER_3]: Write clasificación y cerrar con barra de probabilidades individuales que tienden a cero.

