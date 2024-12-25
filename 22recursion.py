# when a function call itself insite a function is called recursion
# factorial is a good example to understand function

# factorial(5)=5*4*3*2*1
# factrorial(4)=4*3*2*1
# factorial(n)=n*factorial(n-1)


def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1)) #this is return as factorial function is calling itself
print(factorial(15))
print(factorial(2))
print(factorial(5))
print(factorial(7))
