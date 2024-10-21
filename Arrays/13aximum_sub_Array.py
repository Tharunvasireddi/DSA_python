#bruteforce solution
def subarray(nums,k):
    max_len=0
    sum=0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==k:
                max_len=max(max_len,j-i+1)
    return max_len
mylist=[-2,1,-3,4,-1,2,1,-5,4] 
max_sub=subarray(mylist,6)
print(max_sub)

#better aproach
def Subarray(nums1,tar):
    ma_len=0
    sum=0
    map={}
    for i in range(len(nums1)):
        sum+=nums1[i]
        if sum==tar:
            ma_len=max(ma_len,i+1)      
        pre_sum=sum-tar
        if  pre_sum in map:
            ma_len=max(ma_len,i-map[pre_sum])
        if pre_sum not in map:
            map[sum]=i
    return ma_len  
mylist=[-2,1,-3,4,-1,2,1,-5,4] 
ma_sub=Subarray(mylist,6)
print(ma_sub)