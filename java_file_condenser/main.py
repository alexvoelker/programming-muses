file_name = input("Enter a file name in this directory to condense into one line: ")

try:
    with open(f"{file_name}", 'r') as in_file:
        contents = ""
        for line in in_file.readlines():
            contents += line[:len(line) - 1].strip()
    
    print(f"contents: {contents}")

    with open(f"out.{file_name}", 'w') as out_file:
        out_file.write(contents)
    print(f"Data written to out.{file_name}")
    
except FileNotFoundError:
    print("No file of that name found.")

