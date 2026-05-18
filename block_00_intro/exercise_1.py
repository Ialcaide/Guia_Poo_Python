import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercicio 1-------------------------------------------------------
class Book:
    def __init__(self, title: str, isbn: str):
        if not title:
            raise ValueError("Title cannot be empty")
        if not isbn:
            raise ValueError("ISBN cannot be empty")
        self.title = title
        self.isbn = isbn


class User:
    def __init__(self, name: str, user_id: int):
        if not name:
            raise ValueError("Name cannot be empty")
        if user_id < 0:
            raise ValueError("User ID cannot be negative")
        self.name = name
        self.user_id = user_id


class Loan:
    def __init__(self, book: Book, user: User):
        if not book:
            raise ValueError("Book cannot be empty")
        if not user:
            raise ValueError("User cannot be empty")
        self.book = book
        self.user = user


class Author:
    def __init__(self, name: str, nationality: str):
        if not name:
            raise ValueError("Name cannot be empty")
        if not nationality:
            raise ValueError("Nationality cannot be empty")
        self.name = name
        self.nationality = nationality


class Category:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Category name cannot be empty")
        self.name = name
#identificar las 5 clases
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Sistema de Biblioteca" )
    Display.row("identificar 5 clases para modelar un sistema de biblioteca:", FUCSIA )
    Display.empty()

    book     = Book("Divergente", "978-0132350884" )
    author   = Author("Veronica Roth", "Americano")
    category = Category("Ficcion")
    user     = User("Daniel", 1)
    loan     = Loan(book, user)

    Display.row(f"Book     : {book.title} (ISBN: {book.isbn})", MORADO)
    Display.empty()
    Display.row(f"Author   : {author.name} ({author.nationality})", MORADO)
    Display.empty()
    Display.row(f"Category : {category.name}", MORADO)
    Display.empty()
    Display.row(f"User     : {user.name} (ID: {user.user_id})", MORADO)
    Display.empty()
    Display.row(f"Loan     : {book.title} → {user.name}", MORADO)
    Display.footer()