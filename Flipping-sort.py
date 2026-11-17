def flip(arr,i):
    start=0
    while start<i:
        aux=arr[start]
        arr[start]=arr[i]
        arr[i]=aux
        start+=1
        i-=1

def findMax (arr,n):
    max=0
    for i in range (0,n):
        if arr[i]>arr[max]:
            max=i
    return max

def flippingsort(arr,n):
    current_size = n
    while current_size > 1:
        max = findMax(arr,current_size)
        if max != current_size-1:
            flip(arr,max)
            flip(arr,current_size-1)
        current_size-=1

def printArray (arr,n):
    for i in range (0,n):
        print ("%d"%(arr[i]),end=" ")

arr=[23,10,9,65,45,3,31,12]
n=len(arr)
flippingsort(arr,n)
print("Sirul sortat: ")
printArray(arr,n)