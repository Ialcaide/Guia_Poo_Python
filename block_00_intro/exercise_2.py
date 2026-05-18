import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercio 2 ------------------------------------------------------------------------------------
class Person:
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("Name cannot be empty")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age

#intanciamos 3 objetos diferentes
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Clase Persona")
    Display.row("Instanciar 3 objetos diferentes de la clase Person:", FUCSIA)
    Display.empty()

    person_1 = Person("Daniel", 20)
    person_2 = Person("Ana", 22)
    person_3 = Person("Luis", 19)

    Display.row(f"Name: {person_1.name} | Age: {person_1.age}", MORADO)
    Display.empty()
    Display.row(f"Name: {person_2.name} | Age: {person_2.age}", MORADO)
    Display.empty()
    Display.row(f"Name: {person_3.name} | Age: {person_3.age}", MORADO)
    Display.footer()