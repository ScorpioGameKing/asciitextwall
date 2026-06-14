import sys

import pyfiglet
from PIL import Image, ImageDraw, ImageFont, ImageText

img_width = 1920
img_height = 1080
text_var = "Hello World"
font_var = "big"
mono_font = ""
if sys.platform == "win32":
    mono_font = "C:/Windows/Fonts/consola.ttf"
elif sys.platform == "linux":
    mono_font = "/usr/share/fonts/truetype/DejaVu/DejaVuSansMono.ttf"
width = 200
size = 20


def main():
    image = Image.new(mode="RGB", size=(img_width, img_height), color="#000000")
    ascii_art = pyfiglet.figlet_format(text_var, font=font_var, width=width)
    # A monospaced font is needed in this case, because the characters might be missaligned otherwise
    font = ImageFont.truetype(font=mono_font, size=size)
    text = ImageText.Text(ascii_art, font)

    bbox = text.get_bbox()
    # Calculate the position for the text to be in the center of the image
    x = (img_width - bbox[2]) // 2
    y = (img_height - bbox[3]) // 2

    final = ImageDraw.Draw(image)
    # Write the text to the image
    final.text((x, y), text, "#ffffff")

    # Write the image to temp and open it
    image.show()


if __name__ == "__main__":
    main()
