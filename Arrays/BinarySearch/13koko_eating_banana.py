# brute force solution
def Maximum(nums):
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def timeRequirred(nums,rate):
     timereq=0
     for i in range(len(nums)):
         timereq+=(nums[i]+rate-1)//rate  
     return timereq
def linearSearch(nums,hr):
    n=Maximum(nums)
    ans=0
    for i in range(1,n+1):
        totaltime=timeRequirred(nums,i)
        if totaltime<=hr:
           return i
    return -1
mylist=[1,4,5,6,7,13]
time=int(input("enter the deadline : "))
print(f"the minimum banana eat per hour is : {linearSearch(mylist,time)}")          
 
 #optimal solution
def Maximum(nums):
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def timeRequirred(nums,rate):
     timereq=0
     for i in range(len(nums)):
         timereq+=(nums[i]+rate-1)//rate  
     return timereq
def binarySearch(nums,hr):
    low=1
    high=Maximum(nums) 
    ans=-1
    while low<=high:
        mid=(low+high)//2
        totaltime=timeRequirred(nums,mid)
        if totaltime<=hr:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
mylist=[1,4,5,6,7,13]
time=int(input("enter the deadline : "))
print(f"the minimum banana eat per hour is : {binarySearch(mylist,time)}")