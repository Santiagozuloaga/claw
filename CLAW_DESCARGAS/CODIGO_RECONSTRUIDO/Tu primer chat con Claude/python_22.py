import whisper

print("Cargando Whisper small...")
model = whisper.load_model("small")

ruta_video = '/content/drive/MyDrive/a.mp4'
ruta_txt   = '/content/drive/MyDrive/Transcripciones_Claw/clase_01.txt'

os.makedirs('/content/drive/MyDrive/Transcripciones_Claw', exist_ok=True)

print("Transcribiendo... (tarda según duración del video)")
result = model.transcribe(ruta_video, language="es", fp16=True)

with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Listo — guardado en Transcripciones_Claw/clase_01.txt")