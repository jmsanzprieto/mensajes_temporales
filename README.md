# Encriptador y Compartidor de Mensajes Seguro

Este proyecto es una aplicación web construida con FastAPI que permite a los usuarios encriptar mensajes y generar una URL única para compartirlos de forma segura. Una vez que el mensaje es leído a través de la URL compartida, se elimina del servidor.

## Características Principales

* **Encriptación Robusta:** Utiliza la biblioteca `cryptography` de Python con el algoritmo Fernet para encriptar los mensajes, asegurando la confidencialidad de la información.
* **Compartir Fácilmente:** Genera URLs únicas para cada mensaje encriptado, facilitando su compartición a través de cualquier medio.
* **Autodestrucción de Mensajes:** Una vez que un mensaje es leído a través de su URL, el archivo que lo contiene se elimina del servidor, proporcionando una capa adicional de seguridad y privacidad.
* **Interfaz de Usuario Sencilla:** Ofrece un formulario web intuitivo para ingresar y compartir mensajes.
* **Basado en FastAPI:** Aprovecha la velocidad y las características modernas del framework FastAPI.
* **Uso de Plantillas Jinja2:** La interfaz de usuario se renderiza utilizando plantillas Jinja2, permitiendo una separación clara entre la lógica de la aplicación y la presentación.

## Requisitos

Asegúrate de tener instalado Python 3.7+ y pip.

## Instalación

1.  **Clona el repositorio (si aplica):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    .\venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Asegúrate de tener un archivo `requirements.txt` con las dependencias necesarias como `fastapi`, `uvicorn`, `Jinja2`, `cryptography` y `pydantic`.)*

4.  **Configuración:**
    * Crea un archivo `config.py` en el directorio raíz del proyecto.
    * Define una clave secreta segura para la encriptación y la URL base de tu aplicación. Ejemplo:

        ```python
        # config.py
        import os

        SECRET_KEY = os.environ.get("SECRET_KEY") or "tu_clave_secreta_muy_segura"
        BASE_URL = os.environ.get("BASE_URL") or "http://localhost:8000"
        ```
        **¡Importante!** Se recomienda utilizar variables de entorno para `SECRET_KEY` y `BASE_URL` en un entorno de producción por seguridad.

5.  **Crea un directorio `templates`:**
    * Dentro del directorio `templates`, crea los archivos de plantilla Jinja2: `index.html` (para el formulario) y `mensaje.html` (para mostrar el mensaje leído o los errores).
    * Crea un archivo `plantillas.py` para definir las constantes de los nombres de los templates:

        ```python
        # plantillas.py
        INDEX = "index.html"
        MENSAJE = "mensaje.html"
        ```

6.  **Crea un archivo `functions.py`:**
    * Define las funciones `encriptar` y `desencriptar` para manejar la lógica de encriptación y desencriptación utilizando `cryptography.fernet`. Ejemplo:

        ```python
        # functions.py
        from cryptography.fernet import Fernet

        def encriptar(mensaje: str, key: str) -> bytes:
            f = Fernet(key.encode())
            mensaje_encriptado = f.encrypt(mensaje.encode())
            return mensaje_encriptado

        def desencriptar(mensaje_encriptado: bytes, key: str) -> str:
            f = Fernet(key.encode())
            mensaje_desencriptado = f.decrypt(mensaje_encriptado).decode()
            return mensaje_desencriptado
        ```

## Ejecución

1.  **Activa el entorno virtual (si no lo has hecho):**
    ```bash
    source venv/bin/activate  # En Linux/macOS
    .\venv\Scripts\activate  # En Windows
    ```

2.  **Ejecuta la aplicación usando Uvicorn:**
    ```bash
    uvicorn main:app --reload
    ```
    *(Suponiendo que tu archivo principal de FastAPI se llama `main.py` y tu instancia de `FastAPI` se llama `app`.)*

3.  **Accede a la aplicación en tu navegador:**
    Ve a `http://localhost:8000` (o la `BASE_URL` que hayas configurado).

## Uso

1.  Abre la página principal en tu navegador.
2.  Escribe el mensaje que deseas compartir en el formulario.
3.  Haz clic en el botón "Guardar y Compartir".
4.  Se generará una URL única. Comparte esta URL con la persona que deseas que lea el mensaje.
5.  Cuando la persona acceda a la URL, el mensaje encriptado se recuperará, desencriptará y mostrará.
6.  Después de leer el mensaje, se eliminará del servidor.

## Consideraciones de Seguridad

* **Guarda la `SECRET_KEY` de forma segura.** Si esta clave se expone, los mensajes encriptados podrían ser descifrados por personas no autorizadas. No la hardcodees directamente en el código y considera usar variables de entorno o un sistema de gestión de secretos.
* **La seguridad de la comunicación de la URL compartida depende del canal utilizado.** Considera compartir la URL a través de un medio seguro.
* Este sistema proporciona una forma de compartir mensajes que se autodestruyen después de la lectura. Sin embargo, no garantiza la seguridad absoluta si la URL es interceptada antes de ser accedida.

## Posibles Mejoras

* Agregar una fecha de expiración para los mensajes.
* Implementar una forma de proteger las URLs con una contraseña.
* Mejorar la interfaz de usuario y la experiencia del usuario.
* Implementar logging para el seguimiento y la depuración.
* Considerar el uso de una base de datos en lugar de archivos para almacenar los mensajes temporalmente (con mecanismos de eliminación automática más robustos).

¡Espero que esto te sea útil para tu archivo `README.md`! Si tienes alguna otra pregunta, no dudes en consultarme.
