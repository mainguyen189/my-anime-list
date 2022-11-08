from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*":{'origin': "*"}})

@app.route('/', methods=["GET"])
def hello():
    return "To my anime list"

@app.route('/miaow', methods=["GET"])
def miaow():
    return "You found cat not anime"


if __name__ == "__main__":
    app.run(debug=True)
