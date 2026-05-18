import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercicio 1------------------------------------------------------------------------------------
class Product:
    def __init__(self, code: str, name: str, price: float):
        self.code  = code
        self.name  = name
        self.price = price

def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Instanciar Productos")
    Display.row("Creación e impresión de instancias de la clase Product:", FUCSIA)
    Display.empty()

    p1 = Product("P001", "Laptop", 900.0)
    p2 = Product("P002", "Mouse", 25.0)

    Display.row(f"Producto 1 -> Código: {p1.code} | Nombre: {p1.name} | Precio: ${p1.price}", MORADO)
    Display.empty()
    Display.row(f"Producto 2 -> Código: {p2.code} | Nombre: {p2.name} | Precio: ${p2.price}", MORADO)
    Display.footer()