import os
import math
import tempfile
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

# Constants for image dimensions
PHOTO_SLOT_WIDTH_CM = 2.86
PHOTO_SLOT_HEIGHT_CM = 5.08
DPI = 300
CM_TO_PX = DPI / 2.54  # 1 inch = 2.54 cm, so 300 dpi = ~118.11 px/cm
IMG_WIDTH_PX = int(PHOTO_SLOT_WIDTH_CM * CM_TO_PX)
IMG_HEIGHT_PX = int(PHOTO_SLOT_HEIGHT_CM * CM_TO_PX)

# A4 size in pixels at 96 DPI
A4_WIDTH_PX = int(21.0 * CM_TO_PX)
A4_HEIGHT_PX = int(29.7 * CM_TO_PX)

# Color mapping
COLORS = {'red': (200, 0, 0), 'blue': (0, 80, 180)}

# Font path
FONT_PATH = os.path.normpath("C:/Windows/Fonts/Cartoonist Kooky Regular.ttf")


def create_card(image_path, name, color):
    """
    Creates a card with a resized image and a colored name label.

    Args:
        image_path (str): Path to the input image.
        name (str): Person's name.
        color (str): 'red' or 'blue'.

    Returns:
        PIL.Image: Card image.
    """
    img = Image.open(image_path).convert("RGB")
    img.thumbnail((IMG_WIDTH_PX, IMG_HEIGHT_PX), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (IMG_WIDTH_PX, IMG_HEIGHT_PX), "white")
    x_offset = (IMG_WIDTH_PX - img.width) // 2
    tag_height = int(IMG_HEIGHT_PX * 0.25)
    y_offset = IMG_HEIGHT_PX - tag_height - img.height
    canvas.paste(img, (x_offset, y_offset))

    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, IMG_HEIGHT_PX - tag_height, IMG_WIDTH_PX, IMG_HEIGHT_PX], fill=COLORS[color])

    try:
        font = ImageFont.truetype(FONT_PATH, size=48)
    except IOError:
        font = ImageFont.load_default(size=32)

    try:
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        # Fallback for older Pillow versions
        text_width, text_height = draw.textsize(name, font=font)

    text_position = ((IMG_WIDTH_PX - text_width) // 2, IMG_HEIGHT_PX - tag_height + (tag_height - text_height) // 2)
    draw.text(text_position, name, fill="white", font=font)

    return canvas


def layout_cards_to_pdf(cards, output_path):
    """
    Layouts cards on A4 sheets and saves as a PDF.

    Args:
        cards (list): List of PIL Image objects.
        output_path (str): Output PDF path.
    """
    cards_per_row = A4_WIDTH_PX // IMG_WIDTH_PX
    cards_per_col = A4_HEIGHT_PX // IMG_HEIGHT_PX
    cards_per_page = cards_per_row * cards_per_col

    pdf = FPDF(unit='pt', format='A4')

    px_to_pt = 72 / DPI  # ≈ 0.24 for 300 DPI
    spacing_px = 15  # Still in pixels, but smaller than before

    for i in range(0, len(cards), cards_per_page):
        pdf.add_page()
        for idx, card in enumerate(cards[i:i + cards_per_page]):
            row = idx // cards_per_row
            col = idx % cards_per_row

            x = col * (IMG_WIDTH_PX + spacing_px) * px_to_pt
            y = row * (IMG_HEIGHT_PX + spacing_px) * px_to_pt

            w = IMG_WIDTH_PX * px_to_pt
            h = IMG_HEIGHT_PX * px_to_pt

            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmpfile:
                tmp_path = tmpfile.name
            card.save(tmp_path, format="JPEG")
            pdf.image(tmp_path, x=x, y=y, w=w, h=h)
            pdf.set_draw_color(150, 150, 150)
            pdf.rect(x, y, w, h)
            os.unlink(tmp_path)

    pdf.output(output_path)
    print(f"Saved PDF to: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate 'Hvem er jeg' game cards PDF from images.")
    parser.add_argument("--input", required=True, help="Path to the folder containing input images.")
    parser.add_argument("--output", required=True, help="Path to save the generated PDF.")

    args = parser.parse_args()
    input_folder = args.input
    output_pdf_path = args.output

    # Process all valid image files
    all_cards = []
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = os.path.splitext(file_name)[0]
            file_path = os.path.join(input_folder, file_name)

            red_card = create_card(file_path, name, 'red')
            blue_card = create_card(file_path, name, 'blue')
            all_cards.extend([red_card, blue_card])

    if not all_cards:
        print("No valid image files found.")
    else:
        layout_cards_to_pdf(all_cards, output_pdf_path)
