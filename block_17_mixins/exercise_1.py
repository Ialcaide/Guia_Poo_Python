import os
from core.display import Display
try:
    from core.mixins import PromedioMixin
except ImportError:
    

    FUCSIA = "\033[38;2;255;0;127m"
    MORADO = "\033[38;2;148;0;211m"
    RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1 ------------------------------------------------------------
class Student(PromedioMixin):
    def __init__(self, name: str, grades: list):
        self.name   = name
        self.grades = grades

    def display(self):
        # Usamos el método heredado del Mixin
        average = self.calculate_average(self.grades)
        Display.row(f"Estudiante : {self.name}", FUCSIA)
        Display.row(f"Notas      : {self.grades}", MORADO)
        Display.row(f"Promedio   : {average}", MORADO)


def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Mixin de Cálculo (PromedioMixin)")

    # Datos definidos directamente de forma fija
    student_name = "Luis"
    student_grades = [8.5, 9.0, 7.5, 10.0]

    # Instanciamos y mostramos el comportamiento del Mixin
    student = Student(student_name, student_grades)
    student.display()
    
    Display.footer()

