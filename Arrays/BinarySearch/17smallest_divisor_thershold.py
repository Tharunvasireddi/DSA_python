# brute force solution
def maximum(nums): # find maxium for minimize iteraions
    max=float('-inf') 
    for i in range(len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max
def totalSum(nums,div): # calculating the dividing sum
    sum=0
    for i in range(len(nums)):
        sum+=(nums[i]+div-1)//div
    return sum
def linearSearch(nums,ter):
    ans=-1
    for i in range(1,maximum(nums)+1): # iterating for search
        totalsum=totalSum(nums,i)
        if totalsum<=ter: # checking the totalsum is less than or equal 
            ans=i
            break
    return ans
mylist=[1,2,5,6]
ter=int(input("enter the thershold : "))
print(f"the smallest divisor is :{linearSearch(mylist,ter)}")

# optimal solution 
def maximum(nums): # find maxium for minimize iteraions
    max=float('-inf')
    for i in range(len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max
def totalSum(nums,div):# calculating the dividing sum
    sum=0
    for i in range(len(nums)):
        sum+=(nums[i]+div-1)//div
    return sum
def binarySearch(nums,ter):# using binary Search
    low=1
    high=maximum(nums) #intilaising the high with maximum value of given array to iterate to that number
    ans=-1
    while low<=high:
        mid=(low+high)//2
        totalsum=totalSum(nums,mid)
        if totalsum <=ter: # checking the total sum is less than or given thershold 
            ans=mid
            high=mid-1 # go for minimum divisor
        else:
            low=mid+1 # go for sum value less than or equal to ter 
    return ans
mylist=[1,2,5,6]
ter=int(input("enter the thershold : "))
print(f"the smallest divisor is :{binarySearch(mylist,ter)}")
