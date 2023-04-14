import asyncio
import subprocess

START_NUM = 1
END_NUM = 100

async def print_nums(in_number):
    print(in_number)
    await asyncio.sleep(0.1)

async def echo_number(in_number):
    return subprocess.getoutput(f"echo 'echoed: {in_number}'")

async def main():
    CURRENT_NUM = START_NUM
    for number in range(CURRENT_NUM, END_NUM):
        cmd_output = await echo_number(number)
        print(cmd_output)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
