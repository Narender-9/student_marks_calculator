
roll_no = input("Enter Roll Number: ")
name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter Subject {i+1} Marks: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
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
    grade = "D"
print("\n===== STUDENT RESULT =====")
print("Student Report Generated Successfully")
print("------------------------------")
print("        STUDENT PROFILE")
print("------------------------------")
print("Roll Number:", roll_no)
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Grade:", grade)