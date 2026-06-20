result = model.transcribe('/content/drive/MyDrive/a.mp4', language="es", fp16=True)

with open('/content/drive/MyDrive/Transcripciones_Claw/clase_01.txt', "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Listo")