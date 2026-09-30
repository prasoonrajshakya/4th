import os
os.system("cls")

import re

def identify(str):
    pattern=r"^[ab]*aa[ab]*$"

    return re.fullmatch(pattern,str)

str=input("Enter a string to test: ")
if identify(str):
    print("Accepted")
else:
    print("Rejected")