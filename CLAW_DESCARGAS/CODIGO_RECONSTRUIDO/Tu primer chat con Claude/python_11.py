import os
import whisper

# Todos los formatos que Zoom puede generar
FORMATOS_VIDEO = ('.mp4', '.m4v', '.mov', '.avi', '.mkv', '.webm', '.ts', '.mts', '.m4a')

IGNORAR = {'Apuntes', 'Temarios', 'Horarios'}

raiz        = '/content/drive/MyDrive/S2 CAL A 6'
carpeta_salida = '/content/drive/MyDrive/Transcripciones_Claw'
os.makedirs(carpeta_salida, exist_ok=True)

# Buscar videos en TODOS los niveles de subcarpetas
def buscar_videos(carpeta, ignorar=set()):
    encontrados = []
    for entrada in os.scandir(carpeta):
        if entrada.name in ignorar:
            continue
        if entrada.is_dir(follow_symlinks=False):
            encontrados.extend(buscar_videos(entrada.path))
        elif entrada.is_file() and entrada.name.lower().endswith(FORMATOS_VIDEO):
            encontrados.append(entrada.path)
    return encontrados

print("Buscando videos...")
videos = sorted(buscar_videos(raiz, ignorar=IGNORAR))
print(f"Videos encontrados: {len(videos)}")
for v in videos:
    print(f"  {v.replace(raiz, '')}")