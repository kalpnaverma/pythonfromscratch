def cal_sum(number):
    # return sum( int(digit) **2 for digit in str(number))


    sum=0
    while number>0:
        digit=number%10
        sum=sum+digit**2
        number=number//10  
    return sum     #n=23   23%10=3 digit=3  digit=0+3**2=9    sum=9 number=23//10=2  now number=2
                                   
def is_happy(n) :
    seen=set() 
    while n!=1 and  n not in seen :
      seen=set() 
      seen.add(n)
      n=cal_sum(n)
      if (n==1):
          return True


n=int(input("enter a number"))
if is_happy(n) :
    print(f"{n} is happy number")
else:
    print(f"{n} is not happy number")    
     
