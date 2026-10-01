# Door 1 - D / Codeforces Gym 106495

## 1. Contexto del Concurso

- **Certamen / Fase:** ICPC Gran Premio de México, primera fecha.
- **Año / Edición:** 2026, identificado en el HTML y en el encabezado de `D.cpp`.
- **Fuentes:** `Problem - D - Codeforces.html` y `D.cpp`. [Enunciado del concurso](https://codeforces.com/gym/106495/problem/D). No hay editorial adjunto: la actualización bayesiana y la prueba de optimalidad se desarrollan aquí a partir del modelo y del código.
- **Límites:** $N\le500$, $1\le K,H\le12$, $0\le S\le K$; 4 segundos, 1024 MB; error absoluto o relativo $10^{-9}$.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** hay que sobrevivir $N$ horas en una madriguera, administrando comida y baterías. Esconderse evita los hurones, pero no el hambre; salir permite conseguir recursos, aunque expone a ataques y a comida envenenada.
- **Modelo Matemático / Formal:** al principio de la hora $i\in\{1,\ldots,N\}$ se elige una acción entre esconderse, buscar batería y buscar comida. El estado físico contiene $s\in[0,K]$ baterías y $h\in[0,H-1]$ horas consecutivas sin comer con éxito. Inicialmente $(s,h)=(S,0)$.

Durante la hora $i$:

- Se encuentra una batería con probabilidad $b_i$ al buscarla; como máximo se llevan $K$.
- Se encuentra comida con probabilidad $c_i$ al buscarla. Si se encuentra, el veneno mata con probabilidad $v_i$; si no mata, se come y $h$ vuelve a cero.
- Fuera del escondite, un hurón fotosensible aparece con probabilidad $q_i$. Sólo se sobrevive teniendo **al menos dos baterías al inicio de la hora**, y se consumen exactamente dos.
- Un hurón gigante aparece con probabilidad fija desconocida $p$. Se sortea una sola vez $p\sim U[0,1]$ antes de comenzar; condicionado a ese $p$, las apariciones siguen el modelo Bernoulli por hora. Si aparece fuera del escondite, se muere. Al esconderse se observa si apareció, sin sufrir daño.
- Si no se come y se alcanza $h=H$, se muere, incluso si es la última hora.

Se busca una **política adaptativa**: una regla que elige la acción usando sólo la información disponible antes de la hora, para maximizar la probabilidad de estar vivo al terminar la hora $N$.

La multiplicación de probabilidades de búsqueda, veneno y hurón fotosensible sigue el modelo de eventos independientes que utiliza `D.cpp`. La dependencia temporal especial está en el gigante, porque todas sus apariciones comparten el mismo parámetro $p$. No se debe volver a sortear $p$ en cada hora.

### Información suficiente sobre el pasado

Después de $i-1$ horas sobrevividas, se conocen todas las apariciones anteriores del gigante: si se estaba escondido se observó; si se estaba fuera y se sobrevivió, necesariamente no apareció. Sea $g$ su número total de apariciones anteriores. El estado informativo completo se reduce a
$$(i,s,h,g),\qquad0\le g\le i-1.$$
No hace falta almacenar el orden de apariciones, la lista de decisiones ni una densidad continua explícita.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** un árbol de todas las acciones y resultados posibles tiene tamaño exponencial en $N$, incluso con sólo tres acciones. Probar secuencias fijas de $3^N$ acciones además resuelve un problema más débil: no permite adaptar las decisiones a lo observado. Discretizar $p$ añade una dimensión arbitraria y error de aproximación innecesario.
- **La Observación Clave (Insight Ad-Hoc):** el prior uniforme es una Beta$(1,1)$; tras $g$ apariciones y $i-1-g$ ausencias, la posterior es Beta$(g+1,i-g)$. Toda la información relevante para predecir la siguiente aparición cabe en dos contadores, y uno ya es el tiempo.

### Derivación completa de la probabilidad predictiva

Para una historia concreta de indicadores del gigante, su verosimilitud es proporcional a
$$p^g(1-p)^{i-1-g}.$$
El prior tiene densidad uno. Por Bayes, la posterior normalizada es esa expresión dividida por su integral en $[0,1]$. La probabilidad de aparición en la hora $i$ es
$$\alpha_{i,g}
=\frac{\int_0^1p^{g+1}(1-p)^{i-1-g}\,dp}
       {\int_0^1p^g(1-p)^{i-1-g}\,dp}
=\frac{B(g+2,i-g)}{B(g+1,i-g)}
=\frac{g+1}{i+1}.$$
La identidad usa $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$; para enteros positivos también puede derivarse por integración por partes.

Una política que depende de observaciones anteriores no invalida esta posterior: fijada la historia observable, las decisiones son conocidas, y las probabilidades de los otros eventos no aportan factores dependientes de $p$. Sobrevivir fuera del escondite sí aporta información, pero es exactamente una ausencia ya contada del gigante.

Usar siempre $1/2$ confunde media inicial con probabilidad condicional. Después de una aparición, la siguiente probabilidad es $2/3$; después de una ausencia, $1/3$. Por ejemplo, la probabilidad de dos ausencias iniciales es $\int_0^1(1-p)^2dp=1/3$, no $(1/2)^2=1/4$.

### Ecuación de Bellman, con todos los resultados posibles

Sea $F(i,s,h,g)$ la máxima probabilidad de sobrevivir las horas $i,\ldots,N$ **condicionada a haber llegado vivo** al estado. No se multiplica de nuevo por la probabilidad de llegar a él.

Bases:
$$F(i,s,h,g)=0\quad\text{si }h\ge H,$$
$$F(N+1,s,h,g)=1\quad\text{si }0\le h<H.$$
Un estado muerto no se convierte en éxito por haber pasado el horizonte.

Para escribir las transiciones de la hora actual, definamos
$$D(s',h',g')=\begin{cases}0,&h'\ge H,\\F(i+1,\min(K,s'),h',g'),&h'<H.\end{cases}$$

**Acción 1: esconderse.** No se consumen baterías, no se come y se observa al gigante:
$$A_{hide}=\alpha_{i,g}D(s,h+1,g+1)+(1-\alpha_{i,g})D(s,h+1,g).$$
No interviene $q_i$: el hurón fotosensible no puede atacar en el escondite.

**Acción 2: buscar batería.** Sólo sobreviven las ramas sin gigante. Condicionado a esa ausencia, las cuatro combinaciones son:

| Fotosensible | Hallazgo | Probabilidad condicional | Nuevo estado físico | Condición |
|---|---|---|---|---|
| no | sí | $(1-q_i)b_i$ | $(\min(K,s+1),h+1)$ | hambre válida |
| no | no | $(1-q_i)(1-b_i)$ | $(s,h+1)$ | hambre válida |
| sí | sí | $q_ib_i$ | $(s-1,h+1)$ | $s\ge2$, hambre válida |
| sí | no | $q_i(1-b_i)$ | $(s-2,h+1)$ | $s\ge2$, hambre válida |

Así,
$$A_{bat}=(1-\alpha)\left[(1-q_i)\{b_iD(s+1,h+1,g)+(1-b_i)D(s,h+1,g)\}
+\mathbf1_{s\ge2}q_i\{b_iD(s-1,h+1,g)+(1-b_i)D(s-2,h+1,g)\}\right].$$
El `-1` es consumir dos y encontrar una. No se puede utilizar la batería recién encontrada para defenderse si se empezó con una.

**Acción 3: buscar comida.** Si hay comida y veneno, se muere y la contribución es cero. Las demás ramas son:
$$A_{food}=(1-\alpha)\left[(1-q_i)\{c_i(1-v_i)D(s,0,g)+(1-c_i)D(s,h+1,g)\}
+\mathbf1_{s\ge2}q_i\{c_i(1-v_i)D(s-2,0,g)+(1-c_i)D(s-2,h+1,g)\}\right].$$
No debe incluirse $c_iv_iD(s,h+1,g)$: envenenarse no equivale a no encontrar comida.

Finalmente,
$$F(i,s,h,g)=\max\{A_{hide},A_{bat},A_{food}\}.$$
El máximo está **fuera de la esperanza de los resultados de la hora** porque la acción se elige antes de saber qué ocurrirá. Dentro de cada sucesor sí se permite actuar óptimamente según la información entonces disponible. Intercambiar máximo y esperanza permitiría anticipar eventos y sobreestimaría la supervivencia.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** $F(i,s,h,g)$ es el valor óptimo de continuación para cualquier historia viva que termine en ese estado.

**Suficiencia del estado.** Las baterías y el hambre determinan las restricciones físicas; $i$ selecciona las probabilidades de la hora; $(i,g)$ determina la distribución posterior del gigante. Dos historias con el mismo estado inducen las mismas distribuciones de resultados futuros, acciones disponibles y objetivo. Se pueden fusionar.

**Base.** Al terminar las $N$ horas sin morir, el evento objetivo ya ocurrió y vale uno. Una transición que alcanza hambre $H$ vale cero, por definición del evento de supervivencia.

**Paso inductivo.** Supongamos correctos todos los estados de la hora $i+1$. Para una acción fija, sus ramas son disjuntas y cubren todos los resultados; las ramas letales contribuyen cero. La ley de la probabilidad total da exactamente $A_{hide}$, $A_{bat}$ o $A_{food}$. Cada rama viva usa el mejor valor de continuación por hipótesis inductiva. Escoger el máximo de las tres opciones alcanza el mejor valor posible. Una mezcla aleatoria de acciones sería una combinación convexa de sus valores y no puede superar el máximo.

**Conclusión.** Por inducción hacia atrás, el resultado buscado es $F(1,S,0,0)$.

- **Casos Borde y Limitaciones:**
  - $H=1$: hay que comer con éxito cada hora; esconderse y buscar batería tienen valor cero.
  - $N<H$: esconderse siempre garantiza supervivencia 1, aunque el gigante aparezca, porque no se alcanza el hambre límite.
  - $N=H$ sin posibilidad de encontrar comida: se muere al final de la última hora; respuesta cero.
  - $K=1$: la lámpara nunca puede usarse; todas las ramas con fotosensible fuera son letales.
  - $s=1$, hallazgo seguro de batería y fotosensible seguro: se muere; importa la batería **inicial**.
  - $s=K$, sin ataque y con hallazgo: el recurso se satura en $K$.
  - $s=K$, con ataque y hallazgo: termina en $K-1$, no en $K-2$ ni $K$.
  - $v_i=1$: encontrar comida mata; no encontrarla aún puede permitir sobrevivir si sobra margen de hambre.
  - Probabilidades cero y uno no requieren logaritmos ni divisiones especiales. $i+1$ nunca es cero.
  - $0\le g\le i-1$ garantiza $0<\alpha<1$. No recorrer estados con historias imposibles como $g>i-1$.
  - Las probabilidades pueden volverse muy pequeñas. La tolerancia absoluta $10^{-9}$ permite que resultados muchísimo menores se redondeen a cero; no hace falta aritmética de precisión arbitraria.

## 5. Traza Lógica Paso a Paso

Ejemplo pedagógico: $N=2$, $K=S=2$, $H=2$, sin fotosensibles ni veneno, comida segura en ambas horas. Las baterías son irrelevantes en esta instancia.

En la última hora, si $h=0$, esconderse tiene valor 1 porque se termina con hambre 1. Si $h=1$, es obligatorio buscar comida: valor $1-\alpha_{2,g}$.

| Estado al comenzar hora 2 | $\alpha$ | Mejor acción | Valor |
|---|---:|---|---:|
| $(2,2,1,0)$ | $1/3$ | buscar comida | $2/3$ |
| $(2,2,1,1)$ | $2/3$ | buscar comida | $1/3$ |
| $(2,2,0,0)$ | $1/3$ | esconderse | $1$ |

En la hora 1, $\alpha_{1,0}=1/2$:

1. Esconderse: con probabilidad $1/2$ aparece el gigante y se llega al segundo estado; con $1/2$ no aparece y se llega al primero. Valor $(1/2)(1/3)+(1/2)(2/3)=1/2$.
2. Buscar comida: sólo se sobrevive si no aparece el gigante, probabilidad $1/2$. Se come y se llega al tercer estado, valor 1. Total $1/2$.
3. Buscar batería: no se come. Si no aparece el gigante, se llega a $(2,2,1,0)$, valor $2/3$. Total $(1/2)(2/3)=1/3$.

La respuesta es $1/2$. La rama de esconderse muestra que observar una aparición cambia las decisiones y valores posteriores, aunque no haya daño inmediato.

Comprobación del cuarto ejemplo oficial: $N=1,K=12,S=1,H=1$, $c=1,v=1/2,q=1/2$. Hay que buscar comida. Se necesita ausencia del gigante ($1/2$), ausencia del fotosensible ($1/2$, por falta de baterías) y comida no venenosa ($1/2$): respuesta $1/8=0.125$.

## 6. Análisis de Complejidad

- **Complejidad Temporal:** en la hora $i$ hay $i$ valores posibles de $g$, $K+1$ de batería y $H$ de hambre. El número total de estados es
  $$\sum_{i=1}^N i(K+1)H=\frac{N(N+1)}2(K+1)H=O(N^2KH).$$
  Cada estado considera tres acciones con un número constante de resultados. Para $N=500,K=H=12$, son 19 539 000 estados potenciales válidos. No es $O(NKH)$: la información aprendida del gigante aporta la segunda dimensión temporal.
- **Complejidad Espacial:** `D.cpp` reserva dos tablas completas de $505\cdot14\cdot14\cdot505=49\,984\,900$ elementos. Con `double` de 8 bytes y `bool` de 1, son 449 864 100 bytes, unos 429 MiB, además de otros datos. Asintóticamente $O(N^2KH)$ y pila recursiva $O(N)$. Está por debajo del límite de 1024 MB, pero es una reserva considerable.

Sólo se consulta la hora siguiente, por lo que una implementación iterativa necesita dos capas de $(N+1)(K+1)H$ valores: $O(NKH)$ memoria. En los máximos, las dos capas de `double` ocupan aproximadamente 1.19 MiB; no se almacena toda la política.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** DP hacia atrás con dos capas y una función de lectura de sucesores que invalida el hambre y satura baterías. Un ciclo de dos casos representa ausencia/presencia del fotosensible sin duplicar cuatro ramas.

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;
struct Prob { double b, c, v, q; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K, S, H;
    cin >> N >> K >> S >> H;
    vector<Prob> p(N + 1);
    for (int i = 1; i <= N; ++i)
        cin >> p[i].b >> p[i].c >> p[i].v >> p[i].q;
    auto id = [=](int g, int s, int h) {
        return (g * (K + 1) + s) * H + h;
    };
    int size = (N + 1) * (K + 1) * H;
    vector<double> next(size, 1.0), cur(size, 0.0);
    for (int i = N; i >= 1; --i) {
        fill(cur.begin(), cur.end(), 0.0);
        auto value = [&](int g, int s, int h) -> double {
            if (h >= H || s < 0) return 0.0;
            return next[id(g, min(K, s), h)];
        };
        for (int g = 0; g < i; ++g) {
            double giant = double(g + 1) / double(i + 1);
            for (int s = 0; s <= K; ++s) {
                for (int h = 0; h < H; ++h) {
                    double hide = giant * value(g + 1, s, h + 1)
                                + (1 - giant) * value(g, s, h + 1);
                    double bat = 0, food = 0;
                    for (int light = 0; light <= 1; ++light) {
                        if (light && s < 2) continue;
                        int batteries = s - 2 * light;
                        double prob = light ? p[i].q : 1 - p[i].q;
                        bat += prob * (
                            p[i].b * value(g, batteries + 1, h + 1)
                            + (1 - p[i].b) * value(g, batteries, h + 1));
                        food += prob * (
                            p[i].c * (1 - p[i].v) * value(g, batteries, 0)
                            + (1 - p[i].c) * value(g, batteries, h + 1));
                    }
                    cur[id(g, s, h)] = max({hide, (1-giant)*bat, (1-giant)*food});
                }
            }
        }
        cur.swap(next);
    }
    cout << fixed << setprecision(12) << next[id(0, S, 0)] << '\n';
}
```

### Auditoría detallada de `D.cpp`

1. `dpr(i,s,h,g)` coincide con $F$. `dpcheck` distingue entre no calculado y una probabilidad óptima igual a cero.
2. `pGF=(1.0+g)/(1.0+i)` es correcta: antes de la hora $i$ hay $i-1$ observaciones. Su comentario habla de la hora siguiente y puede confundir; el valor realmente se utiliza para la **hora i**.
3. El bloque de esconderse actualiza `g` en ambos resultados posibles; al salir sólo se propaga `g` sin incremento porque una aparición es letal.
4. `s-1` al buscar batería con fotosensible combina los dos consumos con un hallazgo. Las guardas `s>=2` usan correctamente el recurso inicial.
5. `h+1<maxHambre` elimina las ramas de inanición. Encontrar comida segura reinicia en cero sin esa condición.
6. Los factores de veneno sólo aparecen junto al hallazgo de comida; las ramas mortales simplemente no se suman.
7. `act` toma el máximo entre acciones después de sumar resultados, respetando la información disponible.
8. La consulta de memo ocurre antes de saturar `s`. En este archivo concreto el único exceso es $K+1\le13$, que cabe en `MAXK=14`; después se consulta el estado saturado. Es más robusto normalizar antes de indexar, como hace la referencia.
9. El precálculo terminal marca incluso `h==H` con valor uno. Esos estados no se alcanzan desde las transiciones actuales por sus guardas, así que no alteran la respuesta; aun así, la definición matemática limpia asigna uno **sólo a estados vivos**, como en la referencia.
10. Los modos de depuración y la cadena `sangria` no forman parte del algoritmo. Compilar con `LOCAL` cambia entrada y puede añadir salida incompatible con el juez.

### Verificación reproducible

Ejecutar los seis ejemplos del HTML, incluido $H>N$ y el caso de resultado $1/8$. Para instancias pequeñas, comparar contra un árbol de historias completas sin memoización que integre la probabilidad de cada historia del gigante, $B(g+1,a+1)$ para $g$ apariciones y $a$ ausencias. En cada nodo se maximiza después de sumar las ramas de una acción. Esa construcción conserva el historial y las masas no normalizadas; contrasta de forma independiente la compresión de estado y la fórmula predictiva.

### Comprobaciones ejecutadas durante este análisis

La implementación de referencia incluida en este documento se extrajo y compiló con C++17 y optimización. Resultado: 6 ejemplos y 80 instancias contra árbol completo de historias con integración Beta exacta: PASS. Las pruebas se ejecutaron localmente; no constituyen un nuevo envío al juez. Los archivos originales se conservaron sin modificaciones.
