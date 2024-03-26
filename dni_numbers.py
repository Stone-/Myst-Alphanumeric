import Image
import math

'''
    D'ni Numbers

This will create an image of D'ni numbers.

Does not handle negative numbers, I don't have a D'ni symbol for it.
There can be rounding errors with some fractional number.

    version 0.1
    2024-03-25
    stone@stone-shard.com
    Stone
'''


###########################
# User editable settings ##
class user:
    border_size = 100
    background_color = "White"

###########################


# Convert a decimal to a list of base 25 intagers
def to_base25(decimal):
    'decimal -> [int, ]'
    "http://is.gd/aa9xJb"
    base25 = []
    ty = type(decimal)
    decimal = math.fabs(decimal)
    integral = int(decimal)
    fractional = decimal - integral
    fractional = float(str(decimal)[len(str(integral)):])
    
    while integral >= 0:
        base25.insert(0, integral % 25)
        integral = integral // 25
        if integral == 0:
            break
    
    if ty is float:
        i = 1
        limit = len(str(fractional)) - 2
        base25.append(26)
        
        while fractional >= 0:
            fract_25 = fractional * 25
            fractional = fract_25 - int(fract_25)
            base25.append(int(fract_25))   
            
            i += 1
            if i > limit or i >= 10:
                break

    return base25
    

# Create an image of D'ni numbers from a list of base 25 intagers
def to_dni(base_25: [int,]):
    '[base25 int, ] -> Image'
    
    # Load in D'ni numeric symbols
    symbols = []
    for i in range(0, 28):
        symbols.append(Image.open("Images/Dni_%02d.png" % i))

    xd, yd = symbols[0].size  # Background
    char_size = (xd-14, yd-33)  # Character
    offset_size = (xd-60, yd)  # Croped
    
    # Create a empty image
    char_per_row = len(base_25)

    image_size = (
        offset_size[0]
            * char_per_row 
            - offset_size[0]
            + char_size[0]
            + user.border_size * 2,
        
        offset_size[1]
            * int(math.ceil(len(base_25)/char_per_row))
            - offset_size[1]
            + char_size[1]
            + user.border_size * 2
        )
    
    image = Image.new(
        mode = "RGBA",
        color = user.background_color,
        size = image_size
        )
    
    # Paste everthing into the new image
    count = 0
    offset_x = 0
    offset_y = 0
    for n in base_25:
        count += 1

        image.paste(
            symbols[n],
            (offset_x + user.border_size, offset_y + user.border_size),
            mask = symbols[n])
    
        offset_x += offset_size[0]
        if count >= char_per_row:
            offset_x = 0
            offset_y += offset_size[1]
            count = 0
    
    # Show and save
    image.show()
    print('Image size =', image.size)
    
    save_file = ask_save()
    if save_file:
        image.save(f"{save_file}.png")
        print(f'''\n<- Image was saved as "{save_file}.png"\n''')
    
    return image


# Ask user for number
def ask_decimal():
    print('----------------------------------')
    n = input("\nInput a number to convert to D'ni.\n-> ")
    print("\nConverting to base 25...")
    if n.isdigit():
        n = int(n)
    else:
        n = float(n)
    return n


# Ask user to save
def ask_save():
    while True:
        yn = input('\nWould you like to save this image? Y/N\n-> ').upper()
        if yn in ('Y', 'YES'):
            name = input('\nInput a name to save this image as.\n-> ')
            break
        elif yn in ('N', 'NO'):
            name = None
            break
    return name


# Run
def main():
    while True:
        to_dni(to_base25(ask_decimal()))


if __name__ == "__main__":
    main()
