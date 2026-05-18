import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def get_input_padding():
    cols = Display.get_cols()
    return " " * ((cols - Display.WIDTH) // 2 + 2)

# Ejercicio 1-------------------------------------------------
def exercise_1():
    clear()

    # creo la lista inicial
    my_list = ["banana", "manzana", "uva"]

    Display.header("Ejercicio 1 - append y sort")
    Display.row("Lista inicial:", FUCSIA)
    Display.empty()
    Display.row(f"{my_list}", MORADO)
    Display.empty()

    # agrego 3 elementos con append
    my_list.append("pera")
    my_list.append("kiwi")
    my_list.append("mango")

    Display.row("Despues de agregar 3 elementos con append():", FUCSIA)
    Display.empty()
    Display.row(f"{my_list}", MORADO)
    Display.empty()

    # ordeno la lista
    my_list.sort()
    Display.row("Despues de .sort() para ordenar:", FUCSIA)
    Display.empty()
    Display.row(f"{my_list}", MORADO)
    Display.footer()

