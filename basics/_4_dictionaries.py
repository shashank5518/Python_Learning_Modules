student = {"name": "corey", "age": 25, "courses": ["math", "compsci"]}
print(student)

print(student["name"])
print(student["courses"])
print(student["courses"][0])
print(student["courses"][1])

# print(student["phone"]) # key error
print(student.get("name"))
print(student.get("phone"))  # returns none instead of key error
print(student.get("phone", "not found"))  # returns default value if not found

student["phone"] = "999-8888"
print(student.get("phone"))

student["name"] = "shashank"
print(student.get("name"))

student.update({"name": "jane", "age": 26, "phone_2": "555-5555"})
print(student)

del student["phone_2"]
print(student)

age = student.pop("age")
print(student)
print(age)

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} corresponds to {value} in the dictionary 'student'")
