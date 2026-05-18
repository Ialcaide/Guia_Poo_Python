import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2 ------------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Filtrado con filter()")

    my_list = [1, 2, 3, 4, 5]

    # Uso de filter() para extraer los elementos que cumplan la condición lógica
    result = list(filter(lambda x: x > 3, my_list))

    Display.row(f"Lista original cargada : {my_list}", FUCSIA)
    Display.empty()
    Display.row("Ejecutando: list(filter(lambda x: x > 3, my_list))", MORADO)
    Display.empty()
    Display.row(f"Resultado obtenido     : {result}", FUCSIA)
    Display.footer()