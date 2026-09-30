import os

os.system("cls")


def length(str):
    i = 0
    for ch in str:
        i += 1
    return i


s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

if s1 == s2:
    print("improper suffix")
elif length(s2) > length(s1):
    print("Not a suffix")
else:
    suffix = True
    for i in range(1, length(s2)+1):
        if s1[- i] != s2[-i]:
            suffix = False
            break
    if suffix:
        print("Proper Suffix")
    else:
        print("Not a Suffix")
