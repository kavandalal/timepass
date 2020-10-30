def bubble(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=input('Enter the numbers in Bubble sort \n').split()
a = [int(i) for i in a]
print(a)
bubble(a)
print(a)

# 1 64 1 984 165 16874897 13 5132489 413