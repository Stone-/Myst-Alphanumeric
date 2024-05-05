from PIL import Image, ImageColor, ImageFont, ImageDraw

'''
    Narayani Numerals
Convert a decimal to the number system found in Saavedro's journal from Myst III: Exile. 
Uses the Narayani Light font created by Jehon aka. Sebastian Ochs.

    version 0.1
    2024-05-01
    stone@stone-shard.com
    Stone
'''


# Font info
font_ttf = 'Narayani_light.ttf'
font_path = 'Fonts/NarayaniLight/'

def view_font_readme():
    f = open(font_path + 'Narayani.txt')
    print(f.read())
    f.close()


#####################
## Character mapping:

key_map = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '10': ')',
    '10': '='}  # on a German keyboard


# Convert a decimal intager to the Narayani number system.
def convert_number( number ):
    "number: decimal intager -> Narayani keys"
    
    if number > 19:
        print("\nWARNING: We don't know if the Narayani number system extends beond 19.")
        
    keys = ''
    if number == 0:
        return number
        
    tens = number // 10
    number = number - tens * 10
    keys = ')' * tens
        
    fives = number // 5
    number = number - fives * 5
    keys += '5' * fives
        
    if number > 0:
        keys += str(number)
        
    return keys
        

# Create PIL.Image
def draw_image( text,
                font_size = 96,
                font_color = "Black",
                background_color = 'White',  # 'Color' or None for transparent
                border_size = 32
                ):
    "text: 'Narayani keys' -> PIL.image"
    
    border_size = int(border_size / 100 * font_size)
    
    font = ImageFont.truetype(
        font=font_path + font_ttf,
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
        font.getbbox(text)[0] / 2 + border_size, 
        font.getbbox(text)[1] / -2 + border_size)
    
    draw.text(
        draw_position,
        text, 
        font=font, 
        fill=ImageColor.getrgb(font_color))
    
    return image


# Ask user for number
def ask_input():
    "_ -> int"
    print('----------------------------------')
    text = input("\nInput a number to convert to Narayani.\n-> ")
    return int(text)


# Ask user to save image
def ask_save( image ):
    "image: PIL.Image -> _"
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
    

# Run
def main():
    input_text = ask_input()
    narayani_keys = convert_number( input_text )
    image = draw_image( narayani_keys )
    image.show()
    ask_save( image )
    

if __name__ == "__main__":
    main()
