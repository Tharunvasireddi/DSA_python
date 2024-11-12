#brute force algorithm
def root_of_number(num):
    root=-1
    for i in range(num//2+1):
        if i*i <=num:
            root=i
    return root
num=int(input("enter the number : "))
if num>0:
  print(f"the Square root of the number is : {root_of_number(num)}")
else:
    print("value error")
    
#optimal solution 
def  square_root(n):
    low=1
    high=n//2
    root=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=n:
            root=mid
            low=mid+1
        else:
            high=mid-1
    return root
num=int(input("enter the number : "))
if num>0:
  print(f"the Square root of the number is : {square_root(num)}")
else:
    print("value error")