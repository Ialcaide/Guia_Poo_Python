import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Cuadrados de Pares del 1 al 10")
    
    # Mantiene tu list comprehension funcional exacta
    even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

    Display.row(f"Resultado: {even_squares}", FUCSIA)
    Display.footer()
