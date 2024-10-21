#bruete force algorithm
def maximum_sub(nums,k):
    sum=0
    max_len=0
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==k:
                max_len=max(max_len,j-i+1)
    return max_len
mylist=[-2,1,-3,4,-1,2,1,-5,4] 
max_len=maximum_sub(mylist,6)
print("length of maximum array is :",max_len)

#optimal solution 
def Subarray(nums,k):
    max_len=0
    sum=0
    map={}
    for i in range(len(nums)):
        sum+=nums[i]
        if sum==k:
            max_len=max(max_len,i+1)
        diff=sum-k
        if diff in map:
            len1=i-map[diff]
            max_len=max(max_len,len1)
        if diff not in map:
            map[sum]=i
    return max_len
list1=[-2,1,-3,4,-1,2,1,-5,4]
max_sub=Subarray(list1,6)
print("the maximum length of subarray is :",max_sub)