import requests

# Lista de URLs
urls = [
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
    "https://raw.githubusercontent.com/ph00lt0/blocklist/master/blocklist.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_59.txt"
]

# Conjunto para almacenar líneas únicas
lines_set = set()

# Descargar y procesar cada archivo
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        lines = response.text.splitlines()
        lines_set.update(lines)  # Agrega líneas únicas
        print(f"Descargado: {url}")
    except requests.RequestException as e:
        print(f"Error al descargar {url}: {e}")

# Guardar el resultado en un archivo
with open("compilado.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(lines_set)))

print("Archivo 'compilado.txt' generado con éxito.")
