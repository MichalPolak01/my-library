def main():
    print("Witaj w bibliotece!")
    if logIn():
        mainMenu()

def logIn(counter: int = 0) -> bool:

    login=input("Podaj login: ")
    hasło=input("Podaj hasło: ")

    for user in users:
        if user["login"]==login and user["hasło"]==hasło:
            print("Zalogowano pomyślnie.")
            return True
    else:
        counter+=1

    if counter==3:
        print("Zbyt wiele prób logowania. Konto zablokowane.")
        return False
    
    print("Nieprawidłowy login lub hasło. Spróbuj ponownie. Pozostało prób:", 3-counter)
    return logIn(counter)

def mainMenu():
    print("\n~ Menu główne ~\n")
    print("1. Przeglądanie katalogu")
    print("2. Wypożyczanie książki")
    print("3. Moje wypożyczenia")
    print("4. Wyloguj\n")
    option=input("Wybierz opcję: ")

    match option:
        case "1":
            print("Przeglądanie katalogu...")
            browseCatalog()
            mainMenu()
        case "2":
            print("Wypożyczanie książki...")
            mainMenu()
        case "3":
            print("Moje wypożyczenia...")
            mainMenu()
        case "4":
            print("Wylogowano.")
        case _:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
            mainMenu()

def browseCatalog():
    print("\n~ Katalog książek ~\n")
    for book in books:
        print(f"{book['name']} - {book['author']} (Dostępne: {book['available']})")

users=[
    {"login": "michal", "hasło": "qwe123", "role": "czytelnik"},
    {"login": "adam35", "hasło": "password", "role": "czytelnik"},
    {"login": "krzys123", "hasło": "1234", "role": "czytelnik"}
]

books=[
    {"name": "W pustyni i w puszczy", "author": "Henryk Sienkiewicz", "available": 5},
    {"name": "Lalka", "author": "Bolesław Prus", "available": 3},
    {"name": "Pan Tadeusz", "author": "Adam Mickiewicz", "available": 2},
    {"name": "Zbrodnia i kara", "author": "Fiodor Dostojewski", "available": 4},
    {"name": "Harry Potter i Kamień Filozoficzny", "author": "J.K. Rowling", "available": 6}
]


if __name__ == "__main__":
    main()