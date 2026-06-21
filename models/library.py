from collections import Counter
from models.book import Book

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
        
        books = list(self.books)
        self.catalog_menu(books)

        return

    def catalog_menu(self, books : list[Book]):
        while True:
            print("\n\n1. Wyszukaj ksiąkę")
            print("2. Pokaż tylko dostępne książki")
            print("3. Sortowanie")
            print("4. Wyczyść filtry i sortowanie")
            print("5. Wyjdź")
            option = input("Wybierz opcję: ")

            match option:
                case "1":
                    print("\nWyszukiwanie")
                    phase = input("Podaj frazę z tytuł lub autora książki: ")
                    books = [b for b in books if phase.lower() in b.title.lower() or phase.lower() in b.author.lower() ]
                case "2":
                    print("\nFiltrowanie")
                    books = list(filter(lambda b : b.available_quantity > 0, books))
                case "3":
                    print("\nSortowanie")
                    sort_option = input("Wybierz opcję sortowania (1 - tytuł, 2 - autor, 3 - dostępne sztuki): ")
                    arg = ""
                    if sort_option == "1":
                        arg = "title"
                    elif sort_option == "2":
                        arg = "author"
                    elif sort_option == "3":
                        arg = "available_quantity"
                    else:
                        print("Nieprawidłowa opcja sortowania.")
                        continue
                    # books = sorted(books, key=lambda b : getattr(b, arg))
                    books = self.display_collection(
                        books,
                        sort_key=lambda b: getattr(b, arg)
                    )
                case "4":
                    books = list(self.books) 
                case "5":
                    break
                case _:                    
                    print("Nieprawidłowa opcja. Spróbuj ponownie.")
                    pass 

            print("\n\n~ Katalog książek ~\n")
            for book in books:
                print(book)

    def display_collection(self, items, predicate=None, sort_key=None):
        """Funkcja wyższego rzędu - wyświetla kolekcję z filtrem i sortowaniem"""
        result = [item for item in items if predicate(item)] if predicate else items
        result = sorted(result, key=sort_key, reverse=True) if sort_key else result
        
        return result

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
                    loan_request = input("Czy chcesz wysłać prośbę o rezerwację? (T/N): ")
                    if loan_request.lower() == "t":
                        book.request_for_loan()
                        user.reservation_requests.append(book.id)
                        print(f'Wysłano prośbę o rezerwację dla książki: {book.title}')
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
                print(f"Prośba o przedłużenie: {book.title} - {user.login} - liczba rezerwacji: {book._loans_requests}")
                decision = input("Zaakceptować (t/n)?  ")
                if decision.lower() == "t":
                    print(f"Przedłużono wypożyczenie książki: {book.title}")
                else:
                    print(f"Odrzucono prośbę o przedłużenie książki: {book.title}")
                self.loans.remove(request)

    def requested_books_by_user(self, user):
        """Zwraca listę książek zarezerwowanych przez danego użytkownika z liczbą egzemplarzy"""
        book_counts = Counter(user.reservation_requests)
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

    def library_stats(self):
        """Wyświetla statystyki biblioteki"""
        
        print("\n\n1. Najpopularniejsza ksiązka")
        print("2. Liczba aktywnych wypozyczen")
        print("3. Lista czytelników")
        print("4. Zamknij statystyki")
        stat_option = input("Podaj opcje: ")

        match stat_option:
            case "1":
                values = {b.title: b.total_quantity - b.available_quantity for b in self.books}
                max_val = max(values.values(), default=0)
                best = [title for title, val in values.items() if val == max_val]
                print(f"Najpopularniejsza książka: {', '.join(best)} ({max_val} wypożyczeń)")
            case "2":
                active = [loan for loan in self.loans if loan.get("request") != "extension"]
                print(f"Liczba aktywnych wypożyczeń: {len(active)}")
            case "3":
                reader_list = sorted(
                    ((u.login, len(u.borrowed_books)) for u in self.users if hasattr(u, "borrowed_books")),
                    key=lambda item: item[1],
                    reverse=True
                )
                for user, quantity in reader_list:
                    print(f"{user} - {quantity}")
            case "4":
                return
            case _:
                print("Błędna opcja. Spróbuj jeszcze raz.")