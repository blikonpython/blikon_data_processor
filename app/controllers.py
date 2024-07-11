from .models import FirebaseModel

class DataController:
    def __init__(self):
        self.model = FirebaseModel()

    def get_conversions(self):
        return self.model.get_data('conversionCelMXaPersonal')

    def get_conversion_porcentaje_activacion(self):
        return self.model.get_data('conversionPorcentajeActivacion')

    def get_growth(self):
        return self.model.get_data('crecimientoAcumuladoUsuarios')

    def get_user_breakdown(self):
        return self.model.get_data('desgloseUsuarios')

    def get_popular_places(self):
        return self.model.get_data('placesMasUsados')
