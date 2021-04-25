from urllib.request import urlopen,Request
from colorama import Fore, init
import os
from pyfiglet import figlet_format
import ctypes
import re

init(convert=True)

ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker")
art = figlet_format('GD Username Checker')
print(art)
author = figlet_format('by RandomB#6160')
print(author)
invalid = 0
valid = 0
clear = lambda: os.system('cls')
print("Please type the name of the .txt file with the names: ")
nam = str(input(''))
name = nam.replace('.txt', '')
file1 = open(name + '.txt', 'r')
Lines = file1.readlines()
clear()
for line in Lines:
    playername = line.replace('\n', '')
    url = "http://www.boomlings.com/database/getGJUsers20.php"
    p = f"gameVersion=21&binaryVersion=35&gdw=0&str={playername}&total=0&page=0&secret=Wmfd2893gb7"
    p = p.encode()
    data = urlopen(url,p).read().decode()#
    if data == "-1":
        if re.match("^[A-Za-z0-9_-]*$", playername):
            valid += 1
            print(f"{Fore.GREEN}[+] {playername}")
            ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")
            k = open('valid.txt', 'w')
            k.write(f"{playername}\n")
            k.close()
        else:
            invalid += 1
            print(f"{Fore.RED}[-] {playername} (ILLEGAL CHARACTER)")
            ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")

    else:
        invalid += 1
        print(f"{Fore.RED}[-] {playername}")
        ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")
print(f"\n\n{Fore.RESET}Thanks for using my program. \nAll valid codes have been saved to valid.txt. \nSee you later. :)")
input("")
