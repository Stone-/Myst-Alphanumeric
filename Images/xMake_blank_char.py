import Image

''' Make an empty image to use as a space. '''

open_file = "Dni_00.png"
save_file = None #"Dni_space.png"


back_size = Image.open(open_file).size

background = Image.new( 
    mode = "RGBA", 
    color = None, 
    size = back_size )

background.show()
if save_file:
    background.save(save_file)
