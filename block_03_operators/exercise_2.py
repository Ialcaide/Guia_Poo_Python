import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2-----------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Comparación: == vs is")
    
    a = [1, 2]
    b = [1, 2]

    Display.row(f"Listas instanciadas -> a = {a} | b = {b}", FUCSIA)
    Display.empty()
    Display.row(f"a == b : {a == b}   (Mismo contenido estructurado)", MORADO)
    Display.row(f"a is b : {a is b}   (Diferente objeto / dirección en memoria)", MORADO)
    Display.footer()