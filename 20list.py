l=[1,3,"name",23,"sona"]
print(l,type(l))
if "sonaVERMA" not in l:# to check something not present 
# if "sonaVERMA"  in l:# to check something is present 

    print("not present ")
else:
    print("present")  
# lst=[i for i in range(5)]# creating list using for loop
# lst1=[i*i for i in range(5)]# creating list using for loop
# print(lst)      
# print(lst1)
lst2=[2*i for i in range(11)if i%2==0  ] 
print(lst2)
