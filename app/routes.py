from flask import Blueprint, jsonify
from .controllers import DataController

main = Blueprint('main', __name__)
controller = DataController()

@main.route('/api/conversionCelMXaPersonal', methods=['GET'])
def get_conversion_celmx_a_personal():
    data = controller.get_conversions()
    return jsonify(data), 200

@main.route('/api/conversionPorcentajeActivacion', methods=['GET'])
def get_conversion_porcentaje_activacion():
    data = controller.get_conversion_porcentaje_activacion()
    return jsonify(data), 200

@main.route('/api/crecimientoAcumuladoUsuarios', methods=['GET'])
def get_crecimiento_acumulado_usuarios():
    data = controller.get_growth()
    return jsonify(data), 200

@main.route('/api/desgloseUsuarios', methods=['GET'])
def get_desglose_usuarios():
    data = controller.get_user_breakdown()
    return jsonify(data), 200

@main.route('/api/placesMasUsados', methods=['GET'])
def get_places_mas_usados():
    data = controller.get_popular_places()
    return jsonify(data), 200
