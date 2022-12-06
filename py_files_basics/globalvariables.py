'''a = 10                    # changing the value of the global variables without changing local variables
def fun():
    a = 8
    x = globals()['a']
    print("a in fun", a)
    globals()['a'] = 20

fun()
print("a outside fun", a)
'''

# program to take input from users and display the names equal or greater than size 5
n = int(input("enter the size of list"))
lst = []
count  = 0

for i in range(n):
    x = input("enter the name")
    # lst.append(x)

def name():
    global count
    for i in lst:
        if len(i) >= 5:
            count+=1
        else:
            continue
    return count


count1 = name()
print(count1)







