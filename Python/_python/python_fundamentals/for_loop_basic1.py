### Basic For Loops ---> 
## Basic - Print all integers from 0 to 150
for j in range(151):
    print(j)

## Multiples of five - Print all of the multiples of 5 from 5 to 1,000
for j in range(5, 1000, 5):
    print(j)

## Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding
## Dojo".
for j in range(1, 100):
    if j % 5 == 0:
        print("Coding")
    elif j % 10 == 0:
        print("Coding Dojo")
    else:
        print(j)

## Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum.
sum = 0
for j in range(500000):
    if j % 2 != 0:
        sum += j
print(sum)

## Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for j in range(2018, 1, -4):
    print(j)

## Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the
# integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9 (on
# successive lines)
lowNum = 7
highNum = 77
mult = 5
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1