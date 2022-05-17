from model.Biblioteca import Biblioteca

biblioteca = Biblioteca()
class GestioneBiblio:
    def __init__(self):
        pass

    def start(self):
        print("************GestioneBibilio**************")
        ans = True
        while ans:
            choice = input("""
                             1: '"add": inserimento libro, seguito dai parametri autore, titolo, piano, scaffale e ripiano',
                             2: '"list": stampa contenuto scaffale, seguito dai parametri piano e scaffale',
                             3: '"libro": ricerca un libro e stampa la posizione: seguito dai parametri autore e titolo',
                             4: 'quit',
    
                              Please enter your choice: """)

            if choice == "1":
                piano = input("Enter Piano: ")
                scaffale = input("Enter Scaffale: ")
                ripiano = input("Enter Ripiano: ")
                titolo = input("Enter the book Titolo")
                author = input("Enter the book Authore")
                biblioteca.addBookToBiblioteca(int(piano),int(scaffale),int(ripiano),titolo,author)
            elif choice == "2":
                piano = input("Enter Piano: ")
                scaffale = input("Enter Scaffale: ")
                biblioteca.getLibri(int(piano), int(scaffale))
            elif choice == "3":
                titolo = input("Enter the book title")
                authore = input("Enter the book author")
                biblioteca.cerca(titolo,authore)
            elif choice == "4":
                return
            else:
                print("You must only select either 1, 2, 3 or 4")
                print("Please try again")