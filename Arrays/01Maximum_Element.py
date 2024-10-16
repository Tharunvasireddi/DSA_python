def Max(my_list):
    max=my_list[0]
    for i in my_list:
        if max<i:
            max=i
    return max
my_list=[1,10,100,50,30,3,4]
max=Max(my_list)
print("the maximum element of the given array is :",max)