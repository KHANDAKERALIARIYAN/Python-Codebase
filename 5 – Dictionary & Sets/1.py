student={
    "name":"Ariyan",
    "age":20,
    "marks":100,
}
print(student,type(student))
print(student["name"])
print(student.items())
print(student.keys())
print(student.values())
student.update({"name":"Ariyan Khan"})
print(student)

print(student.get("name")) # if it doesnot return then it will return None
print(student["name"]) # if it doesnot return then it will give error