import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1 ------------------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Operaciones Básicas de Conjuntos")
    
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    Display.row(f"Conjunto A = {A}", FUCSIA)
    Display.row(f"Conjunto B = {B}", FUCSIA)
    Display.empty()

    Display.row(f"Unión          A | B  = {A | B}", MORADO)
    Display.row(f"Intersección   A & B  = {A & B}", MORADO)
    Display.row(f"Diferencia     A - B  = {A - B} y B - A  = {B - A}", MORADO)
    Display.footer()