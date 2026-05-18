import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2-----------------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Estructura de Listas y Slicing")
    Display.row("Manipulación de elementos dentro de una lista de 5 elementos:", FUCSIA)
    Display.empty()
    
    lista = ["manzana", "pera", "uva", "sandia", "mango"]
    
    Display.row(f"Lista completa  : {lista}", MORADO)
    Display.empty()
    Display.row(f"Primero [0]     : {lista[0]}", MORADO)
    Display.row(f"Último  [-1]    : {lista[-1]}", MORADO)
    Display.row(f"Sublista [1:4]  : {lista[1:4]}", MORADO)
    Display.footer()