anotherArray = [5,3,7,8,0,9,2,4,6,1]
def insertionSort(arr):
    for j in range(1, len(arr)):
        curr_item = arr[j]
        count = j
        while count > 0 and arr[count -1] > curr_item:
            arr[count] = arr[count -1]
            count -= 1
        arr[count] = curr_item
    return arr
print(insertionSort(anotherArray))