from PIL import Image, ImageColor, ImageFont, ImageDraw

'''
    D'ni Numerals
Convert a decimal to base 25 then draw an image of D'ni numerals using 
the Dni Font created by Cyan.

There can be rounding errors with some fractional number.

    version 0.4
    2024-04-25
    stone@stone-shard.com
    Stone
'''


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
def to_base25(decimal):
    base25 = ''
    
    negative = False
    if decimal.startswith('-'):
        decimal = decimal[1:]
        negative = True
    
    if decimal.isdigit():
        integral = int(decimal)   
        fractional = 'False'  
    else:
        integral = int(float(decimal))
        #fractional = float(decimal) - integral  # float rounding errors
        fractional = float(decimal[len(str(integral)):]) 
    
    while integral >= 0:
        base25 = font_map[integral % 25] + base25
        integral = integral // 25
        if integral == 0:
            break
             
    if negative is True:
        base25 = '-' + base25
    
    if fractional != 'False':
        i = 1
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
    
    font_name = font.getname()[0]
    
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
    print(f'\n{font_name} keys = {base25}')
    image.show()
    print('\nImage size =', image.size)
    return image


########################
## Ask user for input ##

# Ask for number
def ask_decimal():
    return input("\nInput a number to convert to D'ni.\n-> ")


# Ask to save
def ask_save(image):
    while True:
        ask = '\nWould you like to save this image? Y/N\n-> '
        name = '\nInput a name to save this image as.\n-> '
        saved = '''\nImage saved as "{}.png"\n'''
        
        yn = input(ask).upper()
        if yn in ('Y', 'YES'):
            file_name = input(name)
            image.save(file_name + '.png')
            print(saved.format(file_name))
            break
    
        elif yn in ('N', 'NO'):
            print('\n')
            break


#
def main():
    text = ask_decimal()
    keys = to_base25(text)
    image = create_image(keys)
    ask_save(image)


if __name__ == "__main__":
    main()
