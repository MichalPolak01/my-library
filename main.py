from models.book import Book

# Główna funkcja wywołująca logowanie i menu główne biblioteki
def main():
    print("Witaj w bibliotece!")
    if logIn(): # Jeśli logowanie się powiodło, przechodzimy do menu głównego
        mainMenu()

# Funkcja logowania z limitem prób i blokadą konta po 3 nieudanych próbach
# Zwraca True, jeśli logowanie się powiodło, lub False, jeśli konto zostało zablokowane
def logIn(counter: int = 0) -> bool:
    global currentUser
    print("\n~ Logowanie do biblioteki ~\n")
    login=input("Podaj login: ")
    hasło=input("Podaj hasło: ")

    # Pętla sprawdzająca, czy podany login i hasło istnieją w bazie użytkowników (jeśli nie zwiększamy licznik prób)
    for user in users:
        if user["login"]==login and user["hasło"]==hasło:
            print("Zalogowano pomyślnie.")
            currentUser=user["id"]
            return True
    else:
        counter+=1

    # Jeśli licznik prób osiągnie 3, zwracamy False
    if counter==3:
        print("\nZbyt wiele prób logowania. Konto zablokowane.\n")
        return False
    
    print("Nieprawidłowy login lub hasło. Spróbuj ponownie. Pozostało prób:", 3-counter,"\n")
    return logIn(counter)   # Wywołanie rekurencyjne fuinkcji przy nieudanym logowaniu

# Funkcja wyświetlająca menu główne biblioteki i obsługująca wybór opcji użytkownika
def mainMenu():
    print("\n~ Menu główne ~\n")
    print("1. Przeglądanie katalogu")
    print("2. Wypożyczanie książki")
    print("3. Moje wypożyczenia")
    print("4. Wyloguj\n")
    option=input("Wybierz opcję: ")

    match option:
        case "1":
            browseCatalog()
            mainMenu()
        case "2":
            borrowBook()
            mainMenu()
        case "3":
            myLoans()
            mainMenu()
        case "4":
            print("\nWylogowano.\n")
        case _:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
            mainMenu()

# Przeglądanie katalogu książek
def browseCatalog():
    print("\n~ Katalog książek ~\n")
    for book in books:
        print(f"{book['name']} - {book['author']} (Dostępne: {book['available']})")

# Wypożyczanie książki
def borrowBook():
    print("\n~ Wypożyczanie książki ~\n")
    bookName=input("Podaj nazwę książki: ")

    for book in books:
        if bookName in book["name"]:    # Sprawdzenie, czy istnieje podana książka
            if any(loan["user"] == currentUser and loan["book"] == book["id"] for loan in loans):   # Sprawdzenie, czy użytkownik już wypożyczył tę książkę
                print("Już wypożyczyłeś tę książkę.")
                return
            elif book["available"] > 0:   # Sprawdzenie dostępności - jeżeli dostępna to procesujemy wypożyczenie
                book["available"] -= 1
                loans.append({"user": currentUser, "book": book["id"]})
                print("Wypożyczenie książki przebiegło pomyślnie.")
                return
            else:
                print("Niestety, ta książka jest obecnie niedostępna.")
                return

    print("Nie znaleziono książki o podanej nazwie.")  # Komunikat, jeśli książka nie istnieje

# Moje wypożyczenia - lista książek wypożyczonych przez użytkownika
def myLoans():
    print("\n~ Moje wypożyczenia ~\n")
    for loan in loans:
        if loan["user"]==currentUser:
            for book in books:
                if book["id"]==loan["book"]:
                    print(f"{book['name']} - {book['author']}")

# Tablica słowników użytokowników
users=[
    {"id": 1, "login": "michal", "hasło": "qwe123", "role": "czytelnik"},
    {"id": 2, "login": "adam35", "hasło": "password", "role": "czytelnik"},
    {"id": 3, "login": "krzys123", "hasło": "1234", "role": "czytelnik"}
]

# Tablica słowników kisążek
books=[
    {"id": 1, "name": "W pustyni i w puszczy", "author": "Henryk Sienkiewicz", "available": 5},
    {"id": 2, "name": "Lalka", "author": "Bolesław Prus", "available": 0},
    {"id": 3, "name": "Pan Tadeusz", "author": "Adam Mickiewicz", "available": 2},
    {"id": 4, "name": "Zbrodnia i kara", "author": "Fiodor Dostojewski", "available": 4},
    {"id": 5, "name": "Harry Potter i Kamień Filozoficzny", "author": "J.K. Rowling", "available": 6}
]



# Tablica słowników wypożyczeń
loans=[]

if __name__ == "__main__":
    main()