# ---------------------------------------------------------
# server_scrapping.py
# Servidor que simula tareas de scraping y envía los datos
# al servidor de procesamiento
# ---------------------------------------------------------

from fastapi import FastAPI
import httpx  # Cliente HTTP asíncrono para enviar datos
import asyncio

app = FastAPI()

# Dirección del servidor de procesamiento
PROCESSING_SERVER = "http://127.0.0.1:8001/procesar"

# ---------------------------------------------------------
# Ruta raíz: prueba de funcionamiento
# ---------------------------------------------------------
@app.get("/")
def home():
    return {"mensaje": "Servidor de scraping activo"}


# ---------------------------------------------------------
# Simula una tarea de scraping y envía resultados
# ---------------------------------------------------------
@app.post("/procesar")
async def scrapear_datos():
    # Simulamos que obtuvimos datos de scraping
    datos = {
        "sitio": "TiendaEjemplo.com",
        "precios": [100, 120, 90, 110]
    }

    # Enviamos esos datos al servidor de procesamiento
    async with httpx.AsyncClient() as client:
        try:
            respuesta = await client.post(PROCESSING_SERVER, json=datos)
            if respuesta.status_code == 200:
                return {"status": "ok", "respuesta": respuesta.json()}
            else:
                return {"status": "error", "detalle": respuesta.text}
        except Exception as e:
            return {"status": "error", "detalle": str(e)}
