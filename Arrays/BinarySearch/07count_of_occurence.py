#brute force algorithm
def firstAndlast(nums,tar):
    first=-1
    last=-1
    for i in range(len(nums)):
        if nums[i]==tar:
            first=i
            break
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==tar:
            last=i
            break
    return last-first+1
mylist=[1,2,3,4,4,4,4,5,6]
tar=int(input("enter the target value : "))
count=firstAndlast(mylist,tar)
print(f"the first occurence of the given {tar} is : {count} ")

#plane binary search approach
def firstAndlast(nums,tar):
      first=-1
      low=0
      high=len(nums)-1
      while low<=high:
          mid=(low+high)//2
          if nums[mid]==tar:
              first=mid
              high=mid-1
          elif nums[mid]<tar:
              low=mid+1
          else:
              high=mid-1
      last=-1
      low=0
      high=len(nums)-1
      while low<=high:
          mid=(low+high)//2
          if nums[mid]==tar:
              last=mid
              low=mid+1
          elif nums[mid]<tar:
              low=mid+1
          else:
              high=mid-1
      return last-first+1         
mylist=[1,2,3,4,4,4,4,5,6]
tar=int(input("enter the target value : "))
count=firstAndlast(mylist,tar)
print(f"the first occurence of the given {tar} is : {count} ")


#better approach
def firstAndlast(nums,tar):
    first=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=tar:
            first=mid
            high=mid-1
        else:
            low=mid+1
    last=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>tar:
            last=mid
            high=mid-1
        else:
            low=mid+1
    if last==-1:
        last=first
    else:
        last-=1
    return last-first+1
mylist=[1,2,3,4,4,4,4,5,6]
tar=int(input("enter the target value : "))
count=firstAndlast(mylist,tar)
print(f"the first occurence of the given {tar} is : {count} ")

