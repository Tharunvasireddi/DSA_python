def stock(nums):
    buy=float('inf')
    max_profit=0
    for i in range(len(nums)):
        if nums[i]<buy:
            buy=nums[i]
        if nums[i]-buy>max_profit:
            max_profit=nums[i]-buy
            sell_day=nums[i]
    return max_profit
mylist=[4,2,2,2,4]
max_profit=stock(mylist)
print(f"the maximum profit is : {max_profit}")

# using maximmum and minimum
def sell_stock(nums):
    min=float('inf')
    ind =0
    for i in range(len(nums)):
        if nums[i]<min:
            min=nums[i]
            ind=i
    max=min
    for j in range(i,len(nums)):
        if max<=nums[j]:
            max=nums[j]
    return max-min
mylist=[7,6,4,1,6]
max_profit=sell_stock(mylist)
print(f"the maximum profit is : {max_profit}")
