# match case statements 
# x=3
# x=int(input("enter the number to match with x "))
# match x:
#     case 0:
#         print("x is zero incorrect")
#     case 1:
#         print("x is 1 incorrect")
#     case 2:
#         print("x is 2 incorrect") 
#     case 3:
#         print(" woah!!! you are correct  x is 3")    
#     case _ if x!=90:
#         print("x is not 90")
#     case _ if x==80:
#         print("x is 80")    
#     case _ :   
#         print("this is a default case") 
day=int(input("enter one  number (1-7)"))
day =3
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wedneday")        
    case 4:
        print("thursday")        
    case 5:
        print("friday")        
    case 6:
        print("saturday") 
    case 7:
        print("sunday ") 
    case _:
        print("you entered invalid number") 
print("thank you for your participation")                 
                 