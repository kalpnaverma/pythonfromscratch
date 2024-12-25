# program to create a simple calculator

a=3
b=4
print("the value of ",a,"+",b,"is:",a + b)
print("the value of ",a,"-",b,"is:",a - b)
print("the value of ",a,"*",b,"is:",a * b)
print("the value of ",a,"/",b,"is:",a / b)


# by taking user input
operator=input("enter operator(+,-,*,/)")

num1=int(input("enter first number"))
num2=int(input("enter 2nd number"))
if operator=="+":
  print("sum of ",{num1},"+",num2,"is:",num1 + num2)
elif operator=="-":
  print("difference of ",num1,"-",num2,"is:",num1 - num2)
elif operator=="*":
  print("multiplication of ",num1,"*",num2,"is:",num1 * num2)
elif operator=="/":
  print("division of ",num1,"/",num2,"is:",num1 / num2)





