myArr = [6,5,3,1,8,7,2,4]
def bubbleSort(myArr):
    for j in range(len(myArr)-1):
        for i in range(len(myArr)-1-j):
            if myArr[i] > myArr[i+1]:
                myArr[i], myArr[i+1] = myArr[i+1], myArr[i]
    return myArr
print(bubbleSort(myArr))