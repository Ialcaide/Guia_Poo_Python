import os
import json
from functools import reduce
from core.display import Display
from core.navigator import Navigator
from menu.menu import Menu

try:
    from core.mixins import ExportarMixin
except ImportError:
    pass

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_input(prompt: str) -> str:
    cols    = Display.get_cols()
    padding = (cols - Display.WIDTH) // 2
    print(" " * (padding + 2), end="")
    return input(FUCSIA + f"  {prompt} " + RESET)


# bloque 0 - intro ------------------------------------------------------------
def exercise_block00():
    clear()
    # identifico 5 clases para un sistema de tienda
    class Product:
        def __init__(self, name: str, price: float):
            self.name  = name
            self.price = price

    class Customer:
        def __init__(self, name: str):
            self.name = name

    class Order:
        def __init__(self, product: Product, customer: Customer):
            self.product  = product
            self.customer = customer

    class Category:
        def __init__(self, name: str):
            self.name = name

    class Supplier:
        def __init__(self, name: str, country: str):
            self.name    = name
            self.country = country

    # creo instancias de cada clase
    product  = Product("Laptop", 900.0)
    customer = Customer("Daniel")
    order    = Order(product, customer)
    category = Category("Electronica")
    supplier = Supplier("Dell", "USA")

    Display.header("Extra Block 00 - Sistema de Tienda")
    Display.row("5 clases para modelar un sistema de tienda:", FUCSIA)
    Display.empty()
    Display.row(f"Product  : {product.name} | ${product.price}", MORADO)
    Display.row(f"Customer : {customer.name}", MORADO)
    Display.row(f"Order    : {order.product.name} -> {order.customer.name}", MORADO)
    Display.row(f"Category : {category.name}", MORADO)
    Display.row(f"Supplier : {supplier.name} ({supplier.country})", MORADO)
    Display.footer()


# bloque 1 - constructor ------------------------------------------------------------
def exercise_block01():
    clear()
    # clase vehiculo con constructor normal y classmethod
    class Vehicle:
        def __init__(self, brand: str, model: str, year: int):
    
            self.brand = brand
            self.model = model
            self.year  = year

        @classmethod
        def from_dictionary(cls, data: dict):
            return cls(data["brand"], data["model"], data["year"])

    # creo un vehiculo de forma normal
    v1 = Vehicle("Toyota", "Corolla", 2022)

    # creo un vehiculo desde un diccionario
    data = {"brand": "Honda", "model": "Civic", "year": 2023}
    v2   = Vehicle.from_dictionary(data)

    Display.header("Extra Block 01 - Clase Vehiculo")
    Display.row("Instancia normal:", FUCSIA)
    Display.row(f"  {v1.brand} {v1.model} ({v1.year})", MORADO)
    Display.empty()
    Display.row("Instancia desde diccionario:", FUCSIA)
    Display.row(f"  {v2.brand} {v2.model} ({v2.year})", MORADO)
    Display.footer()


# bloque 2 - variables ------------------------------------------------------------
def exercise_block02():
    clear()
    # declaro variables de cada tipo
    my_text   : str   = "Hola Mundo"
    my_number : float = 45.5
    my_bool   : bool  = True
    my_none           = None

    # tipos complejos
    my_list  = [my_text, my_number, my_bool]
    my_dict  = {"texto": my_text, "numero": my_number}
    my_tuple = (my_text, my_number)
    my_set   = {my_text, my_number}

    Display.header("Extra Block 02 - Tipos de Datos")
    Display.row("Tipos simples:", FUCSIA)
    Display.row(f"  str   : {my_text}", MORADO)
    Display.row(f"  float : {my_number}", MORADO)
    Display.row(f"  bool  : {my_bool}", MORADO)
    Display.row(f"  None  : {my_none}", MORADO)
    Display.empty()
    Display.row("Tipos complejos:", FUCSIA)
    Display.row(f"  list  : {my_list}", MORADO)
    Display.row(f"  dict  : {my_dict}", MORADO)
    Display.row(f"  tuple : {my_tuple}", MORADO)
    Display.row(f"  set   : {my_set}", MORADO)
    Display.footer()


# bloque 3 - operators ------------------------------------------------------------
def exercise_block03():
    clear()
    # valores fijos para demostrar los operadores
    a = 10
    b = 3

    Display.header("Extra Block 03 - Operadores")
    Display.row(f"a = {a}, b = {b}", FUCSIA)
    Display.empty()
    Display.row(f"a + b  = {a + b}    (suma)", MORADO)
    Display.row(f"a - b  = {a - b}    (resta)", MORADO)
    Display.row(f"a * b  = {a * b}   (multiplicacion)", MORADO)
    Display.row(f"a / b  = {a / b:.2f}  (division decimal)", MORADO)
    Display.row(f"a // b = {a // b}    (division entera)", MORADO)
    Display.row(f"a % b  = {a % b}    (modulo)", MORADO)
    Display.row(f"a ** b = {a ** b}  (potencia)", MORADO)
    Display.empty()
    Display.row(f"a == b : {a == b}  (igual)", FUCSIA)
    Display.row(f"a > b  : {a > b}   (mayor)", FUCSIA)
    Display.footer()


# bloque 4 - input output - REQUIERE INPUT ------------------------------------------------------------
def exercise_block04():
    clear()
    Display.header("Extra Block 04 - Perfil de Usuario")
    Display.row("Ingresa tus datos para crear tu perfil:", FUCSIA)
    Display.footer()

    # pido los datos al usuario
    while True:
        name = get_input("Tu nombre:").strip()
        if name:
            break
        Display.header("Error")
        Display.row("El nombre no puede estar vacio.", MORADO)
        Display.footer()

    while True:
        try:
            age = int(get_input("Tu edad  :"))
            if age < 0:
                raise ValueError
            break
        except ValueError:
            Display.header("Error")
            Display.row("Ingresa una edad valida.", MORADO)
            Display.footer()

    while True:
        city = get_input("Tu ciudad:").strip()
        if city:
            break
        Display.header("Error")
        Display.row("La ciudad no puede estar vacia.", MORADO)
        Display.footer()

    # muestro el perfil con f-string
    Display.header("Tu Perfil")
    Display.row(f"Hola {name}!", FUCSIA)
    Display.row(f"Tienes {age} anos y vives en {city}.", MORADO)
    Display.row(f"En 5 años tendras {age + 5} anos.", MORADO)
    Display.footer()


# bloque 5 - conditionals - REQUIERE INPUT ------------------------------------------------------------
def exercise_block05():
    clear()
    Display.header("Extra Block 05 - Clasificador de Temperatura")
    Display.footer()

    # pido la temperatura al usuario
    while True:
        try:
            temp = float(get_input("Temperatura en grados C:"))
            break
        except ValueError:
            Display.header("Error")
            Display.row("Ingresa un numero valido.", MORADO)
            Display.footer()

    # clasifico la temperatura con condicionales
    if temp < 0:
        message = "Bajo cero, hace mucho frio!"
    elif temp < 15:
        message = "Frio, abrigate bien."
    elif temp < 25:
        message = "Temperatura agradable."
    elif temp < 35:
        message = "Calor moderado."
    else:
        message = "Mucho calor!"

    Display.header("Resultado")
    Display.row(f"Temperatura : {temp}°C", FUCSIA)
    Display.row(f"Clasificacion: {message}", MORADO)
    Display.footer()


# bloque 6 - loops ------------------------------------------------------------
def exercise_block06():
    clear()
    # tabla de multiplicar del 7 con for
    num = 7

    Display.header("Extra Block 06 - Tabla de Multiplicar")
    Display.row(f"Tabla del {num}:", FUCSIA)
    Display.empty()

    for i in range(1, 11):
        Display.row(f"  {num} x {i:2} = {num * i}", MORADO)

    Display.footer()


# bloque 7 - functions ------------------------------------------------------------
def exercise_block07():
    clear()
    # funciones que retornan multiples valores
    def calculate(x, y):
        return x + y, x * y

    # funcion recursiva simple
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    sum_result, mult_result = calculate(8, 5)
    fact_result             = factorial(5)

    Display.header("Extra Block 07 - Funciones")
    Display.row("Funcion con retorno multiple:", FUCSIA)
    Display.row(f"  calculate(8, 5) -> suma={sum_result}, mult={mult_result}", MORADO)
    Display.empty()
    Display.row("Funcion recursiva:", FUCSIA)
    Display.row(f"  factorial(5) = {fact_result}", MORADO)
    Display.footer()


# bloque 8 - lists ------------------------------------------------------------
def exercise_block08():
    clear()
    # lista de productos de compra
    shopping_list = ["Leche", "Pan", "Manzana", "Arroz"]

    # agrego 3 elementos con append
    shopping_list.append("Huevos")
    shopping_list.append("Queso")
    shopping_list.append("Agua")

    # ordeno la lista
    shopping_list.sort()

    Display.header("Extra Block 08 - Lista de Compras")
    Display.row("Lista ordenada con append() y sort():", FUCSIA)
    Display.empty()

    for i, item in enumerate(shopping_list, 1):
        Display.row(f"  {i}. {item}", MORADO)

    Display.empty()
    Display.row(f"Total productos: {len(shopping_list)}", FUCSIA)
    Display.footer()


# bloque 9 - tuples ------------------------------------------------------------
def exercise_block09():
    clear()
    # lista de coordenadas como tuplas
    coordinates = [
        (40.71, -74.00, "New York"),
        (-0.18, -78.46, "Quito"),
        (51.50, -0.12,  "London"),
    ]

    Display.header("Extra Block 09 - Coordenadas GPS")
    Display.row("Recorriendo coordenadas con unpacking:", FUCSIA)
    Display.empty()

    # desempaqueto cada tupla en el for
    for lat, lon, city in coordinates:
        Display.row(f"  {city:<10} | lat: {lat} | lon: {lon}", MORADO)

    Display.footer()


# bloque 10 - dictionaries ------------------------------------------------------------
def exercise_block10():
    clear()
    # diccionario de contactos
    contacts = {
        "Daniel": "099123456",
        "Ana"   : "099888777",
        "Luis"  : "099555333"
    }

    Display.header("Extra Block 10 - Agenda de Contactos")
    Display.row("Acceso con [] y con get():", FUCSIA)
    Display.empty()

    # acceso directo con []
    Display.row(f"contacts['Daniel'] = {contacts['Daniel']}", MORADO)

    # acceso seguro con get()
    Display.row(f"contacts.get('Ana') = {contacts.get('Ana')}", MORADO)
    Display.row(f"contacts.get('Pedro', 'No existe') = {contacts.get('Pedro', 'No existe')}", MORADO)
    Display.empty()

    # itero sobre todos los contactos
    Display.row("Todos los contactos:", FUCSIA)
    for name, phone in contacts.items():
        Display.row(f"  {name:<10} : {phone}", MORADO)

    Display.footer()


# bloque 11 - sets ------------------------------------------------------------
def exercise_block11():
    clear()
    # dos conjuntos de materias
    student_1 = {"Matematicas", "Fisica", "POO", "Ingles"}
    student_2 = {"POO", "Ingles", "Quimica", "Historia"}

    Display.header("Extra Block 11 - Materias en Comun")
    Display.row(f"Estudiante 1: {student_1}", FUCSIA)
    Display.row(f"Estudiante 2: {student_2}", FUCSIA)
    Display.empty()

    # operaciones de conjuntos
    Display.row(f"Comunes (&)    : {student_1 & student_2}", MORADO)
    Display.row(f"Todas   (|)    : {student_1 | student_2}", MORADO)
    Display.row(f"Solo est1 (-)  : {student_1 - student_2}", MORADO)
    Display.row(f"Solo est2 (-)  : {student_2 - student_1}", MORADO)
    Display.footer()


# bloque 12 - exceptions - REQUIERE INPUT ------------------------------------------------------------
def exercise_block12():
    clear()
    Display.header("Extra Block 12 - Calculadora Segura")
    Display.footer()

    # pido dos numeros al usuario
    while True:
        try:
            dividend = float(get_input("Ingresa el dividendo:"))
            divisor  = float(get_input("Ingresa el divisor  :"))
            result   = dividend / divisor
            Display.header("Resultado")
            Display.row(f"{dividend} / {divisor} = {result}", FUCSIA)
            Display.footer()
            break
        except ValueError:
            Display.header("Error")
            Display.row("Ingresa solo numeros.", MORADO)
            Display.footer()
        except ZeroDivisionError:
            Display.header("Error")
            Display.row("No se puede dividir entre cero.", MORADO)
            Display.footer()


# bloque 13 - decorators ------------------------------------------------------------
def exercise_block13():
    clear()
    # decorador que imprime antes y despues de ejecutar
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            Display.row("[Iniciando funcion...]", FUCSIA)
            result = func(*args, **kwargs)
            Display.row("[Funcion finalizada.]", FUCSIA)
            return result
        return wrapper

    # aplico el decorador con @
    @log_decorator
    def greet(name):
        Display.row(f"   Hola, {name}!", MORADO)

    Display.header("Extra Block 13 - Decorador")
    Display.empty()
    greet("Daniel")
    Display.footer()


# bloque 14 - unpacking ------------------------------------------------------------
def exercise_block14():
    clear()
    # desempaqueto una lista con *
    data = ["Daniel", 20, "Ecuador", "POO", "Fisica"]
    name, age, country, *subjects = data

    # combino dos diccionarios con **
    dict_1   = {"name": name, "age": age}
    dict_2   = {"country": country, "subjects": subjects}
    combined = {**dict_1, **dict_2}

    Display.header("Extra Block 14 - Unpacking")
    Display.row("Desempaquetado con *:", FUCSIA)
    Display.row(f"  name     = {name}", MORADO)
    Display.row(f"  age      = {age}", MORADO)
    Display.row(f"  country  = {country}", MORADO)
    Display.row(f"  subjects = {subjects}", MORADO)
    Display.empty()
    Display.row("Diccionarios combinados con **:", FUCSIA)
    Display.row(f"  {combined}", MORADO)
    Display.footer()


# bloque 15 - higher order ------------------------------------------------------------
def exercise_block15():
    clear()
    # lista de numeros para demostrar map, filter y reduce
    numbers = [1, 2, 3, 4, 5, 6]

    # map - elevo al cuadrado cada elemento
    squares = list(map(lambda x: x ** 2, numbers))

    # filter - solo los pares
    evens = list(filter(lambda x: x % 2 == 0, numbers))

    # reduce - suma total
    total = reduce(lambda x, y: x + y, numbers)

    Display.header("Extra Block 15 - map, filter y reduce")
    Display.row(f"Lista original : {numbers}", FUCSIA)
    Display.empty()
    Display.row(f"map (x²)       : {squares}", MORADO)
    Display.row(f"filter (pares) : {evens}", MORADO)
    Display.row(f"reduce (suma)  : {total}", MORADO)
    Display.footer()


# bloque 16 - files json ------------------------------------------------------------
def exercise_block16():
    clear()
    # guardo un inventario en json y lo cargo
    file_path = os.path.join("data", "extra_inventory.json")
    os.makedirs("data", exist_ok=True)

    # datos fijos del inventario
    inventory = [
        {"product": "Teclado", "price": 45.0},
        {"product": "Mouse",   "price": 20.0},
    ]

    # guardo en json
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)

    # cargo el json
    with open(file_path, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    Display.header("Extra Block 16 - Archivos JSON")
    Display.row(f"Guardado en: {file_path}", FUCSIA)
    Display.empty()
    Display.row("Datos cargados:", FUCSIA)

    for item in loaded:
        Display.row(f"  {item['product']:<10} : ${item['price']}", MORADO)

    Display.footer()


# bloque 17 - mixins ------------------------------------------------------------
def exercise_block17():
    clear()

    # clase que hereda de ExportarMixin
    class Report(ExportarMixin):
        def __init__(self, data: dict):
            self.data = data

    # datos fijos del reporte
    report_data = {"subject": "POO", "grade": 9.5, "status": "Aprobado"}
    report      = Report(report_data)

    # exporto en json y csv usando el mixin
    json_output = report.export_json(report_data)

    Display.header("Extra Block 17 - Mixins (ExportarMixin)")
    Display.row("Datos del reporte:", FUCSIA)
    Display.empty()

    for line in json_output.split("\n"):
        if line.strip():
            Display.row(f"  {line}", MORADO)

    Display.empty()
    Display.row("Exportado en CSV:", FUCSIA)
    Display.empty()
    

    csv_valores = ", ".join(str(valor) for valor in report_data.values()).strip()
    
    Display.row(f"  -> {csv_valores}", MORADO)
    Display.footer()


# menu para ejercicios extra ------------------------------------------------------------
def run_menu():
    block_menu = Menu("Ejercicios Extra", [
        "Block 00 - Sistema de Tienda",
        "Block 01 - Clase Vehiculo",
        "Block 02 - Tipos de datos del usuario",
        "Block 03 - Calculadora de operadores",
        "Block 04 - Perfil de usuario",
        "Block 05 - Clasificador de temperatura",
        "Block 06 - Tabla de multiplicar",
        "Block 07 - Calculadora con funciones",
        "Block 08 - Lista de compras",
        "Block 09 - Coordenadas GPS",
        "Block 10 - Agenda de contactos",
        "Block 11 - Materias en comun",
        "Block 12 - Calculadora segura",
        "Block 13 - Decorador de tiempo",
        "Block 14 - Unpacking de estudiantes",
        "Block 15 - map, filter y reduce",
        "Block 16 - Inventario en JSON",
        "Block 17 - Sistema de Reportes",
    ])

    current_exercise = None

    while True:
        if current_exercise is None:
            block_menu.display()
            choice = block_menu.get_choice()
            if choice == 0:
                break
            else:
                current_exercise = choice

        if current_exercise == 1:
            exercise_block00()
            current_exercise = Navigator.navigate(1, 18, has_input=False)
        elif current_exercise == 2:
            exercise_block01()
            current_exercise = Navigator.navigate(2, 18, has_input=False)
        elif current_exercise == 3:
            exercise_block02()
            current_exercise = Navigator.navigate(3, 18, has_input=False)
        elif current_exercise == 4:
            exercise_block03()
            current_exercise = Navigator.navigate(4, 18, has_input=False)
        elif current_exercise == 5:
            exercise_block04()
            current_exercise = Navigator.navigate(5, 18, has_input=True)
        elif current_exercise == 6:
            exercise_block05()
            current_exercise = Navigator.navigate(6, 18, has_input=True)
        elif current_exercise == 7:
            exercise_block06()
            current_exercise = Navigator.navigate(7, 18, has_input=False)
        elif current_exercise == 8:
            exercise_block07()
            current_exercise = Navigator.navigate(8, 18, has_input=False)
        elif current_exercise == 9:
            exercise_block08()
            current_exercise = Navigator.navigate(9, 18, has_input=False)
        elif current_exercise == 10:
            exercise_block09()
            current_exercise = Navigator.navigate(10, 18, has_input=False)
        elif current_exercise == 11:
            exercise_block10()
            current_exercise = Navigator.navigate(11, 18, has_input=False)
        elif current_exercise == 12:
            exercise_block11()
            current_exercise = Navigator.navigate(12, 18, has_input=False)
        elif current_exercise == 13:
            exercise_block12()
            current_exercise = Navigator.navigate(13, 18, has_input=True)
        elif current_exercise == 14:
            exercise_block13()
            current_exercise = Navigator.navigate(14, 18, has_input=False)
        elif current_exercise == 15:
            exercise_block14()
            current_exercise = Navigator.navigate(15, 18, has_input=False)
        elif current_exercise == 16:
            exercise_block15()
            current_exercise = Navigator.navigate(16, 18, has_input=False)
        elif current_exercise == 17:
            exercise_block16()
            current_exercise = Navigator.navigate(17, 18, has_input=False)
        elif current_exercise == 18:
            exercise_block17()
            current_exercise = Navigator.navigate(18, 18, has_input=False)

        if current_exercise == 0:
            current_exercise = None