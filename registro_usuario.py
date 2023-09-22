import unittest
from pyunitreport import HTMLTestRunner
import os
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import Select

class RegistroTest(unittest.TestCase):

    def setUp(self):
        # URL del EdgeDriver
        edgedriver_url = "https://msedgedriver.azureedge.net/LATEST_STABLE"

        # Obtener la última versión de EdgeDriver
        response = requests.get(edgedriver_url)
        version_number = response.text.strip()

        # Directorio de destino para EdgeDriver
        driver_directory = os.getcwd()  # Carpeta actual del script

        # Crear una carpeta para guardar el archivo zip
        folder_name = f"edgedriver_{version_number}"
        folder_path = os.path.join(driver_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Ruta completa del archivo zip
        zip_file_path = os.path.join(folder_path, f"edgedriver_win64_{version_number}.zip")

        # URL de descarga de EdgeDriver para Windows
        download_url = f"https://msedgedriver.azureedge.net/{version_number}/edgedriver_win64.zip"  # Ajusta la URL según la arquitectura que necesites

        # Descargar el archivo zip de EdgeDriver
        response = requests.get(download_url)
        with open(zip_file_path, "wb") as f:
            f.write(response.content)

        # Descomprimir el archivo zip en la carpeta creada
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(folder_path)

        # Configurar la ubicación del EdgeDriver para Selenium
        edgedriver_path = os.path.join(folder_path, "msedgedriver.exe")

        # Iniciar Selenium con EdgeDriver
        edge_options = EdgeOptions()
        edge_options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # Ruta al ejecutable de Edge (puede variar en tu sistema)
        edge_options.add_argument("start-maximized")  # Maximizar la ventana de Edge al iniciar

        edge_service = EdgeService(executable_path=edgedriver_path)
        self.driver = webdriver.Edge(service=edge_service, options=edge_options)
        driver = self.driver

        # Abre una página web de ejemplo
        driver.get("https://demo.guru99.com/test/newtours/")

    def test_registrar_usuario(self):
        driver = self.driver
        # Variables elementos web
        btnAcount = driver.find_element(By.XPATH,"//a[text()='REGISTER']")
        btnAcount.click()

        first_name=driver.find_element(By.XPATH,"//input[@name='firstName']")
        first_name.send_keys('fernando')

        last_name=driver.find_element(By.XPATH,"//input[@name='lastName']")
        last_name.send_keys('pullutasig')

        phone = driver.find_element(By.XPATH,"//input[@name='phone']")
        phone.send_keys('3154875128')

        email=driver.find_element(By.XPATH,"//input[@name='userName']")
        email.send_keys('ejemplo@correo.com.ec')

        address =  driver.find_element(By.XPATH,"//input[@name='address1']")
        address.send_keys('calle 56 #87 - 64')

        city =  driver.find_element(By.XPATH,"//input[@name='city']")
        city.send_keys('Medellin')

        state =  driver.find_element(By.XPATH,"//input[@name='state']")
        state.send_keys('Antioquia')

        postal =  driver.find_element(By.XPATH,"//input[@name='postalCode']")
        postal.send_keys('050050')

        dropdown = driver.find_element(By.XPATH, "//select[@name='country']")
        select = Select(dropdown)
        select.select_by_visible_text('COLOMBIA')

        user =  driver.find_element(By.XPATH,"//input[@name='email']")
        user.send_keys('Arctyrael')

        password=driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys('abc123')

        password_confir=driver.find_element(By.XPATH, "//input[@name='confirmPassword']")
        password_confir.send_keys('abc123')

        registro=driver.find_element(By.XPATH,"//input[@name='submit']")
        registro.click()

        driver.implicitly_wait(30)

        txtValidate = driver.find_element(By.XPATH,"//b[contains(text(),'Arctyrael')]")

        self.assertTrue(txtValidate.is_enabled())


# Cierra la ventana del navegador
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Registro-test-report'))