import os

os.system("cls")

import re

gmail_pattern = r"^[a-z0-9](\.?[a-z0-9]){5,29}@g(oogle)?mail\.com$"

email = input("Enter a mail: ")

email = email.strip().lower()

if re.fullmatch(gmail_pattern, email):
    print("valid gmail address")
else:
    print("invalid gmail address")
