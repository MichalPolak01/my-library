from models.library import Library
from models.book import Book
from models.user import Reader, Librarian, User

# Inicjalizacja biblioteki
library = Library()

# Dodanie książek do biblioteki
library.add_book(Book("W pustyni i w puszczy", "Henryk Sienkiewicz", 5))
library.add_book(Book("Lalka", "Bolesław Prus", 0))
library.add_book(Book("Pan Tadeusz", "Adam Mickiewicz", 2))
library.add_book(Book("Zbrodnia i kara", "Fiodor Dostojewski", 4))
library.add_book(Book("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 6))

# Dodanie użytkowników
library.add_user(Reader("qwe", "123"))
library.add_user(Reader("michal", "qwe123"))
library.add_user(Reader("adam35", "password"))
library.add_user(Reader("krzys123", "1234"))
library.add_user(Librarian("ewa", "admin123"))
library.add_user(Librarian("jan", "123"))

# Główna funkcja wywołująca logowanie i menu główne biblioteki
def main():
    print("\n~~~ Witaj w bibliotece! ~~~\n")
    while True:
        print("~ Wybierz co chcesz zrobić ~\n")
        print("1. Zaloguj się")
        print("2. Wyjdź")
        choice = input("Wybierz opcję: ")
        match choice:
            case "1":
                login = input("\nPodaj login: ")
                password = input("Podaj hasło: ")
                user = library.log_in(login, password)
                if user:
                    user.menu(library)
            case _:
                print("\nDziękujemy za skorzystanie z biblioteki!")
                break

if __name__ == "__main__":
    main()