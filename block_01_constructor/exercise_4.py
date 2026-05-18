import os
from core.display import Display
from typing import Dict, Any, Optional, List

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Ejercicio 4------------------------------------------------------------------------------------
class Student:
    def __init__(self, name: str, grades: Optional[List[float]] = None):
        if not name.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.name   = name
        self.grades = grades if grades is not None else []

    @classmethod
    def from_dictionary(cls, data: Dict[str, Any]):
        if "name" not in data:
            raise KeyError("El diccionario debe incluir la llave 'name'")
        return cls(name=data["name"], grades=data.get("grades", None))

def exercise_4():
    clear()
    Display.header("Ejercicio 4 - Método de Clase (classmethod)")
    Display.row("Creando una instancia a partir de un diccionario de datos:", FUCSIA)
    Display.empty()

    sample_data = {"name": "Carlos Perez", "grades": [8.5, 9.0, 10.0]}
    Display.row(f"Diccionario de entrada:", MORADO)
    Display.row(f" {sample_data}", MORADO)
    Display.empty()

    new_student = Student.from_dictionary(sample_data)
    Display.row(f"Objeto creado -> Estudiante: {new_student.name}", MORADO)
    Display.row(f"Objeto creado -> Notas: {new_student.grades}", MORADO)
    Display.footer()