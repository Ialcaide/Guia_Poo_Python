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

# Ejercicio 3---------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - El comportamiento de input()")
    Display.footer()
    
    pad = get_input_padding()
    number = input(pad + FUCSIA + "Ingresa un número cualquiera: " + RESET).strip()

    clear()
    Display.header("Ejercicio 3 - Análisis de Concatenación")
    Display.row(f"Valor capturado por teclado : '{number}'", MORADO)
    Display.row(f"Operación evaluada (n + '5') : '{number + '5'}'", FUCSIA)
    Display.empty()
    Display.row("EXPLICACIÓN TÉCNICA:", FUCSIA)
    Display.row("La función nativa input() SIEMPRE retorna un tipo de dato str (texto).", MORADO)
    Display.row("En Python, el operador (+) entre dos strings realiza una CONCATENACIÓN,", MORADO)
    Display.row("uniendo los textos en lugar de efectuar una suma matemática formal.", MORADO)
    Display.empty()
    Display.row(f"Por tal motivo: '{number}' + '5' da como resultado final '{number + '5'}'", MORADO)
    Display.row("Para poder realizar una suma matemática debes castear la entrada: int(input())", FUCSIA)
    Display.footer()
