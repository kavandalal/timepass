def knap(v,w,W):
    vw=[]
    n=len(v)
    for i in range(n):
        vw.append(v[i] / w[i])
    print('\n')
    [print("{:.2f}".format(i),end='\t') for i in vw]
    vwc= vw.copy()
    vwc.sort(reverse=True)
    i=0
    V=0
    while W > 0:
        x= vwc[i] 
        j=vw.index(x)
        vw[j]=0
        #print(v[j],w[j])
        if W - w[j] >= 0:
            V += v[j]
            W -= w[j]
        else : 
            V+=(W /w[j])*v[j]
            W-=(W /w[j])*w[j]
        i+=1
        #print(V,W)
    print('\n\nValue =',V)


v = input('Enter the values in knapsack\n').split()
v = [int(i) for i in v]
w=input('Enter the weights in knapsack\n').split()
w = [int(i) for i in w]
W=int(input('Enter total weight in knapsack\n'))
print('\n\t')
[print('i',i+1,end='\t') for i in range(len(v))]
print('\n')
[print(i,end='\t') for i in v]
print('\n')
[print(i,end='\t') for i in w]
knap(v,w,W)

'''
20 30 66 40 60 
10 20 30 40 50 
100 
Answer =164
'''
'''
10 5 15 7 6 18 3
2 3 5 7 1 4 1
15
Answer = 55
'''