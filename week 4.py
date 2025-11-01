#1st question
tup=(1,2,3,4,5,'a','bb','c','xyz',3,2)
print("Items in a tuple")
for i in tup:
    print(i,end="")
    print("\n Length of tuple ",len(tup))
    i=int(input("Enter a value"))
    print(i in tup)
    print('Occurrence of item 3;',tup.count(3))
    print("Index of item 'xyz'",tup.index('xyz'))
    #2nd question
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