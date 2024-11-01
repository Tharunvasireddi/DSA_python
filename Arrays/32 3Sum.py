#brute force solution
def Three_sum(nums,tar):
   my_Set=set()
   result=[]
   for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==tar:
                    temp=tuple(sorted([nums[i],nums[j],nums[k]]))
                    my_Set.add(temp)
   result.append(my_Set)
   return result
mylist=[-1,0,1,2,-1,-4]
print(f"the triplets of the array is : {Three_sum(mylist,0)}")

#Better approach
def threeSum(nums,tar):
    map={}
    my_set=set()
    result=[]
    for i in range(len(nums)):
        map={}
        for j in range(i+1,len(nums)):
            diff=tar-(nums[i]+nums[j])
            if diff in map:
                 temp=tuple(sorted([nums[i],nums[j],nums[map[diff]]]))
                 my_set.add(temp)
            else : 
                map[nums[j]]=j
    result.append(my_set)
    return result
mylist=[-1,0,1,2,-1,-4]   
print(f"the triplets of the array is : {threeSum(mylist,0)}")

#optimal solution 
def ThreeSum(nums,tar):
    nums.sort()
    result=[]
    for i in range(len(nums)):
        j=i+1
        k=len(nums)-1
        if i>0 and  nums[i]==nums[i-1]:
            continue
        while j < k :
            sum=nums[i]+nums[j]+nums[k]
            if sum < tar:
                j==1
            elif sum>tar:
                k+=1
            else :
               result.append([nums[i],nums[j],nums[k]])  
               while j<k and nums[j]==nums[j-1]:
                   j+=1
               while k>j and nums[k]==nums[k-1]:
                    k+=1
               j+=1
               k-=1
    return result
mylist=[-1,0,1,2,-1,-4]   
print(f"the triplets of the array is : {threeSum(mylist,0)}")

                
            
        