student = {
    "name": "john",
    "age": 24,
    "department": "Computer Science",
    "scores": [72, 81, 65, 90, 55]
}

"""grading system"""
status = ""
score = int(input("Enter your score: " ))
if score == 0 or score <= 39:
    print("F")
    status = "Fail"
elif score == 40 or score <= 44:
    print("E")
    status = "Pass"
elif score == 45 or score <= 49:
    print("D")
    status = "Pass"
elif score == 50 or score <= 59:
    print("C")
    status = "Pass"
elif score == 60 or score <= 69:
    print("B")
    status = "Pass"
elif score == 70 or score <= 100:
    print("A")
    status = "Pass"
else:
    print("Score must be between 0 and 100.")
    raise SystemExit(1)