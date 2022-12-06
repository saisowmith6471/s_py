class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        #self.lap = self.laptop() # creating object of inner class laptop inside the outer class

    class laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu, self.ram)

s1 = student("sai", 158)
s2 = student("sowmith", 40121045)
#print(s1.lap.brand)  # priting object of inner class laptop

#print(s1.name, s1.id)
#print(s2.name, s2.id)
lap1 = student.laptop() # creating object for inner class outside the outer class (Easy for me)
lap1.show()