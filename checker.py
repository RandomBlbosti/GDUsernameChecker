from colorama import Fore, init
import os
from pyfiglet import figlet_format
import ctypes
import re
import requests
init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("GD Username Checker")
art = figlet_format('GD Username Checker')
author = figlet_format('by RandomB#6160')
print(art, author)
invalid = 0
valid = 0
clear = lambda: os.system('cls')
name = str(input("Please type the name of the .txt file with the names: ")).replace(".txt", "")
savename = str(input("Please type the name of the .txt file to save the valid names: ")).replace(".txt", "")
turnon = str(input("Print usernames into the console? (Y/N)\n")).upper()
file1 = open(name + '.txt', 'r')
Lines = file1.readlines()
clear()
for line in Lines:
    numbered = False
    playername = line.replace('\n', '')
    if playername.isnumeric() and not playername.endswith(" "):
        numbered = True
        playername += " "
    url = "http://www.boomlings.com/database/getGJUsers20.php"
    p = f"gameVersion=21&binaryVersion=35&gdw=0&str={playername}&total=0&page=0&secret=Wmfd2893gb7"
    p = p.encode()
    headers = {
        "Host": "www.boomlings.com",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": ""
    }
    data = requests.post(url, p, headers=headers).text
    if data == "-1":
        if re.match("^[A-Za-z0-9_-]*$", playername) or numbered:
            valid += 1
            if turnon == "Y":
                print(f"{Fore.GREEN}[+] {playername}")
            ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")
            k = open(f'{savename}.txt', 'a')
            k.write(f"{playername}\n")
            k.close()
        else:
            invalid += 1
            if turnon == "Y":
                print(f"{Fore.RED}[-] {playername} (ILLEGAL CHARACTER)")
            ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")
    else:
        invalid += 1
        if turnon == "Y":
            print(f"{Fore.RED}[-] {playername}")
        ctypes.windll.kernel32.SetConsoleTitleW(f"GD Username Checker | Valid: {valid} | Invalid: {invalid}")
input(f"\n\n{Fore.RESET}Thanks for using my program. \nAll valid codes have been saved to {savename}.txt. \nSee you later. :)\n")
