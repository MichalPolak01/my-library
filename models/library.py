from collections import Counter

class Library:
    """Klasa reprezentująca bibliotekę, zarządzająca kolekcją książek i użytkowników"""
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        """Dodaje książkę do kolekcji biblioteki"""
        self.books.append(book)

    def add_user(self, user):
        """Dodaje użytkownika do biblioteki"""
        self.users.append(user)

    def log_in(self, login, password):
        """Logowanie użytkownika"""
        for user in self.users:
            if user.check_credentials(login, password):
                print("Zalogowano pomyślnie.")
                return user
        print("Nieprawidłowy login lub hasło.")
        return None

    def browse_catalog(self):
        """Wyświetla katalog książek"""
        print("\n~ Katalog książek ~\n")
        for book in self.books:
            print(book)

    def borrow_book(self, user, book_title):
        """Metoda do wypożyczania książki z biblioteki"""
        for book in self.books:
            if book.title == book_title:
                try:
                    book.borrow()
                    self.loans.append({"user": user.id, "book": book.id})
                    user.borrowed_books.append(book.id)
                    print(f'Wypożyczono książkę: {book.title}')
                    return
                except ValueError as e:
                    print(e)
                    return
        print(f'Książka "{book_title}" nie została znaleziona w bibliotece.')

    def return_book(self, user, book_title):
        """Metoda do zwrotu książki do biblioteki"""
        for id in user.borrowed_books:
            for book in self.books:
                if book.id == id and book.title == book_title:
                    try:
                        book.return_book()
                        user.borrowed_books.remove(id)
                        self.loans = [loan for loan in self.loans if not (loan["user"] == user.id and loan["book"] == book.id)]
                        print(f'Zwrócono książkę: {book.title}')
                        return
                    except ValueError as e:
                        print(e)
                        return
        print(f'Nie znaleziono wypożyczenia dla książki "{book_title}".')

    def borrowed_books_by_user(self, user):
        """Zwraca listę książek wypożyczonych przez danego użytkownika z liczbą egzemplarzy"""
        book_counts = Counter(user.borrowed_books)
        return [f"{book.title} - {book.author} (Sztuk: {book_counts[book.id]})" for book in self.books if book.id in book_counts]