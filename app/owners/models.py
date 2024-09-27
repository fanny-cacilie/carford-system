from app import db
from app.cars.models import CarModel

class OwnerModel(db.Model):
    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, primary_key=True, nullable=False)
    sale_opportunity = db.Column(db.Boolean, nullable=False, default=True)
    cars = db.relationship('CarModel', backref='owner', lazy='select')


    def __repr__(self):
        return f'<Owner {self.owner_id}>'

    
    def __init__(self, owner_id, sale_opportunity):
        self.owner_id = owner_id
        self.sale_opportunity = sale_opportunity


    def json(self):
        return {
            "owner_id": self.owner_id,
            "sale_opportunity": self.sale_opportunity,
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
    
    