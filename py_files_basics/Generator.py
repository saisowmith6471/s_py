'''def fun():
    yield 5
values = fun()
print(values) # prints the address of the function
print(values.__next__()) # prints the value of the function
'''
def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1
values = topten()
for i in values:
    print(i)


