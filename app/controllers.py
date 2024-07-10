from .models import FirebaseModel

class DataController:
    def __init__(self):
        self.model = FirebaseModel()

    def get_conversions(self):
        return self.model.get_data("blikon/conversionCelMXaPersonal")

    def get_conversion_porcentaje_activacion(self):
        return self.model.get_data("blikon/conversionPorcentajeActivacion")

    def get_growth(self):
        return self.model.get_data("blikon/crecimientoAcumuladoUsuarios")

    def get_user_breakdown(self):
        return self.model.get_data("blikon/desgloseUsuarios")

    def get_popular_places(self):
        return self.model.get_data("blikon/placesMasUsados")
