class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for j in nums:
            self.result += j
        self.result += num
        return self
    def subtract(self, num, *nums):
        for y in nums:
            self.result -= y
        self.result -= num
        return self

# create an instance:
md = MathDojo()

# to test:
x = md.add(2).add(2,5,1).add(15).add(4,16,2).subtract(3,2).subtract(4,2,3).subtract(10).result
print(x)