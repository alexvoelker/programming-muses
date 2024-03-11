def DecimalToBinary(string: str) -> str:
    nums = string.split(".")
    for i in range(len(nums)):
        nums[i] = str(bin(int(nums[i]))[2:])
    return ".".join(nums)
def BinaryToDecimal(string: str) -> str:
    nums = string.split(".")
    for i in range(len(nums)):
        digits = []
        for j in range(len(nums[i])):
            if nums[i][len(nums[i]) - j - 1] == '1':
                digits.append(2**j)
                # print(f"2^{j}={2**j}")
        # print(digits)
        nums[i] = str(sum(digits))
    return ".".join(nums)


while True:
    option = input("Decimal to Binary (1) or Binary to Decimal (2)? ")
    if option == "1":
        print(DecimalToBinary(input("Enter an IPv4 Address (incuding decimals): ")))
    elif option == "2":
        print(BinaryToDecimal(input("Enter Binary Values Separated by Decimals: ")))
    else:
        print("Invalid Option")
