class Amiibo():

    def __init__(self, amiiboSeries, character, gameSeries, name, image, amiibo_type):
        self.amiiboSeries = amiiboSeries
        self.character = character
        self.gameSeries = gameSeries
        self.name = name
        self.image = image
        self.type = amiibo_type

    def __str__(self):
        return (f"Nombre: {self.name}\n"
                f"Personaje: {self.character}\n"
                f"Serie de Amiibo: {self.amiiboSeries}\n"
                f"Videojuego: {self.gameSeries}\n"
                f"Tipo: {self.type}\n"
                f"Image URL: {self.image}\n")
    
    # Función para buscar en diferentes atributos de la clase
    @classmethod
    def buscar_por_atributo(cls, amiibos, atributo, valor):
    # Verificar si el atributo es válido
        # Filtrar los amiibos donde el valor del atributo coincide con el valor dado
        resultado = [amiibo for amiibo in amiibos if getattr(amiibo, atributo, None) == valor]
        return resultado