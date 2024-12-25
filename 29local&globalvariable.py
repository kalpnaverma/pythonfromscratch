# introduction of local and global variable
x=4
print(x)#4
def hell():
   x=5
   print(f"the local x is {x}")#5
   print("hello harry")
print(f"the global x is {x}") #4  
hell()

print(f"the global x is {x}")#4
