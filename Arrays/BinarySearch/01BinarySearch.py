# Binary_Search
def binarySearch(nums,tar):
    high=len(nums)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==tar:
            return mid
        elif nums[mid]>tar:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[1,2,3,4,5,6,11,18,19]
tar=int(input("enter the target to search : "))
print(f"the targeted is at : {binarySearch(arr,tar)} ")