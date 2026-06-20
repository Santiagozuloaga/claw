import os
import whisper

os.makedirs('/content/drive/MyDrive/Transcripciones_Claw', exist_ok=True)

model = whisper.load_model("small")
print("Modelo cargado")