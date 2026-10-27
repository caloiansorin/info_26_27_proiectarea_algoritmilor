def partition(array, low, high):
    pivot=array[high]
    i=low-1
    for j in range (low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]

    array[i+1],array[high]=array[high],array[i+1]

    return i+1

def quick_sort(array,low,high):
    if low<high:
        idx=partition(array,low,high)

        quick_sort(array,low,idx-1)
        quick_sort(array,idx+1,high)

def print_arr(arr,n):
    for i in range (n):
        print(arr[i],end=" ")
    print()

arr=input("Introdu elementele: ").split()
for i in range(len(arr)):
    arr[i]=int(arr[i])

quick_sort(arr,0,len(arr)-1)

print ("Sirul sortat este: ")
print_arr(arr,len(arr))