#1st question
import array
arr1=array.array('i'[1,2,3,4,5])
print('Elements of array are :')
for i in arr1:
    print(i,end='')
    #methods of array module
    arr1.append(6)
    arr1.append(2)
    print('Array elements after append operatoin :')
    for i in arr1:
        print(i,end='')
    print('No.of occurences of element 2:',arr1.count(2))
    print('Index of elements 5;',arr1.index(5))
    print('Element removed from array :',arr1.pop(3))
    print('Array element after remove operations :')
    for i in arr1:
        print(i,end='')
    arr1.reverse()
    print('Array elements after revere operation :')
    for i in arr1:
        print(i,end='')
#2nd quetion
import numpy as np
#create a numpy array
arr=np.array([10,20,30,40])
#perform simple operations
print("Array :",arr)
print("Sum :",np.sum(arr))
print("Mean :",np.mean(arr))
print("Maximum :",np.max(arr))
print("Array + 5 :",arr+5)#add 5 to each element
#outpuy not come in vs code because it does not have array copy code and paste in online compiler