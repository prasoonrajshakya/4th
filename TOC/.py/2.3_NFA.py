import os

os.system("cls")

alphabet = {"0", "1"}

# Transition table
transition = {
    "q0": {"0": {"q0", "q1"}, "1": {"q0"}},
    "q1": {"0": {"q2"}},
    "q2": {"1": {"q3"}},
    "q3": {"1": {"qf"}},
    "qf": {"0": {"q0", "q1", "qf"}, "1": {"q0", "qf"}},
}

s = input("Enter a string sequence: ")

states = {"q0"}

for ch in s:
    if ch not in alphabet:
        print("Invalid input")
        break

    next_states = set()

    for state in states:
        next_states.update(transition[state].get(ch, set()))

    states = next_states

    print(f"Input: {ch}, Current States: {states}")

else:
    if "qf" in states:
        print("Accepted")
    else:
        print("Rejected")
