# brute force solution
def merge(num1, num2):
    n=len(num1)
    m=len(num2)
    num3=[0]*(m+n)
    left=0
    right=0
    ind=0
    while left <n and right<m:
        if num1[left]<=num2[right]:
            num3[ind]=num1[left]
            left+=1
            ind+=1
        else :
            num3[ind]=num2[right]
            ind+=1
            right+=1
    while left < n:
        num3[ind]=num1[left]
        left+=1
        ind+=1
    while right<m:
        num3[ind]=num2[right]
        right+=1
        ind+=1
    return num3
mylist=[1,3,4,5,6]
mylist1=[2,4,6,7,8,9]
print(f"the merged array of given two arrays is : {merge(mylist,mylist1)}")

#optimal solution 1
def merge_2(num1,num2):
    n=len(num1)
    m=len(num2)
    left=n-1
    right=0
    while left>=0 and right<m:
        if num1[left]>num2[right]:
            num1[left],num2[right]=num2[right],num1[left]
            left-=1
            right+=1
        else :
            break
    num1.sort()
    num2.sort()
    return num1+num2
mylist=[1,3,4,5,6]
mylist1=[2,4,6,7,8,9]
print(f"the merged array of given two arrays is : {merge_2(mylist,mylist1)}")

#optimal solution 2
def merge_3(num1,num2):
     