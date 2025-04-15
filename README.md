[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JoGu4W9y)
# Trabajo Práctico 3: Desarrollo Guiado por Pruebas (TDD) - Manejo de Excepciones

## Identificación del Alumno
**Nombre y Apellido:** [Melina Navarro]

**Nota:** Este trabajo práctico es de carácter individual. Cada alumno debe realizar su propia implementación y no se permite el trabajo en grupo.

## Objetivo
Este trabajo práctico tiene como objetivo practicar el desarrollo guiado por pruebas (TDD) en Python, implementando un sistema de validación de entrada de números que maneje diferentes tipos de excepciones.

## Fecha de Vencimiento
El trabajo debe ser entregado antes del **16/04/2025 a las 13:00 hs**.

## Enfoque
El trabajo se realizará en dos fases, siguiendo las prácticas de TDD:

### Fase 1: Implementación de Pruebas
En esta primera fase, deberás:
1. Crear los archivos de prueba necesarios
2. Implementar los casos de prueba para la validación de entrada de números
3. Asegurarte de que las pruebas fallen inicialmente (rojo)
4. Hacer commit y push de solo los archivos de prueba

### Fase 2: Implementación de la Solución
En la segunda fase, deberás:
1. Implementar las funciones y excepciones necesarias para pasar las pruebas
2. Refactorizar el código si es necesario
3. Asegurarte de que todas las pruebas pasen (verde)
4. Hacer commit y push de la implementación

## Requisitos
- Python 3.x
- unittest (incluido en la biblioteca estándar de Python)

## Reglas de Validación
Para la validación de entrada de números, deberás implementar las siguientes reglas:
- La entrada debe ser un número válido
- El número debe ser positivo
- Se deben manejar las siguientes excepciones:
  - `ValueError` cuando la entrada no es un número
  - `NumeroDebeSerPositivo` (excepción personalizada) cuando el número es negativo

## Estructura del Proyecto
```
.
├── tests/
│   └── test_calculo_numeros.py
└── src/
    ├── exceptions.py
    └── calculo_numeros.py
```

## Entregables
1. Primer push: Archivos de prueba (`tests/test_calculo_numeros.py`)
2. Segundo push: Implementación completa (`src/exceptions.py` y `src/calculo_numeros.py`)

## Criterios de Evaluación
- Correcta implementación de las pruebas siguiendo TDD
- Cobertura adecuada de casos de prueba
- Implementación correcta de las excepciones personalizadas
- Manejo apropiado de las excepciones estándar
- Código limpio y bien estructurado

## Ejemplos de Uso
```python
import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
```

## Uso del Repositorio
Para trabajar con este repositorio, es importante seguir estas pautas:

1. **Protección de la rama main**
   - La rama main estará protegida
   - No se permiten pushes directos a main
   - Todos los cambios deben realizarse a través de Pull Requests (PR)

2. **Gestión de Issues**
   - Crear un issue para cada tarea (tests e implementaciones)
   - Cada issue debe tener:
     - Título descriptivo
     - Descripción clara de la tarea
     - Milestone asignado (1 o 2 según corresponda)
     - Labels apropiados (ej: "test", "implementation", "bug", etc.)
     - Branch asociada (crear una nueva branch por cada issue)
   - Nombrar las branches siguiendo el formato: `feature/[nombre-del-issue]`

3. **Proceso de trabajo recomendado**:
   ```bash
   # Clonar el repositorio
   git clone <url-del-repositorio>

   # Crear y cambiar a una nueva branch
   git checkout -b feature/[nombre-del-issue]

   # Realizar cambios y commits
   git add .
   git commit -m "Descripción clara de los cambios"

   # Subir cambios al repositorio remoto
   git push origin feature/[nombre-del-issue]

   # Crear Pull Request
   # Realizar merge
   ```

4. **Milestones**
   - Milestone 1: Implementación de Tests
     - Issue: "Agregar tests para ingreso de números válidos"
     - Issue: "Agregar tests para ingreso de números negativos"
     - Issue: "Agregar tests para ingreso de texto no numérico"
   
   - Milestone 2: Implementación de la Solución
     - Issue: "Implementar excepción NumeroDebeSerPositivo"
     - Issue: "Implementar función ingrese_numero"
     - Issue: "Implementar manejo de excepciones"

5. **Commits y Pull Requests**
   - Cada push debe ir acompañado de un PR
   - Los PRs deben ser revisados y aprobados antes de mergear
   - Los mensajes de commit deben ser descriptivos y claros
   - Cada PR debe estar asociado a un issue específico

6. **Estructura de commits**:
   - Fase 1: "Implementación de pruebas para validación de números"
   - Fase 2: "Implementación de excepciones y validación"

## Instrucciones de Ejecución
Para ejecutar el programa y las pruebas, sigue estos pasos:

1. **Ejecutar las pruebas**:
   ```bash
   # Ejecutar todas las pruebas
   python -m unittest discover tests

   # Ejecutar una prueba específica
   python -m unittest tests/test_calculo_numeros.py
   ```

2. **Ejecutar el programa principal**:
   ```bash
   # Ejecutar el programa interactivo
   python src/calculo_numeros.py
   ```

3. **Uso del programa**:
   - El programa aceptará entrada por consola
   - Ingresa un número para validar
   - El programa indicará si el número es válido o mostrará el error correspondiente
   - Presiona Ctrl+C para salir del programa

4. **Ejemplo de uso**:
   ```bash
   $ python src/calculo_numeros.py
   Ingrese un número: 100
   Número válido: 100
   
   Ingrese un número: -100
   Error: El número debe ser positivo
   
   Ingrese un número: ABC
   Error: La entrada debe ser un número válido
   ```
