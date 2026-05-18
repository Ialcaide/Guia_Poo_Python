import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ejercicio 3-------------------------------------------------
def exercise_3():
    clear()

    coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

    Display.header("Ejercicio 3 - Recorrer coordenadas")
    Display.row(f"Coordenadas: {coordinates}", FUCSIA)
    Display.empty()

    for x, y in coordinates:
        Display.row(f"x = {x} | y = {y}", MORADO)
        Display.empty()

    Display.footer()