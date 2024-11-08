#Solution
def insert_position(nums,tar):
      low=0
      high=len(nums)-1
      while low <=  high:
          mid=(low+high)//2
          if nums[mid]==tar:
              return mid
          elif nums[mid]> tar:
              high=mid-1
          else:
              low=mid+1
      return low
arr=[1,2,3,4,5,6,11,18,19]
tar=int(input("enter the target to search : "))
print(f"the insert position of the element is  : {insert_position(arr,tar)}")
