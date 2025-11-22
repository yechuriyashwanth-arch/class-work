#1st question
# add=lambda x,y : x+y
# print(add(5,4))

#2nd question
#filter_even.py
#import not needed for filter()
# nums=[1,2,3,4,5,6,7,8,9,10]
# even_nums=list(filter(lambda x:x % 2 ==0,nums))
# print("Original List :",nums)
# print("Even Numbers :",even_nums)

#3rd question
#map_double.py
# nums=[1,2,3,4,5]
# doubles=list(map(lambda x:x*2,nums))
# print("Original List :",nums)
# print("Doubled List :",doubles)

#4th question
#reduce_sum.py
# from functools import reduce #import reduce
# nums=[5,10,15,20]
# total=reduce(lambda a,b:a+b,nums)
# print("Numbers :",nums)
# print("Sum:",total)