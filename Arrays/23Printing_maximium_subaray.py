#bruete force algorithm
def max_sum(num1):
    sum=0
    start=0
    end=0
    max=float('-inf')
    for i in range(len(num1)):
        sum=0
        for j in range(i,len(num1)):
            sum+=num1[i]
            if sum > 0:
                if sum>max:
                    max=sum
                    start=temp_start
                    end=i
            else:
                sum=0
                temp_start=+1
    return num1[start:end+1]
mylist=[-1,2,3,4,-7,5,-8]
max_sum=max_sum(mylist)
print(f"the maximum subarray sum is : {max_sum}")

#optimal solution
def kadans(num1):
    sum=0
    temp_start=0
    start=0
    end=0
    max=float('-inf')
    for i in range(len(num1)):
        sum+=num1[i]
        if sum<0:
            temp_start=i+1
            sum=0
        if sum >0:
            if sum>max:
                max=sum
                start=temp_start
                end=i
    return num1[start:end+1]
mylist=[-1,2,3,4,-7,5,-8]
max_sum=kadans(mylist)
print(f"the maximum subarray sum is : {max_sum}")