def move_zeros(arr):
    for num in arr:
        if num==0:
            arr.remove(0)
            arr.append(0)
    return arr 

print("here you go move zeros list")
arr=[1,2,3,67,89,0,3,4,78,4,9,0,0,]     
arr.sort()
result=move_zeros(arr)
print(result)
