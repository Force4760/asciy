from PIL import Image
def black_and_white(image_path):
   color_image = Image.open(image_path)
   bw = color_image.convert('LA')
   return bw