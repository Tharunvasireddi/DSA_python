def move_0(mylist):
    temp=[]
    k=0
    for i in  mylist:
        if i != 0:
            k+=1
            temp.append(i)
    mylist=[0]*len(mylist)
    for i in range(k):
        mylist[i]=temp[i]
    return mylist
mylist=[1,0,4,5,0]
print(f"moving the zeros to end {mylist} is {move_0(mylist)}")