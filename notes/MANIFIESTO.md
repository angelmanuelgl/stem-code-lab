# Manifiesto y Taxonomía del Canal: STEM-Code-Lab

Este documento establece la visión estratégica, el diseño pedagógico, las normas de calidad y la taxonomía **exacta** de contenido para el proyecto de divulgación en matemáticas, ciencias de la computación y física teórica.

## 0. Indice

1. Filosofía Educativa e Intención Fundamental
2. Estilo Visual, Motivo y Estética (Manim)
3. Taxonomía de Categorías de Contenido

## 1. Filosofía Educativa e Intención Fundamental

### Propósito y Misión
*   **El "Momento Eureka" Visual:** Romper con los pizarrones aburridos y densos sin dejar el rigor. Transmitir la intuición profunda, la elegancia geométrica y el *core insight* (la idea brillante) detrás de conceptos avanzados, superando la demostración mecánica y la "talacha" de código innecesaria.
*   **El Punto Medio Estratégico:** Evitar los dos extremos fallidos de la divulgación en YouTube:
    1.  *La divulgación ultra superficial:* Basada en analogías vacías o clichés de cultura pop que no aportan valor técnico.
    2.  *El formato universitario tradicional:* Lleno de rigor formal denso ($\epsilon$-$\delta$), tedioso y sin intuición espacial o geométrica.
*   **Standard de Alto Nivel:** Mantener un estándar matemático y computacional universitario/competitivo real (nivel Licenciatura Avanzada / Posgrado CIMAT).

### Público Objetivo
*   Estudiantes universitarios y graduados de carreras STEM (Ciencias de la Computación, Matemáticas, Física).
*   Competidores y entrenadores de Programación Competitiva (ICPC, Codeforces).
*   **Mentes curiosas** y profesionales del software que buscan profundidad técnica real en habla hispana.


### Publico para captar
* Captar a primaria/secundaria/preparatoria para que se interesen en STEM

---

## 2. Estilo Visual, Motivo y Estética (Manim)

*   **100% Animado por Código:** En la categoría principal, todo el contenido visual se construye mediante animaciones vectoriales programadas en **Manim (Community Edition)**. No hay tomas en cámara, pizarrones físicos ni vlogs de campo estilo *Veritasium*.
*   **Estética "Modern Dark / Slate":**
    *   **Fondo Principal:** Gris muy oscuro con matiz azul pizarra (`#181C24` / *Slate Gray*) para prevenir fatiga visual y mantener un alto contraste cromático.
    *   **Paleta Cromática Semántica:** Ausencia de colores neón o primarios saturados por defecto. Uso de tonos sobrios y desaturados (vino/borgoña `#C0392B`, menta/verde sabio `#2DD4BF`, terracota `#D97706`, índigo `#6366F1`) con roles funcionales fijos para guiar la atención del espectador.
*   **Referentes Visuales:** Inspiración explícita en la claridad expositiva y elegancia de *3

### Mis referentes:
(agregue links a los que no son tan conocidos)

**Mates con Manim:**
* Blue1Brown
* Mates Mike
* Fee Phi Fo Fum: https://youtube.com/@feephifofum?si=gCTcaRcFIicL4zCC
* Topos Atipicos: https://youtube.com/@toposatipicos?si=9KNn5rGGgRfVWyEf


**Mates no Manim:**
* Gegiojon: https://youtube.com/@gegiojon1?si=BfYqTADpkE3faUAw
* Webgoatguy: https://youtube.com/@webgoatguy?si=UBmibfJuZHk8xCym

**Divulgacion:**
* Quantum Fracture
* Mark Rober
* Veritasium
* SiencieClic
* Primer

**Codigo**
* Optozorax: https://youtube.com/@optozorax_en?si=YHza3zCjxhHY4dZg
* Artem Kiranow: https://youtube.com/@artemkirsanov?si=WRMJxs2SmhXt8zaE
* Kishimishu: https://youtube.com/@kishimisu?si=BOJhni_4FzTFxrRZ
* Pezza's Work: https://youtube.com/@pezzzaswork?si=TWBqPLOxnis-hfko


**Computer Science**
* https://youtube.com/@polylogcs?si=TT1DkhKtcSNjSSEh

### Otros:

**Productividad/Work**
* Reysu https://youtube.com/@reysu?si=ja-s00De2gz5Hij3
* Chuen https://youtube.com/@chuenl?si=re2zxeSs04_AIEc9

**Evitar:** 

Videos hablando a camara sin recursos:
* Javier Santolalla


---

## 3. Taxonomía de Categorías de Contenido

Para evitar la contaminación temática y la pérdida de foco narrativo, todo video producido debe clasificarse de forma unívoca bajo una de las siguientes cuatro categorías:


### Categoría 1: Animaciones Matemáticas y Computacionales Puras (El Núcleo / *Core*)
*   **Definición Exacta:** Videos de divulgación formal, rigurosa y 100% animada por código (Manim), enfocados en desentrañar la intuición profunda de algoritmos, análisis matemático, probabilidad avanzada, álgebra o física teórica.
*   **Qué SÍ incluye:**
    *   Explicaciones paso a paso de teoremas, pruebas conceptuales y algoritmos (ej. Exponenciación Binaria, KMP, Convergencias Estocásticas, SVD).
    *   Visualizaciones geométricas y simulación de flujos lógicos o estocásticos.
    *   Uso de guiones técnicos en Markdown (`guion.md`) y estructura modular en Python (`scene_01_*.py`).
*   **Qué NO incluye:**
    *   Cámaras reales, pizarrón físico, momentos de ocio personal o tomas en la calle.
    *   Explicaciones superficiales sin sustento formal detrás.

### Categoría 2: Diarios de Investigación y Desarrollo de Software Académico (*Behind the Scenes*)
*   **Definición Exacta:** Bitácoras de ingeniería y desarrollo intelectual enfocadas en el proceso de resolver problemas del mundo real: desde la consultoría de simulaciones numéricas en el CIMAT hasta la redacción de artículos científicos y la preparación competitiva de alto rendimiento.
*   **Qué SÍ incluye:**
    *   Desglose técnico de cómo atacar un bache analítico o un cuello de botella de rendimiento en código científico.
    *   Metodología de organización personal y el paso de la teoría abstracta a la implementación computacional práctica.
    *   Reflexiones sobre el rigor de la licenciatura/posgrado en matemáticas y la gestión del razonamiento bajo presión.
*   **Qué NO incluye:**
    *   Vlogs costumbristas ("estudiante tomando café" u ocio sin contenido técnico).
    *   Quejas informales sobre la universidad o proyectos; todo conflicto debe estar ligado a un reto intelectual real.

### Categoría 3: Mini-Documentales de Eventos Académicos y Concursos (*Event Coverage*)
*   **Definición Exacta:** Cobertura documental y de análisis en formato corto (10–20 minutos) centrada en la cultura, la atmósfera, los retos de ingeniería y la tensión intelectual de eventos de programación competitiva (ICPC) o congresos matemáticos.
*   **Qué SÍ incluye:**
    *   El antes, durante y la autopsia mental posterior de un concurso o examen con los participantes.
    *   Entrevistas técnicas e informales sobre las estrategias empleadas en los problemas.
    *   La realidad humana tras el alto rendimiento académico y algorítmico.
*   **Qué NO incluye:**
    *   Vlogs de viajes o turismo (mostrar hoteles, aeropuertos o comidas ajenas al concurso).
    *   Reportajes superficiales ("miren qué divertido") que ignoren el peso técnico del evento.

### Categoría 4: Cápsulas de Divulgación Académica / Seminarios Sintetizados (*Teaser Talks*)
*   **Definición Exacta:** Versiones condensadas, re-editadas y adaptadas para YouTube de charlas técnicas, seminarios o exposiciones formales impartidas en entornos académicos (CIMAT, conferencias, etc.).
*   **Qué SÍ incluye:**
    *   Disección de un resultado matemático o computacional específico extraído de una presentación larga (40 min), sintetizado en un bloque dinámico de 8 a 12 minutos.
    *   Inclusión de inserciones de pantalla y apoyos visuales para adaptar el contenido de nivel investigación/maestría a una audiencia digital.
*   **Qué NO incluye:**
    *   Subir grabaciones crudas de 40 minutos con cámara fija apuntando a un proyector o pizarrón distante.

---

## 4. Regla de Oro y Protocolo de Validación (Filtro por Contradicción)

Antes de iniciar cualquier fase de producción (guion, animación o grabación), se debe aplicar la siguiente prueba de validación:

> **¿Este video pertenece inequívocamente a la definición operativa de UNA sola de las 4 categorías, o estoy mezclando formatos de manera improductiva?**

*   Si la respuesta indica una mezcla no intencionada (ej. insertar un vlog de rutina personal dentro de un desarrollo técnico puro en Manim), el proyecto **se detiene, se re-delimita o se rechaza**.
*   Todo el contenido del canal se mantendrá en un **único canal oficial**, organizado mediante listas de reproducción (*playlists*) dedicadas para cada una de las 4 categorías taxonomizadas.

---

## 5. Estructura y Arquitectura del Repositorio (`stem-code-lab`)

```text
stem-code-lab/
├── .gitignore
├── README.md                           # Presentación general del proyecto
├── collect_videos.py                   # Script de automatización/recolección
│
├── notes/                              # Bitácoras, guías y documentos internos
│   └── MANIFIESTO.md                   # Taxonomía, intenciones y reglas del canal
│
├── styles/                             # Recursos globales y configuración visual
│   └── theme.py                        # Constantes de paleta y estilos de Manim
│
├── computerscience-standalone/         # Temas sueltos de ciencias de la computación
│   └── 01-exponenciacion-binaria/      # Proyecto base modular de 10 escenas
│       ├── IMPLEMENTACION.md
│       ├── guion.md                    # guion indicado animaciones y todo
│       ├── voz.md                      # guion con voz   
│       ├── scene_01_name.py            # asi para cada escena
│       ├── ....           
│       ├── scene_12_name.py            # asi para cada escena
│       ├── render_all.py               # renderiza todas las escena
│       └── media/                      # (Ignorado por Git)
│
├── math-standalone/                    # Videos sueltos de matemáticas puras
├── serie-probability/                  # Teoría de la Medida y Procesos Estocásticos
├── serie-calculus/                     # Serie de Cálculo Diferencial e Integral
│
└── serie-icpc-problems/                # Colección y análisis para programación competitiva
    ├── analisis_historial_problemas.md
    ├── como_elegir_problemas.md
    ├── sugerencias_42_problemas.md
    └── [carpetas_por_problema]/        # DiabolicDoofenshmirtz, Door1, GataCat, etc.
```