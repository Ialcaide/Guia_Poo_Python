import os
from core.display import Display
from core.decorators_ex13 import  validate_positive

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2 ------------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Validación con Valores Definidos")

#Aplicamos el decorador importado
    @validate_positive  
    def square(x):
        result = x ** 2
        Display.row(f"Función: El cuadrado de {x} es {result}", MORADO)
        return result

    # Valores fijos definidos directamente en el código
    value_valid   = 5
    value_invalid = -3

    #Probando el caso correcto
    Display.row(f"ESCENARIO A: Enviando valor definido positivo ({value_valid})", MORADO)
    Display.empty()
    square(value_valid)
    
    Display.empty()
    Display.row("-" * (Display.WIDTH - 4), MORADO)
    Display.empty()

    #Probando el caso que debe fallar
    Display.row(f"ESCENARIO B: Enviando valor definido negativo ({value_invalid})", MORADO)
    Display.empty()
    square(value_invalid)
    
    Display.footer()
