import asyncio
import subprocess
import threading

PATH = subprocess.getoutput("pwd") + "/Cryptography/CryptoLab/"

with open(f"{PATH}word_list.txt", "r") as word_list_file:
    word_list = sorted(word_list_file.read().split("\n"))

input_file_name = "chand.txt.secret"
output_file_name = "chand.txt"

PASSWORD_FOUND = False

total = len(word_list)
index = 0

async def compare_output_file() -> bool:
    if "ASCII text" in subprocess.getoutput(f"file {PATH}{output_file_name}"):
        return True
    return False

async def check_password(pass_in) -> bool:
    cmd_output = subprocess.getoutput(
        f"openssl enc -d -bf-ofb -nosalt -in {PATH}{input_file_name} -out {PATH}{output_file_name} -k {pass_in}")
    # Check if decrypted properly
    return await compare_output_file()

async def main():
    while len(word_list) > 0 and not PASSWORD_FOUND:
        index += 1
        current_password = word_list.pop()
        print(
            f"Current Key Checked [ {index / total * 100:.2f}% | {index} / {total} ]: \t{current_password}")
        password_status = await check_password(current_password)
        if password_status:
            PASSWORD_FOUND = True
            print(f"\n\n#####\tPASSWORD FOUND!:\t {current_password}\t#####")

def async_runner():
    # Run the async main function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

if __name__ == "__main__":
    # create multiple threads to make this program run faster
    NUM_THREADS = 3
    thread_list = []
    
    for num in range(NUM_THREADS + 1):
        thread = threading.Thread(target=async_runner)
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

# # display decrypted file contents
# try:
#     with open(f"{PATH}{output_file_name}", "r") as decrypted_file:
#         print(decrypted_file.read())
# except FileNotFoundError:
#     print(f"File not found, please encrypt or move file into directory:\n\t{PATH}")
