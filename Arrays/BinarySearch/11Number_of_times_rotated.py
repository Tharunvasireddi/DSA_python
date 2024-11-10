#brute force algorithm
def Rotations(nums):
    Min=float('inf')
    ntimes=0
    for i in range(len(nums)):
        if nums[i]<Min:
            Min=nums[i]
            ntimes=i
    return ntimes
arr=[5,6,7,1,2,3,4,5]
print(f"the is array is rotated by : {Rotations(arr)} times")

#optimal soltion
def Rotations(arr):
    Min=float('inf')
    low=0
    high=len(arr)-1
    ntimes=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==arr[low] and arr[mid]==arr[high]:
            low+=1
            high-=1
        if arr[mid]<=arr[high]:
            if arr[mid]<=Min:
                Min=arr[mid]
                ntimes=mid
            high=mid-1
        else:
            if arr[low]<=Min:
                Min=arr[low]
                ntimes=low
            low=mid+1
    return ntimes
arr=[5,6,7,1,2,3,4,5]
print(f"the is array is rotated by : {Rotations(arr)} times")
