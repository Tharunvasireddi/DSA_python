def maximum_sum(nums):
    sum=0
    max=float('-inf')
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max:
                max=sum
    return max
mylist=[-1,2,3,4,-7,5,-8]
max_sum=maximum_sum(mylist)
print(f"the maximum subarray sum is :",max_sum )

#kadans algortihm or optimal solution
def kadans(nums):
    sum=0
    max_sum=float('-inf')
    for i in range(len(nums)):
        sum+=nums[i]
        if sum>0:
            max_sum=max(max_sum,sum)
        if sum<0:
            sum=0
    return max_sum
mylist=[-1,2,3,4,-7,5,-8]
max_sum=kadans(mylist)
print(f"the maximum subarray sum is : {max_sum}")