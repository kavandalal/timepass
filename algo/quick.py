def part(low,high):
    pivot = a[low]
    i=low+1
    j= high
    while i < j:
        while a[i] < pivot and i<high:
            i+=1
        while a[j] > pivot and j>low:
            j-=1
        if i < j:
            a[i],a[j]=a[j],a[i]
    if a[low] > a[j]:
        a[low],a[j]=a[j],a[low]
    return j 

def quicksort(low,high):
    if low < high:
        pi = part(low,high)
        quicksort(low,pi-1)
        quicksort(pi+1,high)
        
a=input('Enter the numbers in Quick sort \n').split()
a = [int(i) for i in a]
print(a)
l= 0
h= len(a)-1
quicksort(l,h)

print(a)
# 5 2 4 3 1 7 24 50 1
# 54 13213 265 531 31 01 4 68413 1 31 2 256 98 16