"""
PRUEBA TÉCNICA: FUNDAMENTOS DE PYTHON
=====================================

Instrucciones:
- Implementa cada función siguiendo los enunciados
- Mantén los nombres de las funciones exactamente como están
- No modifiques las docstrings
- Puedes agregar código auxiliar si es necesario

Para ejecutar las pruebas:
python -m pytest test.py -v
"""

import json
import os


# =============================================================================
# 1. 🛠️ VARIABLES Y TIPOS DE DATOS
# =============================================================================

def ejercicio_variables():
    """
    Crea las siguientes variables con los tipos de datos especificados:
    - nombre: string con tu nombre
    - edad: entero con tu edad
    - altura: float con tu altura en metros
    - es_estudiante: booleano True si eres estudiante
    - hobbies: lista con al menos 3 hobbies
    - info_personal: diccionario con las claves 'ciudad' y 'profesion'
    
    Retorna una tupla con todas las variables en el orden mencionado.
    """
    # TODO: Implementa aquí tu código
    pass


def convertir_tipos(numero_str, precio_str):
    """
    Convierte los parámetros string a sus tipos apropiados:
    - numero_str: convertir a entero
    - precio_str: convertir a float
    
    Retorna una tupla (numero_int, precio_float)
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# 2. 🔄 CONDICIONALES Y BUCLES
# =============================================================================

def clasificar_edad(edad):
    """
    Clasifica una persona según su edad:
    - 0-12: "Niño"
    - 13-17: "Adolescente"
    - 18-64: "Adulto"
    - 65+: "Adulto Mayor"
    
    Args:
        edad (int): La edad de la persona
        
    Returns:
        str: La clasificación correspondiente
    """
    # TODO: Implementa aquí tu código
    pass


def numeros_pares(limite):
    """
    Genera una lista con todos los números pares desde 0 hasta el límite (inclusive).
    
    Args:
        limite (int): El número límite
        
    Returns:
        list: Lista de números pares
    """
    # TODO: Implementa aquí tu código
    pass


def tabla_multiplicar(numero):
    """
    Genera la tabla de multiplicar del número dado (del 1 al 10).
    
    Args:
        numero (int): El número para generar su tabla
        
    Returns:
        list: Lista de tuplas (multiplicando, resultado)
        Ejemplo: [(1, 5), (2, 10), (3, 15), ...] para numero=5
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# 3. 🧠 FUNCIONES
# =============================================================================

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: π * radio²
    Usa 3.14159 como valor de π
    
    Args:
        radio (float): El radio del círculo
        
    Returns:
        float: El área del círculo
    """
    # TODO: Implementa aquí tu código
    pass


def es_palindromo(texto):
    """
    Verifica si un texto es palíndromo (se lee igual de izquierda a derecha).
    Ignora espacios, mayúsculas y minúsculas.
    
    Args:
        texto (str): El texto a verificar
        
    Returns:
        bool: True si es palíndromo, False si no
    """
    # TODO: Implementa aquí tu código
    pass


def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n (int): El número para calcular su factorial
        
    Returns:
        int: El factorial del número
    """
    # TODO: Implementa aquí tu código
    pass


def fibonacci(n):
    """
    Genera los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n (int): Cantidad de números a generar
        
    Returns:
        list: Lista con los números de Fibonacci
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# 4. 🏫 CLASES
# =============================================================================

class Vehiculo:
    """
    Clase base para representar un vehículo.
    """
    
    def __init__(self, marca, modelo, año):
        """
        Inicializa un vehículo.
        
        Args:
            marca (str): La marca del vehículo
            modelo (str): El modelo del vehículo
            año (int): El año del vehículo
        """
        # TODO: Implementa el constructor
        pass
    
    def arrancar(self):
        """
        Simula el arranque del vehículo.
        
        Returns:
            str: Mensaje de arranque
        """
        # TODO: Implementa este método
        pass
    
    def detener(self):
        """
        Simula la detención del vehículo.
        
        Returns:
            str: Mensaje de detención
        """
        # TODO: Implementa este método
        pass


class Coche(Vehiculo):
    """
    Clase que representa un coche, hereda de Vehículo.
    """
    
    def __init__(self, marca, modelo, año, num_puertas):
        """
        Inicializa un coche.
        
        Args:
            marca (str): La marca del coche
            modelo (str): El modelo del coche
            año (int): El año del coche
            num_puertas (int): Número de puertas del coche
        """
        # TODO: Implementa el constructor (usa super())
        pass
    
    def abrir_maletero(self):
        """
        Simula la apertura del maletero.
        
        Returns:
            str: Mensaje de apertura del maletero
        """
        # TODO: Implementa este método
        pass


class CuentaBancaria:
    """
    Clase para representar una cuenta bancaria.
    """
    
    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa una cuenta bancaria.
        
        Args:
            titular (str): El titular de la cuenta
            saldo_inicial (float): El saldo inicial (por defecto 0)
        """
        # TODO: Implementa el constructor
        # El saldo debe ser un atributo privado (_saldo)
        pass
    
    def depositar(self, cantidad):
        """
        Deposita dinero en la cuenta.
        
        Args:
            cantidad (float): Cantidad a depositar
            
        Returns:
            bool: True si el depósito fue exitoso, False si no
        """
        # TODO: Implementa este método
        # Solo permite depósitos de cantidades positivas
        pass
    
    def retirar(self, cantidad):
        """
        Retira dinero de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar
            
        Returns:
            bool: True si el retiro fue exitoso, False si no
        """
        # TODO: Implementa este método
        # Solo permite retiros si hay saldo suficiente y cantidad positiva
        pass
    
    def consultar_saldo(self):
        """
        Consulta el saldo actual de la cuenta.
        
        Returns:
            float: El saldo actual
        """
        # TODO: Implementa este método
        pass


# =============================================================================
# 5. 📦 MÓDULOS Y PAQUETES
# =============================================================================

def usar_modulos():
    """
    Demuestra el uso de módulos estándar de Python.
    
    Returns:
        dict: Diccionario con la siguiente información:
        {
            'fecha_actual': fecha actual en formato 'YYYY-MM-DD',
            'numero_aleatorio': número aleatorio entre 1 y 100,
            'raiz_cuadrada_64': raíz cuadrada de 64,
            'seno_90_grados': seno de 90 grados en radianes
        }
    """
    # TODO: Implementa aquí tu código
    # Usa los módulos: datetime, random, math
    pass


# =============================================================================
# 6. 📂 LECTURA Y ESCRITURA DE ARCHIVOS
# =============================================================================

def escribir_archivo(nombre_archivo, contenido):
    """
    Escribe contenido en un archivo de texto.
    
    Args:
        nombre_archivo (str): El nombre del archivo
        contenido (str): El contenido a escribir
        
    Returns:
        bool: True si se escribió correctamente, False si no
    """
    # TODO: Implementa aquí tu código
    pass


def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo de texto.
    
    Args:
        nombre_archivo (str): El nombre del archivo
        
    Returns:
        str: El contenido del archivo, o None si no existe
    """
    # TODO: Implementa aquí tu código
    pass


def procesar_csv_simple(datos):
    """
    Procesa una lista de diccionarios y la guarda en formato CSV simple.
    
    Args:
        datos (list): Lista de diccionarios con las claves 'nombre', 'edad', 'ciudad'
        
    Returns:
        str: String en formato CSV con headers
        Ejemplo: "nombre,edad,ciudad\nJuan,25,Madrid\n..."
    """
    # TODO: Implementa aquí tu código
    pass


def manejar_json(datos, nombre_archivo):
    """
    Guarda datos en formato JSON y luego los lee.
    
    Args:
        datos (dict): Diccionario con datos a guardar
        nombre_archivo (str): Nombre del archivo JSON
        
    Returns:
        dict: Los datos leídos del archivo JSON
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# 7. ⚠️ MANEJO DE ERRORES (try/except)
# =============================================================================

def division_segura(a, b):
    """
    Realiza una división manejando posibles errores.
    
    Args:
        a (float): El dividendo
        b (float): El divisor
        
    Returns:
        dict: Diccionario con 'resultado' y 'error'
        Si es exitoso: {'resultado': valor, 'error': None}
        Si hay error: {'resultado': None, 'error': mensaje_de_error}
    """
    # TODO: Implementa aquí tu código
    # Maneja ZeroDivisionError y TypeError
    pass


def acceder_lista_seguro(lista, indice):
    """
    Accede a un elemento de la lista manejando posibles errores.
    
    Args:
        lista (list): La lista de elementos
        indice (int): El índice a acceder
        
    Returns:
        dict: Diccionario con 'valor' y 'error'
        Si es exitoso: {'valor': elemento, 'error': None}
        Si hay error: {'valor': None, 'error': mensaje_de_error}
    """
    # TODO: Implementa aquí tu código
    # Maneja IndexError y TypeError
    pass


def convertir_numero_seguro(texto):
    """
    Convierte un texto a número manejando posibles errores.
    
    Args:
        texto (str): El texto a convertir
        
    Returns:
        dict: Diccionario con 'numero' y 'tipo' y 'error'
        Si es entero: {'numero': valor, 'tipo': 'int', 'error': None}
        Si es float: {'numero': valor, 'tipo': 'float', 'error': None}
        Si hay error: {'numero': None, 'tipo': None, 'error': mensaje_de_error}
    """
    # TODO: Implementa aquí tu código
    # Intenta convertir primero a int, luego a float
    # Maneja ValueError
    pass


def validar_archivo_json(nombre_archivo):
    """
    Valida si un archivo existe y contiene JSON válido.
    
    Args:
        nombre_archivo (str): El nombre del archivo JSON
        
    Returns:
        dict: Diccionario con 'valido', 'datos' y 'error'
        Si es válido: {'valido': True, 'datos': contenido, 'error': None}
        Si hay error: {'valido': False, 'datos': None, 'error': mensaje_de_error}
    """
    # TODO: Implementa aquí tu código
    # Maneja FileNotFoundError y json.JSONDecodeError
    pass


if __name__ == "__main__":
    print("🐍 PRUEBA TÉCNICA: FUNDAMENTOS DE PYTHON")
    print("=" * 50)
    print("Para ejecutar las pruebas, usa: python -m pytest test.py -v")
    print("\nEjercicios disponibles:")
    print("1. 🛠️  Variables y tipos de datos")
    print("2. 🔄 Condicionales y bucles")
    print("3. 🧠 Funciones")
    print("4. 🏫 Clases")
    print("5. 📦 Módulos y paquetes")
    print("6. 📂 Lectura y escritura de archivos")
    print("7. ⚠️  Manejo de errores (try/except)")
