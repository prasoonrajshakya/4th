import os

os.system("cls")

alphabet = {"0", "1"}
s = input("Enter a string sequence: ")

state = "A"

for ch in s:
    if ch not in alphabet:
        state = "Invalid"
        break

    match state:
        case "A":
            state = "B" if ch == "0" else "D"

        case "B":
            state = "C" if ch == "0" else "E"

        case "C":
            state = "A" if ch == "0" else "F"

        case "D":
            state = "E" if ch == "0" else "G"

        case "E":
            state = "F" if ch == "0" else "H"

        case "F":
            state = "D" if ch == "0" else "I"

        case "G":
            state = "H" if ch == "0" else "A"
       
        case "H":
            state = "I" if ch == "0" else "B"
       
        case "I":
            state = "G" if ch == "0" else "C"

if state in ('ABCDG'):
    print("Valid")
else:
    print("Invalid")
