class pycharm:
    def execute(self):
        print("compiling")
        print("running")

class myeditor:
    def execute(self):
        print("sais editor")
class laptop:
    def code(self,ide):
        ide.execute()

ide = myeditor() #ide is of type myeditor()
lap = laptop()
lap.code(ide)