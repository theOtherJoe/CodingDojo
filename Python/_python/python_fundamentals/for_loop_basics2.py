# #1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggieSize(aList):
    for j in range(len(aList)):
        if aList[j] > 0:
            aList[j] = "big"
    return aList
print(biggieSize([]))

# #2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# # (Note that zero is not considered to be a positive number).
def countPositives(listOfNums):
    count = 0
    for j in range(len(listOfNums)):
        if listOfNums[j] > 0:
            count += 1
    listOfNums[-1] = count
    return listOfNums
print(countPositives([]))

# #3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sumTotal(sickList):
    total = 0
    for j in range(len(sickList)):
        total += sickList[j]
    return total
print(sumTotal([]))

# #4 Average - Create a function that takes a list and returns the average of all the values.
def listAverage(sweetList):
    avg = 0
    total = 0
    for j in range(len(sweetList)):
        total += sweetList[j]
    avg = total / len(sweetList)
    return avg
print(listAverage([]))

# #5 Length - Create a function that takes a list and returns the length of the list.
def listLengthFinder(anotherList):
    return len(anotherList)
print(listLengthFinder([]))

# #6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have
# # the function return False.
def listMinimum(whoaList):
    if len(whoaList) < 1:
        return False
    else: 
        min = whoaList[0]
        for j in range(len(whoaList)):
            if whoaList[j] < min:
                min = whoaList[j]
        return min
print(listMinimum([]))

# #7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the
# # function return False.
def listMaximum(bigList):
    if len(bigList) < 1:
        return False
    else: 
        max = bigList[0]
        for j in range(len(bigList)):
            if bigList[j] > max:
                max = bigList[j]
        return max
print(listMaximum([]))

# #8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum,
# # maximum, and length of the list.
def ultimateAnalysis(wildList):
    sumTotal = 0
    minimum = wildList[0]
    maximum = wildList[0]
    for j in range(len(wildList)):
        sumTotal += wildList[j]
        if wildList[j] < minimum:
            minimum = wildList[j]
        if wildList[j] > maximum:
            maximum = wildList[j]
    average = sumTotal / len(wildList)
    new_dict = {
        'sumTotal': sumTotal,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': len(wildList)
    }
    return new_dict
print(ultimateAnalysis([]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a
# second list. (This challenge is known to appear during basic technical interviews).
def reverseMyList(lastList):
    return [lastList[j] for j in range(len(lastList)-1, -1, -1)]
print(reverseMyList([]))