"""
Router para la funcionalidad de transcripción de audio.

- Define el prefijo '/transcribe' y la etiqueta 'Transcription'.
- Expone un endpoint POST que recibe un archivo de audio y retorna la transcripción en formato JSON.
- Utiliza el servicio 'transcribe_audio' para procesar el archivo recibido.
"""

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.transcriber import transcribe_audio

router: APIRouter = APIRouter(prefix="/transcribe", tags=["Transcription"])

# Endpoint para recibir un archivo de audio y devolver la transcripción en JSON
@router.post("/")
async def transcribe(file: UploadFile = File(...)) -> JSONResponse:
    result: str = await transcribe_audio(file)
    return JSONResponse(content={"transcription": result})

