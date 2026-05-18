import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercicio 2------------------------------------------------------------------------------------
class ValidatedProduct:
    def __init__(self, code: str, name: str, price: float):
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.code  = code
        self.name  = name
        self.price = price

def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Validación de Precio")
    Display.row("Intentando crear un producto válido (Laptop, $900):", FUCSIA)
    Display.empty()

    try:
        prod_ok = ValidatedProduct("P001", "Laptop", 900.0)
        Display.row(f"¡Éxito! Creado: {prod_ok.name} : ${prod_ok.price}", MORADO)
    except ValueError as e:
        Display.row(f"Error inesperado: {e}", MORADO)

    Display.empty()
    Display.row("Intentando crear un producto inválido (Mouse, -$10):", FUCSIA)
    Display.empty()

    try:
        ValidatedProduct("P002", "Mouse", -10.0)
    except ValueError as e:
        Display.row(f"Validación exitosa. Error atrapado correctamente:", MORADO)
        Display.row(f"Error: {e}", MORADO)
    Display.footer()