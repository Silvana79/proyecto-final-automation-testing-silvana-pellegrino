
# Automation & Testing QA – Proyecto Final

## Descripción del proyecto

Framework de automatización de pruebas de software que integra pruebas funcionales de interfaz web (UI) y pruebas de API.

El proyecto utiliza **SauceDemo** como aplicación web bajo prueba y **JSONPlaceholder** como servicio REST para las pruebas de API.

El objetivo es validar funcionalidades principales, comprobar respuestas HTTP y estructuras JSON, y aplicar buenas prácticas de automatización mediante Python, Pytest, Selenium WebDriver y Requests.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Requests
- pytest-html
- pytest-metadata
- Git
- GitHub

## Funcionalidades y pruebas implementadas

### Pruebas UI – SauceDemo

Se implementaron cinco escenarios de prueba:

1. Inicio de sesión exitoso con credenciales válidas.
2. Inicio de sesión con credenciales inválidas.
3. Inicio de sesión con usuario bloqueado.
4. Visualización y validación del catálogo de productos.
5. Incorporación de un producto al carrito y verificación de sus datos.

Los dos escenarios negativos de inicio de sesión utilizan parametrización mediante `pytest.mark.parametrize`, leyendo los conjuntos de datos desde `users.json`.

También se utilizan esperas explícitas con `WebDriverWait` para sincronizar las interacciones con la interfaz.

### Pruebas API – JSONPlaceholder

Se implementaron cuatro casos de prueba:

1. **GET:** consulta de una publicación existente y validación del código HTTP 200 y de los datos JSON.
2. **GET negativo:** consulta de una publicación inexistente y validación del código HTTP 404 y de la respuesta JSON.
3. **POST:** envío de una nueva publicación y validación del código HTTP 201 y de los datos devueltos.
4. **DELETE:** solicitud de eliminación de una publicación y validación del código HTTP 200.

Las pruebas se desarrollaron utilizando la biblioteca Requests.

**Nota:** JSONPlaceholder es un servicio de pruebas que simula operaciones de escritura. Las operaciones POST y DELETE no representan modificaciones persistentes en una base de datos real.

## Arquitectura del proyecto

Se utiliza el patrón **Page Object Model (POM)** para separar la interacción con las páginas web de la lógica de las pruebas.

La lectura de datos externos se centraliza en `utils/data_reader.py`, mientras que las pruebas UI y API se organizan en archivos independientes.

Los datos de prueba se almacenan en archivos JSON y CSV.

## Estructura del proyecto

```text
proyecto-final-automation-testing-silvana-pellegrino/
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
- Conexión a Internet para acceder a SauceDemo y JSONPlaceholder e instalar las dependencias.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Silvana79/proyecto-final-automation-testing-silvana-pellegrino.git
cd proyecto-final-automation-testing-silvana-pellegrino
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual en Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

En caso de utilizar CMD:

```bat
venv\Scripts\activate.bat
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Desde la carpeta principal del proyecto y con el entorno virtual activado, ejecutar:

```powershell
pytest -v
```

Pytest ejecuta las pruebas de interfaz y API, muestra los resultados en la terminal y genera automáticamente el reporte HTML y el registro de ejecución.

Para ejecutar solamente las pruebas de interfaz:

```powershell
pytest -v tests/test_saucedemo.py
```

Para ejecutar solamente las pruebas de API:

```powershell
pytest -v tests/test_api.py
```

## Reportes y evidencias

Los archivos generados durante las ejecuciones se almacenan en la carpeta `reports/`.

- **Reporte HTML:** `reports/reporte.html`
- **Registro de ejecución:** `reports/execution.log`
- **Capturas de pantalla:** `reports/screenshots/`

Las capturas se generan automáticamente cuando falla una prueba de interfaz y hay un navegador disponible. Se almacenan como archivos PNG y también se adjuntan al resultado correspondiente dentro del reporte HTML.

### Cómo interpretar el reporte HTML

El reporte permite consultar:

- La cantidad de pruebas ejecutadas.
- El estado de cada prueba: aprobada, fallida o omitida.
- La duración de la ejecución y de los casos individuales.
- Los detalles de los errores cuando una prueba falla.
- Las capturas de pantalla asociadas a los fallos de interfaz, cuando se generan.

Para abrir el reporte en Windows PowerShell:

```powershell
Invoke-Item .\reports\reporte.html
```

## Decisiones técnicas

- Se utiliza Pytest como framework de ejecución y organización de pruebas.
- Se aplica Page Object Model (POM) para separar la interacción con las páginas de la lógica de prueba.
- Se implementan esperas explícitas mediante `WebDriverWait`.
- No se utiliza `time.sleep()`.
- Cada prueba UI utiliza una instancia independiente del navegador mediante un fixture de Pytest.
- Se utiliza WebDriver Manager para gestionar ChromeDriver.
- Se utilizan Requests para realizar las operaciones HTTP de las pruebas API.
- Los datos de prueba se almacenan externamente en archivos JSON y CSV.
- Se utiliza parametrización de Pytest para ejecutar escenarios de login con distintos conjuntos de datos.
- Se implementa captura automática de pantalla ante fallos de pruebas UI.
- Se utiliza pytest-html para generar reportes HTML y adjuntar evidencias.
- Se configura logging para registrar información relevante durante las pruebas.

## Repositorio

GitHub:

https://github.com/Silvana79/proyecto-final-automation-testing-silvana-pellegrino
