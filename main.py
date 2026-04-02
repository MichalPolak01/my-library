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



users=[{"login": "admin", "hasło": "password"},{"login": "user", "hasło": "1234"},{"login": "michal", "hasło": "qwe123"}]

if __name__ == "__main__":
    logIn()