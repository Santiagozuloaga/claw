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

    print(f"[{i}/{len(archivos)}] {nombre}")

    # Saltar si ya existe
    if os.path.exists(ruta_txt):
        print(f"  ⏩ Ya transcrito, saltando.\n")
        continue

    # Descargar video temporalmente
    ruta_video = os.path.join(carpeta_temp, f"clase_{i}.mp4")
    url = f"https://drive.google.com/uc?id={doc_id}"

    try:
        print(f"  ⬇️  Descargando...")
        gdown.download(url, ruta_video, quiet=True, fuzzy=True)

        if not os.path.exists(ruta_video) or os.path.getsize(ruta_video) < 1024:
            raise Exception("Archivo descargado vacío o inaccesible")

        print(f"  🎙️  Transcribiendo...")
        result = model.transcribe(ruta_video, language="es", fp16=False)

        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"  ✅ Guardado.\n")

    except Exception as e:
        print(f"  ❌ Error: {e}\n")
        errores.append(nombre)

    finally:
        # Borrar video temporal para no llenar el disco de Colab
        if os.path.exists(ruta_video):
            os.remove(ruta_video)

print("═══════════════════════════════")
print("PROCESO FINALIZADO")
print(f"Transcritos: {len(archivos) - len(errores)}/{len(archivos)}")
if errores:
    print(f"Errores ({len(errores)}):")
    for e in errores:
        print(f"  - {e}")