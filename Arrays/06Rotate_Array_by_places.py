def Rotate(mylist,k):
    k=k%len(mylist)
    temp=[0]*k
    for i in range(k):
        temp[i]=mylist[i]
    for i in range(k,len(mylist)):
        mylist[i-k]=mylist[i]
    for i in range(0,k):
        mylist[len(mylist)-k+i]=temp[i]
    return mylist
mylist=[1,3,4,5,6]
print(Rotate(mylist,4))
  


#reversal algorithm
"""
[5,6,10,1,32,33]
[3]--->key
[10,6,5,1,32,33]
[10,6,5,33,32,1]
[1,32,33,5,6,10]
"""
def reverse(mylist,start,end):
    while start<end:
        mylist[start],mylist[end]=mylist[end],mylist[start]
        start+=1
        end-=1
def left_rotate(mylist,k):
    k=k%len(mylist)
    reverse(mylist,0,k-1)
    reverse(mylist,k,len(mylist)-1)
    reverse(mylist,0,len(mylist)-1)
    return mylist
mylist=[5,6,10,1,32,33]
k=int(input("enter the number of places you want to rotate :"))
print(f"left rotation of {mylist} by {k} times is {left_rotate(mylist,k)} ")
