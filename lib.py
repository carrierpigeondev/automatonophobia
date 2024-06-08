import time

PUNCT_1: list = [","]
PUNCT_1_MULT = 10
PUNCT_2: list = [".", "!", "?"]
PUNCT_2_MULT = 30

def xprint(text: str, char_delay: float = 0.03, newline: bool = True):
    for char in text:
        print(char, end="")
        if char in PUNCT_1:
            time.sleep(char_delay * PUNCT_1_MULT)
        elif char in PUNCT_2:
            time.sleep(char_delay * PUNCT_2_MULT)
        else:
            time.sleep(char_delay)
    if newline: print("\n")
