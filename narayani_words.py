from PIL import Image, ImageColor, ImageFont, ImageDraw

'''
    Narayani Words
Create an image using the Narayani words as seen in Myst III: Exile. 
Uses the Narayani Light font created by Jehon aka. Sebastian Ochs

    version 0.1
    2024-05-01
    stone@stone-shard.com
    Stone

''' '''

(Use a double spase to seperate words. Single space to overlap.)

'''


# Folder to save images into
save_path = 'Images/'

# Font info
font_ttf = 'Narayani_light.ttf'
readme = 'Narayani.txt'
mapping_gif = 'mapping.gif'
font_path = 'Fonts/NarayaniLight/'

def view_font_readme():
    print(open(font_path + readme).read())

def view_font_mapping():
    Image.open(font_path + mapping_gif).show()


''' ## Shortcuts ##
abcd = u    Top right circle
efgh = v    Bottom right circle
ijkl = w    Blotom left circle
mnop = x    Top left circle
qrst = y    Outer circle
uvwxy = z   All
'''


# Age Symbols
symbols_map = {
    "j'nanin": '6',
    'amateria': '7',
    'edanna': '8',
    'voltaic': '9',
    'rivensquee': '!'
    }


# Wordlist (USING the shortcuts):
word_map = {
    'nature': 'acdehijors_',
    'void': 'ijkpqrs_',
    'intelligence': 'befhklmnq_',
    'love': 'bcdgijlmqs_',
    'energy': 'bfiklopqr_',
    'entropy': 'bcfghijkpqs_',

    'force': 'aijlqr_',
    'mutual': 'adhjknt_',
    'society': 'adghjkmny_',
    'transform': 'adgkmnqrs_',
    'contradict': 'efjksx_',
    'chaos': 'bdefkpqs_',

    'change': 'cdenqtw_',
    'power': 'abcopr_',
    'growth': 'efhnopqrs_',
    'machine': 'abgjkmnqst_',
    'possibility': 'abcgijlmpqs_',
    'civilization': 'abdghjkmnpq_',

    'future': 'aeghklmqr_',
    'convey': 'bghlopqs_',
    'spur': 'bfgirx_',
    'cycle': 'ijkqrt_',
    'encourage': 'bfgkrsx_',
    'infinite': 'alrsx_',

    'merge': 'ilmny_',
    'wisdom': 'abcfglprt_',
    'motion': 'bilmnst_',
    'dependence': 'almpqtv_',
    'dynamic': 'efjkopqrs_',
    'harmony': 'bcghilmnrt_',

    'resurrect': 'ablprtv_',
    'momentum': 'efjklmpst_',
    'static': 'adfghlpqs_',
    'weave': 'aefgx_',
    'balance': 'bcilqs_',
    'exist': 'bfijlmpqrs_',

    'rebirth': 'bcgijlpqrs_',
    'resilence': 'mprsw_',
    'elevate': 'bclrsx_',
    'control': 'bcflopqs_',
    'flow': 'efjkqt_',
    'survival': 'abprsw_',

    'sacrifice': 'bcghjlrt_',
    'believe': 'bcmoprs_',
    'system': 'ceghimno_',
    'time': 'eflqrtx_',
    'tradition': 'abgjkmqst_',
    'remember': 'filmqs_',

    'constraint': 'bdfmoprs_',
    'nurture': 'aefhlnoqt_',
    'sustain': 'ijlmnps_',
    'inhibit': 'cdehklmp_',
    'honor': 'bckmnqs_',
    'ethereal': 'afgiknpqs_',

    'creativity': 'abefgksx_',
    'form': 'fgipqsu_',
    'discover': 'acefgioqr_',
    'stimulate': 'abefhmnoqr_',
    'question': 'dflqx_',
    'explore': 'aefmnps_' 
    }


# Map text to the font keys
def map_text(text):
    result = []
    text = text.lower()
    text_list = text.split(' ')
    
    for text in text_list:

        if text == '':
            text = ' '

        elif text in symbols_map.keys():
            text = symbols_map.get(text)
        
        elif text in word_map.keys():
            text = word_map.get(text)
        
        result.append(text)
    return result


# Create image:  1 23 4 ...
def draw_row(
            text,
            font_size = 96,
            font_color = "Black",
            background_color = 'White',  # 'Color' or None for transparent
            border_size = 32
            ):
    
    text_list = map_text(text)
    
    font = ImageFont.truetype(
        font=font_path + font_ttf,
        size=font_size)
    
    text_length = int(font.getbbox('z')[2] / 1.5) * (len(text_list) - 1)
    
    image_size = (
        font.getsize('z')[0] + text_length + border_size * 2, 
        font.getsize('z')[1] + border_size * 2)
    
    image = Image.new(
        mode="RGBA", 
        color=background_color, 
        size=image_size)
    
    draw = ImageDraw.Draw(
        im=image, 
        mode='RGBA')
    
    draw_position = [
        font.getbbox('z')[1] / 2 + border_size, 
        font.getbbox('z')[1] / -2 + border_size]
    
    x, y = draw_position
    for text in text_list:
        if text == '':
            text = ' '
        draw.text(
            (x, y),
            text, 
            font=font, 
            fill=(*ImageColor.getrgb(font_color),255))

        x += font.getbbox(text)[2] / 1.5
    return image


# Create image:   1
#               2   3
#                 4
def draw_four(
                text,
                font_size = 96,
                font_color = "Black",
                background_color = 'White',  # 'Color' or None for transparent
                border_size = 32
                ):

    text_list = map_text(text)
    
    border_size = int(border_size / 100 * font_size)
    
    font = ImageFont.truetype(
        font=font_path + font_ttf,
        size=font_size)
    
    text_size = font.getsize('z')

    image_size = (
       int(text_size[0] * 2.3) + border_size * 2, 
       int(text_size[1] * 2.3) + border_size * 2)

    image = Image.new(
        mode="RGBA", 
        color=background_color, 
        size=image_size)
    
    draw = ImageDraw.Draw(
        im=image, 
        mode='RGBA')
    
    font_bbox = font.getbbox('z')

    offset = (
        font_bbox[1] * 11.4 + border_size, 
        font_bbox[1] * -0.9 + border_size)

    i = 1
    x, y = offset
    for text in text_list:
        if text == ' ':
            continue

        draw.text(
            (x, y),
            text, 
            font=font, 
            fill=ImageColor.getrgb(font_color))

        if i == 1:
            x -= font_bbox[2] / 1.5 #1.59
            y += font_bbox[3] / 1.48 #1.51
        if i == 2:
            x = offset[0] + font_bbox[2] / 1.5
        if i == 3:
            x = offset[0]
            y = offset[1] + font_bbox[3] * 1.35

        i += 1
    
    return image


# Ask user for number
def ask_input():
    print('----------------------------------')
    text_input = "\nInput some words or font keys to convert to Narayani Lite.\n\
    (Use a double spase to seperate words. Single space to overlap.)\n-> "
    rg_input = "\nDraw symbols in a row or a grid of four? R/G\n-> "
    
    text = input(text_input)
    while True:
        rg = input(rg_input).upper()
        
        if rg in 'ROW':
            layout = 0
            break
        elif rg in 'GRID':
            layout = 1
            break

    return text, layout


# Ask user to save image
def ask_save(image):
    while True:
        ask = '\nWould you like to save this image? Y/N\n-> '
        name = '\nInput a name to save this image as.\n-> '
        saved = '''\nImage saved as "{}"\n'''
        
        yn = input(ask).upper()
        if yn in ('Y', 'YES'):
            file_name = save_path + input(name) + '.png'
            image.save(file_name)
            print(saved.format(file_name))
            break
    
        elif yn in ('N', 'NO'):
            print('\n')
            break
    

# Run
def main():
    view_font_mapping()
    print(symbols_map.keys())
    print(word_map.keys())

    text, row_or_grid = ask_input()
    layout = (draw_row, draw_four)[row_or_grid]
    image = layout(text)
    image.show()
    ask_save(image)
    

if __name__ == "__main__":
    main()
    
    #draw_row('nature  z  uvwx z  Amateria').show()
    #draw_four('Nature Harmony befhklmnq z').show()
