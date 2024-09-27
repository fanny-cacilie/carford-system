from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://user:password@database:5432/postgres"
)

db.init_app(app)

api = Api(app)
