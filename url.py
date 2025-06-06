from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from cryptography.fernet import Fernet
import json
import os
from uuid import uuid4
import config  # Importamos la configuración desde config.py
import plantillas  # Importamos los templates
from functions import encriptar, desencriptar  # Funciones auxiliares
from fastapi.templating import Jinja2Templates

# Plantillas
templates = Jinja2Templates(directory="templates")

# Creamos un router para las rutas
router = APIRouter()

# Clase de entrada de datos para recibir el mensaje desde el formulario
class Message(BaseModel):
    mensaje: str

# Ruta para mostrar el formulario de envío de mensajes
@router.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse(plantillas.INDEX, {"request": request})


## Endpoint para guardar el mensaje
@router.post("/guardar/", response_class=HTMLResponse)
async def guardar_mensaje(request: Request, mensaje: str = Form(...)):
    try:
        mensaje_encriptado = encriptar(mensaje, config.SECRET_KEY)

        unique_id = str(uuid4())
        file_name = f"{unique_id}.json"

        with open(file_name, "w") as f:
            json.dump({"mensaje": mensaje_encriptado.decode()}, f)

        # url = f"{config.BASE_URL}/leer-mensaje/{file_name}"
        url = f"{config.BASE_URL}/leer-mensaje/{unique_id}"

        return templates.TemplateResponse(plantillas.INDEX, {
            "request": request,
            "share_url": url,
            "success_message": f"Mensaje almacenado correctamente. Aquí tienes la URL para compartir: {url}"
        })

    except Exception as e:
        return templates.TemplateResponse(plantillas.INDEX, {
            "request": request,
            "error_message": f"Hubo un error al guardar el mensaje: {str(e)}"
        })

# Endpoint para leer el mensaje
@router.get("/leer-mensaje/{file_name}", response_class=HTMLResponse)
async def leer_mensaje(file_name: str, request: Request):
    # Aseguramos que el nombre del archivo tenga la extensión .json
    file_name = f"{file_name}.json"  
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            mensaje_encriptado = data["mensaje"].encode()
            mensaje = desencriptar(mensaje_encriptado, config.SECRET_KEY)
         
        os.remove(file_name)

        return templates.TemplateResponse(
            plantillas.MENSAJE,
            {"request": request, "mensaje": mensaje}
        )
    except FileNotFoundError:
        return templates.TemplateResponse(
            plantillas.MENSAJE,
            {"request": request, "error_message": "El mensaje no fue encontrado o ha expirado."}
        )
    except Exception as e:
        return templates.TemplateResponse(
            plantillas.MENSAJE,
            {"request": request, "error_message": f"Error al leer el mensaje: {str(e)}"}
        )
