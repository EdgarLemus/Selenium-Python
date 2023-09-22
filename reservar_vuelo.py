import unittest
import os
from pyunitreport import HTMLTestRunner
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import Select

class ReservaTest(unittest.TestCase):
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

    def test_realizar_compra(self):
        driver = self.driver
        
        # Localiza el campo de usuario y llena el formulario
        usuario = driver.find_element(By.XPATH,"//input[@name='userName']")
        usuario.send_keys('Arctyrael')

        # Localiza el campo de contraseña y llena el formulario
        contraseña = driver.find_element(By.XPATH, "//input[@name='password']")
        contraseña.send_keys('abc123')

        # Localiza el botón de inicio de sesión y haz clic en él
        btnLogin = driver.find_element(By.XPATH,"//input[@name='submit']")
        btnLogin.click()

        driver.implicitly_wait(4)

        # Navega a la página de reservas
        reservas = driver.find_element(By.XPATH,"//a[@href='reservation.php']")
        reservas.click()

        driver.implicitly_wait(4)

        # Selecciona opciones en los menús desplegables
        dropdown = driver.find_element(By.XPATH, "//select[@name='fromPort']")
        select = Select(dropdown)
        select.select_by_visible_text('London')

        dropdown = driver.find_element(By.XPATH, "//select[@name='fromMonth']")
        select = Select(dropdown)
        select.select_by_visible_text('November')

        dropdown = driver.find_element(By.XPATH, "//select[@name='fromDay']")
        select = Select(dropdown)
        select.select_by_visible_text('30')

        dropdown = driver.find_element(By.XPATH, "//select[@name='toPort']")
        select = Select(dropdown)
        select.select_by_visible_text('Paris')

        dropdown = driver.find_element(By.XPATH, "//select[@name='toMonth']")
        select = Select(dropdown)
        select.select_by_visible_text('December')

        dropdown = driver.find_element(By.XPATH, "//select[@name='toDay']")
        select = Select(dropdown)
        select.select_by_visible_text('6')

        # Selecciona una opción de servicio
        services = driver.find_element(By.XPATH,"//input[@name='servClass']")
        services.click()

        # Continúa con la reserva
        continuar = driver.find_element(By.XPATH,"//input[@name='findFlights']")
        continuar.click()

# Cierra la ventana del navegador
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Reserva-test-report'))