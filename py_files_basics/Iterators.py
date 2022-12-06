'''nums = [3,4,5,6]

it = iter(nums)
print(it.__next__()) # way of how iter works in the backend
print(it.__next__())
print(next(it)) # another way of how iter works in backend
'''
# the above is by using the in built functions
# we can do that by using our own functions or methods. to define method we need a class.
class topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

c1 = topten()
print(next(c1)) # print 1 ad again 1 is not printed in the for loop as the iterator stores prev value
for i in c1:
    print(i)

