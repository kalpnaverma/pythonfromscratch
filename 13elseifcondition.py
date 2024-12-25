# elseifcondition code 
number=int(input("enter your number"))
print(f"your number is {number}")

# condition operators
# >,<,>=,<=,==,!=

if (number < 0):
    print("number is negative")
elif (number == 0):
    print("number is zero") 
elif (number == 999):
    print("this is a special number")       
else:
    print("number is positive number")    