from flask import request
from flask_restful import Resource, reqparse
from app.owners.models import OwnerModel


class Owners(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument("owner_id", type=int, required=True, help="Owner ID is required.")
    arguments.add_argument(
        "car_quantity", type=int, required=True, help="The field 'car_quantity' cannot be left blank."
    )
    arguments.add_argument(
        "sale_opportunity", type=bool, required=True, help="The field 'sale_opportunity' cannot be left blank."
    )
    arguments.add_argument("cars", type=int, required=True, help="The field 'cars' cannot be left blank.")

    def post(self):
        kwargs = Owners.arguments.parse_args()
        owner_id = kwargs['owner_id']

        if OwnerModel.find_owner(owner_id):
            return {"message": f"Owner id '{owner_id}' already exists."}, 400

        owner = OwnerModel(**kwargs)

        try:
            owner.save_owner()
        except Exception as e:
            return {"message": "An internal error occurred while trying to save a new owner.", "error": str(e)}, 500

        return owner.json(), 201

    def get(self, owner_id):
        owner = OwnerModel.find_owner(owner_id)
        if owner:
            return owner.json(), 200
        return {"message": "Owner not found"}, 404