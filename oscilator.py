import time
import os
from random import choice

DO_RANDOMIZE = True

timeout = 0.1 
symbol = "<x>"
end_symbol = "|"
blank_space_symbol = "-"


def print_ascend(x: int):
    for i in range(x):
        os.system('clear')
        print(end_symbol + "".join([blank_space_symbol for y in range(i)]) 
            + symbol + "".join([blank_space_symbol for y in range(x - i)]) + end_symbol)
        time.sleep(timeout)
        
def print_descend(x: int):
    for i in range(x, 0, -1):
        os.system('clear')
        print(end_symbol + "".join([blank_space_symbol for y in range(i)]) 
            + symbol + "".join([blank_space_symbol for y in range(x - i)]) + end_symbol)
        time.sleep(timeout)

while True:
    print_ascend(25)
    print_descend(25)
    if DO_RANDOMIZE:
        timeout = 0.1 * choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        symbol = choice(["X", "<x>", "(*)", "<|>", "><", "][", "+", "^"])
        end_symbol = choice(["!", "|", "[]", "?", "+", "I", ":", "#"])
        blank_space_symbol = choice(["-", "*", "=", ".", "~", "#"])

