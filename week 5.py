#1st question
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print('1.addition')
print('2.subraction')
print('3.multiplication')
print('4.division')
print('5.floor division')
print('6.remainder')
print('7.power')
ch=int(input("enter choice:"))
if ch ==1:
    print("addition:",n1+n2)
elif ch==2:
    print("subraction:",n1-n2)
elif ch==3:
    print("multiplication:",n1*n2)
elif ch==4:
    print("division:",n1/n2)
elif ch==5:
    print("floor division:",n1//n2)
elif ch==6:
    print("remainder:",n1%n2)
elif ch==7:
    print("power:",n1**n2)
#2nd question
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>=b and b>=c:
    print("Largest number is ",a)
elif b>=a and b>=c:
    print("largest number is",b)
else:
    print("Largest number is",c)
#3rd question
my_list=[10,20,30,40,50]
element=int(input("Enter element to check :"))
if element in my_list:
    print(element,"exists in the list")
else:
    print(element,"does not exist in the list")