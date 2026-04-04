# ***Programowanie wysokopoziomowe***

## Wykonanie: ***Michał Polak***

## Temat projektu: ***Biblioteka***

## Opis projektu
Konsolowa aplikacja do obsługi biblioteki, napisana w języku Python. Program pozwala użytkownikom na logowanie, przeglądanie katalogu książek, wypożyczanie książek oraz przeglądanie listy wypożyczonych pozycji. Wszystkie dane są przechowywane w strukturach takich jak listy i słowniki.

## Funkcjonalności
### Logowanie
Użytkownik podaje login i hasło.
Po 3 nieudanych próbach logowania konto zostaje zablokowane, a program kończy działanie.

### Menu główne
Po zalogowaniu użytkownik ma dostęp do menu głównego, które działa w pętli aż do wybrania opcji „Wyloguj”.
Dostępne opcje:
- Przeglądanie katalogu
- Wypożyczanie książki
- Wyświetlanie listy wypożyczonych książek
- Wylogowanie

### Przeglądanie katalogu
Wyświetlenie wszystkich książek dostępnych w bibliotece wraz z ich autorami i liczbą dostępnych egzemplarzy.

### Wypożyczanie książki
Użytkownik podaje tytuł książki.
Jeśli książka jest dostępna, liczba egzemplarzy zmniejsza się, a książka trafia na listę wypożyczeń użytkownika.
Jeśli książka nie jest dostępna, wyświetlany jest odpowiedni komunikat.

### Moje wypożyczenia
Wyświetlenie listy książek aktualnie wypożyczonych przez zalogowanego użytkownika.

## Wymagania techniczne programu
Program wykorzystuje wyłącznie programowanie strukturalne:
- Funkcje, pętle, instrukcje warunkowe, kolekcje.
- Brak klas i importów zewnętrznych bibliotek.
- Dane są przechowywane w strukturach takich jak listy i słowniki.
<br>

W kodzie zdefiniowano na sztywno:
- 5 książek (tytuł, autor, liczba sztuk).
- 3 użytkowników z hasłami (wszyscy o roli „czytelnik”).
<br>

Każda operacja jest wyodrębniona jako osobna funkcja.

## Struktura danych
**Użytkownicy:**
Przechowywani w liście słowników o strukturze:
- id: Unikalny identyfikator użytkownika (number).
- login: Nazwa użytkownika używana do logowania (string).
- hasło: Hasło użytkownika (string).
- role: Rola użytkownika w systemie (string).

**Książki:**
Przechowywane w liście słowników o strukturze:
- id: Unikalny identyfikator książki (number).
- name: Tytuł książki (string).
- author: Autor Książki (string)
- available: Rola użytkownika w systemie (number).

**Wypożyczenia:**
Przechowywane w liście słowników o strukturze:
- user: Identyfikator użytkownika (number)
- book: Identyfikator książki (number)

## Jak uruchomić program
### Upewnij się, że masz zainstalowne uv. Jeśli nie to wykonaj instalację:
**Windows (PowerShell):**
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**MacOS / Linux:**
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
*Po instalacji zrestartuj terminal i sprawdź: `uv --version`.*

### Otwórz terminal i przejdź do katalogu, w którym projektu `./my-library`
### Odtwórz środowisko:
```
uv sync
```
### Aktywuj środowisko:

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

### Uruchom program poleceniem:
```
uv run main.py
```

### Przykładowy przebieg programu
1. Logowanie:
2. Menu główne:
3. Przeglądanie katalogu:
4. Wypożyczanie książki:
5. Moje wypożyczenia:
6. Wylogowanie:

# Technologie użyte w projekcie
- 🐍 **Python**