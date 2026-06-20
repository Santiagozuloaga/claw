import re
texto_limpio = re.sub(r'(\by\b\s*){5,}', '[pausa]', result["text"])

with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write(texto_limpio)