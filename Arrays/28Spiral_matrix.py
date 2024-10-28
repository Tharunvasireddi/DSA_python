def spiral_mat(nums):
    left,top=0,0,
    right=len(nums[0])-1
    bottom=len(nums)-1
    spiral=[]
    while left<=right and top <=bottom :
        for i in range(left,right+1):
            spiral.append(nums[top][i])
        top+=1
        for i in range(top,bottom+1):
            spiral.append(nums[i][right])
        right-=1
        if top <=bottom:
            for i in range(right,left-1,-1):
                spiral.append(nums[bottom][i])
            bottom-=1
        for i in range(bottom,top-1,-1):
            spiral.append(nums[i][left])
        left+=1
    return spiral
nums=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(f"the spiralmmatrix is : {spiral_mat(nums)}")
                
        