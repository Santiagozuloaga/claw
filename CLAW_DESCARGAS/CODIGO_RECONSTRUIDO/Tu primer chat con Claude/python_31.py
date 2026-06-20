import os, re, whisper
from google.colab import drive

drive.mount('/content/drive')

raiz        = '/content/drive/MyDrive'
carpeta_txt = '/content/drive/MyDrive/Transcripciones_Claw'
formatos    = ('.mp4', '.mkv', '.avi', '.webm', '.mov')

os.makedirs(carpeta_txt, exist_ok=True)

model = whisper.load_model("small")

videos = [f for f in os.listdir(raiz) if f.lower().endswith(formatos)]

if not videos:
    print("No hay videos en la raíz de Drive")
else:
    for video in sorted(videos):
        ruta_video = os.path.join(raiz, video)
        nombre_txt = video.rsplit('.', 1)[0] + '.txt'
        ruta_txt   = os.path.join(carpeta_txt, nombre_txt)

        if os.path.exists(ruta_txt):
            print(f"⏩ Ya transcrito: {video}")
            continue

        tam = os.path.getsize(ruta_video) / 1024**3
        print(f"🎙️ Transcribiendo: {video} ({tam:.2f} GB)...")

        result = model.transcribe(ruta_video, language="es", fp16=True)
        texto  = re.sub(r'(\by\b\s*){5,}', '[pausa]', result["text"])

        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"✅ Guardado: {nombre_txt}\n")

print("--- FINALIZADO ---")