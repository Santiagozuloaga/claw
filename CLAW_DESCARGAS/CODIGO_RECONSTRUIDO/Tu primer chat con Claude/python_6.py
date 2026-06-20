import os
import whisper
from google.colab import drive

# 1. Conectar Drive
drive.mount('/content/drive')

# 2. RUTAS — cambia solo el nombre de la carpeta
carpeta_clases = '/content/drive/MyDrive/NOMBRE_DE_LA_CARPETA_AQUI'
carpeta_salida = '/content/drive/MyDrive/Transcripciones_Claw'

os.makedirs(carpeta_salida, exist_ok=True)

# 3. Cargar modelo — "base" es bueno para español, "small" es mejor si Colab aguanta
print("Cargando Whisper...")
model = whisper.load_model("small")

# 4. Bucle con manejo de errores
formatos_video = ('.mp4', '.mkv', '.avi', '.webm', '.mov')
clases = sorted([
    f for f in os.listdir(carpeta_clases)
    if f.lower().endswith(formatos_video)
])

print(f"Archivos encontrados: {len(clases)}")
errores = []

for i, archivo in enumerate(clases, 1):
    ruta_completa = os.path.join(carpeta_clases, archivo)
    nombre_txt    = archivo.rsplit('.', 1)[0] + ".txt"
    ruta_txt      = os.path.join(carpeta_salida, nombre_txt)

    print(f"\n[{i}/{len(clases)}] {archivo}")

    if os.path.exists(ruta_txt):
        print(f"  ⏩ Ya existe, saltando.")
        continue

    # Verificar que el archivo no esté vacío
    if os.path.getsize(ruta_completa) < 1024:
        print(f"  ⚠️ Archivo muy pequeño, saltando.")
        errores.append(archivo)
        continue

    try:
        result = model.transcribe(ruta_completa, language="es", fp16=False)
        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"  ✅ Guardado.")

    except Exception as e:
        print(f"  ❌ Error en {archivo}: {e}")
        errores.append(archivo)
        continue  # Sigue con el siguiente archivo

print("\n--- PROCESO FINALIZADO ---")
if errores:
    print(f"Archivos con error ({len(errores)}):")
    for e in errores:
        print(f"  - {e}")
else:
    print("Sin errores.")