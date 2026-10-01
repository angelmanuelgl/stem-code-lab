# Guion storyboard / técnico — Jenga Boom

## Convenciones generales de producción

- **Alcance:** guion narrativo y especificación visual exclusivamente de Jenga Boom. Fuente conceptual: `guion_sol.md` de esta misma carpeta. Esta entrega conserva los archivos originales y describe escenas para implementación posterior.
- **Arco de descubrimiento:** criterio geométrico → posiciones frente a cantidades → envolvente de tiras → normalización → reducción a un eje → agregación de masa → productos enteros → actualización y barrido → traza completa → prueba y casos que separan errores conceptuales → costos y verificación → cierre. Cada reducción se demuestra antes de utilizarse como garantía.
- **Frame:** 16:9, ancho lógico 128/9 y alto 8, centro `(0,0,0)`. Área segura x∈[−6.3,6.3],y∈[−3.5,3.5]. Fondo `BG_COLOR`. Título centrado en `(0,3.1,0)`, ancho máximo 11.8 y altura máxima 0.7; títulos largos en dos líneas, con 28–32 pt si hace falta. Ningún dato, flecha o arco invade la franja del título.
- **Tipografía:** todo rótulo visible con `Tex` o `MathTex`. Texto principal 28–34 pt, letras/índices de piezas 26–32 pt, fórmulas 30–36 pt. Tablas densas de la escena 25: 25–26 pt y fila activa ampliable. Salidas `yes`, `no` con `Tex` monoespaciado, índice de operación con `MathTex`. No colocar bloques de código, pseudocódigo, terminal, capturas o el objeto `Code` en pantalla.
- **Objetos Manim:** bloques como `VGroup` de caras `Polygon`, con identidad persistente `(l,k)`; diagramas de datos como registros `RoundedRectangle` más textos; cortes y soportes como planos o bandas `Polygon`; centros como `Dot`; proyecciones `DashedLine`; punteros `Triangle`; arcos y rutas `Arrow`; brackets y llaves `Brace`; contornos `SurroundingRectangle`. Las caras de la torre se dibujan con orden de profundidad consistente. Los nombres de objetos son especificaciones de implementación posterior, no textos que deba leer el espectador.
- **Proyección de bloques:** capa impar ocupa X∈[2(k−1),2k],Y∈[0,2n]; par ocupa X∈[0,2n],Y∈[2(k−1),2k]; cada bloque ocupa altura visual z∈[l−1,l]. Aplicar las funciones P indicadas para cada torre a todas sus esquinas, de modo que la orientación y los huecos sean coherentes. La altura visual se elige para legibilidad; ninguna comprobación depende de ella.
- **Vistas:** planos completos utilizan la escala horizontal especificada; bandas de una dimensión representan únicamente el eje corto y pueden comprimir la dirección larga. Rotular X o Y en el detalle para que cambiar una vista a una fila no cambie el eje matemático. Nunca tratar una banda de soporte convexo como si rellenara los huecos con madera nueva.
- **Paleta:** `BG_COLOR=#181C24`, `TEXT_MAIN=#ECEFF4`, `TEXT_MUTED=#64748B`, `ACCENT_VINO=#C0392B`, `ACCENT_MINT=#2DD4BF`, `ACCENT_TERRACOTTA=#D97706`, `ACCENT_INDIGO=#6366F1`, `ACCENT_CYAN=#38BDF8`, conforme a `styles.theme`. Capas impares/eje X en índigo; pares/eje Y en cian. Centro y pieza activa en terracota; soporte válido y sellos de estabilidad en verde. Rojo se reserva para un fallo probado o un método incorrecto explícitamente rotulado. Una retirada, un hueco o C=0 no son errores por sí mismos.
- **Masa y soporte:** la capa l aporta el soporte del corte; sus bloques NO están en el banco que se usa para comprobar ese corte. El banco contiene todas las capas estrictamente superiores. Campos locales: `count_l,sx_l,sy_l,L_l,R_l`; banco global: `C,S_x,S_y`. Cada uno tiene su rótulo. C positivo habilita la comprobación; con C=0 no dibujar un centro ni una división.
- **Interior estricto:** la envolvente puede dibujarse con contorno cerrado, pero el conjunto admisible es su interior. Marcar los extremos de intervalos admisibles con círculos abiertos. Borde significa caída. Preservar cada símbolo `<`; las cotas débiles de coordenadas son otras desigualdades, nunca una relajación del criterio.
- **Notación inequívoca:** `2(L−1)` es el doble de la diferencia entre L y uno; `2L−1` es un centro y tiene otro significado. El término derecho `2R` es un borde. Mantener paréntesis en todas las sustituciones. Los índices de capas se numeran desde abajo y los de bloques desde un extremo coherente con la fórmula de coordenadas.
- **Sincronización:** triggers numerados desde 1 en cada escena; identidad completa `(escena,trigger)`. La voz de cada escena se copia literalmente entre ambos archivos. Toda creación, desplazamiento, cambio de número, limpieza y transición ocurre dentro de un trigger especificado. El primer trigger realiza la limpieza de objetos no heredados y el cambio de título. No insertar animaciones sin marca entre escenas.
- **Tiempo:** ventanas de animación locales estimadas a 145 palabras/minuto, más 1.5 s por `[Pausa.]` y holds de lectura. Esa indicación se interpreta como silencio, no se pronuncia. La grabación final fija el ajuste de holds. Animaciones simples de 0.5–1 s, transformaciones de 1–1.5 s; enumeraciones acompasan los elementos nombrados. Alargar una ventana si hace falta; no omitir pasos ni acelerar números para cumplir la estimación.
- **Continuidad del ejemplo:** escenas 19–24 conservan la torre n=5,h=6, identidad de sus 30 bloques, detalle de capa4 y bancos. Si se renderizan separadamente, recrear exactamente el estado final anterior. Retirar una pieza elimina sus caras de masa presente; el hueco puede quedar con contorno tenue y sin relleno. No restaurar bloques de operaciones anteriores. El punto de centro Y=5 permanece fijo en las cinco retiradas.
- **Historia frente a configuración:** la primera operación fallida queda fijada. En escena27, una geometría posterior estable se muestra sólo como experimento abstracto y no como reconstrucción física tras caída. En escena29 el orden de retiradas es diferente y se llega a la misma geometría sin caída previa; sus rótulos de orden son indispensables.
- **Discrepancia de la copia:** la escena28 comunica el fallo por declarar caída ante cualquier capa vacía, documentado en la fuente. No ocultarlo, no afirmar que el archivo original se modificó y no convertir el video en un tutorial de parches. El argumento correcto pregunta primero si existe masa superior.
- **Accesibilidad y rigor visual:** cada color tiene rótulo, eje o forma que refuerza su significado. Texto indispensable en `TEXT_MAIN`; `TEXT_MUTED` para referencias/huecos/inactivos. Los datos de tablas, ejemplos y posiciones anunciados como completos aparecen íntegros. Las multiplicidades simbólicas grandes llevan llaves y números; no se pretende enumerar visualmente millones de piezas.
- **Créditos y alcance:** NEERC 2016, temporada 2016–2017, 4 de diciembre de 2016. No inventar un límite oficial de tiempo o memoria. El criterio del problema determina la estabilidad; la animación no necesita simular fuerzas, rotaciones o trayectorias posteriores. Las comprobaciones previas citadas son del análisis fuente y se identifican como tales.

## Escena: 01

## Nombre: El bloque que cambia el destino de una torre

## Descripcion Breve: Una secuencia de retiradas plantea el misterio de la primera caída.

## Objetivo Pedagogico: Introducir la decisión geométrica y separar el número de la operación del piso donde falla el soporte.

## Voz en off:

> “[TRIGGER_1] Una torre de bloques parece firme. Quitamos una pieza y sigue en pie. Quitamos otra, y también. Pero una retirada más puede cambiarlo todo. [Pausa.] ¿Cómo podemos saber exactamente cuál será el primer movimiento que la vuelve inestable, sin tener que reconstruir toda la torre después de cada jugada?
> [TRIGGER_2] La torre tiene capas. En cada una hay el mismo número inicial de bloques, y la orientación gira noventa grados de una capa a la siguiente. Todas las piezas tienen la misma masa. Conocemos de antemano el orden de las retiradas y queremos el índice de la primera que provoca una caída.
> [TRIGGER_3] Los tamaños pueden ser grandes: hasta diez mil bloques por capa, cinco mil capas y cinco mil retiradas. Una torre puede empezar con cincuenta millones de bloques. La imagen que vamos a usar será pequeña, pero nuestro razonamiento tendrá que funcionar también para esa torre enorme.
> [TRIGGER_4] La pregunta no se responde contando cuántas piezas quedan. Hay que mirar dónde apoyan la masa de arriba. Vamos a descubrir cómo una regla que parece tridimensional termina dependiendo de un intervalo, una suma y un conteo. Antes, aprendamos qué significa estar estable en este problema.”

## Descripcion Visual Detallada:

## Objetos:

- Torre isométrica ilustrativa de n=3,h=4, construida con Polygon para las caras de cada bloque, sin motor de física. Cada bloque lleva identidad (l,k) en la especificación, pero no todos los rótulos se muestran a la vez.
- Fila de tarjetas de operación con contador de paso; MathTex n≤10000,h,m≤5000,hn≤5·10^7; crédito Jenga Boom · NEERC 2016.

## Layout y disposicion:

- Torre a la izquierda con proyección P(X,Y,z)=(-3.2+0.35(X−3)−0.35(Y−3),−2.0+0.10(X−3)+0.10(Y−3)+0.75z,0), X,Y∈[0,6],z∈[0,4].
- Tarjetas de operaciones en x=1.9,3.7,5.5,y=1.6; pregunta en (3.2,0.1,0), ancho máximo 5.2. Restricciones en (3.2,-1.7,0) y crédito en (0,-3.25,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear torre n=3,h=4 y primera tarjeta (4,2); sacar esa pieza de la cima hacia x=-6.1. Crear segunda tarjeta (4,1) y retirar esa otra pieza superior. Ambas configuraciones conservan soportes completos en las capas inferiores y son estables; no introducir todavía su aritmética. Rotular las dos jugadas como experimento inicial y detener cursor ante una tarjeta de pregunta durante la pausa. Las jugadas del ejemplo oficial se reservan para escenas 19–25.
- **[TRIGGER_2] — 00:24–00:48:** Señalar cuatro capas mediante brackets numerados desde abajo; alternar flechas de orientación X/Y. Mostrar fichas de igual masa y contador paso, distinguiéndolo del índice de capa.
- **[TRIGGER_3] — 00:48–01:10:** Crear restricciones y producto 10000·5000=5·10^7. Transformar la torre pequeña en una maqueta rotulada, con brace que representa h capas; no sugerir que contiene físicamente cincuenta millones de polígonos.
- **[TRIGGER_4] — 01:10–01:32:** Recuperar la torre de cuatro capas y dibujar un plano de corte. Resaltar masa superior y su apoyo como dos grupos distintos; retirar tarjetas y restricciones al finalizar el trigger, conservando el corte para la regla geométrica.

- **Duración orientativa:** 01:32. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Capas impares en ACCENT_INDIGO y pares en ACCENT_CYAN, rellenos al 0.45–0.6. Retirada activa terracota y huecos inactivos TEXT_MUTED. No marcar una pieza retirada en rojo como si toda retirada causara caída.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 02

## Nombre: Qué debe sostener cada capa

## Descripcion Breve: Cada corte compara el centro de toda la masa superior con el interior del soporte convexo.

## Objetivo Pedagogico: Definir rigurosamente el criterio, la exclusión de la capa de apoyo y el borde inestable.

## Voz en off:

> “[TRIGGER_1] Elige una capa l y traza un corte justo encima de ella. La carga que debe sostener son todos los bloques de las capas superiores: l más uno, l más dos, hasta la cima. La propia capa l es el soporte; no la incluimos en esa carga.
> [TRIGGER_2] Reunimos toda esa masa y miramos su centro de masa desde arriba. Proyectamos el punto sobre el plano horizontal. Para que este corte sea estable, el punto debe quedar en el interior estricto de la envolvente convexa de las piezas que todavía están en la capa de apoyo.
> [TRIGGER_3] Si el punto llega exactamente al borde, el problema ya considera que cae. Si queda fuera, también. En cambio, si no queda ningún bloque por encima del corte, no hay carga que sostener y ese corte no puede provocar una caída, aunque su capa esté vacía.
> [TRIGGER_4] Debemos revisar todos los cortes después de cada retirada. Una sola sección que falle vuelve inestable la configuración. La respuesta es yes y el número de esa primera retirada, o no si todas conservan la estabilidad. El modelo geométrico proporciona la decisión; nuestra tarea es evaluarlo exactamente.”

## Descripcion Visual Detallada:

## Objetos:

- Torre con corte l=2; grupo de apoyo capa 2 y grupo de carga capas 3,4; centro de masa representado por Dot y proyección por DashedLine.
- Tres vistas superiores del soporte: punto interior, punto en borde, punto exterior; región abierta representada con interior semitransparente y contorno sólido.
- Bifurcación carga superior=0 y carga superior>0; tarjetas finales Tex monoespaciadas yes, índice de operación, no.

## Layout y disposicion:

- Torre a la izquierda con P de escena 1. Plano de corte a altura z=2 y prolongación horizontal hasta x=0.
- Vista superior a la derecha: rectángulo de 4×2.2 centrado en (3.3,0.9,0); casos de punto se muestran sucesivamente en ese mismo panel. Leyenda carga≠soporte en y=-0.7; salidas en y=-2.3.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Recrear corte l=2 y colorear por contornos la carga de capas 3,4. Un bracket excluye explícitamente la capa 2. Mostrar rótulos soporte y masa estrictamente superior.
- **[TRIGGER_2] — 00:22–00:44:** Crear vista superior y trasladar sólo la proyección del centro al panel. Dibujar la envolvente como región de soporte; indicar interior mediante relleno y rótulo, sin representar contacto puntual como requisito adicional.
- **[TRIGGER_3] — 00:44–01:06:** Mover el punto interior→borde→exterior, con rótulos estable, cae por borde, cae por exterior. Después retirar toda la carga de una maqueta independiente y mostrar C=0: corte sin comprobación de centro. No mezclar ese experimento con una retirada real de la traza.
- **[TRIGGER_4] — 01:06–01:28:** Encender los cortes de una torre uno a uno como lista de comprobaciones, y mostrar que un fallo basta. Crear dos salidas posibles y un contador de operación, sin fijar aún un resultado del ejemplo oficial. Transición a un soporte visto desde arriba.

- **Duración orientativa:** 01:28. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Centro activo en ACCENT_TERRACOTTA; soporte válido verde; borde/exterior que fallan en ACCENT_VINO. Carga y soporte se distinguen por brackets y rótulos, además del color. C=0 en TEXT_MUTED, no rojo.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 03

## Nombre: Conservar muchas piezas no basta

## Descripcion Breve: Dos capas con igual cantidad de piezas pueden tener soportes diferentes.

## Objetivo Pedagogico: Mostrar por qué la posición de los extremos importa más que el conteo para el soporte.

## Voz en off:

> “[TRIGGER_1] Imagina una capa con cinco tiras numeradas del uno al cinco y un centro de carga proyectado en la coordenada cinco. Dejamos sólo las tiras uno y cinco. Quedan dos bloques, muy separados, y su envolvente se extiende de cero a diez. El centro cinco está dentro.
> [TRIGGER_2] Ahora dejamos sólo las tiras cuatro y cinco. También quedan dos bloques, con la misma masa de apoyo. Pero su envolvente se extiende de seis a diez. El mismo centro cinco está fuera. El conteo de piezas no distingue estos dos casos, y la estabilidad sí.
> [TRIGGER_3] ¿Qué información geométrica cambia entre las dos capas? [Pausa.] La posición de la primera pieza presente y la de la última. No necesitamos saber cuántas piezas de apoyo rodean el centro: necesitamos conocer los límites del soporte convexo.
> [TRIGGER_4] Este experimento deja una segunda pregunta. Entre las tiras uno y cinco hay un hueco enorme. ¿Por qué lo tratamos como parte del soporte? Porque el enunciado usa una envolvente convexa. Entender esa palabra será lo que nos permita abandonar la geometría general.”

## Descripcion Visual Detallada:

## Objetos:

- Dos bandas de proyección sobre el eje corto de una capa n=5, tiras de anchura normalizada 2; configuraciones {1,5} y {4,5}; punto de carga en X=5 en ambos paneles. La dirección larga se comprime en el esquema y no representa su longitud métrica.
- Contadores piezas=2, extremos L,R y bandas de soporte (0,10),(6,10); soporte convexo del hueco con relleno translúcido.

## Layout y disposicion:

- Panel superior centrado en (0,1.25,0), panel inferior en (0,-1.2,0). Cada fila de cinco tiras ocupa x=-5..5 con bordes físicos X=0..10 mapeados por x=X−5; altura de tira 1.0.
- Centro en x=0; contadores de piezas al margen x=5.8 y rótulos de intervalo debajo de cada panel. Pregunta breve en (0,-2.8,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Crear cinco tiras del panel superior, atenuar posiciones 2,3,4 y marcar L=1,R=5. Dibujar banda convexa y centro X=5, rótulo interior.
- **[TRIGGER_2] — 00:22–00:44:** Crear panel inferior, conservar sólo 4,5 y marcar L=4,R=5. Dibujar banda 6..10 y copiar el punto X=5 desde el panel superior sin cambiarlo. Mostrar ambos conteos iguales y resultado diferente.
- **[TRIGGER_3] — 00:44–01:03:** Encerrar extremos de cada panel con flechas; durante la pausa conservar cantidad dos y coordenada cinco. Transformar los rótulos de piezas en primer/último presente, resaltando la información que faltaba.
- **[TRIGGER_4] — 01:03–01:23:** Retirar panel inferior y ampliar el hueco entre tiras 1 y 5 del superior. Superponer segmento entre puntos de las dos tiras dentro de la envolvente. Preparar la definición convexa sin hacer aparecer una pieza física en el hueco.

- **Duración orientativa:** 01:23. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Piezas presentes índigo; huecos TEXT_MUTED sin relleno. Envolvente verde translúcida, punto terracota. Fallo del segundo panel en vino; cantidad dos se mantiene en TEXT_MAIN en ambos.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 04

## Nombre: El hueco está en la envolvente, no en la madera

## Descripcion Breve: Los segmentos entre las tiras extremas llenan un rectángulo convexo.

## Objetivo Pedagogico: Demostrar que la envolvente depende sólo de extremos y distinguirla de la unión de piezas.

## Voz en off:

> “[TRIGGER_1] Una región es convexa cuando contiene el segmento entre cualquier par de sus puntos. La envolvente convexa es la menor región convexa que contiene las piezas. Si dos tiras recorren toda la capa de frente a fondo, los segmentos entre ellas cubren también la franja que queda en medio.
> [TRIGGER_2] Tomemos las tiras dos y cuatro de una capa de cinco. Sus bordes exteriores están en dos y ocho. Cada una ocupa toda la longitud, de cero a diez en la otra dirección. El rectángulo entre esos bordes contiene las dos tiras y todos los segmentos que las conectan.
> [TRIGGER_3] También podemos demostrar que no hace falta una región mayor: todas las piezas presentes están dentro de ese rectángulo, y un rectángulo es convexo. Y no puede ser menor, porque las esquinas extremas de las tiras obligan a incluir los cuatro lados y su interior. Por ambos argumentos, esa es exactamente la envolvente.
> [TRIGGER_4] La madera sigue teniendo huecos. Lo que rellenamos es el objeto matemático que pide el criterio del problema. Por eso quitar una tira interna no cambia esta envolvente si los extremos permanecen. Pero esa pieza tiene masa: retirarla sí puede cambiar lo que tendrán que sostener las capas inferiores. Soporte y masa son dos cuentas distintas.”

## Descripcion Visual Detallada:

## Objetos:

- Plano de cinco tiras, sólo 2 y 4 presentes; unión de madera como dos rectángulos separados y envolvente como rectángulo [2,8]×[0,10].
- Cuatro esquinas extremas, segmentos transversales y diagonales; rótulos unión de piezas y envolvente convexa; caja mínima y caja que contiene todas las piezas.

## Layout y disposicion:

- Plano a la izquierda: transformación F(X,Y)=(-3.2+0.43(X−5),0.43(Y−5),0), con X,Y∈[0,10]; ocupa x=-5.35..-1.05,y=-2.15..2.15.
- Panel de razonamiento en x=3.0, con tarjetas contiene piezas en y=1.35 y está forzado por esquinas en y=-0.2. Leyenda de hueco físico en (3,-1.75,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Recrear sólo tiras 2 y 4. Elegir dos puntos de igual Y en tiras opuestas y dibujar su segmento; deslizar ese segmento por Y=0..10 para barrer la franja intermedia. El barrido pertenece a la envolvente, no a la madera.
- **[TRIGGER_2] — 00:23–00:46:** Encender bordes X=2 y X=8 y bordes largos Y=0,10. Crear rectángulo de envolvente y escribir sus intervalos. Mantener contornos de piezas por encima del relleno para ver el hueco.
- **[TRIGGER_3] — 00:46–01:10:** Mostrar dos inclusiones: envolvente⊆rectángulo porque el rectángulo es convexo y contiene piezas; rectángulo⊆envolvente por las cuatro esquinas extremas y sus combinaciones convexas. Trazar diagonales y bordes, completar igualdad de regiones.
- **[TRIGGER_4] — 01:10–01:36:** Insertar temporalmente tira 3 y luego retirarla: contorno de envolvente queda idéntico y una ficha de masa sale de un contador separado. Retirar ambas tarjetas de prueba y conservar los extremos para la normalización.

- **Duración orientativa:** 01:36. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Madera índigo opaca; envolvente verde al 0.12–0.18; diagonales cian; esquinas activas terracota. No colorear el hueco como una pieza nueva. Texto de inclusiones en TEXT_MAIN.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 05

## Nombre: Elegir unidades que hagan desaparecer el ancho

## Descripcion Breve: Escalar por 2/w convierte centros y bordes en enteros.

## Objetivo Pedagogico: Derivar la normalización y probar que conserva estrictamente la posición respecto del soporte.

## Voz en off:

> “[TRIGGER_1] En las unidades originales, cada bloque mide uno de alto, w de ancho y w por n de largo. La capa ocupa un cuadrado de lado w por n. En la dirección de las tiras, el bloque k va desde k menos uno por w hasta k por w; su centro está en k menos un medio por w.
> [TRIGGER_2] Multipliquemos todas las coordenadas horizontales por dos entre w. Los bordes pasan a dos por k menos uno y dos por k. El centro pasa a dos k menos uno. Así aparecen uno, tres, cinco, hasta dos n menos uno: centros impares entre bordes pares.
> [TRIGGER_3] La mitad del lado largo, w por n entre dos, se convierte en n. Y todo el cuadrado pasa de lado w por n a lado dos n. Como w es positivo, escalar ambos ejes conserva el orden y las desigualdades estrictas: interior, borde y exterior siguen siendo los mismos casos.
> [TRIGGER_4] También el centro de masa escala por ese mismo factor, porque la media de coordenadas escaladas es la escala por la media original. Por eso w deja de participar en las comprobaciones. La altura distingue qué bloques están arriba, pero el criterio utiliza únicamente su proyección horizontal.”

## Descripcion Visual Detallada:

## Objetos:

- Regla original con bordes (k−1)w,kw y centro (k−1/2)w; regla normalizada con bordes 2(k−1),2k y centro 2k−1.
- Flecha ×2/w; MathTex (2/w)·wn=2n, (2/w)·wn/2=n y α·(Σx/C)=Σ(αx)/C para α=2/w>0.
- Tres puntos interior/borde/exterior transformados junto con sus soportes.

## Layout y disposicion:

- Reglas de x=-5.5..5.5 en y=1.5 y -0.4; tres marcas por regla en x=-3,0,3, rotuladas simbólicamente. Factor de escala en (0,0.65,0).
- Cuadrados antes/después en x=-3.2 y 3.2,y=-1.8, lado visual 1.7, con cotas wn y 2n. Identidad de media en y=-3.0; las dimensiones visuales se rotulan como unidades distintas, no como tamaños físicos iguales.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:27:** Crear bloque y regla original; escribir anchura w, longitud wn y altura 1. Marcar ambos bordes y su punto medio con la expresión completa.
- **[TRIGGER_2] — 00:27–00:48:** Aplicar flecha de escala a las tres etiquetas en paralelo y mostrar cancelación de w. Desplegar ejemplo n=5 con centros 1,3,5,7,9 y bordes 0,2,4,6,8,10, todos explícitos.
- **[TRIGGER_3] — 00:48–01:12:** Transformar cotas del cuadrado y punto medio del lado largo. Mostrar un punto interior, uno de borde y uno exterior en una regla auxiliar, transformando soporte y puntos conjuntamente; no escalar sólo el centro.
- **[TRIGGER_4] — 01:12–01:34:** Escribir identidad de la media con factor α y sacar α de la suma. Encerrar w eliminado de las expresiones; trasladar el centro 3D a su proyección y conservar sólo coordenadas X,Y normalizadas.

- **Duración orientativa:** 01:34. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Escala y variables activas terracota, reglas cian. Enteros finales en TEXT_MAIN; cancelación de w verde. Punto en borde conserva vino tras el cambio de unidades: la escala no arregla un fallo.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 06

## Nombre: Capas alternadas, coordenadas alternadas

## Descripcion Breve: La paridad de l decide si 2k−1 aparece en X o en Y.

## Objetivo Pedagogico: Establecer una convención global coherente para centros y eje corto.

## Voz en off:

> “[TRIGGER_1] Numeramos las capas desde abajo. En las impares, las tiras se reparten a lo largo de X y cada una recorre todo Y. El bloque k tiene centro X igual a dos k menos uno y centro Y igual a n.
> [TRIGGER_2] En las capas pares giramos noventa grados: todas las piezas tienen centro X igual a n, mientras su centro Y es dos k menos uno. Para n igual a cinco, una capa impar tiene centros uno, cinco; tres, cinco; cinco, cinco; siete, cinco; nueve, cinco.
> [TRIGGER_3] La capa par tiene cinco, uno; cinco, tres; cinco, cinco; cinco, siete; cinco, nueve. No cambiamos la numeración vertical al girar la orientación, ni cambiamos el significado de la operación l, k: identifica una pieza de una capa concreta.
> [TRIGGER_4] Podríamos intercambiar los nombres X e Y en toda la torre y obtendríamos el mismo algoritmo. Lo esencial es usar una convención global y mantenerla al retirar piezas, actualizar sumas y elegir el eje de soporte. Con estas coordenadas ya podemos escribir el rectángulo usando sólo sus extremos.”

## Descripcion Visual Detallada:

## Objetos:

- Dos planos de n=5 con cinco tiras y centros; fórmulas X(l,k)=2k−1,Y(l,k)=n si l impar; X(l,k)=n,Y(l,k)=2k−1 si l par.
- Diez rótulos de centros completos, cinco por plano; flechas X,Y; etiqueta capas numeradas desde abajo.

## Layout y disposicion:

- Planos centrados en (-3.3,0.25,0) y (3.3,0.25,0), cada uno lado 3.8; mapear coordenadas normalizadas por factor 0.38 alrededor de (5,5).
- Fórmulas de cada panel en y=2.35; rótulos de centro en pequeñas tarjetas externas al plano: usar una tarjeta activa en y=-2.1 y guardar lista de cinco coordenadas en y=-2.85, 25 pt. No superponer diez etiquetas dentro de tiras estrechas.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear plano impar, ejes y cinco tiras; colocar centros (1,5),(3,5),(5,5),(7,5),(9,5). Marcar eje corto X y largo Y, y escribir fórmula de centros.
- **[TRIGGER_2] — 00:19–00:40:** Crear plano par mediante rotación de las formas, recreando sus textos en orientación de lectura. Escribir fórmula correspondiente y mostrar las cinco coordenadas impares del panel izquierdo una a una en su tarjeta externa.
- **[TRIGGER_3] — 00:40–00:59:** Mostrar centros del panel par uno a uno con sus cinco tarjetas; indicar X fijo en cinco y Y variable. Crear una ficha de operación (l,k) y conectarla con identidad de capa y de tira.
- **[TRIGGER_4] — 00:59–01:21:** Intercambiar temporalmente rótulos X/Y en ambos paneles a la vez, junto con las fórmulas, y mostrar invariancia. Restaurar la convención impar→X, par→Y para todas las escenas restantes.

- **Duración orientativa:** 01:21. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Eje X y capas impares índigo; eje Y y capas pares cian. Centros terracota y etiquetas TEXT_MAIN. La rotación afecta formas y coordenadas, pero los textos no quedan girados.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 07

## Nombre: Dos extremos determinan el rectángulo

## Descripcion Breve: L y R fijan el intervalo corto; el intervalo largo conserva 0..2n.

## Objetivo Pedagogico: Derivar bordes exactos y establecer que una capa vacía se trata separadamente.

## Voz en off:

> “[TRIGGER_1] Llamemos L al índice del primer bloque presente y R al del último, en una capa no vacía. El borde izquierdo de la primera tira es el doble del índice anterior a L: dos multiplicado por la diferencia entre L y uno. El borde derecho de la última es dos R. Los paréntesis de la primera expresión son importantes.
> [TRIGGER_2] Por ejemplo, si n es cinco y quedan las tiras tres y cuatro, el soporte corto va de cuatro a ocho. Sus centros están en cinco y siete, pero el soporte lo determinan los bordes, no los centros. Usar cinco y siete como fronteras sería otro criterio.
> [TRIGGER_3] En la dirección larga, cada tira ocupa de cero a dos n. Para una capa impar, el rectángulo es cuatro a ocho en X y cero a diez en Y en este ejemplo. Para una capa par, esos papeles se intercambian: X completo, Y recortado.
> [TRIGGER_4] Si no queda ninguna tira, no existen extremos de soporte que debamos interpretar. Primero preguntaremos si hay masa arriba. Si la hay, una capa vacía falla; si no, ese corte se ignora. Esa decisión tendrá que ocurrir antes de usar L y R.”

## Descripcion Visual Detallada:

## Objetos:

- Fórmulas de rectángulos impares [2(L−1),2R]×[0,2n] y pares [0,2n]×[2(L−1),2R]; interior de cada uno rotulado con intervalos abiertos.
- Ejemplo n=5,L=3,R=4, tiras 3,4 con centros 5,7 y bordes 4,8; compuerta capa no vacía antes de lectura de extremos.

## Layout y disposicion:

- Fila ampliada desde x=-5 a 5,y=0.8, coordenada física X=x+5. Bordes 4 y 8 en x=-1 y 3, centros 5 y 7 en x=0 y 2.
- Dos fórmulas de rectángulo en y=-0.9,-1.9; guardia de capa no vacía en (0,-2.9,0). L,R sobre los bloques en y=2.0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:27:** Crear huecos y tiras con L,R. Escribir 2(L−1) con paréntesis de alto contraste y 2R; mostrar una flecha al borde físico de cada tira. No usar una expresión verbal ambigua como única definición.
- **[TRIGGER_2] — 00:27–00:49:** Sustituir L=3,R=4 y calcular 2(3−1)=4,2·4=8. Marcar centros 5,7 con puntos y bordes 4,8 con líneas; añadir una brace que explique diferencia entre centro y frontera.
- **[TRIGGER_3] — 00:49–01:10:** Expandir fila a vista de plano y escribir rectángulo impar; luego girar su función de soporte para plano par y escribir segundo rectángulo. Mantener abiertos los intervalos usados para estabilidad, aunque se dibuje el contorno cerrado de la envolvente.
- **[TRIGGER_4] — 01:10–01:30:** Retirar ambas tiras en un experimento independiente y apagar L,R como no aplicables. Crear guardia masa superior positiva y soporte vacío; no dibujar un intervalo invertido como soporte válido.

- **Duración orientativa:** 01:30. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Centros terracota, bordes de soporte verde y paréntesis TEXT_MAIN. Ejes X/Y según paleta global. Extremos no aplicables en TEXT_MUTED; capa vacía con carga se marcará vino sólo tras la guardia.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 08

## Nombre: La otra coordenada siempre pasa la prueba

## Descripcion Breve: Toda media de centros permanece en [1,2n−1], interior al intervalo largo.

## Objetivo Pedagogico: Probar por desigualdades que basta revisar un único eje en cada corte.

## Voz en off:

> “[TRIGGER_1] Cada centro de bloque tiene sus dos coordenadas entre uno y dos n menos uno. La coordenada fija n también pertenece a ese intervalo, incluso cuando n vale uno. Si arriba hay C bloques, podemos sumar esas cotas para cualquiera de los dos ejes.
> [TRIGGER_2] Cada coordenada aporta al menos uno y como máximo dos n menos uno. Por tanto la suma S está entre C y dos n menos uno por C. Dividimos entre C, que es positivo, y la media queda entre uno y dos n menos uno.
> [TRIGGER_3] Ahora compárala con los bordes de la dirección larga: cero y dos n. Como uno es mayor que cero y dos n menos uno es menor que dos n, la media está estrictamente dentro. Esto vale aunque falten muchísimos bloques o sus posiciones sean asimétricas.
> [TRIGGER_4] Así que para una capa impar sólo necesitamos revisar X, y para una par sólo Y. No es una aproximación ni estamos olvidando una fuerza lateral: demostramos que la otra desigualdad siempre se cumple bajo el criterio del problema. La envolvente bidimensional se ha reducido a un intervalo.”

## Descripcion Visual Detallada:

## Objetos:

- Recta normalizada con 0,1,n,2n−1,2n; colección de centros y media; MathTex C≤S≤(2n−1)C,1≤S/C≤2n−1 y 0<S/C<2n.
- Dos tarjetas de elección de eje: l impar→X, l par→Y; caso n=1 con centros y media en 1, intervalo largo (0,2).

## Layout y disposicion:

- Recta de x=-5.6 a 5.6 en y=1.2; extremos externos 0,2n y marcas interiores 1,2n−1 se colocan como esquema rotulado no proporcional para n simbólico.
- Cadena de desigualdades en y=0,-1.0,-2.0; elección de eje en x=-3.1 y 3.1,y=-2.9. Caso n=1 sustituye brevemente recta superior.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear intervalo de posibles centros y varias fichas de masa en él. Escribir cota de cada coordenada y marcar n entre los dos límites. Para n=1 colapsar banda de centros a una única marca, conservando bordes 0 y 2.
- **[TRIGGER_2] — 00:21–00:42:** Copiar una unidad mínima por cada ficha para formar C≤S, y un máximo por ficha para S≤(2n−1)C. Transformar a cotas de media usando C>0 como guardia visible.
- **[TRIGGER_3] — 00:42–01:03:** Añadir bordes 0,2n y separar estrictamente la banda interna de ambos. Dibujar el promedio dentro de esa banda sin alterar sus extremos y escribir la conclusión estricta.
- **[TRIGGER_4] — 01:03–01:25:** Transformar rectángulo en intervalo corto y desactivar el chequeo largo con rótulo probado automáticamente. Crear tarjetas de paridad; la reducción sólo aparece después de la demostración, no como una elección arbitraria.

- **Duración orientativa:** 01:25. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Banda de centros terracota, intervalo largo verde y eje que se comprobará cian/índigo. Las desigualdades débiles de centros y estrictas del soporte usan símbolos claramente distintos.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 09

## Nombre: El centro de toda la masa de arriba

## Descripcion Breve: Con masas iguales, el centro se obtiene dividiendo la suma de centros por su cantidad.

## Objetivo Pedagogico: Derivar los tres acumuladores y fijar exactamente qué bloques entran en ellos.

## Voz en off:

> “[TRIGGER_1] La fórmula general del centro de masa pesa cada posición por su masa. Aquí todos los bloques tienen la misma masa b. En X, el numerador es b por X uno, más b por X dos, y así para todos los bloques superiores; el denominador es b por la cantidad C.
> [TRIGGER_2] Sacamos b de la suma y lo cancelamos. Queda la suma de coordenadas X dividida entre C. En Y ocurre lo mismo. Los bloques son uniformes, así que sus posiciones representativas son los centros que ya calculamos.
> [TRIGGER_3] Llamemos S X a esa suma horizontal y S Y a la otra. El centro proyectado es S X entre C, S Y entre C. Sólo necesitamos tres números, aunque la torre superior contenga millones de piezas. Si cambia una pieza, esos números cambian por su contribución exacta.
> [TRIGGER_4] Y la palabra superior sigue siendo esencial: incluimos todos los bloques de las capas por encima de l, no sólo la capa siguiente y no la propia capa l. Si C es cero, la media no se define y tampoco hace falta: el corte no tiene ninguna carga que sostener.”

## Descripcion Visual Detallada:

## Objetos:

- Grupo de bloques superiores con sus centros y fichas de masa b; fórmula (ΣbX_i)/(Cb)→ΣX_i/C y equivalente Y.
- Banco de tres acumuladores C,S_x,S_y; bracket de capas l+1..h y compuerta C>0; punto de centro y su proyección.

## Layout y disposicion:

- Torre esquemática a la izquierda con apoyo en y=-1.8 y tres capas superiores entre y=-0.8 y 1.8, x=-4.8..-1.5. Centros etiquetados en un panel ampliado, no sobre cada cara.
- Fórmulas a la derecha centradas en x=3.0,y=1.2 y 0; banco C,S_x,S_y en x=-3.6,0,3.6,y=-1.9. Guardia en (0,-2.95,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear grupo superior y una ficha de masa igual junto a cada centro. Mostrar suma ponderada completa en forma simbólica con límites de 1 a C, y denominador Cb.
- **[TRIGGER_2] — 00:24–00:42:** Factorizar b en numerador y cancelar con denominador, conservando C>0. Repetir transformación en Y dentro del mismo trigger con ambas expresiones visibles.
- **[TRIGGER_3] — 00:42–01:04:** Agrupar aportes de cada bloque en los tres registros; escribir centro=(S_x/C,S_y/C). Copiar un bloque hacia el registro como delta (1,X,Y), sin retirar la pieza del grupo salvo en una operación específica posterior.
- **[TRIGGER_4] — 01:04–01:27:** Encerrar todos los pisos l+1..h con bracket y dejar capa l fuera. Mostrar C=0 en una segunda maqueta y apagar el punto de centro; no producir divisiones 0/0 ni coordenadas ficticias.

- **Duración orientativa:** 01:27. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- C en verde, S_x índigo y S_y cian; masa común b terracota durante cancelación. Centro terracota, soporte con rótulo independiente. C=0 y punto apagado en TEXT_MUTED.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 10

## Nombre: Promediar capas puede esconder el peso real

## Descripcion Breve: Una capa con tres bloques pesa tres veces lo que una con uno.

## Objetivo Pedagogico: Mostrar por qué se suman momentos y cantidades, en lugar de promediar centros de capas sin ponderación.

## Voz en off:

> “[TRIGGER_1] Tomemos n igual a tres y un corte sobre la capa dos. La capa tres conserva sus tres bloques: todos tienen Y igual a tres, así que aporta cantidad tres y suma Y igual a nueve. La capa cuatro conserva sólo su bloque tres, cuyo centro Y es cinco: aporta cantidad uno y suma cinco.
> [TRIGGER_2] Si promediáramos los centros de las dos capas como si pesaran lo mismo, obtendríamos tres más cinco entre dos: cuatro. Pero la primera tiene tres bloques y la segunda sólo uno. El centro verdadero es nueve más cinco entre cuatro: tres y medio.
> [TRIGGER_3] Podemos verlo colocando tres fichas en la coordenada tres y una en cinco. El punto de equilibrio está más cerca de tres, donde hay más masa. Agrupar por capas es útil siempre que cada grupo conserve su suma y su cantidad.
> [TRIGGER_4] Esta es la razón de nuestros acumuladores. Para combinar capas, sumamos cantidades con cantidades y momentos con momentos. Dividimos una sola vez, si queremos dibujar el centro. El algoritmo ni siquiera necesitará hacer esa división para decidir estabilidad.”

## Descripcion Visual Detallada:

## Objetos:

- Dos capas superiores reales del ejemplo n=3,h=4: capa 3 completa, capa 4 con sólo k=3. Tarjetas (count,sy)=(3,9) y (1,5).
- Recta Y con tres fichas en 3 y una en 5; media de centros sin pesos 4 y centro correcto 14/4=7/2; banco agregado C=4,S_y=14.

## Layout y disposicion:

- Capas en x=-3.5,y=1.35 y -0.4, cada plano de lado 2.1; tarjetas en x=-0.7 junto a ellos. Recta de Y a la derecha, x=1.2..5.8,y=0.65, mapeo y físico a pantalla horizontal x=1.2+0.75Y.
- Comparaciones de medias en (2.9,-1.2,0) y (2.9,-2.15,0); fórmula de agregación en (0,-3.0,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:25:** Crear capas numeradas 3 y 4, marcar su corte inferior l=2. Mostrar centros Y=3 de tres bloques y Y=5 del único superior; llenar dos tarjetas de conteo/suma.
- **[TRIGGER_2] — 00:25–00:45:** Mostrar intento (3+5)/2=4 con rótulo capas sin peso; después sumar cantidades 3+1=4 y momentos 9+5=14, producir 14/4=3.5. Marcar el desacuerdo sin invalidar las coordenadas de cada capa.
- **[TRIGGER_3] — 00:45–01:04:** Colocar tres puntos apilados en Y=3 y uno en Y=5. Mover indicador al centro 3.5 y mostrar distancias ponderadas, si se añaden: 3·(3.5−3)=1·(5−3.5). La igualdad se crea únicamente aquí.
- **[TRIGGER_4] — 01:04–01:22:** Transformar ambas tarjetas en un banco agregado C=4,S_y=14. Rodear suma de capas como operación válida y retirar el cociente, preparando la comparación por productos.

- **Duración orientativa:** 01:22. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Conteos en verde, momentos Y en cian y centro verdadero terracota. Media de capas sin peso con borde vino y rótulo de método incorrecto; centro correcto en TEXT_MAIN.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 11

## Nombre: La frontera se decide con enteros

## Descripcion Breve: Multiplicar por C evita redondeos y conserva la caída por igualdad.

## Objetivo Pedagogico: Derivar la comparación estricta por productos y enumerar izquierda, interior, derecha y exterior.

## Voz en off:

> “[TRIGGER_1] Sea a el borde izquierdo del soporte y b el derecho. Cuando hay C bloques arriba, la estabilidad pide a menor que S entre C, y S entre C menor que b. Como C es positivo, podemos multiplicar ambos lados sin cambiar el sentido: a C menor que S menor que b C.
> [TRIGGER_2] Sustituimos los bordes de nuestras tiras. A la izquierda está el doble de la diferencia entre L y uno, multiplicado por C; a la derecha, dos R multiplicado por C. La suma S debe quedar estrictamente entre ambos. S es la suma X en capas impares y la suma Y en pares. Todas esas cantidades son enteras.
> [TRIGGER_3] Con soporte de cuatro a ocho y tres bloques arriba, las fronteras de la comparación son doce y veinticuatro. Una suma dieciocho da centro seis y pasa. Una suma doce da centro cuatro y cae por el borde izquierdo. Una suma veinticuatro da centro ocho y cae por el derecho.
> [TRIGGER_4] Una suma nueve queda a la izquierda, y veintisiete a la derecha. También fallan. Los cinco casos se distinguen exactamente con las mismas dos desigualdades. No hay que decidir qué tolerancia usar para un decimal cercano al borde: la igualdad entera conserva el caso que el problema considera inestable.”

## Descripcion Visual Detallada:

## Objetos:

- MathTex a<S/C<b ↔ aC<S<bC con guardia C>0; expresión 2(L−1)C<S<2RC.
- Recta con soporte (4,8) y C=3; cinco tarjetas S=18,12,24,9,27 con centros 6,4,8,3,9 y decisiones exactas.

## Layout y disposicion:

- Fórmula de media en (0,2.0,0), productos en (0,0.95,0). Recta x=-5.4..5.4,y=-0.15, coordenadas de centro 3..9 mapeadas por x=1.8(q−6).
- Tarjetas en cinco columnas x=-4.8,-2.4,0,2.4,4.8,y=-1.65; cada una ancho 2.1 y alto 1.8. Desigualdad activa en y=-3.0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear C>0 y expresión con cociente; multiplicar por C mediante transformación alineada de los tres términos. Mostrar la equivalencia como doble flecha, no como una aproximación.
- **[TRIGGER_2] — 00:24–00:50:** Sustituir a=2(L−1),b=2R y seleccionar S_x/S_y mediante una tarjeta de paridad. Resaltar paréntesis y conservar símbolos estrictos <.
- **[TRIGGER_3] — 00:50–01:13:** Fijar soporte y C=3; escribir límites 12,24. Mostrar S=18 en centro interior con 12<18<24. Después S=12 y S=24, uno por uno, con igualdad en el lado correspondiente y decisión de caída.
- **[TRIGGER_4] — 01:13–01:36:** Mostrar S=9 con 12<9 falso y S=27 con 27<24 falso; llenar las cinco tarjetas completas. Cerrar con rótulo aritmética exacta y dejar guardia positiva visible hasta retirar el panel.

- **Duración orientativa:** 01:36. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Interior válido verde y centro terracota; igualdad/exterior que fallan vino. Productos de frontera en TEXT_MAIN, eje relevante cian/índigo. Los dos símbolos < nunca se convierten en ≤.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 12

## Nombre: Cinco datos por capa

## Descripcion Breve: Cantidad, dos sumas y dos extremos sustituyen al recorrido de sus bloques.

## Objetivo Pedagogico: Derivar la inicialización exacta de los agregados y las marcas de retirada.

## Voz en off:

> “[TRIGGER_1] Para cada capa guardamos cantidad de bloques, suma de sus centros X, suma de sus centros Y, extremo izquierdo y extremo derecho. Además, cada posición tiene una marca que recuerda si su bloque fue retirado. No guardamos una geometría nueva después de cada jugada: conservamos sus datos suficientes.
> [TRIGGER_2] Al principio hay n bloques y extremos uno y n. La coordenada variable recorre uno, tres, cinco, hasta dos n menos uno. Sumamos dos k menos uno desde k igual a uno hasta n: dos por n por n más uno entre dos, menos n. El resultado es n al cuadrado.
> [TRIGGER_3] La otra coordenada vale n en cada uno de los n bloques, así que también suma n al cuadrado. Por eso en todas las capas empezamos con ambas sumas iguales, aunque sus orientaciones sean diferentes. Para n igual a cinco, cantidad cinco y sumas veinticinco, veinticinco.
> [TRIGGER_4] Inicializamos todas las marcas como presentes. Los extremos están listos para describir el soporte; las sumas y el conteo, para alimentar la masa de los cortes inferiores. Estos dos usos comparten la capa, pero deben permanecer separados en nuestro dibujo y en el razonamiento.”

## Descripcion Visual Detallada:

## Objetos:

- Banco por capa con campos count,s_x,s_y,L,R; fila de n marcas, presente/retirado; ficha de inicialización (n,n²,n²,1,n).
- MathTex Σ_{k=1}^n(2k−1)=2Σk−n=n(n+1)−n=n²; suma fija Σn=n²; ejemplo n=5 con 1+3+5+7+9=25.

## Layout y disposicion:

- Banco de cinco campos en x=-4.8,-2.4,0,2.4,4.8,y=1.55, cada campo ancho 2.1. Marcas de n=5 en x=-3.6,-1.8,0,1.8,3.6,y=0.1.
- Derivación de suma en y=-1.2 y suma de coordenada fija en y=-2.25; inicialización completa en y=-3.1. Para n simbólico, los extremos de fila llevan brace n y no un número de casillas falsamente completo.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Crear banco y cinco marcas ilustrativas de una capa n=5. Separar flechas de uso: L,R hacia soporte; count,s_x,s_y hacia acumulación. Cada campo tiene rótulo persistente.
- **[TRIGGER_2] — 00:22–00:46:** Crear centros impares 1,3,5,7,9 y escribir suma 25; generalizar mediante las cuatro transformaciones algebraicas de la suma, con límites visibles y paréntesis correctos.
- **[TRIGGER_3] — 00:46–01:08:** Mostrar cinco coordenadas fijas n=5 y total 25. Llenar count=5,s_x=25,s_y=25; alternar orientación de las fichas manteniendo ambos totales, para probar que la inicialización sirve a ambas paridades.
- **[TRIGGER_4] — 01:08–01:29:** Llenar L=1,R=5, poner todas las marcas en presente y escribir la inicialización general. Conservar banco y fila para retirar un bloque en la siguiente escena.

- **Duración orientativa:** 01:29. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- count verde,s_x índigo,s_y cian,L/R con contorno verde. Marcas presentes TEXT_MAIN; futuras retiradas TEXT_MUTED. Sumandos activos terracota.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 13

## Nombre: Una retirada cambia una sola contribución

## Descripcion Breve: Restar (1,X,Y) actualiza exactamente los agregados de la capa afectada.

## Objetivo Pedagogico: Probar la conservación de los datos tras cada operación y la importancia de no repetir bloques.

## Voz en off:

> “[TRIGGER_1] La operación l, k identifica el bloque retirado. Calculamos su centro con la paridad de l, restamos uno de la cantidad y restamos sus coordenadas de las dos sumas. Luego marcamos esa posición como retirada. Todas las demás capas conservan sus datos locales.
> [TRIGGER_2] Probemos n igual a cinco en una capa impar, retirando el bloque dos. Su centro es tres, cinco. La cantidad pasa de cinco a cuatro, suma X de veinticinco a veintidós y suma Y de veinticinco a veinte. Son exactamente los cuatro centros que permanecen.
> [TRIGGER_3] En una capa par, el mismo bloque dos tendría centro cinco, tres. Sus nuevas sumas serían veinte en X y veintidós en Y. La regla es la misma resta de una contribución; la orientación decide las coordenadas que restamos.
> [TRIGGER_4] El enunciado garantiza que las retiradas no repiten piezas. Cada marca cambia una sola vez y nunca descontamos dos veces la misma masa. Tras esta actualización todavía falta ajustar los extremos si quitamos uno de ellos, y volver a comprobar la torre: una modificación local puede afectar muchos cortes inferiores.”

## Descripcion Visual Detallada:

## Objetos:

- Fila de cinco bloques y centro del bloque 2; vector de aporte (1,3,5) para impar y (1,5,3) para par; bancos inicial/final.
- Estados impares (count,sx,sy)=(5,25,25)→(4,22,20); estados pares →(4,20,22); marca eliminada de posición 2.

## Layout y disposicion:

- Fila de bloques x=-4,-2,0,2,4,y=1.5. Banco count,s_x,s_y en x=-3.2,0,3.2,y=-0.2. Tarjeta de aporte en (0,0.7,0).
- Experimentos impar/par se suceden en el mismo panel, con título de paridad en y=2.45. Estado final en y=-1.6 y garantía de retirada única en y=-2.8.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Recrear banco y fila; mover una tarjeta de operación (l,2) hacia su bloque. Mostrar aporte (1,X(l,2),Y(l,2)) y tres flechas de resta al banco; marcar retirada sólo después de descontar.
- **[TRIGGER_2] — 00:20–00:41:** Fijar l impar y n=5, calcular (X,Y)=(3,5); sacar físicamente la ficha 2 de la fila y actualizar 5→4,25→22,25→20. Mostrar centros restantes 1,5,7,9 en X y cuatro veces 5 en Y, validando sumas.
- **[TRIGGER_3] — 00:41–01:00:** Reiniciar como experimento independiente de capa par completa y retirar k=2 con (5,3). Actualizar 5→4,25→20,25→22; no acumular esta segunda retirada sobre el experimento impar.
- **[TRIGGER_4] — 01:00–01:23:** Encerrar la marca de retirada única y mostrar una ficha de operación repetida como caso fuera de la garantía, sin ejecutarla ni descontar. Crear flechas hacia extremos y hacia cortes inferiores para preparar ambos efectos.

- **Duración orientativa:** 01:23. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Bloque activo terracota, marca retirada TEXT_MUTED. Restas en colores de sus campos; resultados exactos TEXT_MAIN. Operación repetida fuera del dominio con borde vino, presentada sólo como explicación de la garantía.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 14

## Nombre: Los extremos caminan sobre las marcas

## Descripcion Breve: L avanza y R retrocede hasta encontrar la primera y última pieza presentes.

## Objetivo Pedagogico: Derivar la actualización protegida de extremos y su movimiento monótono.

## Voz en off:

> “[TRIGGER_1] Los huecos internos no cambian los extremos mientras quede una pieza más allá de ellos. En cinco posiciones, retiramos primero dos y tres. L sigue en uno y R en cinco. Las marcas recuerdan los dos huecos aunque todavía no afectan el borde.
> [TRIGGER_2] Ahora retiramos uno. L estaba allí y debe avanzar: cruza uno, cruza dos, cruza tres y se detiene en cuatro, que está presente. R permanece en cinco. Las piezas restantes son cuatro y cinco, y sus extremos son exactamente cuatro y cinco.
> [TRIGGER_3] Retiramos cinco. R retrocede hasta cuatro. Finalmente retiramos cuatro: la cantidad llega a cero y ya no hay pieza donde detenerse. El recorrido protegido deja L mayor que R; no consultamos una posición fuera de la región ni usamos estos extremos como un soporte válido.
> [TRIGGER_4] L sólo avanza y R sólo retrocede. Una marca eliminada puede ser sobrepasada por cada extremo como máximo una vez. Esos saltos no se repiten desde el principio en cada retirada. Esta monotonicidad de los punteros será útil para el costo; no es una afirmación sobre la monotonicidad de la estabilidad.”

## Descripcion Visual Detallada:

## Objetos:

- Cinco marcas y punteros L/R; operaciones 2,3,1,5,4, todas en una misma capa. Estados de extremos (1,5),(1,5),(4,5),(4,4),vacío.
- Guardia L≤R antes de consultar marca; estado final L=5,R=4,count=0 según avance izquierdo primero; contadores de cruces de marcas.

## Layout y disposicion:

- Marcas en x=-4,-2,0,2,4,y=0.7; puntero L encima en y=1.6 y R debajo en y=-0.2. Índices en y=0.1 sin ocupar la punta del puntero inferior.
- Operaciones en fila y=2.45; banco L,R,count en x=-3.5,0,3.5,y=-1.5. Guardia en (0,-2.75,0). Posición exterior de L=5 en esta convención se rotula índice 5 sobre un hueco ya retirado; no crear una nueva pieza.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear fila completa, retirar 2 y luego 3 con marcas, mostrar L=1,R=5 después de cada una. Registrar que no se desplaza ningún extremo.
- **[TRIGGER_2] — 00:20–00:40:** Retirar 1 y mover L sucesivamente por índices 1→2→3→4 con un pulso por marca cruzada. Detenerlo sólo en 4 presente; actualizar banco a L=4,R=5.
- **[TRIGGER_3] — 00:40–01:01:** Retirar 5 y mover R 5→4. Retirar 4 y, con guardia L≤R, mover L 4→5, obteniendo L>R y count=0. Cerrar guardia antes de cualquier lectura siguiente; apagar extremos como no aplicables.
- **[TRIGGER_4] — 01:01–01:25:** Reproducir en un carril de historial sólo los caminos ya hechos, cada uno orientado hacia dentro. Mostrar límite una pasada por marca y extremo. Añadir rótulo punteros monótonos y conservarlo separado de la etiqueta estabilidad, que aún no se ha analizado globalmente.

- **Duración orientativa:** 01:25. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Punteros cian, marca activa terracota, retiradas TEXT_MUTED. Guardia válida verde y estado vacío neutral. No declarar caída sólo porque L>R.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 15

## Nombre: Quitar una pieza interna sigue cambiando la torre

## Descripcion Breve: El soporte de una capa puede quedar igual mientras cambia su contribución de masa.

## Objetivo Pedagogico: Mostrar que los extremos no sustituyen a las sumas y que retirar un bloque central puede conservar el promedio.

## Voz en off:

> “[TRIGGER_1] Volvamos a una capa impar completa de cinco bloques. Retiramos el bloque dos, cuyo centro X es tres. Los extremos siguen siendo uno y cinco: la envolvente todavía ocupa de cero a diez. Pero la suma X baja de veinticinco a veintidós, y la cantidad de cinco a cuatro.
> [TRIGGER_2] El centro de esa capa pasa de cinco a veintidós entre cuatro, cinco y medio. Ese cambio alimentará el centro de toda la masa que vean los cortes inferiores. Un soporte sin cambios no significa que toda la torre conserve su misma carga.
> [TRIGGER_3] Si en cambio retiramos el bloque central, con X igual a cinco, la nueva suma es veinte y la cantidad cuatro: el promedio sigue siendo cinco. Los agregados sí cambiaron, aunque el cociente no. Esto ocurrirá en la cuarta retirada de nuestro ejemplo principal.
> [TRIGGER_4] Por eso guardamos ambas clases de información. Los extremos describen lo que una capa puede sostener; las sumas y la cantidad describen lo que esa capa aporta a quienes están debajo. Una misma retirada tiene esos dos efectos, y cada corte utilizará sólo el que le corresponde.”

## Descripcion Visual Detallada:

## Objetos:

- Dos experimentos independientes n=5 sobre una capa impar: retirar k=2 o retirar k=3. Intervalo de soporte (0,10) idéntico en ambos.
- Registros 25/5=5→22/4=5.5 y 25/5=5→20/4=5; flechas de contribución hacia capas inferiores.

## Layout y disposicion:

- Fila de cinco centros en x=-4,-2,0,2,4,y=1.0; eje físico X=1,3,5,7,9. Soporte completo en y=0.15, longitud 10.
- Bancos de experimento en x=-3.0 y 3.0,y=-1.5, ancho 5.2. Centro del primer experimento en x=0.5 para X=5.5 bajo el mapeo x=X−5; centro inicial en x=0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:23:** Crear capa completa, marcar centro cinco y retirar k=2. Mantener L=1,R=5 y banda soporte sin transformar; actualizar suma y conteo.
- **[TRIGGER_2] — 00:23–00:43:** Transformar cociente 25/5 a 22/4 y mover punto del centro a 5.5. Copiar el delta de masa hacia un bracket pisos inferiores, sin actualizar una torre no especificada.
- **[TRIGGER_3] — 00:43–01:04:** Reiniciar la fila completa en el segundo experimento y retirar k=3. Actualizar suma a veinte y cantidad a cuatro; mantener punto en cinco y escribir igualdad de promedios. No superponer ambos experimentos como dos retiradas sucesivas.
- **[TRIGGER_4] — 01:04–01:26:** Crear dos canales de salida de una capa: extremos→soporte propio y (count,sx,sy)→carga de cortes inferiores. Encerrar ambos como datos necesarios y retirar filas para el recorrido vertical.

- **Duración orientativa:** 01:26. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Soporte verde persistente, sumas X índigo y conteo verde con rótulo diferenciado. Centro terracota. Retiradas neutras: desplazar el centro no implica por sí mismo una caída.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 16

## Nombre: Leer la torre desde arriba

## Descripcion Breve: Antes de comprobar l, los acumuladores contienen exactamente las capas l+1..h.

## Objetivo Pedagogico: Probar y visualizar el invariante del barrido vertical y el orden comprobar–agregar.

## Voz en off:

> “[TRIGGER_1] Para revisar todos los cortes, bajamos desde la cima. Antes de comprobar la capa h, los acumuladores están en cero: no hay ninguna capa por encima. Por tanto ese primer corte no falla. Después agregamos las contribuciones de la capa h.
> [TRIGGER_2] Al llegar a h menos uno, el banco ya representa exactamente la capa superior. Comprobamos si esa carga cabe en su soporte. Sólo después agregamos la capa h menos uno. Así, al llegar a h menos dos, el banco reúne las dos capas superiores.
> [TRIGGER_3] La regla se repite con una identidad precisa: antes de revisar l, cantidad C y sumas S X, S Y describen las capas l más uno hasta h. Al terminar esa comprobación, sumamos los datos de l y el banco queda listo para revisar l menos uno.
> [TRIGGER_4] No reiniciamos una suma completa para cada corte. Cada capa entra una sola vez en el banco durante este recorrido. Y el orden importa: comprobar primero, agregar después. Si agregamos el propio soporte antes de comprobarlo, incluiremos masa que no pertenece a la carga superior.”

## Descripcion Visual Detallada:

## Objetos:

- Torre esquemática h=4 con tarjetas por capa v_l=(count_l,sx_l,sy_l); banco global (C,S_x,S_y); cursor vertical y bracket superior.
- Historial antes de cortes: l=4 banco 0; l=3 banco v_4; l=2 banco v_4+v_3; l=1 banco v_4+v_3+v_2.
- Dos estaciones comprobar l y agregar v_l conectadas en ese orden; fórmula de invariante (C,S_x,S_y)=Σ_{r=l+1}^h v_r.

## Layout y disposicion:

- Tarjetas de capa a la izquierda en x=-3.8,y=1.8,0.7,-0.4,-1.5 para 4,3,2,1. Banco a la derecha en (3.0,0.6,0), tamaño 5.5×1.5.
- Estaciones comprobar y agregar en (-1.0,-2.6,0) y (2.5,-2.6,0); invariante en (2.7,2.15,0). Flechas entre tarjetas y banco cruzan sólo corredor x=-1.5..0.5.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear cuatro tarjetas y banco cero. Cursor en capa 4, mostrar carga superior vacía y pasar comprobación. Luego mover una copia de v_4 al banco; original permanece como datos locales.
- **[TRIGGER_2] — 00:19–00:40:** Cursor a 3, bracket sólo sobre 4. Mostrar banco v_4 y estación comprobar; al completar, sumar v_3. Cursor a 2 y bracket sobre 3,4, mostrar suma de dos capas.
- **[TRIGGER_3] — 00:40–01:02:** Escribir invariante con límites completos. Comprobar 2, sumar v_2, avanzar a 1 y mostrar v_4+v_3+v_2. Comprobar 1 y añadir v_1 al final sólo como estado de recorrido terminado; ya no hay corte inferior que revisar.
- **[TRIGGER_4] — 01:02–01:23:** Crear las dos estaciones con flecha obligatoria comprobar→agregar. Intentar visualmente intercambiarlas mediante una flecha de experimento con borde vino y detenerla, preparando el contraejemplo numérico de la escena siguiente.

- **Duración orientativa:** 01:23. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Datos locales en índigo/cian; banco con campos rotulados. Cursor terracota, carga superior con bracket cian; estación comprobar verde. Agregar una capa no borra sus datos locales.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 17

## Nombre: Incluir el soporte puede esconder una caída

## Descripcion Breve: Una configuración n=2,h=2 falla por borde, pero el promedio con su propio apoyo aparenta estabilidad.

## Objetivo Pedagogico: Demostrar con números por qué el invariante vertical excluye la capa comprobada.

## Voz en off:

> “[TRIGGER_1] Veamos qué saldría mal. Hay dos capas y dos bloques por capa. Retiramos el bloque uno de la capa inferior. Sólo queda su bloque dos, cuyo soporte X va de dos a cuatro. La capa superior es par: ambos bloques tienen X igual a dos.
> [TRIGGER_2] La carga verdadera tiene cantidad dos y suma X cuatro. Su centro es cuatro entre dos, igual a dos: exactamente el borde izquierdo. El criterio dice caída. La comparación entera exige cuatro menor que cuatro, y eso es falso.
> [TRIGGER_3] Ahora cometamos el error de sumar también el bloque de apoyo. Su centro X es tres. La cantidad aparente pasa a tres y la suma a siete. El promedio siete tercios queda entre dos y cuatro. El dibujo diría estable, pero hemos cambiado la masa que la capa debía sostener.
> [TRIGGER_4] No es un detalle de redondeo. Es una selección incorrecta de objetos. El bloque de apoyo no puede mejorar artificialmente el centro de la carga poniéndose a sí mismo en el promedio. Nuestra secuencia comprobar y luego agregar impide exactamente ese error.”

## Descripcion Visual Detallada:

## Objetos:

- Torre n=2,h=2 tras retirar (1,1); soporte inferior X∈(2,4), bloque restante centro X=3; dos centros superiores X=2.
- Banco correcto C=2,S_x=4 y banco incorrecto C=3,S_x=7; cocientes 2 y 7/3; comparaciones 4<4<8 y 6<7<12.

## Layout y disposicion:

- Torre n=2,h=2 a la izquierda con P(X,Y,z)=(-3.6+0.30(X−2)−0.30(Y−2),−1.3+0.10(X−2)+0.10(Y−2)+0.80z,0). Regla de X en panel derecho: x=1.2+1.0q,y=0.8 para q=0..4.
- Bancos correcto e incorrecto en (2.9,-0.6,0) y (2.9,-1.9,0), ancho 5.3. Criterio de pertenencia en y=-3.0.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear configuración y retirar (1,1). Marcar soporte de bloque 2 entre 2 y 4; agrupar sólo los dos bloques superiores como carga.
- **[TRIGGER_2] — 00:21–00:40:** Llenar banco correcto con dos y cuatro; colocar centro en 2 y escribir 2C=4=S_x. Marcar igualdad y caída por borde; ambas desigualdades siguen visibles.
- **[TRIGGER_3] — 00:40–01:03:** Abrir panel de experimento incorrecto, añadir centro 3 del apoyo al banco y calcular 7/3. Colocar punto aparente dentro del mismo soporte y mostrar 6<7<12 con rótulo masa equivocada, no una nueva decisión válida.
- **[TRIGGER_4] — 01:03–01:23:** Retirar punto aparente y banco incorrecto; devolver apoyo a su rol de soporte. Conservar orden comprobar→agregar y sello carga estrictamente superior. No alterar ni corregir una copia de J.cpp.

- **Duración orientativa:** 01:23. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Carga correcta con bracket cian; centro verdadero en borde vino. Punto aparente terracota con marco vino de método incorrecto, aunque su desigualdad geométrica sea cierta. Apoyo índigo permanece fuera del banco.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 18

## Nombre: Tres ramas antes de cualquier desigualdad

## Descripcion Breve: Sin carga se omite el corte; con carga y sin soporte falla; en otro caso se prueban los productos.

## Objetivo Pedagogico: Dar el algoritmo completo de comprobación en un diagrama de decisiones.

## Voz en off:

> “[TRIGGER_1] Ya podemos describir la revisión de una capa con tres ramas. Primera pregunta: ¿hay bloques por encima? Si C es cero, el corte no falla y no calculamos ningún centro. Después agregamos la capa y seguimos bajando.
> [TRIGGER_2] Si C es positivo, preguntamos si queda alguna pieza en el soporte. Si su cantidad es cero, falla: existe una carga y no hay región que la sostenga. Aquí tampoco consultamos extremos ni dividimos nada.
> [TRIGGER_3] Si hay carga y soporte, elegimos X para capa impar o Y para par. Formamos los productos del borde izquierdo y del derecho por C. El corte pasa únicamente si la suma relevante queda estrictamente entre ellos. Si pasa, agregamos los datos locales y continuamos.
> [TRIGGER_4] Tras una retirada actualizamos su capa, ajustamos sus extremos y ejecutamos este descenso. Si falla cualquier corte, registramos ese número de operación. Si todos pasan, procesamos la siguiente retirada. Son los mismos tres casos para todas las capas, incluidas las vacías y la cima.”

## Descripcion Visual Detallada:

## Objetos:

- Diagrama de decisiones con nodos C=0?,count_l=0?,paridad,producto izquierdo<S<producto derecho; terminales corte pasa y configuración falla.
- Estación agregar capa l sólo en ramas que continúan; ciclo de operaciones actualizar→ajustar extremos→revisar cortes→siguiente o respuesta.

## Layout y disposicion:

- Diagrama vertical en x=-2.2, nodos y=2.1,0.8,-0.55; ramas pasa a x=-5.2 y falla a x=1.0. Estación agregar en (-2.2,-2.3,0).
- Ciclo de operación a la derecha en x=3.9, estaciones y=1.8,0.65,-0.5,-1.65. Ancho de cada tarjeta ≤3.4; flechas no atraviesan otros textos.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:18:** Crear primer rombo y rama C=0 hacia corte pasa, conectada a agregar. Mostrar que esta rama no entra al cálculo de extremos.
- **[TRIGGER_2] — 00:18–00:35:** Crear segundo rombo sólo sobre rama C>0. count_l=0 lleva a falla; count_l>0 continúa. Mantener ambas condiciones encima de la rama de fallo vacío.
- **[TRIGGER_3] — 00:35–00:56:** Crear selector de paridad y tarjeta 2(L−1)C<S<2RC con S elegido. Abrir ramas falla y pasa, y conectar sólo pasa a agregar. Mostrar descenso l→l−1 tras la agregación.
- **[TRIGGER_4] — 00:56–01:17:** Crear ciclo de operación completo y conectar cualquier falla con contador de primera retirada. No usar un bloque de código o pseudocódigo; cada estación es una acción sobre datos con flechas. Retirar diagrama tras lectura y preparar torre oficial.

- **Duración orientativa:** 01:17. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Ramas válidas verde, decisiones índigo/cian, fallo vino. C=0 neutro; retirada activa terracota. Soporte vacío sólo se colorea como fallo después de comprobar C>0.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 19

## Nombre: La torre del ejemplo: seis capas de cinco bloques

## Descripcion Breve: El ejemplo oficial comienza con n=5,w=2,h=6 y foco en el corte sobre capa 4.

## Objetivo Pedagogico: Preparar todas las coordenadas, masas y soportes que se usarán en las cinco retiradas.

## Voz en off:

> “[TRIGGER_1] Pasemos al primer ejemplo oficial. Hay cinco bloques por capa, ancho dos y seis capas. Usaremos nuestras coordenadas normalizadas: el cuadrado va de cero a diez y los centros variables son uno, tres, cinco, siete y nueve.
> [TRIGGER_2] Vamos a seguir especialmente la capa cuatro. Es par, así que su intervalo corto está en Y. Al principio L es uno y R cinco: soporte de cero a diez. Arriba están las capas cinco y seis, con cinco bloques cada una.
> [TRIGGER_3] Cada capa completa aporta suma Y veinticinco. En la cinco, Y es fijo en cinco; en la seis, recorre uno, tres, cinco, siete y nueve. Juntas tienen cantidad diez y suma cincuenta. Su centro Y es cinco, en el interior del soporte.
> [TRIGGER_4] Las retiradas que vamos a comprobar son cuatro, uno; cuatro, dos; cuatro, cinco; cinco, tres; y cuatro, tres. No sabemos todavía cuál fallará. Conservaremos dos paneles: lo que queda del soporte en la capa cuatro y lo que pesa por encima de ella. Así veremos por qué dos jugadas diferentes pueden afectar cosas diferentes.”

## Descripcion Visual Detallada:

## Objetos:

- Torre oficial completa n=5,h=6 con 30 bloques; w=2 anotado como parámetro normalizado. Cinco tarjetas de operaciones (4,1),(4,2),(4,5),(5,3),(4,3).
- Detalle del soporte capa 4 con índices 1..5; banco superior C=10,S_x=50,S_y=50; centro proyectado Y=5 y banda (0,10).

## Layout y disposicion:

- Torre con proyección P(X,Y,z)=(-3.4+0.20(X−5)−0.20(Y−5),−2.1+0.06(X−5)+0.06(Y−5)+0.55z,0), X,Y∈[0,10],z∈[0,6]. Cada bloque ocupa z∈[l−1,l].
- Detalle de capa 4 a la derecha: coordenada Y=q se muestra en x=1.15+0.45q; tiras de anchura 0.9, centradas en Y=1,3,5,7,9 e y=0.35, altura visual 0.6. Índices en y=-0.2.
- Centro Y=5 en (3.4,1.15,0) con línea vertical al soporte. Banco superior en (3.4,2.15,0), ancho 5.4,alto 0.75. Comparación en (3.4,-1.35,0); tarjetas de operaciones en fila y=-2.85.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:18:** Limpiar diagrama anterior y construir torre completa con identidad estable de sus 30 piezas. Crear ejes normalizados y rótulo n=5,w=2,h=6. Los futuros huecos conservan su posición sin una pieza semitransparente que parezca masa presente.
- **[TRIGGER_2] — 00:18–00:38:** Resaltar capa 4 con un contorno y selector eje Y. Abrir detalle de sus cinco tiras, marcar L=1,R=5 y banda de soporte (0,10).
- **[TRIGGER_3] — 00:38–00:58:** Crear bracket de carga capas 5,6; mostrar aportes Y=25+25 y C=5+5. Llenar banco superior y poner punto Y=5, con comparación 0<50<100. Las sumas de capa 4 se muestran en un registro local separado si se necesitan.
- **[TRIGGER_4] — 00:58–01:23:** Crear las cinco tarjetas de operación en su orden exacto, sin etiqueta de fallo. Cursor antes de la primera. Mantener torre, detalle y banco como estado compartido para escenas 20–24.

- **Duración orientativa:** 01:23. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Capas impares índigo y pares cian; capa 4 resaltada con borde verde, carga superior con bracket TEXT_MAIN. Centro terracota, futuras operaciones neutras; no anticipar la quinta en rojo.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 20

## Nombre: Retirada uno: se mueve el borde izquierdo

## Descripcion Breve: Quitar (4,1) deja soporte (2,10) y conserva C=10,S_y=50.

## Objetivo Pedagogico: Ejecutar la primera actualización y la comprobación exacta sin alterar la carga superior.

## Voz en off:

> “[TRIGGER_1] Primera retirada: bloque uno de la capa cuatro. Su centro es X igual a cinco, Y igual a uno. Sale del soporte, y sus datos locales cambian: quedan cuatro bloques, suma X veinte y suma Y veinticuatro.
> [TRIGGER_2] El extremo izquierdo avanza de uno a dos; el derecho sigue en cinco. El nuevo intervalo Y es de dos a diez. Pero este bloque no pertenecía a la carga por encima de cuatro: arriba siguen los diez bloques y suma Y cincuenta.
> [TRIGGER_3] El centro superior continúa en cinco. Multiplicamos las fronteras por diez: veinte menor que cincuenta menor que cien. El corte sobre cuatro sigue estable. No confundimos el cambio de masa local de cuatro con el banco de su carga superior.
> [TRIGGER_4] La capa cinco conserva soporte completo y sostiene la seis; las capas inferiores a cuatro también conservan sus soportes completos. Cualquier centro de carga permanece dentro de ese cuadrado completo por la cota que demostramos. Ningún corte falla en la primera retirada, así que avanzamos a la segunda.”

## Descripcion Visual Detallada:

## Objetos:

- Estado heredado completo; pieza (4,1), banco local de capa4 (5,25,25)→(4,20,24); L=2,R=5; banco superior invariable (10,50,50).
- Banda (2,10), punto Y=5; MathTex 2·10<50<10·10 →20<50<100; columna de cortes 6,5,4,3,2,1 con estado pasa/sin carga.

## Layout y disposicion:

- Conservar P y coordenadas del detalle de escena19. Ficha k=1 ocupa x=1.6,y=0.35; nueva frontera izquierda en x=2.05 para Y=2.
- Banco local temporal en (-3.4,-2.9,0), ancho 5.3; banco superior permanece en (3.4,2.15,0). Columna de cortes, si se muestra, usa x=-6.0 con cifras en y=1.4,0.8,0.2,-0.4,-1.0,-1.6.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:18:** Recrear estado19 si se renderiza por separado. Activar tarjeta paso1, sacar bloque (4,1) y su ficha del detalle; marcar hueco. Restar (1,5,1) sólo al banco local de cuatro.
- **[TRIGGER_2] — 00:18–00:38:** Mover puntero L de 1 a 2 y banda izquierda de Y=0 a Y=2; R no se mueve. Encerrar banco superior y mostrar que no cambia: C=10,S_y=50.
- **[TRIGGER_3] — 00:38–00:57:** Mantener punto en Y=5; escribir los dos productos y simplificar a 20<50<100. Cerrar sello corte4 pasa sin borrar la desigualdad antes del hold.
- **[TRIGGER_4] — 00:57–01:19:** Mostrar corte6 sin carga; corte5 con soporte completo y cortes3,2,1 completos, cada uno con rótulo dentro por cota de centros. Marcar todos sin fallo y mover cursor a paso2. Los datos locales retirados sí se incorporarán a bancos inferiores en el recorrido.

- **Duración orientativa:** 01:19. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Retirada terracota y hueco TEXT_MUTED; nueva frontera verde. Banco superior con contorno cian invariable, datos locales de cuatro con etiqueta explícita. Todos los cortes válidos en verde, cima sin carga neutral.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 21

## Nombre: Retirada dos: el margen se estrecha

## Descripcion Breve: Quitar (4,2) deja L=3,R=5 y soporte (4,10).

## Objetivo Pedagogico: Mostrar que el centro sigue fijo mientras cambia exclusivamente el intervalo de apoyo.

## Voz en off:

> “[TRIGGER_1] Segunda retirada: bloque dos de la capa cuatro. Su centro Y es tres, y X sigue en cinco. La capa pasa a tres bloques, suma X quince y suma Y veintiuno. Los presentes son tres, cuatro y cinco.
> [TRIGGER_2] L avanza a tres. Calculamos el borde izquierdo como dos por la diferencia entre tres y uno: cuatro. El derecho sigue en diez. Arriba no retiramos nada: cantidad diez y suma Y cincuenta, centro cinco.
> [TRIGGER_3] La prueba ahora pide cuarenta menor que cincuenta menor que cien. Pasa, pero el centro quedó mucho más cerca del borde izquierdo. Ese margen visual no reemplaza la desigualdad: la decisión sigue siendo estricta y exacta.
> [TRIGGER_4] Los demás soportes siguen completos. La pérdida de masa de la capa cuatro cambia los bancos de cortes inferiores, pero todos sus centros siguen entre los bordes cero y diez. La segunda operación también deja estable toda la torre.”

## Descripcion Visual Detallada:

## Objetos:

- Estado tras paso1; retirada (4,2); banco local (4,20,24)→(3,15,21); presentes {3,4,5}; L=3,R=5.
- Banda (4,10), centro Y=5, banco superior (10,50,50); desigualdad 40<50<100 y margen corto entre 4 y 5.

## Layout y disposicion:

- Mantener composición principal. Ficha k=2 en x=2.5,y=0.35; nueva frontera izquierda Y=4 en x=2.95, centro sigue x=3.4.
- Banco local y columna de cortes en posiciones de escena20; comparación en (3.4,-1.35,0). Llave de margen 4..5 se coloca en y=0.85 sin tocar el punto superior.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:18:** Recrear estado final paso1. Activar paso2 y retirar bloque (4,2); restar (1,5,3) al banco local y marcar presentes 3,4,5.
- **[TRIGGER_2] — 00:18–00:35:** Mover L=2→3 y borde Y=2→4; escribir 2(3−1)=4 y mantener R=5. Mostrar banco superior sin modificaciones.
- **[TRIGGER_3] — 00:35–00:52:** Escribir 4·10=40 y 10·10=100; comprobar 40<50<100. Crear breve llave entre borde4 y centro5 con rótulo margen positivo, sin redondear ni cambiar centro.
- **[TRIGGER_4] — 00:52–01:11:** Reactivar cortes restantes con soporte completo y cota automática; registrar paso2 estable. Retirar la llave de margen durante este trigger y mantener estado para retirada3.

- **Duración orientativa:** 01:11. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Capa4 cian, frontera verde y centro terracota. Margen con línea fina TEXT_MAIN; banco superior constante con borde cian. Ningún acercamiento al borde se colorea como caída antes de igualdad o exterior.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 22

## Nombre: Retirada tres: también se mueve el borde derecho

## Descripcion Breve: Quitar (4,5) deja presentes 3 y 4 y soporte (4,8).

## Objetivo Pedagogico: Actualizar ambos extremos a lo largo de la traza y confirmar estabilidad del intervalo reducido.

## Voz en off:

> “[TRIGGER_1] Tercera retirada: el bloque cinco de la capa cuatro. Sus coordenadas son cinco, nueve. La cantidad local baja a dos, suma X a diez y suma Y a doce. Quedan los bloques tres y cuatro.
> [TRIGGER_2] El extremo derecho retrocede de cinco a cuatro. Su borde pasa de diez a ocho; el izquierdo sigue en cuatro. La envolvente es el rectángulo completo en X y recortado entre cuatro y ocho en Y.
> [TRIGGER_3] La carga superior todavía tiene diez bloques y suma Y cincuenta. La comparación es cuarenta menor que cincuenta menor que ochenta. El centro cinco sigue dentro, aunque la capa perdió tres de sus cinco piezas originales.
> [TRIGGER_4] Otra vez pasan los demás cortes, que conservan soporte completo. Hemos retirado desde ambos lados, y el conteo de piezas disminuyó mucho, pero el criterio responde a su ubicación y a la carga superior. La tercera retirada todavía es segura dentro del modelo.”

## Descripcion Visual Detallada:

## Objetos:

- Estado tras paso2; retirada (4,5); banco local (3,15,21)→(2,10,12); presentes {3,4}; L=3,R=4.
- Banda (4,8), centro5; productos 4·10=40,8·10=80; resultado exacto 40<50<80.

## Layout y disposicion:

- Mantener P y detalle. Ficha k=5 en x=5.2,y=0.35; frontera derecha nueva Y=8 en x=4.75. L=3 en x=3.4 para centro de su bloque, R=4 en x=4.3.
- Rectángulo de soporte en torre se dibuja sobre capa4 con Y∈[4,8],X∈[0,10]. Comparación en y=-1.35 y estado paso3 en y=-2.2.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:17:** Recrear paso2; activar tarjeta3, retirar bloque (4,5) y restar (1,5,9) al banco local. Mostrar sus sumas finales completas.
- **[TRIGGER_2] — 00:17–00:34:** Mover R=5→4, borde derecho10→8 y conservar L=3. Dibujar rectángulo de envolvente sobre capa4 y banda corta del detalle con sus dos bordes.
- **[TRIGGER_3] — 00:34–00:51:** Conservar banco superior diez/cincuenta, escribir 40<50<80 y marcar centro cinco interior. Mostrar dos piezas presentes como información local, sin usarlas como peso de la carga superior.
- **[TRIGGER_4] — 00:51–01:11:** Recorrer la columna de cortes restantes completos con sus estados válidos. Guardar resultado paso3 estable y dejar huecos 1,2,5 visibles. No restaurar esas piezas al comenzar la siguiente escena.

- **Duración orientativa:** 01:11. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Soporte reducido verde, orientación par cian y huecos TEXT_MUTED. Centro terracota. Cantidad local dos y superior diez llevan rótulos completos para evitar intercambio.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 23

## Nombre: Retirada cuatro: cambia la carga, no el soporte

## Descripcion Breve: Quitar (5,3) reduce la carga de capa4 a C=9,S_y=45 y conserva el centro5.

## Objetivo Pedagogico: Contrastar una retirada superior con las tres retiradas de apoyo y mostrar una media invariable.

## Voz en off:

> “[TRIGGER_1] La cuarta retirada es distinta: bloque tres de la capa cinco. Esta capa es impar, y la pieza central tiene coordenadas cinco, cinco. Quitamos una parte de la carga que sostiene cuatro; no tocamos ninguna de sus dos piezas de apoyo.
> [TRIGGER_2] La capa cinco queda con cuatro bloques y sumas veinte, veinte. La seis sigue con cinco y sumas veinticinco, veinticinco. Por encima de cuatro tenemos ahora cantidad nueve y sumas cuarenta y cinco en ambos ejes.
> [TRIGGER_3] El centro Y es cuarenta y cinco entre nueve: sigue siendo cinco. Retiramos una pieza situada justamente en el centro anterior; al reducir suma y cantidad en la misma proporción, el promedio no se mueve. El soporte de cuatro continúa entre cuatro y ocho.
> [TRIGGER_4] Multiplicamos ahora por nueve, no por diez. Treinta y seis menor que cuarenta y cinco menor que setenta y dos. Pasa. La capa cinco conserva sus extremos uno y cinco pese al hueco central, y los cortes inferiores tienen soporte completo. La cuarta retirada tampoco causa caída.”

## Descripcion Visual Detallada:

## Objetos:

- Estado tras paso3; pieza (5,3); banco local capa5 (5,25,25)→(4,20,20), L=1,R=5; banco local capa4 invariable (2,10,12).
- Banco superior de cuatro (10,50,50)→(9,45,45); centro Y 50/10=45/9=5; desigualdad 36<45<72; soporte (4,8).

## Layout y disposicion:

- Mantener detalle de capa4 y su punto. En torre, resaltar pieza central de capa5 y su posición P(5,5,z) para z∈[4,5]; no convertir su altura en dato requerido del algoritmo.
- Banco local de cinco aparece en (-3.4,-2.9,0). Banco superior de cuatro cambia en (3.4,2.15,0); igualdad de promedios en (3.4,-0.65,0), productos en y=-1.6.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Recrear paso3; activar tarjeta4 y retirar (5,3). Mostrar aporte (1,5,5) y banco de capa5 actualizado. Mantener piezas 3,4 de capa4 sin transformaciones.
- **[TRIGGER_2] — 00:19–00:36:** Sumar aportes de capas5 y6: C=4+5=9,S_x=20+25=45,S_y=20+25=45. Transformar banco superior de cuatro a esos tres valores.
- **[TRIGGER_3] — 00:36–00:57:** Mostrar 50/10=5 y 45/9=5; mantener punto fijo en el detalle mientras cambian los números. Eliminar una ficha situada en el promedio de una recta auxiliar y comprobar el mismo efecto.
- **[TRIGGER_4] — 00:57–01:19:** Escribir 4·9=36,8·9=72 y desigualdad. Marcar capa5 con hueco interno pero extremos intactos, revisar sus carga/corte y restantes soportes completos. Guardar paso4 estable y preparar sólo la quinta retirada.

- **Duración orientativa:** 01:19. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Retirada superior terracota; banco de carga con campos verdes/índigo/cian según tipo. Centro fijo terracota, soporte verde. Hueco central de capa5 neutro; ninguna etiqueta lo confunde con capa vacía.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 24

## Nombre: Retirada cinco: el soporte deja atrás al centro

## Descripcion Breve: Quitar (4,3) deja sólo bloque4, soporte (6,8), y falla 54<45.

## Objetivo Pedagogico: Mostrar el primer fallo exacto y producir yes/5 con causa geométrica explícita.

## Voz en off:

> “[TRIGGER_1] Quinta retirada: bloque tres de la capa cuatro. Su centro es cinco, cinco. Sale otra pieza de apoyo y queda sólo el bloque cuatro, con centro cinco, siete. La cantidad local es uno, suma X cinco y suma Y siete.
> [TRIGGER_2] L avanza de tres a cuatro y R ya era cuatro. El soporte Y queda entre seis y ocho. La carga superior no cambia: nueve bloques, suma Y cuarenta y cinco, centro cinco. Esta vez el borde izquierdo se mueve a la derecha del centro.
> [TRIGGER_3] La comparación pide seis por nueve menor que cuarenta y cinco, y cuarenta y cinco menor que ocho por nueve. Es decir, cincuenta y cuatro menor que cuarenta y cinco menor que setenta y dos. La primera desigualdad es falsa. El centro está fuera, a la izquierda del soporte.
> [TRIGGER_4] Basta este corte para declarar inestabilidad. Las primeras cuatro retiradas fueron estables y la quinta falla, así que la respuesta es yes y cinco. No esperaremos a otra jugada ni buscaremos qué pasaría después de la caída: ya encontramos el primer instante que pedía el problema.”

## Descripcion Visual Detallada:

## Objetos:

- Estado tras paso4; retirada (4,3); banco local capa4 (2,10,12)→(1,5,7); L=R=4; único bloque k4.
- Banco superior (9,45,45), soporte Y∈(6,8), centro5; desigualdad 54<45<72 con primera relación falsa; salida Tex yes y MathTex 5 en líneas separadas.

## Layout y disposicion:

- Mantener P y detalle: ficha k3 en x=3.4 sale; k4 permanece x=4.3. Nueva frontera Y=6 en x=3.85; punto Y=5 permanece x=3.4 y queda fuera de la banda.
- Comparación en (3.4,-1.35,0), salida en (3.4,-2.4,0). Tarjeta5 se resalta en fila de operaciones, sin añadir una sexta retirada.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Recrear paso4; activar tarjeta5 y retirar (4,3), restar (1,5,5) al banco local. Confirmar único bloque presente4 y sus sumas (1,5,7).
- **[TRIGGER_2] — 00:19–00:40:** Mover L=3→4 y frontera Y=4→6, mantener R=4 y frontera8. Banco superior y punto no cambian. Resaltar que soporte sí se transforma y carga no.
- **[TRIGGER_3] — 00:40–01:03:** Mostrar productos 6·9=54,8·9=72. Escribir relación izquierda 54<45 en rojo con rótulo falsa; relación derecha45<72 permanece válida. Colocar una flecha desde punto5 a región exterior sin hacer moverse el punto.
- **[TRIGGER_4] — 01:03–01:25:** Marcar corte4 falla, conservar pasos1..4 como válidos y encerrar paso5. Crear salida yes en primera línea y5 en segunda. Congelar configuración geométrica: no animar una trayectoria física arbitraria de colapso como resultado calculado.

- **Duración orientativa:** 01:25. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Fallo real en ACCENT_VINO sobre frontera y comparación; centro terracota conserva posición. Salida TEXT_MAIN y número5 terracota. Bloques retirados neutros, no rojos; la causa es el corte.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 25

## Nombre: Auditar los seis cortes del ejemplo

## Descripcion Breve: Los bancos completos muestran qué carga corresponde a cada capa antes y después del fallo.

## Objetivo Pedagogico: Enumerar el recorrido vertical real y comprobar que la conclusión no depende de mirar sólo capa4.

## Voz en off:

> “[TRIGGER_1] Comprobemos el estado de la cuarta retirada con el recorrido completo. Antes de capa seis el banco está vacío. Antes de cinco contiene la seis: cantidad cinco y sumas veinticinco, veinticinco. Antes de cuatro reúne cinco y seis: cantidad nueve y sumas cuarenta y cinco, cuarenta y cinco.
> [TRIGGER_2] Agregamos las dos piezas de cuatro, con sumas diez y doce. Antes de tres hay once bloques, suma X cincuenta y cinco y suma Y cincuenta y siete. Agregamos la capa tres completa: antes de dos, dieciséis bloques y sumas ochenta, ochenta y dos. Agregamos la dos: antes de uno, veintiún bloques y sumas ciento cinco, ciento siete.
> [TRIGGER_3] En cinco se comprueba X, en cuatro Y, en tres X, en dos Y y en uno X. Para las capas con soporte completo, las pruebas son cero menor que veinticinco menor que cincuenta; cero menor que cincuenta y cinco menor que ciento diez; cero menor que ochenta y dos menor que ciento sesenta; y cero menor que ciento cinco menor que doscientos diez. Cuatro usa treinta y seis menor que cuarenta y cinco menor que setenta y dos. Todas pasan.
> [TRIGGER_4] Después de la quinta retirada, antes de cuatro el banco sigue siendo nueve, cuarenta y cinco, cuarenta y cinco, pero su soporte pasó a seis, ocho y falla. Si sólo para auditar siguiéramos sumando hacia abajo, los bancos serían diez, cincuenta, cincuenta y dos; quince, setenta y cinco, setenta y siete; veinte, cien, ciento dos. Sus soportes completos pasan. El algoritmo puede detener la comprobación en el primer corte fallido porque un fallo basta.”

## Descripcion Visual Detallada:

## Objetos:

- Tabla completa tras paso4, columnas l,C,Sx,Sy,eje y prueba: 6:(0,0,0),sin carga; 5:(5,25,25),X,0<25<50; 4:(9,45,45),Y,36<45<72; 3:(11,55,57),X,0<55<110; 2:(16,80,82),Y,0<82<160; 1:(21,105,107),X,0<105<210.
- Tabla tras paso5: 6:(0,0,0),sin carga; 5:(5,25,25),X,0<25<50; 4:(9,45,45),Y,54<45<72 falla; 3:(10,50,52),X,0<50<100; 2:(15,75,77),Y,0<77<150; 1:(20,100,102),X,0<100<200.
- Nota visual: las filas inferiores a4 después de hallar el fallo son una auditoría hipotética del mismo estado geométrico, no una continuación de retiradas ni una simulación de torre caída.

## Layout y disposicion:

- Tabla ancho12.1, cabecera y=2.45, seis filas y=1.65,0.95,0.25,-0.45,-1.15,-1.85. Columnas l=-5.65,C=-4.35,Sx=-2.85,Sy=-1.3,eje=0.25,prueba=3.5.
- Texto de datos 25–26 pt y prueba 26 pt; tabla paso4 y paso5 se muestran sucesivamente en la misma posición. Rótulo comprobar antes de agregar en y=-2.95; no colocar toda la torre junto a la tabla.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Crear tabla paso4 con filas vacías; llenar6, luego5 y luego4 mediante sumas de aportes que aparecen brevemente a la derecha. Para cada fila, encender banco antes de la comprobación.
- **[TRIGGER_2] — 00:22–00:48:** Completar filas3,2,1 con tres adiciones explícitas: (9,45,45)+(2,10,12)=(11,55,57), luego +(5,25,25)=(16,80,82), luego +(5,25,25)=(21,105,107). Cada aporte se añade después de comprobar su propia capa.
- **[TRIGGER_3] — 00:48–01:24:** Completar las seis decisiones:6 sin carga;5 prueba X;4 prueba Y;3 X;2 Y;1 X, en ese orden. Encerrar todos los resultados válidos y conservar tabla completa para lectura.
- **[TRIGGER_4] — 01:24–01:57:** Transformar a tabla paso5 y resaltar fila4 fallida. Mostrar parada válida en esa fila. Bajo rótulo auditoría geométrica, completar filas3,2,1 y sus tres desigualdades de soporte completo. El resultado yes/5 permanece fijado aunque estas otras filas pasen.

- **Duración orientativa:** 01:57. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Columnas Sx índigo y Sy cian, C verde. Fila activa terracota, pruebas válidas TEXT_MAIN con sello verde; fila4 fallida vino. Filas auditadas después del fallo con fondo tenue y rótulo explícito.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 26

## Nombre: Por qué estas comprobaciones son suficientes

## Descripcion Breve: Los invariantes de datos y del recorrido enlazan la geometría exacta con la primera operación fallida.

## Objetivo Pedagogico: Dar una demostración completa por mantenimiento, barrido, equivalencia del criterio y cronología.

## Voz en off:

> “[TRIGGER_1] Primero, los datos locales son exactos al comienzo: contamos todas las piezas y sumamos sus centros. Cada retirada elimina una sola contribución y su marca. Los punteros se detienen en la primera y la última posición presentes, o reconocen que la capa está vacía. Por inducción, esos datos siguen describiendo exactamente la configuración.
> [TRIGGER_2] Segundo, el recorrido vertical empieza sin capas superiores. Antes de comprobar l, su banco contiene justamente las capas l más uno hasta h. Agregar l después de comprobarla conserva la misma afirmación para l menos uno. Por inducción, cada corte recibe exactamente su carga, sin piezas de más ni de menos.
> [TRIGGER_3] Tercero, cada decisión coincide con la regla geométrica: sin carga no hay fallo; con carga y sin soporte hay fallo. Con ambos presentes, la envolvente es el rectángulo de los extremos; el eje largo siempre pasa y el corto pasa exactamente cuando se cumplen los productos estrictos. Son equivalencias, así que no rechazamos un corte válido ni aceptamos uno inválido.
> [TRIGGER_4] Por último, procesamos las retiradas en su orden. Antes de anunciar un índice comprobamos todas las operaciones anteriores como estables, y en esa operación encontramos al menos un corte inestable. Por tanto es el primer instante. Si acabamos la lista sin ningún fallo, la respuesta no también queda demostrada.”

## Descripcion Visual Detallada:

## Objetos:

- Cuatro tarjetas de prueba: datos locales exactos, carga superior exacta, equivalencia geométrica, primera operación. Flechas de dependencia entre ellas.
- Base e inducción de marcas/sumas, base e inducción de barrido y línea de tiempo de operaciones con prefijo estable y primer fallo.

## Layout y disposicion:

- Tarjetas en cuadrícula: centros (-3.15,1.2,0),(3.15,1.2,0),(-3.15,-1.1,0),(3.15,-1.1,0); tamaño5.5×1.8.
- Dentro de cada tarjeta, título 28pt, dos diagramas/igualdades breves de26pt; cronología final sustituye fila inferior en y=-1.1. Conclusión en (0,-3.0,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:24:** Crear primera tarjeta con estado inicial y flecha de resta (1,X,Y); añadir marcas y extremos como testigos de conservación. Dibujar transición estado exacto→estado exacto tras retirada.
- **[TRIGGER_2] — 00:24–00:48:** Crear segunda tarjeta con banco0 en cima y fórmula Σ_{r=l+1}^h v_r. Mostrar adición v_l después del chequeo y cambio de límite al siguiente corte.
- **[TRIGGER_3] — 00:48–01:15:** Crear tercera tarjeta y enlazar sus tres ramas con las regiones geométricas. Transformar interior rectangular a intervalo y luego a productos mediante dobles flechas, conservando C>0 como condición.
- **[TRIGGER_4] — 01:15–01:38:** Crear cronología con operaciones1..k−1 válidas y k fallida. Mostrar índice k como certificado de primer instante; en un segundo carril sin fallos mostrar no. Cerrar las cuatro tarjetas y sostener lectura antes de retirarlas.

- **Duración orientativa:** 01:38. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Pruebas válidas verde; datos índigo/cian y paso k terracota. Fallo verdadero vino. Las flechas dobles de equivalencia y simples de actualización se distinguen por forma y rótulo.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 27

## Nombre: Una geometría estable después no borra la primera caída

## Descripcion Breve: La secuencia abstracta n=2,h=3 produce estable, inestable por borde y estable otra vez.

## Objetivo Pedagogico: Probar la ausencia de monotonicidad que impide buscar binariamente el primer fallo.

## Voz en off:

> “[TRIGGER_1] Hay una tentación: buscar la primera caída con búsqueda binaria. Eso exigiría que, una vez inestable una configuración, todas las configuraciones posteriores de la lista también fueran inestables. La caída física ya ocurrió, pero esa propiedad de la geometría abstracta no está garantizada.
> [TRIGGER_2] Tomemos dos bloques por capa y tres capas. Retiramos el bloque uno de la capa inferior. Su soporte X queda entre dos y cuatro. Arriba hay cuatro bloques con suma X ocho: el centro es dos, justo en el borde. La primera retirada causa caída.
> [TRIGGER_3] Sólo como experimento geométrico, continuemos retirando el bloque uno de la capa superior de esa misma configuración. Los centros X que quedan arriba son dos, dos y tres. Cantidad tres, suma siete, centro siete tercios. Está estrictamente entre dos y cuatro: seis menor que siete menor que doce.
> [TRIGGER_4] El otro corte también pasa: la capa intermedia tiene soporte Y completo de cero a cuatro y la única pieza superior tiene Y igual a dos. La cima no tiene carga. La geometría final parecería estable, aunque la primera retirada ya provocó la caída. Estable, inestable, estable: no hay una frontera monótona para buscar. Revisamos cronológicamente y conservamos el primer fallo.”

## Descripcion Visual Detallada:

## Objetos:

- Torre n=2,h=3, estados inicial, tras (1,1), tras retirada hipotética (3,1); soporte inferior X∈(2,4).
- Bancos superiores inferior: (C,Sx)=(4,8)→(3,7); pruebas 8<8<16 falla y6<7<12 pasa. Corte2 Y con C=1,Sy=2,0<2<4; corte3 sin carga.
- Cronología de predicado geométrico true,false,true; tarjeta primera caída=1 que no se modifica; rótulo experimento abstracto posterior a la caída.

## Layout y disposicion:

- Tres paneles secuenciales en x_j=-4.2,0,4.2,y=0.6, cada uno ancho3.6 y alto3.5. Miniaturas n=2,h=3 con P_j(X,Y,z)=(x_j+0.27(X−2)−0.27(Y−2),−0.8+0.08(X−2)+0.08(Y−2)+0.60z,0); reglas de soporte debajo en y=-1.4.
- Cronología de estabilidad en y=-2.35; respuesta primera caída1 en y=-3.15. Rótulo de experimento sobre tercer panel en y=2.3, a dos líneas de24pt.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear torre inicial y tarjeta requisito de búsqueda binaria: falso debe persistir. Mantener predicado del estado geométrico separado del historial ya cayó.
- **[TRIGGER_2] — 00:20–00:41:** Crear segundo panel tras (1,1), sumar centros2,2,1,3 y escribir8/4=2. Marcar punto en borde, predicadofalse y respuesta1.
- **[TRIGGER_3] — 00:41–01:03:** Crear tercer panel con etiqueta experimento abstracto, retirar (3,1) sin animar una torre que se recompone físicamente. Mostrar centros2,2,3 y prueba6<7<12; sólo el predicado geométrico cambia a true.
- **[TRIGGER_4] — 01:03–01:31:** Comprobar corte2 con0<2<4 y cima sin carga. Dibujar secuencia true→false→true, tachar requisito monótono y mantener respuesta1. Retirar tercer panel como experimento, no como continuación válida de una torre que no cayó.

- **Duración orientativa:** 01:31. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Predicado válido verde, fallo por borde vino, historial primera caída terracota. Panel hipotético con contorno punteado TEXT_MUTED y rótulo visible en todo momento.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 28

## Nombre: Una capa vacía sólo falla si sostiene algo

## Descripcion Breve: Tres configuraciones mínimas distinguen vacío sin carga de vacío con carga.

## Objetivo Pedagogico: Exponer y corregir en el razonamiento la discrepancia del archivo adjunto sin modificarlo.

## Voz en off:

> “[TRIGGER_1] Considera la torre más pequeña: una capa con un solo bloque. Lo retiramos. La capa queda vacía, pero no hay ninguna masa por encima ni otro corte que sostener. El criterio correcto da no. Vacío no significa por sí solo caída.
> [TRIGGER_2] Con un bloque por capa y dos capas, retiramos el bloque superior. La pieza inferior sigue sobre el suelo. Encima de la capa vacía no queda nada; encima de la inferior tampoco. La respuesta vuelve a ser no.
> [TRIGGER_3] Ahora hay tres capas de un bloque y quitamos la pieza intermedia. Sigue habiendo un bloque en la cima, pero no hay soporte en la capa dos. Aquí sí cae: cantidad superior positiva y soporte vacío. La respuesta es yes y uno.
> [TRIGGER_4] El análisis de la carpeta documenta que la copia J.cpp declara caída al vaciar cualquier capa antes de preguntar si hay masa encima. Por eso devuelve yes y uno en el primer contraejemplo, mientras la regla del enunciado y la referencia del jurado dan no. El arreglo conceptual es situar la pregunta sobre carga primero, y comprobar el soporte vacío sólo en su rama positiva. La geometría, no la procedencia de un archivo, decide qué condición debemos demostrar.”

## Descripcion Visual Detallada:

## Objetos:

- Tres torres mínimas n=1 con h=1,2,3 y retiradas (1,1),(2,1),(2,1); resultados no,no,yes/1.
- Diagrama correcto C>0?→count_l=0? frente a regla incompleta capa vacía→caída; tarjetas de resultados de copia adjunta y criterio/jurado para h=n=1.
- Nota de producción: el contraejemplo tiene n=w=h=m=1 y una única retirada(1,1), válido según la fuente. No mostrar bloques de código ni alterar J.cpp; se comunica la discrepancia ya documentada en guion_sol.md.

## Layout y disposicion:

- Torres de n=1 en x_j=-4.1,0,4.1, base y=-1.6. Cada bloque de capa l es un Rectangle de ancho0.8,alto0.65,centro(x_j,−1.6+0.65(l−0.5),0); es una elevación esquemática. Salidas en y=-2.5 y parámetros en y=1.7.
- Para comparar reglas, retirar torres y colocar dos paneles en x=-3.1,3.1,y=0.7,ancho5.5; árbol correcto en panel derecho, condición incompleta en izquierdo. Explicación de discrepancia en y=-2.2.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear torre de un bloque, retirarlo y marcar C=0 sobre la capa; mostrar no. La desaparición de la pieza es la retirada solicitada, no una animación de caída secundaria.
- **[TRIGGER_2] — 00:19–00:37:** Crear torre de dos bloques, retirar el superior; recorrer capa2 C=0 y capa1 C=0, mostrar pieza inferior presente y no. Dejar la primera configuración visible como referencia.
- **[TRIGGER_3] — 00:37–00:57:** Crear torre de tres bloques y retirar el intermedio; marcar C=1 en corte2 y count2=0. Mostrar yes y1, contrastando condiciones exactas con los casos anteriores.
- **[TRIGGER_4] — 00:57–01:32:** Retirar miniaturas y crear dos reglas mediante diagramas. Mostrar discrepancia de resultados para primer caso: copiayes/1 frente a criteriono. Trasladar condición soporte vacío bajo C>0 en el diagrama correcto, sin representar una edición del código original ni afirmar una nueva prueba externa del jurado.

- **Duración orientativa:** 01:32. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Vacío sin carga TEXT_MUTED y salidas no verdes; soporte vacío con carga vino. Archivo adjunto y criterio se identifican con rótulos, no con colores de autoridad. Condición correcta verde, fallo conceptual vino.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 29

## Nombre: Mirar sólo la capa vecina también engaña

## Descripcion Breve: Una capa superior adicional desplaza el centro de borde2 a7/3.

## Objetivo Pedagogico: Demostrar la necesidad de incluir toda la torre superior en una configuración alcanzada sin caída previa.

## Voz en off:

> “[TRIGGER_1] Otro error sería calcular sólo el centro de la capa inmediatamente superior. Usemos dos bloques por capa y tres capas, pero ahora cambiemos el orden de las retiradas: primero quitamos el bloque uno de la cima y después el bloque uno de la base.
> [TRIGGER_2] La primera retirada deja estable la torre: la capa intermedia conserva su soporte completo. En la segunda, la base queda con soporte X entre dos y cuatro. La capa vecina tiene dos bloques, ambos con X igual a dos. Si sólo la miramos, su centro dos toca el borde y parecería que cae.
> [TRIGGER_3] Pero también está la pieza que queda en la cima, con X igual a tres. La carga completa contiene los centros dos, dos y tres: su promedio es siete tercios. Cumple seis menor que siete menor que doce. La base sí pasa. En la capa intermedia, el centro Y de la pieza superior es dos, dentro de cero a cuatro.
> [TRIGGER_4] No estamos recuperando una torre después de una caída: estas dos retiradas, en este orden, mantienen la estabilidad. Lo que falló fue el diagnóstico basado sólo en el vecino. Cada bloque estrictamente superior cuenta, aunque haya varias capas entre él y el corte. Por eso sumamos desde arriba y conservamos el banco completo.”

## Descripcion Visual Detallada:

## Objetos:

- Torre n=2,h=3, operaciones (3,1) y(1,1) en ese orden; estados ambos estables. Soporte base X∈(2,4).
- Comparación carga vecina C=2,Sx=4,centro2 frente a carga completa C=3,Sx=7,centro7/3; prueba6<7<12. Corte2 Y:0<2<4.

## Layout y disposicion:

- Torre n=2,h=3 a la izquierda con P(X,Y,z)=(-3.6+0.30(X−2)−0.30(Y−2),−1.5+0.10(X−2)+0.10(Y−2)+0.75z,0); tarjetas de operación en y=2.3. Dos bancos de diagnóstico a la derecha en (3.1,1.05,0),(3.1,-0.75,0), ancho5.5.
- Regla de soporte en y=-2.1, x=1.0+1.1q para q=0..4. Resultado torre estable en(0,-3.1,0).

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Crear torre completa y ejecutar (3,1), mostrando capa2 con soporte completo y banco de cima de un bloque. Sellar primera retirada estable; luego activar tarjeta(1,1).
- **[TRIGGER_2] — 00:21–00:45:** Retirar bloque inferior1 y dibujar soporte(2,4). Abrir diagnóstico vecino con sólo capa2, mostrar promedio2 y rótulo carga incompleta. No fijar respuesta de caída basándose en ese panel.
- **[TRIGGER_3] — 00:45–01:12:** Agregar la pieza de capa3 al segundo banco, obtenerC3,Sx7 y centro7/3. Escribir productos6<7<12 y comprobar corte2 Y con centro2. Mostrar cima sin carga; todos los cortes pasan.
- **[TRIGGER_4] — 01:12–01:36:** Cerrar panel vecino como método incorrecto, mantener resultado estable y orden de retiradas visible. Un bracket abraza capas2,3 como carga completa; conectarlo con invariante del barrido vertical.

- **Duración orientativa:** 01:36. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Carga incompleta con marco vino, carga completa cian y resultado verde. Centros terracota, piezas conservan orientación. No colorear el estado geométrico como inestable porque el panel incorrecto lo sugiera.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 30

## Nombre: Contar trabajo: una pasada por capa, no por bloque

## Descripcion Breve: La matriz se inicializa en O(hn) y las revisiones cuestan O(mh).

## Objetivo Pedagogico: Derivar el costo total, incluidos los saltos amortizados de extremos, y contrastar los intentos ingenuos.

## Voz en off:

> “[TRIGGER_1] El método ingenuo volvería a inspeccionar todos los bloques después de cada retirada. Con los máximos, cinco mil retiradas por cinco mil capas por diez mil posiciones da doscientos cincuenta mil millones de inspecciones. Si además recomputamos cada torre superior por separado, repetimos todavía más sumas.
> [TRIGGER_2] Nuestra inicialización de marcas recorre h por n posiciones una vez: orden de h n. Los datos por capa se inicializan con fórmulas. En cada retirada restamos una contribución en tiempo constante y recorremos como máximo h capas, con un número fijo de operaciones por corte.
> [TRIGGER_3] Aparte están los punteros de extremos. L nunca retrocede y R nunca avanza. Cada marca eliminada se cruza como máximo una vez por extremo; como hay m retiradas distintas, el trabajo total de estos desplazamientos es orden de m, y también queda acotado por orden de h n. No multiplicamos todos esos cruces por el número de revisiones.
> [TRIGGER_4] Sumamos inicialización y recorridos: orden de h n más m h. En el peor tamaño son cincuenta millones de marcas inicializadas y veinticinco millones de comprobaciones de capas. Podemos detener un recorrido al hallar un fallo y detener el análisis geométrico después de la primera caída. Esta cota describe el algoritmo; no demuestra que sea el único método posible ni el óptimo asintótico.”

## Descripcion Visual Detallada:

## Objetos:

- Comparación O(mhn) y O(mh²n) simbólicas; producto5000·5000·10000=2.5·10^11.
- Tres carriles de costo: inicializar hn, revisar mh, cruces de extremos≤2m; fórmula O(hn+mh). Barras de50 millones y25 millones rotuladas como cantidades de operaciones diferentes.
- Nota de producción: un fallo puede acortar el trabajo real; las cotas se refieren al peor caso. La fuente no proporciona un límite oficial de tiempo/memoria, así que no añadirlo.

## Layout y disposicion:

- Panel ingenuo en(-3.2,1.3,0),panel eficiente en(3.2,1.3,0),ancho5.7. Carriles de costos en y=-0.2,-1.25,-2.3; conclusión en y=-3.1.
- Punteros se representan en fila de cinco marcas, ancho4.0, sólo al explicar amortización, reemplazando carril de cifras para conservar legibilidad.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:22:** Crear tres grupos m,h,n y multiplicarlos, escribir cifra completa2.5·10^11. Mostrar anidación de cortes superiores como motivo del costo aún mayor, sin desarrollar un algoritmo ajeno.
- **[TRIGGER_2] — 00:22–00:44:** Crear carril de inicialización con brace hn y carril de revisión con m grupos de h, usando rótulos de multiplicidad. Marcar resta local como una sola ficha de costo por retirada.
- **[TRIGGER_3] — 00:44–01:10:** Recuperar trayectoria de extremos de escena14; poner una ficha de costo por marca cruzada y extremo, máximo dos por retirada. Encerrar suma total≤2m y explicar que no hay reinicio de punteros.
- **[TRIGGER_4] — 01:10–01:39:** Transformar suma de costos en O(hn+mh), sustituir máximos por50·10^6 y25·10^6, manteniendo etiquetas inicialización y comprobaciones. Mostrar parada temprana como ahorro posible, sin afirmar una cota inferior de optimalidad.

- **Duración orientativa:** 01:39. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Costos ingenuos inviables con borde vino; carriles eficientes índigo/cian y cotas verdes. O(hn) no se marca como defecto: es la inicialización de la representación elegida.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 31

## Nombre: La memoria recuerda huecos, no una física completa

## Descripcion Breve: Las marcas dominan O(hn+h); los agregados ocupan O(h).

## Objetivo Pedagogico: Explicar las opciones de representación y las cifras concretas de la copia sin confundirlas con requisitos del enunciado.

## Voz en off:

> “[TRIGGER_1] Las marcas forman una matriz de h capas por n posiciones. Los cinco campos de cada capa y el banco del recorrido añaden una cantidad proporcional a h, más unos pocos acumuladores. La memoria total es orden de h n más h.
> [TRIGGER_2] La copia adjunta reserva cinco mil uno por diez mil uno marcas: cincuenta millones quince mil una posiciones. Si cada booleano ocupa un byte, eso son aproximadamente cuarenta y siete coma siete mebibytes. Es la reserva concreta del archivo, no una cantidad de bloques que se retiran.
> [TRIGGER_3] Una representación por bits puede guardar ocho marcas en un byte y reducir esa parte aproximadamente por ocho. También podría guardarse sólo el conjunto de retiradas de cada capa: la cantidad de información sería orden de h más m, a cambio de operaciones de consulta y mantenimiento de conjuntos.
> [TRIGGER_4] Para comprender esta solución no necesitamos esa alternativa. La matriz hace explícitas las consultas de presencia y los saltos de extremos. Los agregados son pequeños; y no guardamos todos los centros de cada bloque porque sus coordenadas se reconstruyen con l, k y la paridad.”

## Descripcion Visual Detallada:

## Objetos:

- Matriz de marcas representada por6×5 para ejemplo y braces h,n; cinco arreglos por capa y banco global; MathTex O(hn+h).
- Reserva concreta5001·10001=50015001; conversión/2^20≈47.7 MiB con un byte por bool; grupo de8 marcas en byte; alternativa dispersa O(h+m) rotulada con costos de consulta.
- Nota técnica: no prometer un mismo tiempo O(1) de consulta para cualquier conjunto disperso; es una alternativa de espacio y sus costos dependen de la estructura. No se implementa en esta entrega.

## Layout y disposicion:

- Matriz ilustrativa centrada en(-3.5,0.4,0),celdas0.45,6filas×5columnas. Agregados a la derecha en(3.0,1.2,0),ancho5.2.
- Cifra de reserva y conversión en y=-1.5,-2.3. Opciones de almacenamiento sustituyen esos rótulos con dos paneles en x=-3.1,3.1,y=-1.65. Fórmula espacial en y=-3.1.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:20:** Crear matriz de ejemplo con huecos exactos del paso4 y añadir braces h,n. Crear cinco bancos por capa y un banco global; escribir O(hn+h).
- **[TRIGGER_2] — 00:20–00:42:** Crear cálculo de reserva concreta y dividir por1048576 para unidades MiB. Mostrar condición un byte por booleano, evitando etiquetar esa cifra como memoria oficial garantizada para todas las plataformas.
- **[TRIGGER_3] — 00:42–01:05:** Agrupar ocho marcas en una celda byte con ocho casillas de bit; mostrar factor aproximado ocho. En otro panel, representar listas de retiradas por capa y brace totalm, con etiqueta consultas mediante conjuntos.
- **[TRIGGER_4] — 01:05–01:26:** Atenuar alternativas y recuperar matriz como diseño explicado. Mostrar función simbólica centro(l,k) para una pieza sin un banco individual de coordenadas; conectar paridad con suma local y memoria suficiente.

- **Duración orientativa:** 01:26. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Marcas presentes TEXT_MAIN y retiradas TEXT_MUTED; matriz índigo, agregados cian/verde. Opciones de espacio válidas sin rojo; cifras de capacidad terracota.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 32

## Nombre: Exactitud también significa usar enteros suficientemente grandes

## Descripcion Breve: Los productos pueden alcanzar 10^12 y deben calcularse con capacidad de64 bits desde el comienzo.

## Objetivo Pedagogico: Derivar los límites numéricos y proteger tanto las sumas como las multiplicaciones de fronteras.

## Voz en off:

> “[TRIGGER_1] Eliminar los decimales no basta si luego el entero se desborda. La cantidad de bloques por encima de un corte puede llegar a h por n, como máximo cincuenta millones. Cada frontera normalizada es como máximo dos n, veinte mil.
> [TRIGGER_2] Su producto puede llegar a veinte mil por cincuenta millones: un billón, diez elevado a doce. Las sumas de coordenadas también están acotadas por la cantidad de bloques multiplicada por la mayor coordenada. Son magnitudes que exceden la capacidad de un entero de treinta y dos bits.
> [TRIGGER_3] Por eso las sumas acumuladas y los productos se calculan con enteros de sesenta y cuatro bits. La multiplicación debe tener esa capacidad desde su primer paso; guardar después en una caja grande un resultado que ya se desbordó no repara la cuenta.
> [TRIGGER_4] Con esa capacidad, nuestras comparaciones siguen siendo exactas. Estar en el borde es igualdad, fuera es una desigualdad falsa y dentro son dos desigualdades verdaderas. No cambiamos los signos por comodidad y no introducimos tolerancias que conviertan una caída real en estabilidad.”

## Descripcion Visual Detallada:

## Objetos:

- MathTex C≤hn≤5·10^7,2n≤2·10^4,2nC≤10^12; S_x,S_y≤(2n−1)C<10^12 para C>0.
- Dos cajas de capacidad32bits y64bits; rótulo máximo entero con signo32bits2^31−1=2147483647; tubería de producto ancho desde inicio frente a resultado truncado almacenado después.
- Nota: no mostrar sintaxis como2LL ni bloques C++; el storyboard expresa la promoción de capacidad como un diagrama de operación. El archivo fuente contiene la forma concreta para implementación posterior.

## Layout y disposicion:

- Tres cotas superiores en y=2.1,1.15,0.2; producto principal ancho máximo11.6. Cajas32/64en(-3.1,-1.45,0),(3.1,-1.45,0),tamaño5.5×1.6.
- Tubería de multiplicación sustituye cajas al tercer trigger; control de signos en y=-2.95. Todas las cifras largas se agrupan mediante espacios LaTeX, sin abreviaturas decimales ambiguas.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear factores máximos C y2n mediante dos tarjetas; escribir sus cotas a partir de h≤5000,n≤10000. Mantener variables etiquetadas como fronteras y conteo.
- **[TRIGGER_2] — 00:19–00:41:** Multiplicar20000·50000000=1000000000000 y transformar a10^12. Crear cota de sumas y comparar con2^31−1; resaltar capacidad insuficiente de32bits, no un caso geométrico incorrecto.
- **[TRIGGER_3] — 00:41–01:01:** Crear producto que opera en una caja ancha64bits desde sus entradas. En un experimento paralelo, una caja32bits pierde representación antes de pasar a64; rotular resultado dañado y retirar experimento. No inventar un número concreto de desbordamiento dependiente de lenguaje.
- **[TRIGGER_4] — 01:01–01:21:** Recuperar igualdad de borde y pruebas enteras de escena11, con capacidades ya suficientes. Sellar comparaciones exactas y conservar los dos signos< como último recordatorio técnico antes de verificar.

- **Duración orientativa:** 01:21. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Capacidad suficiente verde, insuficiente vino; números activos terracota, sumas índigo/cian. Igualdad de borde en vino por el criterio físico del problema, separada del aviso de capacidad.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 33

## Nombre: Comprobar con otra forma de mirar la misma torre

## Descripcion Breve: Un verificador pequeño reconstruye centros y soportes desde las piezas presentes.

## Objetivo Pedagogico: Diseñar una verificación independiente que contraste cada prefijo y la primera operación fallida.

## Voz en off:

> “[TRIGGER_1] Una comprobación útil no debe repetir a ciegas nuestras mismas actualizaciones. Para torres pequeñas podemos conservar la lista de piezas presentes y, después de cada retirada, reconstruir desde cero la masa sobre cada corte, con sus coordenadas y su centro.
> [TRIGGER_2] También reconstruimos los extremos del soporte desde las piezas que quedan en la capa, en lugar de confiar en los punteros mantenidos. Aplicamos la definición de envolvente y la comparación exacta. Este método lento es manejable en ejemplos pequeños y sirve para contrastar el método rápido.
> [TRIGGER_3] Debemos incluir casos que separen ideas: una sola capa, vaciar la cima, vaciar una capa intermedia, centro exactamente en un borde, huecos internos y una carga repartida entre varias capas. El ancho también puede variar: la normalización debería conservar el resultado. Y las retiradas no se repiten.
> [TRIGGER_4] Comparamos el estado de cada prefijo y el índice de la primera caída. Comparar sólo la configuración final podría pasar por alto el ejemplo estable, inestable, estable que vimos antes. La fuente documenta además contrastes locales con el jurado. Aquí las demostraciones siguen siendo el fundamento, y las comprobaciones buscan errores concretos de implementación o de nuestra traza.”

## Descripcion Visual Detallada:

## Objetos:

- Dos carriles de verificación: rápido con agregados y lento con bloques enumerados; ambos reciben idéntica lista de retiradas. Lista explícita de pruebas h=1,cima vacía,intermedia vacía,borde,huecos,masa en varias capas,w variable.
- Historial de decisiones por prefijo y marcador primera caída; para centro usar Fraction/racionales exactos en verificador de producción, sin mostrarlos como código al espectador.
- Nota documental: guion_sol.md reporta3ejemplos,2casos de capas vacías y250instancias contra geometría enumerada/jurado, más el contraejemplo de la copia adjunta. Esos son resultados previos de la fuente, no una nueva ejecución externa en esta entrega.
- Nota de implementación posterior: el protocolo original usa jenga.in/jenga.out; los diagnósticos Windows y arreglos locales no estándar de la copia no pertenecen al argumento geométrico. Adaptarlos a otra plataforma sería una tarea separada y no se hace al escribir estos guiones.

## Layout y disposicion:

- Carril rápido en x=-3.2,y=1.0 y lento en x=3.2,y=1.0,tamaño5.6×2.2. Tarjetas de pruebas en dos filas y=-1.0,-1.9,cuatro columnas x=-4.5,-1.5,1.5,4.5.
- Línea de prefijos en y=-2.8 y marcador primera caída debajo en y=-3.25. Toda coincidencia entre carriles se muestra con vínculo entre el mismo índice de operación.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:19:** Crear lista común de retiradas y bifurcarla hacia dos carriles. En lento, mostrar agrupación de bloques por corte desde cero; en rápido, banco acumulado y datos locales. No compartir un banco intermedio entre verificadores.
- **[TRIGGER_2] — 00:19–00:41:** Mostrar reconstrucción de extremos del lento leyendo las posiciones presentes, comparándola con L,R del rápido. Para un caso pequeño, poner ambos centros racionales en el mismo soporte y comprobar coincidencia.
- **[TRIGGER_3] — 00:41–01:03:** Crear las siete clases de prueba completas y una tarjeta de garantía operaciones distintas. Iluminar cada clase nombrada; incluir intercambio de w como prueba de escala, sin cambiar n,h ni el orden de retiradas.
- **[TRIGGER_4] — 01:03–01:29:** Crear historial por prefijo con marcas concordantes y marcador primera caída. Recuperar patrón true,false,true y conservar primera caída en ambos carriles. Identificar resultados previos de la fuente con rótulo documentación; no afirmar un nuevo envío al juez ni mostrar una terminal.

- **Duración orientativa:** 01:29. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Carril rápido índigo y lento cian; concordancia verde, diferencias que se investigarían vino. Fuente documental en TEXT_MUTED, prefijo activo terracota. Diagrama de pruebas sin código visible.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---

## Escena: 34

## Nombre: La torre que aprendimos a leer

## Descripcion Breve: El cierre vuelve a la quinta retirada y a la simplificación geométrica demostrada.

## Objetivo Pedagogico: Dejar una pregunta transferible sobre estructura, agregación y datos suficientes.

## Voz en off:

> “[TRIGGER_1] En el ejemplo, la quinta retirada era decisiva. El centro superior seguía en cinco, pero el apoyo se había estrechado hasta seis, ocho. Toda la complejidad visual de la torre terminó en una comparación: cincuenta y cuatro menor que cuarenta y cinco era falso.
> [TRIGGER_2] No llegamos a esa comparación por un truco aislado. Demostramos que las tiras extremas determinan una envolvente rectangular, que la dirección larga siempre pasa y que la masa superior se resume en dos sumas y un conteo. Elegimos coordenadas que hicieron enteros todos los centros y bordes.
> [TRIGGER_3] Después conservamos esos datos con cada retirada y los combinamos de arriba hacia abajo, comprobando antes de agregar el soporte. Los huecos, las capas vacías y el borde dejaron de ser excepciones improvisadas: cada uno encontró su lugar en la regla exacta.
> [TRIGGER_4] La pregunta que nos llevamos es: ¿qué parte de una estructura necesito conocer para decidir, y qué puedo resumir sin perder el argumento? [Pausa.] A veces entender una torre no exige seguir cada uno de sus bloques. Exige descubrir qué información sostienen, y en qué orden debemos reunirla.”

## Descripcion Visual Detallada:

## Objetos:

- Configuración del paso5 en miniatura, soporte(6,8),punto5 y prueba54<45 falsa; tres tarjetas: extremos, sumas/conteo, barrido vertical.
- Pregunta final Tex a tres líneas; crédito Jenga Boom · NEERC2016 ·temporada2016–2017,concurso4diciembre2016.
- Fuente conceptual del video: guion_sol.md. No añadir después del cierre un bloque de código, un tutorial de compilación o una promesa de simulación física.

## Layout y disposicion:

- Miniatura de torre en(-3.7,0.6,0),regla a la derecha en(3.2,0.6,0). Tres tarjetas de lecciones en x=-4,0,4,y=-1.65.
- Pregunta final sustituye todo y ocupa x=-5.8..5.8,y=-0.5..1.15,fuente34pt. Crédito en(0,-3.25,0),fuente21pt.

## Secuencia de animacion:

- **[TRIGGER_1] — 00:00–00:21:** Recuperar sólo el estado geométrico de paso5 y su comparación fallida. Mostrar yes/5 como respuesta ya demostrada, sin mover el centro ni continuar retiradas.
- **[TRIGGER_2] — 00:21–00:43:** Crear tarjetas de extremos,agregados y coordenadas enteras. Enlazarlas con sus objetos del dibujo; las flechas resumen resultados ya probados y no introducen una técnica nueva.
- **[TRIGGER_3] — 00:43–01:03:** Transformar tarjeta de agregados en banco vertical y mostrar comprobar→agregar. Iluminar sucesivamente rótulos huecos, vacío condicionado y borde, con sus reglas correctas. Retirarlos al concluir la frase.
- **[TRIGGER_4] — 01:03–01:26:** Desvanecer torre y tarjetas, escribir únicamente la pregunta transferible. Mantener pausa de 1.5 s y hold de 2 s tras última frase; añadir crédito y FadeOut suave a BG_COLOR. Conservar el silencio visual del cierre sin explicación técnica posterior.

- **Duración orientativa:** 01:26. Tiempo local de escena; ajustar holds con la locución definitiva.

## Código Cromático y Estilo:

- Texto de cierre TEXT_MAIN con acento terracota en información; prueba fallida vino y respuesta TEXT_MAIN. Crédito TEXT_MUTED. Fondo BG_COLOR continuo, sin assets externos necesarios.
- Fondo BG_COLOR; rótulos con Tex/MathTex; respetar límites de frame, roles de masa/soporte e identidad de bloques.

---
