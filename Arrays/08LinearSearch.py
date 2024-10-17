def linear_search(mylist,target):
    for i in mylist:
        if i ==target:
            return True
    return False
my_list=[1,10,23,2,45,4,67,89]
if linear_search(my_list,45):
    print("given element is present in the given list")
else :
    print("given element is absent in the given list")