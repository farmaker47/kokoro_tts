from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import io
import numpy as np
import soundfile as sf
import torch

# Kokoro TTS
from kokoro import KPipeline

# Ngrok + Uvicorn
from pyngrok import ngrok
import nest_asyncio
import uvicorn

# ------------------------------------------------------------------------------
# Global pipeline init

# Choose your language code (🇺🇸='a' 🇬🇧='b' 🇪🇸='e' etc.) from https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
LANG_CODE = "a"
pipeline = KPipeline(lang_code=LANG_CODE)

# ------------------------------------------------------------------------------
# FastAPI setup

app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str
    voice: str = "af_heart"    # default voice identifier OR select from https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
    speed: float = 1.0         # speaking speed multiplier

def generate_audio_from_prompt(prompt: str, voice: str, speed: float) -> io.BytesIO:
    """
    Runs Kokoro TTS pipeline on the prompt, stitches all segments,
    and writes a single WAV into a BytesIO.
    """
    generator = pipeline(
        prompt,
        voice=voice,
        speed=speed,
        split_pattern=r"\n+"
    )

    # collect each chunk of audio
    segments = [audio for (_gs, _ps, audio) in generator]
    if not segments:
        raise RuntimeError("Kokoro returned no audio segments")

    # concatenate into one waveform
    full_audio = np.concatenate(segments, axis=0)

    # write to wav BytesIO
    wav_io = io.BytesIO()
    sf.write(wav_io, full_audio, 24000, format="WAV")
    wav_io.seek(0)
    return wav_io

@app.post("/api/generate")
def generate_endpoint(req: GenerateRequest):
    try:
        wav_io = generate_audio_from_prompt(req.prompt, req.voice, req.speed)
        return StreamingResponse(wav_io, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ------------------------------------------------------------------------------
# Run via `python kokoro_final.py`
if __name__ == "__main__":
    # expose via ngrok if desired
    ngrok.set_auth_token("2veqADueBWtPfZajYkoH5E6apnS_.........")
    tunnel = ngrok.connect(8000)
    print("Public URL:", tunnel.public_url)

    # allow nested asyncio loops
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)
