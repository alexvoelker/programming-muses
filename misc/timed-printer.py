from time import sleep
from sys import stdout

# in seconds
time_delta_input = input("Initial time delta in seconds (-1 for default): ")
time_delta_seconds = 0.05 if time_delta_input == '' or \
    float(time_delta_input) == -1.0 else float(time_delta_input) 

# deceases time delta by a factor every iteration
decrease_factor_input = input("Decrease factor (-1 for default): ")
decrease_factor = 1.05 if decrease_factor_input == '' or \
    float(decrease_factor_input) == -1 else float(decrease_factor_input) 

iterations_input = input("Number of characters to print? (-1 for default): ")
max_iterations = 1000 if iterations_input == '' \
    or int(iterations_input) == -1 else int(iterations_input)
character = input("Character to print: ")

stats = True if input("print stats? (y/n) ") == 'y' else False

if stats == True:
    print("Details:")
    print(f"\ttime_delta_input: {time_delta_seconds}\n \
    \tdecrease_factor: {decrease_factor}\n \
    \tmax_iterations: {max_iterations}\n \
    \tcharacter to print: '{character}'")

for i in range(max_iterations):
    print(character, end='', file=stdout, flush=True)
    sleep(time_delta_seconds)
    time_delta_seconds = time_delta_seconds / decrease_factor

