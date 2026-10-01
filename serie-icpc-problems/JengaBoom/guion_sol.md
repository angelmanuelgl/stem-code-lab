# Jenga Boom - J / NEERC 2016 / Gym 101190

## 1. Contexto del Concurso

- **Certamen / Fase:** ACM ICPC Northeastern European Regional Contest (NEERC), regional del noreste de Europa; sedes indicadas: San Petersburgo, Barnaul, Tbilisi y Almaty.
- **Año / Edición:** temporada 2016–2017; concurso del **4 de diciembre de 2016**.
- **Fuentes:** `20162017-acmicpc-northeastern-european-regional-contest-neerc-16-en.pdf`, página 12; `J.cpp`; contraste adicional con el [archivo oficial de NEERC 2016](https://neerc.ifmo.ru/archive/2016.html), su [presentación de soluciones](https://neerc.ifmo.ru/archive/2016/neerc-2016-review.pdf) y el [archivo del jurado](https://neerc.ifmo.ru/archive/2016/neerc-2016-archive.zip), específicamente `neerc2016/main/problems/jenga/jenga_pkun.c++`, `jenga_gk.java` y `Validate.c++`.
- **Límites del enunciado:** $1\le n,w\le10000$, $1\le h,m\le5000$. Los bloques retirados son distintos. La versión original utiliza `jenga.in` y `jenga.out`. El PDF no especifica aquí un límite de tiempo o memoria; no se inventa uno.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** se construye una torre con capas alternadas de bloques y se retiran piezas en un orden conocido. Hay que encontrar la primera retirada que vuelve inestable alguna sección de la torre.
- **Modelo Matemático / Formal:** inicialmente hay $h$ capas y $n$ bloques por capa. Cada bloque tiene dimensiones $1\times w\times wn$, igual masa y densidad uniforme. Las capas se alternan en orientación y ocupan un cuadrado de lado $wn$. Las operaciones eliminan el bloque $(l,k)$, numerando capas desde abajo y bloques desde un extremo coherente.

Para cada corte encima de una capa $l$, considerar **todos los bloques estrictamente por encima de ella**. Si hay masa arriba, su centro de masa horizontal debe pertenecer al **interior estricto** de la envolvente convexa de la proyección de los bloques restantes de la capa $l$. Estar en el borde ya significa caída. Si no queda masa arriba, ese corte no puede causar una caída.

La salida es `yes` y el índice de la primera operación que provoca caída, o `no` si ninguna lo hace. No se pide una simulación física de rotaciones ni de la trayectoria posterior al colapso: la regla geométrica del enunciado define por completo el resultado.

### Sistema de coordenadas que elimina $w$

Escalamos las coordenadas horizontales por $2/w$. Los centros de las tiras pasan a ser $1,3,5,\ldots,2n-1$, y sus bordes son enteros pares. Con la convención de `J.cpp`:

$$x(l,k)=\begin{cases}2k-1,&l\text{ impar},\\n,&l\text{ par},\end{cases}\qquad
 y(l,k)=\begin{cases}n,&l\text{ impar},\\2k-1,&l\text{ par}.\end{cases}$$

Se puede intercambiar globalmente X e Y sin alterar el algoritmo. El factor $w$ desaparece porque escalar uniformemente tanto centros como soportes conserva la pertenencia al interior. La coordenada vertical tampoco interviene en el criterio proporcionado: sólo se usa la proyección horizontal del centro de masa.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** después de cada eliminación, volver a recorrer todos los bloques y construir envolventes genéricas requiere al menos $O(mhn)$, hasta $2.5\cdot10^{11}$ inspecciones. Si se vuelve a sumar por separado toda la torre superior para cada corte, el costo puede subir a $O(mh^2n)$. Usar geometría convexa general sobre todas las esquinas añade trabajo que esta estructura no necesita.
- **La Observación Clave (Insight Ad-Hoc):** cada capa es un conjunto de tiras paralelas que abarcan todo el cuadrado en una dirección. Su envolvente convexa es un rectángulo determinado únicamente por el primer y el último bloque presentes. El centro de masa de la torre superior se obtiene con sumas de coordenadas y conteo, acumulados de arriba hacia abajo.

### De una envolvente bidimensional a un intervalo

Sean $L_l$ y $R_l$ los índices mínimo y máximo presentes en una capa no vacía. En la dirección corta de las tiras, la envolvente se extiende desde $2(L_l-1)$ hasta $2R_l$. En la dirección larga siempre ocupa $[0,2n]$.

Todos los centros de bloques de la torre tienen cada coordenada dentro de $[1,2n-1]$. Un promedio de coordenadas dentro de ese intervalo también está estrictamente entre 0 y $2n$. Por tanto, la condición de la dirección larga se satisface automáticamente; sólo hay que comprobar la dirección corta:

- Capa impar: comprobar coordenada X.
- Capa par: comprobar coordenada Y.

Los huecos internos de la capa no rompen el intervalo de soporte porque la regla usa la **envolvente convexa**, no la unión de las piezas. Sin embargo, al quitar una pieza interna sí cambia su masa y, por tanto, el centro de masa que ven los cortes inferiores.

### Comparar sin dividir

Si arriba hay $C>0$ bloques y suma $S$ de sus coordenadas en el eje relevante, la condición es
$$2(L_l-1)<\frac SC<2R_l.$$
Como $C$ es positivo, equivale exactamente a
$$2(L_l-1)C<S<2R_lC.$$

No hacen falta `double`, tolerancias ni raíces: las desigualdades enteras conservan el caso crítico de estar exactamente en el borde.

### Datos mínimos por capa

Mantener:

- `count[l]`: cantidad de bloques presentes;
- `sx[l], sy[l]`: suma de coordenadas de sus centros;
- `left[l], right[l]`: extremos presentes;
- una marca de eliminado por posición, para avanzar los extremos cuando desaparecen.

Inicialmente `count=n`, `sx=sy=n*n`, `left=1`, `right=n`: $1+3+\cdots+(2n-1)=n^2$, y la otra coordenada suma $n$ repetido $n$ veces.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** las sumas y el conteo de cada capa representan exactamente sus piezas restantes; los acumuladores del recorrido representan exactamente las capas **estrictamente superiores** a la capa que se está comprobando.

**Mantenimiento tras una retirada.** Restar uno del conteo y las coordenadas del bloque retirado preserva las sumas. Marcarlo eliminado y avanzar el extremo izquierdo mientras esté eliminado, y retroceder el derecho de igual modo, produce los índices mínimo y máximo presentes. Los extremos sólo se desplazan hacia dentro.

**Invariante del recorrido vertical.** Comenzamos en la capa $h$ con acumuladores $C=S_x=S_y=0$. Antes de comprobar $l$, éstos describen las capas $l+1,\ldots,h$. Se aplica el criterio de soporte usando sólo esos acumuladores. **Después** se agregan las contribuciones de la capa $l$ y se pasa a $l-1$. Añadir antes de comprobar incluiría el propio soporte dentro de la masa que debe sostener y cambiaría incorrectamente el criterio.

**Necesidad y suficiencia de la comprobación.** Si no hay masa superior, el corte no falla. Si la hay y el soporte está vacío, falla. En otro caso la envolvente rectangular queda determinada por los extremos; la dirección larga siempre es válida y la dirección corta es válida exactamente cuando pasan las dos desigualdades estrictas. Por tanto se detecta exactamente el criterio de caída del enunciado para cada corte.

**Primer instante.** Se procesa cada retirada en orden y se detiene al primer fallo de algún corte. Todas las anteriores se comprobaron estables y el estado actual es inestable, luego ese índice es la respuesta.

### No hay monotonicidad del estado geométrico para una búsqueda binaria

La primera caída es irreversible en la historia física, pero si se continuara eliminando piezas de una configuración abstracta, su centro de masa podría volver a quedar dentro del soporte. La propiedad “la configuración tras las primeras $k$ retiradas es estable” no es necesariamente monótona.

Ejemplo: $n=2,h=3$. Retirar el bloque 1 de la capa inferior deja soporte X $(2,4)$ y centro superior X igual a 2: caída por borde. Si hipotéticamente se retira después el bloque 1 de la capa superior, la masa superior queda con X promedio $(2+2+3)/3=7/3$, interior al soporte, y los otros cortes son estables. No se permite olvidar la caída anterior porque la geometría final parezca estable. Por eso se comprueban las retiradas cronológicamente.

### Discrepancia concreta del código adjunto

`J.cpp` contiene:

```cpp
if (cnt[hi] == 0) {
    ANS = quitar;
    continue;
}
```

Esto declara caída al vaciar **cualquier** capa, sin comprobar si hay masa encima. No coincide con el criterio del enunciado ni con la solución oficial `jenga_pkun.c++`, que sólo exige soporte cuando `totcnt>0`.

Contraejemplo mínimo válido:

```text
1 1
1 1
1 1
```

Hay un solo bloque, se retira y no hay ninguna torre superior que caiga: salida oficial `no`. El archivo adjunto produce `yes` y `1`. El validador oficial permite $h=n=m=1$ y esa eliminación. Otro ejemplo con torre restante: $n=1,h=2$, retirar el bloque de la capa 2; la pieza inferior queda apoyada en el suelo, así que tampoco hay caída.

Por tanto, aunque el archivo provenga de una solución reportada como aceptada, **esta copia tiene esa discrepancia verificable**. El análisis no la oculta ni modifica el original.

- **Casos Borde y Limitaciones:**
  - Una capa vacía con bloques arriba implica caída; una capa vacía sin bloques arriba, no.
  - $h=1$: sólo hay bloques sobre el suelo, sin cortes entre capas que puedan fallar.
  - $n=1$: mientras exista una pieza por capa bajo toda la masa, el centro está en el interior de su intervalo; quitar una pieza intermedia puede dejar masa sin soporte.
  - Centro exactamente en un borde implica caída. No cambiar `<` por `<=`.
  - Quitar una pieza interna no cambia extremos, pero sí los momentos que ven los pisos inferiores.
  - El centro relevante es el de **toda** la torre superior, no sólo la capa inmediatamente siguiente.
  - Las operaciones no repiten bloques, garantía del enunciado que evita descontar masa dos veces.
  - $C\le hn\le5\cdot10^7$ y los productos frontera por conteo son menores o iguales a $10^{12}$: se necesitan 64 bits. Calcular `2LL*right*count`, no multiplicar primero en 32 bits.
  - El uso de `w` únicamente al leer no es un olvido: se eliminó mediante normalización.

## 5. Traza Lógica Paso a Paso

Primer ejemplo oficial: $n=5,w=2,h=6$. Las primeras cinco retiradas son $(4,1),(4,2),(4,5),(5,3),(4,3)$.

La capa 4 es par; su eje relevante es Y. Mientras las capas 5 y 6 están completas, sus diez bloques tienen suma Y igual a 50 y centro Y igual a 5.

| Retirada | Bloques restantes en capa 4 | Intervalo Y de soporte | Masa/suma arriba de 4 | Centro Y | Resultado |
|---:|---|---|---|---:|---|
| 1: (4,1) | 2,3,4,5 | $(2,10)$ | $C=10,S_y=50$ | 5 | estable |
| 2: (4,2) | 3,4,5 | $(4,10)$ | $C=10,S_y=50$ | 5 | estable |
| 3: (4,5) | 3,4 | $(4,8)$ | $C=10,S_y=50$ | 5 | estable |
| 4: (5,3) | 3,4 | $(4,8)$ | $C=9,S_y=45$ | 5 | estable |
| 5: (4,3) | 4 | $(6,8)$ | $C=9,S_y=45$ | 5 | cae |

La cuarta retirada quita un bloque con Y=5, así que el promedio superior sigue siendo 5. La quinta estrecha el soporte sin cambiar la masa superior. La comparación exacta exige $6\cdot9<45<8\cdot9$, pero $54<45$ es falso. Las capas inferiores conservan su soporte completo y el hueco interno de la capa 5 no cambia su envolvente; ninguna cayó antes. Se emite `yes` y `5`.

## 6. Análisis de Complejidad

- **Complejidad Temporal:** inicializar las marcas de las $hn$ posiciones cuesta $O(hn)$. Cada retirada actualiza conteo y sumas en $O(1)$ y comprueba a lo sumo $h$ capas en $O(h)$, dando $O(mh)$. Los extremos avanzan monotónicamente: cada posición eliminada puede ser sobrepasada por cada extremo a lo sumo una vez. Su costo agregado es $O(m)$ para los desplazamientos sobre marcas eliminadas, y también está acotado por $O(hn)$. Total: **$O(hn+mh)$** para la representación matricial.

En los máximos hay 50 millones de marcas a inicializar y hasta 25 millones de comprobaciones de capas; el recorrido no vuelve a inspeccionar $n$ bloques por capa en cada retirada. Esta solución es suficiente para los límites; no se afirma una cota inferior que demuestre optimalidad asintótica global.

- **Complejidad Espacial:** $O(hn+h)$ con una matriz de marcas. `J.cpp` reserva $5001\cdot10001=50\,015\,001$ booleanos, unos 47.7 MiB si cada `bool` ocupa un byte. Una representación de bits reduce esa parte aproximadamente por ocho. Una alternativa dispersa guarda sólo las retiradas por capa, usando $O(h+m)$ espacio con conjuntos y sus costos de consulta; no es necesaria para explicar el algoritmo adjunto.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** sumas por capa, extremos monotónicos y una función de estabilidad que recorre desde arriba. Usar aritmética entera y tratar el soporte vacío dentro de esa función, donde se conoce si existe masa superior.

```cpp
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Para el juez original, redirigir a jenga.in y jenga.out.
    int n, w, h, m;
    cin >> n >> w >> h >> m;
    vector<vector<unsigned char>> removed(h + 1, vector<unsigned char>(n + 1, 0));
    vector<int> count(h + 1, n), left(h + 1, 1), right(h + 1, n);
    vector<ll> sx(h + 1, 1LL*n*n), sy(h + 1, 1LL*n*n);
    auto stable = [&]() {
        ll total = 0, sumx = 0, sumy = 0;
        for (int l = h; l >= 1; --l) {
            if (total > 0) {
                if (count[l] == 0) return false;
                ll sum = (l & 1) ? sumx : sumy;
                ll lo = 2LL * (left[l] - 1) * total;
                ll hi = 2LL * right[l] * total;
                if (!(lo < sum && sum < hi)) return false;
            }
            total += count[l];
            sumx += sx[l];
            sumy += sy[l];
        }
        return true;
    };
    int answer = -1;
    for (int step = 1; step <= m; ++step) {
        int l, k; cin >> l >> k;
        if (answer != -1) continue;
        --count[l];
        sx[l] -= (l & 1) ? 2LL*k - 1 : n;
        sy[l] -= (l & 1) ? n : 2LL*k - 1;
        removed[l][k] = 1;
        while (left[l] <= right[l] && removed[l][left[l]]) ++left[l];
        while (left[l] <= right[l] && removed[l][right[l]]) --right[l];
        if (!stable()) answer = step;
    }
    if (answer == -1) cout << "no\n";
    else cout << "yes\n" << answer << '\n';
}
```

### Correspondencia con `J.cpp` y aspectos de portabilidad

`cordX`, `cordY` implementan los centros normalizados. `cordXY` devuelve la coordenada variable $2k-1$. `queEjeMeInteresa` selecciona el eje corto según la paridad. `sum`, `cnt` y `extremos` son los agregados descritos. El recorrido original empieza en `h-1` y agrega `piso+1` antes de comprobar; equivale al recorrido de referencia que empieza en `h` y agrega después de comprobar.

Las cabeceras `windows.h`, `psapi.h` y `check_memory()` son diagnósticos ajenos a la solución y hacen que esta copia no compile directamente en sistemas sin la API de Windows. Los arreglos locales de tamaño dependiente de `h` son una extensión de compilador, no C++ estándar; la referencia usa `vector`. Los flujos locales `ifstream cin("jenga.in")` y `ofstream cout("jenga.out")` sí reflejan el protocolo original por archivos; se deben adaptar sólo si la plataforma de ejecución pide entrada/salida estándar.

El defecto funcional principal es el retorno por piso vacío antes del recorrido. La referencia lo corrige comprobando `count[l]==0` únicamente cuando `total>0`, y protege ambos desplazamientos de extremos con `left<=right`.

### Verificación reproducible

Comparar contra una implementación pequeña que enumere todos los bloques restantes, reconstruya su centro de masa por corte y obtenga extremos desde cero después de cada operación. Probar los tres ejemplos oficiales, $h=1$, eliminación de la capa superior completa, capa vacía intermedia y centro sobre el borde. Contrastar también contra `jenga_pkun.c++` del jurado. La primera retirada problemática debe coincidir, no sólo la estabilidad del estado final.

### Comprobaciones ejecutadas durante este análisis

La implementación de referencia incluida en este documento se extrajo y compiló con C++17 y optimización. Resultado: 3 ejemplos, 2 casos de capas vacías y 250 instancias contra enumeración geométrica y solución oficial: PASS. Las pruebas se ejecutaron localmente; no constituyen un nuevo envío al juez. Los archivos originales se conservaron sin modificaciones.

Además, se compiló una copia temporal de `J.cpp` retirando únicamente diagnósticos de Windows y adaptando la entrada/salida. El algoritmo original devolvió `yes / 1` para el contraejemplo de un solo bloque; tanto la referencia corregida como el código del jurado devolvieron `no`.
