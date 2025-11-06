# ----------------------------------------------------------
# server_processing.py
# Servidor FastAPI para recibir y procesar datos de scraping
# ----------------------------------------------------------

from fastapi import FastAPI, Request
import json

# Creamos la aplicación principal de FastAPI
app = FastAPI()

# Base de datos simulada (por ahora un diccionario en memoria)
data_store = []

# ----------------------------------------------------------
# Ruta principal: solo para verificar que el servidor funcione
# ----------------------------------------------------------
@app.get("/")
def home():
    return {"mensaje": "Servidor de procesamiento activo"}

# ----------------------------------------------------------
# Ruta para recibir datos de scraping desde los clientes
# ----------------------------------------------------------
@app.post("/procesar")
async def procesar_datos(request: Request):
    # Leemos el cuerpo de la solicitud (el JSON que envía el cliente)
    datos = await request.json()

    # Guardamos esos datos en memoria
    data_store.append(datos)

    # Simulamos un procesamiento básico: promedio de precios
    if "precios" in datos:
        promedio = sum(datos["precios"]) / len(datos["precios"])
        return {"status": "ok", "promedio": promedio}

    # Si no vienen precios, solo confirmamos recepción
    return {"status": "ok", "mensaje": "Datos recibidos correctamente"}

# ----------------------------------------------------------
# Ruta para consultar los datos procesados
# ----------------------------------------------------------
@app.get("/resultados")
def ver_resultados():
    return {"datos_guardados": data_store}
