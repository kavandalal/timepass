#205

s="aba"
t="baa"

d1 ={}
d2 ={}
#d[z]=d.get(z,0)+1

for i,j in enumerate(s):
    if j not in d1:
        d1[j]=i
    print(d1[j])
for i,j in enumerate(t):
    if j not in d2:
        d2[j]=i
    print(d2[j])
if [d1[j] for i,j in enumerate(s)] == [d2[j] for i,j in enumerate(t)]:
    print(True)
else:
    print(False)