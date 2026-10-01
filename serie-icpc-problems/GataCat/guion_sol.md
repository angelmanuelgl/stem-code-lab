# GATA-CAT - G / ICPC Latin America Championship 2026

## 1. Contexto del Concurso

- **Certamen / Fase:** ICPC Latin America Championship, campeonato latinoamericano; no es una fecha del Gran Premio de México.
- **Año / Edición:** 2026; celebrado el 7 de marzo de 2026 según la portada del documento.
- **Fuentes:** `contest_2026_championship.pdf`, portada y página física 14 (impresa 12); código adjunto `G.cpp`. Autor del problema: Humberto Díaz Suárez, Puerto Rico. No se adjuntó editorial; las demostraciones siguientes se reconstruyen a partir del enunciado y del código.
- **Límites:** hasta $Q=1000$ solicitudes; $0\le G,C\le10^6$; cada respuesta debe ser no vacía, contener sólo `C,G,A,T` y tener a lo sumo 500 caracteres.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** se quiere fabricar una secuencia de ADN con dos indicadores felinos prescritos. Un indicador cuenta `CAT` y el otro `GATA`, permitiendo saltarse nucleobases intermedias.
- **Modelo Matemático / Formal:** para una cadena $s$ de longitud $L$, definir
  $$N_{CAT}(s)=|\{(i,j,k):1\le i<j<k\le L,\ s_i=C,s_j=A,s_k=T\}|,$$
  $$N_{GATA}(s)=|\{(i,j,k,l):1\le i<j<k<l\le L,\ s_i=G,s_j=A,s_k=T,s_l=A\}|.$$
  Dados $G,C$, construir $s$ con $N_{GATA}(s)=G$, $N_{CAT}(s)=C$ y $1\le L\le500$. Se cuentan **subsecuencias por sus posiciones**, no subcadenas contiguas ni palabras distintas.

No hay función objetivo de minimización de longitud: basta una construcción dentro de la cota. Eso permite un greedy de representación sin demostrar que use el mínimo número de letras.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** probar las $4^L$ cadenas de longitud $L$ es imposible. Generar una copia de `CAT` o `GATA` por unidad puede necesitar millones de caracteres y además crea subsecuencias que cruzan copias. Una DP directa sobre los dos objetivos tendría hasta $10^{12}$ pares de contadores y ni siquiera esos dos contadores bastarían para describir el efecto de añadir una letra: también importan los prefijos parciales.
- **La Observación Clave (Insight Ad-Hoc):** fijar un esqueleto alternante de letras `A,T`, e insertar `C` y `G` en sus huecos. Cada `C` contribuye únicamente al contador CAT y cada `G` únicamente al contador GATA. Ambas contribuciones dependen sólo del número de pares `AT` que quedan a su derecha.

### Derivación de las dos familias de pesos

Sea el sufijo $(AT)^i=A_1T_1A_2T_2\cdots A_iT_i$.

Una `C` delante del sufijo permite escoger $A_a,T_b$ con $a\le b$. Para cada $T_b$ hay $b$ opciones de `A` anterior. Su contribución es
$$T_i=1+2+\cdots+i=\frac{i(i+1)}2=\binom{i+1}{2}.$$

Una `G` delante permite escoger $A_a,T_b,A_c$ con $a\le b<c$. Para cada $b$ hay $b(i-b)$ opciones, por lo que
$$V_i=\sum_{b=1}^{i}b(i-b)=\frac{(i-1)i(i+1)}6=\binom{i+1}{3}.$$

Otra derivación, idéntica a la del código: al añadir el último par `AT`, el nuevo `T` genera $i$ pares `AT`, y la nueva `A` cierra $\binom i2$ triples `ATA` del prefijo. De ahí
$$T_i=T_{i-1}+i,\qquad V_i=V_{i-1}+\frac{i(i-1)}2.$$

**Corrección de un comentario de `G.cpp`:** `GATA[i]` no cuenta `GATA` dentro de `C(AT)^i`, cadena que no contiene `G`. Cuenta `ATA` dentro de $(AT)^i$, equivalentes a los `GATA` creados por **una G colocada delante**.

### La construcción compartida

Recorrer $i=144,143,\ldots,1$. En el hueco al que seguirán exactamente $i$ pares `AT`:

1. Insertar tantas `C` como permita el residuo de $C$, pagando $T_i$ por cada una.
2. Para $i\ge2$, insertar tantas `G` como permita el residuo de $G$, pagando $V_i$ por cada una.
3. Emitir el siguiente par `AT`.

El código omite los primeros pares si aún no ha emitido ninguna letra. Desde la primera inserción emite todos los pares restantes; así una letra colocada al procesar $i$ termina teniendo exactamente $i$ pares a su derecha.

Los contadores se descomponen de forma independiente sobre **un mismo** esqueleto. Las otras `C` y `G` intercaladas no cambian el número de pares `AT` ni de triples `ATA`.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** si se insertan $a_i$ letras `C` y $b_i$ letras `G` en el hueco con $i$ pares posteriores, la cadena completa tiene exactamente
  $$N_{CAT}=\sum_{i=1}^{144}a_iT_i,\qquad N_{GATA}=\sum_{i=2}^{144}b_iV_i.$$

**Por qué es una suma sin interacciones ocultas.** Toda subsecuencia CAT tiene una única posición inicial `C`; clasificarla por esa posición particiona todas las subsecuencias. Para una `C` fija, las elecciones restantes son exactamente los pares `AT` de su sufijo. Insertar otra `C` no añade `A` ni `T`. El mismo razonamiento, usando la única `G` inicial, particiona las subsecuencias GATA. No existen términos multiplicativos entre cantidades de `C` y `G`.

**Invariante de residuos.** En cada paso, objetivo original = suma de contribuciones ya asignadas + residuo no negativo. Cada inserción resta exactamente su contribución. Al llegar a $i=1$, $T_1=1$ permite consumir cualquier residuo CAT; al llegar a $i=2$, $V_2=1$ consume cualquier residuo GATA. Los residuos finales son cero y ambas igualdades se satisfacen.

**El greedy no necesita ser óptimo en monedas.** La existencia de denominaciones de valor uno asegura representación exacta. La propiedad adicional que necesitamos es una cota de longitud, demostrada a continuación; no que las monedas sean un sistema canónico.

### Demostración analítica de la cota de 500 caracteres

El comentario que llama empírico al límite 143 no basta. En realidad, con `MAXL=145` el código empieza en **144**, y podemos demostrar una cota conservadora de **401 caracteres**.

Se emiten a lo sumo $2\cdot144=288$ letras del esqueleto.

**Cantidad de C.** $T_{144}=10440$, así que se pueden insertar a lo sumo $\lfloor10^6/10440\rfloor=95$ letras en el primer hueco. El residuo queda menor que 10440. Si para un residuo $r$ elegimos el mayor $j$ con $T_j\le r<T_{j+1}$ y restamos una vez $T_j$, el nuevo residuo es menor que
$$T_{j+1}-T_j=j+1.$$
Las siguientes cotas se encadenan:

| Cota inicial del residuo | Mayor índice posible | Cota tras una inserción |
|---|---:|---|
| $r<10440$ | 143 | $r<144$ |
| $r<144$ | 16 | $r<17$ |
| $r<17$ | 5 | $r<6$ |
| $r<6$ | 2 | $r<3$ |

El último residuo se paga con a lo sumo dos monedas de valor uno. Si un residuo ya es cero, se omiten pasos. Total: a lo sumo $95+4+2=101$ letras `C`.

**Cantidad de G.** $V_{144}=497640$, así que hay a lo sumo dos `G` en ese hueco y queda $r<497640$. Para el mayor $j$ permitido, tras restar una vez $V_j$:
$$r<V_{j+1}-V_j=T_j.$$

| Cota inicial del residuo | Mayor índice posible | Cota tras una inserción |
|---|---:|---|
| $r<497640$ | 143 | $r<10296$ |
| $r<10296$ | 39 | $r<780$ |
| $r<780$ | 16 | $r<136$ |
| $r<136$ | 9 | $r<45$ |
| $r<45$ | 6 | $r<21$ |

Para $r\le20$, las monedas disponibles relevantes son 20,10,4,1. Si $r=20$, basta una. Si $r\le19$, hay como máximo una moneda de 10, dos de 4 y tres de 1, pero las tres cantidades máximas no son simultáneas; verificando los residuos módulo 4 se obtiene como máximo cinco monedas (por ejemplo, $17=10+4+1+1+1$). Por tanto bastan $2+5+5=12$ letras `G`.

En total:
$$L\le288+101+12=401<500.$$

Esta prueba cubre todos los pares $(G,C)$ del dominio, sin depender de ensayos aleatorios. Una comprobación exhaustiva unidimensional de los conteos del greedy da máximos de 100 letras `C` y 10 letras `G`, y por tanto la cota certificada computacionalmente 398; no hace falta esa mejora para cumplir el límite.

- **Casos Borde y Limitaciones:**
  - $(G,C)=(0,0)$: el programa devuelve `CA`, válida y no vacía. Sin caso especial, la omisión del prefijo produciría una cadena vacía.
  - $G=0$ o $C=0$: se construye sólo el contador no nulo sin crear el otro.
  - $V_1=0$: nunca se debe entrar en un ciclo que reste esta cantidad; el código exige `i>=2`.
  - El orden de entrada es **G, C**, no C, G.
  - Usar `long long` en fórmulas evita desbordamientos al generalizar; con $i\le144$ las cantidades actuales son pequeñas.
  - No concatenar construcciones independientes sin analizar subsecuencias que atraviesen la frontera.
  - Los límites 144 y 500 se justifican para objetivos hasta $10^6$; un límite mayor de objetivos exige revisar la prueba.

## 5. Traza Lógica Paso a Paso

Tomemos $G=5$, $C=8$.

| $i$ | $T_i$ | $V_i$ | Inserciones | Residuos $(G,C)$ | Prefijo emitido |
|---:|---:|---:|---|---|---|
| $144\ldots4$ | al menos 10 | al menos 10 | ninguna | $(5,8)$ | vacío |
| 3 | 6 | 4 | una C, una G | $(1,2)$ | `CGAT` |
| 2 | 3 | 1 | una G | $(0,2)$ | `CGATGAT` |
| 1 | 1 | 0 | dos C | $(0,0)$ | `CGATGATCCAT` |

La primera `C` ve tres pares y aporta 6; las dos últimas ven un par y aportan 1 cada una: $6+1+1=8$. La primera `G` ve tres pares y aporta 4; la segunda ve dos y aporta 1: $4+1=5$. Las letras de otros tipos insertadas entre pares no alteran esos conteos.

## 6. Análisis de Complejidad

- **Complejidad Temporal:** con $B=144$ y longitud emitida $L$, el preprocesamiento es $O(B)$ y cada caso cuesta $O(B+L)$. Cada iteración de un `while` imprime una letra, por lo que su costo está incluido en $L$, no en $10^6$. Para $Q$ casos: $O(B+QB+\sum L_q)$. La escritura tiene cota inferior $\Omega(\sum L_q)$; no se afirma que se minimice la longitud.
- **Complejidad Espacial:** $O(B)$ para tablas. El código original imprime directamente y usa $O(1)$ adicional por caso. Si se guarda la respuesta para verificar longitud antes de imprimir, se usan $O(L)$ adicionales.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** dos tablas de pesos y un único recorrido descendente. Cambiar repeticiones por cocientes hace explícita la representación, aunque los `while` del original ya son eficientes por la cota de salida.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long T[145]{}, V[145]{};
    for (int i = 1; i <= 144; ++i) {
        T[i] = T[i-1] + i;
        V[i] = V[i-1] + 1LL*i*(i-1)/2;
    }
    int q; cin >> q;
    while (q--) {
        long long g, c; cin >> g >> c;
        string out;
        bool started = false;
        for (int i = 144; i >= 1; --i) {
            long long nc = c / T[i];
            c %= T[i];
            long long ng = (i >= 2 ? g / V[i] : 0);
            if (i >= 2) g %= V[i];
            out.append(static_cast<size_t>(nc), 'C');
            out.append(static_cast<size_t>(ng), 'G');
            started = started || nc > 0 || ng > 0;
            if (started) out += "AT";
        }
        if (out.empty()) out = "CA";
        cout << out << '\n';
    }
}
```

### Correspondencia con `G.cpp`

`CAT` es $T$; `GATA` es $V$; `cnt` y `cnt2` son las multiplicidades; `algun` indica que el esqueleto ya comenzó. La condición con `algun` es esencial: incluso cuando no se inserta nada en un hueco posterior, hay que imprimir su `AT` para cumplir los pesos ya asignados. Las utilidades PBDS, el generador aleatorio, `MOD` y las funciones de depuración no participan en la solución. La macro `all` está mal formada, pero no se utiliza y no afecta a este programa.

### Verificador independiente

Para contar subsecuencias de un patrón $p$ de longitud $k$, inicializar `ways[0]=1`, los otros ceros. Por cada letra `x` de la respuesta, recorrer $j=k-1,\ldots,0$ y, si `p[j]==x`, sumar `ways[j]` a `ways[j+1]`. El recorrido descendente impide reutilizar la misma posición para dos letras del patrón, especialmente las dos `A` de GATA. Ejecutarlo para CAT y GATA, comprobar ambos objetivos y $1\le L\le500$. Su costo es $O(L)$ porque los patrones tienen longitud constante.

### Comprobaciones ejecutadas durante este análisis

La implementación de referencia incluida en este documento se extrajo y compiló con C++17 y optimización. Resultado: 1000 construcciones verificadas; residuos 0..1000000 de ambas familias, máximos 100/10: PASS. Las pruebas se ejecutaron localmente; no constituyen un nuevo envío al juez. Los archivos originales se conservaron sin modificaciones.
