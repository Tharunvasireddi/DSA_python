#method [1]: arranging positives in even indexes and arranging negatives  in odd indexes
#bruete force
def rearranging(nums):
    pos=[]
    neg=[]
    for i in nums:
        if i <0:
            neg.append(i)
        else:
            pos.append(i)
    for i in range(len(pos)):
        nums[i*2]=pos[i]
    for i in range(0,len(neg)):
        nums[i*2+1]=neg[i]
    return nums
mylist=[1,2,-3,-4,5,-8,9,-7]
print("the rearranging of negatives and positives in alternative order is :",rearranging(mylist))

#optimal solution
def Re_arranging(nums):
    pos=0
    neg=1
    result=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i]<0:
            result[neg]=nums[i]
            neg+=2
        else: 
             result[pos]= nums[i]
             pos+=2
    return result
mylist=[1,2,-3,-4,5,-8,9,-7]
print("the rearranging of negatives and positives in alternative order is :",Re_arranging (mylist))