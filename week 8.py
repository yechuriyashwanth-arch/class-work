#1st question
n=int(input("Enter a number :"))
total=0
for i in range(1,n+1):
    total+=i
print("sum of first",n,"natural numbers is :",total)
#2nd question
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="")
    print()