file = "POI-binary.txt"

with open(file, 'r') as data:
    data_workable = [int(_.replace("\n", ""), 2) for _ in data.readlines()]


print("Data in binary:")
for _ in data_workable:
    _ = str("{:b}".format(_)).rjust(27, '0')
    print(f"\t{_}")


print("Data in base-10:")
for _ in data_workable:
    print("\t%i" % _)


print("Data in hexadecimal:")
for _ in data_workable:
    print("\t{:x}".format(_).upper())


print("Data in ASCII:\n")
concatenated_data = ""
for _ in data_workable:
    concatenated_data += str("{:b}".format(_)).rjust(27, '0')

print(concatenated_data)

chars = []
for i in range(0, len(concatenated_data) // 8):
    chars.append(int(concatenated_data[i*8:(i+1)*8-1], 2))

print(chars)
chars = [ascii(c) for c in chars]
print(chars)
