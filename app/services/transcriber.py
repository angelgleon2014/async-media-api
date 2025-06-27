"""
Servicio de transcripción de audio a texto usando Whisper.

- Carga el modelo Whisper ('small') una sola vez al iniciar el módulo para eficiencia.
- La función 'transcribe_audio' recibe un archivo de audio, lo guarda temporalmente, realiza la transcripción y elimina el archivo temporal.
- La transcripción se realiza de forma sincrónica ya que Whisper no es nativo async.
- Devuelve el texto transcrito.
"""

import whisper
import aiofiles
import uuid
import os
from fastapi import UploadFile

# Cargar el modelo (una sola vez al iniciar)
model = whisper.load_model("small")

async def transcribe_audio(file: UploadFile) -> str:
    # Guardar archivo temporal
    filename: str = f"temp_{uuid.uuid4().hex}_{file.filename}"

    async with aiofiles.open(filename, "wb") as out_file:
        content: bytes = await file.read()
        await out_file.write(content)

    # Transcripción sincrónica (Whisper no es async nativo, se adapta)
    result: dict = model.transcribe(filename)
    text: str = result["text"]

    # Eliminar archivo temporal
    os.remove(filename)
    return text
