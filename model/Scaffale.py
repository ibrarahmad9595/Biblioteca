from model.Ripiano import Ripiano
class Scaffale:
    def __init__(self):
        self.ripiano = {}
        for x in range(6):
            self.ripiano[x] = Ripiano()

    def getRipiano(self,ripiano):
        return ripiano