# bruet force algorithm
def lower_bound(nums,tar):
    ind=None
    for i in range(len(nums)):
        if nums[i]>=tar:
            ind=i
            return ind
    return -1
arr=[1,2,3,4,5,6,11,18,19]
tar=int(input("enter the target to search : "))
print(f"the lower bound of the element is : {lower_bound(arr,tar)}")

#optimal solution 
def lowerbound(nums,tar):
    high=len(nums)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=tar:
            ind=mid
            high=mid-1
        else:
            low=mid+1
    return ind
arr=[1,2,3,4,5,6,11,18,19]
tar=int(input("enter the target to search : "))
print(f"the targeted is at : {lowerbound(arr,tar)} ")
