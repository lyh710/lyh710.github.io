import PIL, argparse
from PIL import Image
 

msg = '''
        python image_resize.py -i input_image -b basewidth(default=300) -o output_image
      '''

# Initialize parser 
parser = argparse.ArgumentParser(description = msg) 

# Input image
parser.add_argument('-i','--i', help='input image', required=True) 

# Base Width
parser.add_argument('-b', '--b', help='base width, default=300',default=300, required=True) 

# Out image
parser.add_argument('-o', '--o', help='output image', required=True) 

# Read arguments from command line 
args = parser.parse_args() 

# print(args)

input_image  = args.i
img          = Image.open(input_image)
basewidth    = int(args.b)
wpercent     = (basewidth / float(img.size[0]))
hsize        = int((float(img.size[1]) * float(wpercent)))
img          = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
output_image = args.o
img.save(output_image)
