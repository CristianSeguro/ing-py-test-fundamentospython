"""
Tests para la prueba técnica de fundamentos de Python.
Ejecutar con: python -m pytest test.py -v
"""

import pytest
import os
import json
import tempfile
# from main import *
from ejemplo_implementacion import *


class TestVariablesYTipos:
    """Tests para ejercicios de variables y tipos de datos."""
    
    def test_ejercicio_variables(self):
        """Test para verificar que se crean las variables correctamente."""
        resultado = ejercicio_variables()
        
        assert isinstance(resultado, tuple), "Debe retornar una tupla"
        assert len(resultado) == 6, "La tupla debe tener 6 elementos"
        
        nombre, edad, altura, es_estudiante, hobbies, info_personal = resultado
        
        assert isinstance(nombre, str), "nombre debe ser string"
        assert isinstance(edad, int), "edad debe ser entero"
        assert isinstance(altura, float), "altura debe ser float"
        assert isinstance(es_estudiante, bool), "es_estudiante debe ser booleano"
        assert isinstance(hobbies, list), "hobbies debe ser lista"
        assert len(hobbies) >= 3, "hobbies debe tener al menos 3 elementos"
        assert isinstance(info_personal, dict), "info_personal debe ser diccionario"
        assert 'ciudad' in info_personal, "info_personal debe tener clave 'ciudad'"
        assert 'profesion' in info_personal, "info_personal debe tener clave 'profesion'"
    
    def test_convertir_tipos(self):
        """Test para verificar conversión de tipos."""
        numero_int, precio_float = convertir_tipos("42", "19.99")
        
        assert isinstance(numero_int, int), "Debe retornar un entero"
        assert isinstance(precio_float, float), "Debe retornar un float"
        assert numero_int == 42, "El número debe ser 42"
        assert precio_float == 19.99, "El precio debe ser 19.99"


class TestCondicionalesYBucles:
    """Tests para ejercicios de condicionales y bucles."""
    
    def test_clasificar_edad(self):
        """Test para clasificación por edad."""
        assert clasificar_edad(8) == "Niño"
        assert clasificar_edad(15) == "Adolescente"
        assert clasificar_edad(25) == "Adulto"
        assert clasificar_edad(70) == "Adulto Mayor"
        assert clasificar_edad(12) == "Niño"
        assert clasificar_edad(13) == "Adolescente"
        assert clasificar_edad(64) == "Adulto"
        assert clasificar_edad(65) == "Adulto Mayor"
    
    def test_numeros_pares(self):
        """Test para generar números pares."""
        resultado = numeros_pares(10)
        esperado = [0, 2, 4, 6, 8, 10]
        assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"
        
        resultado = numeros_pares(5)
        esperado = [0, 2, 4]
        assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"
    
    def test_tabla_multiplicar(self):
        """Test para tabla de multiplicar."""
        resultado = tabla_multiplicar(5)
        esperado = [(1, 5), (2, 10), (3, 15), (4, 20), (5, 25), 
                   (6, 30), (7, 35), (8, 40), (9, 45), (10, 50)]
        assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"


class TestFunciones:
    """Tests para ejercicios de funciones."""
    
    def test_calcular_area_circulo(self):
        """Test para cálculo de área del círculo."""
        area = calcular_area_circulo(5)
        esperado = 3.14159 * 25  # π * r²
        assert abs(area - esperado) < 0.001, f"Área incorrecta: {area}"
        
        area = calcular_area_circulo(1)
        esperado = 3.14159
        assert abs(area - esperado) < 0.001, f"Área incorrecta: {area}"
    
    def test_es_palindromo(self):
        """Test para verificar palíndromos."""
        assert es_palindromo("ana") == True
        assert es_palindromo("Ana") == True
        assert es_palindromo("A man a plan a canal Panama") == True
        assert es_palindromo("racecar") == True
        assert es_palindromo("hello") == False
        assert es_palindromo("Python") == False
    
    def test_factorial(self):
        """Test para cálculo de factorial."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(4) == 24
    
    def test_fibonacci(self):
        """Test para secuencia de Fibonacci."""
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
        assert fibonacci(0) == []


class TestClases:
    """Tests para ejercicios de clases."""
    
    def test_vehiculo(self):
        """Test para clase Vehiculo."""
        vehiculo = Vehiculo("Toyota", "Corolla", 2020)
        
        assert vehiculo.marca == "Toyota"
        assert vehiculo.modelo == "Corolla"
        assert vehiculo.año == 2020
        
        assert "arrancando" in vehiculo.arrancar().lower()
        assert "deteniendo" in vehiculo.detener().lower()
    
    def test_coche(self):
        """Test para clase Coche que hereda de Vehiculo."""
        coche = Coche("Honda", "Civic", 2021, 4)
        
        # Atributos heredados
        assert coche.marca == "Honda"
        assert coche.modelo == "Civic"
        assert coche.año == 2021
        
        # Atributo propio
        assert coche.num_puertas == 4
        
        # Métodos heredados
        assert "arrancando" in coche.arrancar().lower()
        assert "deteniendo" in coche.detener().lower()
        
        # Método propio
        assert "maletero" in coche.abrir_maletero().lower()
    
    def test_cuenta_bancaria(self):
        """Test para clase CuentaBancaria."""
        cuenta = CuentaBancaria("Juan Pérez", 1000)
        
        assert cuenta.titular == "Juan Pérez"
        assert cuenta.consultar_saldo() == 1000
        
        # Test depósito válido
        assert cuenta.depositar(500) == True
        assert cuenta.consultar_saldo() == 1500
        
        # Test depósito inválido
        assert cuenta.depositar(-100) == False
        assert cuenta.consultar_saldo() == 1500
        
        # Test retiro válido
        assert cuenta.retirar(200) == True
        assert cuenta.consultar_saldo() == 1300
        
        # Test retiro inválido (cantidad negativa)
        assert cuenta.retirar(-50) == False
        assert cuenta.consultar_saldo() == 1300
        
        # Test retiro inválido (saldo insuficiente)
        assert cuenta.retirar(2000) == False
        assert cuenta.consultar_saldo() == 1300
        
    def test_cuenta_bancaria_saldo_inicial_cero(self):
        """Test para cuenta bancaria con saldo inicial por defecto."""
        cuenta = CuentaBancaria("Ana García")
        assert cuenta.consultar_saldo() == 0


class TestModulos:
    """Tests para ejercicios de módulos."""
    
    def test_usar_modulos(self):
        """Test para uso de módulos estándar."""
        resultado = usar_modulos()
        
        assert isinstance(resultado, dict), "Debe retornar un diccionario"
        
        # Verificar claves requeridas
        claves_requeridas = ['fecha_actual', 'numero_aleatorio', 'raiz_cuadrada_64', 'seno_90_grados']
        for clave in claves_requeridas:
            assert clave in resultado, f"Falta la clave '{clave}'"
        
        # Verificar tipos y valores
        assert isinstance(resultado['fecha_actual'], str), "fecha_actual debe ser string"
        assert len(resultado['fecha_actual']) == 10, "fecha_actual debe tener formato YYYY-MM-DD"
        
        assert isinstance(resultado['numero_aleatorio'], int), "numero_aleatorio debe ser entero"
        assert 1 <= resultado['numero_aleatorio'] <= 100, "numero_aleatorio debe estar entre 1 y 100"
        
        assert abs(resultado['raiz_cuadrada_64'] - 8.0) < 0.001, "raiz_cuadrada_64 debe ser 8.0"
        
        # seno de π/2 radianes (90 grados) debe ser 1
        assert abs(resultado['seno_90_grados'] - 1.0) < 0.001, "seno_90_grados debe ser 1.0"


class TestArchivos:
    """Tests para ejercicios de lectura y escritura de archivos."""
    
    def test_escribir_y_leer_archivo(self):
        """Test para escribir y leer archivos."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
            nombre_archivo = tmp.name
        
        try:
            contenido = "Hola, este es un archivo de prueba.\nSegunda línea."
            
            # Test escribir archivo
            resultado = escribir_archivo(nombre_archivo, contenido)
            assert resultado == True, "escribir_archivo debe retornar True"
            
            # Test leer archivo
            contenido_leido = leer_archivo(nombre_archivo)
            assert contenido_leido == contenido, "El contenido leído debe coincidir"
            
        finally:
            if os.path.exists(nombre_archivo):
                os.unlink(nombre_archivo)
    
    def test_leer_archivo_inexistente(self):
        """Test para leer archivo que no existe."""
        resultado = leer_archivo("archivo_que_no_existe.txt")
        assert resultado is None, "Debe retornar None si el archivo no existe"
    
    def test_procesar_csv_simple(self):
        """Test para procesamiento de CSV simple."""
        datos = [
            {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'},
            {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Barcelona'},
            {'nombre': 'Carlos', 'edad': 35, 'ciudad': 'Sevilla'}
        ]
        
        resultado = procesar_csv_simple(datos)
        lineas = resultado.strip().split('\n')
        
        assert lineas[0] == "nombre,edad,ciudad", "Header incorrecto"
        assert "Juan,25,Madrid" in lineas, "Datos de Juan incorrectos"
        assert "Ana,30,Barcelona" in lineas, "Datos de Ana incorrectos"
        assert "Carlos,35,Sevilla" in lineas, "Datos de Carlos incorrectos"
    
    def test_manejar_json(self):
        """Test para manejo de archivos JSON."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
            nombre_archivo = tmp.name
        
        try:
            datos_originales = {
                'nombre': 'Test',
                'numero': 42,
                'lista': [1, 2, 3],
                'objeto': {'clave': 'valor'}
            }
            
            datos_leidos = manejar_json(datos_originales, nombre_archivo)
            
            assert datos_leidos == datos_originales, "Los datos leídos deben coincidir con los originales"
            
        finally:
            if os.path.exists(nombre_archivo):
                os.unlink(nombre_archivo)


class TestManejoErrores:
    """Tests para ejercicios de manejo de errores."""
    
    def test_division_segura(self):
        """Test para división segura."""
        # División exitosa
        resultado = division_segura(10, 2)
        assert resultado['resultado'] == 5.0
        assert resultado['error'] is None
        
        # División por cero
        resultado = division_segura(10, 0)
        assert resultado['resultado'] is None
        assert resultado['error'] is not None
        assert "zero" in resultado['error'].lower()
        
        # Tipo incorrecto
        resultado = division_segura("10", 2)
        assert resultado['resultado'] is None
        assert resultado['error'] is not None
    
    def test_acceder_lista_seguro(self):
        """Test para acceso seguro a lista."""
        lista = [1, 2, 3, 4, 5]
        
        # Acceso exitoso
        resultado = acceder_lista_seguro(lista, 2)
        assert resultado['valor'] == 3
        assert resultado['error'] is None
        
        # Índice fuera de rango
        resultado = acceder_lista_seguro(lista, 10)
        assert resultado['valor'] is None
        assert resultado['error'] is not None
        assert "index" in resultado['error'].lower()
        
        # Tipo incorrecto
        resultado = acceder_lista_seguro("no es lista", 0)
        assert resultado['valor'] is None
        assert resultado['error'] is not None
    
    def test_convertir_numero_seguro(self):
        """Test para conversión segura de números."""
        # Conversión a entero
        resultado = convertir_numero_seguro("42")
        assert resultado['numero'] == 42
        assert resultado['tipo'] == 'int'
        assert resultado['error'] is None
        
        # Conversión a float
        resultado = convertir_numero_seguro("3.14")
        assert resultado['numero'] == 3.14
        assert resultado['tipo'] == 'float'
        assert resultado['error'] is None
        
        # Error de conversión
        resultado = convertir_numero_seguro("no es numero")
        assert resultado['numero'] is None
        assert resultado['tipo'] is None
        assert resultado['error'] is not None
    
    def test_validar_archivo_json(self):
        """Test para validación de archivo JSON."""
        # Archivo JSON válido
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
            json.dump({'test': 'data'}, tmp)
            nombre_archivo = tmp.name
        
        try:
            resultado = validar_archivo_json(nombre_archivo)
            assert resultado['valido'] == True
            assert resultado['datos']['test'] == 'data'
            assert resultado['error'] is None
        finally:
            os.unlink(nombre_archivo)
        
        # Archivo que no existe
        resultado = validar_archivo_json("archivo_inexistente.json")
        assert resultado['valido'] == False
        assert resultado['datos'] is None
        assert resultado['error'] is not None
        
        # Archivo con JSON inválido
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
            tmp.write("{ esto no es json válido }")
            nombre_archivo = tmp.name
        
        try:
            resultado = validar_archivo_json(nombre_archivo)
            assert resultado['valido'] == False
            assert resultado['datos'] is None
            assert resultado['error'] is not None
        finally:
            os.unlink(nombre_archivo)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
