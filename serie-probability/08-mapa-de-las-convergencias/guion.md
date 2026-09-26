# Video 08: El mapa de las convergencias y el zoo de contraejemplos

Las cinco nociones del roadmap se convierten en una herramienta para razonar sobre aproximaciones.

## Producción y alcance

- Formato 16:9; frame_width=14.222, frame_height=8. Márgenes seguros: x entre -6.5 y 6.5; y entre -3.5 y 3.5. Texto 30–34 pt; fórmulas 36–42 pt; anotaciones 24–26 pt. Dividir ecuaciones largas en renglones, sin reducirlas por debajo de 28 pt.
- Locución prevista: aproximadamente 496 palabras (3.4–4.1 minutos a 120–145 palabras por minuto, sin pausas). La duración final se fija con una lectura de prueba y el montaje de las demostraciones; no alargar artificialmente las escenas. Reservar 2–4 segundos por fórmula y 5–8 segundos para las preguntas al espectador.
- Estilo: importar styles.theme; BG_COLOR para fondo, TEXT_MAIN para fórmulas, TEXT_MUTED para contexto. ACCENT_INDIGO identifica estructuras; ACCENT_TERRACOTTA, el parámetro activo; ACCENT_CYAN, correspondencias; ACCENT_MINT, la conclusión; ACCENT_VINO, una hipótesis incumplida. Añadir etiquetas y trazos para que el color nunca sea la única señal. No se añaden colores.
- Los triggers se reinician en cada escena y se ejecutan al pronunciar el fragmento que sigue a la marca. Cada marca tiene exactamente una entrada en la secuencia; las transiciones internas se encadenan dentro de esa entrada.
- p≥1. 'Segura' se interpreta como convergencia puntual para todo ω, no uniforme. Acoplamiento explícito al comparar variables.

## Bibliografía y decisiones matemáticas

Proba §§2.2–2.8 y §§3.3–3.4. Probita §3.2 para Borel-Cantelli. Se usan pruebas y contraejemplos originales adaptados al formato visual.

#### Escena: 01

##### Nombre: Cinco preguntas distintas

##### Descripcion Breve: Las diferentes nociones de cercanía aparecen como instrumentos de medida.

##### Objetivo Pedagogico: Dar sentido a un mapa de implicaciones.

##### Voz en off:

> "[TRIGGER_1] Una aproximación puede acertar en cada historia, tener error medio pequeño o reproducir solo una distribución. [TRIGGER_2] Cada afirmación mide algo distinto. Compartir la palabra convergencia no las vuelve intercambiables. [TRIGGER_3] Construiremos un mapa donde cada flecha expresa una garantía y cada camino prohibido tiene un contraejemplo que podremos calcular."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{puntual},\quad\text{c.s.},\quad L^p,\quad P,\quad\mathcal D$`.
- Cinco RoundedRectangle con nombres completos; miniaturas de trayectoria, pico e histograma; título «¿qué información conserva cada límite?».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: FadeIn las cinco tarjetas.
- [TRIGGER_2]: Asociar miniaturas a tarjetas mediante Arrow.
- [TRIGGER_3]: Escribir la pregunta y dejar las conexiones aún vacías.

#### Escena: 02

##### Nombre: Las flechas válidas

##### Descripcion Breve: Se construyen dos ramas que confluyen en probabilidad.

##### Objetivo Pedagogico: Evitar una jerarquía lineal falsa.

##### Voz en off:

> "[TRIGGER_1] Convergencia puntual implica casi segura, que implica probabilidad y después distribución. [TRIGGER_2] L p también implica probabilidad. Sobre un espacio de probabilidad, L q implica L p si q es mayor o igual que p. [TRIGGER_3] Casi segura y L p deben permanecer en ramas distintas. Ninguna controla automáticamente a la otra."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$\text{puntual}\Rightarrow\text{c.s.}\Rightarrow P\Rightarrow\mathcal D$`.
- MathTex: `$L^q\Rightarrow L^p\Rightarrow P,\quad1\le p\le q$`.
- Grafo dentro del panel izquierdo: rama superior y=1.3, inferior y=−1.3; nodos de ancho 1.1; ecuaciones justificativas en panel derecho; P común en extremo derecho del grafo.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create rama superior con flechas.
- [TRIGGER_2]: Create rama inferior y unión en P; anotar P(Ω)=1.
- [TRIGGER_3]: Encerrar c.s. y Lp con cajas independientes y conservar espacio entre ellas.

#### Escena: 03

##### Nombre: Picos contra los momentos

##### Descripcion Breve: Altura y anchura compensan un límite puntual.

##### Objetivo Pedagogico: Refutar c.s. implica Lp.

##### Voz en off:

> "[TRIGGER_1] El pico de altura n y anchura uno sobre n desaparece finalmente de cada punto de [0,1]. En cero lo definimos como cero. [TRIGGER_2] Su momento p vale n elevado a p menos uno. Para p igual a uno queda constante; para p mayor que uno crece. [TRIGGER_3] Por tanto ni siquiera convergencia puntual garantiza L p. El promedio puede conservar masa que se concentra en regiones diminutas."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=n\mathbf1_{(0,1/n)}\to0\text{ puntualmente}$`.
- MathTex: `$\mathbb E|X_n|^p=n^{p-1}\not\to0\quad(p\ge1)$`.
- Axes [0,1]×[0,16]; picos n=2,4,8,16; medidor de área y momento; miniatura de flecha tachada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Transform los picos siguiendo un punto fijo.
- [TRIGGER_2]: Write altura^p por anchura y resultados p=1,2.
- [TRIGGER_3]: Colocar miniatura del pico sobre la flecha c.s. hacia Lp tachada.

#### Escena: 04

##### Nombre: Momentos sin calma

##### Descripcion Breve: Indicadores independientes convergen en todos los Lp finitos pero siguen parpadeando.

##### Objetivo Pedagogico: Refutar Lp implica c.s.

##### Voz en off:

> "[TRIGGER_1] Tomemos indicadores independientes con probabilidad uno sobre n de valer uno. Todo momento positivo vale uno sobre n y tiende a cero. [TRIGGER_2] La serie de probabilidades diverge. Borel-Cantelli garantiza infinitos unos casi seguramente. Los complementos también son independientes y tienen suma divergente, así que hay infinitos ceros. [TRIGGER_3] Las trayectorias no convergen, aunque desaparezcan todos esos momentos. La independencia es parte esencial de este ejemplo."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=\mathbf1_{A_n},\quad P(A_n)=1/n$`.
- MathTex: `$\mathbb E|X_n|^p=1/n\to0$`.
- MathTex: `$\limsup X_n=1,\quad\liminf X_n=0\quad\text{c.s.}$`.
- Fila de indicadores simulados con semilla 804; tarjeta «independientes»; series armónicas y de complementos; no inferir infinitud de la muestra mostrada.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create fila y probabilidades.
- [TRIGGER_2]: Write momento y aplicar Borel-Cantelli a eventos y complementos.
- [TRIGGER_3]: Adjuntar contraejemplo a flecha Lp hacia c.s. tachada.

#### Escena: 05

##### Nombre: Las otras recíprocas

##### Descripcion Breve: Una alternancia simétrica y un punto nulo separan otras nociones.

##### Objetivo Pedagogico: Completar el mapa con testigos precisos.

##### Voz en off:

> "[TRIGGER_1] Si X es normal centrada, alternar X y menos X conserva la ley, pero la probabilidad de distancia grande al X original no desaparece. [TRIGGER_2] Para separar casi segura de puntual, ponemos el valor n en el punto cero y cero en el resto del intervalo unidad. [TRIGGER_3] La excepción tiene probabilidad cero, aunque su trayectoria diverge. La noción puntual depende de lo que hacemos incluso en resultados nulos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n=(-1)^nX,\quad X\sim N(0,1)$`.
- MathTex: `$Y_n=n\mathbf1_{\{0\}}\to0\text{ c.s., no puntualmente}$`.
- Campana fija junto a trayectoria alternante; punto aislado creciendo sobre ω=0; dos etiquetas de flechas inversas falsas.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Create alternancia y mostrar P(2|X|>ε)>0 en impares.
- [TRIGGER_2]: Create punto nulo y aumentar su altura.
- [TRIGGER_3]: Colocar ambos testigos en el mapa sin modificar flechas válidas.

#### Escena: 06

##### Nombre: Puentes con hipótesis

##### Descripcion Breve: Dominación y límites constantes recuperan implicaciones.

##### Objetivo Pedagogico: Entender condiciones adicionales.

##### Voz en off:

> "[TRIGGER_1] Si X n converge casi seguramente y su potencia p está dominada por una variable integrable, recuperamos convergencia L p por dominada. [TRIGGER_2] Desde probabilidad podemos extraer una subsucesión casi seguramente convergente; esa garantía no cubre todos los índices. [TRIGGER_3] Si el límite en distribución es una constante, sí obtenemos convergencia en probabilidad. Cada condición elimina una dificultad específica de los ejemplos anteriores."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$|X_n|^p\le Y\in L^1,\ X_n\to X\text{ c.s.}\Rightarrow\mathbb E|X_n-X|^p\to0$`.
- MathTex: `$|X_n-X|^p\le2^pY$`.
- MathTex: `$X_n\Rightarrow c\iff X_n\xrightarrow P c$`.
- Puentes con líneas discontinuas rotulados dominación/subsucesión/constante; curva techo Y y selección de índices.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Dibujar puente de dominación y cota del error.
- [TRIGGER_2]: Seleccionar índices y anotar «solo subsucesión».
- [TRIGGER_3]: Dibujar puente de distribución a probabilidad con c constante visible.

#### Escena: 07

##### Nombre: Mapeo continuo

##### Descripcion Breve: Se transforman variables manteniendo el límite cuando la función es regular.

##### Objetivo Pedagogico: Separar continuidad e integrabilidad.

##### Voz en off:

> "[TRIGGER_1] Una transformación continua conserva convergencia casi segura, en probabilidad y en distribución. [TRIGGER_2] Para distribución basta que las discontinuidades tengan probabilidad cero bajo la ley límite. El recíproco uno sobre x exige vigilar el cero. [TRIGGER_3] No añadimos L p a esa lista sin más: una transformación continua puede aumentar demasiado las colas. Allí hacen falta condiciones de momentos."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n\Rightarrow X,\ P(X\in D_g)=0\Rightarrow g(X_n)\Rightarrow g(X)$`.
- MathTex: `$g(x)=1/x,\quad D_g=\{0\}\text{ si se define allí arbitrariamente}$`.
- Curva x² con puntos de entrada/salida; después 1/x con asíntota y cero marcado; tarjeta «Lp requiere control adicional».

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Mover puntos por x².
- [TRIGGER_2]: Transform al recíproco y destacar discontinuidad.
- [TRIGGER_3]: Añadir tarjeta de momentos y mantener teorema en pantalla.

#### Escena: 08

##### Nombre: Slutsky hace útil el mapa

##### Descripcion Breve: Una escala aleatoria consistente puede reemplazarse por una constante.

##### Objetivo Pedagogico: Aplicar convergencia conjunta con un componente constante.

##### Voz en off:

> "[TRIGGER_1] Si X n converge en distribución y Y n converge en probabilidad a c, podemos sumar y multiplicar sus límites; dividir requiere c distinto de cero. [TRIGGER_2] No hace falta independencia. La pareja converge conjuntamente a X,c porque el segundo componente se concentra en una constante. [TRIGGER_3] Así justificamos sustituir parámetros por estimadores consistentes. Con dos límites aleatorios, conocer solo las dos marginales no basta para controlar una suma."

##### Descripcion Visual Detallda:

###### Objetos:

- MathTex: `$X_n\Rightarrow X,\ Y_n\xrightarrow P c\Rightarrow(X_n,Y_n)\Rightarrow(X,c)$`.
- MathTex: `$X_n+Y_n\Rightarrow X+c,\quad X_nY_n\Rightarrow cX$`.
- MathTex: `$X_n/Y_n\Rightarrow X/c\quad(c\ne0)$`.
- Entradas Xn,Yn a cajas suma/producto/cociente; hipótesis fija encima; mapa final con ejemplos en miniatura.

###### Layout y disposicion:

- Título en UP * 3.25, ancho máximo 12.4. Demostración en LEFT * 3.15, centro DOWN * 0.15, caja útil 6.0 × 5.1. Ecuaciones en RIGHT * 3.15, ancho 5.8; arrange(DOWN, buff=0.45), alineadas a la izquierda, centro UP * 0.2. Conclusión en DOWN * 3.1.
- Conservar fijos ejes y etiquetas durante cambios de parámetro. Mantener el objeto anterior a opacidad 0.25 hasta completar la comparación; retirarlo antes de escribir la conclusión. Colocar cada rótulo de muestra o esquema junto al objeto que califica.

##### Secuencia de animacion:

- [TRIGGER_1]: Write hipótesis y pareja límite.
- [TRIGGER_2]: Transform operadores y marcar c≠0 al dividir.
- [TRIGGER_3]: Restaurar mapa y conectar la ruta P→constante→Slutsky.

