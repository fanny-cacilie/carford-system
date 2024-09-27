from flask import request
from flask_restful import Resource, reqparse
from app.cars.models import CarModel, ColorEnum, ModelEnum
from app.owners.models import OwnerModel


def validate_color(value):
    try:
        return ColorEnum[value]
    except KeyError:
        raise ValueError(f"{value} is not a valid color. Possible values: {[color.name for color in ColorEnum]}.")

def validate_model(value):
    try:
        return ModelEnum[value]
    except KeyError:
        raise ValueError(f"{value} is not a valid model. Possible values: {[model.name for model in ModelEnum]}.")


class Cars(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument("car_id", type=int, required=True, help="Car ID is required.")
    arguments.add_argument(
        "color", type=validate_color, required=True, help="The field 'color' must be: blue, yellow or gray."
    )
    arguments.add_argument(
        "model", type=validate_model, required=True, help="The field 'model' must be: hatch, sedan or convertible."
    )
    arguments.add_argument("owner_id", type=int, required=True, help="Owner ID is required.")

    def post(self):

        kwargs = Cars.arguments.parse_args()

        print(kwargs)

        car_id = kwargs['car_id']
        if CarModel.find_car(car_id):
            return {"message": f"Error while registering car. Car id '{car_id}' already exists."}, 400
        car = CarModel(**kwargs)

        owner_id = kwargs['owner_id']
        if not OwnerModel.find_owner(owner_id):
            return {"message": f"Error while registering car. Owner id '{owner_id}' does not exist in the system."}, 400

        owner = OwnerModel.find_owner(owner_id)
        if len(owner.cars) > 3:
            return {"message": f"Error while registering car to Owner id '{owner_id}'. It has reached the limit of 3 cars."}, 400

        try:
            car.save_car()
        except Exception as e:
            return {"message": "An internal error occurred while trying to save a new car.", "error": str(e)}, 500

        return car.json(), 201


    def get(self):
        return {"Cars": [car.json() for car in CarModel.query.all()]}
