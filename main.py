import argparse
import os

import pyfiglet
from PIL import Image, ImageDraw, ImageFont, ImageText


parser = argparse.ArgumentParser(
    prog='asciitextwall',
    description='Simple tool to generate ascii text wallpapers',
)

parser.add_argument('-t', '--text', help="Text to display", type=str, required=True)
parser.add_argument('-f', '--font', help="Pyfiglet font to use", type=str, required=True)
parser.add_argument('-mf', '--mono_font', help="Monospaced font to use", type=str, required=True)
parser.add_argument('-s', '--size', help="Size of the text", type=int, required=True)
parser.add_argument('-w', '--width', help="Width of the text. 80 by default", type=int)
parser.add_argument('-c', '--color', help="Color of the text", type=str, required=True)
parser.add_argument('-b', '--bg_color', help="Color of the background", type=str, required=True)
parser.add_argument('-iw', '--img_width', help="Output image width", type=int, required=True)
parser.add_argument('-ih', '--img_height', help="Output image height", type=int, required=True)
parser.add_argument('-p', '--preview', help="Preview the image output without writing it", action="store_true")

args = parser.parse_args()


def get_output_path(filename="output.png"):
    """Function to generate the output filename checking if there is duplicates"""
    root, ext = os.path.splitext(filename)
    output_name = filename
    counter = 1

    while os.path.exists(output_name):
        output_name = f"{root}_{counter}{ext}"
        counter += 1

    return output_name


def main():
    image = Image.new(mode="RGB", size=(args.img_width, args.img_height), color=args.bg_color)
    ascii_art = pyfiglet.figlet_format(args.text, font=args.font, width=args.width or 80)
    # A monospaced font is needed in this case, because the characters might be missaligned otherwise
    font = ImageFont.truetype(font=args.mono_font, size=args.size)
    text = ImageText.Text(ascii_art, font)

    bbox = text.get_bbox()
    # Calculate the position for the text to be in the center of the image
    x = (args.img_width - bbox[2]) // 2
    y = (args.img_height - bbox[3]) // 2

    final = ImageDraw.Draw(image)
    # Write the text to the image
    final.text((x, y), text, args.color)

    # Preview the image or save it
    if args.preview is True:
        image.show()
    else:
        # Save the image to the current dir
        output_path = get_output_path("output.png")
        image.save(output_path)
        print(f"Image saved to: {output_path}")


if __name__ == "__main__":
    main()
