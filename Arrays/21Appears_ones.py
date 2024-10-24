#brute force solution
def Appeares_ones(nums):
    count=0
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count==1:
            return nums[i]
mylist=[2,2,3,3,4,4,5,6,6,7,7]
print(f"the number that appears ones in {mylist} is : {Appeares_ones(mylist)}")

#better approach 
def Appearesones(arr):
    map={}
    for i in arr:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    for i in map:
        if map[i]==1:
            return i
    return 0
mylist=[2,2,3,3,4,4,5,6,6,7,7]
print(f"the number that appears ones in {mylist} is : {Appearesones(mylist)}")

#optimal solution
def Xor_sum(list1):
    xor=list1[0]
    for i in range(1,len(list1)):
        xor^=list1[i]
    return xor
mylist=[2,2,3,3,4,4,5,6,6,7,7]
print(f"the number that appears ones in {mylist} is : {Appearesones(mylist)}")


