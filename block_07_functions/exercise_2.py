import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ejercicio 2 ------------------------------------------------------------
def exercise_2():
    clear()

    # funcion que suma todos los elementos con *args
    def sum_all(*numbers):
        return sum(numbers)

    number_list = [1, 2, 3, 4]
    result      = sum_all(*number_list)

    Display.header("Ejercicio 2 - Suma con *args")
    Display.row("def sum_all(*numbers): return sum(numbers)", FUCSIA)
    Display.empty()
    Display.row(f"Lista     : {number_list}", MORADO)
    Display.row(f"Resultado : {result}", FUCSIA)
    Display.footer()
