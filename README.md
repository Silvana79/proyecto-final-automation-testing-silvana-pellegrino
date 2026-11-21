# Automation & Testing QA – Proyecto Final

## Descripción del proyecto

Proyecto de automatización de pruebas de software que integra pruebas funcionales de interfaz web (UI) y pruebas de API.

El proyecto utiliza **SauceDemo** como aplicación web bajo prueba y **JSONPlaceholder** como servicio REST para las pruebas de API.

El objetivo es verificar funcionalidades principales de la aplicación, validar respuestas HTTP y estructuras JSON, y aplicar buenas prácticas de automatización mediante Python, Pytest, Selenium WebDriver y Requests.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- webdriver-manager
- Requests
- pytest-html
- Git
- GitHub

## Funcionalidades y pruebas implementadas

### Pruebas UI – SauceDemo

- Login exitoso con credenciales válidas.
- Validación de acceso a la página de productos (`/inventory.html`).
- Verificación del título de la sección Products.
- Login con credenciales inválidas.
- Validación del mensaje de error correspondiente.
- Login con usuario bloqueado.
- Verificación del catálogo de productos.
- Obtención y validación del nombre y precio del primer producto.
- Comparación de los datos de la página con información almacenada en un archivo CSV.
- Agregado de un producto al carrito.
- Validación del contador del carrito.
- Navegación a la sección del carrito.
- Verificación del producto agregado y su precio.

### Pruebas API – JSONPlaceholder

- GET: consulta de una publicación existente y validación de la respuesta.
- POST: envío de una nueva publicación y validación de los datos devueltos.
- DELETE: solicitud de eliminación de una publicación y validación del código HTTP.

Las pruebas API utilizan Requests y validan códigos de estado y contenido JSON.

**Nota:** JSONPlaceholder es un servicio de pruebas que simula operaciones de escritura. Las operaciones POST y DELETE no representan modificaciones persistentes en una base de datos real.

## Arquitectura del proyecto

Se utiliza el patrón **Page Object Model (POM)** para separar la interacción con las páginas web de la lógica de las pruebas.

La lectura de datos externos se centraliza en utilidades específicas, mientras que las pruebas UI y API se organizan en archivos independientes.

## Estructura del proyecto

```text
pre-entrega-automation-testing-silvana-pellegrino/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_saucedemo.py
│   └── test_api.py
├── test_data/
│   ├── users.json
│   └── products.csv
├── utils/
│   ├── __init__.py
│   └── data_reader.py
├── reports/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Requisitos previos

- Python instalado.
- Google Chrome instalado.
- Git instalado.
- Conexión a Internet para acceder a SauceDemo, JSONPlaceholder e instalar las dependencias.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Silvana79/pre-entrega-automation-testing-silvana-pellegrino.git
cd pre-entrega-automation-testing-silvana-pellegrino
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual en Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Si se utiliza el Símbolo del sistema (CMD):

```bat
venv\Scripts\activate.bat
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Desde la carpeta principal del proyecto, ejecutar:

```bash
pytest -v
```

Pytest ejecuta las pruebas UI y API y genera automáticamente el reporte HTML y el registro de ejecución.

## Reportes y evidencias

Los archivos generados durante la ejecución se almacenan en la carpeta `reports/`.

- **Reporte HTML:** `reports/reporte.html`
- **Registro de ejecución:** `reports/execution.log`
- **Capturas de pantalla:** `reports/screenshots/`

Las capturas se generan automáticamente cuando falla una prueba UI y hay un navegador disponible.

Para abrir el reporte HTML en Windows PowerShell:

```powershell
Invoke-Item .\reports\reporte.html
```

## Decisiones técnicas

- Se utiliza Pytest como framework de ejecución y organización de pruebas.
- Se aplica Page Object Model (POM) para separar la interacción con las páginas de la lógica de prueba.
- Se implementan esperas explícitas mediante `WebDriverWait`.
- No se utiliza `time.sleep()`.
- Cada prueba UI utiliza una instancia independiente del navegador mediante un fixture de Pytest.
- Se utiliza webdriver-manager para gestionar ChromeDriver.
- Se utilizan Requests para realizar las operaciones HTTP de las pruebas API.
- Los datos de prueba se almacenan externamente en archivos JSON y CSV.
- Se implementa la captura automática de pantallas ante fallos de pruebas UI.
- Se utiliza pytest-html para generar reportes de ejecución.
- Se configura logging para registrar información durante las pruebas.

## Repositorio

GitHub:

https://github.com/Silvana79/pre-entrega-automation-testing-silvana-pellegrino
