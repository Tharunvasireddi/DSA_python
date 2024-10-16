def Rotate(mylist):
    last=mylist[0]
    for i in range(1,len(mylist)):
         mylist[i-1]=mylist[i]
    mylist[-1]=last
    return mylist
mylist=[1,2,3,4,5]
print("rotation of {0} is :".format(mylist),Rotate(mylist))