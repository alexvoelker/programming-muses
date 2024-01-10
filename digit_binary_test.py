digits_binary = 1

while(True):
    number = 2**digits_binary
    print(f"Digits binary: {digits_binary}, Digits decimal: {str(number).__len__()}")
    digits_binary += 1
