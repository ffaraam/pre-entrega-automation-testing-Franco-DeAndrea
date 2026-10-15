from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def iniciar_sesion(driver):
    # Reutiliza el login y espera la redireccion antes de continuar con cada test.
    driver.get("https://www.saucedemo.com/")
    espera = WebDriverWait(driver, 15)

    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    espera.until(EC.url_contains("/inventory.html"))
