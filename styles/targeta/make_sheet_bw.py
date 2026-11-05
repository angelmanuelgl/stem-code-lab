"""
Versión blanco y negro: reverso con QR + hojas Carta (frente y reverso).
Requiere make_sheet.py en la misma carpeta.

    manim -s card_front_bw.py CardFrontBW
    python make_sheet_bw.py media/images/card_front_bw/CardFrontBW_ManimCE_*.png
"""
import sys
import glob
import qrcode
from PIL import Image, ImageDraw, ImageFont

from make_sheet import URL, CARD_W, CARD_H, DPI, make_sheet


def make_back_bw():
    back = Image.new("RGB", (CARD_W, CARD_H), "white")
    d = ImageDraw.Draw(back)
    # Marco doble, igual que el frente
    d.rounded_rectangle([20, 20, CARD_W - 21, CARD_H - 21], radius=22, outline="black", width=5)
    d.rounded_rectangle([34, 34, CARD_W - 35, CARD_H - 35], radius=16, outline="black", width=2)

    qr = qrcode.QRCode(border=2, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(URL)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    size = CARD_H - 190
    qr_img = qr_img.resize((size, size), Image.NEAREST)
    x, y = (CARD_W - size) // 2, 60
    back.paste(qr_img, (x, y))

    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", 56)
    except OSError:
        font = ImageFont.load_default(34)
    # Etiqueta invertida (negro con texto blanco), como el subtítulo del frente
    txt = "YouTube: Another.Math.Channel"
    txt2 = "Github: angelmanuelgl"
    w = d.textlength(txt, font=font)
    bx0, by0 = (CARD_W - w) / 2 - 18, y + size + 0
    d.rounded_rectangle([bx0, by0, bx0 + w + 36, by0 + 44], radius=10, fill="white")
    d.text((bx0 + 18, by0 + 8), txt, fill="black", font=font)
    w2 = d.textlength(txt2, font=font)
    bx0_2, by0_2 = (CARD_W - w2) / 2 - 18, y + size + 0 + 44
    d.rounded_rectangle([bx0_2, by0_2, bx0_2 + w2 + 36, by0_2 + 44], radius=10, fill="white")
    d.text((bx0_2 + 18, by0_2 + 8), txt2, fill="black", font=font)
    return back


if __name__ == "__main__":
    front_path = sys.argv[1] if len(sys.argv) > 1 else glob.glob("media/images/**/CardFrontBW*.png", recursive=True)[0]
    # Convierte a 1 bit con tramado desactivado -> negro y blanco puros
    front = Image.open(front_path).convert("L").resize((CARD_W, CARD_H), Image.LANCZOS)
    front = front.point(lambda v: 255 if v > 140 else 0).convert("RGB")
    back = make_back_bw()
    back.save("card_back_bw.png", dpi=(DPI, DPI))
    make_sheet(front, "sheet_front_bw.png")
    make_sheet(back, "sheet_back_bw.png")
    print("Listo: sheet_front_bw.(png|pdf), sheet_back_bw.(png|pdf)")
