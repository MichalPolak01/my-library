class User:
    """Klasa reprezentująca użytkownika systemu bibliotecznego"""
    _id_counter = 1

    def __init__(self, login, password, role):
        """Inicjalizacja obiektu użytkownika"""
        self.id = self._id_counter
        User._id_counter += 1
        self.login = login
        self.password = password
        self.role = role

    def check_credentials(self, login, password):
        """Metoda logowania użytkownika"""
        if self.login == login and self.password == password:
            return True
        return False

    def menu(self):
        """Metoda menu, która powinna być zaimplementowana w klasach potomnych"""
        raise NotImplementedError("Metoda menu() musi być zaimplementowana w klasie potomnej.")

    def __str__(self):
        """Reprezentacja tekstowa użytkownika"""
        return f"User(login='{self.login}', role='{self.role}')"
    
    def __repr__(self):
        """Reprezentacja debugowania użytkownika"""
        return f"User(login='{self.login}', role='{self.role}')"
    

class Reader(User):
    """Klasa reprezentująca czytelnika, dziedzicząca po klasie User"""

    def __init__(self, login, password):
        """Inicjalizacja obiektu czytelnika"""
        super().__init__(login, password, role='reader')
        self.borrowed_books = []

    def menu(self, library):
        """Metoda menu dla czytelnika, wyświetlająca dostępne opcje"""
        while True:
            print(f"\n ~~ Menu czytelnika {self.login} ~~\n")
            print("1. Przeglądaj katalog książek")
            print("2. Wypożycz książkę")
            print("3. Zwróć książkę")
            print("4. Moje wypożyczenia")
            print("5. Wyloguj")
            option = input("Wybierz opcję: ")

            match option:
                case "1":
                    library.browse_catalog()
                case "2":
                    print("\n~ Wypożyczanie książki ~\n")
                    book_title = input("Podaj tytuł książki: ")
                    library.borrow_book(self, book_title)
                case "3":
                    print("\n~ Zwracanie książki ~\n")
                    book_title = input("Podaj tytuł książki do zwrotu: ")
                    library.return_book(self, book_title)
                case "4":
                    print("\nTwoje wypożyczenia:")
                    for book in library.borrowed_books_by_user(self):
                        print(book)
                case "5":
                    print("Wylogowano.")
                    break
                case _:
                    print("Nieprawidłowa opcja. Spróbuj ponownie.")

class Librarian(User):
    """Klasa reprezentująca bibliotekarza, dziedzicząca po klasie User"""

    def __init__(self, login, password):
        """Inicjalizacja obiektu bibliotekarza"""
        super().__init__(login, password, role='librarian')

    def menu(self):
        """Metoda menu dla bibliotekarza, wyświetlająca dostępne opcje"""
        print(f"Menu bibliotekarza {self.login}:")
        print("  1. Lista wszystkich wypożyczeń")
        print("  2. Prośby o przedłużenie")
