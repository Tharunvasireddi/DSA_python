def Sum(arr):
    length=len(arr)
    sum=0
    for i in range(length+2):
        sum+=i
    sum1=0
    for j in arr:
        sum1+=j
    mis=sum-sum1
    return mis
mylist=[1,2,4,5]
print(Sum(mylist))

def Hashing(nums):
    length=len(nums)+1
    count=[0]* length
    for k in range(len(nums)-1):
        count[nums[k]]+=1
    for t in range(1,len(count)):
        if count[t]==0:
            return t
mylist=[1,2,4,5]
print(Hashing(mylist))

def Missing_xor(arr):
    xor=0
    for i in range(len(arr)+2):
        xor^=i
    for j in arr:
        xor^=j
    return xor
ylist=[1,2,4,5]
print(Missing_xor(ylist))