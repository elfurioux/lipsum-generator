from random import randint
 
BASIC_LIPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus
tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas
ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim
est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae,
consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras
vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque
sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing
ante non diam sodales hendrerit. Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci
vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis
ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id
felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum
dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et
sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis
vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula
justo vitae magna. Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis,
ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus
leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla
in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel
rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.
"""
LIPSUM = BASIC_LIPSUM.replace("\n"," ").split(" ")

basicWords, specialWords = [], []
for word in LIPSUM:
    if word.count(';')>0 or word.count(',')>0 or word.count('.')>0:
        specialWords.append(word)
    else:
        basicWords.append(word)

def pick(__l: list):
    return __l[randint(0, len(__l)-1)]

def lipsum(words: int, startswithloremipsum: bool = False) -> str:
    __text = []

    for i in range(words):
        if i+1 >= words: # if it's the last iteration
            __text.append(pick(specialWords)[:-1] + ".")
        elif i == 0: # first iteration
            __text.append(str.capitalize(pick(basicWords)))
        elif randint(1,10) <= 8: # ~80% chance
            __text.append(pick(basicWords))
        else:
            __text.append(pick(specialWords))

    if startswithloremipsum:
        return " ".join(["Lorem","ipsum","dolor","sit","amet,"] + __text[5:])
    return " ".join(__text)

def wrap(text: str, char_per_line: int, tolerance: float = 0.10) -> str:
    __rtext = ""

    i = 0
    for char in text:
        i += 1
        if i <= char_per_line:
            __rtext += char
            continue

        if i < char_per_line*(1+tolerance):
            if char == ' ':
                __rtext += '\n'
                i = 0
            else:
                __rtext += char
        
        else:
            __rtext += '-' + '\n'
            i = 0

    return __rtext

import os.path

__HSUGG = "Type 'python lipsum.py -h' for more infos"
USAGE = "Usage: python lipsum.py <filename> <word count> [-l | --lorem]" + '\n' + __HSUGG
HELP = f"""{USAGE.split('\n')[0]}

-h              : Provides this help page and then exit.
-l | --lorem    : [Optional] Starts the lipsum by "Lorem ipsum dolor sit amet, (...)"
"""[:-1]
ERR = {
    # 0x00 to 0x1F: Critical argument errors
    #   0x00 to 0x0F: Classic argument error
    #   0x10 to 0x1F: Argument error to be provided with 1 string via format()
    0x00: "TOO FEW ARGUMENTS",
    0x01: "TOO MANY ARGUMENTS",
    0x10: "FILE \"{0}\" ALREADY EXISTS",
    0x11: "DIRECTORY \"{0}\" DOESN'T EXIST, CREATE IT",
    0x12: "INVALID WORDCOUNT \"{0}\"",
    0x12: "UNRECOGNISED ARGUMENT \"{0}\""
}
ARGUMENTS = ["-l","--lorem"]

def main(argv: list[str]):
    argn = len(argv)
    if argn >= 2 and argv[1]=="-h":
        print(HELP)
        return
    if argn > 4 or argn < 3:
        print("ERROR:", ERR[0x00+int(argn>4)])
        print(USAGE,sep="\n")
        return

    filename = argv[1]
    usr_wordcount = argv[2]
    options = argv[3:]

    _abs_fname = os.path.abspath(filename)
    _dir = os.path.dirname(_abs_fname)
    if os.path.isfile(filename):
        print("ERROR:",ERR[0x10].format(filename))
        return
    if not os.path.isdir(_dir):
        print("ERROR:",ERR[0x11].format(_dir))
        return

    try:
        wordcount = int(usr_wordcount)
    except ValueError:
        print("ERROR:",ERR[0x12].format(usr_wordcount))
        return

    for opt in options:
        if opt not in ARGUMENTS:
            print("ERROR:",ERR[0x12].format(opt))
            return

    # print(f"{filename=}; {wordcount=}; {options=}")

    text = wrap(
        lipsum(wordcount, len(options)>0),
        90,
        0.15
    )
    with open(file=filename,mode="w",encoding="utf8") as fstream:
        fstream.write(text)
    
    print("done!")

if __name__=="__main__":
    from sys import argv
    main(argv)
