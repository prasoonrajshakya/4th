# TOC Lab: Turing Machine (TM) for L = { a^n b^n c^n | n >= 1 } over {a, b, c}
import os

os.system("cls")


def turing_machine(string: str) -> bool:
    tape = list(string)
    head = 0

    # n >= 1: empty input is rejected; alphabet is {a, b, c} only
    if not tape or any(ch not in "abc" for ch in tape):
        return False

    print(f"Input : {string}")
    print(f"Start : {''.join(tape)}")
    pass_no = 0

    while True:
        # Scan back to the left end, past already-crossed a's
        head = 0
        while head < len(tape) and tape[head] == "X":
            head += 1

        # No unmarked 'a' remains -> leave the loop and check the rest
        if head == len(tape) or tape[head] != "a":
            break

        # Cross out one 'a'
        tape[head] = "X"

        # Sweep right for the first unmarked 'b' (skip a's, X's, Y's)
        head += 1
        while head < len(tape) and tape[head] in ("a", "X", "Y"):
            head += 1
        if head >= len(tape) or tape[head] != "b":
            return False
        tape[head] = "Y"            # cross out one 'b'

        # Sweep right for the first unmarked 'c' (skip b's, Y's, Z's)
        head += 1
        while head < len(tape) and tape[head] in ("b", "Y", "Z"):
            head += 1
        if head >= len(tape) or tape[head] != "c":
            return False
        tape[head] = "Z"            # cross out one 'c'

        pass_no += 1
        print(f"Pass {pass_no}: {''.join(tape)}")

    # Any raw a/b/c left behind means counts (or a*b*c* order) were unequal
    if any(ch in "abc" for ch in tape):
        return False
    return True


string = input("Enter a string over {a, b, c}: ")

if turing_machine(string):
    print("\nAccepted")
else:
    print("\nRejected")
