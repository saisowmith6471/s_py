'''def fact(n): # factorial of a number
    f = 1
    for i in range(2,n+1):
        f = f * i
    return f
f = fact(4)
print(f)
'''

def bact(n):
    if n==0:
        return 1
    return n * bact(n-1)
result = bact(5)
print(result)
