
# Student Marks Calculator

name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3

percentage = (total / 300) * 100

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
