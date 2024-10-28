#printing nth value of pascal triangl
def pascal(row,col):
    res=1
    for i in range (col):
        res=res*(row-i)
        res=res//(i+1)       
    return res
row=int(input("enter the row number : "))
col=int(input("enter the column number :  "))
print(f"the nth value of the pascal triangle is {pascal(row,col)}")

#  nth row of pascal triangle
 