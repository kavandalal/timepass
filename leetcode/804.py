#804

a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
print(len(a))

words=["rwjje","aittjje","auyyn","lqtktn","lmjwn"]

l1=''

lst=dict()

for i in words:
    for j in i:
        l=ord(j)-97
        l1+=a[l]
    l1 = ''.join(l1)
    print(l1)
    lst[l1]=0
    l1=''
    
print(len(lst))