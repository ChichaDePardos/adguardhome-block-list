# Compilador de Listas de Bloqueo

Este script en Python descarga archivos de listas de bloqueo desde varias URLs, los combina en un solo archivo y elimina los duplicados.

## Características
- Descarga archivos de listas de bloqueo desde URLs predefinidas.
- Elimina líneas duplicadas automáticamente.
- Guarda el resultado en un archivo `compilado.txt` ordenado.

## Requisitos
Necesitas tener instalado Python 3 y la librería `requests`. Si no la tienes, instálala con:

```sh
pip install requests
```

## Uso
1. Clona este repositorio o descarga el archivo `compilar_listas.py`.
2. Ejecuta el script en tu terminal o línea de comandos:

```sh
python compilar_listas.py
```

3. Se generará un archivo `compilado.txt` con las listas de bloqueo unificadas y sin duplicados.

## Código
El script principal es el siguiente:

```python
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
```

## Contribuciones
Si deseas agregar más listas o mejorar el script, ¡eres bienvenido a hacer un pull request!

## Licencia
Este proyecto está bajo la licencia MIT.

