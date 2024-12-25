'''we use input()function to take input from user'''
# #by default is takes string value so to get output in integers we have to typecast it 
name=input("enter your name ")
print(f"your name is {name}")


# for integer output
number1=int(input("enter you number1:"))
number2=int(input("enter you number2:"))


print("sum of ",number1,"and",number2 ," is :", number1+number2) 


# another way:
num1=input("enter a number")
num2=input("enter another number")
print(int(num1)+int(num2))# for integer output
print(float(num1)+float(num2))# for float output

