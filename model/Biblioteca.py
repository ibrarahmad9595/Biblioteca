from model.Piano import Piano
from model.Scaffale import Scaffale
from model.Ripiano import Ripiano
from model.Libro import Libro

pia = Piano()
scaf = Scaffale()
rip = Ripiano()

class Biblioteca:
    def __init__(self):
        piano1 = []
        piano1.append(Piano())
        piano2 = []
        piano2.append(Piano())
        piano3 = []
        piano3.append(Piano())
        self.piani = [piano1, piano2, piano3]

    def getPiano(self, piano):
        return piano

    # ******************* R2: Inserimento libro nella biblioteca *******************
    def addBookToBiblioteca(self, piano, scaffale, ripiano, titolo, author):
        p = self.piani[piano - 1]
        s = p[0].scaffale["SC" + str(scaffale)]
        r = s.ripiano[ripiano-1]
        r.libro.append(Libro(titolo,author))
        print("a")

    def contiente(self, piano, scaffale, ripiano):
        pian = self.piani[piano - 1]
        scaffal = pian[0].scaffale["SC" + str(scaffale)]
        r = scaffal.ripiano[ripiano - 1]
        if len(r.libro)==0:
            print("Non c'e libro")
        elif len(r.libro)>0:
            print("----Si, trovato questi {} libri----".format(len(r.libro)))
            for l in r.libro:
                print(l.titolo,",",l.autore);

    # ******************* R3: Stampa contenuto scaffale *******************
    def getLibri(self, piano, scaffale):
        pian = self.piani[piano]
        scaffal = pian[0].scaffale["SC" + str(scaffale)]
        for index,x in enumerate(scaffal.ripiano):
            if len(scaffal.ripiano[x].libro) == 0:
                print("Non c'e libro in ripiano {}".format(index+1))
            elif len(scaffal.ripiano[x].libro) > 0:
                print("----Si, trovato questi {} libri in ripiano {}----".format(len(scaffal.ripiano[x].libro),index+1))
                for l in scaffal.ripiano[x].libro:
                    print("   ",l.titolo, ",", l.autore);

    # ******************* R4: Stampa posizione libro *******************
    def lib(self,titolo,autore):
        libro = self.cerca(titolo,autore)

    # ******************* R5: Ricerca di un libro *******************
    def cerca(self, titolo, autore):
        pianoo = 0
        for index,x in enumerate(self.piani):
            if index == pianoo:
                pianoo = pianoo + 1
                count_scaff = 0
                for s in x[0].scaffale:
                    count_rip = 0
                    count_scaff =count_scaff+1
                    if s=='SC'+str(count_scaff):
                            for r in x[0].scaffale['SC' + str(count_scaff)].ripiano:
                                if r==count_rip:
                                    if count_rip < 5:
                                        count_rip = count_rip + 1
                                    for l in x[0].scaffale['SC' + str(count_scaff)].ripiano[count_rip].libro:
                                        count_rip = count_rip + 1
                                        if titolo == l.titolo and autore ==l.autore:
                                            piano = pianoo
                                            scaffale = 'SC'+str(count_scaff)
                                            ripiano = count_rip
                                            print("\n--------Ho trovato un libro--------")
                                            print("Piano: {}, Scaffale: {}, Ripiano: {}, Titolo di libro: {}, Autore di libro: {}"
                                                  .format(piano,scaffale,ripiano,l.titolo,l.autore))

    # ******************* R6: Interfaccia utente *******************

