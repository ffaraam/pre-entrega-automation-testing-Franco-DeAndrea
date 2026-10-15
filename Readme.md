# Pre-entrega de QA Automation - SauceDemo

**Alumno:** Franco De Andrea

## Objetivo

Este proyecto es una pre-entrega de QA Automation. Automatice tres pruebas sobre [SauceDemo](https://www.saucedemo.com/) para verificar el inicio de sesion, el catalogo de productos y el agregado de un producto al carrito.

El objetivo es practicar el uso de Selenium WebDriver con Python y Pytest, aplicar esperas explicitas y realizar validaciones que permitan detectar errores en estos flujos.

## Tecnologias utilizadas

- Python: lenguaje utilizado para escribir las pruebas.
- Pytest: framework para organizar y ejecutar los tests.
- Selenium WebDriver: herramienta para interactuar con el navegador.
- Google Chrome: navegador utilizado en las pruebas.
- webdriver-manager: administra la descarga de ChromeDriver.
- pytest-html: genera el reporte HTML de resultados.
- Git y GitHub: control de versiones y almacenamiento del proyecto.

## Casos de prueba

| Test | Validaciones realizadas |
| --- | --- |
| `test_01_login` | Ingresa con `standard_user` y `secret_sauce`, espera la redireccion a `/inventory.html` y verifica el titulo `Swag Labs`. |
| `test_02_verificar_inventario` | Verifica los titulos `Swag Labs` y `Products`, la presencia de productos visibles, el menu y el filtro. Muestra el nombre y el precio del primer producto. |
| `test_03_agregar_producto_al_carrito` | Agrega el primer producto, verifica que el contador muestre `1` y comprueba que el nombre del producto dentro del carrito coincida con el agregado. |

Las credenciales utilizadas son las de prueba publicadas por SauceDemo:

- Usuario: `standard_user`
- Password: `secret_sauce`

## Estructura del proyecto

```text
pre-entrega-automation-testing-Franco-DeAndrea/
|-- tests/
|   `-- test_saucedemo.py
|-- utils/
|   `-- helpers.py
|-- reports/
|   `-- reporte.html
|-- pytest.ini
|-- .gitignore
`-- Readme.md
```

- `tests/test_saucedemo.py`: contiene los tres tests y la fixture que crea y cierra el navegador.
- `utils/helpers.py`: contiene la funcion `iniciar_sesion`, reutilizada en los tests de inventario y carrito.
- `reports/reporte.html`: guarda el reporte generado por Pytest.
- `pytest.ini`: configura la carpeta de tests, las importaciones y la salida HTML.
- `.gitignore`: excluye el entorno virtual y los archivos de cache.

No se utiliza una carpeta `datos/` porque las pruebas no leen archivos de datos externos.

## Requisitos previos

- Python 3 instalado y disponible desde la terminal.
- Google Chrome instalado.
- Git instalado para clonar el repositorio.
- Conexion a internet para instalar las dependencias, descargar ChromeDriver y acceder a SauceDemo.

## Instalacion

Los siguientes comandos estan preparados para Windows con PowerShell.

1. Clonar el repositorio y entrar a la carpeta:

   ```powershell
   git clone https://github.com/ffaraam/pre-entrega-automation-testing-Franco-DeAndrea.git
   cd pre-entrega-automation-testing-Franco-DeAndrea
   ```

2. Crear un entorno virtual:

   ```powershell
   python -m venv .venv
   ```

3. Instalar las dependencias dentro del entorno:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install pytest selenium webdriver-manager pytest-html
   ```

Se utiliza directamente el Python del entorno virtual, por lo que no es necesario activarlo. Actualmente el proyecto no incluye un archivo `requirements.txt`.

## Ejecucion

Ejecutar los comandos desde la carpeta principal del proyecto.

Para correr los tres tests:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Para ver en la terminal los mensajes impresos durante las pruebas:

```powershell
.\.venv\Scripts\python.exe -m pytest -s
```

Para ejecutar solamente el test de login:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_saucedemo.py::test_01_login
```

Chrome se abre durante la ejecucion y se cierra al finalizar. Se utilizan esperas explicitas de hasta 15 segundos para esperar elementos visibles y la redireccion al inventario. El tiempo limite de carga de pagina es de 30 segundos.

## Reporte y evidencias

La configuracion de `pytest.ini` genera automaticamente un reporte en `reports/reporte.html` con cada ejecucion. El archivo se reemplaza al ejecutar nuevamente los tests y puede abrirse en un navegador. Es un HTML autocontenido, por lo que no necesita archivos de estilos externos.

El reporte incluido registra una ejecucion del **14/10/2026** con **3 tests aprobados, 0 fallos y 0 errores**. Tambien contiene la salida capturada de los tests, incluido el nombre y el precio del primer producto: `Sauce Labs Backpack | $29.99`.

En la ejecucion normal, Pytest captura los mensajes impresos y los incluye en el reporte. La opcion `-s` permite verlos directamente en la terminal.

## Estado actual y mejoras pendientes

Los tres casos funcionales estan implementados. Cada test utiliza un navegador nuevo mediante una fixture con alcance de funcion y realiza su propio login. El navegador se cierra al finalizar cada prueba para evitar compartir estado entre tests.

Actualmente no se generan archivos de log separados ni capturas automaticas ante fallos. La evidencia disponible es el reporte HTML y la salida capturada en el mismo.
