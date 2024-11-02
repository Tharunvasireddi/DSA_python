#solution
def Max(my_list):     # max function
    max=float("-inf") # instialising with minimum value
    for i in my_list: #traverse the list using for loop
        if max<i:     #check condition
            max=i     #if condition is true update max
    return max        
my_list=[1,10,100,50,30,3,4]
max=Max(my_list)
print("the maximum element of the given array is :",max)
