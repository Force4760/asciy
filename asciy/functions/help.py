def helper():
    h = """
        ASCII is a standard for encoding text in electronical comunication.

        Ascii is a python cli app that allows you to transform images into ASCII art pieces.

        CLI:
            ascii path -w=new_width -chars=abcdefghij

            path: path to the image
                
                if path is a folder all images inside will be transformed
            
            -w: if specified the image will be resized to that width

            -chars: if specified the characters provided will be used to draw the image                                                                                                                   
    """
    print(h)