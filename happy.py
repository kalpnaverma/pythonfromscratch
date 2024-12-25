# number=int(input("enter a number"))

# def calculate_sqr(num):
#     return sum(int(digit)**2 for digit in str(num))


# def ishappy(n):
#     seen=set()
#     while(n!=0) and n not in seen:
#         seen.add(n)
#         n=calculate_sqr(n)

#         if (n==1):
#              return True
    

# if ishappy(number):
#         print(f"{number } is a happy number")
# else:
#      print(f"{number} is not a happy number")  













def is_power(n):
    if(n<=0):
        return False
    
    return(n & (n-1))== 0


number=int(input("enter a number"))
if is_power(number):
    print(f"{number} is power of two")
else:
    print(f"{number} is not a power of two")    


