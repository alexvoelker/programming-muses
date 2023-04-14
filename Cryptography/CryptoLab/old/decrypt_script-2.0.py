import asyncio
import subprocess
import threading

PATH = subprocess.getoutput("pwd") + "/Cryptography/CryptoLab/"

with open(f"{PATH}word_list.txt", "r") as word_list_file:
    word_list = sorted(word_list_file.read().split("\n"))

input_file_name = "chand.txt.secret"
output_file_name = "chand.txt"

async def compare_output_file() -> bool:
    check_file_output = subprocess.getoutput(f"file {PATH}{output_file_name}")
    if "ASCII text" in check_file_output:
        return True
    return False

async def check_password(pass_in) -> bool:
    cmd_output = subprocess.getoutput(
        f"openssl enc -d -bf-ofb -nosalt -in {PATH}{input_file_name} -out {PATH}{output_file_name} -k {pass_in}")
    # Check if decrypted properly
    return await compare_output_file()

async def main():
    total = len(word_list)
    index = 1

    while len(word_list) > 0:
        current_password = word_list.pop()
        print(
            f"Current Key Checked [ {index / total * 100:.2f}% | {index} / {total} ]: \t{current_password}")
        password_status = await check_password(current_password)
        if password_status:
            print(f"\n\n#####\tPASSWORD FOUND!:\t {current_password}\t#####") 
            break   
        index += 1


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

# display decrypted file contents
try:
    with open(f"{PATH}{output_file_name}", "r") as decrypted_file:
        print(decrypted_file.read())
except FileNotFoundError:
    print(f"File not found, please encrypt or move file into directory:\n\t{PATH}")
