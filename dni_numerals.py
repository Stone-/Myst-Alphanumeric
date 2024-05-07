from PIL import Image, ImageColor, ImageFont, ImageDraw
from math import fabs

'''
    D'ni Numerals
Convert a decimal to base 25 then draw an image of D'ni numerals.
Uses the Dni Font created by Cyan.

There can be rounding errors with some fractional number.

    version 0.4
    2024-05-07
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
        base10 = fabs(decimal)
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
        font_size = 96,
        font_color = "Black",
        background_color = 'White',  # 'Color' or None for transparent
        border_size = 42,
        ):

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
    
    # Display image
    font_name = font.getname()[0]
    print(f'\n{font_name} keys = {base25}')
    image.show()
    print('\nImage size =', image.size)
    return image


#
def save_image(image: Image, name: str): 
    fp = save_path + name + '.png'
    image.save(fp)
    print(f'''\nImage saved as "{fp}"\n''')
        
     
########################
## Ask user for input ##

# Ask for number
def ask_decimal():
    text = input("\nInput a number to convert to D'ni.\n-> ")
    if text.isdigit():
        decimal = int(text)
    else:
        decimal = float(text)
    return decimal

  
# Ask to save
def ask_save(image: Image):
    save = '\nWould you like to save this image? Y/N\n-> '
    name = '\nInput a name to save this image as.\n-> '

    while True:       
        yn = input(save).upper()
        if yn in ('Y', 'YES'):
            save_image(image, input(name))
            break
    
        elif yn in ('N', 'NO'):
            print('\n')
            break


#########
## Run ##

# Convert decimal then create image
def main(decimal, **kwargs) -> Image:
    keys = to_base25(decimal)
    image = create_image(keys, **kwargs)
    return image


# Ask user for input, view and save image
def main_ask_input():
    decimal = ask_decimal()
    keys = to_base25(decimal)
    image = create_image(keys)
    ask_save(image)


if __name__ == "__main__":
    main_ask_input()
