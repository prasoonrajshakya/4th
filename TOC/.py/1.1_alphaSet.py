import os
os.system("cls")

symbol_set = input("Enter symbol set: ")
string = input("Enter string: ")

for ch in string:
    found = False
    for sym in symbol_set:
        if ch == sym:
            found = True
            break
    if not found:
        print("Invalid String")
        exit()
print("Valid String")