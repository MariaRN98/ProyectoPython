class Amiibo():

    def __init__(self, amiiboSeries, character, gameSeries, name, image, amiibo_type):
        self.amiiboSeries = amiiboSeries
        self.character = character
        self.gameSeries = gameSeries
        self.name = name
        self.image = image
        self.type = amiibo_type

    def __str__(self):
        return (f"Amiibo: {self.name}\n"
                f"Character: {self.character}\n"
                f"Amiibo Series: {self.amiiboSeries}\n"
                f"Game Series: {self.gameSeries}\n"
                f"Type: {self.type}\n"
                f"Image URL: {self.image}\n")