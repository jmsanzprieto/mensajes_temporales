# functions.py
from cryptography.fernet import Fernet

# Función para encriptar
def encriptar(mensaje, key):
    fernet = Fernet(key)
    return fernet.encrypt(mensaje.encode())

# Función para desencriptar
def desencriptar(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()