import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_input(prompt: str) -> str:
    cols    = Display.get_cols()
    padding = (cols - Display.WIDTH) // 2
    print(" " * (padding + 2), end="")
    return input(FUCSIA + f"  {prompt} " + RESET)

# ejercicio 1 ------------------------------------------------------------
def exercise_1():
    clear()

    def double(x):
        return x * 2

    Display.header("Ejercicio 1 - Funcion que calcula el doble")
    Display.row("def double(x): return x * 2", FUCSIA)
    Display.footer()

    while True:
        try:
            number = float(get_input("Ingresa un numero:"))
            break
        except ValueError:
            Display.header("Error")
            Display.row("Ingresa un numero valido.", MORADO)
            Display.footer()

    result = double(number)

    Display.header("Resultado")
    Display.row(f"Numero    : {number}", MORADO)
    Display.row(f"El doble  : {result}", FUCSIA)
    Display.footer()