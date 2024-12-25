# introduction of for loop in python
# for loop for string
name ="kalpnaverma"
for i in name:
    # print(i,end=",")#this will print all character in one line separated by comma
    print(i)#this will print each character in next line
    if(i=="k"):
        print("thi is first character of the name ") 


# # for loop  for list
# states=["uttar-pradesh","madhya-pradesh","Gujrat","maharashtra"]
# for i in range(len(states)):
#     if i==2:
#         print([i],states[i],"this is my native ")            
#     print([i],states[i])

colors=["Red","Yellow","Pink"]
for color in colors:
    print(color)
    for i in color:
        print(i)

 # range -function
for k in range(21):#output
    print(k+1)# will print from 1to 20
for j in range(20): 
    print(j)#prints 0-19  
for s in range(1,15)  :
    print(s)#"this will print from 1-14" 
for r in range(1,13) :
    print(r+1) #this will print 2-13 
for p in range(1,12,2) :# it will start from 1 take 2digit gap goes till 11
    print(p)    




