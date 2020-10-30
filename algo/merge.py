import random 
def mer(arr):
    if len(arr)>1:
        mid= len(arr)//2
        L = arr[:mid]
        R= arr[mid:]
        mer(L)
        mer(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
        

a=input('Enter the numbers in Merge sort \n').split()
a = [int(i) for i in a]
print(a)
#l= random.sample(range(0,20),random.randint(1,20)) # making a random list 
#print(l)
mer(a)

print(a)


# 1 2 3 4 5 6 7 8 9 0