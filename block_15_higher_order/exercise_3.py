import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3 ------------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Reducción con reduce()")

    my_list = [1, 2, 3, 4]

    # Uso de reduce() para acumular multiplicativamente la estructura
    result = reduce(lambda x, y: x * y, my_list)

    Display.row(f"Lista original cargada : {my_list}", FUCSIA)
    Display.empty()
    Display.row("Ejecutando: reduce(lambda x, y: x * y, my_list)", MORADO)
    Display.empty()
    
    Display.row(f"Resultado final acumulado : {result}", FUCSIA)
    Display.footer()
