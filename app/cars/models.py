from app import db
from app.owners.models import OwnerModel

class CarModel(db.Model):
    __tablename__ = 'cars'

    car_id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(15), nullable=False) # Enum
    model = db.Column(db.String(15), nullable=False) # Enum
    owner_car_id = db.Column(db.Integer) # db.Column(db.Integer, db.ForeignKey(OwnerModel.car_id))


    def __repr__(self):
        return f'<Car {self.car_id}>'


    def __init__(self, car_id, color, model, owner_car_id):
        self.car_id = car_id
        self.color = color
        self.model = model
        self.owner_car_id = owner_car_id

    def json(self):
        return {
            "car_id": self.car_id,
            "color": self.color,
            "model": self.model,
            "owner_car_id": self.owner_car_id,
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
    