import os

raiz = '/content/drive/MyDrive/S2 CAL A 6'

print("Escaneando TODO el contenid[LOCAL_PATH]")
for root, dirs, files in os.walk(raiz):
    nivel = root.replace(raiz, '').count(os.sep)
    sangria = '  ' * nivel
    print(f"{sangria}{os.path.basename(root)}/")
    for archivo in files:
        print(f"{sangria}  [{archivo.split('.')[-1].upper()}] {archivo}")