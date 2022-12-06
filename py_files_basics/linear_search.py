pos = 0
def search(list, n):        #linear search using for loop ( using while loop explained in tutorial)
    for i in list:
        if list[i] == n:
            globals()['pos'] = i
            return True
        else:
            continue

list = [2,5,6,8,4]
n = 6
if search(list,n):
    print("value found", pos+1)
else:
    print("not found")