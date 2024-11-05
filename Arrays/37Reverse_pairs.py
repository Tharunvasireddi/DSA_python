# bruete force solution
def countReverse(nums):
    count=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]> 2*nums[j]:
                count+=1
    return count
arr=[12,11,10,6,3,2,1]
print(f"the nuber of count inversions are : {countReverse(arr)}")

#optimal solution
def countPairs(nums,low,mid,high):
    count=0
    right=mid+1
    for i in range(low,mid+1):
        while right<=high and nums[i]> 2*nums[right]:
            right+=1
        count+=right-(mid+1)
    return count
def merge(nums,low,mid,high):
    left=low
    right= mid+1
    merg=[]
    while left <=mid and right<=high:
        if nums[left]<=nums[right]:
            merg.append(nums[left])
            left+=1
        else:
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
def mergeSort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=(low+high)//2
    count+=mergeSort(arr,low,mid)
    count+=mergeSort(arr,mid+1,high)
    count+=countPairs(arr,low,mid,high)
    merge(arr,low,mid,high)
    return count
def countReverse(nums):
    count=0
    high=len(nums)-1
    count=mergeSort(nums,0,high)
    return count
arr=[12,11,10,6,3,2,1]
print(f"the nuber of count inversions are : {countReverse(arr)}")