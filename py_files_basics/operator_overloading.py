class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    def __gt__(self, other):
        c1 = self.m1 + self.m2
        c2 = other.m1 + other.m2
        if c1 > c2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)


s1 = student(50, 95)
s2 = student(51, 100)

#s3 = s1 + s2

#print(s3.m1)
if s1 > s2:
    print("S1 is greater")
else:
    print("S2 is greater")

#print(s1)
print(s2)
