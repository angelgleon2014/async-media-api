"""
Archivo principal de la aplicación FastAPI para el proyecto 'Asynchronous Media API'.

- Registra los routers de transcripción y síntesis de medios.
- Expone un endpoint '/health' para chequeo de salud.
- El objeto 'app' es la instancia principal de FastAPI.
"""

from fastapi import FastAPI
from app.routes import transcribe, synthesize

app: FastAPI = FastAPI(title="Asynchronous Media API")

# Registro de los routers para las funcionalidades de transcripción y síntesis
# Incluye las rutas definidas en transcribe y synthesize
app.include_router(transcribe.router)
app.include_router(synthesize.router)

# Endpoint de salud para verificar que la API está activa
@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
