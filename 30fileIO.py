# to open a file 
# syntax open('filename','mode') # mode'r','w','a'
# f=open('myfile.txt','r')#r mode is default so no need to mention
# f1=open("myfile2.txt",'w') # this will create a new file 

# print(f)
# text=f.read()# to read the file
# print(text)
# f.close()


# appending and writing a file  
# f2=open('myfile.txt','a') # 'a' mode will keep adding  the cotent as many time you run it 
# f2=open('myfile.txt','w') # while 'w' mode add the contence once only
# f2.write("hello world!!")

# f2.close() # we should close the file at last
# alternative of close() is 'with '
# now we donot need to manually close the file with keyword will do it automatically 

with open('myfile.txt','a') as f2:
    f2.write("hey i am inside with")