#brute force algorithm
def maxSubarray(nums,tar):
    count=0
    for i in range(len(nums)):
        xor=0
        for j in range(i,len(nums)):
            xor^=nums[j]
            if xor==tar:
                count+=1
    return count
mylist=[4,2,2,6,4]      
print(f"the count of subarray with given xor is : {maxSubarray(mylist,6)}")

#optimal solution
def MaxSubarray(nums,tar):
    count=0
    map={0:1}
    xor=0
    for i in range(len(nums)):
       xor^=nums[i]
       x=xor^tar
       count+=map.get(x,0)
       map[xor]=map.get(xor,0)+1
    return count
mylist=[4,2,2,6,4]      
print(f"the count of subarray with given xor is : {MaxSubarray(mylist,6)}")
    