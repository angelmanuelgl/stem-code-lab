from manim import *


class BaseProceso(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        self.intro()
        self.circuito()
        self.sedes_y_reloj()
        self.clasificacion()
        self.desempate()
        self.final_y_repechaje()
        self.cierre()

    def clear_scene(self):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.35)

    def title(self, text):
        return Tex(text, color=WHITE).scale(0.72).to_edge(UP, buff=0.5)

    def intro(self):
        q = Tex(r"Pero... ¿cómo funciona todo esto realmente?", color=WHITE).scale(0.75)
        self.play(Write(q), run_time=1.2)
        self.wait(1)
        self.play(FadeOut(q))

    def circuito(self):
        heading = self.title(r"El camino a la Gran Final Mexicana")
        icpc = Tex(r"ICPC", color=WHITE).scale(1.05)
        gp = Tex(r"Gran Premio", color=WHITE).scale(0.75)
        final = Tex(r"Gran Final Mexicana", color=WHITE).scale(0.75)
        nodes = VGroup(icpc, gp, final).arrange(RIGHT, buff=1.15).shift(0.35 * DOWN)
        arrows = VGroup(*[
            Arrow(nodes[i].get_right(), nodes[i + 1].get_left(), color=WHITE, buff=0.15)
            for i in range(2)
        ])
        self.play(FadeIn(heading), FadeIn(icpc), run_time=0.6)
        self.play(GrowArrow(arrows[0]), FadeIn(gp), run_time=0.7)
        self.play(GrowArrow(arrows[1]), FadeIn(final), run_time=0.7)
        dates = VGroup(*[Tex(f"Fecha {i}", color=WHITE).scale(0.55) for i in range(1, 4)])
        dates.arrange(RIGHT, buff=0.7).next_to(gp, DOWN, buff=0.75)
        repechaje = Tex("Repechaje", color=WHITE).scale(0.55).next_to(dates, DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(d) for d in dates], lag_ratio=0.2), FadeIn(repechaje))
        self.wait(1.5)
        self.clear_scene()

    def sedes_y_reloj(self):
        heading = self.title(r"Universidades sede en México")
        # Silueta esquemática a partir de coordenadas geográficas (lon/lat),
        # sin fronteras estatales. La península de Baja California va separada.
        shift = LEFT * 3.80 + DOWN * 0.05
        sx, sy = 0.265, 0.235
        def xy(lon, lat):
            return shift + RIGHT * ((lon + 112) * sx) + UP * ((lat - 23) * sy)

        outline = [
            (-97.139908, 25.870001),
            (-97.527962, 24.992140),
            (-97.702942, 24.272341),
            (-97.775955, 22.932581),
            (-97.872269, 22.444220),
            (-97.699020, 21.898689),
            (-97.388870, 21.411011),
            (-97.189323, 20.635441),
            (-96.525574, 19.890940),
            (-96.292091, 19.320379),
            (-95.900879, 18.828020),
            (-94.839027, 18.562719),
            (-94.425697, 18.144381),
            (-93.548630, 18.423840),
            (-92.786034, 18.524839),
            (-92.037346, 18.704571),
            (-91.407883, 18.876080),
            (-90.771828, 19.284121),
            (-90.533562, 19.867420),
            (-90.451363, 20.707529),
            (-90.278519, 20.999840),
            (-89.601318, 21.261730),
            (-88.543777, 21.493679),
            (-87.658356, 21.458851),
            (-87.051880, 21.543550),
            (-86.811920, 21.331520),
            (-86.845871, 20.849859),
            (-87.383202, 20.255421),
            (-87.621002, 19.646561),
            (-87.436676, 19.472389),
            (-87.586525, 19.040131),
            (-87.837135, 18.259809),
            (-88.090614, 18.516640),
            (-88.299957, 18.499990),
            (-88.490105, 18.486830),
            (-88.848312, 17.883190),
            (-89.029846, 18.001520),
            (-89.150848, 17.955460),
            (-89.143066, 17.808310),
            (-90.067925, 17.819321),
            (-91.001419, 17.817600),
            (-91.002258, 17.254650),
            (-91.453918, 17.252190),
            (-91.081657, 16.918470),
            (-90.711761, 16.687481),
            (-90.600822, 16.470770),
            (-90.438812, 16.410120),
            (-90.464478, 16.069559),
            (-91.747887, 16.066580),
            (-92.229248, 15.251440),
            (-92.087105, 15.064590),
            (-92.203140, 14.830110),
            (-92.227684, 14.538830),
            (-93.359406, 15.615440),
            (-93.875183, 15.940180),
            (-94.691650, 16.200991),
            (-95.250137, 16.128330),
            (-96.053299, 15.752080),
            (-96.557320, 15.653510),
            (-97.263512, 15.917080),
            (-98.012978, 16.107321),
            (-98.947693, 16.566040),
            (-99.697365, 16.706181),
            (-100.829422, 17.171070),
            (-101.666061, 17.649019),
            (-101.918503, 17.916090),
            (-102.478035, 17.975750),
            (-103.500961, 18.292299),
            (-103.917442, 18.748569),
            (-104.991890, 19.316130),
            (-105.493042, 19.946770),
            (-105.731369, 20.434111),
            (-105.397652, 20.531710),
            (-105.500671, 20.816891),
            (-105.270645, 21.076290),
            (-105.265808, 21.422110),
            (-105.603127, 21.871149),
            (-105.693306, 22.269079),
            (-106.028664, 22.773760),
            (-106.909973, 23.767780),
            (-107.915359, 24.548920),
            (-108.401810, 25.172331),
            (-109.260193, 25.580601),
            (-109.444084, 25.824890),
            (-109.291611, 26.442949),
            (-109.801445, 26.676170),
            (-110.391724, 27.162109),
            (-110.640976, 27.859871),
            (-111.178879, 27.941259),
            (-111.759567, 28.467951),
            (-112.228188, 28.954399),
            (-112.271759, 29.266830),
            (-112.809540, 30.021099),
            (-113.163712, 30.786880),
            (-113.148682, 31.170980),
            (-113.871780, 31.567610),
            (-114.205650, 31.524050),
            (-114.776405, 31.799540),
            (-114.936592, 31.393490),
            (-114.771126, 30.913610),
            (-114.673889, 30.162689),
            (-114.330887, 29.750420),
            (-113.588852, 29.061621),
            (-113.423981, 28.826170),
            (-113.271965, 28.754780),
            (-113.139999, 28.411289),
            (-112.962257, 28.425180),
            (-112.761482, 27.780210),
            (-112.457855, 27.525810),
            (-112.244919, 27.171740),
            (-111.616432, 26.662821),
            (-111.284653, 25.732590),
            (-110.987755, 25.294609),
            (-110.709923, 24.826000),
            (-110.654999, 24.298590),
            (-110.172852, 24.265539),
            (-109.771736, 23.811180),
            (-109.409012, 23.364660),
            (-109.433311, 23.185591),
            (-109.854141, 22.818270),
            (-110.031357, 22.823071),
            (-110.295029, 23.430969),
            (-110.949425, 24.000950),
            (-111.670502, 24.484430),
            (-112.181976, 24.738420),
            (-112.148872, 25.470140),
            (-112.300621, 26.011990),
            (-112.777275, 26.321960),
            (-113.464653, 26.768190),
            (-113.596741, 26.639450),
            (-113.848923, 26.900049),
            (-114.465660, 27.142090),
            (-115.055092, 27.722731),
            (-114.982216, 27.798201),
            (-114.570267, 27.741489),
            (-114.199242, 28.115009),
            (-114.161957, 28.566111),
            (-114.931808, 29.279470),
            (-115.518570, 29.556360),
            (-115.887299, 30.180799),
            (-116.258263, 30.836460),
            (-116.721466, 31.635731),
            (-117.127731, 32.535339),
            (-115.991318, 32.612389),
            (-114.721359, 32.720829),
            (-114.815002, 32.525280),
            (-113.304886, 32.039139),
            (-111.023506, 31.334721),
            (-109.034943, 31.341940),
            (-108.241943, 31.342220),
            (-108.239983, 31.754854),
            (-106.507545, 31.754520),
            (-106.142868, 31.399950),
            (-105.631592, 31.083830),
            (-105.037338, 30.644020),
            (-104.705750, 30.121731),
            (-104.456970, 29.571960),
            (-103.940002, 29.270000),
            (-103.109970, 28.969999),
            (-102.479958, 29.760000),
            (-101.662308, 29.779301),
            (-100.957558, 29.380711),
            (-100.455780, 28.696119),
            (-100.109970, 28.110001),
            (-99.519920, 27.540001),
            (-99.299973, 26.840000),
            (-99.019920, 26.370001),
            (-98.239983, 26.059999),
            (-97.529938, 25.840000),
            (-97.139908, 25.870001),
        ]
        mexico_shape = Polygon(*[xy(lon, lat) for lon, lat in outline],
                               color=WHITE, stroke_width=2.2)

        # Una marca por municipio/campus listado; sedes que comparten ciudad
        # quedan ligeramente separadas para que no se tapen unas a otras.
        sites = [
            ("Agua Prieta",-109.55,31.33),("Ciudad Acuña",-100.93,29.32),("Ciudad Constitución",-111.66,25.03),("Acatlán de Osorio",-98.05,18.20),
            ("Acayucan",-94.91,17.95),("Álamo",-97.68,20.91),("Alvarado",-95.76,18.77),
            ("Altamira",-98.00,22.39),("Ameca",-104.05,20.55),("Apatzingán",-102.35,19.09),
            ("Atitalaquia",-99.22,20.06),("Atlixco",-98.43,18.91),
            ("Aguascalientes",-102.30,21.88),("Ensenada",-116.61,31.87),
            ("Mexicali",-115.47,32.63),("Chihuahua",-106.08,28.63),
            ("Ciudad Juárez",-106.49,31.74),("Guadalajara",-103.35,20.66),
            ("Monterrey",-100.31,25.69),("Querétaro",-100.39,20.59),
            ("San Luis Potosí",-100.98,22.15),("Mazatlán",-106.42,23.25),
            ("Tampico",-97.86,22.23),("Ciudad Victoria",-99.14,23.74),
            ("Tlaxcala",-98.24,19.32),("Mérida",-89.62,20.97),
            ("Tizimín",-88.15,21.14),("Zacatecas",-102.58,22.77),
            ("Pachuca",-98.76,20.10),("Colima",-103.72,19.24),
            ("Morelia",-101.19,19.70),("Veracruz",-96.13,19.17),
            ("Puebla",-98.21,19.04),("Ciudad de México",-99.13,19.43),
            ("Cuernavaca",-99.23,18.92),("Toluca",-99.66,19.29),
            ("Ecatepec",-99.07,19.60),("Cuautitlán Izcalli",-99.21,19.65),
            ("Huixquilucan",-99.35,19.36),("Ixtapaluca",-98.88,19.32),
            ("Jilotepec",-99.53,19.95),("Jocotitlán",-99.79,19.71),
            ("Cuautla",-98.95,18.81),("Cancún",-86.85,21.16),
            ("Chetumal",-88.30,18.50),("Calkiní",-90.05,20.37),
            ("Centla",-92.65,18.53),("Champotón",-90.72,19.35),
            ("Chilpancingo",-99.50,17.55),("Ciudad Altamirano",-100.65,18.36),
            ("Ciudad Cuauhtémoc",-106.88,28.41),("Ciudad Guzmán",-103.46,19.70),
            ("Ciudad Jiménez",-104.92,27.13),("Ciudad Madero",-97.83,22.27),
            ("Ciudad Serdán",-97.45,18.99),("Ciudad Valles",-99.02,21.99),
            ("Comitán",-92.13,16.25),("Culiacán",-107.39,24.81),
            ("Iguala",-99.54,18.35),("Jiquilpan",-102.72,19.99),
            ("Torreón",-103.45,25.54),("Lázaro Cárdenas",-102.20,17.96),
            ("León",-101.68,21.12),("Lerdo",-103.52,25.53),("Los Reyes",-102.47,19.59),("Zamora",-102.28,19.98),("Oaxaca",-96.72,17.07),
            ("Ocotlán",-102.77,20.35),("Orizaba",-97.10,18.85),
            ("Parral",-105.67,26.93),("Piedras Negras",-100.52,28.70),
            ("Pochutla",-96.47,15.74),("Puerto Vallarta",-105.23,20.65),
            ("Purísima del Rincón",-101.88,21.03),("Rioverde",-99.99,21.93),
            ("Salvatierra",-100.88,20.21),("San Juan del Río",-100.00,20.39),
            ("San Marcos",-99.40,16.80),("San Martín Texmelucan",-98.44,19.28),
            ("Santiago Papasquiaro",-105.42,25.04),("Saltillo",-100.99,25.43),
            ("Tehuacán",-97.39,18.46),("Teposcolula",-97.49,17.51),
            ("Zacatepec",-99.19,18.65),("Zitácuaro",-100.36,19.44),
            ("Huatusco",-96.97,19.15),("Huauchinango",-98.05,20.17),
            ("Huetamo",-100.90,18.63),("Huichapan",-99.65,20.38),
            ("Irapuato",-101.35,20.68),("Pátzcuaro",-101.61,19.51),
            ("Misantla",-96.85,19.93),("Monclova",-101.42,26.91),
            ("Naranjos",-97.68,21.35),("Nuevo Casas Grandes",-107.91,30.42),
            ("Pánuco",-98.18,22.05),("Poza Rica",-97.46,20.53),
            ("Puerto Peñasco",-113.53,31.32),("Región Sierra",-92.60,17.50),
            ("San Andrés Tuxtla",-95.21,18.45),("Tantoyuca",-98.18,21.35),
            ("Teziutlán",-97.36,19.82),("Uruapan",-102.06,19.42),
            ("Villa La Venta",-94.05,18.10),("Zacapoaxtla",-97.59,19.87),
            ("Istmo",-95.20,16.43),("Tepic",-104.90,21.50),
            ("Tepatitlán",-102.76,20.81),("Ameca",-104.05,20.55),
            ("Puerto Vallarta",-105.23,20.65),("Ciudad Guzmán",-103.46,19.70),
            ("Tonalá",-103.23,20.62),("Tequila",-103.84,20.88),
        ]
        # Separa unos píxeles las sedes repetidas en una misma ciudad/campus.
        # Cantidad de universidades/campus que se superponen en los principales
        # núcleos; jitter radial preserva la ubicación y permite ver cada punto.
        multiplicity = {
            "Ciudad de México": 14, "Guadalajara": 12, "Monterrey": 7,
            "Puebla": 7, "Aguascalientes": 5, "Morelia": 4,
            "Querétaro": 4, "León": 4, "Mérida": 4, "Toluca": 5,
            "Cuernavaca": 3, "Veracruz": 4, "Torreón": 3,
            "San Luis Potosí": 3, "Culiacán": 3, "Tepatitlán": 2,
            "Puerto Vallarta": 2, "Ciudad Guzmán": 2, "Tizimín": 2,
            "Mexicali": 3, "Ensenada": 2,
        }
        grouped = {}
        for city, lon, lat in sites:
            grouped.setdefault((lon, lat), []).append(city)
        points = []
        for (lon, lat), names in grouped.items():
            for city in names:
                n = multiplicity.get(city, 1)
                for i in range(n):
                    # Dos anillos pequeños evitan que las marcas oculten la ciudad.
                    radius = 0.10 if i < 8 else 0.17
                    angle = i * 2.399
                    points.append((lon + radius * np.cos(angle),
                                   lat + radius * np.sin(angle), city))
        dots = VGroup(*[Dot(xy(lon, lat), radius=0.027, color=WHITE)
                        for lon, lat, _ in points])
        # Solo algunas etiquetas principales; todos los sitios sí tienen punto.
        featured = {"Ensenada", "Mexicali", "Monterrey", "Guadalajara", "Ciudad de México", "Mérida"}
        labels = VGroup()
        labeled = set()
        for dot, (_, _, name) in zip(dots, points):
            if name in featured and name not in labeled:
                label = Tex(name, color=WHITE).scale(0.34).next_to(dot, UP, buff=0.04)
                label_shifts = {
                    "Ensenada": LEFT * 0.30 + DOWN * 0.08,
                    "Mexicali": RIGHT * 0.27 + UP * 0.08,
                    "Guadalajara": LEFT * 0.32 + UP * 0.10,
                    "Ciudad de México": RIGHT * 0.36 + DOWN * 0.18,
                }
                label.shift(label_shifts.get(name, ORIGIN))
                labels.add(label)
                labeled.add(name)
        count = Tex("Universidades y tecnológicos", color=WHITE).scale(0.38)
        count.to_edge(DOWN, buff=0.28)

        self.play(FadeIn(heading), Create(mexico_shape), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(dot, scale=2) for dot in dots], lag_ratio=0.012),
                  run_time=1.8)
        self.play(FadeIn(labels), FadeIn(count), run_time=0.6)
        self.wait(1.5)
        self.clear_scene()

    def clasificacion(self):
        heading = self.title(r"¿Quién gana?")
        teams = VGroup(*[Tex(f"Equipo {i}", color=WHITE).scale(0.52) for i in range(1, 5)])
        rows = VGroup(*[VGroup(team, Tex(f"{5-i} problemas", color=WHITE).scale(0.52))
                        .arrange(RIGHT, buff=1.1) for i, team in enumerate(teams)])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.27).shift(0.2 * DOWN)
        winner = SurroundingRectangle(rows[0], color=WHITE, buff=0.13)
        note = Tex("Más problemas resueltos = mejor resultado", color=WHITE).scale(0.5).to_edge(DOWN)
        self.play(FadeIn(heading), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.18))
        self.play(Create(winner), FadeIn(note))
        self.wait(1.5)
        self.clear_scene()

    def desempate(self):
        heading = self.title(r"Si hay empate: decide el tiempo")
        formula = MathTex(r"\text{tiempo total}=\sum t_{\text{solución}}+20\times\text{intentos fallidos}", color=WHITE).scale(0.72).shift(0.3 * UP)
        clock = Circle(radius=0.66, color=WHITE).shift(LEFT * 3 + DOWN * 1.05)
        hand = Line(clock.get_center(), clock.get_center() + UP * 0.42, color=WHITE)
        wrong = Tex("Intento incorrecto", color=WHITE).scale(0.55).shift(LEFT * 0.1 + DOWN * 0.85)
        penalty = MathTex(r"+20\ \text{min}", color=WHITE).scale(0.8).shift(RIGHT * 2.6 + DOWN * 0.85)
        arrow = Arrow(wrong.get_right(), penalty.get_left(), color=WHITE, buff=0.15)
        warning = Tex("Un error puede costar decenas de lugares.", color=WHITE).scale(0.5).to_edge(DOWN)
        self.play(FadeIn(heading), Write(formula), Create(clock), Create(hand))
        self.play(FadeIn(wrong), GrowArrow(arrow), FadeIn(penalty))
        self.play(FadeIn(warning))
        self.wait(2)
        self.clear_scene()

    def final_y_repechaje(self):
        heading = self.title(r"Tres fechas. Una última oportunidad.")
        scores = VGroup(*[Tex(f"Fecha {i}: puntos", color=WHITE).scale(0.55) for i in range(1, 4)])
        scores.arrange(DOWN, aligned_edge=LEFT, buff=0.28).shift(LEFT * 2 + DOWN * 0.15)
        bracket = Brace(scores, LEFT, color=WHITE)
        selected = Tex("Mejores equipos → Final", color=WHITE).scale(0.6).next_to(scores, RIGHT, buff=0.7)
        last = Tex("¿Te quedaste cerca?", color=WHITE).scale(0.62).shift(DOWN * 1.25)
        repechaje = Tex("Repechaje: 5 horas a todo o nada", color=WHITE).scale(0.62).next_to(last, DOWN, buff=0.35)
        self.play(FadeIn(heading), LaggedStart(*[FadeIn(s) for s in scores], lag_ratio=0.2))
        self.play(GrowFromCenter(bracket), FadeIn(selected))
        self.play(FadeIn(last), FadeIn(repechaje))
        self.wait(2)
        self.clear_scene()

    def cierre(self):
        lines = VGroup(
            Tex("Meses. A veces años.", color=WHITE),
            Tex("Entrenamiento diario. Resiliencia.", color=WHITE),
            Tex("Y por eso están aquí.", color=WHITE),
        ).arrange(DOWN, buff=0.3).scale(0.67)
        self.play(Write(lines[0]), run_time=0.8)
        self.play(Write(lines[1]), run_time=1.0)
        self.play(Write(lines[2]), run_time=0.8)
        self.wait(2)


class Proceso(BaseProceso):
    """Escena completa de explicación del proceso ICPC."""
    pass


class MapaSedes(BaseProceso):
    def construct(self):
        self.camera.background_color = BLACK
        self.sedes_y_reloj()
