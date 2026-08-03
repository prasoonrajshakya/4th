import os

os.system("cls")  # Windows

fact=1
n=int(input("Enter number to find factorial of: "))
for i in range(1,n+1):
  fact=fact*i
print(f"Factorial of {n} is {fact}")
