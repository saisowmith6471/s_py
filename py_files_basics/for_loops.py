'''for i in range(1,50):
    if i**2 <= 50:
        print(i**2)


num = int(input("Enter the number")) # Checking if the given number is prime or not
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
        continue

if count == 2:
            print("The number is prime")
else:
            print("The number is not prime")

for num in range(2,101): # printing series of prime numbers
    if all(num%i!=0 for i in range(2,num)):
       print (num)


a = 0  # fbonacci series
b = 1
print(a)
print(b)
i = 1
while i <= 10:
    res = a + b
    print(res, end=",")
    a = b
    b = res
    i += 1

# printing patterns another logic
for i in range(4):
    for j in range(4 - i):
        print("#", end=" ")
    print()

x = [1,2,3,4] # printing patterns logic for different numbers
for i in range(4):
    for j in range(4-i):
        print(x[j], end=" ")
    x.pop(0)
    print()

x = ['A','P','Q','R']
y = ['B','C','D']
for i in range(4):
    for j in range(4):
        print(x[j], end=" ")
    print()
    if i < 3:
        x.pop(i + 1)
        x.insert(i + 1, y[i])
    else:
        break
'''
nums = [11,21,12,33,41]  # for else example
for i in nums:
    if i % 5 ==0:
        print(i)
        break
else:
    print("not found")







