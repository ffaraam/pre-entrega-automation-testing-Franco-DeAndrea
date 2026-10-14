import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    servicio = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servicio)

    try:
        navegador.set_page_load_timeout(30)
        yield navegador
    finally:
        navegador.quit()


def test_01_login(driver):

    driver.get("https://www.saucedemo.com/")
    espera = WebDriverWait(driver, 15)


    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    espera.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    assert driver.title == "Swag Labs", "El título de la página es incorrecto"

    print("Test OK: login exitoso")


