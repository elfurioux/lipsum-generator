from lipsum.funcs import (wrap,lipsum)
import lipsum.constants as constants
import os.path

def main(argv: list[str], _vb: bool = False):
    argn = len(argv)
    if argn >= 1 and argv[0]=="-h":
        print(constants.HELP)
        exit(0)
    if argn > 3 or argn < 2:
        # argn>3 will be either 0 or 1 so the error would be either too few or too many arguments
        print("ERROR:", constants.ERR[0x00+int(argn>3)])
        print(constants.USAGE,sep="\n")
        exit(1)

    filename = argv[0]
    usr_wordcount = argv[1]
    options = argv[2:]

    _abs_fname = os.path.abspath(filename)
    _dir = os.path.dirname(_abs_fname)
    if os.path.isfile(filename):
        print("ERROR:",constants.ERR[0x10].format(filename))
        exit(1)
    if not os.path.isdir(_dir):
        print("ERROR:",constants.ERR[0x11].format(_dir))
        exit(1)

    try:
        wordcount = int(usr_wordcount)
    except ValueError:
        print("ERROR:",constants.ERR[0x12].format(usr_wordcount))
        exit(1)

    for opt in options:
        if opt not in constants.ARGUMENTS:
            print("ERROR:",constants.ERR[0x12].format(opt))
            exit(1)

    if _vb: print(f"{filename=}; {wordcount=}; {options=}")

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
    main(argv=argv[1:])
