import os

os.system("cls")

import re

def validMAC(string: str) -> bool:
    pattern = r"^([0-9A-Fa-f]{2}[-:]){5}([0-9A-Fa-f]{2})$"

    return re.fullmatch(pattern, string)

mac = input("Enter MAC address to check: ")
if validMAC(mac):
    print("Valid MAC address")
else:
    print("Invalid MAC address")
