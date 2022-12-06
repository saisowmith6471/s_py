class A:
    def __init__(self):
        print("This is A")
    def feature1(self):
        print("this is 1-A")
    def feature2(self):
        print("this is 2")

class B:
    def __init__(self):
        #super().__init__()  # calls the constructor of A too
        print("This is B")
    def feature1(self):
        print("this is 1-B")
    def feature4(self):
        print("this is 4")

class C(A,B):
    def __init__(self):
        super().__init__()  # MRO concept
        print("This is c")
    def sup_feat(self):
        super().feature2()  # Calling function with super() class
c1 = C()
c1.feature1()
c1.sup_feat()






