import os

def get_name(path):
    base=os.path.basename(path)
    return os.path.splitext(base)[0]

def get_ext(path):
    base=os.path.basename(path)
    return os.path.splitext(base)[1]
