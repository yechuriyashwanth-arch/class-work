n=int(input("Enter a number"))
i=fact=1
while(i<=n):
    fact*=i
    i+=1
    print("Factorial of",n,"is",fact)
#4th question
start=int(input("Enter start number :"))
end=int(input("Enter end number :"))
for i in range (start,end+1):
    print(i)