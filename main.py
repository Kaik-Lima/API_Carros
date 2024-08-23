from flask import Flask, jsonify, make_response, request
from bd import Cars


app = Flask('cars')
@app.route('/cars', methods=['GET'])
def get_carros(): return Cars


# Visualizar dados
@app.route('/cars/<int:id>', methods=['GET'])
def get_cars_id(id):
    for car in Cars:
        if car.get('id') == id: return jsonify(car)


# Criar dados
@app.route('/cars', methods=['POST'])
def cars_create():
    car = request.json
    Cars.append(car)
    return make_response(
        jsonify(msg='Carro cadastrado com sucesso',
                car=car)
    )

# Editar dados
@app.route('/cars/<int:id>', methods=['PUT'])
def car_edit(id):
    alterCar = request.get_json()
    for index, car in enumerate(Cars):
        if car.get('id') == id:
            Cars[index].update(alterCar)
            return jsonify(Cars[index]) 
        
# Deletar dados
@app.route('/cars/<int:id>', methods=['DELETE'])
def car_del(id):
    for index, car in enumerate(Cars):
        if car.get('id') == id:
            del Cars[index]
            return jsonify({'msg': 'Carro excluído com sucesso'})

app.run(port=5000, host='localhost')