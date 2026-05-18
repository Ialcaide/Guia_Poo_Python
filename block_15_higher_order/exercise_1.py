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
    Display.header("Ejercicio 1 - Transformación con map()")

    my_list = [2, 4, 6]

    # Uso de map() con una función lambda para incrementar cada elemento en 1
    result = list(map(lambda x: x + 1, my_list))

    Display.row(f"Lista original cargada : {my_list}", FUCSIA)
    Display.empty()
    Display.row("Ejecutando: list(map(lambda x: x + 1, my_list))", MORADO)
    Display.empty()
    Display.row(f"Resultado obtenido     : {result}", FUCSIA)
    Display.footer()

