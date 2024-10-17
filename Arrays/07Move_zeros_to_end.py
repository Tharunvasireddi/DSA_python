def move_0(mylist):
    temp=[]
    k=0
    for i in  mylist:
        if i != 0:
            k+=1
            temp.append(i)
    mylist=[0]*len(mylist)
    for i in range(k):
        mylist[i]=temp[i]
    return mylist
mylist=[1,0,4,5,0]
print(f"moving the zeros to end {mylist} is {move_0(mylist)}")

#optimal approach
def moves_0s(nums):
    i=-1
    for k in range(len(nums)):
        if nums[k]==0:
            i=k
            break
    if i==-1:
        return nums
    for j in range(i+1,len(nums)):
        if nums[j]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            i+=1
    return nums
nums=[1,20,5,0,6,0]
print(f"Array after moving zeros to end {nums} is {moves_0s(nums)}")