student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}

for key, value in student.items():
    print(f"{key}: {value}")

if "email" not in student:
    email = input("Enter email: ")
    student["email"] = email

while True:
    new_city = input("Enter new city: ").strip()
    if new_city != "":
        student["city"] = new_city
        break
    print("City cannot be empty.")

if student.get("phone") is None:
    print("Phone number not found.")

student["contact"] = {
    "phone": "13800001111",
    "email": student["email"]
}

student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

total = 0
count = 0
for score in student["courses"].values():
    total = total + score
    count = count + 1
average = total / count

if average >= 90:
    student["academic_status"] = "Excellent"
elif average >= 75:
    student["academic_status"] = "Good"
elif average >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

search_course = input("Enter course to search: ").strip()
if search_course in student["courses"]:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found.")

update_course = input("Enter course name to update: ").strip()
if update_course in student["courses"]:
    new_score = input("Enter new score: ").strip()
    if new_score.isdigit():
        new_score = int(new_score)
        if 0 <= new_score <= 100:
            student["courses"][update_course] = new_score
            print(f"{update_course} score updated to {new_score}.")
        else:
            print("Score must be between 0 and 100.")
    else:
        print("Score must be a number.")

total = 0
count = 0
for score in student["courses"].values():
    total = total + score
    count = count + 1
average = total / count

if average >= 90:
    student["academic_status"] = "Excellent"
elif average >= 75:
    student["academic_status"] = "Good"
elif average >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print("")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print("")
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print("")
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score}")
print("")
print(f"Average Score: {average:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("")
print("=====================================")