# Automated-Testing.

# 🧪 Automatización de Pruebas Web con Selenium y Pytest

Este proyecto en Python+Selenium realiza **pruebas automatizadas** del sitio web [Swag Labs](https://www.saucedemo.com/), una plataforma de demostración para pruebas funcionales de UI.

El flujo simula la experiencia completa de un usuario: **inicio de sesión, agregar productos al carrito, finalizar compra y cerrar sesión**, tomando capturas de pantalla en cada paso y generando un **reporte HTML** detallado.

---

## 🚀 Tecnologías y Herramientas

- [Python](https://www.python.org/) 3.10+
- [Pytest](https://docs.pytest.org/) - Framework de pruebas
- [Selenium](https://www.selenium.dev/) - Automatización del navegador
- [Webdriver Manager](https://pypi.org/project/webdriver-manager/) - Gestión automática de drivers
- [Pytest HTML](https://pypi.org/project/pytest-html/) - Reportes HTML de pruebas

---

### 📋 Instalación
1. Clona el repositorio o copia los archivos:
2. Instala las dependencias: pip install -r requirements.txt


### 🧑‍💻 Cómo ejecutar las pruebas
1. Para correr pruebas en Google Chrome, usa:
- pytest --html=results/reporte.html

2. Para ejecutarlas en Firefox, usa:
- pytest --browser=firefox --html=results/reporte.html


### 🧪 Flujo de prueba automatizada.
1. Inicio de sesión con credenciales válidas.
2. Agregar un producto (Sauce Labs Backpack) al carrito.
3. Verificar el contenido del carrito.
4. Llenar el formulario de checkout y finalizar la compra.
5. Confirmar el mensaje de orden completada.
6. Cerrar sesión desde el menú lateral.
7. Durante cada etapa, se toma una captura de pantalla que se guarda en la carpeta results


###  🧩 Características especiales
- Compatible con Chrome y Firefox
- Ejecuta pruebas en modo incógnito para evitar popups molestos (como el guardado de contraseñas)
- Toma capturas automáticas en cada paso y también en caso de fallos (en el futuro, puedes añadir el hook de fallo)
- Genera reportes HTML legibles para presentar resultados
- Uso de pytest_addoption para personalizar navegador


### 📌 Credenciales usadas
Usuario de prueba incluido por Swag Labs:
- Usuario: standard_user
- Contraseña: secret_sauce
