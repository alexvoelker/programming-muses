import getopt, sys

def join(arr: list[int], s: str) -> str:
	out = ''
	for i in range(len(arr) - 1):
		out += str(arr[i]) + s
	if len(arr) > 0:
		out += str(arr[len(arr) - 1])
	return out


def extract_digit(x: int) -> int:
	digits = 0
	if x == 0:
		return 0

	while x > 0:
		x = x // 10
		digits += 1
	return digits


def print_tree(x: int):
	largest_digit = extract_digit(x)
	spaces = (largest_digit * x * 2 - 2) * 2 + 1
	spaces = spaces if spaces > 3 else 3

	for i in range(1, x + 1):
		array = [i]
		for j in range(i - 1, 0, -1):
			array.insert(0, j)
			array.append(j)
		print(f"{join(array, ' '):^{spaces}}")
	print(f"{'| |':^{spaces}}")

if __name__ == '__main__':
	list_of_arguments = sys.argv[1:]
	if len(list_of_arguments) > 0:
		options = "s:"
		long_options = ["size="]
		try:
			arguments, values = getopt.getopt(list_of_arguments, options, long_options)
			# Only one argument is set up now
			print(arguments[0][1])

			if len(arguments) >= 1:
				if arguments[0][0] in ("-s", "--size"):
					print(arguments[0][1])
					print_tree(int(arguments[0][1]))
		except getopt.error as error:
			print(str(error))
	else:
		print_tree(5)
