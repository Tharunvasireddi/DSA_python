#brute force algorithm
def linearSearch(nums,tar):
    for i in range(len(nums)):
        if nums[i] == tar:
            return i
    return None
mylist=[7,8,9,10,1,2,3,4,5,6]
tar=int(input("enter the target value : "))
print(f"given element is at : {linearSearch(mylist,tar)} index")

#optimal solution 
def binarySearch(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]>=arr[low]:
            if tar>=arr[low] and tar<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            low=mid+1
    return -1
mylist=[7,8,9,10,1,2,3,4,5,6]
tar=int(input("enter the target value : "))
print(f"given element is at : {binarySearch(mylist,tar)} index")