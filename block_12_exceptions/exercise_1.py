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

# Ejercicio 1 ------------------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Captura de ValueError")
    Display.footer()
    
    pad = get_input_padding()
    
    try:
        # Intentamos capturar y convertir la entrada directamente
        number = int(input(pad + FUCSIA + "Ingrese un número entero: " + RESET))
        
        clear()
        Display.header("Ejercicio 1 - Resultado")
        Display.row(f"El numero que ingreso es: {number}", FUCSIA)
        
    except ValueError as error:
        clear()
        Display.header("Ejercicio 1 - Error Detectado")
        Display.row("Error: debe ingresar un número entero.", FUCSIA)
        Display.empty()
        Display.row(f"Detalle técnico: {error}", MORADO)
        
    Display.footer()