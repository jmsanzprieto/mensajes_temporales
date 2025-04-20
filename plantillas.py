# templates.py
import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

INDEX =  os.getenv("INDEX")
MENSAJE =  os.getenv("MENSAJE")
