def ugly_number(n):
    if n<=0:
        return False
    
    while n%2==0:
        n//=2

    while n%3==0:
        n//=3 

    while n%5==0:
        n//=5

    return  (n==1) 


test_list=[1,2,3,45,55,23,0,1,67,9,0,78,43]
for num in test_list:
    if ugly_number(num):
        print(f"{num} is a ugly number ")
    else:
        print(f"{num} is not an ugly number")