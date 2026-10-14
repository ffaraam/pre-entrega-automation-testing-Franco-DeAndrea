import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import iniciar_sesion

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

def test_02_verificar_inventario(driver):
    iniciar_sesion(driver)
    espera = WebDriverWait(driver, 15)
    productos = espera.until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f"Título de ventana incorrecto: {page_title}"
    assert section_title == "Products", f"Título de sección incorrecto: {section_title}"
    assert len(productos) > 0, "No hay productos visibles"

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed(), "El menú no está visible"
    assert filtro.is_displayed(), "El filtro no está visible"

    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} | Precio: {precio}")
