import os

os.system("cls")

alphabet = {"a", "b"}
s = input("Enter a string sequence: ")

state = "A"

for ch in s:
    if ch not in alphabet:
        state = "dead"
        break

    match state:
        case "A":
            state = "B" if ch == "a" else "E"

        case "B":
            if ch == "a":
                state = "C"
            else:
                state = "dead"
                break

        case "C":
            if ch == "a":
                state = "D"
            else:
                state = "dead"
                break

        case "D":
            state = "B" if ch == "a" else "E"

        case "E":
            if ch == "b":
                state = "F"
            else:
                state = "dead"
                break

        case "F":
            if ch == "b":
                state = "D"
            else:
                state = "dead"
                break

if state == "D":
    print("Valid")
else:
    print("Invalid")
