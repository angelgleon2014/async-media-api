"""
Router para la funcionalidad de síntesis de texto a audio.

- Define el prefijo '/synthesize' y la etiqueta 'Synthesis'.
- Declara el modelo 'TextInput' que espera un campo 'text' (texto a sintetizar).
- Expone un endpoint POST que recibe un JSON con el texto y responde con la ruta del archivo de audio sintetizado en formato JSON.
- Utiliza el servicio 'synthesize_text' para generar el audio a partir del texto recibido.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.services.synthesizer import synthesize_text

router: APIRouter = APIRouter(prefix="/synthesize", tags=["Synthesis"])

class TextInput(BaseModel):
    text: str

# Endpoint para recibir texto y devolver la ruta del archivo de audio sintetizado en JSON
@router.post("/")
async def synthesize(input: TextInput) -> JSONResponse: # se espera un texto y responde con la ruta del archivo de audio sintetizado en formato JSON
    audio_path: str = await synthesize_text(input.text)
    return JSONResponse(content={"audio_file": audio_path})
