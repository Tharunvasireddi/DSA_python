#brute force
def count_subarray(num1,k):
    count=0
    for i in range(len(num1)):
        sum=0
        for j in range(i,len(num1)):
            sum+=num1[j]
            if sum==k:
                count+=1
    return count
mylist=[2,1,3,4,1,2,1,5,4] 
max_len=count_subarray(mylist,6)
print("count of subaaray with sum k is :",max_len)


#optimal solution
