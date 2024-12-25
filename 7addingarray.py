# first way of adding 2 array
a1=[23,1,2,3,6]
b1=[2,6,7,9,10]
result=[a1[i]+b1[i] for i in range(len(b1)) ]# it will add according to the length of b1
# print(result)

# 2nd way
import numpy as np
arr1=np.array([12,3,5,7,9])
arr2=np.array([1,0,6,7,9])#both should be of same length otherwise get error 
results= arr1+arr2
print(results)




# leetcode query

def sum_array(nums,target):
    for i in range(len(nums)):
        for j in range (i+1,len(nums)): 
            if nums[i]+nums[j]==9:
                return[i,j]
            else:
                print("invalid")
            
nums=[2, 7, 11, 15]
target=9
print(sum_array(nums,target))
