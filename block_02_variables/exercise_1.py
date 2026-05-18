import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1-------------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Variables Simples y Complejas")
    
    # tipos simples
    numero_entero: int = 19
    numero_decimal: float = 3.14
    cadena_texto: str = "Hola Python"
    booleano: bool = True
    nulo = None

    # tipos complejos
    lista: list = [1, 2, 3, "python", True]
    tupla: tuple = (1, "hello", 3.14)
    diccionario: dict = {"nombre": "Juan", "edad": 25}
    conjunto: set = {1, 2, 3, 4, 5}

    Display.row("TIPOS SIMPLES:", FUCSIA)
    Display.empty()
    Display.row(f"int   : {numero_entero}", MORADO)
    Display.row(f"float : {numero_decimal}", MORADO)
    Display.row(f"str   : {cadena_texto}", MORADO)
    Display.row(f"bool  : {booleano}", MORADO)
    Display.row(f"None  : {nulo}", MORADO)

    Display.empty()
    Display.row("TIPOS COMPLEJOS:", FUCSIA)
    Display.empty()
    Display.row(f"list  : {lista}", MORADO)
    Display.row(f"tuple : {tupla}", MORADO)
    Display.row(f"dict  : {diccionario}", MORADO)
    Display.row(f"set   : {conjunto}", MORADO)
    Display.footer()

