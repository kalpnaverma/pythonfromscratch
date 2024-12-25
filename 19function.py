# # functions in python 
# # without using functions
# a=4
# b=5
# geometrical_mean=(a*b)/(a+b)
# # print(geometrical_mean)

# # with using functions
# def gmean(a,b):
#     return (a*b)/(a+b)
# print(gmean(8,7))


# # if you want to initialise function but dont give body use pass keyword to avoid errors you can move to some other function by  doning this 
# def num(a,c):
#     pass
# # functions operations
# def default(a=4,b=2):#called default parameters
#     return a*b
# print(default())
# print(default(a=6,b=3))# will take this updated value not previous one
# print(default(a=5))    #will take a=5 and b=2


def average(*numbers):#for integer
    sum = 0
    for i in numbers:
     sum = sum+i
        
    print(sum/len(numbers))
average(5,6)     


def listfunc(**name):
   print("hello",name["fname"],name["mname"],name["lname"])
   name(fname="kalpna",lname="verma")

   
