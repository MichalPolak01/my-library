
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
        self.requests_for_extension = []

    def menu(self):
        """Metoda menu dla czytelnika, wyświetlająca dostępne opcje"""
        print(f"Menu czytelnika {self.login}:")
        print("1. Przeglądaj katalog książek")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Moje wypożyczenia")


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
