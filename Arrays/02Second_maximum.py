# solution
def Second_max(my_list):
    max = float('-inf') # intialising max and max2 with minimum values
    max2 = float('-inf')
    for i in my_list: # iterating the arary
        if max < i: # 
             max2=max
             max=i
        elif i >max2 and max!=i:
            max2=i         
    return max2
my_list=[1,100,90,83,97]
max2=Second_max(my_list)
print("the second maximum element of the array is :",max2)