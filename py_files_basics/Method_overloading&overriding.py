'''class student:  # method overloading indirectly
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a ='none',b ='none',c ='none'):
        s = 0
        if a!='none' and b!='none' and c!='none':
            s = a+b+c
        elif a!="none" and b!="none":
            s = a+b
        else:
            s = a
        return s

s1 = student(40,60)
print(s1.sum(6))
'''
class A:  # method overriding
    def show(self):
        print("In A class")
class B(A):
    def show(self):
        print("In B class")

q1 = B()
q1.show()
