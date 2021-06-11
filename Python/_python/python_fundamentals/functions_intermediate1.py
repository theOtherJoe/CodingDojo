import random
def randInt(min=" ", max=" "):
    if min != " " and max != " ":
        print("You gave me both inputs!")
        return int(random.random() * (max - min) + min)
    elif max != " ":
        print("I'm running the max block")
        return int(random.random() * max)
    elif min != " ":
        print("I'm running the min block")
        return int(random.random() * min + (100 - min)) # return a random integer between the min number and 100
    else:
        print("Hit the catch all.")
        return int(random.random() * 100)
print(randInt())