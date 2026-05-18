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
    Display.header("Ejercicio 2 - Desempaquetado de Listas como Argumentos")

    # Función que multiplica 3 números posicionales
    def multiply(a, b, c):
        return a * b * c

    my_list = [2, 3, 4]
    result = multiply(*my_list)

    Display.row(f"Lista de elementos definidos : {my_list}", FUCSIA)
    Display.empty()
    Display.row(f"Resultado de la operación : {result}", FUCSIA)
    Display.footer()
