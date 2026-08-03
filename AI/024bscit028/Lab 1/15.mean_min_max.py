import os

os.system("cls")

ages = [18, 20, 19, 21, 22, 18, 20, 23, 21, 19]
mean = sum(ages) / len(ages)
minimum = min(ages)
maximum = max(ages)
no_above_mean = sum(1 for x in ages if x > mean)

print(f"Mean ={mean}")
print(f"Minimum ={minimum}")
print(f"Maximum ={maximum}")
print(f"Ages above mean = {no_above_mean}")
