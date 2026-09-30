# TOC Lab: Turing Machine for L = { a^n b^n c^n | n >= 1 }

import os
os.system("cls")


def turing_machine(string):
    tape = list(string)
    head = 0

    # Initial checks
    if len(tape) == 0:
        return False

    for ch in tape:
        if ch not in "abc":
            return False

    # Initial state
    state = "q0"

    print("\nInput :", string)
    print("Tape  :", "".join(tape))

    while state != "q_accept" and state != "q_reject":

        # --------------------------------
        # q0: Find an unmarked 'a'
        # --------------------------------
        if state == "q0":

            if head >= len(tape):
                state = "q4"

            elif tape[head] == "X":
                head = head + 1

            elif tape[head] == "Y":
                # All a's are marked -> verify the rest of the tape
                state = "q4"

            elif tape[head] == "a":
                tape[head] = "X"
                head = head + 1
                state = "q1"

            else:
                state = "q_reject"


        # --------------------------------
        # q1: Find an unmarked 'b'
        # --------------------------------
        elif state == "q1":

            if head >= len(tape):
                state = "q_reject"

            elif tape[head] in ["a", "X", "Y"]:
                head = head + 1

            elif tape[head] == "b":
                tape[head] = "Y"
                head = head + 1
                state = "q2"

            else:
                state = "q_reject"


        # --------------------------------
        # q2: Find an unmarked 'c'
        # --------------------------------
        elif state == "q2":

            if head >= len(tape):
                state = "q_reject"

            elif tape[head] in ["b", "Y", "Z"]:
                head = head + 1

            elif tape[head] == "c":
                tape[head] = "Z"
                head = head - 1
                state = "q3"

            else:
                state = "q_reject"


        # --------------------------------
        # q3: Move left to the beginning
        # --------------------------------
        elif state == "q3":

            if head < 0:
                head = 0
                state = "q0"

            elif tape[head] in ["X", "Y", "Z", "a", "b", "c"]:
                head = head - 1


        # --------------------------------
        # q4: Check remaining tape
        # --------------------------------
        elif state == "q4":

            if head >= len(tape):
                state = "q_accept"

            elif tape[head] in ["X", "Y", "Z"]:
                head = head + 1

            else:
                state = "q_reject"


    # Display final tape
    print("Final :", "".join(tape))

    if state == "q_accept":
        return True
    else:
        return False


# Main program
string = input("Enter a string over {a, b, c}: ")

if turing_machine(string):
    print("\nAccepted")
else:
    print("\nRejected")