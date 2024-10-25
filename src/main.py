import json
import requests
from amiibo import Amiibo

# Descargar el archivo JSON y cargarlo como una lista de instancias de Amiibo
url = "https://raw.githubusercontent.com/matthewlyons/amiibo-database/master/db/amiibo.json"
response = requests.get(url)
data = response.json()

# Crear una lista de objetos Amiibo
amiibos = [Amiibo(item['amiiboSeries'], item['character'], item['gameSeries'], 
                  item['name'], item['image'], item['type']) for item in data]

columna = ""
busqueda = ""

print("Bienvenido a AmiiboDB")

while True:
    print("1- Mostrar todos los datos")
    print("2- Buscar")
    print("0- Salir del programa")
    seleccion = int(input("Seleccione una opcion...")) #condicion para que olo meta los numeros deseados

    if seleccion == 1:
        print("opcion 1")
    elif seleccion == 2:
        print("opcion 2")
        print("Selecione la categoria por la que desea buscar")
        print("1- Nombre")
        print("2- Personaje")
        print("3- Serie Amiibo")
        print("4- Videojuego")
        print("5- Tipo")
        print("0- Salir")
        seleccionCat = int(input("Seleccione una categoria de busqueda...")) #condicion para que solo meta los numeros eseados
        if seleccionCat == 1:
            columna = "name"
        elif seleccionCat == 2:
            columna = "character"
        elif seleccionCat == 3:
            columna = "amiiboSeries"
        elif seleccionCat == 4:
            columna = "gameSeries"
        elif seleccionCat == 5:
            columna = "type"
        elif seleccionCat == 0:
            print("salir") #que salga de la seleccion de categoria y vuelva al menu
            break
        busqueda = input("¿Que desea buscar?" )
        resultado = Amiibo.buscar_por_atributo(amiibos, columna, busqueda)
        for amiibo in resultado:
            print(amiibo)

    elif seleccion == 0:
        break












"""
        # Descargar el archivo JSON desde la URL cruda de GitHub
        url = "https://raw.githubusercontent.com/matthewlyons/amiibo-database/refs/heads/master/db/amiibo.json"
        response = requests.get(url)

        # Asegúrate de que la solicitud fue exitosa
        if response.status_code == 200:
         # Paso 2: Cargar los datos JSON
            data = response.json()  # O también puedes usar json.loads(response.text)
    
        # Paso 3: Filtrar y mostrar solo los datos donde el name sea "Mario"
            filtro = [item for item in data if item[columna] == busqueda]
    
        # Paso 4: Mostrar los datos filtrados por consola
            for item in filtro:
             print(json.dumps(item, indent=4))  # Imprimir cada objeto de Mario en formato JSON legible
        else:
            print(f"Error al descargar el archivo: {response.status_code}")

"""




