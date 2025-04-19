# 🎙️ kokoro_tts

An elegant and efficient **Text-To-Speech (TTS)** implementation powered by the amazing **Kokoro** library.  
> *Kokoro* (心) is a Japanese word that means **"heart"** or **"spirit"** – and that’s exactly what this TTS brings to your audio! 💖

---

## 🔥 About Kokoro

[Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) is an **open-weight TTS model** with **82 million parameters**. Despite its lightweight architecture, Kokoro offers:

- 🎧 High-quality speech synthesis  
- ⚡️ Fast and efficient inference  
- 💸 Low compute cost  
- 🛠️ Apache-licensed weights for **commercial and personal use**

👉 Check out the original [GitHub repository](https://github.com/hexgrad/kokoro)  
👉 Try it out on [Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)

---

## 🔊 Try It Yourself

🎵  **[Experience sample audios](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/SAMPLES.md)**  
📊  **[Check out evaluations](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/EVAL.md)**

---

## 🚀 Getting Started

### 🧰 Installation

```bash
pip install -r requirements.txt
```

### ▶️ Running the Server

```bash
python kokoro_final.py
```

## 🔁 Example Usage

Once your server is up and running (e.g., via `python kokoro_final.py`), use the following `curl` command to generate speech. You’ll get a public URL from `ngrok`. Use that URL in the following curl command:

```bash
curl -X POST https://<your-ngrok-url>/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Well, hello there!", "voice": "af_heart"}' \
  --output test_audio_heart.wav
```
📝 Note: Replace the `https://<your-ngrok-url>` url with the actual `ngrok`will provide like `https://5483-3478-2345.ngrok-free.app`

## 💡 Credits

This repository is built on top of the incredible [Kokoro TTS model](https://huggingface.co/hexgrad/Kokoro-82M) by **hexgrad**. 
