#1 

nums = [2,8,7,3]
target = 9
d=dict()
for i,n in enumerate(nums):
    v = target - n
    if v not in d:
        d[n] =i
    else:
        print([d[v]],i)