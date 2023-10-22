def join(arr: list[int], s: str) -> str:
	out = ''
	for i in range(len(arr) - 1):
		out += str(arr[i]) + s
	if len(arr) > 0:
		out += str(arr[len(arr) - 1])
	return out


def print_tree(x: int):
	spaces = (x * 2 - 2) * 2 + 1
	spaces = spaces if spaces > 3 else 3

	for i in range(1, x + 1):
		array = [i]
		for j in range(i - 1, 0, -1):
			array.insert(0, j)
			array.append(j)
		#print(f"i: {i} // {join(array, ' ')}")
		print(f"{join(array, ' '):^{spaces}}")
	print(f"{'| |':^{spaces}}")

if __name__ == '__main__':
	print_tree(5)
