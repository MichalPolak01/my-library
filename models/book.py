class Book:
    """Klasa reprezentująca książkę w bibliotece"""
    _id_counter = 1

    def __init__(self, title, author, total_quantity):
        """Inicjalizacja obiektu książki"""
        if total_quantity <= 0:
            raise ValueError("Całkowita liczba egzemplarzy musi być większa od zera.")

        self.id = self._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self._total_quantity = total_quantity
        self._available_quantity = total_quantity

    @property
    def available_quantity(self):
        """Zwraca liczbę dostępnych książek"""
        return self._available_quantity

    def borrow(self):
        """Procesowanie wypożyczenia książki"""
        if self._available_quantity <= 0:
            raise ValueError(f'Wszystkie egzemplarze {self.title} są już wypożyczone.')

        self._available_quantity -= 1

    def return_book(self):
        """Procesowanie zwrotu książki"""
        if self._available_quantity >= self._total_quantity:
            raise ValueError(f'Wszystkie egzemplarze {self.title} są już dostępne.')

        self._available_quantity += 1

    def __str__(self):
        """Reprezentacja tekstowa książki"""
        return f'{self.title} - {self.author}:	 Dostępne: {self._available_quantity}'

    def __repr__(self):
        """Reprezentacja debugowania książki"""
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', total_quantity={self._total_quantity}, available_quantity={self._available_quantity})"