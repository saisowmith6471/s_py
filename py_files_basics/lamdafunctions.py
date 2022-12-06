# filter function using normal function
'''def is_even(n):
    return n%2==0
nums = [2,4,6,5,3,12,3]
evens = list(filter(is_even,nums))
print(evens)
'''

# filter function using lambda
from functools import reduce
nums = [2,4,6,5,3,12,2]
#evens = list(filter(lambda n : n%2==0,nums)) # filter
doubles = list(map(lambda n : n+2,nums)) # map
sum = reduce(lambda a,b : a+b, nums) # reduce
#print(evens)
#print(doubles)
print(sum)



