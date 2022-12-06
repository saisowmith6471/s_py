from numpy import *
'''arr = array([1,2,3,4])
#new_arr = array([a*5 for a in arr]) # multiplying array with a number: method 1
arr = arr * 5 # multiplying array with a number: method 2

print(arr)


arr1 = array([1,2,3,4]) # program to add 2 arrays using for loop
arr2 = array([2,3,4,5])
arr3 = []
for i in range(0,4):
    arr3.append(arr1[i] + arr2[i])
print(arr3)
'''


arr = array([20,31,42,12,11,7]) # print maximum value without using in-built function
for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            continue
print("maximum value is", arr[i+1])









