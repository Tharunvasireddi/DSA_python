# brute force algorithm
def Divisor(num):
    div=1
    for i in range(2,num+1):
        if num%i==0: #checking the it is divisor or not 
            div=i
            break
    return div
num=int(input("enter the number : "))
if num==0:
    print("the smallest divioser is not difined ")
else:
    print(f"the smallest divisor is : {Divisor(num)} ")
    
#optimal Solution(Binary Search)
def Divisor(num):
    low=2
    high=num**(1/2) # intialising high with root value of the number 
    while low<=high:
        mid=(low+high)//2
        if num%mid==0: #checking the mid if it divisor or not 
            high=mid-1
        else :
            low=mid+1
    return low if num%low==0 else num
num=int(input("enter the number : "))
if num==0:
    print("the smallest divioser is not difined ")
else:
    print(f"the smallest divisor is : {Divisor(num)} ")
     
