#brute force algorithim
def Maximum(nums): #calculating the maximum days of flowers in the garden will bloom
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def total_boque(nums,k,day): #calculating boques for the given days  
    count=0
    total_boq=0
    for i in range(len(nums)): #iteraring the array for the caslculating the number of boque will be made
        if nums[i]<=day: # checking if the flower will bloom on the given day or not 
            count+=1 # if it ,the count will increase
            if count==k: # if the count is == k then boque will be ready
                total_boq+=1 # if it ,increase the count of boque and reset the count for  next boque
                count=0 
        else:
            count=0 # if not then reset the count because the we have to take adjacent flowers
    return total_boq
def linearSearch(nums,m,k):
    high=Maximum(nums)
    total_day=-1
    for i in range(high+1): #iterating the for loop for searching the days 
        if total_boque(nums,k,i)==m: #checking the days is answer or not
            total_day=i
            break
    return total_day
my_list=[5,5,5,5,10,5,5]
m=int(input("enter the no boques : "))
k=int(input("enter the no of flowers per boque : "))
print("the minimum days to make {0}  boques are :".format(m),linearSearch(my_list,2,3))
#optimal Solution(BinarySearch)
def Maximum(nums): #calculating the maximum days of flowers in the garden will bloom
    max=float('-inf')
    for i in nums:
        if i>max:
            max=i
    return max
def total_boque(nums,k,day): #calculating boques for the given days  
    count=0
    total_boq=0
    for i in range(len(nums)): #iteraring the array for the caslculating the number of boque will be made
        if nums[i]<=day: # checking if the flower will bloom on the given day or not 
            count+=1 # if it ,the count will increase
            if count==k: # if the count is == k then boque will be ready
                total_boq+=1 # if it ,increase the count of boque and reset the count for  next boque
                count=0 
        else:
            count=0 # if not then reset the count because the we have to take adjacent flowers
    return total_boq
def binarySearch(nums,m,k): # using binary Search for decreasing time complexity
    low=1                #intialising the low value to one for checking from fist day
    high=Maximum(nums)   # high is intialise the maximum no of days 
    total_day=-1 
    while low<=high:
        mid=(low+high)//2
        total_b=total_boque(nums,k,mid) # calling the function to count boques can made on the day
        if total_b>=m: # checking the obtain boques are enough or not 
            total_day=mid
            high=mid-1 # if it then go for minimum days 
        else:
            low=mid+1 # if not go for sufficient days 
    return total_day
my_list=[5,5,5,5,10,5,5]
m=int(input("enter the no boques : "))
k=int(input("enter the no of flowers per boque : "))
print("the minimum days to make {0}  boques are :".format(m),binarySearch(my_list,2,3))