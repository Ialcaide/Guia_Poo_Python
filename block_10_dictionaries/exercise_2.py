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
    Display.header("Ejercicio 2 - Iteración de Estructuras (items)")
    
    person = {
        "name"  : "Ileana",
        "age"   : 21,
        "city"  : "Baba"
    }
    
    Display.row(f"Diccionario base: {person}", FUCSIA)
    Display.empty()
    
    Display.row("Recorriendo Claves y Valores simultáneamente:", FUCSIA)
    Display.empty()
    for key, value in person.items():
        Display.row(f"{key} : {value}", MORADO)
        
    Display.footer()
