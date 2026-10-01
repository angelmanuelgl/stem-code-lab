# Diabolic Doofenshmirtz - D / GCPC 2022

## 1. Contexto del Concurso

- **Certamen / Fase:** German Collegiate Programming Contest (GCPC), concurso alemán del circuito de programación competitiva ICPC. No corresponde a una fecha del Gran Premio de México.
- **Año / Edición:** 2022.
- **Fuentes:** `problemset.pdf`, páginas físicas 9–10 (numeración impresa 7–8); `solutions.pdf`, páginas físicas 18–23. Autor del problema: Michael Zündorf. [Editorial oficial](https://2022.gcpc.nwerc.eu/solutions.pdf). No se adjuntó código: el programa de la sección 7 es una implementación de referencia derivada aquí.
- **Límites relevantes:** 1 segundo; longitud desconocida entre 1 y $10^{12}$; tiempos enteros menores que $10^{18}$; a lo sumo 42 mensajes de consulta, **incluida la respuesta final**.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** Perry recorre una pista circular a velocidad constante de un metro por segundo. Doofenshmirtz puede medir su posición dentro de la vuelta, pero necesita deducir la longitud de la pista con pocas mediciones y sin retroceder en el tiempo.
- **Modelo Matemático / Formal:** existe un entero fijo desconocido $L\in[1,10^{12}]$. Una consulta en un entero $t\in[0,10^{18})$ devuelve
  $$r(t)=t\bmod L=t-L\lfloor t/L\rfloor.$$
  Si se realizan $q$ mediciones, deben satisfacer $t_1<t_2<\cdots<t_q$. Se debe recuperar exactamente $L$ y emitir `! L`, con $q+1\le42$.

Una respuesta $r=t$ equivale a $t<L$. Si $r<t$, sabemos que $L\mid(t-r)$, pero **en general no** que $L=t-r$: podría haber transcurrido más de una vuelta. La dificultad no consiste en detectar cualquier vuelta, sino en hacer que la primera medición que detecta una vuelta corresponda exactamente a una.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** consultar $1,2,3,\ldots$ hasta observar cero descubre $L$, pero requiere $\Theta(L)$ mediciones: hasta un billón, frente al presupuesto de 41 mediciones más respuesta. Enumerar divisores de $t-r$ tras una consulta enorme tampoco identifica necesariamente el divisor correcto. Una búsqueda binaria ordinaria sobre la propiedad $t<L$ puede pedir después un tiempo menor que uno ya utilizado y viola el protocolo.
- **La Observación Clave (Insight Ad-Hoc):** buscar un tiempo $t$ dentro de $[L,2L)$. En ese intervalo $\lfloor t/L\rfloor=1$, luego $L=t-r(t)$.

### Cómo diseñar los tiempos, en vez de adivinarlos

Supongamos que la última consulta fue $u$ y devolvió $u$. Entonces $L\ge u+1$. Si la próxima consulta se fija en
$$t=2u+1,$$
se garantiza $t\le2L-1<2L$. Hay únicamente dos posibilidades:

1. $t<L$: no hubo vuelta; la respuesta sigue siendo $t$ y se fortalece la cota inferior.
2. $L\le t<2L$: hubo exactamente una vuelta; la diferencia revela $L$.

Partiendo de $t=1$ obtenemos $1,3,7,15,31,63,\ldots$, es decir, $t_k=2^k-1$. El término `+1` aprovecha que $L$ es entero y permite el mayor salto compatible con esta garantía.

No hace falta construir un conjunto de candidatos, calcular un MCD ni resolver congruencias. Se conserva una sola cota implícita en el tiempo actual.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** antes de la consulta $t_k=2^k-1$, si las consultas anteriores no terminaron el algoritmo, entonces $L\ge2^{k-1}$.

**Base, $k=1$.** La restricción $L\ge1$ da $t_1=1<2L$.

**Paso inductivo.** Si la consulta anterior devolvió $r=t_{k-1}$, entonces $L>2^{k-1}-1$, por lo que, al ser entero, $L\ge2^{k-1}$. Así,
$$t_k=2^k-1<2L.$$
Si ahora $r<t_k$, necesariamente $L\le t_k$. Combinando ambas desigualdades:
$$L\le t_k<2L\implies r=t_k-L\implies t_k-r=L.$$
Si $r=t_k$, entonces $L\ge t_k+1=2^k$ y se mantiene el invariante para el siguiente paso.

**Terminación.** Existe un primer $k$ con $2^k-1\ge L$. Ese valor es
$$k=\lceil\log_2(L+1)\rceil.$$
Como $2^{40}-1=1\,099\,511\,627\,775>10^{12}$, son necesarias a lo sumo 40 mediciones, más la respuesta final: **41 mensajes**, dentro del límite 42. El mayor tiempo usado es además mucho menor que $10^{18}$.

**Ausencia de ambigüedad.** La primera respuesta distinta del tiempo no se interpreta aislada: se usa junto con la última cota inferior. Esa información excluye todos los múltiplos $2L,3L,\ldots$ que podrían contaminar la diferencia.

- **Casos Borde y Limitaciones:**
  - $L=1$: `? 1` responde 0; se termina con `! 1`.
  - $L=2^a-1$: la consulta exacta responde 0 y se recupera ese mismo tiempo.
  - $L=2^a$: la consulta anterior $2^a-1$ aún no detecta vuelta; $2^{a+1}-1$ responde $L-1$ y revela $L$.
  - `int` de 32 bits no alcanza. Todos los tiempos, residuos y diferencias deben ser de 64 bits.
  - Consultar cero es legal, pero no aporta información porque siempre responde cero.
  - Los tiempos deben ser **estrictamente** crecientes. La actualización `2*t+1` lo asegura.
  - Es obligatorio vaciar el búfer después de cada mensaje. Un algoritmo matemáticamente correcto puede bloquearse sin `flush`.
  - No imprimir explicaciones ni depuración en la salida del protocolo. Ante fin de entrada se debe terminar.
  - La prueba depende de longitud entera y constante, velocidad conocida y residuo exacto; no se traslada sin cambios a mediciones ruidosas.

## 5. Traza Lógica Paso a Paso

Supongamos $L=42$, desconocido para el programa.

| Medición | Tiempo $t$ | Respuesta $r$ | Información deducida |
|---:|---:|---:|---|
| 1 | 1 | 1 | $L\ge2$ |
| 2 | 3 | 3 | $L\ge4$ |
| 3 | 7 | 7 | $L\ge8$ |
| 4 | 15 | 15 | $L\ge16$ |
| 5 | 31 | 31 | $L\ge32$ |
| 6 | 63 | 21 | $L\le63$ y ya sabíamos $L\ge32$ |

En la última fila, $63<2\cdot32\le2L$. Por tanto $63-21=42$ es una vuelta completa, no varias. Se imprime `! 42` y se termina. Son siete mensajes contando la respuesta.

Ejemplo de por qué no sirve cualquier consulta grande: si $L=6$, consultar directamente 20 devuelve 2. La diferencia 18 es $3L$, no $L$.

## 6. Análisis de Complejidad

- **Complejidad Temporal:** $O(\log L)$ operaciones aritméticas y consultas; cada iteración hace una comparación y, si hace falta, una multiplicación por dos y una suma. La complejidad importante es el número de interacciones, a lo sumo 40 mediciones. En modelo de bits, imprimir enteros de hasta $O(\log L)$ bits introduce el correspondiente costo de representación; el análisis de concurso usa enteros de máquina de 64 bits.
- **Complejidad Espacial:** $O(1)$ auxiliar: únicamente tiempo y residuo. No se almacena el historial.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** un bucle con una consulta, una condición de éxito y la actualización del tiempo. El invariante vive en la secuencia de tiempos, no en una estructura de datos.

```cpp
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t = 1;
    while (true) {
        cout << "? " << t << endl; // endl imprime salto y hace flush
        long long r;
        if (!(cin >> r)) return 0;
        if (r < 0 || r > t) return 0; // respuesta fuera del dominio
        if (r != t) {
            cout << "! " << t - r << endl;
            return 0;
        }
        t = 2 * t + 1;
    }
}
```

### Correspondencia entre el código y la prueba

1. `t=1` establece la base $t<2L$.
2. `r==t` certifica $L\ge t+1$; sólo en este caso se aumenta el tiempo.
3. `r!=t` certifica al menos una vuelta. El invariante certifica a lo sumo una.
4. `return 0` tras `!` respeta la terminación inmediata requerida.

### Verificación reproducible

Se puede sustituir el juez por `r=t%L` y comprobar, para cada $L$ pequeño y para $10^{12}$ y vecinos de potencias de dos, que la respuesta es exacta, que los tiempos aumentan, que no alcanzan $10^{18}$ y que mediciones más respuesta no superan 42. Esto prueba la implementación en esos casos; la cobertura de todos los enteros proviene de la inducción anterior.

### Comprobaciones ejecutadas durante este análisis

La implementación de referencia incluida en este documento se extrajo y compiló con C++17 y optimización. Resultado: 100000 longitudes consecutivas, extremos/potencias de dos; 30 conversaciones con el ejecutable: PASS. Las pruebas se ejecutaron localmente; no constituyen un nuevo envío al juez. Los archivos originales se conservaron sin modificaciones.
