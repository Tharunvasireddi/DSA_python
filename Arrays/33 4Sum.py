#brute force algorithm
def four_sum(nums,tar):
    my_set=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==tar:
                        temp=tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
                        my_set.add(temp)
    result=list(my_set)
    return result
mylist=[10,11,10,12,11]
print(f"the elements of the array that give the sum is : {four_sum(mylist,43)}")

#better solution 
def Foursum(nums,tar):
    my_set=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            map={}
            for k in range(j+1,len(nums)):
                sum=nums[i]+nums[j]+nums[k]
                diff=tar-sum
                if diff in map:
                    temp=tuple(sorted([nums[i],nums[j],nums[k],nums[map[diff]]]))
                    my_set.add(temp)
                else:
                    map[nums[k]]=k
    result=list(my_set)
    return result
mylist=[10,11,10,12,11]
print(f"the elements of the array that give the sum is : {Foursum(mylist,43)}")

#optimal solution 
def fourSum(nums,tar):
    nums.sort()
    result=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j !=i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=len(nums)-1
            while k < l:
                sum=nums[i]+nums[j]+nums[k]+nums[l]
                if sum==tar:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                elif sum>tar:
                    l-=1
                else:
                    k+=1
    return result
mylist=[10,11,10,12,11]
print(f"the elements of the array that give the sum is : {fourSum(mylist,43)}")
 
    
     