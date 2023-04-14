import asyncio
import subprocess
import os

PATH = subprocess.getoutput("pwd") + "/Cryptography/practice/dec_script2-test/"

with open(f"{PATH}word_list.txt", "r") as word_list_file:
    word_list = word_list_file.read().split("\n")

input_file_name = "file.secret"
output_file_name = "file.decoded.txt"

async def compare_output_file() -> bool:
    out_file_type = subprocess.getoutput(f"file {PATH}{output_file_name}")
    if "ASCII text" in out_file_type:
        return True
    return False

async def check_password(pass_in) -> bool:
    cmd_output = subprocess.getoutput(f"openssl enc -d -bf-ofb -nosalt -in {PATH}{input_file_name} -out {PATH}{output_file_name} -k {pass_in}")
    # Check if decrypted properly
    return await compare_output_file()

async def main():
     while len(word_list) > 0:
        current_password = word_list.pop()
        print(f"Current Key Checked: {current_password}", end="")
        password_status = await check_password(current_password)
        if password_status:
            print(f"\n\n\tPassword found!:\t {current_password}")
            break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

# display decrypted file contents
try:
    with open(f"{PATH}{output_file_name}", "r") as decrypted_file:
        print("\n\n\t\t\tFILE CONTENTS\n\n")
        print(decrypted_file.read())
except FileNotFoundError:
    print("File not found, please encrypt or move file into directory:\n\t", end="")
    os.system("pwd")
