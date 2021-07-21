import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-life'
    MONGO_URI = "mongodb://localhost:270717/viruses"