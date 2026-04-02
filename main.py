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
            currentUser = user["id"]
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
            browseCatalog()
            mainMenu()
        case "2":
            borrowBook()
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

def borrowBook():
    print("\n~ Wypożyczanie książki ~\n")
    bookName=input("Podaj nazwę książki: ")

    for book in books:
        if bookName in book["name"]:
            if any(loan["user"] == currentUser and loan["book"] == book["id"] for loan in loans):
                print("Już wypożyczyłeś tę książkę.")
            elif book["available"]>0:
                book["available"]-=1
                loans.append({"user": currentUser, "book": book["id"]})
                print("Wypożyczenie książki przebiegło pomyślnie.")
            else:
                print("Niestety, ta książka jest obecnie niedostępna.")

users=[
    {"id": 1, "login": "michal", "hasło": "qwe123", "role": "czytelnik"},
    {"id": 2, "login": "adam35", "hasło": "password", "role": "czytelnik"},
    {"id": 3, "login": "krzys123", "hasło": "1234", "role": "czytelnik"}
]

books=[
    {"id": 1, "name": "W pustyni i w puszczy", "author": "Henryk Sienkiewicz", "available": 5},
    {"id": 2, "name": "Lalka", "author": "Bolesław Prus", "available": 0},
    {"id": 3, "name": "Pan Tadeusz", "author": "Adam Mickiewicz", "available": 2},
    {"id": 4, "name": "Zbrodnia i kara", "author": "Fiodor Dostojewski", "available": 4},
    {"id": 5, "name": "Harry Potter i Kamień Filozoficzny", "author": "J.K. Rowling", "available": 6}
]

currentUser=None

loans=[]

# borrowBook()

if __name__ == "__main__":
    main()