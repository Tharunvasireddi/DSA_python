# brute force 

def Floor(nums,tar):
    low=0
    high=len(nums)-1
    floor=-1
    while low <= high:
        mid=(low+high)//2
        if nums[mid]<=tar:
            floor=nums[mid]
            low=mid+1
        else :
            high=mid-1
    return floor
def Ceil(nums,tar):
    low=0
    high=len(nums)-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=tar:
            ceil=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return ceil
arr=[1,2,3,4,5,6,11,18,19]
tar=int(input("enter the target to search : "))
print(f"the floor of the given target is : {Floor(arr,tar)} and ceil is : {Ceil(arr,tar)}")


            