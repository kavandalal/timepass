#1st number is keyword 

l1=['dig0 1 2 3','dig1 0 1 2 ','let0 abc y','let1 xy abc xy','g1 abc asdy','a1 abc asdy']

l2 = []
c= []
for i in l1:
    i_s=i.split()
    
    if i_s[1].isalpha():
        l2.append(i)
        continue
    else: 
        c.append(l1.index(i))

l2_s=[]
for j in l2:
    j_s = j.split()
    l2_s.append(j_s)
l2_s.sort()
l2_s.sort(key = lambda l2_s:l2_s[1:])


print([" ".join(j) for j in l2_s] + [l1[i] for i in c])