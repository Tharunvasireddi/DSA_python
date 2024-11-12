# brute force solution
def Maximum(nums): # finding maximum value to determin the eating bananas per hour
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def timeRequirred(nums,rate):
     timereq=0
     for i in range(len(nums)):# calculating the time if i banana are eating
         timereq+=(nums[i]+rate-1)//rate 
     return timereq
def linearSearch(nums,hr):
    n=Maximum(nums)
    ans=0
    for i in range(1,n+1): # using linear search to find the minimum number of  bananas 
        totaltime=timeRequirred(nums,i)
        if totaltime<=hr:
           return i
    return -1
mylist=[1,4,5,6,7,13]
time=int(input("enter the deadline : "))
print(f"the minimum banana eat per hour is : {linearSearch(mylist,time)}")          
 
 #optimal solution
def Maximum(nums):# finding maximum value to determin the eating bananas per hour
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def timeRequirred(nums,rate):# calculating the time if i banana are eating
     timereq=0
     for i in range(len(nums)):
         timereq+=(nums[i]+rate-1)//rate  
     return timereq
def binarySearch(nums,hr): 
    low=1                 # intilaising the low with intilal value 
    high=Maximum(nums) # intialising the high with maximum bananans can heat per hour
    ans=-1
    while low<=high:
        mid=(low+high)//2
        totaltime=timeRequirred(nums,mid) # calling function to know the how much time required to eat mid  babanans per hour
        if totaltime<=hr: # checking the total time is less than or equal to given hour
            ans=mid
            high=mid-1# and going for mimimum bananas
        else:
            low=mid+1 # going to greater number of bananas
    return low
mylist=[3,6,7,11]
time=int(input("enter the deadline : "))
print(f"the minimum banana eat per hour is : {binarySearch(mylist,time)}")