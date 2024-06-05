''' CreateImage.py
    Create and save a PIL Image from the given font string.   

    2024-06-05 - v0.01
    stone@stone-shard.com
    Stone {Matt Cascone}
'''

from PIL import Image, ImageFont, ImageColor, ImageDraw


kColors = {  # MOULa Colors
    'clear': (0, 0, 0, 0),
    'agenbluedk': (166, 162, 190, 255),
    'agengreenlt': (223, 255, 217, 255),
    'agengreendk': (166, 190, 162, 255),
    'dniyellow': (217, 207, 147, 255),
    'dnicyan': (147, 221, 217, 255),
    'dniblue': (199, 180, 222, 255),
    'dnired': (255, 55, 97, 255),
    'dnigreen': (178, 224, 194, 255),
    'dnigreendk': (0, 152, 54, 255),
    'dnipurple': (224, 178, 209, 255),
    'dniwhite': (255, 255, 255, 255),
    'dnishowred': (255, 217, 223, 255),
    'dnihideblue': (199, 180, 222, 76)}
ImageColor.colormap.update(kColors)


# Create PIL.Image.Image
def createImage(
            text,
            font_path= 'Fonts/Dni.ttf',
            font_size= 96,
            font_color= "Black",
            stroke_width= 1,
            stroke_color= 'DniCyan',
            background_color= 'White',  # 'Clear' for transparent
            border_size= 42,
            ) -> Image.Image:
    ''' Create a PIL Image from the given font string.

        Perameters
        ----------
            text : string  # Must match the font given in font_path.

        Optional Perameters
        -------------------
            -- Colors can be a name from... 
                Cyan's kColors or PIL.ImageColor.colormap or
                'Clear' for transparent.
                
            font_path: string  # 'Path/Name.ttf' of the .ttf file.
            font_size: int  # Size in px
            font_color: string  # "color_name"
            stroke_width: int  # Color around symbol in px
            stroke_color: string  # "color_name" 
            background_color: string  # "color_name"
            border_size: int  # px Scales with font_size
            
        Returns
        -------
            PIL.Image.Image
    '''

    border_size = int(border_size / 100 * font_size)

    font = ImageFont.truetype(
        font=font_path,
        size=font_size)

    image_size = (
        font.getsize(text)[0] + border_size * 2,
        font.getsize(text)[1] + border_size * 2)

    image = Image.new(
        mode="RGBA",
        color=ImageColor.getrgb(background_color),
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
        fill=ImageColor.getrgb(font_color),
        stroke_fill=ImageColor.getrgb(stroke_color),
        stroke_width=stroke_width)

    return image


# Save Image to
def saveImage(image: Image.Image, name=None, path='Images') -> str:
    ''' Save the given Image.

            Perameters
            ----------
                image : PIL.Image.Image
                name : string, optional  # Will ask user if None.
                path : string, optional  # File path Defalts to 'Images'.

            Returns
            -------
                string  # File path of saved image. ''' 
    while not name:
        image.show()
        yn = input('\nWould you like to save this image? Y/N\n-> ').upper()
        if yn in ('Y', 'YES'):
            name = input('\nInput a name to save this image as.\n-> ')
        elif yn in ('N', 'NO'):
            print('\n')
            break
    if name:          
        fp = f'{path}/{name}.png'
        image.save(fp)
        print(f'''\nImage saved as "{fp}"\n''')
        return fp


# Ask user for kwargs
def askKwargs() -> {'kw':'args'}:
    ''' Ask user to input the kwargs, used when creating an Image.
        Result
        ------ 
            kwargs
        Usage
        -----
            createImage("text", **askKwargs()) '''

    kwargs = {}
    color_keys = ImageColor.colormap.keys()
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
        'test': color_keys,
        'key': 'font_color',
        'error': (color_keys, 
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
        'test': color_keys,
        'error': (color_keys, 
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
        'test': color_keys,
        'error': (color_keys, 
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


# Ask for kwargs if not given
def _CreateImage(text, **kwargs):
    if kwargs.get('ask'):
        kwargs.update(AskKwargs())
    return _CreateImage(text, **kwargs)
 


if __name__ == "__main__":
    help(__name__)

