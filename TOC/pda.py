# TOC Lab: PDA (Pushdown Automaton) for L = { a^n b^n | n >= 0 } over {a, b}
# Accepts strings with the same number of a's followed by the same number of b's
import os

os.system("cls")

Z0 = "$"  # bottom-of-stack marker (initial stack content)
A = "A"  # one marker pushed for every 'a' read


def pda(string: str) -> bool:
    stack = [Z0]  # start with only the bottom marker on the stack
    state = "q0"

    print(f"{'Symbol':<8}{'State':<8}Stack (top -> bottom)")
    print(f"{'-':<8}{'q0':<8}{''.join(reversed(stack))}")

    for ch in string:
        top = stack[-1]

        if state == "q0":
            if ch == "a":
                stack.append(A)
            elif ch == "b":
                if top != A:
                    return False
                stack.pop()
                state = "q1"
            else:
                print(f"Invalid symbol: {ch!r}")
                return False

        elif state == "q1":
            if ch == "b":
                if top != A:
                    return False
                stack.pop()
            else:
                return False

        print(f"{ch:<8}{state:<8}{''.join(reversed(stack))}")

    # Accept by empty stack: every pushed 'A' matched, only Z0 remains
    return len(stack) == 1 and stack[0] == Z0


s = input("Enter a string over {a, b}: ")

if pda(s):
    print("\nAccepted")
else:
    print("\nRejected")
