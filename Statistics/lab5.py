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

with open("data_sets/weights_lab_5.txt", 'r') as file:
    info = file.read()
    data = info.split("\n")
    data = [float(item) for item in data]
    print(data)
print(f"Length of data Set: {len(data)}")

stats = Statistics()
stats.set_values(data)

deviation = stats.std_deviation()
for i in range(1, 4):
    print(i)
    std_dev_set = []
    upper_bound = deviation * i + stats.avg()
    lower_bound = deviation * i - stats.avg()
    print(f"Deviation: {deviation * i}"
          f"\nUpper Bound: {upper_bound}"
          f"\nLower Bound: {lower_bound}")

    for value in stats.values:
        if not (value > upper_bound or value < lower_bound):
            std_dev_set.append(value)

    print(f"{std_dev_set}\nLen set: {len(std_dev_set)}"
          f"\n% of data: {len(std_dev_set) / len(stats.values) * 100}")
