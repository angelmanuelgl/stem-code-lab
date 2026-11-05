"""
Genera la tarjeta trasera con QR y dos hojas Carta listas para imprimir (frente y reverso).

Uso:
    pip install pillow "qrcode[pil]"
    manim -s card_front.py CardFront      # genera la imagen del frente
    python make_sheet.py media/images/card_front/CardFront_ManimCE_*.png

Imprime la hoja 1 (frente), voltea el papel por el lado LARGO y pasa la hoja 2 (reverso).
"""
import sys
import glob
import qrcode
from PIL import Image, ImageDraw, ImageFont

URL = "https://www.youtube.com/@Another.Math.Channel"

DPI = 300
MM = DPI / 25.4
CARD_W, CARD_H = round(90 * MM), round(50 * MM)        # 1063 x 591
PAGE_W, PAGE_H = round(215.9 * MM), round(279.4 * MM)  # Carta
COLS, ROWS = 2, 5
BG = "#14121E"
CYAN = "#00E5FF"
MUTED = "#64748B"


def make_back():
    back = Image.new("RGB", (CARD_W, CARD_H), BG)
    qr = qrcode.QRCode(border=2, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(URL)
    qr.make(fit=True)
    # QR oscuro sobre blanco para que los lectores lo detecten bien
    qr_img = qr.make_image(fill_color="#14121E", back_color="white").convert("RGB")
    size = CARD_H - 120
    qr_img = qr_img.resize((size, size), Image.NEAREST)
    x, y = (CARD_W - size) // 2, (CARD_H - size) // 2 - 10
    back.paste(qr_img, (x, y))
    d = ImageDraw.Draw(back)
    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", 26)
    except OSError:
        font = ImageFont.load_default()
    txt = "Escanea para ver el canal"
    w = d.textlength(txt, font=font)
    d.text(((CARD_W - w) / 2, y + size + 18), txt, fill=CYAN, font=font)
    d.rectangle([6, 6, CARD_W - 7, CARD_H - 7], outline=MUTED, width=1)
    return back


def make_sheet(card, path, guides=True):
    page = Image.new("RGB", (PAGE_W, PAGE_H), "white")
    ox = (PAGE_W - COLS * CARD_W) // 2
    oy = (PAGE_H - ROWS * CARD_H) // 2
    for r in range(ROWS):
        for c in range(COLS):
            page.paste(card, (ox + c * CARD_W, oy + r * CARD_H))
    if guides:  # marcas de corte en los bordes
        d = ImageDraw.Draw(page)
        for c in range(COLS + 1):
            x = ox + c * CARD_W
            d.line([(x, oy - 25), (x, oy - 5)], fill="black", width=2)
            d.line([(x, oy + ROWS * CARD_H + 5), (x, oy + ROWS * CARD_H + 25)], fill="black", width=2)
        for r in range(ROWS + 1):
            y = oy + r * CARD_H
            d.line([(ox - 25, y), (ox - 5, y)], fill="black", width=2)
            d.line([(ox + COLS * CARD_W + 5, y), (ox + COLS * CARD_W + 25, y)], fill="black", width=2)
    page.save(path, dpi=(DPI, DPI))
    page.save(path.replace(".png", ".pdf"), resolution=DPI)


if __name__ == "__main__":
    front_path = sys.argv[1] if len(sys.argv) > 1 else glob.glob("media/images/card_front/CardFront*.png", recursive=True)[0]
    front = Image.open(front_path).convert("RGB").resize((CARD_W, CARD_H), Image.LANCZOS)
    back = make_back()
    back.save("card_back.png", dpi=(DPI, DPI))
    make_sheet(front, "sheet_front.png")
    make_sheet(back, "sheet_back.png")
    print("Listo: sheet_front.(png|pdf), sheet_back.(png|pdf), card_back.png")
