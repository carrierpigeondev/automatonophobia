import time

def xprint(text: str, char_delay: float = 0.02, newline: bool = True):
    for char in text:
        print(char, end="")
        time.sleep(char_delay)
    if newline: print("\n")
