# decorators/loggers.py
from core.display import Display
from core.navigator import Navigator

# Colores necesarios para la interfaz gráfica
FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"

#ejercicio 1 bloque 13-------------------------------------------------
def log_simple(func):
    def wrapper(*args, **kwargs):
        Display.row("[Decorador]: Iniciando...", FUCSIA)
        Display.empty()
        result = func(*args, **kwargs)  # Ejecuta la función original (saludar)
        return result
    return wrapper

#ejercicio 2 bloque 13-------------------------------------------------

def validate_positive(func):
#Decorador Ejercicio 2: Valida que el argumento sea mayor o igual a cero."""
    def wrapper(x):
        if x < 0:
            Display.row(f"[Error]: El valor {x} no es positivo.", FUCSIA)
            return None
        return func(x)
    return wrapper

#ejercicio 3 bloque 13-------------------------------------------------

def log_advanced(func):
#Decorador Ejercicio 3: Inspecciona el nombre de la función y su resultado."""
    def wrapper(*args, **kwargs):
        Display.row(f"[Decorador]: Llamando a la función '{func.__name__}'...", FUCSIA)
        Display.empty()
        result = func(*args, **kwargs)  # Ejecuta la función original (suma)
        Display.row(f"[Decorador]: Resultado retornado: {result}", FUCSIA)
        return result
    return wrapper