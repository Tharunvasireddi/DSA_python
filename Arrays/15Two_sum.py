#brute force
def Twosum(nums,tar):
    sum=0
    index=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum=nums[i]+nums[j]
            if sum==tar:
                index.append(i)
                index.append(j)
                return index
    return -1
mylist=[7,11,9,15,13,14]
two_sum=Twosum(mylist,22)
print("the two indices are :",two_sum)


#better approch
def Two_sum(arr,tar):
    map={}
    index=[]
    for i in range(len(arr)):
        diff=tar-arr[i]
        if diff in map:
            index.append(i)
            index.append(map[diff])
        else:
            map[arr[i]]=i
    return index
mylist=[7,11,9,15,14]
print("two sum of the given list is :",Two_sum(mylist,22))