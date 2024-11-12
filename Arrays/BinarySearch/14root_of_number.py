#brute force algorithm
def root_of_number(num):
    root=-1
    for i in range(num//2+1): #iterating the for loop 
        if i*i <=num: #checking the i is it sqaure root or not 
            root=i
    return root
num=int(input("enter the number : "))
if num>0:
  print(f"the Square root of the number is : {root_of_number(num)}")
else:
    print("value error")
    
#optimal solution 
def  square_root(n):
    if n==1: #return in 1 if number == 1
        return 1
    low=1
    high=n//2 #intilaisng high with n//2 to decrease the iterations
    root=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=n: # checking the mid is it squre root of the number or not and also less then  or not 
            root=mid
            low=mid+1 #if it is true go futher for the correct value
        else:
            high=mid-1 # if it is false then going for lesser values 
    return root
num=int(input("enter the number : "))
if num>0:
  print(f"the Square root of the number is : {square_root(num)}")
else:
    print("value error")