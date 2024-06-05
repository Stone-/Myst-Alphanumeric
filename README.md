# Myst Alphanumericals
-----------------------------------------------------------------
"Alphanumericals or Alphanumeric characters are any collection of number characters and letters in a certian language."[^wiki]

These will create text and images of the D’ni  alphanumeric characters found in the Myst game series.


## DniNumerals.py
-----------------------------------------------------------------
Convert a decimal to base 25,  *Pentavigesimal[^Fandom]* numeral.

>**class Alphanumericals:**  
	*Convert a decimal to a D’ni, base-25.*  

>- __ __init__ __(decimal: float):  
	*Decimal to convert to base-25.*

>- **alphabetic**(standard: string') -> str  
	*D'ni Alphabetic Translation Standard. "OTS" or "NTS"*    
	"-sehnsee+fah/vahgahbree"

>- **alphanumeric**(fraction: bool) -> str:   
	*Base-25 Alphanumeric Number System.*   		0123456789ABCDEFGHIJKLMNO  
	"-3.3DC8E" or as fraction "-3+1/7"
   
>- **numeric**(fraction: bool) -> string:  
	*Numeric base-25 number.*  
	"|-|3|.|3|13|12|8|14|" *or as fraction* "|-|3|+|1|/|7|"


**ntsToDnifont**(text: str) -> string:  
   *Map Alphanumeric or New Translation Standards to the D’ni Font[^dnifont].*   
   "-3.3#@8$"


## CreateImage.py
-----------------------------------------------------------------
*"Create and save a PIL Image from the given font string."*  

**createImage**( text: string , **kwargs) -> PIL.Image:  
*Create a PIL Image from the given font string.*

**saveImage**(image: PIL.Image, name: string, path: string) -> str:  
*Save the given Image.*

**askKwargs**() -> {'kw':'args'}:  
*Ask user to input the kwargs, used when creating an Image.*  
ex: createImage("text", **askKwargs()) 


## Examples: 
-----------------------------------------------------------------

### Alphabetic fraction:

Ask for decimal..

	anum = Alphanumericals()

Convert the decimal to alphabetic "NTS".  

	nts = anum.alphabetic()

Convert NTS to dnifont[^dnifont].  

	dni = ntsToDnifont(nts)

Ask for kwargs.

	kwargs = askKwargs()

Draw the image.  

	image = createImage(dni, **kwargs)

Ask to save image

	saveImage(image)
![image](https://github.com/Stone-/Myst-Alphanumeric/blob/main/Images/dni_spell_numbers%20-%3E%2025.png)


### Alphanumeric:

	anum = Alphanumericals(25).alphanumeric()
	dni = ntsToDnifont(anum)
	image = createImage(dni, font_color="Black", stroke_color="DniCyan")
	saveImage(image)
![image](https://github.com/Stone-/Dni-Alphanumeric/blob/4ede0b41ca1f9ff67ee7c31fd08a40faba2620c1/Images/dni_numerals%20-%3E%20233.png)


# Narayani
-----------------------------------------------------------------

## narayani_numerals.py  
Convert a decimal to the number system from Saavedro's journal found in Myst III: Exile. Uses the *Narayani Light[^Jehon]* font.  
![image](https://github.com/Stone-/Dni-Alphanumeric/blob/4ede0b41ca1f9ff67ee7c31fd08a40faba2620c1/Images/narayani%20_numerals%20-%3E%2017.png)


## narayani_words.py   
Create an image using Narayani words as seen in Myst III: Exile. Uses the *Narayani Light[^Jehon]* font.  
![image](https://github.com/Stone-/Dni-Alphanumeric/blob/4ede0b41ca1f9ff67ee7c31fd08a40faba2620c1/Images/narayani_words%20-%3E%20____.png)


# Useful Links: 
-----------------------------------------------------------------

### Guild of Archivists'

- Myst Fonts:
https://www.guildofarchivists.org/utilities/fonts/

-  D’ni Numerals:
https://archive.guildofarchivists.org/wiki/D'ni_numerals


### Myst Embassy

- D’ni Font Chart[^BladeLakem]:
http://www.mystembassy.net/downloads/dnifontchart.pdf

-----------------------------------------------------------------

    2024-06-05 - v0.01
    stone@stone-shard.com
    Stone {Matt Cascone}
   


[^Cyan]: [Cyan inc.](https://cyan.com/)

[^dnifont]: **D’ni Font** - Copyright 볉 1995 by Cyan, Inc.

[^Jehon]: **Narayani Light Font** - created by Jehon aka. Sebastian Ochs.

[^BladeLakem]: **D’ni Font Chart** - Created by community member BladeLakem.

[^wiki]: [“Alphanumericals" - wiki](https://en.m.wikipedia.org/wiki/Alphanumericals)
 
[^Fandom]: [Base naming systems - Fandom.com](https://numerals.fandom.com/wiki/Base_naming_systems)
