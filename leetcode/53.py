#53


nums = [-2,1,-3,4,-1,2,1,-5,4]

size=len(nums)
def n(a,size): 

    mx =a[0] 
    c_mx = a[0] 

    for i in range(1,size): 
        c_mx = max(a[i], c_mx + a[i]) 
        mx = max(mx,c_mx) 

    return mx
mx=n(nums,size)
print(mx)