import os
from core.display import Display
from typing import Optional, List

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercicio 3------------------------------------------------------------------------------------
class Student:
    def __init__(self, name: str, grades: Optional[List[float]] = None):
        if not name.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.name   = name
        self.grades = grades if grades is not None else []

def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Estudiante con Notas Opcionales")
    Display.row("Instancias con y sin lista de notas iniciales:", FUCSIA)
    Display.empty()

    s1 = Student("Daniel")
    s2 = Student("Ana", [10.0, 9.0])

    Display.row(f"Estudiante 1: {s1.name} -> Notas: {s1.grades}", MORADO)
    Display.empty()
    Display.row(f"Estudiante 2: {s2.name} -> Notas: {s2.grades}", MORADO)
    Display.footer()