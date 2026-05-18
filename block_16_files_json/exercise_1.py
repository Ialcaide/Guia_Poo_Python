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

# Configuración de rutas para la carpeta data
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_PATH, exist_ok=True)

# Ejercicio 1 ------------------------------------------------------------

def exercise_1():
    clear()
    Display.header("Ejercicio 1 - Escribir 'Python' en un archivo")
    
    file_path = os.path.join(DATA_PATH, "ejercicio1.txt")
    
    # 1. Escribimos la palabra "Python" en el archivo
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Python\n")
    
    Display.row("Texto 'Python' guardado con f.write().", FUCSIA)
    Display.empty()

    # 2. Leemos el archivo directamente
    with open(file_path, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
        
    Display.row(f"Texto leído desde el archivo: {contenido}", MORADO)
    Display.footer()