import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# Ejercicio 3-----------------------------------------------------------------
class DataTypes:
    def __init__(self):
        self.texto: str  = "Hola Python"
        self.lista: list = ["manzana", "pera", "uva", "sandia", "mango"]
        self.diccionario: dict = {
            "nombre": "Juan",
            "edad": 25,
            "ciudad": "Guayaquil"
        }

    def display_data(self):
        Display.row("TIPO STR:", FUCSIA)
        Display.row(f"Texto completo      : {self.texto}", MORADO)
        Display.row(f"Primer carácter [0] : {self.texto[0]}", MORADO)
        Display.empty()

        Display.row("TIPO LIST:", FUCSIA)
        Display.row(f"Lista completa      : {self.lista}", MORADO)
        Display.row(f"Último elemento [-1]: {self.lista[-1]}", MORADO)
        Display.empty()

        Display.row("TIPO DICT:", FUCSIA)
        Display.row(f"Diccionario completo: {self.diccionario}", MORADO)
        Display.row(f"Valor de 'nombre'   : {self.diccionario['nombre']}", MORADO)


def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Clase con Tipos Compuestos")
    
    data = DataTypes()
    data.display_data()
    Display.footer()
