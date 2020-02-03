import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.warning('Hello World')
    return 'Hello World'


if __name__ == '__main__':
    handler = RotatingFileHandler('/logs/app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host="0.0.0.0", port=8000)
