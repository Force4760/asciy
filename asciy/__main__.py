import sys
import os
from .functions.parser import parser
from .functions.bw import black_and_white
from .functions.resize import resize_image
from .functions.save import save
from .functions.draw import draw_ascii
from .functions.help import helper
from .functions.get_name import get_name, get_ext

def main():
    args = sys.argv[1:]
    if args:
        file, w, c = parser(args)
        if c:
            chars = c
        else:
            chars = ["@", "#", "S", "%", "?", "*","+",";",":","."]

        if os.path.isfile(file):
            process_file(file,w,chars,get_name(file)+".txt")
        elif os.path.isdir(file):
            if not os.path.exists('ascii'):
                os.makedirs('ascii')
            process_folder(file,w,chars, "ascii")
    else:
        helper()

    


def process_folder(f,w,chars, final_folder):
    files = os.listdir(f)
    for file in files:
        p = os.path.join(f,file)
        ext = get_ext(p)
        if ext == ".jpeg" or ext == ".jpg" or ext == ".png":
            process_file(p, w, chars,os.path.join(f,os.path.join(final_folder,get_name(p)+".txt")))

def process_file(f,w,chars, name):
    img=black_and_white(f)
        
    if w:    
        img = resize_image(img, w)

    width,height = img.size

    divider = 255 // (len(chars)-1)

    ascii_img = draw_ascii(img, chars, height, width, divider)

    save(ascii_img, name)






if __name__ == '__main__':  
    main()