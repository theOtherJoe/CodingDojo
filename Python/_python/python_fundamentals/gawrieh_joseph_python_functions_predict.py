#1
def a():
    return 5
print(a())
## This function will return 5 and print 5

#2
def a():
    return 5
print(a()+a())
## This function will return 5, and when invoked with print() will print 10

#3
def a():
    return 5
    return 10
print(a())
## This function will return 5 (not 10) and print 5

#4
def a():
    return 5
    print(10)
print(a())
## This function will return 5 and print 5

#5
def a():
    print(5)
x = a()
print(x)
## This function will print 5 when invoked but will return None since it's not explicitly returning a value

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
## This function will print 3 and 5 when invoked, but will (I think) error out because nothing is explicitly being returned, so
# it will try to add None + None

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
## This function will convert the integer arguments to strings, and concatenate them, returning 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
	    return 10
    return 7
print(a())
## This function will print 100, then will return 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
## This function will, on the first invokation, return 7; on the second it will return 14; the third it will return 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
## This function will return 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
## This block of code will print 500 as print is being called before the function, then will also print 500 again since the
# function has yet to be called, then it will print 300 since the function was called, then lastly will print 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
## This block of code will print 500, then print 500 again since a() hasn't been invoked, then will print 300, then print 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
## This block of code will print 500, print 500 again, then print 300 and lastly return 300 (and print it)

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
## This function will print 1, print 3, and lastly print 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
## This function will print 1, print 3, then print 5, lastly it will print 10