def main():
    print("Witamy w bibliotece!")
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

users=[{"login": "admin", "hasło": "password"},{"login": "user", "hasło": "1234"},{"login": "michal", "hasło": "qwe123"}]


if __name__ == "__main__":
    main()