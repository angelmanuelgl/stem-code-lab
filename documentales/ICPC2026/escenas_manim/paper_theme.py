"""Compatibilidad con escenas antiguas; los colores proceden de theme.py."""
from theme import (BG_COLOR, TEXT_MAIN, TEXT_MUTED, ACCENT_VINO, ACCENT_MINT,
                   ACCENT_TERRACOTTA, ACCENT_INDIGO, ACCENT_CYAN)

# Alias antiguos mapeados a la paleta slate actual.
PAPER = BG_COLOR
INK = TEXT_MAIN
INK_SOFT = TEXT_MUTED
GRAPHITE = TEXT_MUTED
RULE = TEXT_MUTED
ACCENT = ACCENT_CYAN
