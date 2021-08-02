import re
# ascii file -w=200 -char=["","",""]
# arg parse

# file/folder
# if folder do all pics inside

# -w=100 new width
# if -w resize image
# /-w=(\d*)/

# -char=["asf","asf","asf","af"]
# if char new CHARS list
# /-char=(\[.*\])/


def parser(args):
    flags = ""
    w = ""
    char = ""
    if len(args) > 1:
        flags = " ".join(args[1:])
    if flags:
        w = re.findall("-w=(\d*)", flags)
        char = re.findall("-char=(\S*)", flags)
    if char:
        char = list(char[0])
    else:
        char = []
    if w:
        w = int(w[0])
    else:
        w = 0

    file = args[0]
    return [file, w, char]

