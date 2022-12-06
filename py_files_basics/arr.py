from array import *
vals = array('i', [4,7,9,2,3]) # sorting array in ascending order
temp = 0
for a in range(0, len(vals)):
    for b in range(a+1, len(vals)):
        if vals[a] > vals[b]:
            temp = vals[a]
            vals[a] = vals[b]
            vals[b] = temp
print(vals)

arr = array("i", [5, 10])
x = int(input("enter the number for search"))
for i in range(0, len(arr)):
    if x == arr[i]:
        print("the number found at index", i)
        break
else:
    print("entered number not found")






