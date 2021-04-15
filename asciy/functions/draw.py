def draw_ascii(image, chars,height, width, divider):
    px = image.load()
    ascii_img=""
    for y in range(1,height):
        for x in range(1,width):
            col, alpha = px[x,y]
            if alpha:
                ascii_img+=str(chars[int(col/divider)])
            else:
                ascii_img+=" "
        ascii_img+="\n"
    
    return ascii_img