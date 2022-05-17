class Libro:
    def __init__( self, titolo, autore, ripiano):
        self.titolo = titolo
        self.autore = autore
        self.ripiano = ripiano

    def getTitoloAutore(self):
        print("**************** getTitoloAutore ****************")
        return self.titolo + ", " + self.autore + '\n'

    def getPiano(self):
        return self.ripiano.scaffale.piano

    def getScaffale(self):
        return self.ripiano.scaffale

    def getRipiano(self):
        return self.ripiano
