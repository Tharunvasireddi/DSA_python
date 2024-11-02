#brute force solution 
def union(num1,nums2):
     set1=set(num1) # declaring  
     for i in nums2:
          set1.add(i)
     list1=list(set1)
     return list1
nums1=[1,2,3,4,5]
nums2=[2,3,4,4,6]
print(f"Union of two arrays is {union(nums1,nums2)}")
     
def Union(arr1,arr2):
     i,j=0,0
     res=[]
     while i <len(arr1) and j<len(arr2):
          if arr1[i]<=arr2[j]:
               if len(res)==0 or res[-1]!=arr1[i]:
                    res.append(arr1[i])
               i+=1
          else:
              if len(res)==0 or res[-1]!=arr2[j]:
                  res.append(arr2[j])
              j+=1
     while i<len(arr1):
         if res[-1]!=arr1[i]:
             res.append(arr[i])
         i+=1
     while j<len(arr2):
         if res[-1]!=arr2[j]:
             res.append(arr2[j])
         j+=1
     return res
nums1=[1,2,3,4,5]
nums2=[2,3,4,4,6]
print(f"Union of two arrays is {Union(nums1,nums2)}")
               
              