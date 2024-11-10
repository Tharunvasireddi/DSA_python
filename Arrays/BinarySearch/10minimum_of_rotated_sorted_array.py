#brute force algorithm
def minimum(nums):
    Min=float('inf')
    for i in nums:
        Min=min(Min,i)
    return Min
mylist=[5,6,7,1,2,3,4]
print(f"minimum of the array is : {minimum(mylist)}")

#optimal solution
def Minimum(arr):
    Min=float('inf')
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low+=1
            high-=1
        if arr[low]<=arr[mid]:
            Min=min(Min,arr[low])
            low=mid+1
        else:
            Min=min(Min,arr[mid])
            high=mid-1
    return Min
mylist=[5,6,7,1,2,3,4,5]
print(f"minimum of the array is : {Minimum(mylist)}")
