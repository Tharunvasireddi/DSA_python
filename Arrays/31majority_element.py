#brute force solution
def majority_element(nums):
    count=0
    n=len(nums)
    greater=[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count > n//3:
            if nums[i] not in greater:   
             greater.append(nums[i])
        if len(greater)==2:
            break 
    return greater
nums=[1,2,1,3,1,4,1,2,2,1,2]
print(f"those elements which have count greater the n/3 times of length : {majority_element(nums)}")

#optimal solution
def Majority(nums):
    map={}
    max=[]
    for i in  nums:
        if i in map:
            map[i] +=1
            if map[i] == 3 and i not in max:
                max.append(i)
        else :
                map[i]=1
                map[nums[i]]=1
    return max
nums=[1,2,1,3,1,4,1,2,2,1,2]
print(f"those elements which have count greater the n/3 times of length : {Majority(nums)}")  

#optimal solution
def mores_count(nums):
    count1=0 
    count2=0
    element1=0
    element2=0
    for i in range(2,len(nums)):
        if count1==0 and nums[i]!= element2:
            element1=nums[i]
            count1=1
        elif count2==0 and element1!=nums[i]:
            element2=nums[i]
            count2=1
        elif nums[i]==element2:
            count2+=1
        elif nums[i]==element1:
            count1+=1
        else :
            count1-=1
            count2-=1
    return element1,element2
mylist=[1,2,1,3,1,4,1,2,2,1,2]
print(f"the elements that are greater than length//3 times is : {mores_count(mylist)} ")
        
            
            
    