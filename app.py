from fastapi import FastAPI

from url import router  # Importamos el router desde url.py

# Inicializamos FastAPI
app = FastAPI()

# Incluimos las rutas desde url.py
app.include_router(router)
