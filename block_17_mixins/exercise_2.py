import os
from core.display import Display
try:
    from core.mixins import ValidacionMixin
except ImportError:

    FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Ejercicio 2 ------------------------------------------------------------
class Usuario(ValidacionMixin):
    def __init__(self, name: str, email: str, age: int):
        # Ejecutamos las validaciones heredadas del Mixin
        self.validate_email(email)
        self.validate_age(age)
        self.name  = name
        self.email = email
        self.age   = age

    def display(self):
        Display.row(f"Nombre : {self.name}", FUCSIA)
        Display.row(f"Email  : {self.email}", MORADO)
        Display.row(f"Edad   : {self.age} años", MORADO)


def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Probando Reglas de ValidacionMixin")
    Display.row("ESCENARIO A: Enviando datos válidos definidos...", FUCSIA)
    Display.empty()
    
    user_valido = Usuario("Ana Gómez", "ana@correo.com", 22)
    user_valido.display()
    
    Display.empty()
    Display.row("-" * (Display.WIDTH - 4), FUCSIA)
    Display.empty()
    Display.row("ESCENARIO B: Enviando datos inválidos (Menor de edad)...", FUCSIA)
    Display.empty()
    
    try:
        # Esto va a fallar a propósito porque la edad es menor a 18
        user_invalido = Usuario("Pedrito", "pedro@correo.com", 15)
        user_invalido.display()
    except ValueError as error:
        # El Mixin lanza el error y lo atrapamos de forma escolar sencilla
        Display.row(f"[Validación Bloqueada]: {error}", FUCSIA)
    
    Display.footer()
