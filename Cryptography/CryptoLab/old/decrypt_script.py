import os

with open("word_list.txt", "r") as word_list_file:
    word_list = word_list_file.read().split("\n")

input_file_name = "chand.txt.secret"
output_file_name = "chand.txt"

while len(word_list) > 0:
    PASSWORD = word_list.pop()

    output_status = os.system(
        f"openssl enc -d -a -bf-ofb -nosalt -in {input_file_name} -out {output_file_name} -k {PASSWORD}")

    # Find output file size: https://stackoverflow.com/questions/2104080/how-do-i-check-file-size-in-python
    output_length = os.path.getsize(f"{output_file_name}")

    # # obtain command output: https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
    # # Checking file size: https://www.howtouselinux.com/post/check-file-size-in-linux
    # output_info = subprocess.check_output(f"du {output_file_name}")
    #
    # # convert output to string; https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
    # output_info = output_info.decode()
    # output_info = output_info.split('\t')[0]  # get only the file size output
    # output_info = int(output_info)  # convert the size to a float type
    # print(output_info)

    # Check if the command was run successfully and the output file contains data

    if output_status == 0 and output_length > 0:
        print(output_length)
        print(f"Password found!\t {PASSWORD}")
        break


# display decrypted file contents
try:
    with open(f"{output_file_name}", "r") as decrypted_file:
        print(decrypted_file.read())
except FileNotFoundError:
    print("File not found, please encrypt or move file into directory:\n\t", end="")
    os.system("pwd")
