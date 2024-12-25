
# tuple are immutable
tup=(2,3,"sona",True)# acceptable
print(type(tup))
# tup=(3)#it will act as in interger 
# tup=(3,)#now this will act as integer if single vale is there in tuple add comma at the end 
# tup[0]=20#this will throw an error as it is immutable
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
# print(tup[4])# out of range throw an error
if "sona1" in tup:
    print("yes")
else:
    print("false")  

tup7=tup[1:3] #slicing
print(tup7) 



# operations on tuple

countries=("India","Spain","Italy", "England","Germany")
print(countries)
temp=list(countries) #now country has coverted in list datatype
print(type(temp))# as tuple are immutable so we change it into list and perform operation after this we will back converted it to tuple 
temp.append("Russia") #add item
temp.pop(3) #remove item
temp[2]="Finland"
countries=tuple(temp) # back to tuple  data type with updation in countries
print(countries)

cont1=("America","Africa")
cont2=("Austrailia", "England")
cont3=cont1+cont2  # will concatenate the two tuple into one 
print(cont3)


tuple1=(1,2,2,3,4,3,5,3,"", 90)
tuple2=tuple1.count(2)
tuple2=tuple1.index(1) #this will return the index of item 1 here
tuple2=tuple1.index(3,1,8) # this will return the  index of first  occurence of 3 from index 4 to 8
tuple2=len(tuple1)
print(tuple2)





