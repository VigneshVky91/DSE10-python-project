print("Please Input student details...")

studentId = input("Enter Student ID:")
studentName = input("Enter Student Name:")
age = int(input("Enter Student age:"))
location = input("Enter Student location:")
degree = input("Enter Student degree:")
cgpa = float(input("Enter the CGPA of the student:"))

print("Student id: "+studentId)
print("Student Name: "+studentName)
print(f"Student age: {age+1}")
print("Location: "+location)
print("Degree: "+degree)
print(f"CGPA: {cgpa}")