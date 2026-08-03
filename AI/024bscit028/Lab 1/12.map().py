#12. Write a Python program using the map () function to create a new list containing squares of all elements in a given list.
import os
os.system("cls")

numbers = [1,2,3,4,5]
result = map(lambda x: x * x, numbers)
print(f"Original list = {numbers}")
print(f"Squared numbers = {list(result)}")