import Image
import math


'''
    D'ni Numeral

This will create an image of D'ni numerals.

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
    border_size = 50
    background_color = "White"
    max_char_per_row = 25
    resize_x_y = False, False
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


# Open the numrals we need
def numeral_gen(ints):
    "ints: [int, ] -> images:gen, len, (int,int), (int, int)"
    t = "Images/Dni_%02d.png"
    x, y = Image.open(t % 0).size
    size = (x-14, y-33)  # Character
    offset = (x-60, y)  # Croped

    def images():
        for n in ints:
            yield Image.open(t % n)

    return (images, len(ints), size, offset)


# Create an image of D'ni numbers from a list of symbols
def to_dni(numerals, char_count, char_size, offset_size):
    '[Image,], int, (x,y), (x,y) -> Image'

    char_per_row = char_count
    if  char_per_row > user.max_char_per_row:
        char_per_row = user.max_char_per_row

    # Create a empty image
    image_size = (
        offset_size[0]
            * char_per_row
            - offset_size[0]
            + char_size[0]
            + user.border_size * 2,

        offset_size[1]
            * int(math.ceil(char_count/char_per_row))
            - offset_size[1]
            + char_size[1]
            + user.border_size * 2
        )

    image = Image.new(
        mode = "RGBA",
        color = user.background_color,
        size = image_size
        )

    # Paste everthing into the empty image
    count = 0
    offset_x = 0
    offset_y = 0
    for symbol in numerals():
        count += 1

        image.paste(
            symbol,
            (offset_x + user.border_size, offset_y + user.border_size),
            mask=symbol)

        offset_x += offset_size[0]
        if count >= char_per_row:
            offset_x = 0
            offset_y += offset_size[1]
            count = 0

    # Resize the image
    x, y = user.resize_x_y
    if x or y:
        X, Y = image.size
        if x:
            y = int(Y / (X / x))
        elif y:
            x = int(X / (Y / y))
        image = image.resize((x, y))

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


# Ask user to save image
def ask_save(image):
    image.show()
    print('Image size =', image.size)

    while True:
        yn = input('\nWould you like to save this image? Y/N\n-> ').upper()

        if yn in ('Y', 'YES'):
            file_name = input('\nInput a name to save this image as.\n-> ')
            image.save(f"{file_name}.png")
            print(f'''\n<- Image was saved as "{file_name}.png"\n''')
            break

        elif yn in ('N', 'NO'):
            break

    return image


# Run
def main():
    while True:
        ask_save(to_dni(*numeral_gen(to_base25(ask_decimal()))))


if __name__ == "__main__":
    main()
