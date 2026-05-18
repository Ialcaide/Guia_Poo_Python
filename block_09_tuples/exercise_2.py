import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ejercicio 2-------------------------------------------------
def exercise_2():
    clear()

    my_tuple = (100, 200, 300, 400)

    # unpacking
    a, b, *rest = my_tuple

    Display.header("Ejercicio 2 - Unpacking de tupla")
    Display.row(f"Tupla original : {my_tuple}", FUCSIA)
    Display.empty()
    Display.row("a, b, *rest = my_tuple", MORADO)
    Display.empty()
    Display.row(f"a    = {a}", MORADO)
    Display.row(f"b    = {b}", MORADO)
    Display.row(f"rest = {rest}", MORADO)
    Display.footer()
