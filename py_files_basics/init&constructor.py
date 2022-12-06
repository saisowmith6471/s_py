class computer:

    def __init__(self):
        self.name = "sai"
        self.age = 28
    def update(self):  # self  (updating age)
        self.age = 30
    def compare(self,other):  # compare
       if self.age == other.age:
           return True
       else:
           return False

c1 = computer()
c2 = computer()

c1.name = "sowmith"  # changing the name and age
c1.age = 29

c2.update()

if c1.compare(c2):
    print("the age is same")
else:
    print("the age is not same")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)





