from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("its working")

class whiteboard(computer):
    def process(self):
        print("its writing")

class programmer:
    def work(self,com):
       print("solving bugs")
       com.process()



#com = computer()
com1 = laptop()
com2 = whiteboard()
#com2 = programmer()
#com1.process(com2)
prog1 = programmer()
#com1.process()
prog1.work(com2)