from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = hello()
t2 = hi()

t1.start() # start method calls the run internally bcoz the thread class is having run method by default.
t2.start()

t1.join() # join makes main thread wait till t1 and t2 get completed its execution
t2.join()
print("bye")
