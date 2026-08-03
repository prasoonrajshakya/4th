import os

os.system("cls")  # Windows
print("Prime numbers between 1 and 100")
for i in range(1,101):
  flag=False
  for j in range(2,i):
    if i%j==0:
      flag = True
      break
  if not flag:
    print(i, end=" ")
