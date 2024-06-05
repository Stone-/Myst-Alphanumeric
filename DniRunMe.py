''' Run Me for D'ni Numerals, Create Image

Ask for a decimal to convert to base-25 D'ni numerals.
Then create and save the result as a PIL.Image using Cyan's D'ni Font. 

There can be rounding errors with some fractional number.

    2024-06-05 - v0.01
    stone@stone-shard.com
    Stone {Matt Cascone}
'''

from DniNumerals import Alphanumericals, ntsToDnifont
from CreateImage import createImage, saveImage,  askKwargs


# Ask for decimal to convert to Base 25.
anum = Alphanumericals()
kwargs = askKwargs()

# Alphanumeric 'decimal'
text = anum.alphanumeric()
font = ntsToDnifont(text)
image = createImage(font, **kwargs)
print(anum.numeric())
saveImage(image)

# Alphabetic fraction
text = anum.alphabetic()
font = ntsToDnifont(text)
image = createImage(font, **kwargs)
print(anum.numeric(fraction=True))
saveImage(image)


