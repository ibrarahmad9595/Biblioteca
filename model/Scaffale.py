from model.Ripiano import Ripiano
class Scaffale:
    def __init__(self,piano):
        self.ripiano = {}
        self.piano = piano
        for x in range(6):
            self.ripiano[x] = Ripiano(self)

