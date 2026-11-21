
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

# Crear las carpetas necesarias automáticamente.
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def driver():
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
    outcome = yield
    report = outcome.get_result()

    # Tomar captura solamente cuando falla la ejecución de una prueba.
    if report.when != "call" or not report.failed:
        return

    # Las pruebas API no tienen navegador.
    browser = item.funcargs.get("driver")

    if browser is None:
        return

    SCREENSHOTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

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
        browser.save_screenshot(str(screenshot_path))
    except Exception:
        pass
