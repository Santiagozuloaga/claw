import os

raiz = '/content/drive/MyDrive/S2 CAL A 6'
formatos_video = ('.mp4', '.mkv', '.avi', '.webm', '.mov')

for materia in os.listdir(raiz):
    ruta_materia = os.path.join(raiz, materia)
    if not os.path.isdir(ruta_materia) or materia == 'Apuntes':
        continue
    for subcarpeta in os.listdir(ruta_materia):
        ruta_sub = os.path.join(ruta_materia, subcarpeta)
        if not os.path.isdir(ruta_sub):
            continue
        videos = [f for f in os.listdir(ruta_sub) if f.lower().endswith(formatos_video)]
        if videos:
            print(f"{materia}/{subcarpeta}: {len(videos)} videos")
            print(f"   Ejemplo: {videos[0]}")