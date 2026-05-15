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

    def request_extension(self, user, book_title):
        """Dodaje prośbę o przedłużenie wypożyczenia książki"""
        for book in self.books:
            if book.title == book_title and book.id in user.borrowed_books:
                self.loans.append({"user": user.id, "book": book.id, "request": "extension"})
                print(f"Dodano prośbę o przedłużenie dla książki: {book.title}")
                return
        print(f"Nie znaleziono książki o tytule '{book_title}' w Twoich wypożyczeniach.")

    def handle_extension_requests(self):
        """Obsługuje prośby o przedłużenie wypożyczeń"""
        requests = [loan for loan in self.loans if loan.get("request") == "extension"]
        if not requests:
            print("Brak próśb o przedłużenie.")
            return

        for request in requests:
            user = next((u for u in self.users if u.id == request["user"]), None)
            book = next((b for b in self.books if b.id == request["book"]), None)
            if user and book:
                print(f"Prośba o przedłużenie: {book.title} - {user.login}")
                decision = input("Zaakceptować (t/n)?  ")
                if decision.lower() == "t":
                    print(f"Przedłużono wypożyczenie książki: {book.title}")
                else:
                    print(f"Odrzucono prośbę o przedłużenie książki: {book.title}")
                self.loans.remove(request)

    def borrowed_books_by_user(self, user):
        """Zwraca listę książek wypożyczonych przez danego użytkownika z liczbą egzemplarzy"""
        book_counts = Counter(user.borrowed_books)
        return [f"{book.title} - {book.author} (Sztuk: {book_counts[book.id]})" for book in self.books if book.id in book_counts]
    
    def list_loans(self):
        """Wyświetla listę wszystkich wypożyczeń w bibliotece"""
        if not self.loans:
            print("Brak wypożyczeń.")
            return

        print("\n~ Lista wypożyczeń ~\n")
        for loan in self.loans:
            if loan.get("request") == "extension":
                continue  # Pomijamy prośby o przedłużenie
            
            user = next((u for u in self.users if u.id == loan["user"]), None)
            book = next((b for b in self.books if b.id == loan["book"]), None)
            if user and book:
                print(f"{user.login} wypożyczył: {book.title} - {book.author}")