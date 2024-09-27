import time

from app import app, db, api
from app.cars.resources import Cars
from app.owners.resources import Owners


def create_tables():
    with app.app_context():
        for _ in range(50):
            try:
                db.create_all()
                return
            except Exception:
                print("Database is not ready yet. Waiting...")
                time.sleep(10)
        print("Failed to create tables after 5 attempts.")


def run():
    create_tables()
    app.run(host="0.0.0.0", port=8000, debug=True)


api.add_resource(Cars, "/cars")
api.add_resource(Owners, "/owners")


if __name__ == "__main__":
    run()
