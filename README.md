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

## ⚡️ Performance Tip: Use a GPU! 🖥️💨

Running **kokoro_tts** on a **GPU** 🖥️ will significantly speed up the text-to-speech generation process.

- 🚀 Faster inference times
- 🎯 More responsive real-time applications
- 🔊 Smoother experience for generating longer audio clips

If you're working on a local machine, make sure your environment is set up with CUDA and a compatible GPU.  
For cloud deployments, platforms like Google Colab, AWS, and Paperspace offer GPU-backed runtimes.

> 💡 Tip: CPU works fine too, but for blazing fast results, GPU is the way to go!

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

---

## 📱 Android Integration: Jetson Kokoro TTS App

You can connect this **kokoro_tts** server with the Android client app from the following repository:  
👉 [Jetson_App (kokoro_tts branch)](https://github.com/farmaker47/Jetson_App/tree/kokoro_tts)

### 🔗 How it works

The Android app sends POST requests to the kokoro_tts server's `/api/generate` endpoint — just like the `curl` example in the README. This makes it easy to use the TTS engine on your mobile device via a responsive UI.

### ✅ What you need to do:

1. **Run the kokoro_tts server** on a machine (locally or hosted).
2. **Expose it using [ngrok](https://ngrok.com/)** or any other tunneling tool.
3. **Set the base URL** in the Android app's NetworkModule file to match your server URL (e.g., `https://your-ngrok-url/api/generate`).
4. **Build and run** the Android app to start sending TTS prompts directly from your device!

> 💡 Great for real-time speech generation, prototyping voice interfaces, and testing multilingual support on mobile!

---

📂 Check out the Android repo here:  
[https://github.com/farmaker47/Jetson_App/tree/kokoro_tts](https://github.com/farmaker47/Jetson_App/tree/kokoro_tts)

---

## 💡 Credits

This repository is built on top of the incredible [Kokoro TTS model](https://huggingface.co/hexgrad/Kokoro-82M) by **hexgrad**. 
