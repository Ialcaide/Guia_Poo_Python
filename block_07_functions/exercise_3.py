import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ejercicio 3 ------------------------------------------------------------
def exercise_3():
    clear()

    # funcion recursiva para calcular factorial
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    number = 5
    result = factorial(number)

    proceso = ""
    for i in range(number, 0, -1):
        proceso += f"{i} x "
    proceso += f"1 = {result}"

    Display.header("Ejercicio 3 - Factorial recursivo")
    Display.row("def factorial(n):", FUCSIA)
    Display.row("    if n == 0: return 1", MORADO)
    Display.row("    return n * factorial(n - 1)", MORADO)
    Display.empty()
    Display.row(f"factorial({number}) = {result}", FUCSIA)
    Display.empty()
    Display.row("Proceso:", FUCSIA)
    Display.row(proceso, MORADO)
    Display.footer()