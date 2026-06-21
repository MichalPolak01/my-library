from typing import ClassVar
from pydantic import BaseModel, field_validator, model_validator, PrivateAttr

class Book(BaseModel):
    """Klasa reprezentująca książkę w bibliotece"""

    title: str
    author: str
    total_quantity: int

    _available_quantity: int = PrivateAttr(default=0)
    _loans_requests: int = PrivateAttr(default=0)
    _id: int = PrivateAttr(default=0)

    _id_counter: ClassVar[int] = 1

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Tytuł książki nie może być pusty.")
        return v.strip()

    @field_validator("author")
    @classmethod
    def author_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Autor książki nie może być pusty.")
        return v.strip()

    @field_validator("total_quantity")
    @classmethod
    def quantity_non_negative(cls, v):
        if v < 0:
            raise ValueError("Całkowita liczba egzemplarzy musi być większa lub równa zero.")
        return v

    @model_validator(mode='after')
    def set_private_fields(self):
        self._available_quantity = self.total_quantity
        self._id = Book._id_counter
        Book._id_counter += 1
        return self

    @property
    def id(self):
        return self._id

    @property
    def available_quantity(self):
        """Zwraca liczbę dostępnych książek"""
        return self._available_quantity

    def borrow(self):
        """Procesowanie wypożyczenia książki"""
        if self._available_quantity <= 0:
            raise ValueError(f'Niestety, ale wszystkie egzemplarze {self.title} są już wypożyczone.')
        self._available_quantity -= 1

    def return_book(self):
        """Procesowanie zwrotu książki"""
        if self._available_quantity >= self.total_quantity:
            raise ValueError(f'Wszystkie egzemplarze {self.title} są już zwrócone.')
        self._available_quantity += 1

    def request_for_loan(self):
        """Procesowanie prośby o wypożyczenie książki"""
        self._loans_requests += 1

    def __str__(self):
        """Reprezentacja tekstowa książki"""
        return f'{self.title} - {self.author}:\t Dostępne: {self._available_quantity}'

    def __repr__(self):
        """Reprezentacja debugowania książki"""
        return f"Book(id={self._id}, title='{self.title}', author='{self.author}', total_quantity={self.total_quantity}, available_quantity={self._available_quantity})"
