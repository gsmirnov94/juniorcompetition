from flask import Flask
from pymongo import MongoClient
from config import Config
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
mongo = MongoClient('localhost', 27017)
csrf = CSRFProtect(app)

from app import routes