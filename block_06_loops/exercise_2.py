import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Lista de Frutas con Enumerate")
    
    fruit_list = ["manzana", "pera", "uva", "sandia", "mango"]

    for index, fruit in enumerate(fruit_list):
        Display.row(f"[{index}] {fruit}", MORADO)
        
    Display.footer()
