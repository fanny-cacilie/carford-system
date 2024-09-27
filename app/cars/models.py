from enum import Enum
from sqlalchemy import ForeignKey

from app import db


class ColorEnum(Enum):
    yellow = 1
    blue = 2
    gray = 3


class ModelEnum(Enum):
    hatch = 1
    sedan = 2
    convertible = 3


class CarModel(db.Model):
    __tablename__ = "cars"

    car_id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(ColorEnum), nullable=False)
    model = db.Column(db.Enum(ModelEnum), nullable=False)
    owner_id = db.Column(db.Integer, ForeignKey("owners.owner_id"), nullable=False)

    def __repr__(self):
        return f"<Car {self.car_id}>"

    def __init__(self, car_id, color, model, owner_id):
        self.car_id = car_id
        self.color = color
        self.model = model
        self.owner_id = owner_id

    def json(self):
        return {
            "car_id": self.car_id,
            "color": self.color.name,
            "model": self.model.name,
            "owner_id": self.owner_id,
        }

    @classmethod
    def find_car(cls, car_id):
        car = cls.query.filter_by(car_id=car_id).first()
        if car:
            return car
        return None

    def save_car(self):
        db.session.add(self)
        db.session.commit()
