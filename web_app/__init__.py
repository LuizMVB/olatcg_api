from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Falsk's gateway
app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Database
db = SQLAlchemy(app)