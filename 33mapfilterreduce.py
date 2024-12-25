# map,filter,reduce functions are build in function in python
cube=lambda x: x*x*x
l=[1,2,3,4,5]
new1=list(map(cube,l))# in this case need to make separate lambda function
new1=list(map(lambda x: x*x*x,l)) # for this no need to make above lamda function

print(new1)


# filter
fil=lambda x :x>2
new2=list(filter(fil,l))
print(new2)

# reduce
# unlike other two function we need to import reduce function
from functools import reduce
numbers=[1,2,3,4,5,6,7]
new3=reduce(lambda x,y : x + y,numbers)
print(new3)

