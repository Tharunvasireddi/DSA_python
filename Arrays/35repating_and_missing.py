#brute force algorith
def miss_repeating(nums):
    rep=-1
    count=0
    mis=-1
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
            if i != nums[j]:
                mis=i
            if count==2:
                rep=nums[i]
            if mis!= -1 and rep != -1 :
                break
    return rep , mis
mylist=[1,2,3,4,1,6]
rep,mis = miss_repeating(mylist)
print(f"the missing number is : {mis} and repeating number is : {rep} in {mylist}")

#better solution 
def missAndrepeating(nums):
    count_array=[0]*(len(nums)+1)
    for i in range(len(nums)):
        count_array[nums[i]]+=1
    mis=-1
    rep=-1
    for i in range(len(count_array)):
        if count_array[i]==0:
            mis=i
        elif count_array[i]==2:
            rep=i
    return rep,mis
mylist=[1,2,3,4,1,6]
rep,mis = missAndrepeating(mylist)
print(f"the missing number is : {mis} and repeating number is : {rep} in {mylist}")

#optimal solution 
def miss_Repeating(nums):
    n=len(nums)
    sum=(n*(n+1))//2
    sum1=0
    for i in range(len(nums)):
        sum1+=nums[i]
    val1= sum-sum1
    s2=(n*(n+1)*(2*n+1))//6
    sn2=0
    for i in range(len(nums)):
        sn2+=nums[i]*nums[i]
    val2=s2-sn2
    val=val2//val1
    mis=(val1+val)//2
    rep=mis-val1
    return rep , mis 
mylist=[1,2,3,4,1,6]
rep,mis = miss_Repeating(mylist)
print(f"the missing number is : {mis} and repeating number is : {rep} in {mylist}") 