# Async Media API

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-asyncio-green)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

---

## Descripción

**Async Media API** es una API profesional construida con **FastAPI** que permite:

- Transcribir archivos de audio a texto usando el modelo **Whisper (small)** de OpenAI.
- Sintetizar texto a voz en formato MP3 usando **gTTS**.
- Arquitectura completamente **asíncrona** para alta concurrencia y eficiencia.

Este proyecto es ideal para automatización, bots, asistentes de voz y aplicaciones multimedia.

---

## Características principales

- Endpoints RESTful con validación de datos.
- Procesamiento asíncrono de archivos multimedia.
- Modelos Open Source para transcripción de voz.
- Documentación interactiva automática con Swagger UI.
- Código limpio, modular y con anotaciones de tipo para fácil mantenimiento.

---

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/async-media-api.git
cd async-media-api
```

2. Crea y activa un entorno virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Instala FFmpeg en tu sistema:

- **Windows**: Usa Chocolatey (`choco install ffmpeg`) o descárgalo desde [ffmpeg.org](https://ffmpeg.org/download.html)
- **Linux (Debian/Ubuntu)**:

```bash
sudo apt update && sudo apt install ffmpeg
```

---

## Uso

Ejecuta el servidor local con:

```bash
uvicorn app.main:app --reload
```

Abre en tu navegador la documentación interactiva:

📍 http://localhost:8000/docs

---

## Endpoints principales

| Endpoint        | Método | Descripción                                                   |
|-----------------|--------|---------------------------------------------------------------|
| `/transcribe`   | POST   | Subir archivo de audio y obtener transcripción en texto.      |
| `/synthesize`   | POST   | Enviar texto y recibir archivo de audio MP3 con síntesis de voz. |
| `/health`       | GET    | Verifica que la API esté funcionando correctamente.           |

---

## Ejemplos de uso con `curl`

### Transcribir audio:

```bash
curl -X POST "http://localhost:8000/transcribe/" -F "file=@ruta/al/audio.mp3"
```

### Sintetizar texto:

```bash
curl -X POST "http://localhost:8000/synthesize/" -H "Content-Type: application/json" -d "{\"text\":\"Hola desde Async Media API\"}"
```

---

## Contribuciones

¡Contribuciones y sugerencias son bienvenidas!  
Por favor abre un issue o pull request para mejorar este proyecto.

---

## Licencia

Este proyecto está bajo licencia MIT.  
Consulta el archivo `LICENSE` para más detalles.

---

## Autor

**Ángel León**  
[https://github.com/angelgleon2014](https://github.com/angelgleon2014)  
angelgleoncl@gmail.com
