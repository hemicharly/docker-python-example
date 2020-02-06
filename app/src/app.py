import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import names


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URL_CONNECT"]
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name})

@app.route('/user/create')
def create_user():
    db.session.add(User(name=names.get_full_name()))
    db.session.commit()
    return "User created"

@app.route('/user/list')
def list_user():
    users = User.query.all()
    return str(users)

if __name__ == '__main__':
    db.create_all()  # Cria tabela caso não existir
    handler = RotatingFileHandler('/logs/app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host="0.0.0.0")
