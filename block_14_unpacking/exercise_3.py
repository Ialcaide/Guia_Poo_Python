import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3 ------------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Combinar Diccionarios con Operador **")

    dict1 = {"a": 1}
    dict2 = {"b": 2}

    # Combinamos ambos mapas en una nueva dirección de memoria
    combined = {**dict1, **dict2}

    Display.row(f"Diccionario 1 (dict1) : {dict1}", MORADO)
    Display.row(f"Diccionario 2 (dict2) : {dict2}", MORADO)
    Display.empty()
    Display.row("Ejecutando: combined = {**dict1, **dict2}", FUCSIA)
    Display.empty()
    Display.row(f"Resultado (combined)  : {combined}", FUCSIA)
    Display.empty()
    Display.row(f"Verificación: dict1 sigue intacto : {dict1}", MORADO)
    Display.row(f"Verificación: dict2 sigue intacto : {dict2}", MORADO)
    Display.footer()