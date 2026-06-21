from models.library import Library
from models.book import Book
from models.user import Reader, Librarian, User

# Inicjalizacja biblioteki
library = Library()

# Dodanie książek do biblioteki
library.add_book(Book(title="W pustyni i w puszczy", author="Henryk Sienkiewicz", total_quantity=5))
library.add_book(Book(title="Lalka", author="Bolesław Prus", total_quantity=0))
library.add_book(Book(title="Pan Tadeusz", author="Adam Mickiewicz", total_quantity=2))
library.add_book(Book(title="Zbrodnia i kara", author="Fiodor Dostojewski", total_quantity=4))
library.add_book(Book(title="Harry Potter i Kamień Filozoficzny", author="J.K. Rowling", total_quantity=6))

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