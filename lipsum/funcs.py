from random import randint
import lipsum.constants as constants

def pick(__l: list) -> object:
    """Pick a random index in the list `__l` and returns it."""
    return __l[randint(0, len(__l)-1)]

def gen(words: int, lipsumStart: bool = False) -> str:
    """Generates a Lorem Ipsum text with a determined number of words."""
    __text = []

    for i in range(words):
        if i+1 >= words: # if it's the last iteration
            __text.append(pick(constants.SPECIAL_WORDS)[:-1] + ".")
        elif i == 0: # first iteration
            __text.append(str.capitalize(pick(constants.BASIC_WORDS)))
        elif randint(1,10) <= 8: # ~80% chance
            __text.append(pick(constants.BASIC_WORDS))
        else:
            __text.append(pick(constants.SPECIAL_WORDS))

    if lipsumStart:
        return " ".join(constants.BEGINNING + __text[5:])
    return " ".join(__text)

def wrap(text: str, char_per_line: int, tolerance: float = 0.10) -> str:
    """Word wrapping function, loops through the `text` and when the line is at least
    `char_per_line` long, marks a newline at the next word, `tolerance` is a float
    number from 0 to 1, it represents the absolute maximum characters per line, such as:
    `char_per_line` * (1 + `tolerance`)
    Example, `tolerance` is `0.10` and `char_per_line` is 100, the maximum numbers of chars
    per line is `100*1.10` = `110`
    Tolerance of zero cuts the string precisely at `char_per_line` numbers of chars."""
    __rtext = ""

    i = 0
    for char in text:
        i += 1
        if i <= char_per_line:
            __rtext += char
            continue

        # From this point code executes if i is over char_per_line
        if i < char_per_line*(1+tolerance):
            if char == ' ':
                __rtext += '\n'
                i = 0
            else:
                __rtext += char
        
        # If a space is not found between the char_per_line and tolerance,
        # cuts the line here and \n
        else:
            __rtext += '-' + '\n'
            i = 0

    return __rtext
