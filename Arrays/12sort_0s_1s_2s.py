#using dutch national flag algorithm
def Dutch_flag(nums):
    low,mid,high=0,0,len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1
    return nums
mylist=[1,0,1,2,0,1]
print(f"sorting of 0s,1s and 2s in {mylist} is {Dutch_flag(mylist)}")

#using quicksort
def quicksort(nums,low,high):
    if low>=high:
        return
    pivot=nums[low]         
    left=low
    right=high
    while left<=right:
        while left<=high and nums[left]<=pivot:
            left+=1
        while right>=low and nums[right]>pivot:
            right-=1
        if left<right:
            nums[left],nums[right]=nums[right],nums[left]   
            left+=1
            right-=1
    quicksort(nums,low,right)
    quicksort(nums,left,high)
mylist=[1,0,1,2,0,1]
print(f"sorting of 0s,1s and 2s in {mylist} is {quicksort(mylist,0,len(mylist)-1)}")
