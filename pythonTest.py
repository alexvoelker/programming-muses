import time

time_start = time.time_ns()

for item in range(0, 10000000000):
    print(f"at index: {item}\n" if item % 10000000 == True else "", end="")

time_elapsed = time.time_ns() - time_start
print(f"Loop Completed in {time_elapsed} nano seconds")


