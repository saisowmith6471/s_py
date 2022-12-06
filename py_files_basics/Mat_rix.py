from numpy import *
'''arr = array([
              [1,2,3,4,5,6,7,8,9],
            [7,8,9,10,11,12,13,14,15]
])
arr2 = arr.reshape(2,3,3)

print(arr2)

m = matrix('1 2 3 ; 4 5 6 ; 6 7 8')
print(diagonal(m))
print(m * m)'''

m1 = matrix('1 2 3 ; 4 5 6')
m2 = matrix('7 8 ; 9 10 ; 11 12')
print(m1.dot(m2))

'''A = array([
    [1,2,3],
    [5,6,7]
])
B = array([
    [3,4,5],
    [5,8,7],
    [3,6,1]
])
result = array([
    [0,0,0],
    [0,0,0]
])
for m in range(len(A)): # iterate through rows of A
   for n in range(len(B[0])): # iterate through columns of B
          for o in range(len(B)): # iterate through rows of B
               result[m][n] += A[m][o] * B[o][n]
for res in result:
   print(res)'''






