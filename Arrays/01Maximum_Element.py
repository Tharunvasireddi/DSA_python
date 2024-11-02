#solution
def Max(my_list):
    max=float("-inf") # instialising with minimum value
    for i in my_list:
        if max<i:     #checking the elements in the array 
            max=i
    return max # retrun maximum elemenet 
my_list=[1,10,100,50,30,3,4]
max=Max(my_list)
print("the maximum element of the given array is :",max)