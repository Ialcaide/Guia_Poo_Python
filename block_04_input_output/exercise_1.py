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

# Ejercicio 1---------------------------------------------------------
def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Formateo de Cadenas (f-string)")
    Display.footer()
    
    pad = get_input_padding()

    # Validar nombre
    while True:
        name = Display.input_at("Ingresa nombre:")
        if name:
            break
        print(pad + MORADO + "El nombre no puede estar vacío. Inténtalo de nuevo." + RESET)

    # Validar edad
    while True:
        try:
            age = Display.input_at("Ingresa edad:")
            if age < 0:
                print(pad + MORADO + "La edad no puede ser negativa." + RESET)
            else:
                break
        except ValueError:
            print(pad + MORADO + "Por favor, ingresa un número entero válido." + RESET)

    clear()
    Display.header("Ejercicio 1 - Resultado")
    Display.row(f"Hola {name}, actualmente tienes {age} años.", MORADO)
    Display.empty()
    Display.row(f"En una década (10 años) tendrás {age + 10} años.", FUCSIA)
    Display.footer()
