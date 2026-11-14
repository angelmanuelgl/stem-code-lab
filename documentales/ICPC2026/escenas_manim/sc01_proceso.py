"""Render opcional de la secuencia completa del bloque 2.

Las escenas independientes están en sc10_conceptos.py, sc20_courier.py,
sc30_final.py y sc40_clasificacion.py. Esta clase las encadena para obtener
un único reel, conservando el orden del storyboard.
"""
from manim import *
from base_theme import BaseScene
from sc10_conceptos import (EscuelaVsICPC, PelarCebolla, MenuTecnicas,
                            ElegirBatallasA, ElegirBatallasB)
from sc20_courier import (EnunciadoCourier, TraduccionCourier, CourierBase2x2,
                          CourierOneUp, CourierEscala)
from sc30_final import (RolesEquipo, TalentoReclutadores, EntradaResultados,
                        FiltroEquipos, MedallasPorRendimiento, TablaTop25)
from sc40_clasificacion import (AvanceLATAM, ComparacionPuestos, FactoresLogisticos,
                                Reconocimiento, CierreEntrevistas)


class Proceso(BaseScene):
    SEQUENCE = [
        EscuelaVsICPC, PelarCebolla, MenuTecnicas, ElegirBatallasA,
        ElegirBatallasB, EnunciadoCourier, TraduccionCourier, CourierBase2x2,
        CourierOneUp, CourierEscala, RolesEquipo, TalentoReclutadores,
        EntradaResultados, FiltroEquipos, MedallasPorRendimiento, TablaTop25,
        AvanceLATAM, ComparacionPuestos, FactoresLogisticos, Reconocimiento,
        CierreEntrevistas,
    ]

    def construct(self):
        for scene_class in self.SEQUENCE:
            scene_class.construct(self)
            self.clear_scene(run_time=0.45)
