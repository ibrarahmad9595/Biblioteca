from model.Biblioteca import Biblioteca
from model.GestioneBiblio import GestioneBiblio
from model.Piano import Piano
from model.Libro import Libro

# ****************** R1: Dati del Libro ******************
libro2 = Libro("java","James Gosling", 3)
titolo_autore2 = libro2.getTitoloAutore();
print(titolo_autore2)

print("******************* R2: Inserimento libro nella biblioteca *******************")
biblioteca = Biblioteca()
biblioteca.addBookToBiblioteca(2,2,3,"Python","Guido van rossow")
biblioteca.addBookToBiblioteca(2,2,3,"Java","James Gosling")
biblioteca.addBookToBiblioteca(2,2,3,"c++","Bjarne Stroustrup")
biblioteca.addBookToBiblioteca(2,2,3,"Ruby","Yukihiro Matsumoto")

biblioteca.contiente(2,2,3)

print("\n******************* R3: Stampa contenuto scaffale *******************")
lib = biblioteca.getLibri(1,2);


print("\n******************* R4: Stampa posizione libro *******************")
libro = biblioteca.piani[1].scaffale['SC2'].ripiano[2].libro[0]
rrr = libro.getRipiano()
ppp = libro.getPiano()
sss = libro.getScaffale()

print("\n******************* R5: Ricerca di un libro *******************")
biblioteca.cerca("Python","Guido van rossow")
