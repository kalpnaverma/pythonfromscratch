class person:
    name="kalpna"
    occupation="student"
    roll_no=34

    # making function inside class
    def info(self): #
     print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
b.name="ritika"
b.occupation="teacher" 
print(b.name)


a.name="sona" #allowed
a.occupation="fresher" #allowed
print(a.name,a.occupation,a.roll_no)   
# a.info()
# b.info()





