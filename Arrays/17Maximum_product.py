#brute force
def max_product(nums):
    product=1
    max_prod=float('-inf')
    for i in range(len(nums)): 
        product=1
        for j in range(i,len(nums)):
            product*=nums[i]
            if product>max_prod:
                max_prod=product
    return max_prod
mylist=[-1,2,3,4,-7,5,-8]
max_pro=max_product(mylist)
print(f"the maximum product of subaray is : {max_pro}")