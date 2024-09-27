import pytest

from app import app, db
from app.models import CarModel, ColorEnum, ModelEnum


@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://user:password@database:5432/postgres_test"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def test_car_model_creation(test_client):
    car = CarModel(car_id=1, color=ColorEnum.yellow, model=ModelEnum.sedan, owner_id=1)
    car.save_car()
    fetched_car = CarModel.find_car(1)
    assert fetched_car is not None
    assert fetched_car.color == ColorEnum.yellow
    assert fetched_car.model == ModelEnum.sedan
    assert fetched_car.owner_id == 1


def test_car_model_json(test_client):
    car = CarModel(
        car_id=2, color=ColorEnum.blue, model=ModelEnum.convertible, owner_id=2
    )
    car.save_car()

    expected_json = {
        "car_id": 2,
        "color": "blue",
        "model": "convertible",
        "owner_id": 2,
    }
    assert car.json() == expected_json


def test_find_nonexistent_car(test_client):
    assert CarModel.find_car(999) is None
