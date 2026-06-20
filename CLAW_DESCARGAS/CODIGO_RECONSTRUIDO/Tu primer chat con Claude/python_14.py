import os
import json
import whisper
import gdown

raiz           = '/content/drive/MyDrive/S2 CAL A 6'
carpeta_salida = '/content/drive/MyDrive/Transcripciones_Claw'
carpeta_temp   = '/content/temp_videos'
os.makedirs(carpeta_salida, exist_ok=True)
os.makedirs(carpeta_temp,   exist_ok=True)

IGNORAR = {'Apuntes', 'Temarios', 'Horarios'}

# Recopilar todos los .gdrive de clases
def buscar_gdrive(raiz, ignorar):
    encontrados = []
    for root, dirs, files in os.walk(raiz):
        # Ignorar carpetas que no son clases
        dirs[:] = [d for d in dirs if d not in ignorar]
        for f in files:
            if f.endswith('.gdrive') and not f.endswith('.png.gdrive') and not f.endswith('.pdf.gdrive') and not f.endswith('.jpg.gdrive'):
                ruta = os.path.join(root, f)
                try:
                    data     = json.load(open(ruta))
                    doc_id   = data.get('doc_id', '')
                    if doc_id:
                        # Ruta relativa para nombre del txt
                        rel = os.path.relpath(ruta, raiz)
                        encontrados.append({
                            'nombre': rel.replace('/', '_').replace('.gdrive', ''),
                            'doc_id': doc_id,
                        })
                except:
                    pass
    return encontrados

archivos = buscar_gdrive(raiz, IGNORAR)
print(f"Clases encontradas: {len(archivos)}")
for a in archivos:
    print(f"  {a['nombre']}")