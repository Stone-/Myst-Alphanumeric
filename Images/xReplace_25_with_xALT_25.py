import Image

''' Replace the broken D'ni 25 image with a new one. '''

#Image.open("Dni_25.png").save("Dni_25.png-_ORGINAL_WITH_BAD_MASK.png")

open_file = "xAlt_25.PNG"
save_file = None #"Dni_25.png"

pict_size = ( 194-14-2, 186-33-2 )

pict = Image.open( open_file ).resize( pict_size )
background = Image.new( mode = "RGBA", color=None, size=Image.open("Dni_00.png").size )

background.paste( pict, (0,1), mask = pict )

#test = Image.open( "Dni_00.png" )
#background.paste( test, (0,0), mask = test)

background.show()
if save_file:
    background.save( save_file )


