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

# Ejercicio 2---------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Captura Numérica y Promedios")
    Display.footer()
    
    pad = get_input_padding()

    # Validar número 1
    while True:
        try:
            num1 = float(input(pad + FUCSIA + "Ingresa el primer número (decimal/entero): " + RESET))
            break
        except ValueError:
            print(pad + MORADO + "Ingresa un valor numérico válido." + RESET)

    # Validar número 2
    while True:
        try:
            num2 = int(input(pad + FUCSIA + "Ingresa el segundo número (entero): " + RESET))
            break
        except ValueError:
            print(pad + MORADO + "Ingresa un número entero válido." + RESET)

    addition = num1 + num2
    average = addition / 2

    clear()
    Display.header("Ejercicio 2 - Cálculos Aritméticos")
    Display.row(f"Número 1 ingresado : {num1}", MORADO)
    Display.row(f"Número 2 ingresado : {num2}", MORADO)
    Display.empty()
    Display.row(f"Resultado de la Suma : {addition}", FUCSIA)
    Display.row(f"Resultado del Promedio : {average}", FUCSIA)
    Display.footer()