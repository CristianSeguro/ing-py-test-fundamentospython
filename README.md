# 🐍 Prueba Técnica: Fundamentos de Python

Esta prueba técnica evalúa conocimientos fundamentales de Python a través de ejercicios prácticos con validación automática usando pytest.

## 📋 Contenido de la Prueba

La prueba incluye 7 áreas principales:

1. **🛠️ Variables y tipos de datos** - Manejo básico de tipos primitivos y estructuras de datos
2. **🔄 Condicionales y bucles** - Estructuras de control de flujo
3. **🧠 Funciones** - Definición y uso de funciones, recursión
4. **🏫 Clases** - Programación orientada a objetos, herencia, encapsulación
5. **📦 Módulos y paquetes** - Uso de librerías estándar de Python
6. **📂 Lectura y escritura de archivos** - Manejo de archivos de texto, CSV y JSON
7. **⚠️ Manejo de errores** - Uso de try/except para control de errores

## 🚀 Instrucciones de Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/CristianSeguro/ing-py-test-fundamentospython.git
cd ing-py-test-fundamentospython
```

### 2. Crear Entorno Virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 📝 Desarrollo de la Actividad

### Estructura del Proyecto

```
Recorderis/
├── main.py           # Archivo principal con los ejercicios a implementar
├── test.py           # Tests automatizados con pytest
├── requirements.txt  # Dependencias del proyecto
├── README.md         # Este archivo con las instrucciones
└── venv/            # Entorno virtual (creado al seguir las instrucciones)
```

### Instrucciones para Implementar

1. **Abrir el archivo `main.py`**: Aquí encontrarás todos los ejercicios con sus enunciados y funciones/clases a implementar.

2. **Leer cuidadosamente cada enunciado**: Cada función incluye una docstring detallada con:
   - Descripción de lo que debe hacer
   - Parámetros de entrada
   - Valor de retorno esperado
   - Ejemplos cuando sea necesario

3. **Implementar las funciones**: Reemplaza el comentario `# TODO: Implementa aquí tu código` con tu implementación.

4. **Mantener las signaturas**: No cambies los nombres de las funciones, clases o sus parámetros.

5. **Ejecutar tests frecuentemente**: Usa los tests para verificar que tu implementación es correcta.

### Consejos de Desarrollo

- ✅ Implementa una función a la vez
- ✅ Ejecuta los tests después de cada implementación
- ✅ Lee los mensajes de error de los tests para entender qué corregir
- ✅ Puedes agregar código auxiliar si lo necesitas
- ✅ Usa comentarios para explicar lógica compleja
- ❌ No modifiques los tests
- ❌ No cambies las signaturas de las funciones

## 🧪 Ejecutar Pruebas

### Ejecutar Todos los Tests

```bash
python -m pytest test.py -v
```

### Ejecutar Tests por Categoría

```bash
# Solo tests de variables y tipos
python -m pytest test.py::TestVariablesYTipos -v

# Solo tests de clases
python -m pytest test.py::TestClases -v

# Solo tests de manejo de errores
python -m pytest test.py::TestManejoErrores -v
```

### Ejecutar un Test Específico

```bash
python -m pytest test.py::TestFunciones::test_factorial -v
```

### Interpretación de Resultados

- ✅ **PASSED**: Test exitoso - tu implementación es correcta
- ❌ **FAILED**: Test fallido - revisa tu implementación
- ⚠️ **ERROR**: Error en el código - verifica sintaxis y lógica

## 📤 Enviar Resultados

### 1. Ejecutar Tests Finales

Antes de enviar, ejecuta todos los tests y verifica que pasen:

```bash
python -m pytest test.py -v --tb=short
```

### 2. Generar Reporte Completo

```bash
python -m pytest test.py -v --tb=short > resultados_tests.txt 2>&1
```

### 3. Capturar Salida con Cobertura (Opcional)

```bash
python -m pytest test.py --cov=main --cov-report=term-missing > reporte_completo.txt 2>&1
```

### 4. Archivos a Enviar

Envía los siguientes archivos:

1. **`main.py`** - Tu implementación completa
2. **`resultados_tests.txt`** - Salida de los tests
3. **`reporte_completo.txt`** - (Opcional) Reporte con cobertura

### Formato de Entrega

Comprime todos los archivos en un ZIP con el siguiente nombre:
```
PruebaPython_[TuNombre]_[Fecha].zip
```

Ejemplo: `PruebaPython_JuanPerez_2025-07-23.zip`

## 📊 Criterios de Evaluación

| Categoría | Peso | Descripción |
|-----------|------|-------------|
| **Funcionalidad** | 60% | Los tests pasan correctamente |
| **Calidad del Código** | 20% | Código limpio, legible y bien estructurado |
| **Manejo de Casos Edge** | 10% | Considera casos especiales y validaciones |
| **Documentación** | 10% | Comentarios útiles cuando sea necesario |

### Puntuación por Ejercicio

- Variables y tipos: 10 puntos
- Condicionales y bucles: 15 puntos  
- Funciones: 20 puntos
- Clases: 25 puntos
- Módulos: 10 puntos
- Archivos: 15 puntos
- Manejo de errores: 15 puntos

**Total: 110 puntos** (puntuación extra disponible)

## ❓ Ayuda y Resolución de Problemas

### Problemas Comunes

**Error: "pytest no se encuentra"**
```bash
# Verifica que el entorno virtual esté activado
pip install pytest
```

**Error: "No module named 'main'"**
```bash
# Ejecuta desde el directorio correcto donde está main.py
```

**Tests fallan constantemente**
```bash
# Ejecuta un test específico para ver el error detallado
python -m pytest test.py::TestNombreClase::test_nombre_funcion -v -s
```

### Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Guía de pytest](https://docs.pytest.org/)
- [PEP 8 - Guía de estilo](https://pep8.org/)

## ⏰ Tiempo Estimado

- **Principiante**: 4-6 horas
- **Intermedio**: 2-3 horas  
- **Avanzado**: 1-2 horas

¡Buena suerte con la prueba! 🍀
