# bruete force algorithm
def max_consecutive(nums):
    long_count=0
    stcount=0
    tar=0
    for i in nums:
        tar=i
        stcount=0
        while tar in nums:
           stcount+=1
           tar+=1
        long_count=max(long_count,stcount)
    return long_count
mylist=[1,102,103,104,2,5,4,6,3,101,105,106,107]
print(f"the longest consecutive sequence in {mylist} is : {max_consecutive(mylist)}")

#better solution 
def maxConsecutive(nums):
    nums.sort()  
    stseq=float("-inf")
    curcount=1
    long_count=0
    for i in nums:
        if i-1==stseq:
            curcount+=1
            stseq=i
        elif i-1!=stseq:
            stseq=i
            curcount=1
        long_count=max(curcount,long_count)
    return long_count
mylist=[1,102,103,104,2,5,4,6,3,101,105,106,107]
print(f"the longest consecutive sequence in {mylist} is : {max_consecutive(mylist)}")

#optimal solution
def max_Consecutive(nums):
    myset=set(nums)
    curcout=1
    long_count=0
    for i in myset:
        curcout=1 
        if i-1  not in myset:
            while i+1  in myset:
                curcout+=1
                i+=1
            long_count=max(long_count,curcout)
    return long_count
mylist=[1,102,103,104,2,5,4,6,3,101,105,106,107,108]
print(f"the longest consecutive sequence in {mylist} is : {max_Consecutive(mylist)}")

                
                

        