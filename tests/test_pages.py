import time
import pytest
from selenium.webdriver.common.by import By
import os


class TestLoginPage:
    def take_screenshot(self, driver, name):
        path = os.path.join("results/successful_test", f"{name}.png")
        driver.save_screenshot(path)

    def test_user_flow(self, driver):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        self.take_screenshot(driver, "01_inicio_sesion")
        time.sleep(1)

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.take_screenshot(driver, "02_producto_agregado")

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        self.take_screenshot(driver, "03_verificar_carrito")
        time.sleep(1)

        producto = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert producto.text == "Sauce Labs Backpack"
        time.sleep(1)

        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("Juan")
        time.sleep(1)
        driver.find_element(By.ID, "last-name").send_keys("Perez")
        time.sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("11403")
        time.sleep(2)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        self.take_screenshot(driver, "04_formulario_checkout")
        time.sleep(1)

        driver.find_element(By.ID, "finish").click()
        time.sleep(1)
        self.take_screenshot(driver, "05_compra_finalizada")
        time.sleep(1)

        confirmacion = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order!" in confirmacion

        driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
        self.take_screenshot(driver, "06_logout")
        time.sleep(1)

        assert "https://www.saucedemo.com/" in driver.current_url
