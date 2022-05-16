class Libro:
    def __init__(self,titolo,autore):
        self.titolo = titolo
        self.autore = autore

    def getTitoloAutore(self):
        print("**************** getTitoloAutore ****************")
        return self.titolo + ", " + self.autore + '\n'

