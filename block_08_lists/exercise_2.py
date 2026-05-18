import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# Ejercicio 2-------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Funciones Integradas en Listas")
    
    number_list = [5, 3, 8, 1, 9, 3]

    Display.row(f"Estructura analizada -> Lista: {number_list}", FUCSIA)
    Display.empty()
    Display.row(f"Suma total (sum)    : {sum(number_list)}", MORADO)
    Display.row(f"Valor máximo (max)  : {max(number_list)}", MORADO)
    Display.row(f"Valor mínimo (min)  : {min(number_list)}", MORADO)
    Display.footer()

