# 13. Write a Python program using the filter () function to extract all even numbers from a given list.
import os

os.system("cls")

numbers = [11, 22, 33, 44, 55]
result = filter(lambda x: x % 2 == 0, numbers)
print(f"Extracted even numbers: {list(result)}")
