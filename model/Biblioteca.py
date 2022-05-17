from model.Piano import Piano
from model.Scaffale import Scaffale
from model.Ripiano import Ripiano
from model.Libro import Libro

class Biblioteca:
    def __init__(self):
        piano1 = Piano()
        piano2 = Piano()
        piano3 = Piano()
        self.piani = [piano1, piano2, piano3]

    # ******************* R2: Inserimento libro nella biblioteca *******************

    def addBookToBiblioteca(self, piano, scaffale, ripiano, titolo, author):
        p = self.piani[piano - 1]
        s = p.scaffale["SC" + str(scaffale)]
        r = s.ripiano[ripiano - 1]
        r.libro.append(Libro(titolo, author, r))

    def contiente(self, piano, scaffale, ripiano):
        pian = self.piani[piano - 1]
        scaffal = pian.scaffale["SC" + str(scaffale)]
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
        scaffal = pian.scaffale["SC" + str(scaffale)]
        for index,x in enumerate(scaffal.ripiano):
            if len(scaffal.ripiano[x].libro) == 0:
                print("Non c'e libro in ripiano {}".format(index+1))
            elif len(scaffal.ripiano[x].libro) > 0:
                print("----Si, trovato questi {} libri in ripiano {}----".format(len(scaffal.ripiano[x].libro),index+1))
                for l in scaffal.ripiano[x].libro:
                    print("   ",l.titolo, ",", l.autore);

    # ******************* R4: Stampa posizione libro *******************
        # Refer Python file libro

    # ******************* R5: Ricerca di un libro *******************
    def cerca(self, titolo, autore):
        for index_piano, piano in enumerate(self.piani):
            for index_scaf, scaffale in enumerate(dict(piano.scaffale)):
                for index_rip, ripiano in enumerate(dict(piano.scaffale[scaffale].ripiano)):
                    for libro in piano.scaffale[scaffale].ripiano[ripiano].libro:
                        if libro.titolo == titolo and libro.autore == autore:
                            print("\n--------Ho trovato un libro--------")
                            print("Piano: {}, Scaffale: {}, Ripiano: {}, Titolo di libro: {}, Autore di libro: {}"
                                  .format(index_piano+1,index_scaf+1,index_rip+1,libro.titolo,libro.autore))
