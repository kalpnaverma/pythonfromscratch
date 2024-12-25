
# python allows else block to be executed with for and whipe loop it will prrint after the for block
for i in range(6):# this will print

    print(i)
else:
    print("sorry no i") # this will also print


for i in []:
    print(i)
else:
    print("no i")  # in this case only else will print no for block  

for i in range(6):# this will print

    print(i)
    if i==4:
        break  # loop will break after printing 0-4 else block will not displayed
else:
    print("sorry no i")
