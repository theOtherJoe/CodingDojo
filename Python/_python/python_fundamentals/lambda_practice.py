# create a list
my_arr = [1,2,3,4,5]
# define a function that squares values
def square(num):
    return num ** 2
# invoke map function
print(list(map(square, my_arr)))

my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) 
############################################

class Underscore:
    def map(self, list, callback):
        for j in range(len(list)):
            list[j] = callback(list[j])
        return print(list)

    def find(self, list, callback):
        for b in range(len(list)):
            if callback(list[b]) == True:
                return print(list[b])
    def filter(self, list, callback):
        new_list = []
        for r in range(len(list)):
            if callback(list[r]) == True:
                new_list.append(list[r])
        return print(new_list)

    def reject(self, list, callback):
        final_list = []
        for r in range(len(list)):
            if callback(list[r]) == False:
                final_list.append(list[r])
        return print(final_list)

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)

_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]