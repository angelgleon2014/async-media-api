"""
Servicio de síntesis de texto a voz usando gTTS (Google Text-to-Speech).

- La función 'synthesize_text' recibe un texto, genera un archivo de audio MP3 ('output.mp3') y retorna el nombre del archivo.
- Aunque la función es asíncrona, las operaciones de gTTS y guardado de archivo son sincrónicas.
"""

from gtts import gTTS

async def synthesize_text(text: str) -> str:
    filename: str = "output.mp3"
    tts: gTTS = gTTS(text)
    tts.save(filename)
    return filename
