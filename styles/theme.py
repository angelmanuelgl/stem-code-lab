"""
Módulo de Estilos Globale y Paleta "Modern Flat" para Manim
Ubicación: styles/theme.py
"""

# Configuración de Fondo
BG_COLOR = "#181C24"

# Jerarquía de Texto y Fórmulas
TEXT_MAIN = "#ECEFF4"
TEXT_MUTED = "#64748B"

# Paleta Semántica
ACCENT_VINO = "#C0392B"         # Ineficiencia / O(n) / Warning
ACCENT_MINT = "#2DD4BF"         # Optimización / O(log n) / Exito
ACCENT_TERRACOTTA = "#D97706"   # Exponentes / Variables activas
ACCENT_INDIGO = "#6366F1"       # Bases / Módulos / Estructuras
ACCENT_CYAN = "#38BDF8"         # Conectores / Mallas / Punteros

# Diccionario completo para acceso dinámico
COLOR_THEME = {
    "background": BG_COLOR,
    "text_main": TEXT_MAIN,
    "text_muted": TEXT_MUTED,
    "vino": ACCENT_VINO,
    "mint": ACCENT_MINT,
    "terracotta": ACCENT_TERRACOTTA,
    "indigo": ACCENT_INDIGO,
    "cyan": ACCENT_CYAN,
}
