KG_LB = 0.45359237 # Kilograms in 1 Pound
LB_KG = 2.2046226218 # Pounds in 1 Kilogram

unit = input("Convert from Kilograms to Pounds (K) or Pounds to Kilograms (P): ")
try:
    quantity = eval(input("How many: "))
    if unit.upper() == "P":
        print(f"\t{quantity * KG_LB}")
    elif unit.upper() == "K":
        print(f"\t{quantity * LB_KG}")
    else:
        print("Invalid unit entered!")
except NameError:
    print("Enter a number!")

