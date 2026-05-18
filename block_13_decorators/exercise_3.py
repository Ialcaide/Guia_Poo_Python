import os
from core.display import Display
from core.decorators_ex13 import log_advanced

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
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
    Display.header("Ejercicio 3 - Decorador con Inspección de Nombres")

    @log_advanced  
    def suma(a, b):
        Display.row(f"Función: Sumando internamente {a} + {b}", MORADO)
        return a + b

    # Variables en inglés con valores fijos definidos
    num_a = 2
    num_b = 3

    # Ejecución directa
    suma(num_a, num_b)
    Display.footer()
