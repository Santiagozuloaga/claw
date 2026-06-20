import os
raiz = '/content/drive/MyDrive'
for f in os.listdir(raiz):
    if f.endswith(('.mp4', '.mkv', '.avi', '.webm', '.mov')):
        tam = os.path.getsize(os.path.join(raiz, f)) / 1024**3
        print(f"{f} — {tam:.2f} GB")