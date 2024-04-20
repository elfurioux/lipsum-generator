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

BEGINNING = ["Lorem","ipsum","dolor","sit","amet,"]

BASIC_WORDS, SPECIAL_WORDS = [], []
for word in LIPSUM:
    if word.count(';')>0 or word.count(',')>0 or word.count('.')>0:
        SPECIAL_WORDS.append(word)
    else:
        BASIC_WORDS.append(word)

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
