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
    return first ,last
mylist=[1,2,3,4,4,4,4,5,6]
first,last=firstAndlast(mylist,4)
print(f"the first occurence of the arget is : {first} and last occurence of the target is : {last}")

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
      return first,last         
mylist=[1,2,3,4,4,4,4,5,6]
first,last=firstAndlast(mylist,6)
print(f"the first occurence of the arget is : {first} and last occurence of the target is : {last}")
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
    return first,last
mylist=[1,2,3,4,4,4,4,5,6]
first,last=firstAndlast(mylist,4)
print(f"the first occurence of the arget is : {first} and last occurence of the target is : {last}")
