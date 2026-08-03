import os

os.system("cls")  # Windows

students = {}

for i in range(5):
    print(f"Details of student {i+1}")
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))

    students[i + 1] = {
        "name": name,
        "grade": grade,
    }

highest = 1
lowest = 1
avg = 0

for student_id, info in students.items():
    if info["grade"] > students[highest]["grade"]:
        highest = student_id

    if info["grade"] < students[lowest]["grade"]:
        lowest = student_id

    avg += info["grade"]

print("Maximum Scorer:")
print(students[highest])

print("Minimum Scorer:")
print(students[lowest])

print("Average marks =", avg / 5)
