"""Static implementation of Banker's Algorithm for deadlock avoidance."""

import os

os.system("cls")

# allocation[i][j] = instances of resource j currently held by process i
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

# maximum[i][j] = maximum instances of resource j process i may request
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]

# available[j] = currently available instances of resource j
available = [0, 0, 0]


def bankers_algorithm(allocation, maximum, available):
    process_count = len(allocation)
    resource_count = len(available)

    # Need = Maximum - Allocation
    need = [
        [maximum[i][j] - allocation[i][j] for j in range(resource_count)]
        for i in range(process_count)
    ]

    work = available.copy()
    finished = [False] * process_count
    safe_sequence = []

    while len(safe_sequence) < process_count:
        found_process = False

        for i in range(process_count):
            if not finished[i] and all(
                need[i][j] <= work[j] for j in range(resource_count)
            ):
                # Process i can finish and release its allocated resources.
                for j in range(resource_count):
                    work[j] += allocation[i][j]

                finished[i] = True
                safe_sequence.append(f"P{i}")
                found_process = True

        if not found_process:
            return False, []

    return True, safe_sequence


is_safe, sequence = bankers_algorithm(allocation, maximum, available)

if is_safe:
    print("System is in a safe state.")
    print("Safe sequence:", " -> ".join(sequence))
else:
    print("System is not in a safe state.")
