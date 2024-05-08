from PIL import Image, ImageColor, ImageFont, ImageDraw
from math import fabs
from copy import copy

'''
    D'ni Numerals
Convert a decimal to base 25 then draw an image of D'ni numerals.
Uses the Dni Font created by Cyan.

There can be rounding errors with some fractional number.

    version 0.6
    2024-05-08
    stone@stone-shard.com
    Stone
'''

# Folder to save images into
save_path = 'Images/'

# Font info
font_ttf = 'Fonts/Dni.ttf'
font_map = ('0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
            ')', '!', '@', '#', '$',
            '%', '^', '&', '*', '(',
            '[', ']', '\\','{', '}',
            '|', '=', '+',
            ',', '.', '-' )


# Convert to base 25
def to_base25(decimal) -> str:
    "decimal: int or float -> 'Dni font keys'"

    base25 = ''
    base10 = decimal

    negative = False
    if decimal < 0:
        base10 = fabs(base10)
        negative = True

    integral = int(base10)

    while integral >= 0:
        base25 = font_map[integral % 25] + base25
        integral = integral // 25
        if integral == 0:
            break

    if negative is True:
        base25 = '-' + base25

    if type(decimal) is float:
        i = 1
        #fractional = base10 - int(base10)  # float rounding errors
        fractional = float(str(base10)[len(str(int(base10))):])

        limit = len(str(fractional)) - 2
        base25 += '.'

        while fractional >= 0:
            fract_25 = fractional * 25
            fractional = fract_25 - int(fract_25)
            base25 += font_map[int(fract_25)]
            i += 1
            if i > limit or i >= 15:
                break

    return base25


# Create PIL.Image
def create_image(
        base25,
        font_size= 96,
        font_color= "Black",
        background_color= 'White',  # 'Clear' for transparent
        border_size= 42,
        ):

    if background_color.lower() == 'clear':
        background_color = None

    border_size = int(border_size / 100 * font_size)

    font = ImageFont.truetype(
        font=font_ttf,
        size=font_size)

    image_size = (
        font.getsize(base25)[0] + border_size * 2,
        font.getsize(base25)[1] + border_size * 2)

    image = Image.new(
        mode="RGBA",
        color=background_color,
        size=image_size)

    draw = ImageDraw.Draw(
        im=image,
        mode='RGBA')

    draw_position = (
        font.getbbox(base25)[0] * -1 + border_size,
        font.getbbox(base25)[1] * -0.5 + border_size)

    draw.text(
        draw_position,
        base25,
        font=font,
        fill=ImageColor.getrgb(font_color))

    return image


# Save Image to
def save_image(image: Image, name: str) -> (Image, str):
    fp = save_path + name + '.png'
    image.save(fp)
    return (image, fp)


########################
## Ask user for input ##

# Ask for number
def ask_decimal() -> str:
    text = input("\nInput a number to convert to D'ni.\n-> ")
    if '.' in text:
        decimal = float(text)
    else:
        decimal = int(text)
    base25 = to_base25(decimal)
    print(f'\nDni font keys = {base25}')
    return base25


# Ask user for create_image kwargs
def ask_create(base25: str) -> Image:
    kwargs = {}
    color_map = copy(ImageColor.colormap)
    color_map['clear'] = None
    l = ({
        # Font size
        'type': 'number',
        'ask': '\nInput a font size.\n-> ',
        'key': 'font_size',
        'error': ('\nERROR: Font size must be an integer.', )
        }, {
        # Font color
        'type': 'color',
        'ask': '\nInput a font color.\n-> ',
        'test': ImageColor.colormap.keys(),
        'key': 'font_color',
        'error': (ImageColor.colormap.keys(), '\n\nERROR: Font color must be from the list above.')
        }, {
        # Background color
        'type': 'color',
        'ask': "\nInput a background color.\n\tclear = transparent.\n-> ",
        'key': 'background_color',
        'test': color_map.keys(),
        'error': (color_map.keys(), "\n\nERROR: Background color must a color from the list above.")
        }, {
        # Border size
        'type': 'number',
        'ask': '\nInput a border size.\n-> ',
        'key': 'border_size',
        'error': ('\nERROR: Border size must be an integer or leave blank to use the default setting.', )
        })

    print('\nThe following will use the default settings if skipped.')
    for d in l:
        while True:
            arg = input(d.get('ask'))
            if not arg:
                break

            if d.get('type') == 'number':
                if arg.isnumeric():
                    kwargs[d.get('key')] = int(arg)
                    break

            elif d.get('type') == 'color':
                if arg.lower() in d.get('test'):
                    kwargs[d.get('key')] = arg
                    break

            print(*d.get('error'))

    image = create_image(base25, **kwargs)
    image.show()
    print('\nImage size =', image.size)
    return image


# Ask to save image
def ask_save(image: Image) -> (Image, str):
    save = '\nWould you like to save this image? Y/N\n-> '
    name = '\nInput a name to save this image as.\n-> '
    path = '''\nImage saved as "{}"\n'''
    while True:
        yn = input(save).upper()
        if yn in ('Y', 'YES'):
            saved = save_image(image, input(name))
            print(path.format(saved[1]))
            break

        elif yn in ('N', 'NO'):
            saved = (image, None)
            print('\n')
            break

    return saved


#########
## Run ##

# Convert decimal then create image
def main(decimal, **kwargs) -> Image:
    return create_image(to_base25(decimal), **kwargs)


# Ask user for decimal and args then view and save image.
def main_ask_input():
    return ask_save(ask_create(ask_decimal()))


if __name__ == "__main__":
    main_ask_input()
