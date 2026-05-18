import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_input_padding():
    cols = Display.get_cols()
    return " " * ((cols - Display.WIDTH) // 2 + 2)

# Ejercicio 3 ------------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Manejo de ValueError y ZeroDivisionError")
    
    # Valores fijos definidos directamente por el estudiante
    dividendo = 20
    divisor   = 0  # Provocará el ZeroDivisionError automáticamente
    
    Display.row(f"Valores base -> Dividendo: {dividendo} | Divisor: {divisor}", FUCSIA)
    Display.empty()

    try:
        # Intentamos hacer la operación matemática
        resultado = dividendo / divisor
        Display.row(f"Resultado: {resultado}", MORADO)
        
    except ZeroDivisionError as error:
        Display.row("Error: No se puede dividir entre cero.", FUCSIA)
        Display.row(f"Detalle: {error}", MORADO)
        
    except ValueError as error:
        Display.row("Error: Hubo un problema con el valor de los datos.", FUCSIA)
        Display.row(f"Detalle: {error}", MORADO)
        
    Display.footer()
