'''class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is :",self.cpu,self.ram)

c1 = computer("dell","16GB")
c2 = computer("12",8)
c1.config()
c2.config()
'''
'''class computer:
    def __init__(self):
        self.name = "sai"
        self.age = 28
    def update(self): # object variable
        self.age = 29
    def compare(self,other):
        if c1.age == c2.age:
            return True
        else:
            return False

c1 = computer()
c2 = computer()

c2.name = "sunny"
c2.age = 29

c1.update()

if c1.compare(c2):
    print("The age is same")
else:
    print("The age is different")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
'''

'''class car:
    wheels = 4  # class variables
    def __init__(self):
        self.mil = 15    # mil and brand are instance variables
        self.brand = "Honda"

c1 = car()
c2 = car()
c2.brand = "Hero"
car.wheels = 3
print(c1.mil, c1.brand, c1.wheels)
print(c2.mil, c2.brand, c2.wheels)
'''

class student:
    school = "telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def stat():
        print("This is a static method")
#    def get_m3(self):
 #       return self.m3
 #   def set_m2(self , value):
 #       self.m2 = value

s1 = student(39,43,76)
s2 = student(56,92,34)

#s2.m3 = 100
#print(s2.m3)
#print(s2.get_m3())
#print(s2.set_m2(200))
print(student.getschool())
student.stat()



