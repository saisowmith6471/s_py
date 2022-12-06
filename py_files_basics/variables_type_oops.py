class car:
    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.company = "Benz"


c1 = car()
c2 = car()

car.wheels = 6

print(c1.mileage, c1.company, c1.wheels) # can be car.wheels (i.e.class.<class var name>) It works
print(c2.mileage, c2.company, c2.wheels)

