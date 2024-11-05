# brute Force algorithm 
def countInversion(nums):
    count=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]> nums[j]:
                count+=1
    return count
arr=[12,11,10,6,3,2,1]
print(f"the nuber of count inversions are : {countInversion(arr)}")

#optimal solution
def merge(nums,low,mid,high):
    count=0
    left=low
    right= mid+1
    merg=[]
    while left <=mid and right<=high:
        if nums[left]<=nums[right]:
            merg.append(nums[left])
            left+=1
        else:
            count+=mid-left+1
            merg.append(nums[right])
            right+=1
    while left<=mid:
        merg.append(nums[left])
        left+=1
    while right<=high:
            merg.append(nums[right])
            right+=1
    for i in range(len(merg)):
        nums[low+i]=merg[i]
    return count
def mergeSort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=(low+high)//2
    count+=mergeSort(arr,low,mid)
    count+=mergeSort(arr,mid+1,high)
    count+=merge(arr,low,mid,high)
    return count
def countInversions(nums):
    count=0
    high=len(nums)-1
    count=mergeSort(nums,0,high)
    return count
arr=[12,11,10,6,3,2,1]
print(f"the nuber of count inversions are : {countInversions(arr)}")