from app import db

class OwnerModel(db.Model):
    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, primary_key=True, nullable=False)
    car_quantity = db.Column(db.Integer, nullable=False)
    sale_opportunity = db.Column(db.Boolean, nullable=False, default=True)
    cars = db.Column(db.Integer, nullable=False) # db.relationship('CarModel', backref='OwnerModel')

    def __repr__(self):
        return f'<Owner {self.owner_id}>'

    
    def __init__(self, owner_id, car_quantity, sale_opportunity, cars):
        self.owner_id = owner_id
        self.car_quantity = car_quantity
        self.sale_opportunity = sale_opportunity
        self.cars = cars


    def json(self):
        return {
            "owner_id": self.owner_id,
            "car_quantity": self.car_quantity,
            "sale_opportunity": self.sale_opportunity,
            "cars": self.cars,
        }


    @classmethod
    def find_owner(cls, owner_id):
        owner = cls.query.filter_by(owner_id=owner_id).first()
        if owner:
            return owner
        return None


    def save_owner(self):
        db.session.add(self)
        db.session.commit()
    
    