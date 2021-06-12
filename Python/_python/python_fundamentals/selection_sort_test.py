someArray = [3,7,5,9,1,4,2,8,6,0]
def selectionSort(arr):
    count = 0
    while count < len(arr): 
        for i in range(count,len(arr)):
            if arr[i] < arr[count]:
                arr[i], arr[count] = arr[count], arr[i]
        count += 1
    return arr
print(selectionSort(someArray))