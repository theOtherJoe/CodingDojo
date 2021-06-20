import unittest
#1 reverseList - Write a function that reverses the values in the list (without creating a temporary array)
def reverseTheList(arr):
    for i in range(int(len(arr)/2)):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr

#2 isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backwards).
def isPalindrome(word):
    back_word = ""
    for j in word:
        back_word = j + back_word
    if back_word == word:
        return True
    else:
        return False

#3 coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for change where
# you minimize the number of coins you give out
def coins(num):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    remainder = num % 25
    if remainder == 0:
        quarters = int(num / 25)
        return [quarters, dimes, nickels, pennies]
    elif remainder != 0:
        quarters = int(num / 25)
        new_remainder = remainder % 10
        if new_remainder == 0:
            dimes = int(remainder / 10)
            return [quarters, dimes, nickels, pennies]
        elif new_remainder != 0:
            dimes = int(remainder / 10)
            if new_remainder % 5 == 0:
                nickels = int(new_remainder / 5)
                return [quarters, dimes, nickels, pennies]
            elif new_remainder % 5 != 0:
                nickels = int(new_remainder / 5)
                pennies = new_remainder % 5
    return [quarters, dimes, nickels, pennies]

class ReverseTheListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseTheList([5,4,3,2,1]), [1,2,3,4,5])
    def testTwo(self):
        self.assertEqual(reverseTheList([7,4,5,2]), [2,4,5,7])
    def testThree(self):
        self.assertEqual(reverseTheList([12,4,15,6]), [6,15,4,12])
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

class IsPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isPalindrome("testing"), False)
    def testTwo(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testThree(self):
        self.assertTrue(isPalindrome("tacocat"))
    def testFour(self):
        self.assertTrue(isPalindrome("deified"))
    def testFive(self):
        self.assertFalse(isPalindrome("fried"))
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

class CoinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(124), [4,2,0,4])
    def testTwo(self):
        self.assertEqual(coins(12), [1,1,0,2])
    def testThree(self):
        self.assertEqual(coins(38), [1,1,0,3])
    def testFour(self):
        self.assertEqual(coins(205), [8,0,0,0])
    def testFive(self):
        self.assertEqual(coins(177), [7,0,0,2])
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests