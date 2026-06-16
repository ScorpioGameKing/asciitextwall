from PIL.ImageDraw import ImageDraw as pImageDraw
from PIL.ImageText import Text
from PIL.ImageFont import FreeTypeFont
from PIL.Image import Image as pImage
from PIL import Image, ImageDraw, ImageFont, ImageText
from argparse import ArgumentParser, Namespace
from pyfiglet import figlet_format, FigletString, FigletFont
from os.path import exists, splitext, expanduser
from os import remove
from random import choice

parser: ArgumentParser = ArgumentParser(
    prog='asciitextwall',
    description='Simple tool to generate ascii text wallpapers',
)

# All required arguments, they provide no default
required= parser.add_argument_group(title='Required', description='These options are hard required to generate an image')
required.add_argument('-t', '--text', help="Text to display", type=str, required=True )
required.add_argument('-f', '--font', help="Pyfiglet font to use, use 'random' for a random font", type=str, required=True)
required.add_argument('-mf', '--mono_font', help="Monospaced font to use", type=str)
required.add_argument('-s', '--size', help="Size of the text", type=int, required=True)
required.add_argument('-c', '--color', help="Color of the text", type=str, required=True)
required.add_argument('-b', '--bg_color', help="Color of the background", type=str, required=True)

# All optional arguments, when not found they will use the provided defaults
optional= parser.add_argument_group(title='Optional', description='These are optional adjustments to the Image Generation Process')
optional.add_argument('-w', '--width', help="Width of the text. 80 by default", type=int, default=80)
optional.add_argument('-iw', '--img_width', help="Output image width, 1920 by default", type=int, default=1920)
optional.add_argument('-ih', '--img_height', help="Output image height, 1080 by default", type=int, default=1080)
optional.add_argument('-n', '--name', help="The name of the generated image, 'output.png' by default", type=str, default='output.png')
optional.add_argument('-o', '--output', help="The location of the generated image, local by default", type=str, default='')
optional.add_argument('-ic', '--increment', help="Decide if the saved image is incremented or overwritten, not incremented by default", action="store_true")
optional.add_argument('-p', '--preview',  help="Preview the image output without writing it", action="store_true")

args: Namespace = parser.parse_args()

def get_output_path(filename:str) -> str:
    """Function to generate the output filename checking if there is duplicates"""
    root, ext = splitext(filename)
    output_name: str = f"{expanduser(path=args.output)}{filename}"
    if args.increment:
        counter = 1
        while exists(path=output_name):
            output_name = f"{expanduser(path=args.output)}{root}_{counter}{ext}"
            counter += 1
    else:
        if exists(path=output_name):
            remove(path=output_name)
    return output_name

def get_random_font() -> str:
    return choice(FigletFont.getFonts())

def main() -> None:
    """ Takes the given command line arguments and renders an ascii art image"""
    # Check if we need a random font
    if args.font in 'random':
        _font:str = get_random_font()
    else:
        _font:str = args.font

    image: pImage = Image.new(mode="RGB", size=(args.img_width, args.img_height), color=args.bg_color)
    ascii_art: FigletString = figlet_format(text=args.text, font=_font, width=args.width)
    # A monospaced font is needed in this case, because the characters might be missaligned otherwise
    font: FreeTypeFont = ImageFont.truetype(font=args.mono_font, size=args.size)
    text: Text[str] = ImageText.Text(text=ascii_art, font=font)

    bbox: tuple[float, float, float, float] = text.get_bbox()
    # Calculate the position for the text to be in the center of the image
    x = (args.img_width - bbox[2]) // 2
    y = (args.img_height - bbox[3]) // 2

    final: pImageDraw = ImageDraw.Draw(im=image)
    # Write the text to the image
    final.text(xy=(x, y), text=text, fill=args.color)

    # Preview the image or save it
    if args.preview is True:
        image.show()
    else:
        # Save the image to the current dir
        output_path: str = get_output_path(filename=args.name)
        image.save(fp=output_path)
        print(f"Image saved to: {output_path}")

if __name__ == "__main__":
    main()
