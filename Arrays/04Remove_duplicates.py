def rem_Dup(my_list):
    i=0
    for j in range(1,len(my_list)):
        if my_list[i]!=my_list[j]:
            i+=1
            my_list[i]=my_list[j]
    return i+1
my_list=[1,1,2,2,3,3,4]
print(f"after removing duplicates in {my_list} is {rem_Dup(my_list)}")