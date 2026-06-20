import os, whisper

drive.mount('/content/drive')

ruta_video  = '/content/drive/MyDrive/Captures/NOMBRE_CLASE.mp4'
ruta_salida = '/content/drive/MyDrive/Transcripciones_Claw/'

os.makedirs(ruta_salida, exist_ok=True)
model  = whisper.load_model("small")
result = model.transcribe(ruta_video, language="es", fp16=True)

nombre_txt = os.path.basename(ruta_video).replace('.mp4', '.txt')
with open(ruta_salida + nombre_txt, "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Listo:", nombre_txt)