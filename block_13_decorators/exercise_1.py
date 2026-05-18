import os
from core.display import Display
from core.decorators_ex13 import log_simple

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1 ------------------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Decorador Base (Importado)")

# Llamada al decorador 
    @log_simple  
    def saludar():
        Display.row("Función: ¡Hola mundo!", MORADO)

    saludar()
    Display.footer()