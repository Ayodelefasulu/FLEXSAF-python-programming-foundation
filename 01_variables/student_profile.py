student = {
    "name": "john",
    "age": 24,
    "department": "Computer Science",
    "scores": [72, 81, 65, 90, 55]
}

print(f"Student:", student["name"].capitalize())
print(f"Department:", student["department"])
print(f"Number of courses:", len(student["scores"]))
print(f"Total score:", sum(student["scores"]))

avg = sum(student["scores"]) / len(student["scores"])

print(f"Average score:", avg)