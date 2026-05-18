import os
from core.display import Display
try:
    from core.mixins import ExportarMixin
except ImportError:

    FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3 ------------------------------------------------------------
class Reporte(ExportarMixin):
    def __init__(self, data: dict):
        self.data = data

def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Mixin de Utilidad (ExportarMixin)")

    product_data = {
        "product" : "Laptop ASUS",
        "price"   : 850.00,
        "quantity": 3
    }

    reporte = Reporte(product_data)

    Display.row("Datos del producto serializados a JSON:", FUCSIA)
    Display.empty()
    
    json_completo = reporte.export_json(product_data)
    
    for linea in json_completo.split("\n"):
        if linea.strip():  
            Display.row(f"  {linea}", MORADO)
    
    Display.empty()
    Display.row("-" * (Display.WIDTH - 4), FUCSIA)
    Display.empty()
    
    Display.row("Datos del producto formateados a línea CSV:", FUCSIA)
    Display.empty()
    
    linea_csv = ", ".join(str(valor) for valor in product_data.values())
    
    Display.row(f"  -> {linea_csv}", MORADO)
    
    Display.footer()