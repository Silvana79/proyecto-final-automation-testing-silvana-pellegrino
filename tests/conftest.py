
import base64
import logging
from datetime import datetime
from pathlib import Path

import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"


# Crear automáticamente la carpeta de reportes.
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def driver():
    """
    Crea una instancia independiente de Chrome para cada prueba UI.
    """
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    browser.implicitly_wait(0)

    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captura la pantalla cuando falla una prueba UI.

    Guarda la imagen en reports/screenshots/ y también
    la adjunta al reporte HTML de pytest-html.
    """
    outcome = yield
    report = outcome.get_result()

    # Capturar solamente cuando falla la ejecución del test.
    if report.when != "call" or not report.failed:
        return

    # Obtener el navegador utilizado por la prueba.
    browser = item.funcargs.get("driver")

    # Las pruebas API no utilizan navegador.
    if browser is None:
        return

    SCREENSHOTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    safe_test_name = "".join(
        character
        if character.isalnum() or character in ("-", "_")
        else "_"
        for character in item.nodeid
    )

    screenshot_path = (
        SCREENSHOTS_DIR
        / f"{safe_test_name}_{timestamp}.png"
    )

    try:
        # Obtener la captura en formato Base64.
        screenshot_base64 = browser.get_screenshot_as_base64()

        if not screenshot_base64:
            raise RuntimeError(
                "El navegador no devolvió una captura de pantalla."
            )

        # Guardar la imagen físicamente.
        screenshot_path.write_bytes(
            base64.b64decode(screenshot_base64)
        )

        # Adjuntar la captura al reporte HTML.
        extras = getattr(report, "extras", [])

        extras.append(
            pytest_html.extras.png(
                screenshot_base64,
                name="Captura de pantalla"
            )
        )

        report.extras = extras

        logger.info(
            "Captura guardada y adjuntada al reporte: %s",
            screenshot_path
        )

    except Exception:
        # Registrar el problema sin ocultar el fallo original.
        logger.exception(
            "No se pudo generar la captura para: %s",
            item.nodeid
        )
