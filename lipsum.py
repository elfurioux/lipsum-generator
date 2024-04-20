from lipsum.utils import (wrap,lipsum)
import os.path

_NL = '\n'
__HSUGG = "Type 'python lipsum.py -h' for more infos"
USAGE = "Usage: python lipsum.py <filename> <word count> [-l | --lorem]" + '\n' + __HSUGG
HELP = f"""{USAGE.split(_NL)[0]}

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
