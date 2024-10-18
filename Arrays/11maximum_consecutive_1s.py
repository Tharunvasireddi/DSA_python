def consecutive(mylist):
    count =0
    max_count=0
    for i in mylist:
        count = count+1 if i==1 else 0
        max_count=max(count,max_count)
    return max_count

nums=[1]
print("maximum consecutive ones is :",consecutive(nums)) 