from PIL import Image, ImageColor, ImageFont, ImageDraw
from math import fabs
from copy import copy

'''
    D'ni Spell Numbers
Convert a decimal to base 25, 
convert to the NTS writing system,
map to the dni font keys, 
draw an image using D'ni font.

Uses the Dni Font created by Cyan.

    version 0.1
    2024-05-09
    stone@stone-shard.com
    Stone {Matt Cascone}
'''

''' 
    Numerals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The D’ni numeral system is based on the number 5. 
Distinct stems exist for 1-4 and multiples of 5.
0: roon
1: fah
2: bree
3: sen
4: tor
5: vaht
10: nayvoo
15: heebor
20: rish

Numbers of the form 5x+y combine a reduced form of the fives stem with the ones 
stem using the conjunction gah. 6=5+1 is vahgahfah, 12=10+2 is naygahbree, 
18=15+3 is heegahsen, 24=20+4 is rigahtor.

Powers of 25 are formed with the addition of suffixes.
25: fahsee
50: breesee
625=252: fahrah
15,625=253: fahlahn
390,625=254: fahmel
9,765,625=255: fahblo

Combinations of powers of 25 are formed with juxtaposition, so 27=25+2 is fahseebree.

This note was taken from...
https://talashargeltahn.wordpress.com/grammar/#numerals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# Folder to save images into
save_path = 'Images/'

# Font info
font_ttf = 'Fonts/Dni.ttf'


#~~~~~~~~~~~~~~~~~~~~~~~#
# Standards OTS and NTS #
#~~~~~~~~~~~~~~~~~~~~~~~#

negative = '-'
radix = '.'

ots = 0
nts = 1

ones_stems = (  # ((OTS, ), (NTS, ))
    ("roon","fah","bree","sehn","tor"),
    ("rún", "fa", "brí", "sen", "tor"))

conjunctions = ('gah', 'ga')

# v[:2] = reduced form
fives_stems = (  # ({stem: OTS, }, {stem: NTS, })
    {20: "rish", 15: "heebor", 10: "nayvoo", 5: "vaht"},
    {20: "riš", 15: "híbor", 10: "névú", 5: "vat"})

# 25 ** index
powers_suffixes = ( # ((OTS, ), (NTS, ))
    ('', "see", "rah", "lahn", "mel", "blo"),
    ('', "sí", "ra", "lan", "mel", "blo"))

font_map = {  # {'NTS': 'DniFont', }
    'æ': 'å', 'a': 'a', 'é': 'A', 'b': 'b', 'ç': 'c', 'd': 'D', 'ð': 'd',
    'í': 'E', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'á': 'I', 'i': 'i',
    'j': 'j', 'k': 'K', 'x': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
    'ó': 'O', 'p': 'p', 'r': 'r', 's': 's', 'š': 'S', 't': 't', 'þ': 'T',
    'c': 'x', 'ú': 'U', 'u': 'u', 'v': 'v', 'w': 'w', 'y': 'y', 'z': 'z',
    '.': '.', '-': '-', ',': ','}

error_alphabetic = "ERROR: 244,140,624 is the largest number that can be represented alphabeticly in D'ni."


#~~~~~~~~~~~~~~~~~~~~~~~#
# Convert to a standard #
#~~~~~~~~~~~~~~~~~~~~~~~#

# Convert a decimal integer to a base 25 list of integers.
def decimalToBase25(decimal: int) -> [int, ]:
    ""

    base25 = []
    base10 = decimal

    radix = '.'
    negative = ''
    if decimal < 0:
        base10 = fabs(base10)
        negative = '-'

    integral = int(base10)

    while integral >= 0:
        base25.insert(0, integral % 25)
        integral = integral // 25
        if integral == 0:
            break

    if negative:
        base25.insert(0, negative)

    if type(decimal) is float:
        i = 1
        #fractional = base10 - int(base10)  # float rounding errors
        fractional = float(str(base10)[len(str(int(base10))):])

        limit = len(str(fractional)) - 2
        base25.append(radix)

        while fractional >= 0:
            fract_25 = fractional * 25
            fractional = fract_25 - int(fract_25)
            base25.append(int(fract_25))
            i += 1
            if i > limit or i >= 15:
                break

    return base25


# Convert a base 25 integer list to an NTS string.
def base25ToNts(base25: list, comma=',', standard=nts) -> str:
    ""
    
    result = ''
    if base25[0] == negative:
        base25 = base25[1:]
        result += negative

    def combine_stems(n: int) -> str:
        combined = ''
        for key, stem in fives_stems[standard].items():
            if n // key:
                n -= key
                if n == 0:
                    return stem
                else:
                    combined += stem[:2] + conjunctions[standard]
                break
        combined += ones_stems[standard][n]
        return combined

    i = len(base25)
    if i > 6:  # 244140624
        return error_alphabetic
        
    if i == 0 and base25[0] == 0:
        return ones_stems[standard][0]
    
    for n in base25:
        i -= 1
        if n > 0:
            result += combine_stems(n) + powers_suffixes[standard][i]
            result += comma
        
    if result.endswith(comma):
        result = result[:-1]
    if result == '':
        result = ones_stems[standard][0]
    return result#.replace(comma + comma, comma)


#~~~~~~~~~~~~~~~~#
# Font and Image #
#~~~~~~~~~~~~~~~~#

# Map a NTS string to dni font
def ntsToFont(text):
    for k, v in font_map.items():
        text = text.replace(k, v)
    return text


# Create PIL.Image
def createImage(
        text,
        font_size= 96,
        font_color= "Black",
        stroke_width= 1,
        stroke_color= 'cyan',  
        background_color= 'White',  # 'Clear' for transparent
        border_size= 42,
        font= font_ttf,
        ) -> Image:
    ""

    if background_color.lower() == 'clear':
        background_color = None

    border_size = int(border_size / 100 * font_size)

    font = ImageFont.truetype(
        font=font_ttf,
        size=font_size)

    image_size = (
        font.getsize(text)[0] + border_size * 2,
        font.getsize(text)[1] + border_size * 2)

    image = Image.new(
        mode="RGBA",
        color=background_color,
        size=image_size)

    draw = ImageDraw.Draw(
        im=image,
        mode='RGBA')

    draw_position = (
        font.getbbox(text)[0] * -1 + border_size,
        font.getbbox(text)[1] * -0.5 + border_size)

    draw.text(
        draw_position,
        text,
        font=font,
        fill=font_color, #ImageColor.getrgb(font_color),
        stroke_fill=stroke_color,
        stroke_width=stroke_width
        )

    return image


#~~~~~~~~~~~~~~~~~~~~#
# Ask user for input #
#~~~~~~~~~~~~~~~~~~~~#

# Ask for number
def ask_decimal() -> str:
    while True:
        text = input("\nInput a number to convert to D'ni.\n>> ")
        try:
            return int(text)
        except:
            print('\nERROR: Input must be an integer.')


# Ask user for kwargs used in createImage
def ask_kwargs() -> dict:
    kwargs = {}
    color_map = copy(ImageColor.colormap)
    color_map['clear'] = None
    l = ({
        # Font size
        'type': 'integer',
        'ask': '\nInput a font size.\n>> ',
        'key': 'font_size',
        'error': ('\nERROR: Font size must be an integer.', )
        }, {
        # Font color
        'type': 'color',
        'ask': '\nInput a font color.\n>> ',
        'test': ImageColor.colormap.keys(),
        'key': 'font_color',
        'error': (ImageColor.colormap.keys(), 
                '\n\nERROR: Font color must be from the list above.')
        }, {
        # Stroke width
        'type': 'integer',
        'ask': '\nInput a font stroke width.\n>> ',
        'key': 'stroke_width',
        'error': ('\nERROR: Stroke width must be an integer.', )
        }, {
        # Stroke color
        'type': 'color',
        'ask': "\nInput a stroke color.\n>> ",
        'key': 'stroke_color',
        'test': ImageColor.colormap.keys(),
        'error': (ImageColor.colormap.keys(), 
                "\n\nERROR: Stroke color must a color from the list above.")
        }, {
        # Border size
        'type': 'integer',
        'ask': '\nInput a border size.\n>> ',
        'key': 'border_size',
        'error': ('\nERROR: Border size must be an integer',
                'or leave blank to use the default setting.', )
        }, {
        # Background color
        'type': 'color',
        'ask': "\nInput a background color.\n\tclear = transparent.\n>> ",
        'key': 'background_color',
        'test': color_map.keys(),
        'error': (color_map.keys(), 
                "\n\nERROR: Background color must a color from the list above.")
        })

    print('\nThe following will use the default settings if skipped...(just hit return)')
    for d in l:
        while True:
            arg = input(d.get('ask'))
            if not arg:
                break

            if d.get('type') == 'integer':
                if arg.isnumeric():
                    kwargs[d.get('key')] = int(arg)
                    break

            elif d.get('type') == 'color':
                if arg.lower() in d.get('test'):
                    kwargs[d.get('key')] = arg
                    break

            print(*d.get('error'))

    return kwargs


# Ask to save Image
def ask_saveImage(image: Image) -> (Image, str):
    save = '\nWould you like to save this image? Y/N\n>> '
    name = '\nInput a name to save this image as.\n-> '
    saved = '''\nImage saved as "{}"\n'''
    while True:
        yn = input(save).upper()
        if yn in ('Y', 'YES'):
            fp = save_path + input(name.format(save_path)) + '.png'
            image.save(fp)
            print(saved.format(fp))
            break

        elif yn in ('N', 'NO'):
            saved = (image, None)
            print('\n')
            break

    return saved


#~~~~~~#
# Main #
#~~~~~~#

# Convert decimal then create image
def main(decimal, **kwargs) -> Image:
    ""
    base25 = decimalToBase25(decimal)
    nts_word = base25ToNts(base25, comma=',')
    dni_text = ntsToFont(nts_word)
    return createImage(dni_text, **kwargs)


# 
def ask_main():
    ""
    base25 = decimalToBase25(ask_decimal())
    print(f'\nbase 25 = {base25}')
    nts_word = base25ToNts(base25, comma=',')
    print(f'NTS = {nts_word}')
    dni_text = ntsToFont(nts_word)
    print(f'Dni font = {dni_text}\n')
    image = createImage(dni_text, **ask_kwargs())
    image.show()
    print('\nImage size =', image.size)
    ask_saveImage(image)
    

# 
if __name__ == "__main__":
    ask_main()
