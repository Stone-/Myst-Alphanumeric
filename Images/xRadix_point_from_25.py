import Image

''' Resize the D'ni numder 25 to be used as a radix point. '''

#
open_file = "Dni_25.png"
save_file = None # "Dni_radix.png"

scale = 1/3
offset = ( -4, 25 ) #(20,25)
bg_color = None

  
pict = Image.open( open_file )

bg_size = pict.size

pict_size = ( int( bg_size[0] * scale ), 
              int( bg_size[1] * scale ) )
pict = pict.resize( pict_size )
 
background = Image.new( mode = "RGBA", color = bg_color, size = bg_size )
    
position = ( bg_size[0]//2 - pict_size[0]//2 + offset[0],
             bg_size[1]//2 - pict_size[1]//2 + offset[1] )
    
background.paste( pict, position, mask = pict )

#   
background.show()
if save_file: 
    background.save( save_file )
