# brute force solution
def sum_0(nums):
    sum=0
    max_len=0
    for i in range(len(nums)):
        sum+=nums[i]
        for j in range(i+1,len(nums)):
            sum+=nums[j]
            if sum==0:
                max_len=max(max_len,j-i+1)
        sum=0
    return max_len
nums=[5,-1,-1,-1,-1,-1,7,-1,-1 ,7]
print(f"the length  maximum sub array with sum 0 is : {sum_0(nums)}")

#optimal solution
def Sum_0(nums):
    map={}
    max_len=0
    len1=0
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum in map:
            len1=i-map[sum]
            max_len=max(max_len,len1)
        else:
            map[sum]=i
    return max_len
nums=[5,-1,-1,-1,-1,-1,7,-1,-1 ,7]
print(f"the length  maximum sub array with sum 0 is : {Sum_0(nums)}")



                