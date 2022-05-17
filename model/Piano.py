from model.Scaffale import Scaffale
class Piano:
    def __init__(self):
        self.scaffale = {}
        for x in range(1,31):
            self.scaffale["SC{}".format(x)] = Scaffale(self)









