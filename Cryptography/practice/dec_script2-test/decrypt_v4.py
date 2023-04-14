import subprocess
import threading
import datetime

##### If necessary, replace this with the path in which the "chand.txt.secret" file is located #####
PATH = subprocess.getoutput("pwd") + "/"
# PATH = subprocess.getoutput("pwd") + "/Cryptography/practice/dec_script2-test/"
##### ######################################################################################## #####

INPUT_FILE_NAME = "file.secret"
OUTPUT_FILE_NAME = "file.decrypted.txt"
LOG_FILE_NAME = f"decrypt_{datetime.datetime.now().strftime('%Y-%m-%d_%X')}.log"
PASSWORD_FOUND = False
### SET THE NUMBER OF THREADS BELOW AT BOTTOM OF PROGRAM ###

### Begin Program ###

with open(f"{PATH}word_list.txt", "r") as word_list_file:
    WORD_LIST = word_list_file.read().split("\n")

WRD_LST_TOTAL = len(WORD_LIST)
WRD_LST_INDEX = 0


def compare_output_file(file_path) -> bool:
    try:
        file_type = subprocess.getoutput(f"file {file_path}")
        if "ASCII text" in file_type:
            subprocess.getoutput(f"mv {file_path} {PATH}{OUTPUT_FILE_NAME}")
            return True
    except UnicodeDecodeError:
        error_msg = f"[ERROR] {datetime.datetime.now().strftime('%X')} : UnicodeDecodeError for file: {file_path}"
        with open(f"{PATH}{LOG_FILE_NAME}", 'a') as log_file:
            log_file.write(error_msg + "\n")
        print(error_msg)

    subprocess.getoutput(f"rm {file_path}")
    return False


def check_password(pass_in) -> bool:
    cmd_output = subprocess.getoutput(
        f"openssl enc -d -bf-ofb -nosalt -in {PATH}{INPUT_FILE_NAME} -out {PATH}{pass_in}.{OUTPUT_FILE_NAME} -k {pass_in}")
    # Check if decrypted properly
    return compare_output_file(f"{PATH}{pass_in}.{OUTPUT_FILE_NAME}")


def password_checker():
    global PASSWORD_FOUND, WRD_LST_INDEX, WRD_LST_TOTAL

    while len(WORD_LIST) > 0:
        if PASSWORD_FOUND:
            break

        WRD_LST_INDEX += 1

        try:
            current_password = WORD_LIST.pop()
        except IndexError:
            # Note: Thread Is Done, list is empty
            break

        key_check_msg = f"[INFO] {datetime.datetime.now().strftime('%X')} : Current Key Checked [ {WRD_LST_INDEX / WRD_LST_TOTAL * 100:.2f}% | {WRD_LST_INDEX} / {WRD_LST_TOTAL} ]: \t{current_password}"
        with open(f"{PATH}{LOG_FILE_NAME}", 'a') as log_file:
            log_file.write(key_check_msg + "\n")
        print(key_check_msg)

        password_status = check_password(current_password)
        if password_status:
            PASSWORD_FOUND = True

            success_msg = f"\n[SUCCESS!] {datetime.datetime.now().strftime('%X')} \n\nPASSWORD FOUND!: {current_password}"
            with open(f"{PATH}{LOG_FILE_NAME}", 'a') as log_file:
                log_file.write(success_msg + "\n")
            print(success_msg)


if __name__ == "__main__":
    # create multiple threads to make this program run faster
    # Set the number of threads to execute the program here
    NUM_THREADS = 3

    thread_list = []

    for num in range(NUM_THREADS):
        thread = threading.Thread(target=password_checker)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()
