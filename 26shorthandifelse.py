a=330
b=334
print("A") if a>b else print("=") if a==b else print("B")

print(9) if a<b else "" #it will print nothing to else statement  only if block will be executed if condition matched
c=9 if a>b else 0   # if condition matched if will execute otherwise 0 will print

print(c)

# shorthandifelse is not recommendable for complex situation
