import os
import io
import json
import whisper
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.colab import auth

# Autenticar
auth.authenticate_user()
service = build('drive', 'v3')

raiz           = '/content/drive/MyDrive/S2 CAL A 6'
carpeta_salida = '/content/drive/MyDrive/Transcripciones_Claw'
carpeta_temp   = '/content/temp_videos'
os.makedirs(carpeta_salida, exist_ok=True)
os.makedirs(carpeta_temp,   exist_ok=True)

IGNORAR = {'Apuntes', 'Temarios', 'Horarios'}

def buscar_gdrive(raiz, ignorar):
    encontrados = []
    for root, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in ignorar]
        for f in files:
            if not f.endswith('.gdrive'):
                continue
            if any(f.endswith(x) for x in ('.png.gdrive', '.pdf.gdrive', '.jpg.gdrive')):
                continue
            if f.startswith('¡Bienvenid'):
                continue
            ruta = os.path.join(root, f)
            try:
                data   = json.load(open(ruta))
                doc_id = data.get('doc_id', '')
                if doc_id:
                    rel = os.path.relpath(ruta, raiz)
                    encontrados.append({
                        'nombre': rel.replace('/', '_').replace('.gdrive', ''),
                        'doc_id': doc_id,
                    })
            except:
                pass
    return encontrados

def descargar_con_api(service, doc_id, ruta_destino):
    request  = service.files().get_media(fileId=doc_id)
    fh       = io.FileIO(ruta_destino, 'wb')
    downloader = MediaIoBaseDownload(fh, request, chunksize=50*1024*1024)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"    {int(status.progress() * 100)}%", end='\r')
    fh.close()

print("Cargando Whisper small...")
model = whisper.load_model("small")
print("Whisper listo.\n")

archivos = buscar_gdrive(raiz, IGNORAR)
print(f"Clases a procesar: {len(archivos)}\n")

errores = []

for i, clase in enumerate(archivos, 1):
    nombre   = clase['nombre']
    doc_id   = clase['doc_id']
    ruta_txt = os.path.join(carpeta_salida, nombre + '.txt')
    ruta_vid = os.path.join(carpeta_temp, f'clase_{i}.mp4')

    print(f"[{i}/{len(archivos)}] {nombre}")

    if os.path.exists(ruta_txt):
        print(f"  ⏩ Ya transcrito.\n")
        continue

    try:
        print(f"  ⬇️  Descargando...")
        descargar_con_api(service, doc_id, ruta_vid)

        if not os.path.exists(ruta_vid) or os.path.getsize(ruta_vid) < 1024:
            raise Exception("Archivo vacío")

        print(f"  🎙️  Transcribiendo...")
        result = model.transcribe(ruta_vid, language="es", fp16=False)

        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"  ✅ Guardado.\n")

    except Exception as e:
        print(f"  ❌ Error: {e}\n")
        errores.append(nombre)

    finally:
        if os.path.exists(ruta_vid):
            os.remove(ruta_vid)

print("═══════════════════════════════")
print(f"Transcritos: {len(archivos)-len(errores)}/{len(archivos)}")
if errores:
    print("Errores:")
    for e in errores: print(f"  - {e}")