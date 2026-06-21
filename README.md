# ***Programowanie wysokopoziomowe***

## Wykonanie: ***Michał Polak***

## Temat projektu: ***Biblioteka — refaktoryzacja do OOP, rola bibliotekarza i programowanie funkcyjne***

## Opis projektu
Konsolowa aplikacja do obsługi biblioteki, napisana w języku Python z wykorzystaniem **programowania obiektowego (OOP)** oraz **programowania funkcyjnego**. Program pozwala użytkownikom na logowanie, przeglądanie katalogu książek, wypożyczanie i zwracanie książek. Aplikacja obsługuje dwie role: **Czytelnika** i **Bibliotekarza**, każda z innymi uprawnieniami i funkcjonalnościami. Wszystkie dane są reprezentowane jako obiekty klas: `Book`, `User`, `Reader`, `Librarian` i `Library`.

Aplikacja jest rozszerzeniem wersji strukturalnej z Części 1 programu nauczania i dodatkowo zawiera nowe funkcjonalności z Części 3, zaimplementowane w stylu funkcyjnym: wyszukiwanie, filtrowanie, sortowanie oraz statystyki bibliotekarza.

## Funkcjonalności

### Logowanie
Użytkownik podaje login i hasło. System automatycznie określa rolę użytkownika (Czytelnik lub Bibliotekarz) i wyświetla odpowiednie menu.

### Menu Czytelnika
Po zalogowaniu czytelnik ma dostęp do następujących opcji:

1. **Przeglądaj katalog książek** — Wyświetlenie wszystkich książek dostępnych w bibliotece wraz z ich autorami i liczbą dostępnych egzemplarzy.

2. **Wypożycz książkę** — Czytelnik podaje tytuł książki. Jeśli książka jest dostępna, liczba egzemplarzy zmniejsza się, a książka trafia na listę wypożyczeń użytkownika. Jeśli nie jest dostępna, wyświetlany jest komunikat.

3. **Zwróć książkę** — Czytelnik może zwrócić wcześniej wypożyczoną książkę. Liczba dostępnych egzemplarzy zwiększa się, a książka usuwana jest z listy wypożyczeń.

4. **Moje wypożyczenia** — Wyświetlenie listy wszystkich książek aktualnie wypożyczonych przez zalogowanego czytelnika.

5. **Wyślij prośbę o przedłużenie** — Czytelnik może wysłać prośbę o przedłużenie wypożyczenia wybranej książki. Prośba trafia do kolejki, gdzie bibliotekarz może ją zaakceptować lub odrzucić.

6. **Wyloguj** — Wylogowanie z systemu.

### Menu Bibliotekarza
Po zalogowaniu bibliotekarz ma dostęp do następujących opcji:

1. **Lista wszystkich wypożyczeń** — Wyświetlenie listy wszystkich aktualnie wypożyczonych książek wraz z loginami użytkowników, którzy je wypożyczyli. Każde wypożyczenie zawiera informacje o tytule i autorze książki.

2. **Obsługa próśb o przedłużenie** — Bibliotekarz widzi wszystkie oczekujące prośby o przedłużenie wypożyczeń. Dla każdej prośby bibliotekarz może:
   - **Zaakceptować** — Prośba zostaje zatwierdzona.
   - **Odrzucić** — Prośba zostaje odrzucona, a czytelnik nie może przedłużyć wypożyczenia.

3. **Statystyki biblioteki** — Wyświetlenie statystyk biblioteki dla bibliotekarza, w tym najpopularniejsza książka, liczba aktywnych wypożyczeń i lista czytelników.
4. **Wyloguj** — Wylogowanie z systemu.

### Statystyki bibliotekarza
W menu bibliotekarza dodano opcję statystyk, która obejmuje:
- najpopularniejszą książkę (największa różnica między łączną liczbą sztuk a dostępnymi),
- liczbę aktywnych wypożyczeń ogółem,
- listę czytelników posortowaną malejąco wg liczby wypożyczonych książek.

## Wymagania techniczne programu

Program wykorzystuje **programowanie obiektowe (OOP)** w Pythonie:

### Klasy i Dziedziczenie
- **Zastosowanie dziedziczenia** — Klasy `Reader` i `Librarian` dziedziczą po klasie bazowej `User`.
- **Hermetyzacja** — Pola prywatne (`_total_quantity`, `_available_quantity`) są chronione i dostępne przez metody lub properties.
- **Metoda `__str__`** — Implementowana w klasach `Book` i `User` do wyświetlania czytelnej reprezentacji obiektu.
- **Instancje klas** — Dane początkowe (książki i użytkownicy) są tworzone jako instancje klas.

### Struktury danych
W kodzie zdefiniowano na sztywno:
- **5 książek** (tytuł, autor, liczba sztuk) — jako instancje klasy `Book`.
- **4 czytelników** — jako instancje klasy `Reader`.
- **2 bibliotekarzy** — jako instancje klasy `Librarian`.

### Logika biznesowa
Operacje biznesowe są zaimplementowane jako metody w klasie `Library`:
- Wyszukiwanie książek
- Wypożyczanie i zwracanie książek
- Zarządzanie listą wypożyczeń
- Obsługa próśb o przedłużenie

### Funkcje programowania funkcyjnego
Nowe funkcjonalności zostały zaimplementowane przy użyciu technik funkcyjnych:
- wyszukiwanie i filtrowanie katalogu za pomocą `filter`/`lambda` i list comprehension,
- sortowanie katalogu za pomocą `sorted(..., key=lambda ...)`,
- rezerwacja niedostępnych książek i informacja o rezerwacjach przy obsłudze próśb o przedłużenie,
- statystyki bibliotekarza obliczane przy użyciu comprehension i funkcji wbudowanych,
- funkcja wyższego rzędu `display_collection(...)`, która przyjmuje funkcję jako argument.

## Struktura Klas i Danych

### Klasa `Book`
Reprezentuje książkę w bibliotece.

**Atrybuty:**
- `id` — Unikalny identyfikator książki (generowany automatycznie).
- `title` — Tytuł książki (string).
- `author` — Autor książki (string).
- `_total_quantity` — Łączna liczba egzemplarzy (hermetyzowany).
- `_available_quantity` — Liczba dostępnych egzemplarzy (hermetyzowany).

**Metody:**
- `borrow()` — Zmniejsza liczbę dostępnych egzemplarzy.
- `return_book()` — Zwiększa liczbę dostępnych egzemplarzy.
- `__str__()` — Reprezentacja tekstowa książki.

**Przykład:**
```python
book = Book("Pan Tadeusz", "Adam Mickiewicz", 2)
book.borrow()  # Wypożyczenie książki
```

### Klasa `User` (klasa bazowa)
Klasa bazowa dla użytkowników systemu.

**Atrybuty:**
- `id` — Unikalny identyfikator użytkownika (generowany automatycznie).
- `login` — Login użytkownika (string).
- `password` — Hasło użytkownika (string).
- `role` — Rola użytkownika: `'reader'` lub `'librarian'` (string).

**Metody:**
- `check_credentials(login, password)` — Weryfikacja danych logowania.
- `menu(library)` — Abstrakcyjna metoda menu (zaimplementowana w klasach potomnych).
- `__str__()` — Reprezentacja tekstowa użytkownika.

### Klasa `Reader` (dziedziczy po `User`)
Reprezentuje czytelnika biblioteki.

**Dodatkowe atrybuty:**
- `borrowed_books` — Lista ID wypożyczonych książek (list).
- `extension_requests` — Lista próśb o przedłużenie (list).

**Metody:**
- `menu(library)` — Menu interaktywne dla czytelnika z dostępem do wszystkich funkcji czytelnika.

**Inicjalizacja:**
```python
reader = Reader("michal", "qwe123")
```

### Klasa `Librarian` (dziedziczy po `User`)
Reprezentuje bibliotekarza.

**Metody:**
- `menu(library)` — Menu interaktywne dla bibliotekarza z dostępem do funkcji zarządzania biblioteką.

**Inicjalizacja:**
```python
librarian = Librarian("ewa", "admin123")
```

### Klasa `Library`
Zarządza kolekcją książek i użytkowników oraz realizuje logikę biznesową.

**Atrybuty:**
- `books` — Lista wszystkich książek (list).
- `users` — Lista wszystkich użytkowników (list).
- `loans` — Lista wszystkich wypożyczeń (list słowników zawierających informacje o użytkowniku, książce i ewentualnych prośbach).

**Metody:**
- `add_book(book)` — Dodaje książkę do biblioteki.
- `add_user(user)` — Dodaje użytkownika do biblioteki.
- `log_in(login, password)` — Logowanie użytkownika; zwraca obiekt użytkownika lub `None`.
- `browse_catalog()` — Wyświetla katalog wszystkich książek.
- `borrow_book(user, book_title)` — Wypożyczanie książki przez danego użytkownika.
- `return_book(user, book_title)` — Zwracanie książki przez użytkownika.
- `borrowed_books_by_user(user)` — Zwraca listę wypożyczonych książek dla danego użytkownika.
- `request_extension(user, book_title)` — Zgłasza prośbę o przedłużenie wypożyczenia.
- `list_loans()` — Wyświetla wszystkie aktualnie wypożyczone książki (dla bibliotekarza).
- `handle_extension_requests()` — Obsługuje prośby o przedłużenie (dla bibliotekarza).

## Dane przykładowe

Aplikacja zawiera wstępnie zdefiniowane dane:

**Książki:**
- W pustyni i w puszczy — Henryk Sienkiewicz (5 egzemplarzy)
- Lalka — Bolesław Prus (0 egzemplarzy)
- Pan Tadeusz — Adam Mickiewicz (2 egzemplarze)
- Zbrodnia i kara — Fiodor Dostojewski (4 egzemplarze)
- Harry Potter i Kamień Filozoficzny — J.K. Rowling (6 egzemplarzy)

**Użytkownicy:**
- Czytelnicy: `qwe` (hasło: `123`), `michal` (hasło: `qwe123`), `adam35` (hasło: `password`), `krzys123` (hasło: `1234`)
- Bibliotekarze: `ewa` (hasło: `admin123`), `jan` (hasło: `123`)

## Jak uruchomić program

### Upewnij się, że masz zainstalowane uv. Jeśli nie, wykonaj instalację:

**Windows (PowerShell):**
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Po instalacji zrestartuj terminal i sprawdź: `uv --version`.*

### Przejdź do katalogu projektu
```
cd ./my-library
```

### Odtwórz środowisko
```
uv sync
```

### Aktywuj środowisko

**Windows (PowerShell):**
```
.venv\Scripts\activate
```

**Windows (cmd):**
```
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```
source .venv/bin/activate
```

*Po aktywacji zobaczysz `(.venv)` na początku wiersza poleceń.*

### Uruchom program
```
uv run main.py
```

## Przykładowy przebieg programu

1. **Ekran startowy** — Wyświetlony zostaje komunikat powitalny i menu logowania.

2. **Logowanie** — Użytkownik wpisuje login i hasło (np. `michal` / `qwe123` dla czytelnika).

3. **Menu Czytelnika** — Po zalogowaniu czytelnik widzi swoje menu:
   - Może przeglądać katalog
   - Może wypożyczyć "Pan Tadeusz"
   - Może zobaczyć swoje wypożyczenia
   - Może wysłać prośbę o przedłużenie

4. **Menu Bibliotekarza** — Po zalogowaniu bibliotekarza (np. `ewa` / `admin123`) widzi on:
   - Listę wszystkich wypożyczeń w bibliotece
   - Prośby o przedłużenie (jeśli są jakieś)
   - Możliwość zaakceptowania lub odrzucenia próśb

5. **Wylogowanie** — Użytkownik powraca do ekranu logowania.

## Struktura projektu

```
my-library/
├── main.py                 # Główny plik aplikacji
├── models/
│   ├── book.py            # Klasa Book
│   ├── user.py            # Klasy User, Reader, Librarian
│   └── library.py         # Klasa Library
├── pyproject.toml         # Konfiguracja projektu
└── README.md              # Ten plik
```

## Technologie użyte w projekcie

- 🐍 **Python** — Język programowania
- 📦 **OOP** — Programowanie obiektowe (dziedziczenie, hermetyzacja, polimorfizm)
- 🎯 **UV** — Zarządca pakietów i środowisk Pythona

