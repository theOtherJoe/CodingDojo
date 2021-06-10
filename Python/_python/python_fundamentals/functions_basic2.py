#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element).
def countdown(num):
    new_list = []
    for j in range(num, -1, -1):
        new_list.append(j)
    return new_list
print(countdown())

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printAndReturn(aList):
    for j in aList:
        print(aList[0])
        return aList[1]
print(printAndReturn([]))

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's
# length.
def firstPlusLength(anyList):
    finalVal = anyList[0] + len(anyList)
    return finalVal
print(firstPlusLength([]))

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the
# original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has
# less than 2 elements, have the function return false.
def valuesGreaterThanSecond(anotherList):
    anotherNewList = []
    count = 0
    if len(anotherList) > 2:
        for j in anotherList:
            if j > anotherList[1]:
                anotherNewList.append(j)
                count += 1
        print(count)
    else:
        return False
    return anotherNewList
print(valuesGreaterThanSecond([]))

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create
# and return a list whose length is equal to the given size, and whose values are all the given value.
def thisLengthThatValue(size, value):
    finalList = []
    for j in range(size):
        finalList.append(value)
    return finalList
print(thisLengthThatValue())