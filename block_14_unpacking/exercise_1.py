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
    Display.header("Ejercicio 1 - Desempaquetado Avanzado de Tuplas")

    my_tuple = (10, 20, 30, 40)

    # Desempaquetado usando el operador asterisco para capturar la mitad
    primera, *mitad, ultima = my_tuple

    Display.row(f"Tupla original cargada : {my_tuple}", FUCSIA)
    Display.empty()
    Display.row("Ejecutando: primera, *mitad, ultima = my_tuple", MORADO)
    Display.empty()
    Display.row(f"Variable 'primera' (int)  : {primera}", MORADO)
    Display.row(f"Variable 'mitad'   (list) : {mitad}", MORADO)
    Display.row(f"Variable 'ultima'  (int)  : {ultima}", MORADO)
    Display.footer()
