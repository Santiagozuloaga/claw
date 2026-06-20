import os
import whisper
from google.colab import drive

drive.mount('/content/drive')

# Buscar el video automáticamente en la raíz de MyDrive
raiz = '/content/drive/MyDrive'
formatos = ('.mp4', '.mkv', '.avi', '.webm', '.mov')

videos = [f for f in os.listdir(raiz) if f.lower().endswith(formatos)]
print("Videos encontrados:")
for v in videos:
    tam = os.path.getsize(os.path.join(raiz, v)) / 1024**3
    print(f"  {v} — {tam:.2f} GB")