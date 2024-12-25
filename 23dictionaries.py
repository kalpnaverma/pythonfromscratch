# its a ordered collection of data items in key value pair it is enclosed by {}

dict={

    "name":"kalpna",
    "roll-no":40,
    "age":23, 
    "religion":"Hindu",
}
print(dict)
print(dict["name"])# this will give error if we tru to acces the element that is not present un the dictionar
print(dict.get("name"))# both are same but it give not give an error return none 
print(dict.keys())# this will print the keys
print(dict.values())
for key in dict.keys():
    print(dict[key])

# dictionaries methods
ep1={123:345,23:56,45:89}
ep2={12:34,56:80}
ep1.update(ep2) #it will update the ep1
# ep1.clear()# clear all the items of ep1 and print empty dictionary
ep1.pop(23)
print(ep1)





