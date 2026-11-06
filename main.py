
roll_no = input("Enter Roll Number: ")
name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter Subject {i+1} Marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if min(marks) < 35:
    grade = "Fail"
elif average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Pass"

print("\n===== STUDENT RESULT =====")
print("Roll Number:", roll_no)
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Grade:", grade)
