set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
#3rd question
student={"name":"Alice","age":20,"Course":"Math"}
print(student["name"])
print(student.get("age"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"age":21})
print(student)
student.pop("Course")
print(student)