def next_permutation(nums):
    ind =-1
    for i in range(len(nums)-2,0-1,-1):
        if nums[i]>nums[i+1]:
            ind=i
            break
    if ind ==-1:
        left=0
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
    for i in range(len(nums)-1,0-1,-1):
        if nums[ind]<nums[i]:
            nums[ind],nums[i]=nums[i],nums[ind]
            break
    left=ind+1
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums
mylist=[1,2,3,4,5,6,7]
perm=next_permutation(mylist)
#print(f"the next permutation of the given {mylist} is : {next_permutation(mylist)}")
print(perm)