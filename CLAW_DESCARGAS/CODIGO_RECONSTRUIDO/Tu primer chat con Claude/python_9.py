import os

raiz = '/content/drive/MyDrive/S2 CAL A 6'
for carpeta in os.listdir(raiz):
    ruta = os.path.join(raiz, carpeta)
    if os.path.isdir(ruta):
        archivos = os.listdir(ruta)
        print(f"{carpeta}: {len(archivos)} archivos")
        for a in archivos[:3]:  # muestra los primeros 3
            print(f"   - {a}")