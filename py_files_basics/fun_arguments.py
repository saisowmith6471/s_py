'''def update(lst):
    lst[0] = 2
    print("updated lst=", lst)
    print(id(lst))
lst = [10,20,30]
update()
print("lst =", lst)
print(id(lst))


def sum(a, *b):  # variable length (types of arguments)
    print(a)
    print(b)
    c = 0
    for i in b:
        c = c + i
    print(c)
sum(3,4,5,6,7,8,9)
'''

def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person("sai", age = 28, city = "kurnool")


