# string slicing syntax-[0:2]
# indexing alwayas starts with 0

name="kalpna-verma"
print(name[0:4]) # output-kalp :it prints  characters from 0-3 index
print(name[:4])  # same output as above as by default it starts with 0
print(name[1:3]) # will starts with one and goes to index 2 
print(name[:])#output->kalpna-verma: will return the full length of name 

# "negative slicing"
fruit="mango"
print(fruit[0:-3])# python interpreter will read it as 
                  # print(fruit[0:len(fruit)-3])
                  # total len of mango is 5 so 5-3=2 means 
                  # print (fruit[0:2])this is now negative slicing works

print(fruit[-3:-1])# it will do len(fruit-3)means(5-3)=2
                   # and (5-1)=4 so it will slice from [2:4]    
                    


# 2:len() function:it starts with 1
# print(len(name))# it also cout spaces i,it resturn the length
# len1=len(name)
# print(f"kalpna-verma is {len1} character name ")


Teacher="CodeWithHarry"
print(Teacher[-4:-2])#output-> ar 
print(Teacher[-1:-2])# no output -in this case it will print nothing
# note:last dighit must be smaller than 1 one 
