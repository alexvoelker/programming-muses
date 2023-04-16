import random
import time

character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', 
                '=', ']', '[', '{', '}', '\\', '|', "'", ';', '"', ':', '?', ',', 
                '.', '<', '>', '`', '~', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 

# count = 0
while True: #count <= 10000000000:
    print(random.choice(character_list), flush=True, end="")
    time.sleep(0.01)
    # count += 1
