import os
import json
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

# Ejercicio 2 ------------------------------------------------------------

def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Guardar y cargar JSON")
    
    file_path = os.path.join(DATA_PATH, "ejercicio2.json")

    # Definimos el diccionario fijo que pide el ejercicio
    datos = {"x": 10, "y": 20}

    # 1. Guardamos el diccionario en formato JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2)

    Display.row("Diccionario {'x': 10, 'y': 20} guardado con json.dump().", FUCSIA)
    Display.empty()

    # 2. Cargamos el archivo JSON de vuelta
    with open(file_path, "r", encoding="utf-8") as f:
        cargado = json.load(f)

    # Mostramos los valores cargados directamente
    Display.row("Datos cargados con json.load():", MORADO)
    Display.row(f"Valor de x: {cargado['x']}", MORADO)
    Display.row(f"Valor de y: {cargado['y']}", MORADO)
    Display.footer()
