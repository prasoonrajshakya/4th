import os
os.system("cls")

def length(str):
    i = 0
    for ch in str:
        i += 1
    return i


s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
i = 0

if s1 == s2:
    print("improper prefix")
elif length(s2) > length(s1):
    print("not a prefix")
else:
    prefix = True
    for i in range(length(s2)):
        if s1[i] != s2[i]:
            prefix = False
            break
    if prefix:
        print("Proper Prefix")
    else:
        print("Not a Prefix")
