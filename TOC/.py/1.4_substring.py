import os

os.system("cls")


def length(s):
    count = 0
    for ch in s:
        count += 1
    return count

s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

substring = False
if s1==s2:
    print("Improper Substring")
    exit()
for i in range(length(s1) - length(s2) + 1):
    match = True
    for j in range(length(s2)):
        if s1[i + j] != s2[j]:
            match = False
            break
    if match:
        substring = True
        break

if substring:
    print("Proper Substring")
else:
    print("Not a Substring")