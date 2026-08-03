import os

os.system("cls")

from collections import deque


def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        next_states = [
            (cap1, y),  # Fill Jug 1
            (x, cap2),  # Fill Jug 2
            (0, y),  # Empty Jug 1
            (x, 0),  # Empty Jug 2
            (max(0, x - (cap2 - y)), min(cap2, y + x)),  # Pour Jug1 -> Jug2i
            (min(cap1, x + y), max(0, y - (cap1 - x))),  # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution exists.")


jug1 = int(input("Maximum capacity of Jug 1: "))
jug2 = int(input("Maximum capacity of Jug 2: "))
goal = int(input("Enter goal: "))
water_jug(jug1, jug2, goal)
