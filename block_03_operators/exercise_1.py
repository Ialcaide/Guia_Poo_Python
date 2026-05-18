import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1-----------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Operadores Aritméticos")
    
    a = 20
    b = 4

    Display.row(f"Variables base -> a = {a}, b = {b}", FUCSIA)
    Display.empty()
    Display.row(f"a + b  = {a + b}   (Suma)", MORADO)
    Display.row(f"a - b  = {a - b}   (Resta)", MORADO)
    Display.row(f"a * b  = {a * b}   (Multiplicación)", MORADO)
    Display.row(f"a / b  = {a / b}   (División decimal)", MORADO)
    Display.row(f"a // b = {a // b}   (División entera)", MORADO)
    Display.row(f"a % b  = {a % b}   (Módulo / Residuo)", MORADO)
    Display.row(f"a ** b = {a ** b}   (Potencia)", MORADO)
    Display.footer()