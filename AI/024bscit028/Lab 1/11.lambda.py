import os

os.system("cls")  # Windows

square = lambda x: x * x
greater = lambda x, y: x > y

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"The square of {x} is {square(x)}")

if greater(x, y):
    print(f"{x} is the greater number")
else:
    print(f"{y} is the greater number")