import os

os.system("cls")

state = "q0"
count = 0

string = input("Enter the input string: ")

for symbol in string:
    match state:
        case "q0":
            match symbol:
                case "a":
                    state = "q1"
                case "b":
                    state = "q0"

        case "q1":
            match symbol:
                case "a":
                    state = "q2"
                case "b":
                    state = "q0"

        case "q2":
            match symbol:
                case "a":
                    state = "q2"
                case "b":
                    state = "q3"

        case "q3":
            count += 1
            match symbol:
                case "a":
                    state = "q1"
                case "b":
                    state = "q0"

if state == "q3":
    count += 1

print("Occurrences of 'aab' =", count)
