 #bruete force solution
def majority(nums):
     count=0
     n=len(nums)//2
     max_count=0
     ind=0
     for i in range(len(nums)):
         count=0
         for j in range(len(nums)):
             if nums[i]==nums[j]:
                 count+=1
         if count>n:
            if max_count<count:
                max_count=count
                ind=i
     return ind
mylist=[1,2,1,1,1,1,1,3,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
max=majority(mylist)
print("the majority element that the count greater than half of array is :",mylist[max])
            
#better approach
def majorty_ele(nums):
    map={}
    element=0
    n=len(nums)//2
    max_count=0
    for i in nums:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    print(map)
    for i in nums:
        if map[i]>n:
            if max_count < map[i]:
                element=i
                max_count=map[i]
    return element
mylist=[1,2,1,1,1,1,1,3,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
max=majorty_ele(mylist)
print("the majority element that the count greater than half of array is :",mylist[max])
