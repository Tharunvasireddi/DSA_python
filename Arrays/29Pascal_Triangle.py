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
def pascal_row(row):
    res=1
    pascal=[]
    pascal.append(res)
    for i in range(0,row):
        res=res*(row-i)
        res=res//(i+1)
        pascal.append(res)
    return pascal 
row=int(input("enter the row number : "))
print(f"the nth row of the pascal triangle is : {pascal_row(row)} ")

# pascal triangle
def pascal_triangle(row):
    pascal=[]
    temp=[]
    for i in range(1,row+1):
        temp=[]
        res=1
        temp.append(res)
        for j in  range(1,i):
            res=res*(i-j)
            res=res//j
            temp.append(res)
        pascal.append(temp)
    return pascal
row=int(input("enter the row number : "))
print(f"the pascal triangle is : {pascal_triangle(row)} ")
