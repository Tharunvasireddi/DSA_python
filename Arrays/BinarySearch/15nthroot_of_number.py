#brute force solution 
def nth_root(num,n):
    root=-1   
    for i in range(1,num//n): # iterating the for loop from one to the number
        if i**n <=num:#checking the nth power the i is less than/equal 
            root=i # if it is true then assign the i to the root
    return root  
num=int(input("enter the number : "))
n=int(input("enter the nth root : "))
if num>0: #checking the number greater than 0
    print(f"the {n} of the number is : {nth_root(num,n)} ")
else :
    print("value error")
    
#optimal solutiuon(using binary Search)
def nth_root(num,pow):
    root=-1
    low=1 #intialising low with 1 to start from 1
    high=num//pow #intialising high with num//pow times to decrease the end posibility
    while low <=high:
        mid=(low+high)//2
        if mid**pow<=num:#checking the nth power the i is less than/equal 
            root=mid
            low=mid+1 #go to the further higher value wich is lesse than or equal to
        else:
            high=mid-1
    return root
num=int(input("enter the number : "))
n=int(input("enter the nth root : "))
if num>0: #checking the number greater than 0
    print(f"the {n} of the number is : {nth_root(num,n)} ")
else :
    print("value error")
    