import flask
from flask import request
import numpy as np

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    z = np.random.randn()
    return f'Ausgabe: {z}'


if __name__ == '__main__':
    app.run()
