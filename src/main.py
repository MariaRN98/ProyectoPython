import json
import requests

# Descargar el archivo JSON desde la URL cruda de GitHub
url = "https://raw.githubusercontent.com/matthewlyons/amiibo-database/refs/heads/master/db/amiibo.json"
response = requests.get(url)

# Asegúrate de que la solicitud fue exitosa
if response.status_code == 200:
    # Paso 2: Cargar los datos JSON
    data = response.json()  # O también puedes usar json.loads(response.text)
    
        # Paso 3: Filtrar y mostrar solo los datos donde el name sea "Mario"
    mario_data = [item for item in data if item['character'] == "Mario"]
    
    # Paso 4: Mostrar los datos filtrados por consola
    for item in mario_data:
        print(json.dumps(item, indent=4))  # Imprimir cada objeto de Mario en formato JSON legible
else:
    print(f"Error al descargar el archivo: {response.status_code}")