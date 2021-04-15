def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    print(width)
    print(height)
    print(new_width)
    print(ratio)
    new_height = int(new_width * ratio)
    print(new_height)
    resized = image.resize((new_width, new_height))
    return resized