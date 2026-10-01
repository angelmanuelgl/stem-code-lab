# Hardcore Hangman - H / GCPC 2022

## 1. Contexto del Concurso

- **Certamen / Fase:** German Collegiate Programming Contest (GCPC), concurso alemán del circuito ICPC.
- **Año / Edición:** 2022.
- **Fuentes:** `problemset.pdf`, páginas físicas 17–18 (impresas 15–16); `solutions.pdf`, páginas físicas 25–28. Autor: Marcel Wienöbst. [Editorial oficial](https://2022.gcpc.nwerc.eu/solutions.pdf). No hay código adjunto; se desarrolla abajo una implementación de referencia.
- **Límites:** 2 segundos; palabra no vacía de longitud $n\le10^4$; 26 letras minúsculas; máximo siete mensajes de consulta incluyendo la respuesta.

## 2. Abstracción Formal del Problema

- **Narrativa (Cuentito):** se juega ahorcado, pero cada intento puede contener un conjunto de letras. El juez devuelve las posiciones que contienen alguna de ellas, sin decir cuál corresponde a cada posición.
- **Modelo Matemático / Formal:** hay una cadena fija $s\in\Sigma^n$, $\Sigma=\{a,\ldots,z\}$ y $1\le n\le10^4$, inicialmente desconocida incluso en longitud. Una consulta a un conjunto $Q\subseteq\Sigma$ devuelve
  $$R(Q)=\{j\in\{1,\ldots,n\}:s_j\in Q\}.$$
  El protocolo escribe `? letras` con caracteres distintos, y recibe primero $k=|R(Q)|$ y luego $k$ índices de base uno. El objetivo es escribir `! s`. El juez responde `correct` o `incorrect`; se termina después de la respuesta correcta.

Cada consulta da **un bit de información por posición**, no un bit para toda la palabra. El indicador de pertenencia de cada índice se procesa por separado.

## 3. Solución Naive vs. La "Idea Brillante" (Insight)

- **Aproximación Obvia / Fuerza Bruta:** preguntar por las letras una a una requiere hasta 26 consultas y otra para contestar; excede siete. Enumerar cadenas es aún peor: hay $26^n$ posibilidades para una longitud fija. Dividir recursivamente letras sin compartir consultas entre posiciones desperdicia el paralelismo que permite el oráculo.
- **La Observación Clave (Insight Ad-Hoc):** asignar a cada letra una firma binaria distinta. Con cinco bits existen $2^5=32$ firmas, suficientes para 26 letras. La consulta $b$ incluye todas las letras cuyo bit $b$ vale uno. Los cinco indicadores recibidos en una posición forman exactamente la firma de su letra.

### Versión del editorial: siete mensajes

1. Consultar todo el alfabeto para obtener $n$.
2. Codificar las letras con los enteros $0,\ldots,25$.
3. Hacer cinco consultas, una por bit.
4. Emitir la palabra: $1+5+1=7$ mensajes.

El código cero es legal en esta versión porque ya sabemos qué posiciones existen. Una posición ausente de las cinco respuestas corresponde a `a`.

### Refinamiento: seis mensajes y longitud sin consulta adicional

Asignar ahora `a=1`, `b=2`, ..., `z=26`. Todas las firmas son **no nulas**. Por ello cada posición aparece en alguna de las cinco respuestas. La unión de sus índices es exactamente $\{1,\ldots,n\}$ y su máximo revela $n$.

Se hace simultáneamente la identificación de letras y la identificación de posiciones existentes. Esto ahorra la consulta de todo el alfabeto. El editorial menciona que existe una solución con seis consultas; aquí se explicita la construcción.

No usar códigos $0,\ldots,25$ sin la consulta de longitud: una palabra formada por `a` produciría cinco respuestas vacías y sería imposible conocer su longitud.

## 4. Demostración y Corrección Formal

- **Invariante o Argumento de Corrección:** denotemos $c(\ell)=1+(\ell-a)$ y
  $$Q_b=\{\ell\in\Sigma: c(\ell)\mathbin{\&}(1\ll b)\ne0\},\quad b=0,\ldots,4.$$
  Se inicializa $M_j=0$ y, al recibir una posición $j$ en la respuesta $b$, se realiza $M_j\gets M_j\mathbin{|}(1\ll b)$.

**Invariante parcial.** Tras consultar los bits $0,\ldots,b$, $M_j$ coincide con los $b+1$ bits bajos de $c(s_j)$, y los restantes bits siguen en cero. Cada posición está en $R(Q_b)$ si y sólo si ese bit de su código vale uno. Por tanto la actualización por OR establece exactamente el bit correcto, sin afectar a los anteriores.

**Identificación.** Tras cinco consultas, $M_j=c(s_j)$. La aplicación $c$ es inyectiva sobre las 26 letras, así que `char('a'+M[j]-1)` recupera la letra única.

**Longitud.** Ningún código es cero, luego cada posición pertenece al menos a una respuesta. No hay índices ficticios porque el juez sólo devuelve posiciones reales. Por tanto el máximo índice recibido es exactamente $n$. No hace falta que las respuestas estén ordenadas.

**Presupuesto.** Son cinco consultas de conjuntos y una respuesta final: seis mensajes, menores o iguales a siete.

**Límite informativo.** Si sólo se usan consultas de pertenencia a conjuntos para identificar una letra arbitraria en una palabra de longitud uno, cuatro respuestas binarias distinguen a lo sumo $2^4=16<26$ casos, incluso si se eligen adaptativamente. Se necesitan al menos cinco consultas de este tipo para identificar la letra antes de emitir la respuesta. Esta observación justifica la cantidad de bits; no depende de asumir una distribución aleatoria de palabras.

- **Casos Borde y Limitaciones:**
  - $n=1$, tanto `a` como `z`: sus códigos son no nulos y aparecen en alguna respuesta.
  - Una palabra con una sola letra repetida: todas sus posiciones reciben la misma firma; no se confunden entre sí.
  - Una respuesta vacía es válida; simplemente no se actualiza ninguna máscara.
  - La última posición puede aparecer sólo en uno de los cinco conjuntos; no se debe fijar prematuramente la longitud.
  - Usar cinco bits basta para 26; para un alfabeto general de tamaño $\sigma$, códigos no nulos requieren $\lceil\log_2(\sigma+1)\rceil$ bits.
  - El protocolo devuelve índices de base uno. Convertirlos a base cero exige hacerlo consistentemente.
  - El juez entrega primero el número de índices: no confundirlo con longitud salvo al consultar el alfabeto completo.
  - Cada consulta debe contener letras distintas. Generarla recorriendo una vez el alfabeto lo garantiza.
  - Se necesita `flush`; no hay cadena inicial que leer antes de preguntar.

## 5. Traza Lógica Paso a Paso

Palabra oculta: `banana`, de longitud desconocida.

Los códigos relevantes son `a=1=00001`, `b=2=00010`, `n=14=01110` (escritura de bit alto a bajo).

| Bit consultado | Letras relevantes incluidas | Respuesta del juez | Máscaras después de procesarla |
|---:|---|---|---|
| 0 | a | 2,4,6 | $[0,1,0,1,0,1]$ |
| 1 | b,n | 1,3,5 | $[2,1,2,1,2,1]$ |
| 2 | n | 3,5 | $[2,1,6,1,6,1]$ |
| 3 | n | 3,5 | $[2,1,14,1,14,1]$ |
| 4 | ninguna de a,b,n | vacía | sin cambios |

Las consultas reales incluyen todas las letras con el bit correspondiente, no sólo las que aparecen en esta tabla. El máximo índice observado es 6. Decodificar $[2,1,14,1,14,1]$ produce `banana`, por lo que se envía `! banana` y se lee el veredicto.

## 6. Análisis de Complejidad

- **Complejidad Temporal:** cinco recorridos de 26 letras para formar consultas, a lo sumo $5n$ índices recibidos y $n$ decodificaciones: $O(26\cdot5+5n)=O(n)$ para este alfabeto fijo. El volumen total de datos recibidos también es $O(n)$. Para alfabeto variable sería $O((n+\sigma)\log(\sigma+1))$ con la construcción directa.
- **Complejidad Espacial:** $O(n)$ para las máscaras y la respuesta. Reservar el máximo permitido usa $10^4+1$ enteros, unos 40 KB, además de la cadena. Una implementación que crece según el mayor índice conserva el mismo orden asintótico.

## 7. Ficha de Implementación Elegante

- **Enfoque de codificación:** cinco consultas estáticas, una máscara por posición y un máximo de índices. No se necesitan conjuntos de candidatos ni búsquedas de letras después de las consultas.

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> mask(10001, 0);
    int n = 0;
    for (int b = 0; b < 5; ++b) {
        string query;
        for (int c = 1; c <= 26; ++c)
            if (c & (1 << b)) query += char('a' + c - 1);
        cout << "? " << query << endl;
        int k;
        if (!(cin >> k) || k < 0) return 0;
        for (int j = 0; j < k; ++j) {
            int pos;
            if (!(cin >> pos) || pos < 1 || pos > 10000) return 0;
            n = max(n, pos);
            mask[pos] |= 1 << b;
        }
    }
    string answer;
    for (int j = 1; j <= n; ++j) {
        if (mask[j] < 1 || mask[j] > 26) return 0;
        answer += char('a' + mask[j] - 1);
    }
    cout << "! " << answer << endl;
    string verdict;
    cin >> verdict;
    return 0;
}
```

### Lectura del código

`c` es la identidad binaria de una letra; `b` decide cuál coordenada de esa identidad se pregunta. `mask[pos]` acumula las respuestas afirmativas para una posición. El OR no cuenta apariciones: reconstruye bits. `n=max(n,pos)` aprovecha las firmas no nulas. El chequeo de máscaras detecta una conversación inconsistente; en una interacción válida nunca falla.

### Verificación reproducible

Un simulador puede formar $R(Q_b)$ directamente a partir de una palabra conocida, pasar los índices al mismo decodificador y comparar la salida con la palabra original. Incluir las 26 letras, repeticiones, palabras de longitud uno y una de longitud $10^4$. La prueba de inyectividad anterior cubre las demás cadenas sin enumerar $26^n$ posibilidades.

### Comprobaciones ejecutadas durante este análisis

La implementación de referencia incluida en este documento se extrajo y compiló con C++17 y optimización. Resultado: 30 conversaciones, incluyendo longitud 10000 y alfabeto completo: PASS. Las pruebas se ejecutaron localmente; no constituyen un nuevo envío al juez. Los archivos originales se conservaron sin modificaciones.
