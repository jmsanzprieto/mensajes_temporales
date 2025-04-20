# config.py
import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Configuración desde el archivo .env
SECRET_KEY = os.getenv("SECRET_KEY")
# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# SMTP_USER = os.getenv("SMTP_USER")
# SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
# FROM_EMAIL = os.getenv("FROM_EMAIL")
BASE_URL = os.getenv("BASE_URL")

