import os

os.system("cls")  # Windows

a=int(input("Enter marks:"))
if a>=80:
  print("Distinction")
elif a>=65:
  print("First Division")
elif a>=55:
  print("Second Division")
elif a>=40:
  print("Third Division")
else:
  print("Fail")
