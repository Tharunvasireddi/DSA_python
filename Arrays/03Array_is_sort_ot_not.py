def is_sort(my_list):
    for i in range(len(my_list)-1):
        if my_list[i]>my_list[i+1]:
            return False
    return True
my_list=[1,2,3,4,6,7,5,8]
print(is_sort(my_list))