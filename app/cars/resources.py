from flask import request
from flask_restful import Resource, reqparse
from app.cars.models import CarModel


class Cars(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument("car_id", type=int, required=True, help="Car ID is required.")
    arguments.add_argument(
        "color", type=str, required=True, help="The field 'color' cannot be left blank."
    )
    arguments.add_argument(
        "model", type=str, required=True, help="The field 'model' cannot be left blank."
    )
    arguments.add_argument("owner_car_id", type=int, required=True, help="The field 'cars' cannot be left blank.")

    def post(self):
        kwargs = Cars.arguments.parse_args()
        car_id = kwargs['car_id']

        if CarModel.find_car(car_id):
            return {"message": f"Car id '{car_id}' already exists."}, 400

        car = CarModel(**kwargs)

        try:
            car.save_car()
        except Exception as e:
            return {"message": "An internal error occurred while trying to save a new car.", "error": str(e)}, 500

        return car.json(), 201

    def get(self, car_id):
        car = CarModel.find_car(car_id)
        if car:
            return car.json(), 200
        return {"message": "Car not found"}, 404