# Selenium-Python
Realicé la automatización en el sitio web [New Tour](https://demo.guru99.com/test/newtours/) de los procesos de Registro de Usuario y Reserva de Vuelo, todo implementado utilizando Python y Selenium.

## Registro de Usuario:

- Utilicé Selenium para abrir un navegador web y navegar al sitio web de destino donde se encuentra el formulario de registro.
- Identifiqué los elementos HTML relevantes, como campos de entrada, botones y formularios.
- Escribí código en Python para automatizar el proceso de llenado del formulario de registro con información de prueba, como nombre, correo electrónico y contraseña.
- Implementé acciones de Selenium para hacer clic en botones de envío y confirmar el registro del usuario.
- Utilicé afirmaciones para verificar que el proceso de registro se realizara con éxito y que el nuevo usuario tuviera acceso al sitio.

## Reserva de vuelo:

- Navegué nuevamente al sitio web y realicé la reserva de un vuelo específico.
- Automatizado el proceso de selección de vuelo, ingresando detalles de viaje y confirmación de reserva.
- Simulé la navegación a través del proceso de reserva, completando los detalles del pasajero y pago.
- Utilicé afirmaciones para confirmar que la reserva de vuelo se completó con éxito.

#### registro_usuario.py
This code is an automated testing script that uses Selenium with Python to register a customer on an example website.

Import of modules and elementary classes:

- unittest: Imports the unittest module, which is used to write and perform unit tests in Python.
- HTMLTestRunner: Imports the HTMLTestRunner class from the pyunitreport module. HTMLTestRunner is an HTML report generator for unit testing.

Environment configuration (setUp):

- Download and unzip the latest version of EdgeDriver from the given URL.

Customer Registration Test (test_registrar_user):

- Locate and click a "REGISTER" button on the website to begin the registration process.
- Use the Select procedure to choose a territory from a drop-down menu.
- Submit the registration form.
- Make an assertion (self.assertTrue) to verify that a factor on the page (spelled "Arctyrael") is enabled, which asserts the known record.

Script execution:

- The condition if __name__ == "__main__": guarantees that the script will be executed only if it is done directly as a program.

- unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Registration-test-report')) starts the tests execution.

#### reservar_vuelo.py

Este código es otro script de prueba automatizado que utiliza Selenium con Python para secuenciar actividades relacionadas con la reserva de vuelos en un sitio web de ejemplo.

Importación de módulos y clases elementales:

unittest: Importa el módulo unittest, que se utiliza para escribir y realizar pruebas unitarias en Python.

HTMLTestRunner: Importa la clase HTMLTestRunner del módulo pyunitreport. HTMLTestRunner es un generador de informes HTML para pruebas unitarias.

Configuración del entorno (setUp):

Descarga y descomprime la última versión de EdgeDriver desde la URL proporcionada.

Prueba de ejecución de la compra (test_realizar_compra):

Introduzca el nombre y la contraseña del cliente en los campos correspondientes.

Navegue a la página de reserva.

Completar una secuencia de selecciones en los cuestionarios, como elegir el lugar de origen, el mes y día de salida, el lugar de destino, etc.

Ejecución del script:

La condición if __name__ == "__main__": garantiza que el script sólo se ejecutará si se ejecuta directamente como programa.

unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Reservation-test-report')) inicia la ejecución de las pruebas.


