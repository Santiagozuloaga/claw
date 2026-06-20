import os, re, whisper
from google.colab import drive

drive.mount('/content/drive')

model = whisper.load_model("small")

videos = {
    'a.mp4': 'Biologia_Macro_Teorica_Clase_01.txt',
    'b.mp4': 'Biologia_Macro_Teorica_Clase_02.txt',
}

os.makedirs('/content/drive/MyDrive/Transcripciones_Claw', exist_ok=True)

for video, nombre_txt in videos.items():
    ruta_video = f'/content/drive/MyDrive/{video}'
    ruta_txt   = f'/content/drive/MyDrive/Transcripciones_Claw/{nombre_txt}'

    if not os.path.exists(ruta_video):
        print(f"No encontrado: {video}")
        continue

    print(f"Transcribiendo {video}...")
    result = model.transcribe(ruta_video, language="es", fp16=True)
    texto  = re.sub(r'(\by\b\s*){5,}', '[pausa]', result["text"])

    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"✅ {nombre_txt}\n")

print("Listo — borra los videos de Drive cuando confirmes los .txt")