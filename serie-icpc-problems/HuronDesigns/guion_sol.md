# Huron Designs - H / Codeforces Gym 105873

## 1. Contexto del Concurso

- **Certamen / Fase:** ICPC Gran Premio de México, primera fecha.
- **Año / Edición:** **2025**, según el nombre del concurso en el HTML adjunto y el [registro del problema en Codeforces](https://codeforces.com/gym/105873/status/H).
- **Fuentes:** `Problem - H - Codeforces.html` y **`H.HuronDesing.cpp`**, que es el código del usuario para este problema. [Enlace del problema](https://codeforces.com/gym/105873/problem/H). No hay editorial oficial adjunto; se contrastan el enunciado, el código aportado y la implementación de referencia incluida aquí.
- **Identificación de archivos:** `H.HuronDesing.cpp` corresponde a Huron Designs, Gym 105873, primera fecha de México 2025. La carpeta también conserva `H.cpp`, que corresponde a Huron Airlines y no se usa para este análisis. Los dos archivos permanecen sin modificaciones.
- **Límites:** $1\le n\le20$; tiempos y beneficios hasta $10^9$; 1 segundo, 256 MB; error absoluto o relativo hasta $10^{-6}$.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** Tony elige cuáles encargos de diseño aceptar y en qué orden completarlos. Cada encargo paga una base si se entrega a tiempo y puede incluir un bono cuyo importe y fecha límite son aleatorios.
- **Modelo Matemático / Formal:** cada trabajo $i$ tiene tiempo de proceso $c_i>0$, fecha límite obligatoria $d_i$, beneficio base $p_i$, bono $X_i\sim U[lx_i,rx_i]$ y umbral de bono $Y_i\sim U[ly_i,ry_i]$. Se elige una secuencia de índices distintos $\pi=(\pi_1,\ldots,\pi_k)$ para una única máquina, con finalizaciones
  $$F_{\pi_j}=\sum_{r=1}^{j}c_{\pi_r}.$$
  Cada trabajo aceptado debe satisfacer $F_i\le d_i$. La recompensa es
  $$\sum_{i\in\pi}\left(p_i+X_i\mathbf1\{F_i\le Y_i\}\right).$$
  El objetivo es maximizar su esperanza, permitiendo no aceptar algunos trabajos.

La solución usa el modelo de sorteos independientes del importe y el umbral de cada bono. **Precisión probabilística:** el HTML describe ambas distribuciones uniformes sin especificar una correlación. La factorización siguiente corresponde a la interpretación de sorteos independientes; si sólo se dieran marginales y se permitiera dependencia arbitraria entre $X_i,Y_i$, el valor esperado no quedaría determinado. No se necesita independencia entre ganancias de trabajos distintos para aplicar linealidad de la esperanza.

### Convertir el azar en una función determinista del tiempo

Por independencia dentro del bono:
$$\mathbb E[X_i\mathbf1\{t\le Y_i\}]=\mathbb E[X_i]\Pr(Y_i\ge t).$$
La media del importe es $\mu_i=(lx_i+rx_i)/2$. Definamos
$$q_i(t)=\begin{cases}
1,&t\le ly_i,\\
0,&t>ry_i,\\
\dfrac{ry_i-t}{ry_i-ly_i},&ly_i<t\le ry_i\text{ y }ly_i<ry_i.
\end{cases}$$
Si $ly_i=ry_i=a$, el umbral es determinista: $q_i(t)=1$ para $t\le a$ y cero en otro caso. Esta definición evita dividir entre cero.

La ganancia esperada por finalizar $i$ en $t$ es
$$w_i(t)=p_i+\mu_iq_i(t),\quad\text{utilizable sólo si }t\le d_i.$$
Para una uniforme no degenerada, $\Pr(Y_i=ry_i)=0$; por eso terminar exactamente en $ry_i$ da probabilidad cero. En una distribución degenerada, terminar exactamente en el único valor sí da probabilidad uno.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** enumerar subconjuntos y permutaciones cuesta
  $$\sum_{k=0}^n\frac{n!}{(n-k)!}=\Theta(n!),$$
  y $20!\approx2.43\cdot10^{18}$ es inviable. Una DP indexada por tiempo puede necesitar hasta $\sum c_i\le2\cdot10^{10}$ estados temporales por etapa; no es una mochila con capacidad pequeña.
- **La Observación Clave (Insight Ad-Hoc):** para un subconjunto fijo de trabajos $S$, su tiempo total
  $$T[S]=\sum_{i\in S}c_i$$
  es independiente del orden. Distintas permutaciones de $S$ tienen ganancias y factibilidad diferentes, pero **terminan al mismo tiempo** si no hay pausas. Para todas sus posibles continuaciones sólo importa ese tiempo y el conjunto ya usado. Se conserva únicamente el mejor valor para cada máscara.

### Por qué se eliminan los tiempos ociosos

Cada $w_i(t)$ es no creciente en $t$ y todas las fechas límite son superiores, no inferiores. Si un plan contiene una pausa, desplazar a la izquierda los trabajos posteriores reduce sus finalizaciones, no rompe ninguna fecha límite y no disminuye ninguna recompensa. Existe, por tanto, una solución óptima sin pausas. No hace falta almacenar tiempo como segunda dimensión.

### Estado y recurrencia estricta de la implementación de referencia

$$DP[S]=\text{máxima ganancia esperada de un orden factible que realiza exactamente }S.$$
Se usa $DP[\varnothing]=0$ y $DP[S]=-\infty$ cuando el conjunto no tiene un orden factible. Para un trabajo nuevo $j\notin S$, sea $t=T[S]+c_j$. Si $t\le d_j$:
$$DP[S\cup\{j\}]\gets\max\bigl(DP[S\cup\{j\}],DP[S]+w_j(t)\bigr).$$

La respuesta es $\max_S DP[S]$, no sólo $DP[\{1,\ldots,n\}]$: aceptar todos los trabajos puede ser imposible o perjudicar bonos muy grandes al desplazar otros encargos.

### Recurrencia que usa exactamente `H.HuronDesing.cpp`

El código recorre las máscaras en orden creciente y elige qué trabajo hacer **al final**, en vez de extender un prefijo hacia delante. Denotemos su arreglo por $A$ para distinguirlo de la DP estricta:

$$A[\varnothing]=0,\qquad
A[M]=\max\left(\{0\}\cup\left\{A[M\setminus\{i\}]+w_i(T[M]):i\in M,\ T[M]\le d_i\right\}\right).$$

`tiempoNecesario(mask)` calcula $T[M]$; `prevMask` es $M\setminus\{i\}$; `valEsperadoGanancia(i, tiempo)` calcula $w_i(T[M])$. Quitar un bit encendido produce un entero menor, así que `dp[prevMask]` ya está calculado cuando se lo consulta. A pesar del nombre `dpfunc`, **no hay recursión**: su cuerpo no llama a `dpfunc(prevMask)`.

La diferencia sustancial es el cero inicial en **todas** las máscaras. Por eso $A[M]$ no debe interpretarse como el óptimo de realizar exactamente todos los trabajos de $M$: puede heredar un cero de un subconjunto inviable. Sin embargo, maximizar $A[M]$ sobre todas las máscaras sigue dando la respuesta correcta. La prueba precisa se presenta en la sección siguiente.

**Por qué no basta ordenar por fechas límite:** para un conjunto fijo, ordenar por fecha límite ayuda a la factibilidad sin bonificaciones, pero no necesariamente maximiza recompensas dependientes del instante. Por ejemplo, dos trabajos de duración uno, bases uno, fechas límite 10 y 11: el primero no da bono; el segundo da bono fijo 100 si acaba antes o en 1. Ordenar por fecha límite produce 2; hacer primero el segundo produce 102. Tampoco hay una única razón beneficio/tiempo que represente todos los cambios de pendiente de los bonos.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** al procesar una máscara $S$, $DP[S]$ es el mejor valor entre todos sus órdenes factibles sin pausas.

**Base.** El conjunto vacío se realiza en tiempo cero con beneficio cero.

**Validez de cada transición.** Partimos de un orden factible de $S$. Añadir $j$ al final no modifica las finalizaciones anteriores. Su propia finalización es $T[S]+c_j$, y se comprueba su fecha límite. Por tanto el nuevo orden es factible y la ganancia adicional es exactamente $w_j(t)$.

**Exhaustividad.** Todo orden factible no vacío de $U$ tiene un último trabajo $j$. Su prefijo realiza $S=U\setminus\{j\}$ y acaba en $T[S]$. La transición desde ese prefijo está incluida en la recurrencia porque $T[U]\le d_j$.

**Dominancia.** Si dos órdenes del mismo $S$ tienen valores $v_1\le v_2$, ambos terminan en $T[S]$ y dejan exactamente los mismos trabajos disponibles. Cualquier continuación factible del primero también lo es del segundo y añade las mismas ganancias esperadas. Se puede descartar $v_1$. Este es el motivo formal para comprimir factorialmente muchos órdenes en una máscara.

Por inducción sobre $|S|$, las transiciones alcanzan el óptimo para cada subconjunto. Maximizar sobre todos los subconjuntos recupera el óptimo global. La eliminación previa de pausas asegura que no se perdió una mejor solución fuera de ese espacio.

### Por qué la inicialización en cero de tu código no altera la respuesta final

No basta con trasladar a ese arreglo la prueba del estado estricto. Se necesitan dos desigualdades.

**1. Tu DP no pierde el óptimo.** Para cualquier conjunto con un orden factible, el valor estricto $DP[M]$ es menor o igual que $A[M]$. Se prueba por inducción: el último trabajo de ese orden satisface la fecha límite, su transición está incluida y el valor de su prefijo en $A$ no es menor que el valor estricto. Por tanto $\max_M A[M]\ge OPT$.

**2. Ningún valor artificial supera el óptimo global.** Para toda máscara $M$ existe un plan factible que ejecuta un **subconjunto** de $M$, termina a más tardar en $T[M]$ y obtiene una ganancia esperada al menos $A[M]$.

- Si el valor elegido es cero, el plan vacío es un testigo válido.
- Si el valor elegido procede de $P=M\setminus\{i\}$, por inducción existe un plan testigo de $P$ que termina en algún $t_P\le T[P]$ y gana al menos $A[P]$.
- Añadir $i$ después de ese plan lo termina en $t_P+c_i\le T[M]\le d_i$. El trabajo $i$ no estaba en el plan anterior porque éste usaba sólo elementos de $P$.
- Como $w_i$ es no creciente, $w_i(t_P+c_i)\ge w_i(T[M])$. El plan ampliado gana al menos $A[P]+w_i(T[M])=A[M]$ y termina a más tardar en $T[M]$.

Todo valor del arreglo está, pues, dominado por la recompensa de algún plan realmente factible. En particular $\max_M A[M]\le OPT$. Combinando ambas desigualdades:
$$\boxed{\max_M A[M]=OPT.}$$

Una interpretación útil es que los trabajos descartados de una máscara pueden estar introduciendo esperas ficticias. Eliminarlas sólo adelanta las tareas que sí aportan beneficio y nunca reduce su recompensa. El arreglo puede describir incorrectamente la factibilidad de una máscara exacta, pero no produce una respuesta global demasiado grande.

**Límite de esta justificación:** no autoriza a consultar `dp[fullMask]` como única respuesta, reconstruir todas las tareas de una máscara sin más comprobaciones ni reutilizar la inicialización en cero en problemas donde una recompensa crece con el tiempo. Si se desea que cada entrada represente exactamente su conjunto, debe usarse un centinela de inviabilidad como en la referencia.

- **Casos Borde y Limitaciones:**
  - Un trabajo con $c_i>d_i$ nunca puede realizarse, ni siquiera primero.
  - Si todos son imposibles, el conjunto vacío da respuesta cero.
  - `lx=rx` hace determinista el monto, sin problemas para la media.
  - `ly=ry` exige el tratamiento anterior; no dividir entre cero.
  - Finalizar exactamente en $d_i$ es válido.
  - Una máscara puede tener tiempo total razonable pero ningún orden factible: no confundir `T[mask]` con factibilidad.
  - Aunque cada duración cabe en 32 bits, la suma puede alcanzar $2\cdot10^{10}$: usar 64 bits en tiempos.
  - La suma esperada es como máximo $20(10^9+10^9)=4\cdot10^{10}$. `double` tiene precisión suficiente para la tolerancia relativa; `long double` es una opción conservadora.
  - En la DP estricta, los conjuntos inviables necesitan un centinela negativo. Tu código usa cero y, por ello, otro invariante: su máximo global es correcto por la prueba anterior, aunque una entrada aislada no certifique la factibilidad de toda su máscara.
  - La factorización del bono no autoriza reemplazar la decisión por una basada en el promedio de la fecha; se necesita la probabilidad de superar la **fecha real de finalización**.

## 5. Traza Lógica Paso a Paso

Usamos el segundo ejemplo del enunciado:

| Trabajo | $d$ | $p$ | $c$ | $[lx,rx]$ | $[ly,ry]$ |
|---|---:|---:|---:|---|---|
| A | 10 | 15 | 8 | [50,50] | [1,8] |
| B | 20 | 1 | 7 | [20,30] | [6,10] |

1. $DP[\varnothing]=0$, $T[\varnothing]=0$.
2. Sólo A: termina en 8, dentro de su fecha 10. Como $Y_A$ es continuo en [1,8], $\Pr(Y_A\ge8)=0$. Valor $DP[A]=15$.
3. Sólo B: termina en 7. $\mu_B=25$, $q_B(7)=(10-7)/(10-6)=3/4$. Valor $DP[B]=1+25(3/4)=19.75$.
4. A seguido de B: B termina en 15, antes de 20 pero después del umbral máximo 10. Añade sólo su base 1, total 16.
5. B seguido de A: A terminaría en 15, después de su fecha obligatoria 10; transición rechazada.
6. $DP[A,B]=16$, pero la respuesta es $\max(0,15,19.75,16)=19.75$.

Este caso muestra por qué se maximiza sobre subconjuntos y por qué una mayor cantidad de trabajos no implica mayor beneficio.

### La misma traza en los nombres de tu código

Numerando A como bit 0 y B como bit 1, `mask=0,1,2,3` produce respectivamente tiempos `0,8,7,15` y valores `0,15,19.75,16`. Al calcular `mask=3`, elegir A como última tarea se descarta por `d[A]=10<15`; elegir B como última usa `dp[1]+1=16`. La variable global `ans` conserva 19.75.

Para observar la diferencia de semántica entre ambas DP, tomar A con $c_A=2,d_A=1,p_A=100$, B con $c_B=1,d_B=10,p_B=7$, y bonos cero. A es imposible en cualquier orden. Tu código obtiene `dp[1]=0`, `dp[2]=7` y `dp[3]=7`: en la última máscara agrega B al cero de A y lo evalúa en tiempo 3. La DP estricta marca `DP[1]` y `DP[3]` como inviables. Aun así, ambas respuestas globales son 7, alcanzable haciendo únicamente B y terminándolo en tiempo 1.

## 6. Análisis de Complejidad

- **Complejidad Temporal de la referencia:** precalcular sumas por máscara cuesta $O(2^n)$ retirando un bit. Las transiciones recorren exactamente $n2^{n-1}$ pares $(S,j)$ con $j\notin S$ si se visitan todas las máscaras, por lo que el total es $O(n2^n)$. Para $n=20$, son 10 485 760 extensiones potenciales; cada una usa una suma, comparaciones y a lo sumo una división real.
- **Complejidad Espacial de la referencia:** $O(2^n+n)$, dominada por tiempos y valores DP. Con `long long` y `double`, dos arreglos de $2^{20}$ elementos requieren unos 16 MiB. Si se guardan predecesores para reconstruir un orden, se añaden $O(2^n)$ enteros; el enunciado sólo pide el valor.

### Complejidad de `H.HuronDesing.cpp`

`main` llama una vez a `dpfunc` para cada una de las $2^n$ máscaras. `tiempoNecesario` recorre los $n$ trabajos en cada llamada, y el bucle que busca el último trabajo vuelve a recorrerlos. Son dos recorridos de longitud $n$ por máscara: **$O(n2^n)$ tiempo**, el mismo orden que la referencia aunque se recalculen las sumas. Para $n=20$ hay 41 943 040 iteraciones de esos dos bucles en conjunto; únicamente $n2^{n-1}$ entradas del segundo tienen el bit encendido, y algunas se descartan por fecha límite.

No existe pila recursiva creciente: `dpfunc` se ejecuta y retorna directamente. `dpcheck` es redundante con el recorrido actual, que no repite máscaras; quitarlo sería una limpieza opcional, no una corrección necesaria.

En esta copia, **`dpcheck` es `double`, no `bool`**, y ambos arreglos reservan `1 << MAXN` con `MAXN=21`: cada uno contiene 2 097 152 valores de 8 bytes, 16 MiB por arreglo, **32 MiB en total**, aunque sólo se usan las primeras $2^n$ posiciones. Los arreglos de parámetros suman una cantidad pequeña adicional. Si se parametrizara la reserva según $n$, el orden espacial sería $O(2^n+n)$; la copia concreta mantiene esa reserva máxima incluso para entradas pequeñas.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** tu archivo separa el cálculo de la ganancia esperada, la suma de duraciones de una máscara y la elección de la última tarea. La referencia siguiente conserva el mismo objetivo con sumas precalculadas, transiciones hacia delante y un estado estricto de factibilidad. Ambos programas producen el mismo máximo global, aunque no necesariamente los mismos valores por máscara.

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
struct Job { ll d, p, c, lx, rx, ly, ry; };

double gain(const Job& a, ll t) {
    double prob;
    if (t <= a.ly) prob = 1.0;
    else if (t >= a.ry) prob = 0.0;
    else prob = double(a.ry - t) / double(a.ry - a.ly);
    return double(a.p) + (double(a.lx) + double(a.rx)) * 0.5 * prob;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<Job> a(n);
    for (auto& x : a) cin >> x.d >> x.p >> x.c >> x.lx >> x.rx >> x.ly >> x.ry;
    int lim = 1 << n;
    vector<ll> duration(lim, 0);
    for (int mask = 1; mask < lim; ++mask) {
        int j = __builtin_ctz(static_cast<unsigned>(mask));
        duration[mask] = duration[mask ^ (1 << j)] + a[j].c;
    }
    vector<double> dp(lim, -1.0);
    dp[0] = 0.0;
    double answer = 0.0;
    for (int mask = 0; mask < lim; ++mask) {
        if (dp[mask] < 0.0) continue;
        answer = max(answer, dp[mask]);
        unsigned remaining = static_cast<unsigned>((lim - 1) ^ mask);
        while (remaining) {
            int j = __builtin_ctz(remaining);
            remaining &= remaining - 1;
            ll t = duration[mask] + a[j].c;
            if (t > a[j].d) continue;
            int next = mask | (1 << j);
            dp[next] = max(dp[next], dp[mask] + gain(a[j], t));
        }
    }
    cout << fixed << setprecision(12) << answer << '\n';
}
```

### Justificación de cada decisión de implementación

`-1` es un centinela seguro porque todo valor factible es no negativo. `__builtin_ctz` sólo se llama con valores no nulos. Quitar el bit menos significativo permite construir `duration` desde una máscara menor. Añadir un bit también produce una máscara mayor; recorrerlas en orden numérico es, por ello, un orden topológico de las transiciones. La primera condición de `gain` cubre correctamente `ly==ry` y `t==ly`, antes de cualquier división.

### Auditoría de `H.HuronDesing.cpp`, función por función

1. **Parámetros globales.** `d,p,c,lx,rx,ly,ry` corresponden a los siete datos del enunciado y se leen en ese orden. El tipo `ll` protege la suma de duraciones, que puede llegar a $2\cdot10^{10}$ al evaluar una máscara, aunque sus trabajos resulten inviables.
2. **`valEsperadoGanancia(i,hora)`.** `0.5*(lx[i]+rx[i])` obtiene la media sin división entera. Si `hora<=ly[i]`, todo el intervalo admite el bono. Si `ly[i]<hora<ry[i]`, multiplica la media por la fracción de intervalo restante. En otro caso devuelve la base. La multiplicación empieza con `double`, de modo que la división no se trunca a entero.
3. **Intervalos degenerados.** Si `ly==ry`, la primera condición acepta la igualdad y la segunda nunca se ejecuta. No hay división entre cero. Si el intervalo no es degenerado, terminar en `ry` produce únicamente la base, correctamente.
4. **Comentario de la esperanza.** El comentario escribe $\mathbf1\{t<Y_i\}$, pero el enunciado exige $\mathbf1\{t\le Y_i\}$. Para una uniforme continua no degenerada son equivalentes casi seguramente; para `ly==ry` no lo son. **El código ejecutable usa correctamente la igualdad**; el comentario es el que debe leerse con esta precisión.
5. **`tiempoNecesario(mask)`.** Suma `c[i]` por cada bit encendido; implementa $T[M]$. En esta función los bits indican tiempos incluidos en la máscara, no certifican que se pueda ejecutar todo ese conjunto.
6. **`dpfunc(mask)`.** Marca la entrada calculada, obtiene el tiempo total, inicia `ans=0` y considera cada bit como última tarea. `clear_bit(prevMask,i)` sólo modifica la copia local. La guarda `d[i]>=tiempo` admite entregas exactamente a tiempo. Cada candidato usa el valor ya calculado `dp[prevMask]` más la ganancia al terminar en `tiempo`.
7. **Orden de dependencia.** `prevMask<mask` al quitar un bit encendido. El recorrido creciente de `main` es indispensable para leer `dp[prevMask]` directamente. Llamar únicamente `dpfunc((1<<n)-1)` no resolvería las dependencias, porque no hay recursión dentro de la función.
8. **Base y estados inviables.** Para `mask=0` no hay candidatos y se guarda cero. Para otras máscaras sin candidato también se guarda cero; no es la misma semántica que “ejecutar exactamente mask”. La prueba de dominancia de la sección 4 justifica la respuesta final con esta implementación.
9. **Máximo global.** La variable `ans` de `main` reúne todas las máscaras, que es exactamente la condición usada en la prueba. La variable homónima dentro de `dpfunc` es local y calcula sólo el valor de una máscara.
10. **Reserva y precisión.** `dpcheck` almacena 0/1 convertidos a `double` y funciona como condición booleana, aunque use ocho veces la memoria de un `bool` típico. Las operaciones con `1<<i` son seguras para $i\le19$, y `1<<MAXN` también cabe en `int`. `setprecision(10)` satisface la tolerancia del problema; la validación local incluye ganancias de $4\cdot10^{10}$.
11. **Elementos ajenos al algoritmo.** Alias no utilizados, `MOD`, `set_bit` y macros de depuración no intervienen en el resultado. Con `LOCAL` la entrada pasa a `in.txt` y la depuración escribe texto adicional; las verificaciones se realizaron sin esa macro. `bitset<3>` sólo muestra tres bits en depuración y no representa todas las máscaras cuando $n>3$.

### Interpretación de la nota sobre esperanza e integración

La nota inicial menciona la ley del estadístico inconsciente. Aquí se aplica a la función $g_t(y)=\mathbf1\{t\le y\}$:
$$\mathbb E[g_t(Y_i)]=\int g_t(y)\,dF_{Y_i}(y).$$
Para $ly_i<ry_i$, la medida tiene densidad constante $1/(ry_i-ly_i)$ en su intervalo; integrar el indicador da la longitud de la parte con $y\ge t$, dividida por la longitud total. Para `ly==ry`, la medida es una masa puntual y el resultado es el indicador evaluado en ese punto. Multiplicar por la media de $X_i$ utiliza independencia; sumar la base utiliza linealidad. No es necesario un cambio de variable para obtener esta fórmula.

### Verificación reproducible

Comparar la DP con enumeración de todas las secuencias de trabajos distintos para $n\le8$. La fuerza bruta calcula cada finalización y rechaza el orden al violar una fecha. Incluir intervalos degenerados, trabajos imposibles, finalizaciones en ambos extremos y los dos ejemplos oficiales (33 y 19.75). Esa comparación verifica la compresión por máscaras frente a una implementación que conserva los órdenes completos.

### Comprobaciones ejecutadas durante este análisis

La referencia incluida pasó previamente los dos ejemplos y 100 instancias contra enumeración exacta. En la revisión del archivo añadido se compiló **`H.HuronDesing.cpp` directamente, sin modificarlo**, con GCC, C++17 y optimización. Los resultados de esta nueva comprobación se consignan a continuación. Las pruebas son locales y no constituyen un nuevo envío al juez; los dos archivos C++ de la carpeta se conservaron intactos.

- **397 casos contra enumeración de todas las secuencias**, con ganancias calculadas mediante fracciones exactas: dos ejemplos oficiales, un caso con máscara inviable, 144 pares exhaustivos de trabajos pequeños y 250 instancias aleatorias de hasta siete trabajos. Todos coinciden.
- **Dos casos con $n=20$ y valores de hasta $10^9$**: uno fuerza duraciones totales mayores que 32 bits; el otro alcanza ganancia $4\cdot10^{10}$. Ambos coinciden con sus resultados analíticos.
- La revisión confirma la ganancia esperada, la guarda de deadline, el orden de máscaras, la respuesta global y las cotas de tiempo/memoria. No se encontró un defecto funcional en el código de Designs bajo el modelo del enunciado.
