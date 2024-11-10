#brute force algorithm
def sigleElement(nums):
    for i in range(len(nums)):
        if i==0 and nums[1]!=nums[0]:
            return nums[i]
        elif i==len(nums)-1 and nums[i]!=nums[i-1]:
            return nums[i]
        else:
            if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                return nums[i]
    return None
arr=[1,1,2,2,3,3,4,5,5,6,6]
print(f"the sigle element is : {sigleElement(arr)}")
            
#optimal solution
def singleElement(arr):
    if arr[0]!=arr[i]:
        return arr[0]
    if arr[-1]!=arr[-2]:
        return arr[-1]
    low=1
    high=len(arr)-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        elif (mid%2==0 and arr[mid]==arr[mid+1]) or (mid%2==1 and arr[mid-1]==arr[mid]):
            low=mid+1
        else:
            high=mid-1
    return None
arr=[1,1,2,2,3,3,4,5,5,6,6]
print(f"the sigle element is : {sigleElement(arr)}")
                  