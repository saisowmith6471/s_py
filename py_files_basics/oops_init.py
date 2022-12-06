class computer:
    def __init__(self,cpu,ram): # init gets called automatically n times for n objects
        self.cpu = cpu  # assigning the arguments to the object
        self.ram = ram

    def config(self):
        print("cofig is:",self.cpu,self.ram)

comp1 = computer("i3",16) # computer () calls init instantly
comp2 = computer("i5", 8)

comp1.config()
comp2.config()

