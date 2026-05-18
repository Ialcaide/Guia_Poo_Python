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

# Ejercicio 3 ------------------------------------------------------------

def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Lista de usuarios en JSON")
    
    file_path = os.path.join(DATA_PATH, "ejercicio3.json")

    # Definimos la lista fija con los datos de 2 usuarios (en formato inglés/llaves sencillas)
    usuarios = [
        {"name": "Ileana", "age": 21},
        {"name": "Caridad", "age": 18}
    ]

    # 1. Guardamos la lista completa en el archivo JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2)

    Display.row("Lista de 2 usuarios guardada en JSON con json.dump().", FUCSIA)
    Display.empty()

    # 2. Cargamos el archivo de vuelta a la variable 'loaded'
    with open(file_path, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    Display.row("Recorriendo y mostrando los usuarios cargados con un bucle for:", MORADO)
    Display.empty()

    # 3. Recorremos la estructura limpia con el ciclo for tal como pide el ejercicio
    for u in loaded:
        Display.row(f"Nombre: {u['name']} | Edad: {u['age']}", MORADO)

    Display.footer()
