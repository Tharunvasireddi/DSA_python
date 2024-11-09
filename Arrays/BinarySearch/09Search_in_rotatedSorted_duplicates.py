#brute force solution
def linearSearch(nums,tar):
    for i in range(len(nums)):
        if nums[i]==tar:
            return i
    return -1
mylist=[9,9,9,10,1,2,3,4,5,9]
tar=int(input("enter the target value : "))
print(f"the targed value is at :{linearSearch(mylist,tar)} index")

# optimalSolution
def binarySearch(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<=arr[high]:
            if tar<=arr[high] and tar>=arr[mid]:
                low=mid+1
            else:
                high=mid-1
        else:
            high=mid-1
    return -1
mylist=[9,9,9,10,1,2,3,4,5,9]
tar=int(input("enter the target value : "))
print(f"the targed value is at :{linearSearch(mylist,tar)} index")

                
            
    