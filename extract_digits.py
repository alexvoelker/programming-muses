def sumDigits(num: int) -> int:
    total = 0
    while num != 0:
        if num == 10:
            total += 1
            break
        else:
            total += num % 10
        num //= 10
    return total


print(sumDigits(102))  # 3
print(sumDigits(510))  # 6
print(sumDigits(1330)) # 7
print(sumDigits(1073)) # 11
print(sumDigits(1350)) # 9
