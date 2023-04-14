#!/Users/alexvoelker/Documents/GitHub/100DaysOfCode-Alex/venv/bin/python3
import os
import subprocess
import asyncio

PASSWORD = "passphrase"
FILE_NAME = "text_file.txt"

input_encrypt = f"{FILE_NAME}.enc"
output_encrypt = f"{FILE_NAME}.dec"

os.system("openssl version")


async def encrypt_file(file_name, output_name, password):
    command_encrypt = f"openssl enc -a -bf-ofb -nosalt -in {file_name} -out {output_name} -k {password}"
    cmd_output = subprocess.getoutput(command_encrypt)
    return cmd_output

async def decrypt_file(file_name, output_name, password):
   command_decrypt = f"openssl enc -d -a -bf-ofb -nosalt -in {file_name} -out {output_name} -k {password}"
   cmd_output = subprocess.getoutput(command_decrypt)
   return cmd_output

async def main():
    out = await encrypt_file(FILE_NAME, input_encrypt, PASSWORD)
    print(out)
    out = await decrypt_file(input_encrypt, output_encrypt, PASSWORD)
    print(out)
    print(subprocess.getoutput(f"file {output_encrypt}"))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # display decrypted file contents
    try:
        with open(f"{FILE_NAME}.dec", "r") as decrypted_file:
            print(decrypted_file.read())
    except FileNotFoundError:
        print("File not found, please encrypt or move file into directory:\n\t", end="")
        os.system("pwd")

