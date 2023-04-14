#!/Users/alexvoelker/Documents/GitHub/100DaysOfCode-Alex/venv/bin/python3
import os
import subprocess

PASSWORD = "passphrase"
FILE_NAME = "text_file.txt"

input_encrypt = f"{FILE_NAME}.enc"
output_encrypt = f"{FILE_NAME}.dec"


os.system("openssl version")


os.system(f"openssl enc -a -bf-ofb -nosalt -in {FILE_NAME} -out {input_encrypt} -k {PASSWORD}")
output = os.system(f"openssl enc -d -a -bf-ofb -nosalt -in {input_encrypt} -out {output_encrypt} -k {PASSWORD}")
print(output)
# output_info = subprocess.check_output(["du", "-h", f"{output_encrypt}"])
output_info = subprocess.getoutput(["du", "-h", "../CryptoLab/word_list.txt"])

# convert output to string; https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
output_info = output_info.decode()
output_info = output_info.split('\t')[0]  # get only the file size output
output_info = output_info[:len(output_info) - 1]  # all but the last character of the size output
output_info = float(output_info) # convert the size to a float type
print(output_info > 0)

# while True:
#     if output == 0:
#         break

# display decrypted file contents
# try:
#     with open(f"{FILE_NAME}.dec", "r") as decrypted_file:
#         print(decrypted_file.read())
# except FileNotFoundError:
#     print("File not found, please encrypt or move file into directory:\n\t", end="")
#     os.system("pwd")
