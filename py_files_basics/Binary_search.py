# IN Binary search all values are sorted
# sorting is done by placing first value at lower bound (l) and last value at upper bound (u)
pos = 0
def search(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False


list = [34,56,65,78,98]
n = 78

if search(list,n):
    print("value found at position:", pos+1)
else:
    print("value not found")