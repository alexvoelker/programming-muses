from summary_statistics import Statistics

# with open("stats.txt", 'r') as file:
#     info = file.read()
#     data = info.split("\n")
#     data = [float(item) for item in data]
#     print(data)
# print(f"Length of data Set: {len(data)}")
#
# stats = Statistics()
# stats.set_values(data)
# stats.print_summary_statistics()
#
# data_sorted = sorted(stats.get_values())
# highest = data_sorted[len(data_sorted) - 1]
# print(highest - stats.avg())
# print((highest - stats.avg()) / stats.std_deviation())
#
# with open("stuff2.txt", 'r') as file:
#     info = file.read()
#     data2 = info.split("\n")
#     data2 = [float(item) for item in data2]
#     print(data2)
# print(f"Length of data Set: {len(data2)}")
#
# stats = Statistics()
# stats.set_values(data2)
# stats.print_summary_statistics()
#
# data_sorted = sorted(stats.get_values())
# highest = data_sorted[len(data_sorted) - 1]
# print(highest)
# print(highest - stats.avg())
# print((highest - stats.avg()) / stats.std_deviation())

with open("lab4.txt", 'r') as file:
    info = file.read()
    data = info.split("\n")
    data = [float(item) for item in data]
    print(data)
print(f"Length of data Set: {len(data)}")

stats = Statistics()
stats.set_values(data)
stats.print_summary_statistics()

print(stats.median())
print(stats.Q1())
print(stats.Q3())
print(stats.IQR())
