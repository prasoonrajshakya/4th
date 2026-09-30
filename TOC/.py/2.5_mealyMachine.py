import os

os.system("cls")

state = "q0"

string = input("Enter binary nubmer: ")

if all(bit == '1' for bit in string):
    print(1,end="")

for symbol in reversed(string): 
    match state:
        case "q0":
            match symbol:
                case "0":
                    print(1, end="")
                    state = "q1"
                case "1":
                    print(0, end="")
                    state = "q2"
        case "q1":
            match symbol:
                case "0":
                    print(1, end="")
                    state = "q1"
                case "1":
                    print(1, end="")
                    state = "q1"
        case "q2":
            match symbol:
                case "0":
                    print(1, end="")
                    state = "q1"
                case "1":
                    print(0, end="")
                    state = "q2"
