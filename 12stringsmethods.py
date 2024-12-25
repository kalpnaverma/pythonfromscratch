# strings are immutable (cannot changed)
# it doesnot change existing string instead it will create a new string
# for exapmple
a= "kalpna"

print(a.upper())#here it orint create a new sring in uppercase 
                # but it didnot change the existing string so strings are immutable 
print(a.lower())
surname="verma!!!!!"                            
# rstrip() method is used to strip (remove trailing characcter(char that come after the end of string ) like ! here)
print(surname.rstrip("!"))# output KALPNAverma 
surname2="!!!kabirpanth!!!"
print(surname2.rstrip("!")) #output !!!kabirpanth itbonly remove character after end of strings 

# replace method it replaces all  the ouucrence of particular string 
str="""her name is kalpna 
kalpna's fav color is black 
kalpna name sounds boring for herself"""
print(str.replace("kalpna","sona "))# it will replace all kalpna with sona
fullname="kalpna verma is my name" 
print(fullname.capitalize())  # convert the first character of string in uppercase
print(len(fullname))
print(len(fullname.center(46)))
print("kalpna count is ",str.count("kalpna"))
print(fullname.split(" "))#create the  list of strings 
print(fullname.endswith("!!!"))#returns boolean value True if string ends with !!! otherwise false
print(fullname.startswith("kal"))
print(str.find("kalpna")) #it returns the first occurence index of kalpna  
print(str.find("sona"))# will return -1 as substring is not available not raised  an error
# print(str.index("sona"))#this will raise an error instead of an output
print(str.isalnum())#if string contains  A-Z,a-z,or 0-9 called isalnum it returns boolean value
print(str.isalpha())# strings contains A-Z or a-z return boolean
str2="we wish you merry christmas\n" 
print(str2.isprintable())# returns true if string is printable hence \n is not printable here so it will be returning false here in this case
str3=" "
print(str3.isspace())#returns true if whitespace are there is string it is true with both spacebar  and tab key
str4="Hello We Are Happy"
print(str4.istitle())#this method return true is first letter of the word is capitalize
print(str4.swapcase())#it swaps the letter
str5="i am a girl"
print(str5.title())#it converts the first character into capital letter