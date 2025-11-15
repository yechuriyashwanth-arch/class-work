#1st question
#function without parameter and without return type
# def add():
#     n1=int(input("Enter first number :"))
#     n2=int(input("Enter second number :"))
#     print("Sum :",n1+n2)
#     add()
# #function with parameters and with out return types
# def add(a,b):
#     n1=int(input("Enter first number :"))
#     n2=int(input("Enter second number :"))
#     add(n1,n2)
# #function without parameter and with return type
# def add():
#     n1=int(input("Enter first number :"))
#     n2=int(input("Enter second number :"))
#     return n1+n2
# print("Sum :",add())
# #function with parameter and with return type
# def add(a,b):
#     return a+b
# n1=int(input("Enter first number :"))
# n2=int(input("Enter second number :"))
# print("Sum :",add(n1,n2))

#2nd question
#function with different argument types
# def show_details(name,age=18,*subjects,**marks):
#     print("Name :",name)
#     print("Age :",age)
#     print("Subjects :",subjects)
#     print("Marks :",marks)
#     #1.positional argument
#     show_details("Alice",20)
#     #2.keyword arguments
#     show_details (name="Bob",age=22)
#     #3.default argument(uses default age=18)
#     show_details("charlie")
#     #4.variable length argument (*args and *kwargs)
#     show_details("David",21,"Math","Science",Math=90,science=85)

    #3rd question
    #global variable
x=10
def local_example():
    y=5 #Local variable
    print("Inside function-Local y :",y)
    print("Inside function-Global x :",x)
def modify_global():
    global x
    x=20 #Modify global variable
    print("Global x changed to :",x)
#function calls
local_example()
print("Outside function-Global x :",x)
#modify_global()
print("After modification-Global x :",x)