import os
from random import *
from sys import platform
from time import sleep

def main():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    else:
        print("What on earth operting system are you using?")

    for i in range(15):
        print("")

    print("Yellow, black. Yellow, black.")
    print("Yellow, black. Yellow, black.")
    print("Ooh, black and yellow!")
    print("Let's shake it up a little.")
    sleep(5)

    x = "Yellow,"
    y = " black."
    end = "Ooh, black and yellow!\nLet's shake it up a little."

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        for i in range(10):
            sleep(1)
            os.system('clear')
            for u in range(randint(1, 30)):
                print("")
            p = (" ") * (randint(1, 37))
            q = (" ") * (randint(1, 15))
            print(q + x + p + y)
        os.system('clear')
        for i in range(15):
            print("")
        print(end)
        sleep(10)
    elif platform == "win32":
        for i in range(10):
            sleep(1)
            os.system('cls')
            for u in range(randint(1, 30)):
                print("")
            p = (" ") * (randint(1, 37))
            q = (" ") * (randint(1, 15))
            print(q + x + p + y)
        os.system('cls')
        for i in range(15):
            print("")
        print(end)
        sleep(10)
    else:
        print("What on earth operating system are you using?")

main()