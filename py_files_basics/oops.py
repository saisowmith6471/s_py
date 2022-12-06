class computer:
    def config(self): # defining method
        print("i5", "16gb", "1 TB")

# object creation
comp1 = computer() # comp1 is an object of class (computer)
comp2 = computer()

computer.config(comp1) # method calling ( only for understanding purpose and we don't call like this)
computer.config(comp2)

comp1.config() # method calling using the object itself. Normal way of calling




