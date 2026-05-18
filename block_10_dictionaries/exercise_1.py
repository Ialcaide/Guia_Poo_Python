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
    Display.header("Ejercicio 1 - Métodos de Acceso en Diccionarios")
    
    person = {
        "name"  : "Ileana",
        "age"   : 21,
        "city"  : "Baba"
    }

    Display.row(f"Diccionario base: {person}", FUCSIA)
    Display.empty()

    Display.row("Acceso tradicional con llaves []:", FUCSIA)
    Display.row(f"person['name'] = {person['name']}", MORADO)
    Display.row(f"person['age']  = {person['age']}", MORADO)
    Display.row(f"person['city'] = {person['city']}", MORADO)
    
    Display.empty()
    Display.row("Acceso seguro con el método get():", FUCSIA)
    Display.row(f"person.get('name')  = {person.get('name')}", MORADO)
    Display.row(f"person.get('age')   = {person.get('age', 'N/A')}", MORADO)
    Display.row(f"person.get('city')  = {person.get('city', 'N/A')}", MORADO)
    Display.footer()