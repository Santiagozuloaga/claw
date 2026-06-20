import json, os

# Ver qué hay dentro de un .gdrive
raiz = '/content/drive/MyDrive/S2 CAL A 6'
for root, dirs, files in os.walk(raiz):
    for f in files:
        if f.endswith('.gdrive'):
            ruta = os.path.join(root, f)
            try:
                contenido = open(ruta).read()
                print(f"{f}:")
                print(contenido[:200])
                print("---")
                break  # Solo ver el primero
            except:
                pass
    break